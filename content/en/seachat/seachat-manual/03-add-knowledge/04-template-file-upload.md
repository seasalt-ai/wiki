---
title: "Template Upload"
description: "Enhance your SeaChat agent's capabilities with our easy-to-follow tutorial on uploading spreadsheets to customize your knowledge base[^1^][1]. Sign up for free and navigate to the Knowledge Base dashboard to upload your data using our provided templates. Successfully manage your AI agent's knowledge with SeaChat's user-friendly platform. Need help? Reach out at seachat@seaslt.ai."
lead: ""
date: 2024-04-11 10:43:51.069 +0100
lastmod: 2024-04-11 10:43:51.069 +0100
weight: 33
draft: false
images: []
aliases:
  - /en/seachat/seachat-intro/03-add-knowledge/04-template-file-upload/
---
> 🧭 **File Size Rule**
>
> Your file size limit for each uploaded document varies depending on your subscription plan. If you exceed the file upload limitation, you will receive an error message. Please reduce the size of your file before uploading again. Please refer to the [File Size Rule](https://wiki.seasalt.ai/seachat/seachat-manual/03-add-knowledge/file-size-rule/) for more information.


## Overview
SeaChat provides several methods to upload files to your agent. We will focus on the **Upload Spreadsheet** method in this tutorial and by the end of the tutorial your SeaChat agent will have a customized knowledge base at your service.


## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based AI in [Create an Agent](/en/seachat/seachat-intro/02-how-to-create/).


## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. Click on **Upload from Template File**. SeaChat provides template files that can you can directly input.

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/knowledge-base.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a CSV or JSON file to an agent by selecting Upload from Template File.">

*Knowledge Base Dashboard*
</center>

## Template Files
SeaChat offers CSV and JSON template files that you can download and fill in with your data. Once you have filled in the template files, you can upload it to your agent by clicking on the drag-and-drop section.

###### Preview Example:
```CSV```

<div style="overflow-x: auto;">
<table>
<tr>
  <th>id</th>
  <th>title</th>
  <th>text</th>
  <th>references</th>
  <th>reminder</th>
  <th>capture</th>
  <th>live_agent_transfer</th>
  <th>sample_key</th>
</tr>
<tr>
  <td>kb-1</td>
  <td>Sample KB Doc</td>
  <td>This is an example of a KB document.</td>
  <td>[{"title":"Seasalt.ai","url":"https://seasalt.ai"}]</td>
  <td>This is some reminder text!</td>
  <td>Email,Phone Number</td>
  <td>False</td>
  <td>sample value</td>
</tr>
</table>
</div>


```JSON```
```json
[{
  "id": "kb-1",
  "title": "Sample KB Doc",
  "text": "This is an example of a KB document.",
  "custom": {"sample_key": "sample value"},
  "actions": {
    "references": [
      {"title": "Seasalt.ai", "url": "https://seasalt.ai"},
      {"title": "SeaChat", "url": "https://chat.seasalt.ai/"}
    ],
    "reminder": "This is some reminder text!",
    "capture": ["Email", "Phone Number"],
    "live_agent_transfer": false
  }
}]
```

1. **id**: Unique identifier for the document.
2. **title**: Title of the document.
3. **text**: Content of the document that the AI agent will interpret.
4. **custom**: Additional information that the AI agent can refer to. For example, when you need to refine a knowledge base response, you can add a custom key-value pair to the document for the AI agent to refer to.
4. **references**: Additional information or links that the AI agent can provide. Where **title** is the name of the reference that will render in the UI and **url** is the link.
5. **reminder**: Additional information that the AI agent will provide in the formatted reminder banner.
6. **capture**: Information that the AI agent will capture from the user. For example, when this specific knowledge is used. Agent will ask users for the inputs in capture field.
7. **live_agent_transfer**: Boolean value to enable or disable live agent transfer.

## Before Submission
You will see the status of each uploading file in the section below the drag-and-drop zone. Once you are sure with the uploaded files, you can upload them by clicking on the **Submit** button.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/template-upload/before-submission.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/before-submission.png" alt="Interface of SeaChat showing the upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded, reminding users to verify file format and content before submission.">
</a>

*Check the Uploaded Files*
</center>


## Submit to Existing Knowledge Base
Submit it and it's done. You have successfully customized your AI agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the "Files" section.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/template-upload/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/existing-files.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Look for Files in **Existing***
</center>

## Review your Knowledge Base
Click on the file you just uploaded to review the content. That's it! You have successfully uploaded a spreadsheet to your SeaChat agent. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the next part of the tutorial.

<div style="display: flex; justify-content: space-between; align-items: center;">
  <div style="display: flex; flex-direction: column; text-align: center;">
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/template-upload/csv-uploaded.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/csv-uploaded.png" alt="Example of a successfully uploaded csv.">
</a>
    <em>CSV File</em>
  </div>

  <div style="display: flex; flex-direction: column; text-align: center;">
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/template-upload/json-uploaded.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/json-uploaded.png" alt="Example of a successfully uploaded json.">
</a>
    <em>JSON File</em>
  </div>
</div>



## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 