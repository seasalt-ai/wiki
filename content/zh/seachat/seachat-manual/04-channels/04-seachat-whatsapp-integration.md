---
title: "WhatsApp"
description: "利用Seasalt.ai的SeaChat平台解鎖WhatsApp自動化功能。透過整合ChatGPT驅動的聊天AI，輕鬆管理對話，並通過真人助理連接提升客戶支持。"
date: 2024-07-12T08:48:57+00:00
lastmod: 2024-07-12T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
   - /zh/seachat/seachat-integrations/whatsapp/
url: /zh/seachat/integrations/whatsapp/   
weight: 40
toc: true
---

## 🎥影片教學
<iframe width="100%" height="400" src="https://www.youtube.com/embed/?v=qpNlWtGP9jw&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

## 簡介
在本節中，我們將深入探討如何在**WhatsApp**上設置一個**ChatGPT**驅動的聊天機器人或聊天助理。完成本節後，您將清楚了解如何：
1. **自動回應用戶訊息**:
- 將您的**WhatsApp**企業帳戶連接到**SeaChat**助理平台。
- 使用**ChatGPT**的先進語言模型訓練AI助理，生成自然語言回應以應對各種用戶查詢。
- 配置聊天助理，根據您的知識庫自動回應來訊消息。
2. **通過SeaChat訪問所有與用戶的對話**:
- 使用**SeaChat**這個用戶友好的界面，訪問和監控用戶與您的AI助理之間的所有對話。
- 查看聊天記錄，分析用戶行為，識別聊天助理回應中的改進空間。
- 高效管理和組織對話，確保與用戶的無縫通信。
3. **允許用戶請求真人助理協助**:
- 實施特殊指令，讓用戶在遇到複雜查詢或需要個性化支持時請求真人助理的幫助。
- 將對話從AI聊天助理無縫轉移到真人助理，確保順利且高效的過渡。
- 賦予用戶選擇所需支持級別的權利，提升整體客戶體驗。

在開始設置過程之前，請記住以下幾點關鍵：

**WhatsApp Business App限制**:
- 一旦您將**SeaChat**與**WhatsApp**集成，您將無法再使用常規的**WhatsApp Business App**。
- **SeaChat AI**助理僅設計用於回應來訊消息，無法自行發起對話。
- 不過，作為助理創建者，一旦請求真人助理，您仍然可以與用戶對話。

**誰能從此集成中受益**:
- 擁有大量來訊**WhatsApp**消息並需要自動化的企業和組織。
- 希望提供個性化和引人入勝的客戶支持體驗的公司。
- 希望通過自動化常規查詢來減輕真人助理負擔的客戶服務部門。
---

## WhatsApp 設定
在有正確指引的情況下，設定**WhatsApp**可以是一個簡單的過程。以下是步驟的簡短版本。你也可以點擊標題來查看每個步驟的詳細說明：

1. **[建立 WhatsApp 應用](#create-a-whatsapp-app)**:
- 前往**Meta Developer Site**。
- 點擊右上角的**My Apps**。
- 從下拉選單中選擇**Create App**。

2. **[選擇應用類型](#choose-app-type)**:
- 在**App Type**下選擇**Other**。
- 輸入一個獨特的應用名稱，避免使用**WhatsApp**在名稱中。

3. **[添加 WhatsApp 產品](#add-whatsapp-product)**:
- 向下滾動到應用列表底部。
- 找到**WhatsApp**並選擇它來添加產品到你的應用。

4. **[連接到企業](#connect-to-business)**:
- 將**WhatsApp**應用與你的企業關聯。
- 這一步是利用**WhatsApp Business Platform API**所必需的。

5. **[配置 WhatsApp 應用](#configure-whatsapp-application)**:
- 仔細檢查配置頁面上的信息。
- 按照說明提供必要的詳細信息，如企業名稱、地址和聯繫信息。
- 確保所有必填字段都正確填寫。

6. **[生成訪問token](#lets-set-up-a-permanent-token)**:
- 完成配置後，生成一個永久訪問token。
- 此token對使用**WhatsApp Business API**至關重要。

7. **[測試和發布](#test-your-seachat-agent-via-whatsapp)**:
- 測試你的**WhatsApp**應用以確保其按預期工作。
- 根據測試結果進行必要的調整。
- 一旦對性能滿意，公開發布你的應用。

8. **[移除訊息整合](#remove-your-whatsapp-integration)**:
- 正確移除你的**Meta**應用中的頁面訪問
- 點擊**SeaChat**內的移除按鈕

> :books: **推薦閱讀**:
>
> 記得遵守[**WhatsApp Business API**](https://developers.facebook.com/docs/whatsapp/)的政策和指南，以保持合規並避免潛在問題。

以下將逐步引導你完成過程的詳細說明：

### 建立 WhatsApp 應用

首先，您需要前往 [Meta Developer Site](https://developers.facebook.com/) 並點擊右上角的 **My Apps**，然後從下拉選單中選擇 **Create App**，來建立一個新的 WhatsApp 應用。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/channels/whatsapp/create-new-whatsapp-app.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/create-new-whatsapp-app.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">創建新的 WhatsApp</p>
</div>
</div>

### 選擇應用類型
建立一個 **Other** 應用，因為我們只使用這個應用來訪問您的 WhatsApp 帳戶。在 **Select app type page** 頁面上，選擇 **Business** 類型，然後點擊 **Next**。

<br/>
<div style="display: flex; flex-direction: column; align-items: center;">
    <div style="width: 100%; height:100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/choose-app-type-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/choose-app-type-1.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">創建 <strong>Other</strong> app</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/choose-app-type-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/choose-app-type-2.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">填寫 App Details</p>
    </div>
</div>

<br/>

這裡我們創建了一個名為 **Seasalt.ai WA** 的應用，請注意 Meta 不允許應用名稱中包含 **WhatsApp**。



### 新增 WhatsApp 產品

建立應用後，讓我們新增 WhatsApp 產品。在 **Add products to your app** 區域下找到 WhatsApp 框，然後點擊 **Set up** 來建立您的應用。

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/channels/whatsapp/whatsApp-integration.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/whatsApp-integration.svg" alt="">
    </a>
    <p style=" font-size: 15px">新增 WhatsApp 到您的 App</p>
</div>
</div>

### 連接到企業帳戶
WhatsApp 應用需要與您的企業相關聯，因為它需要使用 [WhatsApp Business Platform API](https://developers.facebook.com/docs/whatsapp/)。選擇一個企業投資組合並點擊繼續。回到您的應用儀表板，您應該會看到已添加的 WhatsApp 產品。點擊 **Start using the API** 開始配置。

<br/>
<div style="display: flex; flex-direction: column; align-items: flex-start;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/connect-to-business-1.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/connect-to-business-1.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">選擇 Business Portfolio</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/connect-to-business-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/connect-to-business-2.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">點擊 <strong>Start Using the API</strong></p>
    </div>
</div>


## 如何配置 WhatsApp 應用程式
> :rotating_light: **警告** :rotating_light:
>
> 這部分會比較複雜。如果您不夠小心並且漏掉某個步驟，可能無法成功配置您的 WhatsApp 應用程式。所以，讓我們一起仔細地進行以下說明。

如果您從上方點擊 **Start using the API**，它會將您帶到如下的 **API Setup**。但是，我們不需要過多關注這裡的信息。真正重要的是 **Step 3: Configure webhooks**。

<br/>
<div style="display: flex; flex-direction: column; align-items: center; justify-content: space-between">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-1.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">API 設置</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-2.svg" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-2.svg" alt="">
        </a>
        <p style="font-size: 15px"><strong>配置 Webhooks</strong></p>
    </div>
</div>

這會將您帶到左側的 **Configuration** 下的 **WhatsApp**。從這裡，我們首先需要配置由 SeaChat 提供的 Webhook 和 token。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-3.svg" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-3.svg" alt="">
    </a>
    <p style=" font-size: 15px">配置儀表板</p>
</div>
</div>

<br/>

對於 Webhook 的配置，我們會參考上圖中的 **Step 1**。這是您需要做的所有事情。前往 SeaChat，導航到 **Agent Configuration → Channels → WhatsApp** 來獲取 **Callback URL** 和 **Verify token**。

複製 SeaChat 的 Step 1 並將其貼上到 WhatsApp 儀表板上的相應部分，如下圖所示。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-4.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-4.svg" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">複製 SeaChat 內容並貼上至 Webhook 配置</p>
</div>
</div>

<br/>

> :point_down: **不要忘記使用設定的 Webhook 欄位！** :point_down:
>
> 我們需要給 API 訊息許可權，這樣 SeaChat 助理才能接收來自 WhatsApp 的任何傳入訊息。
>
>
> <div style="display: flex; flex-direction: column; align-items: center;">
> <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
>   <a href="/images/seachat/zh/channels/whatsapp/dont-forget-to-use-set-Webhook-fields.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank"><img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/dont-forget-to-use-set-Webhook-fields.svg" alt=""></a>
>     <p style="margin-top: 10px; font-size: 15px">Webhook 欄位</p>
> </div>
> </div>
>



### 設置一個永久 token

[Step 2](#perma-token-webhook) 是獲取一個 **WhatsApp Access Token** 並將其傳遞給 SeaChat。

您可能在 API 設置中見過臨時訪問 token：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
 <a href="/images/seachat/zh/channels/whatsapp/permanent-token-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/permanent-token-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Temporary Access Token</p>
</div>
</div>

<br/> 

<p>:point_up: 如 Meta 所述，此 token 僅有效 24 小時。所以我們不使用它。</p>

<br/> 



### 1. 創建系統用戶

您應該通過生成一個 [System User Access Token](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) 來獲取永久 token。

以下是創建系統用戶的步驟：

1. 登錄 [Meta Business Suite](https://business.facebook.com/)。
2. 在左上角下拉選單中找到您的業務帳戶並點擊其 **Settings**（齒輪）圖標。
3. 點擊 **Business settings**。
4. 導航到 **Users** → **System users**
5. 點擊 **Add** 按鈕，創建一個 admin 或 employee 系統用戶。


### 2. 生成系統用戶訪問 token

創建系統用戶後，生成系統用戶訪問 token：

1. 登錄 [Meta Business Suite](https://business.facebook.com/)。
2. 在左上角下拉選單中找到您的業務帳戶並點擊其 **Settings**（齒輪）圖標。
3. 點擊 **Business settings**。
4. 導航到 **User** → **System** 用戶。
5. 從系統用戶列表中選擇適當的系統用戶。
6. ~~點擊生成新 token 按鈕~~。→ **暫不要這樣做**。請參閱下文 [Assign Assets](#assign-assets)。
7. 選擇將使用 token 的應用。
8. 選擇應用正常運行所需的任何許可權並生成 token。

##### Assign Assets
我們在第 6 步停止，因為您需要先將您的 WhatsApp 應用指定為 **Asset** 以獲取正確的 token 範圍。請按照以下步驟將您的 WhatsApp 應用指定為 Asset：

1. 在 System Users 中，點擊 [**Assign Asset**](#assign-assets-step-1)。
2. 然後轉到 **Apps** 並選擇您創建的應用，並賦予其 [**Full control**](#assign-assets-step-2)。
3. 點擊 **Generate new token** 並選擇 ***whatsapp_business_messaging*** 和 ***whatsapp_business_management*** 在 **Permissions**。應如下圖所示 [this](#assign-assets-step-3)。
4. token 生成後，將彈出一個 [pop-up](#assign-assets-step-4) 顯示生成的 token 信息。複製 token。
5. 現在點擊 token，將打開 [**Access Token Debugger**](#assign-assets-step-5) 並顯示正確的 Scope。這裡您需要確保擁有 ***whatsapp_business_messaging*** 和 ***whatsapp_business_management***。
6. 複製並粘貼 token 到 [SeaChat](#assign-assets-step-6)。
7. 將您的 [**App Mode**](#assign-assets-step-7) 設置為 **Live**。
8. 通過返回 [**WhatsApp** →  **Configuration**](#assign-assets-step-8) 並將您的 WhatsApp 號碼添加到 WhatsApp 應用中。它應顯示至少一個生產號碼。

<div style="display: flex; flex-direction: column; width:100%  ; align-items: center;">
    <div id="assign-assets-step-1" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-1.svg" target="_blank" style=" width: 100%; height: 10%; display: flex; justify-content: center; align-items: center; overflow: hidden; padding: 0">
            <img style="max-width: 100%; max-height: 50%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-1.svg" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 1: 點擊 <strong>Assign Asset</strong></p>
    </div>
    <div id="assign-assets-step-2" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-2.svg" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-2.svg" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 2: 選擇 <strong>Full control</strong></p>
    </div>
</div>
<div id="assign-assets-step-3" style="display: flex; flex-direction: column; width:100%; align-items: center;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-3.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-3.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 3: <strong>Generate token</strong> 及設置 <strong>Permission</strong></p>
    </div>
    <div id="assign-assets-step-4" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-4.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-4.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 4: 複製 token</p>
    </div>
</div>
<div style="display: flex; flex-direction: column; width:100% ; align-items: center;">
    <div id="assign-assets-step-5" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-5.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-5.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 5: 開啟 <strong>Access Token Debugger</strong></p>
    </div>
    <div id="assign-assets-step-6" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-6.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-6.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 6: 將 token 貼上至 SeaChat</p>
    </div>
</div>
<div style="display: flex; flex-direction: column; width:100% ; align-items: center;">
    <div id="assign-assets-step-7" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-7.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-7.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 7: 將 <strong>App Mode</strong> 設定成 <strong>Live</strong></p>
    </div>
    <div id="assign-assets-step-8" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-8.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-8.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 8: 新增企業號碼</p>
    </div>
</div>


## 測試您的 SeaChat 助理通過 WhatsApp

終於設置完成了！一旦您的助理設置好後，試著發送幾條消息並期待 SeaChat 的回覆：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/test-whatsapp-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/test-whatsapp-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">WhatsApp 對話</p>
</div>
</div>

<br/> 

在 SeaChat 的 **Conversations** 視圖中，您可以看到相同的對話以及用戶/發送者的名字。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/test-whatsapp-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/test-whatsapp-2.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">SeaChat 對話</p>
</div>
</div>

### 正確設置您的 WhatsApp 商業帳戶

上述截圖顯示了一個非常基本的 WhatsApp 帳戶，甚至沒有個人資料圖片。在競爭激烈的數字環境中，擁有強大的在線形象對各種規模的企業都至關重要。WhatsApp 擁有龐大的用戶群和廣泛的知名度，為企業提供了一個強大的平台來與客戶聯繫。然而，有效地設置和管理 WhatsApp 商業帳戶可能是一項艱巨的任務。

管理 WhatsApp 商業帳戶的一個重要方面是正確設置個人資料。一個優化良好的個人資料能夠創造專業形象，建立信任，並提高可見度。不幸的是，許多企業忽視了個人資料設置的重要性，或難以找到正確的設置。

讓我們通過訪問 [Meta WhatsApp Business Manager](https://business.facebook.com/wa/manage) 來正確設置 WhatsApp 帳戶個人資料。或者，如果您仍在 Meta for Developers 網站，導航到 **WhatsApp → Quickstart → WhatsApp Business** 並點擊 **Account information**：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/deploy-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/deploy-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Account information</p>
</div>
</div>

<br/> 

這將帶您進入 **WhatsApp Business Manager** 下的正確帳戶。在這裡，您可以進行必要的更改，上傳個人資料圖片，並保存更新。這些更改可能需要幾分鐘才能生效。一旦生效，當您訪問 WhatsApp 商業帳戶的信息頁面時，您會注意到更新的個人資料信息。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/deploy-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/deploy-2.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">編輯帳戶</p>
</div>
</div>

<br/> 

幾分鐘後，如果您在手機上的 WhatsApp 應用中點擊您的 WhatsApp 商業帳戶的信息頁面，它將反映出這些更改：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/deploy-3.png" target="_blank">
<img width="50%" height="auto" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/deploy-3.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">WhatsApp Business Account Info</p>
</div>
</div>

<br/> 


優化您的 WhatsApp 商業個人資料不僅僅是添加個人資料圖片。以下是一些增強個人資料的額外提示：

2. **使用清晰專業的個人資料圖片**：
選擇能代表您的品牌或業務的高質量圖片。避免模糊或低解析度的圖片，因為它們會給人負面印象。

3. **添加相關聯絡信息**：
確保您的電話號碼、電子郵件地址和網站（如適用）在個人資料中顯眼顯示。這讓客戶可以通過他們喜歡的渠道輕鬆聯繫您。

4. **使用標籤和標記**：
使用標籤和標記來組織您的聯絡人和對話。這有助於您有效地分類和管理客戶互動，使您更容易跟踪和回應特定查詢或請求。

通過遵循這些提示，您可以正確地優化您的 WhatsApp 商業帳戶，創建專業的個人資料，並增強整體的客戶參與度。

# 與真人助理互動
您是否注意到在上面的圖片中我使用 /live_agent 來請求真人助理？如果助理通過設置他們的在線狀態在線：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/live-agent-status.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理狀態
</p>
</div>
</div>

<br/> 

他們可以直接與用戶對話！

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/live-agent-interaction.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent 互動
</p>
</div>
</div>

<br/> 

如果助理不在線，他們可以打開電子郵件通知，在用戶啟動聊天或請求真人助理時接收實時電子郵件：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/ai-agent-preference.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent 偏好設定
</p>
</div>
</div>

<br/>

## WhatsApp 的訊息回傳 (Postback)
當你設定好 Messenger 的整合後，你就可以使用 SeaChat 的[按鈕功能](https://wiki.seasalt.ai/zh/seachat/seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers/)來與客戶互動。這允許你在答案中以按鈕的形式加入網址或其他附加資訊。

現在，客戶可以點擊按鈕來獲取更多資訊或導航到網頁。

每次按鈕被點擊時，會觸發 SeaChat API 與 WhatsApp API 的訊息回傳。

### WhatsApp 按鈕限制
WhatsApp 對於訊息回傳有一些限制。請在創建按鈕時注意以下事項，以避免任何問題。

限制條件如下：

- WhatsApp 的訊息 API 支援每條訊息最多**3個互動按鈕**。
- 每個按鈕的文字（標題）限制為**20個字元**。
- 按鈕被點擊時傳送的回傳資料或回傳訊息限制為**200個字元**。
- 這些限制適用於每個按鈕，並非所有按鈕的總和。
- [開發者文件](https://developers.facebook.com/docs/whatsapp/guides/interactive-messages/)

[//]: # (用戶可以使用 SeaChat 的 **[KB ID]&#40;https://wiki.seasalt.ai/zh/seachat/seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers/#kb-id&#41;** 功能，來改善這些限制所帶來的不便，請參閱連結以獲取更多資訊。)


## 移除您的 WhatsApp 整合

如果您想移除 WhatsApp 整合，您需要在兩個地方進行操作：

1. 從您的 Meta 應用程式中正確移除 webhook
2. 點擊 SeaChat 內的移除按鈕

對於步驟 1，請前往您的 [Meta Business app](https://developers.facebook.com/) → WhatsApp → Configuration → Callback URL → Edit → Remove webhook

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/remove-app-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/remove-app-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">移除整合</p>
</div>
</div>

<br/>

## :dart: 疑難排解

如果您沒有收到來自 SeaChat Agent 在 WhatsApp 上的回應，您應該檢查用戶容易忽略的以下設置：
- 您是否使用了僅有效 24 小時的 **temporary access token**？應該使用系統用戶的 [**Permanent Access Token**](#1-creating-system-users)。
- 您的 WhatsApp 應用程式是否已設置為 [**Live mode**](#assign-assets)？確保它沒有在開發模式下運行。
- 您是否配置了 [**webhook fields**](#perma-token-webhook) 以允許 **message permission**？如果此權限未正確授予，SeaChat 將無法接收來自 WhatsApp 的消息。
- 您的 SeaChat agent 是否收到消息，但您無法在 WhatsApp 上看到回覆？這可能是因為在生成永久token時，您沒有先進行 [**Assign Assets**](#assign-assets)。

## 支援
需要幫助？請聯繫我們 [seachat@seasalt.ai](mailto:seachat@seasalt.ai)。


 
