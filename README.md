# Intro
This repo serves [wiki.seasalt.ai](https://wiki.seasalt.ai). Wiki is product documentation/user manual for non-technical Seasalt.ai customers. 

## How to Develop?

### Doks
To get started with development, follow [Doks](https://getdoks.org/tutorial/introduction/). To modify and extend components of Doks, go to [detailed documentation](https://getdoks.org/docs/prologue/introduction/).

### Hugo

### Article Format

`---` can be replaced to `+++` or `{}`

```
---
title: "Introduction"
description: "Discover how SeaChat empowers you to build and launch AI agents in under 10 minutes. With support for 30+ document types and seamless integrations, including web chat, SMS, CRM, and more, SeaChat offers multilingual capabilities and a code-free experience. Learn to create your first agent with our comprehensive tutorial"
date: 2024-03-08 10:43:51.069 +0100
lastmod: 2024-03-08 10:43:51.069 +0100
weight: 201
draft: false
images: []
aliases:
  - /en/seachat/seachat-intro/01-introduction/
  - /seachat/seachat-intro/01-seachat-intro/
---

This is simple page content...

```

Default attributes:

- title - the title for the content.
- date - the datetime assigned to this page
- draft - if true, the content will not be rendered

Other attributes:
- lastmod - By default, the lastmod will be updated to git commit time. If you want to manually set the lastmod, you can still do so in the front matter of the page, but the value will be overwritten by the git commit time. Check [here](https://www.andrewjstevens.com/posts/2021/03/last-modified-date-with-hugo/) for more details.
- description - the description for the content, for SEO purpose.
- aliases - the path to the content from the web root.
- weight - used for ordering your content in lists. Lower weight gets higher precedence. So content with lower weight will come first. If set, weights should be non-zero, as 0 is interpreted as an unset weight.

### Develop Locally

1. Run `npm install` to install all required npm packages. 
2. Run `npm run start`. Doks will start the Hugo development webserver accessible by default at http://localhost:1313. Saved changes will live reload in the browser.

To preview the static files that will be generated, run `hugo` and check `/public`. Open `/public/index.html` to see result.

## Pagefind

This repo uses [Pagefind](https://pagefind.app/) to enable the searching feature. Pagefind is a search engine for static sites. It indexes your site and provides a search bar to search through your content.

### How to Update Pagefind Index?
Pagefind uses indices to search for content. To update the index, run `npm run pagefind` to generate the `pagefind.json` file. This command will index the content in the `content` directory and generate the `pagefind.json` file in the `data` directory.

1. Build the Hugo project

```bash
hugo
```

2. Generate the indexing files

```bash
npx pagefind --site ./public # this will generate the indexing files in the public directory
```

3. Run project server

```bash
hugo server
```

*Note: Every time the content is updated, the indexing files should be regenerated.*

### Deployment
To deploy your changes, make a PR to merge changes to `main` branch as usual. When your code is merged to `main` branch, Github Actions for deployment (see `.github/workflows/deploy-github.yml`) will be triggered to rebuild and publish static files to `gh-pages` branch. The webpage, [wiki.seasalt.ai](https://wiki.seasalt.ai), serves the static files that are pushed to `gh-pages` directly.