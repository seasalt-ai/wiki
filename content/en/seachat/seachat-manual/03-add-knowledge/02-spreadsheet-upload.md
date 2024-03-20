---
title: "Spreadsheet Upload"
description: "SeaChat SpreadSheet Upload"
lead: ""
date: 2024-03-04 10:43:51.069 +0100
lastmod: 2024-03-04 10:43:51.069 +0100
weight: 31
draft: false
images: []
aliases:
  - /en/seachat/seachat-intro/03-add-knowledge/add-knowledge-intro
---

## Overview````
SeaChat provides many methods to upload files to your agent. We will focus on the **Upload Spreadsheet** method in this tutorial and by the end of the tutorial your SeaChat agent will have a customized knowledge base at your service.


## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based AI agent in [Create an Agent](/en/seachat/seachat-intro/02-how-to-create/).


## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. By choosing **Upload Spreadsheet**, you can upload a .csv or .xlsx file to your agent.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step2.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a CSV or JSON file to an agent by selecting Upload from Template File.">

## Upload File
By clicking on the upload button, you can submit to your agent choosing from various file formats[^1]. The file will be processed and the knowledge base will be updated accordingly once submitted.
[^1]: SeaChat supports .csv, .xls, .xlsx, .xlsm, .xlsb, .odf, .ods and .odt files.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step3.png" alt="Screenshot illustrating the navigation through the dashboard of knowledge base for SeaChat's AI agents. It illustrates the user interface">
<br/>
<br/>
<br/>

> :rotating_light: **Note** :rotating_light:
> 
> Before uploading the file, check if the files meet the two following requirements:
> - Your spreadsheet table must use the first row as the header. If your header is the first column, please [transpose your table](https://support.microsoft.com/en-us/office/transpose-rotate-data-from-rows-to-columns-or-vice-versa-3419f2e3-beab-4318-aae5-d0f862209744) first.
> - The content in any row may not exceed 2000 tokens. If your row exceeds this limit, please contact us!
> 
> Check **Upload Guidelines** for more information.

## Before Submission
SeaChat allows users to upload in bulk. You can see the status of each uploading file in the section below the drag-and-drop zone.
You can upload as many spreadsheet files as you wish and each file can have more than just one worksheet. 
<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step4.png" alt="Interface of SeaChat showing the bulk upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded and a preview section for the spreadsheet data, reminding users to verify file format and content before submission.">
<br/>
<br/>

Scroll further down for the dedicated preview window that will list the first 10 rows of your spreadsheet. Once you have included all the files to be uploaded, you can upload them by clicking on the **Next** button.

###### Preview Example:
<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step4-table-example.png" alt="An example of table preview">


## Submit to Existing Knowledge Base
Voilà! You have successfully customized your SeaChat agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the **Files** section.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step5.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Next' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">


## Review your Knowledge Base
Click on the file you just uploaded to review the content. That's it! You have successfully uploaded a spreadsheet to your SeaChat agent. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the **Advance** section of the tutorial.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step6.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Next' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">


## :brain: Under the Hood

Why does SeaChat single out spreadsheet/table uploads? Because we believe spreadsheet/table are the most common way that any users organize their knowledge base. Yet special attention needs to be paid to optimize a Large Language Model's (e.g. ChatGPT) ability to understand tables:

1. We sacrifice space in exchange for understanding accuracy. In each data row, the actual values are prefixed with their header fields. So when a table becomes too big, the LLM/ChatGPT does not lose context.
2. Because of the limited context length of LLMs, we limit each row to be more than 2,000 tokens.



## Support
Need assistance? Contact us at [seachat@seaslt.ai](mailto:seachat@seaslt.ai).

 