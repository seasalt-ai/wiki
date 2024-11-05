---
title: "匯入站點地圖"
description: "探索如何利用SeaChat將站點地圖直接匯入到您AI助理的知識庫中。本教學詳細介紹了將站點地圖內容完整匯入助理的全部步驟，以及如何提取XML文件中的所有網址。"
date: 2024-04-18 10:43:51.069 +0100
lastmod: 2024-04-19 10:43:51.069 +0100
weight: 36
draft: false
images: []
aliases:
  - /zh/seachat/seachat-manual/03-add-knowledge/07-import-sitemap/
url: /zh/seachat/manual/add-knowledge/import-sitemaps/
---
> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。


## 簡介
SeaChat 提供許多不同的方式讓您上傳文件到您助理的知識庫中。在本教學中，我們將專注於 **匯入站點地圖** 方法。讓我們以站點地圖向您展示如何將網址匯入到您的助理的知識庫。

## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/) 找到創建AI助理的步驟。

## 打開知識庫
通過側邊欄選單中的 **AI助理配置** 下的 **知識庫** 面板找到您的助理的知識庫。選擇 **匯入站點地圖**，並準備好要上傳到您的助理的 XML 文件。

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/choose-import-sitemaps.png" alt="通過側邊欄選單中的助理進入知識庫面板以顯示如何通過匯入網址進行上傳。">

*知識庫面板*
</center>

## 輸入站點地圖
通過匯入站點地圖，您可以跳過逐一添加網址的過程。您的站點地圖，通常是 XML 文件，將包含您匯入的網站中的所有連結。

將網址複製並粘貼到相應的輸入框中。一旦您確定包含的網址，點擊 **新增** 以確認。

> :rotating_light: **注意** :rotating_light:
>
> 請注意，並非所有網站都有站點地圖。取得定位網站的 XML 站點地圖的最常見（且簡單）方法之一是手動檢查。您需要做的是在瀏覽器中輸入您的網站 URL，然後在 URL 的末尾添加 `sitemap.xml`，例如 www.YourWebsiteUrl.com/sitemap.xml。如果出現站點地圖（看起來像 XML 文件），則該網站具有站點地圖。有更多定位您的站點地圖的方法，請參閱 [此文章](https://seocrawl.com/en/how-to-find-a-sitemap/) 以了解更多信息。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/enter-url.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/enter-url.png" alt="">
</a>

*插入站點地圖的 URL*
</center>

## 提交之前
一旦您添加了站點地圖，SeaChat 將自動解析 XML 文件並提取網址。您可以在提交到您的助理的知識庫之前檢查這些網址。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/before-submission.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/before-submission.png" alt="SeaChat 的介面顯示了用於監控正在上傳的每個文件狀態的上傳部分，提醒用戶在提交之前驗證文件格式和內容。">
</a>

*檢查已上傳的文件*
</center>

## 送出到現有知識庫
文件成功上傳後，您將看到一個成功的消息。您已成功的為您的 AI 助理，增加了新的知識。要查看已上傳的文件，您可以到頁面右上角的 **現有知識** ，在那裡您可以在 **網站地圖** 中找到新的上傳數據。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/existing-files.png" alt="視覺指南突出顯示位於屏幕右上角的 '現有' 部分，其中突出顯示了 '網站地圖' 部分中的上傳文件。">
</a>

*在 **現有知識** 中查找文件*
</center>

## 檢查知識庫
單擊您剛上傳的文件以查看內容。您站點地圖上的文本現在已經被加入到您的知識庫中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/review-upload.png" alt="視覺指南突出顯示位於屏幕右上角的 '現有' 部分，其中突出顯示了 '網站地圖' 部分中的上傳文件。">
</a>

*審核上傳的站點地圖*
</center>


## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。
