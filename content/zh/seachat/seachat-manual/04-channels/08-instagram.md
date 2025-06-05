---
title: "Instagram (不推薦使用)"
description: "按照以下步驟將 Instagram 與您的應用程式整合，並建立AI agent的訊息。"
date: 2024-12-24T08:00:00+00:00
lastmod: 2024-12-24T08:00:00+00:00
weight: 305
draft: false
toc: true
url: /zh/seachat/manual/channels/instagram-webhook/
---

注意：此 Instagram 整合已不再推薦使用。請改用[Instagram 登錄使用](/zh/seachat/manual/channels/instagram/)。

## 前置需求

- **Instagram Professional Account**：您需要擁有 **Business** 或 **Creator** 帳戶才能設定 **Instagram Messaging**。如果您目前的帳戶類型不符，可以在 **Instagram settings** 中 [切換到 Professional Account](https://www.facebook.com/business/help/502981923235522)。

## 操作指引

### 步驟 1：建立 **Instagram App**

1. 訪問 [Meta Developer Site](https://developers.facebook.com/) 並點擊右上角的 **My Apps**。
2. 在下拉選單中選擇 **Create App** 開始建立。

- 輸入應用程式的相關資訊，如 **App Name** 和 **Contact Email**，然後點擊 **Next**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-name.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-name.png" alt="App Creation">
    </a>
</div>
</div>

<br/>

- 選擇一個使用案例，選擇 **Other**，然後點擊 **Next**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/use-cases.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/use-cases.png" alt="App Use Case Selection">
    </a>
</div>
</div>

<br/>

- 將 **App Type** 設定為 **Business**，然後點擊 **Next**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-type.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-type.png" alt="App Type Selection">
    </a>
</div>
</div>

<br/>

- 檢查應用程式的詳細資訊後，點擊 **Create App**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/business-details.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/business-details.png" alt="App Review and Creation">
    </a>
</div>
</div>

<br/>

### 步驟 2：將 **Instagram Product** 加入應用程式

- 在 **Add Products to Your App** 區域中選擇 **Instagram**。
- 點擊 **Set Up** 按鈕將其新增至應用程式。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/add-instagram.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/add-instagram.png" alt="Add Instagram Product">
    </a>
</div>
</div>

<br/>

### 步驟 3：連結 **Instagram Account**

- 前往 **API Setup with Instagram** 頁面。
- 在步驟 1 點擊 **Add Account**，連結您的 **Instagram Account**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/instagram-connect.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/instagram-connect.png" alt="Connect Instagram Account">
    </a>
</div>
</div>

<br/>

### 步驟 4：配置 **Webhook**

1. 在 **SeaChat** 獲取 **Webhook URL**。
    - 前往 **Agent Configuration** → **Channels** → **Instagram** 查看 **Callback URL** 和 **Verify Token**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/seachat-channel.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/seachat-channel.png" alt="SeaChat Webhook Details">
    </a>
</div>
</div>

<br/>

2. 點擊步驟 1 中的 **Set Up Verify Token**。完成後，會彈出提示框確認 Token 已成功儲存。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/verify-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/verify-token.png" alt="Verify Token Confirmation">
    </a>
</div>
</div>

<br/>

3. 回到 **Instagram App Dashboard**，將 **Webhook URL** 和 **Verify Token** 貼入相應欄位並點擊 **Save**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/callback-url.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/callback-url.png" alt="Webhook URL and Tokens">
    </a>
</div>
</div>

<br/>

- 點擊 **Manage**，啟用所有必要的 **Webhook Events**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/manage-webhook.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/manage-webhook.png" alt="Webhook Configuration">
    </a>
</div>
</div>

<br/>

### 步驟 5：生成 **Access Token**

- 在 **Generate Access Token** 區域中點擊 **Generate Token** 按鈕。
- 在彈出窗口中勾選 **I Understand**，然後複製 **Access Token**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/generated-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/generated-token.png" alt="Generate Access Token">
    </a>
</div>
</div>

<br/>

- 將複製的 **Token** 貼到 **SeaChat Instagram Setup Interface** 的步驟 2，然後點擊 **Save**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/save-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/save-token.png" alt="Access Token Setup">
    </a>
</div>
</div>

<br/>

完成所有步驟後，您已經成功在 **SeaChat** 中設置 **Instagram Integration**！

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/seachat-setup.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/seachat-setup.png" alt="Integration Complete">
    </a>
</div>
</div>

<br/>
