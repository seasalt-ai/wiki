---
title: "來電轉接"
description: "SeaChat 來電轉接教學"
lead: ""
date: 2024-10-03 10:43:51.069 +0100
lastmod: 2024-10-04 10:43:51.069 +0100
draft: false
images: []
weight: 401
---


---

以下是上述18分鐘教程的視頻，無需編程技能即可部署AI語音助理：

<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/Hh04t_Qg8-I" title="YouTube Video Player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## 來電轉接簡介及運作原理

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/inbound-voice-agent/call-forwarding/call-forwarding-diagram.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; background-color: #ffffff" src="/images/seachat/zh/inbound-voice-agent/call-forwarding/call-forwarding-diagram.png" alt="來電轉接示意圖">
</a>

**來電轉接**
</center>

來電轉接是一種電信功能，允許用戶將來電從一個號碼轉接到另一個號碼。這確保即使您無法接聽主要電話時，重要的電話也不會錯過。來電轉接主要有兩種類型：無條件來電轉接，即轉接所有來電，和有條件來電轉接，即只在特定情況下（如忙線或無應答時）進行轉接。

通常，企業和個人偏好使用有條件來電轉接，確保只有在必要時才轉接來電，而不是每次來電都進行轉接。設置這項功能通常很簡單，不同的電信提供商和VoIP服務都提供簡單的方法來通過設置或在電話上撥打特定代碼來配置來電轉接。

---


## 將來電轉接到AI助理
一旦您在電信服務商處配置了來電轉接後，您可以通過將來電轉接到您的SeaChat語音助理來簡化您的應答服務。您的SeaChat助理可以幫助您管理預約，並在繁忙時段或您無法接聽時生成來電摘要。

以下教程將指導您完成所有必要步驟，以設置您的電話號碼來轉接到您的SeaChat助理。成功設置來電轉接後，您可以訪問我們的[wiki](https://wiki.seasalt.ai/zh/)或在Seasalt.ai的YouTube頻道上觀看我們的教程視頻，進一步了解如何將SeaChat的不同功能應用到您的生產環境中。

## 準備步驟
在進行來電轉接設置之前，讓我們確保AI助理已準備好接收來電。


- **步驟1** – **創建一個SeaChat助理**:
  - 如果這是您首次登錄SeaChat，您需要先創建一個新的助理才能繼續後續步驟。歡迎訪問我們的[wiki](https://wiki.seasalt.ai/zh/seachat/seachat-manual/02-create-agent/01-create-new-agent/)，以獲取更詳細的說明。
- **步驟2** – **部署語音AI助理**:
  - 我們需要為語音AI助理分配一個電話號碼，這樣我們才能將其部署到生產環境中進行來電應答。按照以下說明完成此步驟，或您可以查看我們的[wiki](https://wiki.seasalt.ai/zh/seachat/seachat-manual/04-channels/07-seachat-voicebot/)，以獲取更全面的指南——來電通道配置。
    - ***步驟2.1*** – ***導航到來電配置頁面***。
      - 在左側側邊欄中前往“Channel -> Calls”下的助理配置部分。
    - ***步驟2.2*** – ***購買一個免付費號碼並將AI助理部署到該號碼***。
      - 按照SeaChat UI上的步驟購買一個免付費號碼，該AI助理將部署到該號碼。
      - 配置AI助理並設置您希望助理具備的正確行為。
    - ***步驟2.3*** – ***測試您的AI助理***。
      - 您應該在將AI助理部署到生產環境之前進行測試。微調和調整助理的配置，以實現您需要的最佳性能。

  

