---
title: "上傳試算表"
description: "SeaChat 試算表上傳"
lead: ""
date: 2024-03-11 10:43:51.069 +0100
lastmod: 2024-04-19 10:43:51.069 +0100
weight: 31
draft: false
images: []
aliases:
  - /zh/seachat/seachat-manual/03-add-knowledge/add-knowledge-intro
---

## 簡介
SeaChat 提供多種方法來上傳文件到您的AI助理知識庫。在本教學中，我們將專注於**上傳試算表**的方法，在本教學結束時，您的 SeaChat 助理將擁有一個客製的知識庫為您服務。

## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](/zh/seachat/seachat-manual/01-create-agent/) 找到創建AI助理的步驟。


## 開啟知識庫
在側邊欄中，選擇**AI助理配置**下的**知識庫**。選擇**上傳試算表**，您就可以上傳 .csv 或 .xlsx 等電子試算表文件到您的AI助理知識庫。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/product-updates/seachat/zh/tutorial-add-knowledge/05-document-upload/20240313-spreadsheet-tutorial-step2.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step2.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a CSV or JSON file to an agent by selecting Upload from Template File.">
</a>

*知識庫面板*
</center>

## 上傳檔案
點擊**上傳您的試算表**的區塊，您就可以從多種文件格式[^1]中選擇想要提交給AI助理的文件。送出後，知識庫會處理送出的文件並更新。
[^1]: SeaChat 支援 .csv, .xls, .xlsx, .xlsm, .xlsb, .odf, .ods 和 .odt 等文件。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/product-updates/seachat/zh/tutorial-add-knowledge/05-document-upload/20240313-spreadsheet-tutorial-step3.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step3.jpg" alt="Screenshot illustrating the navigation through the dashboard of knowledge base for SeaChat's AI agents. It illustrates the user interface">
</a>

*上傳檔案*
</center>

> :rotating_light: **注意事項** :rotating_light:
>
> 上傳文件前，請檢查文件是否符合以下兩個要求：
> - 表格必須在第一行有標題。
> - 單一行的內容不得超過 2000 個tokens。
> 參考**表格上傳準則**以獲取更多信息。

## 送出文件前
SeaChat允許用戶批量上傳。您可以在拖放區域下方的部分查看每個上傳檔案的狀態。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/product-updates/seachat/zh/tutorial-add-knowledge/05-document-upload/20240313-spreadsheet-tutorial-step4.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step4.jpg" alt="Interface of SeaChat showing the bulk upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded and a preview section for the spreadsheet data, reminding users to verify file format and content before submission.">
</a>

*已上傳檔案預覽*
</center>

向下滾動以查看專用的預覽窗口，該窗口將列出您的試算表格的前10行。一旦確認所有要上傳的檔案無誤，您可以點擊**繼續**按鈕進行上傳。

###### 預覽範例:
<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step4-table-example.jpg" alt="An example of table preview">
</center>

## 已添加到知識庫

您已成功上傳新知識。要查看已上傳的檔案，您可以至頁面右上角的「**現有知識**」區塊，在那裡您可以在「**上傳檔案**」裡找到剛剛上傳的資料。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/product-updates/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step5.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step5.jpg" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Next' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*在 **現有知識** 中查找文件*
</center>

## 檢查知識庫

點擊您剛剛上傳的檔案並檢視內容。大功告成！您已成功地將一份試算表格上傳到您的SeaChat助理中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/product-updates/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step6.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step6.jpg" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Next' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*審核上傳的試算表*
</center>

## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。

 