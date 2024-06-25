---
title: "新增URL按鈕到知識庫回應"
description: "學習如何在 SeaChat AI 助理的回應中新增參考 URL，為用戶提供更詳細的信息。本指南將帶您通過在「現有知識」頁面中新增 URL，豐富 AI 助理的互動。包括的 YouTube 視頻教程將詳細展示這個過程，確保易於理解和實施這些增強功能。通過新增 URL，您的 AI 助理將能夠提供更全面的客戶支持，提升用戶體驗。"
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-05-29T08:48:57+00:00
draft: false
images: []
aliases:
  - /zh/seachat/seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers/
weight: 150
toc: true
---

# 簡介

您可以在 AI 助理的回應中包含相關的參考 URL，讓用戶可以訪問更詳細的內容。在 **現有知識** 頁面中，您可以找到相關知識並將參考 URL 新增到 AI 助理的回應中。此功能通過在用戶尋找特定信息時提供額外的信息和資源來增強用戶體驗。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/new-kb-ui.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/new-kb-ui.png" alt="展示如何撰寫代理描述的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">知識附加設置</p>
</div>

## [知識庫中的其他設置](#additional-setting-ui)

在**AI助理配置**下找到**知識庫**並點擊開啟已上傳的知識，找到**編輯**按鈕，並新增URL按鈕到該知識上。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/choose-knowledge.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/choose-knowledge.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Choose the Knowledge to add URL Buttons to</p>
</div>

確保提供一個清晰的 **文件標題** 以便助理輕鬆檢索知識。此外，在 **文件文本** 中仔細描述您提供的信息。您的描述將幫助助理根據您提供的信息形成回應。

現在，每當 AI 助理從知識庫檢索這些信息時，它將記得在其回應中附上 URL 按鈕。

## [按鈕](#additional-setting-ui)

SeaChat 提供了不同的方法來向助理的回應中添加額外信息。選擇「按鈕」選項，將 URL 按鈕添加到助理的回應中。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/choose-button.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/choose-button.png" alt="展示如何撰寫代理描述的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px"> 選擇按鈕類型</p>
</div>

您在這裡提供的 URL 將作為按鈕顯示在聊天窗口中。當用戶點擊該按鈕時，他們將被重定向到您提供的 URL。在 **標題** 中放入您希望顯示給用戶的標籤，並在 **內容** 欄位中提供 URL。您可以通過簡單地點擊加號（新增）按鈕來將任意多個按鈕新增到答案中。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/add-more-url.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/add-more-url.png" alt="展示如何撰寫代理描述的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">按加號按鈕新增 URL 按鈕</p>
</div>

## 新增 URL 按鈕到知識庫回應

知識庫是我們的助理將尋找信息以回應用戶查詢的地方。一個非常強大的用例將是 FAQ 助理，助理可以提供對常見問題的回答。在這種情況下，您可以將 URL 新增到助理的回答中，為用戶提供更詳細的信息。

現在，讓我們在聊天窗口中測試 URL 按鈕。當 AI 助理從知識庫中檢索某些信息作為上下文信息時，如果為這些信息啟用了按鈕功能，它將在回應中顯示 URL 按鈕。用戶可以點擊按鈕訪問 URL 並獲取更詳細的信息，就這麼簡單！

首先，我們將一些信息上傳到助理的知識庫。請參考[這裡](/zh/seachat/seachat-manual/03-add-knowledge/)以找到將信息上傳到助理知識庫的方法。

一旦知識庫中有信息，助理將開始使用這些信息來回應用戶查詢。我會在助理的回答中提供多個 URL，以向您展示它是如何工作的。您可以將任意多個 URL 新增到助理的答案中。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/url-to-answer.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/url-to-answer.png" alt="展示如何撰寫代理描述的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">URL 已新增到助理的答案中</p>
</div>

## 從試算表中新增URL按鈕到助理的回應

您也可以使用試算表在助理的回應中新增 URL 按鈕。當您使用試算表上傳大量資訊時，手動為每個知識添加參考按鈕可能會很困難。不用擔心，SeaChat 為您提供了解決方案。

通過在試算表中添加名為 **seachat_ref** 的額外欄位，您的AI助理將自動提取資訊，將 URL 按鈕新增到助理的回應中。

| seachat_ref ||
|-------------|-|
| 按鈕標題        |
| 按鈕值         |
|             |

由於助理將檢查此特定欄位，我們需要確保使用正確的變數來幫助助理理解資訊。

**請務必按照以下格式操作，以確保助理能正確提取資訊：**

在 **seachat_ref** 欄位的每一行中，您的 AI 助理將尋找兩條資訊：<code>按鈕標題</code>（第1行）和<code>按鈕值</code>（第2行）。以下是 seachat_ref 欄位的範例：

在 SeaChat 助理的知識庫中還有更多進階功能，您可以利用這些功能來優化助理的回應。請查看我們的[進階功能](/zh/seachat/seachat-manual/03-add-knowledge/09-advanced-features/)教學，以了解有關這些功能的更多信息。

```
"用戶手冊 Wiki" --- 第1行
"https://user-manual-wiki.com" --- 第2行
```

> 🚨注意🚨
>
> 如果按鈕值不是 URL，例如某些文本、2段落或3行中的3個 URL，按鈕將在點擊時顯示按鈕值的全部內容。


<br/>

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/spreadsheet-example.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/spreadsheet-example.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">試算表範例</p>
</div>


您放入 `seachat_ref` 的所有信息都會被提取為按鈕。如果按鈕值的內容是 URL，則點擊按鈕時會將用戶重定向到該 URL。如果按鈕值不是 URL，則按鈕會在回應中顯示按鈕值。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/non-url-buttons.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/non-url-buttons.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">回應中加上按鈕</p>
</div>


<br/>

這樣一來，當您上傳包含大量信息的試算表格時，就不再需要擔心需要手動將 URL 按鈕添加到您的助理回應中。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/spreadsheet-url-buttons.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/spreadsheet-url-buttons.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">回應中加上多個連結按鈕</p>
</div>


<br/>

在 SeaChat 助理的知識庫中還有更多進階功能，您可以利用這些功能來優化助理的回應。請查看我們的[進階功能](/zh/seachat/seachat-manual/03-add-knowledge/09-advanced-features/)教學，以了解有關這些功能的更多信息。
