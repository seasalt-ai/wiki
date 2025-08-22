#!/usr/bin/env python3
"""
Wiki Content Combiner with Proper Hugo Ordering

This script reads all Markdown files from a specified folder (like content/en/seachat)
and combines them into a single Markdown file while properly respecting Hugo's weight-based
ordering system globally, not just within directories.
"""

import os
import sys
from pathlib import Path
import yaml
from typing import Dict, List, Tuple, Optional
import re


def extract_frontmatter_and_content(file_path: str) -> Tuple[Optional[Dict], str]:
    """
    Extract YAML frontmatter and content from a Markdown file.
    
    Returns:
        Tuple of (frontmatter_dict, content_string)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file starts with frontmatter
        if content.startswith('---\n'):
            # Find the end of frontmatter
            parts = content.split('---\n', 2)
            if len(parts) >= 3:
                frontmatter_text = parts[1]
                content_text = parts[2]
                try:
                    frontmatter = yaml.safe_load(frontmatter_text)
                    return frontmatter, content_text
                except yaml.YAMLError:
                    # If YAML parsing fails, treat entire content as content
                    return None, content
            else:
                return None, content
        else:
            return None, content
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None, ""


def get_hugo_sort_key(file_path: str, frontmatter: Optional[Dict]) -> Tuple[int, int, int, str]:
    """
    Generate a sort key for Hugo-style ordering.
    
    Returns:
        Tuple of (weight, depth, filename_number, filename) for sorting
    """
    path = Path(file_path)
    filename = path.stem
    
    # Calculate depth (number of directory levels)
    depth = len(path.parts) - 1
    
    # Get weight from frontmatter (default to 999 if not specified)
    weight = 999
    if frontmatter and 'weight' in frontmatter:
        try:
            weight = int(frontmatter['weight'])
        except (ValueError, TypeError):
            weight = 999
    
    # Extract number prefix from filename (e.g., "01-intro" -> 1)
    filename_number = 999
    match = re.match(r'^(\d+)-', filename)
    if match:
        filename_number = int(match.group(1))
    
    # Index files should come first within their weight group
    if filename == '_index':
        filename_number = -1
    
    return (weight, depth, filename_number, filename)


def get_file_hierarchy_hugo_ordered(root_path: str) -> List[Tuple[str, int]]:
    """
    Get all .md files in the directory tree with their relative paths and depth levels,
    ordered according to Hugo conventions (weight-based globally).
    
    Returns:
        List of tuples (file_path, depth_level) in proper Hugo order
    """
    root = Path(root_path)
    if not root.exists():
        raise FileNotFoundError(f"Directory {root_path} does not exist")
    
    # Collect all files with their metadata
    all_files = []
    for file_path in root.rglob("*.md"):
        relative_path = file_path.relative_to(root)
        depth = len(relative_path.parts) - 1
        
        # Extract frontmatter to get weight
        frontmatter, _ = extract_frontmatter_and_content(str(file_path))
        
        # Create sort key
        sort_key = get_hugo_sort_key(str(file_path), frontmatter)
        
        all_files.append((str(file_path), depth, sort_key, frontmatter))
    
    # Sort all files globally by Hugo rules
    # Primary sort: weight (ascending)
    # Secondary sort: depth (ascending - shallower files first)
    # Tertiary sort: filename number (ascending)
    # Quaternary sort: filename (alphabetical)
    all_files.sort(key=lambda x: x[2])
    
    # Return just the file path and depth
    return [(file_path, depth) for file_path, depth, sort_key, frontmatter in all_files]


def generate_heading_from_path(file_path: str, root_path: str, frontmatter: Optional[Dict]) -> str:
    """
    Generate a heading for the file based on its path and frontmatter.
    """
    relative_path = Path(file_path).relative_to(Path(root_path))
    
    # Use title from frontmatter if available
    if frontmatter and 'title' in frontmatter:
        title = frontmatter['title']
    else:
        # Generate title from filename
        filename = relative_path.stem
        if filename == '_index':
            # For _index files, use the parent directory name
            title = relative_path.parent.name.replace('-', ' ').replace('_', ' ').title()
        else:
            # Remove number prefixes and convert to title case
            title = re.sub(r'^\d+-', '', filename).replace('-', ' ').replace('_', ' ').title()
    
    return title


def calculate_heading_level(depth: int, is_index_file: bool) -> int:
    """
    Calculate the appropriate heading level based on file depth and type.
    """
    if is_index_file:
        # Index files get heading level based on their directory depth
        return min(depth + 1, 6)  # Max heading level is 6
    else:
        # Regular files get one level deeper than their directory
        return min(depth + 2, 6)  # Max heading level is 6


def combine_wiki_content(root_path: str, output_file: str) -> None:
    """
    Combine all Markdown files from the root_path into a single output file,
    respecting Hugo ordering conventions (weight-based globally).
    """
    print(f"Processing directory: {root_path}")
    
    # Get all markdown files with their hierarchy in proper Hugo order
    files = get_file_hierarchy_hugo_ordered(root_path)
    
    if not files:
        print(f"No Markdown files found in {root_path}")
        return
    
    print(f"Found {len(files)} Markdown files")
    
    # Start building the combined content
    combined_content = []
    
    # Add main title
    root_name = Path(root_path).name.replace('-', ' ').replace('_', ' ').title()
    combined_content.append(f"# {root_name} Documentation\n")
    combined_content.append(f"*Combined documentation from {root_path} (Hugo weight-ordered)*\n")
    combined_content.append("---\n")
    
    for file_path, depth in files:
        print(f"Processing: {file_path} (depth: {depth})")
        
        # Extract frontmatter and content
        frontmatter, content = extract_frontmatter_and_content(file_path)
        
        # Skip empty files
        if not content.strip():
            continue
        
        # Determine if this is an index file
        is_index_file = Path(file_path).stem == '_index'
        
        # Generate heading
        title = generate_heading_from_path(file_path, root_path, frontmatter)
        heading_level = calculate_heading_level(depth, is_index_file)
        heading_prefix = '#' * heading_level
        
        # Add file section
        combined_content.append(f"\n{heading_prefix} {title}\n")
        
        # Add file path as comment for reference
        relative_path = Path(file_path).relative_to(Path(root_path))
        combined_content.append(f"<!-- Source: {relative_path} -->\n")
        
        # Add weight and ordering info as comment
        if frontmatter and 'weight' in frontmatter:
            combined_content.append(f"<!-- Weight: {frontmatter['weight']} -->\n")
        else:
            combined_content.append(f"<!-- Weight: 999 (default) -->\n")
        
        # Add description from frontmatter if available
        if frontmatter and 'description' in frontmatter and frontmatter['description']:
            combined_content.append(f"*{frontmatter['description']}*\n")
        
        # Add the content
        combined_content.append(content)
        
        # Add separator
        combined_content.append("\n---\n")
    
    # Write combined content to output file
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined_content))
    
    print(f"Combined documentation written to: {output_file}")
    print(f"Total sections: {len(files)}")


def main():
    """Main function to handle command line arguments and run the combiner."""
    if len(sys.argv) < 2:
        print("Usage: python wiki_combiner_hugo_fixed.py <input_folder> [output_file]")
        print("Example: python wiki_combiner_hugo_fixed.py content/en/seachat seachat_combined.md")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    
    # Generate default output filename if not provided
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        folder_name = Path(input_folder).name
        output_file = f"{folder_name}_weight_ordered.md"
    
    try:
        combine_wiki_content(input_folder, output_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()