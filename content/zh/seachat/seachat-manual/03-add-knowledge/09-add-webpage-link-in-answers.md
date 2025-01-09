---
title: "新增URL按鈕到知識庫回應"
description: "學習如何在 SeaChat AI 助理的回應中新增參考 URL，為用戶提供更詳細的信息。通過新增 URL，您的 AI 助理將能夠提供更全面的客戶支援。"
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-05-29T08:48:57+00:00
draft: false
images: []
aliases:
  - /zh/seachat/seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers/
url: /zh/seachat/manual/add-knowledge/webpage-link/
weight: 30
toc: true
---

> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。

# 簡介

您可以在 AI 助理的回應中包含相關的參考 URL，讓用戶可以訪問更詳細的內容。在 **現有知識** 頁面中，您可以找到相關知識並將參考 URL 新增到 AI 助理的回應中。此功能通過在用戶尋找特定信息時提供額外的信息和資源來增強用戶體驗。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/new-kb-ui.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/new-kb-ui.png" alt="展示如何撰寫助理描述的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">知識附加設置</p>
</div>

## [知識庫中的其他設置](#additional-setting-ui)

在**AI助理配置**下找到**知識庫**並點擊開啟已上傳的知識，找到**編輯**按鈕，並新增URL按鈕到該知識上。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/choose-knowledge.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/choose-knowledge.png" alt="選擇要新增URL按鈕的知識項目">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">選擇要新增URL按鈕的知識項目</p>
</div>

## [按鈕](#additional-setting-ui)

SeaChat 提供了不同的方法來向助理的回應中添加額外信息。選擇「按鈕」選項，將 URL 按鈕添加到助理的回應中。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/choose-button.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/choose-button.png" alt="選擇按鈕類型以新增URL按鈕">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">選擇按鈕類型以新增URL按鈕</p>
</div>

## 新增 URL 按鈕到知識庫回應

知識庫是我們的助理將尋找信息以回應用戶查詢的地方。一個非常強大的用例將是 FAQ 助理，助理可以提供對常見問題的回答。在這種情況下，您可以將 URL 新增到助理的回答中，為用戶提供更詳細的信息。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/url-to-answer.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/url-to-answer.png" alt="URL 已新增到助理的答案中">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">URL 已新增到助理的答案中</p>
</div>

### 按鈕訊息的限制

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/kb-id-problem.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/kb-id-problem.png" alt="因字元限制所造成的訊息中斷">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">因字元限制所造成的訊息中斷</p>
</div>
<br/>

以下是我們按鈕模板和回傳按鈕的目前的限制摘要：

- 訊息字元限制：200 字元
- 回傳按鈕內容字元限制：所有按鈕共 300 字元
- 回傳按鈕數量限制：最多 4 個按鈕

### KB ID

KB ID 是每個知識庫項目中的知識的唯一識別碼。您可以通過點擊該知識項目下的 **更多** 按鈕中的 **複製 KB ID** 按鈕，將知識項目的 ID 複製到剪貼板。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/kb-id.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/kb-id.png" alt="使用 KB ID 完整消息">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">使用 KB ID 完整消息</p>
</div>

> 🚨注意 🚨
>
> 出於安全考量，AI 助理無法訪問來自其他 AI 助理知識庫中的 KB ID。KB ID 是該指定 AI 助理知識庫中的知識的唯一識別碼，無論它們是否位於同一工作區。

## 從試算表中新增URL按鈕到助理的回應

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/spreadsheet-example.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/spreadsheet-example.png" alt="試算表範例">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">試算表範例</p>
</div>
