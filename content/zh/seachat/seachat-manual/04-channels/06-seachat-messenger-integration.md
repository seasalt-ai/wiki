---
title: "Facebook Messenger"
description: "利用本指南或YouTube視頻教程，探索如何將SeaChat AI助理集成到Facebook Messenger，設置自動回應，並管理真人客服交接。"
date: 2024-04-22T08:48:57+00:00
lastmod: 2024-04-22T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /zh/seachat/seachat-manual/04-channels/06-seachat-messenger-integration/
url: /zh/seachat/manual/channels/facebook-messenger/  
weight: 302
toc: true
---

## 🎥 影片教學

<iframe width="100%" height="400" src="https://www.youtube.com/embed/aFruY5bwG00?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


## 簡介
在這教學中，我們將深入探討在Facebook Messenger上設置由ChatGPT驅動的聊天機器人（AI助理）的過程。從本教學，您將清楚了解如何：
1. **自動回App戶消息**：
- 將您的Messenger商業帳號連接到SeaChat聊天機器人/AI助理平台。
- 使用ChatGPT等先進大語言模型訓練聊天機器人，以生成對廣泛用戶查詢的自然語言回應。
- 配置聊天助理，根據您的知識庫自動回應訊息。
2. **通過SeaChat管理所有與用戶的對話**：
- 使用SeaChat，掌握用戶和您的聊天機器人之間的所有對話。
- 查看聊天記錄，分析用戶行為，並識別聊天助理回應中的需要改進的部分。
- 管理對話，確保與用戶的無縫溝通。
3. **用戶能夠請求真人客服協助**：
- 允許用戶在他們有更進階需求或需要個性化支援時請求真人客服的協助。
- 順暢地將對話從AI聊天助理轉移到真人客服。
- 用戶可選擇他們需要的客服支援層級，增強整體客戶體驗。

到本教學結束時，您將擁有一個由SeaChat驅動的Facebook Messenger機器人以及一個SeaChat控制台來查看所有消息，如下所示：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/facebook-messenger-integration.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/facebook-messenger-integration.png" alt="SeaChat | Messenger | Facebook Messenger集成">
</a>
    <p style="margin-top: 20px; font-size: 15px">使用SeaChat的ChatGPT驅動的聊天機器人與Facebook Messenger集成</p>
</div>
</div>

<br/>

在開始設置過程之前，有幾個關鍵點需要記住：

**Messenger的限制**：
- SeaChat AI助理設計只能回應訊息，不能自行主動開始對話。
- 作為SeaChat管理員的您仍然能夠與用戶進行對話，但請事先安排真人助理。

**誰需要Messenger頻道**：
- 需要自動化處理大量Messenger訊息的企業和組織。
- 尋求提供個性化和更好客戶體驗的公司。
- 通過自動化常規查詢來減輕人力負擔的客戶服務部門。

---

## Facebook Messenger設置
設置Facebook Messenger需要仔細照著以下步驟設定，往下滑可看到逐步詳細指南：

1. **[創建MessengerApp](###創建Facebook-MessengerApp)**:
- 轉到Meta Developer網站。
- 點擊右上角的**MyApps**。
- 從下拉選單選擇**CreateApp**。

2. **[選擇App類型](###選擇App類型)**:
- 在**App Type**下選擇**Other**。
- 輸入一個全新的App名稱，避免使用**MessengerApp**或**Facebook**等難以辨識的名稱。

3. **[添加Messenger產品](###添加Messenger產品)**:
- 滾動到App列表的底部。
- 找到**Messenger**並選擇它以將該產品添加到您的App中。

5. **[配置MessengerApp](#如何配置messengerapp)**:
- 仔細閱讀配置頁面上的信息。
- 按照指示提供必要的細節，例如商業名稱、地址和聯繫信息。
- 確保正確填寫所有必填欄位。

6. **[生成訪問金鑰](#步驟2生成訪問金鑰)**:
- 配置完成後，生成一個永久的訪問金鑰。
- 此金鑰對於使用Messenger API至關重要。

7. **[移除您的Messenger集成](#移除您的messenger集成)**:
- 從您的MetaApp中正確移除頁面訪問權限
- 在SeaChat內點擊移除按鈕

> :books: **推薦閱讀**:
>
> 記得遵守[Messenger API](https://developers.facebook.com/docs/messenger/)政策和指南，以維持合規並避免任何潛在問題。

以下將逐步引導您完成過程並配上詳細操作指南：

### 創建Facebook MessengerApp

您首先需要前往[Meta Developer網站](https://developers.facebook.com/)，點擊右上角的**我的App**，然後從下拉選單中選擇**創建App**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/facebook-messenger/create-new-messenger-app.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/create-new-messenger-app.png" alt="SeaChat | Messenger | 創建新的Messenger App">
    </a>
<br/>
    <p style="margin-top: 20px; font-size: 15px">創建新的Messenger App</p>
</div>
</div>

### 選擇App類型

創建一個**Other** App，因為我們將僅使用此App來訪問您的Messenger帳戶。在**Selectapp type page**上，選擇**Business**作為類型，然後點擊**Next**。

<br/>
<div style="display: flex; flex-direction: column; align-items: center;">
    <div style="width: 100%; height:100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-1.png" alt="SeaChat | Messenger | 創建一個 Other App">
        </a>
        <p style="margin-top: 20px; font-size: 15px">創建一個 <strong>Other</strong> app</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-2.png" alt="SeaChat | Messenger | 選擇Business">
        </a>
        <p style="margin-top: 20px; font-size: 15px">選擇<strong>Business</strong></p>
    </div>
</div>

<br/>

在這裡，我們創建了一個名為**Seasalt.aiApp**的App，請注意，Meta不允許App名稱中包含**Facebook**或**Messenger**。在選擇App名稱時，請仔細閱讀警告消息。

<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-3.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-3.png" alt="SeaChat | Messenger | 創建App">
        </a>
        <p style="margin-top: 20px; font-size: 15px">創建App</p>
    </div>
<br/>

### 添加Messenger產品

創建App後，讓我們添加[Messenger產品](https://developers.facebook.com/docs/messenger/)。在**Add products to yourapp**部分下找到Messenger框，並點擊**Set up**以創建您的App。

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/facebook-messenger/add-messenger-product.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/add-messenger-product.png" alt="SeaChat | Messenger | 將Messenger添加到您的App<">
    </a>
<br/>
    <p style=" font-size: 15px">將Messenger添加到您的App</p>
</div>
</div>


## 如何配置MessengerApp
> :rotating_light: **警告** :rotating_light:
>
> 這裡的事情可能會變得有些複雜。如果您不夠小心並且錯過了一步，可能無法成功配置您的MessengerApp。所以，讓我們一起仔細地遍歷以下指示。

### 步驟1：配置Webhooks

在左側的**Messenger**下找到**Messenger API**。從這裡，我們首先需要配置Webhook和SeaChat提供的金鑰。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-1.png" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-1.png" alt="SeaChat | Messenger | Verify token">
    </a>
<br/>
    <p style=" font-size: 15px">Verify token</p>
</div>
</div>


您只需要做以下操作。前往SeaChat，導航至**Agent Configuration → Channels → Messenger**以獲取**Callback URL**和**Verify token**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-2.png" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-2.png" alt="SeaChat | Messenger | 導航至SeaChat的Messenger">
    </a>
<br/>
    <p style=" font-size: 15px">導航至SeaChat的<strong>Messenger</strong></p>
</div>
</div>
``
將SeaChat的步驟1的信息複製並貼上到Messenger儀表板的相應部分。


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-3.png" alt="SeaChat | Messenger | 將SeaChat信息配置到儀表板">
</a>
    <p style="margin-top: 20px; font-size: 15px">將SeaChat信息配置到儀表板</p>
</div>
</div>

<br/>

將**Callback URL**和**Verify token**貼上到Messenger儀表板的相應字段中：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-4.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-4.png" alt="SeaChat | Messenger | 貼上URL和金鑰">
</a>
    <p style="margin-top: 20px; font-size: 15px">貼上URL和金鑰</p>
</div>
</div>

<br/>

之後，我們需要正確配置**Webhook Fields**，以授予webhook回調URL適當的權限：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-5.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-5.png" alt="SeaChat | Messenger | Webhook Fields配置">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Webhook Fields</strong>配置</p>
</div>
</div>

<br/>

選擇**messages**並點擊**Subscribe**：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-6.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-6.png" alt="SeaChat | Messenger | 訂閱選擇的消息">
</a>
    <p style="margin-top: 20px; font-size: 15px">訂閱選擇的消息</p>
</div>
</div>

<br/>

您的webhook最終配置應如下所示：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-7.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-7.png" alt="SeaChat | Messenger | Webhook配置">
</a>
    <p style="margin-top: 20px; font-size: 15px">Webhook配置</p>
</div>
</div>

<br/>

### 步驟2：生成訪問金鑰

MetaApp需要訪問某個Facebook頁面，以便能夠接收從該頁面發送的消息。因此，在步驟2中，您首先需要授權它訪問您的公共Facebook頁面。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-1.png" alt="SeaChat | Messenger | 生成訪問金鑰">
</a>
    <p style="margin-top: 20px; font-size: 15px">生成訪問金鑰</p>
</div>
</div>

<br/>

在授權Facebook頁面後，您可以進一步**Add Subscriptions**：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-2.png" alt="SeaChat | Messenger | 添加訂閱">
</a>
    <p style="margin-top: 20px; font-size: 15px">點擊<strong>添加訂閱</strong></p>
</div>
</div>

<br/>

同樣，我們要訂閱**messages**：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-3.png" alt="SeaChat | Messenger | 選擇messages">
</a>
    <p style="margin-top: 20px; font-size: 15px">選擇<strong>messages</strong></p>
</div>
</div>

<br/>

最後，讓我們生成訪問金鑰：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-4.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-4.png" alt="SeaChat | Messenger | 金鑰生成">
</a>
    <p style="margin-top: 20px; font_size: 15px">金鑰生成</p>
</div>
</div>

<br/>

一旦生成了金鑰，我們需要複製該金鑰：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-5.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-5.png" alt="SeaChat | Messenger | 金鑰詳情">
</a>
    <p style="margin-top: 20px; font-size: 15px">金鑰詳情</p>
</div>
</div>

<br/>

將其貼上到SeaChat Messenger設置的第二步：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-6.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-6.png" alt="SeaChat | Messenger | 將金鑰貼上到SeaChat">
</a>
    <p style="margin-top: 20px; font-size: 15px">將金鑰貼上到SeaChat</p>
</div>
</div>

<br/>

現在將您的App模式設為**Live**，您就可以與機器人對話了：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a id="live-mode" href="/images/seachat/en/channels/facebook-messenger/access-token-7.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-7.png" alt="SeaChat | Messenger | "真人模式>
</a>
    <p style="margin-top: 20px; font-size: 15px">真人模式</p>
</div>
</div>

<br/>

### 步驟3：替代完成App審查

到目前為止，您的Messenger機器人只會對您這位App創建者做出回應。如果您將其交給其他人，他們將得不到任何回應。按照Facebook的指示完成“步驟3. 完成App審查”可能很誘人：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/app-review-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/app-review-1.png" alt="SeaChat | Messenger | App審查">
</a>
    <p style="margin-top: 20px; font-size: 15px">App審查</p>
</div>
</div>

<br/> 

然而，完成App審查可能需要多達5天的時間，而且過程非常繁瑣。例如，Meta會要求您錄製MetaApp的影片演示。

替代方法是將頁面分配給您在Meta擁有的業務。為此，前往[Meta商業套件](https://business.facebook.com/)，選擇您創建MetaApp的業務，然後轉到**Accounts** → **Pages**，並確保您的聊天機器人連接的Facebook頁面出現在那裡：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/facebook-pages.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/facebook-pages.png" alt="SeaChat | Messenger | Facebook頁面">
</a>
    <p style="margin-top: 20px; font-size: 15px">確保Facebook頁面在您的業務下顯示
</p>
</div>
</div>

<br/> 

您現在應該已經全部設置完成了！

# 與真人助理互動
您是否注意到在上圖中我使用了`/live_agent`來請求真人助理？如果助理恰好在線並設置了他們的在線狀態：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 40%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" alt="SeaChat | Messenger | 真人助理狀態">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理狀態
</p>
</div>
</div>

<br/> 

他們可以直接與用戶對話！

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" alt="SeaChat | Messenger | 真人助理互動">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理互動
</p>
</div>
</div>

<br/> 

如果助理不在線，他們可以開啟電子郵件通知以在用戶發起聊天或請求真人助理時收到當時的電子郵件：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" alt="SeaChat | Messenger | 真人助理偏好">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理偏好
</p>
</div>
</div>

<br/> 

## 移除您的Messenger集成

如果您想要移除Messenger集成，您需要在兩個地方進行操作：
1. 從您的MetaApp中正確移除頁面訪問權限
2. 在SeaChat內點擊移除按鈕

對於第1步，請前往您的**[Meta商業App](https://developers.facebook.com/)** → **Messenger** → **Messenger API Settings** → **Generate access tokens** → 移除

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" alt="SeaChat | Messenger | 移除集成">
</a>
    <p style="margin-top: 20px; font-size: 15px">移除集成</p>
</div>
</div>

<br/> 


## 回應語音剪輯
您知道SeaChat也支持語音消息嗎？如果用戶發送語音剪輯，SeaChat可以將其轉錄為文字，並通過文字回應！

目前，它支持英語語音到文字轉錄，但如果您需要更多語言支持，請告訴我們。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" alt="SeaChat | Messenger | 語音剪輯轉錄和SeaChat回應">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Facebook Messenger語音剪輯轉錄和SeaChat回應</strong></p>
</div>
</div>

<br/> 

## Messenger 的訊息回傳 (Postback)
當你設定好 Messenger 的整合後，你就可以使用 SeaChat 的[按鈕功能](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/webpage-link/)來與客戶互動。這允許你在答案中以按鈕的形式加入網址或其他附加資訊。

要啟動此功能，請進入 Messenger 的 **Edit Page Subscription** 頁面。


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" alt="SeaChat | Messenger | Edit Page Subscription">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Edit Page Subscription</strong></p>
</div>
</div>

<br/> 

### Messenger 按鈕限制

按照上述步驟操作後，你現在可以在整合後的 Messenger 中使用 SeaChat 的按鈕功能。然而，由於我們仍在使用 Messenger 提供的 API，因此在建立按鈕時有一些限制需要注意，以避免任何問題。

以下是限制條件：

兒每個訊息範本最多允許**3個回傳按鈕**。
- 每個按鈕的回傳資料最多可達**1000個字元**，按下時將傳送回你的webhook。
- 按鈕標題限制為**20個字元**。
- 這些限制適用於每個按鈕，因此你可以每個訊息擁有 3 個按鈕，每個按鈕擁有各自的 1000 字元回傳資料與 20 字元的標題。
- [開發者文件](https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback)

用戶可以使用 SeaChat 的 **[KB ID](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/webpage-link/#kb-id)** 功能，來改善這些限制所帶來的不便，請參閱連結以獲取更多資訊。

## :dart: 故障排除

如果您沒有收到來自SeaChat助理的Messenger回應，您應該驗證以下容易被忽略的設置：
- 您的MessengerApp是否已設置為[**真人模式**](#live-mode)？確保它不是在開發模式下運行。
- 您是否配置了[**webhook字段**](#perma-token-webhook)以允許**消息權限**？如果未正確授予此權限，SeaChat將無法接收來自Messenger的消息。


## 支持
需要協助？聯繫我們：[seachat@seasalt.ai](mailto:seachat@seasalt.ai).

