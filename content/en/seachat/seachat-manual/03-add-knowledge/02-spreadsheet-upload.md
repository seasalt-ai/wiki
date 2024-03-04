---
title: "Spreadsheet Upload"
description: "SeaChat SpreadSheet Upload"
lead: ""
date: 2024-03-04 10:43:51.069 +0100
lastmod: 2024-03-04 10:43:51.069 +0100
weight: 32
draft: false
images: []
aliases:
  - /en/seachat/seachat-intro/03-add-knowledge/add-knowledge-intro
---

## Overview
SeaChat provides two methods to upload files to your agent. The first method is dedicated to CSV, JSON, or Excel files, and the second provides upload support for more than 20 types of file formats. We will focus on the first method in this tutorial.

## Step 0: Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based chatbot in [Create an Agent](/en/seachat/seachat-intro/02-how-to-create/).

## Step 1: Open Knowledge Base
Find your agent's knowledge base by navigating to the "Knowledge Base" dashboard under "Agent Configuration" in the sidebar menu. By choosing "Upload from Template File", you can upload a CSV or JSON file to your agent.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240304-spreadsheet-tutorial-step1.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a CSV or JSON file to an agent by selecting Upload from Template File.">

## Step 2: Upload File
By clicking on the upload button, you can submit CSV, JSON, or Excel files to your agent. The file will be processed and the knowledge base will be updated accordingly once submitted. 

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240304-spreadsheet-tutorial-step2.png" alt="Screenshot illustrating the navigation through SeaChat's knowledge dashboard. It indicates where the buttons of 'Download CSV Template', 'Download JSON Template' and image-upload are">
<br/>
<br/>

SeaChat also provides sample files for you to download and use as a template. By clicking on "Download CSV Template" or "Download JSON Template", you can download the sample files to your local device. You can then fill in the template with your own data and upload it to your agent.

JSON File Example:
```json
 {"id": "kb-1", "title": "Sample KB Doc", "text": "This is an example of a KB document.", "custom": {"sample_key": "sample value"}, "actions": {"references": [{"title": "Seasalt.ai", "url": "https://seasalt.ai"}, {"title": "SeaChat", "url": "https://chat.seasalt.ai/"}], "reminder": "This is some reminder text!", "capture": ["Email", "Phone Number"], "live_agent_transfer": false}}
```

CSV File Example:

| id  | title         | text                            | references            | reminder               | capture          | transfer | key         |
|-----|---------------|---------------------------------|-----------------------|------------------------|------------------|----------|-------------|
| kb-1| Sample KB Doc | This is an example of a KB doc. | **References Example* | This is reminder text! | Email, Phone No. | No       | sample value |
###### **References Example*: 
```json
 [{"title":"Seasalt.ai","url":"https://seasalt.ai"}, {"title":"SeaChat","url":"https://chat.seasalt.ai"}]
```

## Step 3: Before Submission
SeaChat allows users to upload in bulk. You can see the status of each uploading file in the section below the drag-and-drop zone. Make Sure to check the file format and the content before submission.

<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240304-spreadsheet-tutorial-step3.png" alt="Interface of SeaChat showing the bulk upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded, reminding users to verify file format and content before submission.">


## Step 4: Submit to Existing Knowledge Base
Once you are sure of the files included, you can submit the file to upload by clicking on the "Submit" button. Voilà! You have successfully customized your agent with new knowledge. To view the files uploaded, you can navigate to the "Existing" section in the top-right corner of the page, where you can find the uploaded data in the "Files" section.
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/spreadsheet/20240304-spreadsheet-tutorial-step4.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Submit' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">


### Support
Need assistance? Contact us at [seachat@seaslt.ai](mailto:seachat@seaslt.ai).

 