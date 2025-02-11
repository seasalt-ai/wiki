---
title: "Enabling References in Chat"
description: "The Knowledge Base References feature in SeaChat by Seasalt.ai provides a convenient way to link back to documents used to generate chat responses. When enabled, each chat response will include a References section that lists the source documents, allowing users to see exactly what information contributed to the response."
lead: ""
date: 2025-02-11T08:48:45+00:00
lastmod: 2025-02-11T08:48:45+00:00
weight: 109
draft: false
images: []
toc: true
aliases:
  - /en/seachat/seachat-manual/02-create-agent/03-advanced-settings/05-kb-references
  - /en/seachat/manual/create-agent/advanced-settings/kb-references/
url: /en/seachat/manual/create-agent/advanced-settings/kb-references/
---

#### Overview

The Knowledge Base References feature in SeaChat by Seasalt.ai provides a convenient way to link back to documents used to generate chat responses. When enabled, each chat response will include a References section that lists the source documents, allowing users to see exactly what information contributed to the response.

#### How to Enable Knowledge Base References

To enable this feature, follow these steps:

1. **Go to the Agent Information \-\> Advanced Settings** tab
2. **Toggle Knowledge Base References**
   - Find the Knowledge Base References setting and switch it on to activate the feature.

<center>
<a href="/images/seachat/en/kb-references/image01.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image01.png"  alt="KB References Section in the Advanced Settings Page">
</a>
<br/>

</center>

Once enabled, the References section appears under the AI Agent’s responses, displaying the names of the Knowledge Base documents that SeaChat used to generate the answer. If the source is a clickable URL, it will be displayed as a link for easy access. This allows users to verify the sources and gain a better understanding of how responses are formed.

#### What Kind of Knowledge Base Entries Show as References?

The types of Knowledge Base entries that can appear as references include:

#### **1\. URL-Based Entries**

Web pages or publicly accessible articles added to the KB. When the chatbot retrieves information from a URL, the reference appears as a clickable link.

<center>
<a href="/images/seachat/en/kb-references/image02.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image02.png"  alt="AI agent response displays two clickable urls">
</a>
<br/>

_Example: AI agent response displays two clickable urls._

</center>

#### **2\. Manual Knowledge Base Entries**

Custom text-based knowledge entries manually added. These are typically short documents or FAQs written in SeaChat’s _Write a New KB Document_ page. The reference will display the title of the manual KB entry.

<center>
<a href="/images/seachat/en/kb-references/image03.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image03.png"  alt="A Manual KB entry">
</a>
<br/>
</center>
<br/>
<center>
<a href="/images/seachat/en/kb-references/image04.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image04.png"  alt="AI agent response displays a citation from the Manual KB entry">
</a>
<br/>

_Example: AI agent response displays a citation from the Manual KB entry: The Basics of Renewable Energy._

</center>

#### **3\. Uploaded Files**

Various document types that users upload to the Knowledge Base. When an uploaded document contributes to a response, the filename will appear in the References section. Supported file formats include:

- Excel Files (.csv, .xls, .xlsx, .xlsm, .xlsb, .odf, .ods and .odt)

- Documents (.doc, .docx, .eml, .epub, .gif, .jpg, .json, .html, .msg, .odt, .ogg, .pdf, .png, .pptx, .ps, .rtf, .tiff, .txt, .zip)

<center>
<a href="/images/seachat/en/kb-references/image05.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image05.png"  alt="A document">
</a>
<br/>
</center>
<br/>
<center>
<a href="/images/seachat/en/kb-references/image06.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image06.png"  alt="AI agent response displays a citation from the document">
</a>
<br/>

_Example: AI agent response displays a citation from the document: artificial_intelligence-docx._

</center>

<center>
<a href="/images/seachat/en/kb-references/image07.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image07.png"  alt="An Excel file">
</a>
<br/>
</center>
<br/>
<center>
<a href="/images/seachat/en/kb-references/image08.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image08.png"  alt="AI agent response displays a citation from a worksheet: renewable_energy-xlsx">
</a>
<br/>

_Example: AI agent response displays a citation from a worksheet: renewable_energy-xlsx._

</center>

#### Use Cases

Here are some scenarios where **Knowledge Base References** can be particularly valuable:

- **Customer Support & Helpdesk**
  - Human agents can quickly verify that chatbot responses align with official documentation.
  - Customers can see where information is sourced, ensuring transparency and trust.
- **Internal Knowledge Sharing**
  - Employees using SeaChat to find company policies or technical guidelines can check references for accuracy.
  - Training new team members becomes easier as they can trace back responses to internal knowledge base articles.
- **Education & Research**
  - Students and researchers can use SeaChat for academic inquiries while verifying the credibility of the sources used.
  - Teachers can guide students by pointing them to specific referenced materials.

By enabling Knowledge Base References, users gain better transparency, increased trust in AI responses, and more control over chatbot-generated content. 🚀
