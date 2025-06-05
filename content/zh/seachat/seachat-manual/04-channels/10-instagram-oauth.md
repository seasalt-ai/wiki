---
title: "Instagram 登錄使用"
description: "按照以下步驟將 Instagram 與您的應用程式整合，並建立AI agent的訊息。"
date: 2024-12-24T08:00:00+00:00
lastmod: 2024-12-24T08:00:00+00:00
weight: 304
draft: false
toc: true
url: /zh/seachat/manual/channels/instagram-oauth/
---

## 前置需求

- **Instagram Professional Account**：您需要擁有 **Business** 或 **Creator** 帳戶才能設定 **Instagram Messaging**。如果您目前的帳戶類型不符，可以在 **Instagram settings** 中 [切換到 Professional Account](https://www.facebook.com/business/help/502981923235522)。

### 只需兩步完成 Instagram 整合

前往 SeaChat 通道頁面中的 `Instagram` 卡片。
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/instagram/instagram-card.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/instagram/instagram-card.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

**步驟 1: 登入你的 Instagram 帳號**

點擊 `Connect` 按鈕，將出現 Instagram 登入弹窗。授予所有權限並點擊 `允許`

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/instagram/instagram-step-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/instagram/instagram-step-1.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 


**步驟 2: 選擇訊息輸入語言**

設定輸入訊息的語言，SeaChat 將以相同語言轉錄並回應。這個設定同樣適用於系統訊息（例如點擊 🧹開始新話題時）


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/instagram/instagram-step-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/instagram/instagram-step-2.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

🚀 完成啦！整合完成後，SeaChat 將開始以你的 AI 智能助理處理 Instagram 訊息，你可以立即測試發送訊息。

### 曾使用舊方式連線 Instagram？

如果你過去是用舊方式連線，現在需要分成兩步重新設定：

#### 步驟 1: 從 SeaChat 移除
- 前往 SeaChat 的 Instagram 連線頁面，在 Deprecated 區塊中找到舊會訊卡片
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/instagram/instagram-card-deprecated.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/instagram/instagram-card-deprecated.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

<br/> 

- 點擊右上角的 `移除` 按鈕刪除
- 然後前往新的 `Instagram` 卡片，依照新步驟重新連線

#### 步驟 2: 從 Meta App 移除認證
正確從 Meta App 中移除帳號認證
前往 **Meta Business App** → **Instagram API setup with Instagram login** → **Generate access tokens** → 垃圾桶圖示 → **Remove Account**

🙋 需要遷移協助嗎？ <br/>
📧 請聯絡我們： seachat@seasalt.ai  <br/> 
