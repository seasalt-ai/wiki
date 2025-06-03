---
title: "真人客服"
description: "學習如何在與 SeaChat 的聊天對話中轉接至真人客服。同時探索如何、管理對話，確保順暢的客戶支援體驗。探索在不同頻道（如 WebChat 和 LINE）上轉接真人客服的步驟。"
lead: ""
date: 2024-05-08T08:48:45+00:00
lastmod: 2024-05-21T08:48:45+00:00
weight: 102
draft: false
images: []
aliases:
  - /zh/seachat/seachat-manual/02-create-agent/02-live-agent-transfer/
url: /zh/seachat/live-agent-transfer/  
toc: true
---

真人客服在需要時可以接管 AI 助理的對話。真人客服不僅可以接管對話，還可以為AI助理提供新知識，並通過測試和微調AI助理的回應來幫助培訓AI助理。

SeaChat 提供許多集成配置和頻道，可能需要不同的配置才能啟用真人客服功能。 我們建議您參考 [第三方整合](https://wiki.seasalt.ai/zh/seachat/seachat-manual/05-integrations/01-seachat-google-calendar-integration/) 或 [頻道](https://wiki.seasalt.ai/zh/seachat/manual/channels/webpage/) 以了解如何正確設置您的真人助理模式。

在本教學中，我們將向您展示如何在聊天對話中轉接至真人客服，以及如何使用 SeaChat 提供的不同方法設置它。

## 助理設定

在將自定義 AI 助理集成到工作環境之前，我們需要確保您的 SeaChat 帳戶中已啟用了真人客服功能。 到側邊欄選單中的**AI助理配置**下的**AI助理資訊**。 您可以看到您的 AI 助理的所有基本設置。 如果您想重新配置您的助理，您都可以在這裡完成。

在屏幕底部，您可以看到一個勾選框，上面寫著***用戶可以在聊天期間要求與客服人員對話***。 請務必勾選此框以啟用真人客服功能。

> :exclamation: **重要提示** :exclamation:
>
> 如果您選擇啟用真人客服功能，您的客戶現在將在聊天對話期間有轉接真人客服的選項。 這需要您提供一位真人客服定期值班，該客服將檢查新對話並即時回答用戶。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-1.png" alt="在SeaChat基本設定頁面開啟真人客服">
</a>
</center>
<br/>

## 以真人客服身份與客戶交談
點開在左側選單的**對話**部分。 在這裡，您可以查看 AI 助理與客戶之間的所有對話。 您可以查看對話歷史和對話狀態，這是您的真人客服對話的控制中心。

如果客戶在聊天對話期間轉接真人客服，人類助理將看到一個指示轉接的彈出通知。 如果對話列表過長，只需點擊**真人客服**按鈕即可查看真人客服需要完成的對話列表。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-2.png" alt="真人客服查看對話">
</a>
</center>
<br/>
<br/>

就是這麼簡單。 您現在已為您的 SeaChat AI 助理設置了真人客服轉接功能。 您可以讓真人客服接管對話，以進一步協助您的客戶。 一旦真人客服完成客戶的轉接，真人客服必須點擊**完成**按鈕將對話交還給 AI 助理。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-3.png" target="_blank">
<img width="70%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-3.png" alt="與真人客服對話">
</a>
</center>
<br/>
<br/>

一旦真人客服完成對話，對話將標記為已完成，並通知客戶對話已完成。 在需要時，真人客服也可以重新啟動對話。 只需點擊**重新啟用**按鈕即可重新開始對話。

### Markdown 支援

SeaChat 對話在其網頁頻道中支援 URL 和 Markdown 格式。無論是您的真人助理還是用戶，都可以在聊天對話中插入連結和 Markdown 文字。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/live-agent-transfer/markdown-support-in-response.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/markdown-support-in-response.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">助理回應中的 Markdown 支援</p>
</div>
</div>

<br/> 

對話將以輸入時的相同格式顯示。這個功能在需要保持信息的原始格式以便於閱讀時特別有用。您可以輕鬆地將信息複製並貼上到對話中，而不會丟失格式。目前，Markdown 支援僅適用於網頁聊天整合。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/live-agent-transfer/markdown-response-in-web-ui.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/markdown-response-in-web-ui.png" alt="SeaChat | Markdown 支援">
</a>
    <p style="margin-top: 20px; font-size: 15px">WebChat UI 中的 Markdown 支援</p>
</div>
</div>

<br/> 


## 如何在 WebChat 上轉接真人客服

> :open_book: **備註** :open_book:
>
> WebChat widget 可以同時嵌入在你的自製網站或者你的**Shopify**、**Squarespace**、**Wix**網站中。可以查看[網頁機器人](https://wiki.seasalt.ai/zh/seachat/manual/channels/webpage/)和[第三方整合](https://wiki.seasalt.ai/zh/seachat/seachat-manual/05-integrations/01-seachat-google-calendar-integration/) 以獲取更多把Webchat widget嵌入到網站的相關信息。


WebChat 頻道讓您在網站上嵌入 SeaChat 對話小工具。這個頻道是企業用於提供客戶支援的最常見頻道。

聊天對話將向您的客戶顯示目前有多少真人客服可用，他們可以在聊天對話期間通過點擊***轉接真人***按鈕轉接真人客服。若沒有真人客服在線上，客戶也可以選擇留言，客服人員上班時可以查看並回覆訊息。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-web-widget-1.png" alt="若沒有真人客服在線上，客戶也可以選擇留言，客服人員上班時可以查看並回覆訊息。">
</a>
</center>
<br/>

如果您的AI助理程式部署到非網頁聊天頻道（例如 Messenger 和 WhatsApp），它們將無法顯示該按鈕。使用者可以像下面這樣口頭請求人工客服轉接：

<br/>
<a href="/images/seachat/zh/live-agent-transfer/ask-to-chat-with-live-agent-zh.jpeg" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/ask-to-chat-with-live-agent-zh.jpeg" alt="Request Live Agent | SeaChat Live Agent Transfer">
</a>
<br/>


這項功能可以單獨打開，或者和真人轉接按鈕一起使用：

<br/>
<a href="/images/seachat/zh/live-agent-transfer/settings-ask-to-chat-with-live-agent-zh.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/settings-ask-to-chat-with-live-agent-zh.png" alt="Request Live Agent | SeaChat Live Agent Transfer">
</a>
<br/>


## 如何在 LINE 上轉接真人客服

一旦您集成了 LINE 頻道並開啟真人客服服務，您的客戶將在 LINE 聊天的底部看到 **Live Agent** 按鈕。 客戶可以在聊天對話期間點擊**Live Agent**按鈕轉接真人客服。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-line-channel.png" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-line-channel.png" alt="集成 LINE 頻道並開啟真人客服服務">
</a>
</center>
<br/>

## 混合模式 (AI 助理 + 真人客服)

除了僅由真人客服或僅由 AI 助理提供服務的模式，SeaChat 還提供一種混合模式，讓真人客服與 AI 助理能夠協同合作，共同提供客戶支援。

混合模式 (AI 助理 + 真人客服) 結合了真人客服和 AI 助理的優勢，大大提升了提供客戶支援的靈活性。

基於這種靈活性，以下是僅在混合模式下可用的功能選項：

### 1. 不允許客戶主動請求真人客服

若選擇此選項，**顯示摘要** 和 **自動切換至 AI 助理** 功能將隱藏或顯示為灰色，且用戶在對話期間無法請求真人客服。

<center>
<a href="/images/seachat/zh/live-agent-transfer/do-not-request.png" target="_blank" alt="不允許客戶主動請求真人客服">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/do-not-request.png" alt="不允許客戶主動請求真人客服">
</a>
</center>
<br/>


### 2. 顯示摘要
若選擇此功能，對話中的所有人都可以查看對話的摘要。

<center>
<a href="/images/seachat/zh/live-agent-transfer/remove-live-agent.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/remove-live-agent.png" alt="SeaChat | 自動切換">
</a>
</center>
<br/>

### 3. 自動切換至 AI 助理

有時候，真人客服可能需要同時處理大量對話，可能會忘記點擊 **完成** 按鈕，將對話交回給 AI 助理。為了防止這種情況發生，可以設定真人客服功能的自動超時。若對話在一段時間內無活動，系統將自動完成對話。

<center>
<a href="/images/seachat/zh/live-agent-transfer/auto-timeout.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/auto-timeout.png" alt="Auto Transfer Back to AI Agent"">
</a>
</center>
<br/>

## :dart: 疑難排解

### 移除真人客服功能
若要停用真人客服功能，只需在 **基本設定** 的 **對話處理模式** 中取消勾選 ***不允許客戶主動請求真人客服***。這將停用真人客服功能，客戶在對話期間將無法請求真人客服，也無法看到 **真人客服** 按鈕。


> :pushpin: 注意
>
> 若有真人客服可用，他們仍然可以在 **對話** 中監控並接管對話。取消勾選此選項僅會移除客戶請求真人客服的選項。


## 需要幫忙?
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。
