---
title: "客制GPT工具"
description: ""
date: 2025-01-06T08:48:45+00:00
lastmod: 2024-01-06T08:48:45+00:00
draft: false
weight: 54
url: /zh/seachat/seachat-manual/custom-gpt-tool/gpt-tools
---

## 簡介

SeaChat 的 客制GPT工具 允許用戶通過將自定義操作直接整合到對話中來增強代理的回應能力。此功能使用戶能夠定義具體條件，以便代理在滿足條件時執行這些操作，提供量身定制的回應和基於實時資訊的智能支援。例如，您可以讓代理執行搜索或從您公司的 API 獲取數據，讓 SeaChat 能夠利用外部資源提供更豐富的答案。

## 影片教學

以下是簡單教程，展示如何調用兩個 APIs 以顯示單張圖片。我們演示了如何配置 API 端點，並在聊天中顯示可愛的狗狗圖片：

<iframe width="100%" height="400" src="https://www.youtube.com/embed/olWQTiPLHOc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第二個教程中，我們通過配置 API 參數調用天氣 API，並動態將地點名稱轉換為 GPS 座標以獲取準確的天氣資訊：

<iframe width="100%" height="400" src="https://www.youtube.com/embed/7v7zBr5j-So?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第三個教程中，我們演示了如何在聊天中獲取包含多張狗狗圖片的卡片輪播。我們展示了如何利用 **PATH** 參數來顯示特定狗品種的多張圖片：

<iframe width="100%" height="400" src="https://www.youtube.com/embed/wBGJyfB9hcY?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第四個教程中，我們展示了如何使用 SeaChat 的 客制GPT工具 設置電子郵件警報，檢測聊天中的敏感內容並自動發送電子郵件通知。

<iframe width="100%" height="400" src="https://www.youtube.com/embed/KhjHDbRTIJc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第五個教程中，我們展示了如何在 SeaChat 中設置簡訊 通知來監控用戶對話。例如，我們演示了如何在檢測到用戶對話中有抑鬱跡象時設置簡訊 警報。

<iframe width="100%" height="400" src="https://www.youtube.com/embed/Z7Zj6BWEXTc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第六個教程中，我們展示了如何自動通過簡訊 向呼叫者發送資訊。

<iframe width="100%" height="400" src="https://www.youtube.com/embed/LNezPT4qzCs?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>


## 快速入門

要啟用此功能，登錄 SeaChat 後，導航至 **AI助理配置** \-\> **整合** \-\> **客制GPT工具**。

>
> SeaChat 目前支持三種類型的工具：
>
> - **搜尋和顯示**：允許 SeaChat 使用您的 API 執行外部搜索，並基於對話上下文獲取附加資訊。搜索結果將以純文本或卡片輪播形式顯示在 webchat 中。
> - **電子郵件**：根據您的指示自動發送電子郵件。請確保指定目的、收件人和條件。要向用戶發送電子郵件，請通過 webchat 表單收集他們的電子郵件地址。
> - **發送簡訊**：根據您的指示自動發送簡訊。定義目的、收件人和條件。要向用戶發送簡訊，請確保通過渠道或 webchat 表單獲取他們的電話號碼。
>
> <br/>
> <center>
> <a href="/images/seachat/en/gpt-tools/seachat-tool-options.png">
> <img height="100%" width="100%" src="/images/seachat/en/gpt-tools/seachat-tool-options.png"  alt="SeaChat 支援的工具類型">
> </a>
> <br/>
> </center>

## 配置 搜尋和顯示的步驟：

### 步驟 1：選擇工具類型

SeaChat 目前支持一種類型的工具：

* **搜尋和顯示**：這些工具允許 SeaChat 使用您的 API 執行外部搜索，並基於對話上下文獲取附加資訊。搜索結果將以純文本或卡片輪播形式顯示在 webchat 中。

我們計劃未來支持更多類型的工具。
