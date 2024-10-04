---
title: "時間意識與上下文"
description: "了解 SeaChat AI 的時間意識與上下文功能，提升助理在時間敏感回應中的控制能力。"
lead: ""
date: 2024-10-01T08:48:45+00:00
lastmod: 2024-10-01T08:48:45+00:00
weight: 100
draft: false
images: []
toc: true
aliases:
   - /zh/seachat/seachat-manual/02-create-agent/03-advanced-settings/04-time-awareness-context/
---

---

## 簡介

除了 [檢索增強生成 (RAG)](https://wiki.seasalt.ai/seachat/seachat-manual/02-create-agent/03-advanced-settings/02-retrieval-augmented-generation-rag/) 功能和 [記憶](https://wiki.seasalt.ai/seachat/seachat-manual/02-create-agent/03-advanced-settings/03-agent-memory/)，SeaChat AI 還提供了多種進階設定選項，讓用戶可以進一步控制助理們行為。

雖然這些功能不如 RAG 和記憶那麼複雜，但在某些情況下，它們提供相當的價值。本文將簡單介紹這些功能。

---

## 時間意識

<br/>

<center>
<a href="/images/seachat/zh/time-awareness-context/time-awareness-ui.png">
<img height="100%" width="100%" src="/images/seachat/zh/time-awareness-context/time-awareness-ui.png"  alt="UI of Time Awareness Feature">
</a>

</center>

<br/>

時間感知功能讓 AI 助理能夠理解特定時區的當前時間。這對於向客戶提供與時間相關的資訊非常有幫助。

<br/>

<center>
<a href="/images/seachat/zh/time-awareness-context/time-awareness-kb.png">
<img height="100%" width="100%" src="/images/seachat/zh/time-awareness-context/time-awareness-kb.png"  alt="Knowledge Example Used in Example Use Case">
</a>

</center>

<br/>

例如，如果企業用戶在營業時間和非營業時間有兩個不同的客戶服務電話號碼（分別是 02-37284471 和 02-37222231），時間感知的 AI 助理可以根據當前時間提供相應的號碼。

如果客戶在營業時間聯絡 AI 助理，助理可以提供第一個號碼（02-37284471）。如果在非營業時間聯絡，助理則會提供第二個號碼（02-37222231）。這項功能為 AI 助理的回應增添了個性化的層次。
<br/>

<center>
<a href="/images/seachat/zh/time-awareness-context/time-awareness-example.png">
<img height="100%" width="100%" src="/images/seachat/zh/time-awareness-context/time-awareness-example.png"  alt="Example Use Case of Time Awareness">
</a>

</center>

<br/>

## 上下文

上下文功能允許用戶設置 AI 助理在生成回應時應參考的最大對話輪數。當您希望提供具有上下文感知的回應，但又不想引用整個對話歷史時，這個功能非常有用。

通過限制對話輪數，用戶可以減少回應延遲，並避免 AI 助理被過多的信息所淹沒。
