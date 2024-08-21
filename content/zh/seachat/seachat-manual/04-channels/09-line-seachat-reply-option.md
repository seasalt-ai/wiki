---
title: "管理 Line 和 SeaChat 的整合"
description: "了解如何管理和整合 Line 與 SeaChat 的回覆系統，包括完全關閉 Line 的真人聊天功能或同時使用兩個平台來處理訊息。此指南詳細介紹了各種選項的優缺點，幫助您在提供最佳客戶體驗的同時，優化訊息管理的成本。"
date: 2024-08-20T08:48:57+00:00
lastmod: 2024-08-20T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
      parent: "seachat-intro"
aliases:
  - /zh/seachat/seachat-manual/04-channels/09-line-seachat-reply-option/
weight: 90
toc: true
---

本節將說明在整合 Line 和 SeaChat 時的步驟與考量，包括完全取代 Line 的真人聊天功能或同時使用兩個平台的選項。

## 選項 1：完全關閉 Line 的真人聊天功能

**步驟 1：** 關閉 Line 的真人聊天功能。

* 參考以下圖片： 這張圖片顯示了 Line 的可用訂閱方案，並詳細說明了各個訊息限額的定價。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/seachat-channels/09-line-seachat-reply-option/" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/seachat-channels/09-line-seachat-reply-option/" alt="">
</a>

**模型定價**
</center>

**關閉後：**

* 參考以下圖片： 此界面顯示目前已關閉聊天功能。
* 此時，您可以使用 SeaChat 的功能來取代 Line 的自動回覆和真人聊天功能，所有對話記錄都將保存在 SeaChat 中。
  
<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/seachat-channels/09-line-seachat-reply-option/" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/seachat-channels/09-line-seachat-reply-option/" alt="">
</a>

**模型定價**
</center>

## 選項 2：同時使用兩個平台

在此設置中，Line 和 SeaChat 都可以對來訊作出回應。不過，需要注意處理每個平台回覆的相關事項。用戶均可從Line後台或SeaChat後台切換真人

### 自動回覆：

* SeaChat 可以自動回覆訊息。這些回覆會同時顯示在 Line 後台和 SeaChat 後台。

### 從 Line 後台真人回覆：

**優點：**

* 真人回覆的訊息會完整展示在 Line 後台。

**缺點：**

* 真人回覆的訊息不會顯示在 SeaChat 後台。
* SeaChat 不會知道 Line 已經有真人回覆訊息，因此 SeaChat 仍會照常回覆，這可能導致用戶收到兩則回覆：SeaChat 的回覆（通常是第一條）以及 Line 後台的真人回覆。
* 使用 SeaChat 回覆會產生費用，每則訊息大約花費新台幣 $0.3（GPT-3.5）或 $0.18（GPT-4o-mini）。

### 從 SeaChat 真人回覆：

**優點：**

* 真人回覆的訊息會完整展示在 SeaChat 後台。

**缺點：**

* 真人回覆的訊息不會顯示在 Line 後台。
* 這些回覆會占用 Line 的每月訊息數量限額（免費用戶每月 200 則）。若當月用完，則無法發送訊息，必須升級方案。

## Line 的收費策略

* 透過 LINE 官方帳號管理員真人回覆不會佔用免費訊息數量。
* 參考官方定價詳情：[LINE 官方帳號管理員定價](https://tw.linebiz.com/column/LINEOA-2023-Price-Plan/)

### 哪些訊息類型會列入計費？

* 只有「群發訊息」、「Messaging API 進階功能的 Push API 訊息」以及「漸進式訊息」會列入計費。以下訊息類型屬於「免付費」訊息：
    * 加入好友的歡迎訊息。
    * 一對一的真人聊天訊息。
    * 自動回覆訊息。
    * AI 自動回覆訊息。
    * Messaging API 的 Reply API。
  
* 請參考以下推廣方案細節。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/seachat-channels/09-line-seachat-reply-option/" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/seachat-channels/09-line-seachat-reply-option/" alt="">
</a>

**模型定價**
</center>