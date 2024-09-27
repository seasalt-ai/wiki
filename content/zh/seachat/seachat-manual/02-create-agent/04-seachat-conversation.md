---
title: "助理對話"
description: "透過 SeaChat 助理對話，輕鬆管理和回應所有進行中的對話，並有效提升互動效率。瞭解如何查看對話歷史並下載音訊記錄。"
date: 2024-07-30T08:48:57+00:00
lastmod: 2024-07-30T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /zh/seachat/seachat-manual/seachat-agent-conversation/
weight: 100
toc: true
---

## 對話列表

對話列表是您可以查看和管理所有助理正在處理的對話的地方。您可以查看每個對話的詳細資訊，檢查對話歷史記錄，並手動回答用戶的問題。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/seachat-conversation/conversation-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/seachat-conversation/conversation-dashboard.png" alt="">
</a>

**助理對話**
</center>

用戶可以在所有對話和真人助理對話之間切換。在真人助理對話中，用戶可以查看由真人助理處理的對話。

在每個對話行中，都會有一個圖標指示對話頻道，如LINE或網頁機器人。您可以通過這些圖標輕鬆識別對話的溝通渠道。

## 下載音訊對話

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/seachat-conversation/download-audio.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/seachat-conversation/download-audio.png" alt="">
</a>

**下載音訊對話**
</center>

對於帶有電話圖標的對話，您可以通過點擊對話內的下載圖標來下載音訊對話。音訊對話將以 `mp3` 格式下載。這是功能在品質保管理和培訓目的上非常有用，因為您可以收聽助理和用戶之間的對話，並提供回饋以改善助理的回應。


## 下載助理對話歷史記錄

如果您希望下載某些助理對話的歷史記錄，您可以前往 **工作區** -> **AI助理**。

點擊 **下載對話**，然後選擇您想下載的對話歷史記錄的年份。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/seachat-conversation/download-conversation-history.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/seachat-conversation/download-conversation-history.png" alt="">
</a>

**下載對話歷史記錄**
</center>

根據對話歷史記錄的大小，這個過程可能需要一些時間。當下載準備好時，您會收到系統通知，內容為「AI助理對話歷史導出成功,請點擊或複製連結至瀏覽器下載,該連結有效期為 24 小時。」

點擊連結以下載以壓縮檔格式保存的對話歷史記錄。

您將會看到以 CSV 檔案格式保存的對話歷史記錄。CSV 檔案包含以下欄位：

| Sender type | Channel type | Sender name | Time in GMT | Message | Data |
|-------------|--------------|-------------|-------------|---------|------|


- **發送者類型 (Sender type)**：發送者的類型。您可以識別發送者是AI助理、系統通知、用戶等。
- **頻道類型 (Channel type)**：對話的通訊通道。您可以識別對話是來自 WebChat、WhatsApp、電話等。以下為頻道類型的列表：
  - `系統（這指的是系統訊息）`
  - `WebChat`
  - `SeaAuth（這通常用於驗證目的）`
  - `Line`
  - `WhatsApp`
  - `Messenger`
  - `Instagram`
  - `語音（這指的是電話通話）`
  - `第三方客戶端`
  - `AgentPhone（這指的是來自 SeaChat 語音助理的電話通話，通常用於驗證 token）`
  - `SeaX_Call（這指的是透過 SeaX 進行的電話通話）`
  - `SeaX_SMS（這指的是透過 SeaX 發送的 SMS）`
- **發送者名稱 (Sender name)**：發送者的名稱。如果發送者是真人用戶，您會在此欄位找到發送者的 ID 或電子郵件。否則，將會顯示系統的識別碼。
- **GMT 時間 (Time in GMT)**：訊息的 GMT 格式時間戳。
- **訊息 (Message)**：對話的訊息內容。大部分情況下，這個欄位包含純文字訊息。然而，它也可以包含特定的指令類型，例如：
  - `/live_agent: 使用者要求將對話轉接至 live agent。`
  - `/submit_form: 使用者提交表單。如果涉及實體，指令會顯示為 /submit_form{"entity_name":"entity_value"}。`
  - `/clear_history: 使用者要求 bot 忘記對話記錄並重新開始。`
  - `/ai_agent: 使用者要求將對話轉接至 AI agent。`
- **資料 (Data)**：以JSON格式呈現的對話資料內容。如果對話中沒有資料內容，這個欄位將會是空的。當資料存在時，它可能包含但不限於以下類型：
  - `在訊息中傳送的圖片 URL。`
  - `語音通話的錄音檔案 URL。`
  - `使用者在聊天過程中填寫的表單。`
