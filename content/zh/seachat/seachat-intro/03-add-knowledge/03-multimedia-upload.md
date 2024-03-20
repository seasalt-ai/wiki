---
title: "多媒體知識庫"
description: "如何用 Seasalt.ai 的 SeaChat 轉錄多媒體檔到知識庫中"
lead: ""
date: 2024-03-04 10:43:51.069 +0100
lastmod: 2024-03-04 10:43:51.069 +0100
weight: 32
draft: false
images: []
aliases:
  - /en/seachat/seachat-intro/03-add-knowledge/add-knowledge-intro
---

## 簡介
您也可以加入多媒體檔到您SeaChat助理的知識庫中！我們大多時候可以先將這些文件轉錄為文本，然後上傳到 AI 助理平台。SeaChat替您省去了轉錄步驟，並直接接受多媒體檔案！

SeaChat 提供許多不同文件上傳到您助理的方式。在本教學中，我們將專注於**轉錄音訊/影訊**的方法，在本教學結束時，您的 SeaChat 助理將擁有一個客製的知識庫為您服務。

## 為什麼需要轉錄多媒體檔案?
與其他轉錄服務相比，音頻/視頻文件的上傳似乎非常有限。為什麼我們還要將它獨立成一個功能？因為SeaChat支持從WhatsApp和Facebook Messenger的音頻輸入，而您的聊天助理能夠理解這些語音輸入。然後我們使用相同的管道來接受音頻/視頻的上傳！
每個WhatsApp和Messenger的音頻訊息通常包含一個發言者，且小於1分鐘。多媒體上傳功能是這個功能的延伸。

> :exclamation:**重要提醒**:exclamation:
>
> 請注意，您的多媒體檔案需符合以下假設：
> 1. 語言是英文或中文
> 2. 檔案中只有一位發言者
> 3. 總長度少於15分鐘


## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](/zh/seachat/seachat-intro/02-create-agent/) 找到所有你需要的資訊。

## 開起知識庫
在側邊欄中，選擇**AI助理配置**下的**知識庫**。選擇**轉錄音訊/影訊**，您就可以上傳音訊或影訊檔案到您的AI助理。
<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step2.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a CSV or JSON file to an agent by selecting Upload from Template File.">

## 上傳檔案
點擊檔案上傳的區塊，您就可以從多種文件格式[^1]中選擇想要提交給AI助理的文件。送出後，知識庫會處理送出的文件並更新。
[^1]: SeaChat 支援 .wav, .flac, .aac, .opus, .mp3, .mp4, .ogg, .m4a 等檔案.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step3.png" alt="Screenshot illustrating the navigation through the dashboard of knowledge base for SeaChat's AI agents. It illustrates the user interface">
<br/>
<br/>
<br/>

> :rotating_light: **提醒** :rotating_light:
>
> 上傳文件前，請檢查文件是否符合以下兩個要求:
> - 媒體內容必須是英文或中文。
> - 文件的時長不得超過15分鐘。
## 檢查語言

請確認已選擇的多媒體檔案是否正確。目前SeaChat支持英文和繁體中文。一旦您確認了所有上傳的文件，您可以點擊提交按鈕進行上傳。

請注意，英文/中文支持僅意味著您上傳的音頻/視頻文件會被轉錄成相應的語言。SeaChat後端是由一個大型語言模型(LLM)所驅動的，也是多語言的。這代表的用戶可以用完全不同的語言與SeaChat進行對話。

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step4.png" alt="Interface of SeaChat showing the bulk upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded and a preview section for the spreadsheet data, reminding users to verify file format and content before submission.">
<br/>
<br/>


## 送出至現有知識庫
你看! 您已成功地將新知識自訂到您的聊天機器人代理中。要查看已上傳的檔案，您可以至頁面右上角的**現有知識**區塊，在那裡您可以在**上傳檔案**區段找到等待您的上傳資料。

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step5.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Submit' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">


## 檢查知識庫
點擊您剛剛上傳的檔案並檢視內容。大功造成！您已成功地將一份試算表格上傳到您的SeaChat代理中。您現在可以使用知識庫來測試您的助理。SeaChat提供了額外的設定來客制您的知識庫，我們將在教學的下一部分繼續探索這些功能。

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step6.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Next' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">


## :brain: 運作原理``

使用這個功能時請注意以下幾點:

1. SeaChat不對視頻文件的內容做任何處理. 它單純從視頻中提取音軌，並將音頻轉錄為文本，這些文本可以拿在知識庫中使用。
2. 對於每個轉錄的音頻和視頻，您可以在現有知識庫中檢查轉錄品質。
3. 如果您有其他語言的多媒體文件，請先將它們轉錄為文本，然後上傳到SeaChat而達到相同的目的。
4. 對於音頻/視頻文件，SeaChat會預設文件中只有一位發言者。也就是說，SeaChat不進行話者分離或話者識別。如果您有一個包含對話的音頻文件（例如，一個兩人的廣播），您應該首先將其轉錄並在每句發言者的開頭加上發言者的名字。



## 協助支援
需要協助？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai).
