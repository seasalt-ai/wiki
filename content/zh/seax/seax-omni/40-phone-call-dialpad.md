---
title: "SeaX 撥號盤的來電/去電功能"
description: "使用 SeaX 撥打和接聽電話：VoIP, Twilio, SIP, PSTN"
date: 2025-06-24T08:48:57+00:00
lastmod: 2025-06-24T08:48:57+00:00
draft: false
images: []
menu:
  seax:
    parent: "seax-omni"
url: /zh/seax/seax-omni/phone-call-dialpad/
weight: 40
toc: true
---

SeaX 提供完整聯絡中心解決方案，讓你透過整合式撥號盤介面處理來電與去電。此功能補足 SeaX 既有的大型外撥活動、WhatsApp 訊息與 SMS 通訊能力。

## 🎥 撥號盤操作影片教學

完整影片教學將逐步展示如何設置與使用 SeaX 進行電話，包括由真人代理處理的去電與來電。

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/1luD3EFnIu4?list=PL8K7_LTqly45pLJ1NAw3P3VlPseovylOC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


**涵蓋重點功能：**
- ✅ 撥號盤設置與設定
- ✅ 來電處理
- ✅ 去電管理
- ✅ AI 代理整合
- ✅ 多代理輪詢分配
- ✅ 聯絡人管理與通話紀錄



### 先決條件

在使用撥號盤功能前，請確保：
- 已啟用 SeaX 工作區
- 已設定可語音通話的電話號碼
- 已正確設置音訊裝置（麥克風與喇叭）
- 代理狀態設為「可用」

### 撥號盤設置

#### 代理設定

1. **進入撥號盤**：進入 SeaX 工作區並找到撥號盤介面
2. **設置代理狀態**：將狀態切換為「可用」以接聽來電
3. **音訊裝置設定**：
   - 選擇偏好的喇叭（電腦或外接裝置）
   - 選擇麥克風輸入
   - 通話前測試音訊設定

#### 電話號碼設定

1. **進入號碼管理**：前往 **Workspace > Numbers** 查看可用號碼
2. **確認語音啟用**：確保號碼已啟用語音（會看到 SMS、MMS 與電話選項）
3. **檢查號碼類型**：SeaX 支援多種號碼類型，包括：
   - 支援 WhatsApp 的號碼
   - 支援舊式 PSTN 的 SIP trunk
   - 支援 SMS/MMS 的標準號碼

### 處理來電

#### 接聽來電

當有來電時：
1. 你會聽到來電通知
2. 點擊瀏覽器介面上的按鈕接聽
3. 通話中如需 IVR 可用螢幕上的數字鍵盤

#### 通話管理功能

- **通話紀錄**：可查詢所有來電與去電詳細紀錄
- **聯絡人整合**：已儲存聯絡人的號碼會顯示姓名
- **多通道整合**：同一號碼可用於語音與 WhatsApp

### 撥打去電

#### 手動撥號

1. **開啟撥號盤**：進入撥號盤介面
2. **搜尋聯絡人**：使用搜尋功能找現有聯絡人
3. **選擇號碼**：如有多個號碼可選擇
4. **發起通話**：點擊開始去電

#### AI 協助撥號

SeaX 支援 AI 代理協助去電：
1. **選擇 AI 代理**：從 SeaChat 設定的語音 AI 代理中選擇
2. **輸入目標號碼**：輸入收件人電話
3. **啟動 AI 撥號**：AI 代理會自動撥打
4. **應用場景**：適用於面試、預約、回訪等

### 進階設定

#### 號碼分配

每個號碼可設定：
- **多代理分配**：多位代理共同處理同一號碼來電
- **預設來電代理**：可設定由真人或 AI 處理來電
- **通道專屬設定**：SMS 與語音可分別指定不同代理

#### 輪詢分配系統

多代理分配時：
- 來電會以輪詢方式分配給可用代理
- 每位代理響鈴 10 秒後轉給下一位
- 系統優先分配給「最閒」的代理
- 若無真人代理，來電可自動轉給 AI

### 與其他 SeaX 功能整合

撥號盤功能可無縫整合：
- **大規模外撥活動**
- **WhatsApp Business 訊息**
- **SMS/MMS 通訊**
- **SeaChat AI 全通道支援**

### 最佳實踐

1. **代理狀態**：隨時更新狀態以確保正確分配來電
2. **音訊品質**：建議使用高品質耳麥
3. **聯絡人管理**：保持聯絡人名單最新，提升外撥效率
4. **AI 備援**：設定 AI 代理作為真人代理的備援
5. **通話紀錄**：定期檢視通話紀錄以優化表現

### 疑難排解

**常見問題：**
- **回音問題**：調整麥克風與喇叭設定避免回音
- **漏接來電**：確認代理狀態為「可用」並開啟通知
- **號碼設定**：於號碼管理確認號碼已啟用語音

此撥號盤功能讓 SeaX 成為完整的人機協作聯絡中心，實現自動化活動與個人化互動的無縫切換。

## 📷 撥號盤圖文教學

### 概覽

SeaX 將內外部電話通訊整合於單一平台。在此平台你可以：

**撥打與接聽電話**

* 直接搜尋或輸入號碼即可撥打電話  
* 不需切換應用程式即可接聽來電  
* 可選擇不同外撥號碼或讓 AI 代理處理

**通話管理**

* 所有來電、去電與未接來電自動記錄  
* 已儲存聯絡人於通話紀錄中顯示姓名  
* 可搜尋通話紀錄以追蹤或查詢歷史

**聯絡人管理**

* 匯入與匯出聯絡人清單  
* 每位聯絡人可設定多個標籤  
* 依標籤分組方便管理

### 撥號盤通話

SeaX 內建撥號盤，讓用戶可直接於平台撥打與接聽電話，無需外接裝置或應用程式。

#### 如何撥打去電

點擊右上角撥號盤圖示開啟撥號盤。可手動輸入號碼或搜尋姓名／號碼快速撥號。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/1-dialpad.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/1-dialpad.png" alt="SeaX | Dialpad">
</a>

*SeaX Dialpad*
</center>


#### 如何接聽來電

有來電時，右上角會出現通知卡片。點擊即可接聽或拒接。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/2-dialpad-inbound-call.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/2-dialpad-inbound-call.png" alt="SeaX | Dialpad Inbound Call">
</a>

*SeaX Dialpad Inbound Call*
</center>


#### 切換 AI agent 進行通話

點擊撥號盤上的箭頭可選擇 AI Agent，然後輸入或搜尋聯絡人號碼進行撥號。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/3-dialpad-ai-agent.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/3-dialpad-ai-agent.png" alt="SeaX | Dialpad Calling with an AI Agent">
</a>

*SeaX Dialpad Calling with an AI Agent*
</center>


#### 通話紀錄總覽

所有來電與去電都會記錄於左側通話紀錄面板，可依時間、時長、聯絡人等條件查詢。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/4-call-logs.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/4-call-logs.png" alt="SeaX | Dialpad Call Logs">
</a>

*SeaX Dialpad Call Logs*
</center>


### 代理狀態設定

SeaX 提供狀態切換功能，代理可自行控制可用性，系統會依據狀態分配來電。

狀態類型

* 可用  
* 離開  
* 勿擾  
* 離線  
* 通話中

#### 如何切換狀態

1. 登入 SeaX 後點擊右上角個人頭像

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/5-status-menu.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/5-status-menu.png" alt="SeaX | Dialpad Status Menu">
</a>

*SeaX Dialpad Status Menu*
</center>


2. 找到顯示目前可用性的狀態面板

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/6-status-menu-open.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/6-status-menu-open.png" alt="SeaX | Dialpad Status Menu Open">
</a>

*SeaX DialpadStatus Menu Open*
</center>


3. 點擊目前狀態可查看所有選項（可用、離開、勿擾、離線），選擇後 SeaX 會立即更新。

#### 狀態說明：

在線：綠色 – 可接聽來電  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/7-status-available.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/7-status-available.png" alt="SeaX | Dialpad Status Green">
</a>

*SeaX 撥號盤狀態：在線*
</center>


離開：橘色 – 不會分配新來電  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/8-status-away.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/8-status-away.png" alt="SeaX | Dialpad Status Away">
</a>

*SeaX 撥號盤狀態：離開*
</center>


請勿打擾：紅色 – 不會分配新來電  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/9-status-do-not-disturb.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/9-status-do-not-disturb.png" alt="SeaX | Dialpad Status: DND">
</a>

*SeaX 撥號盤狀態：請勿打擾*
</center>

離線：灰色 – 完全離線  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/10-status-offline.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/10-status-offline.png" alt="SeaX | Dialpad Status: Offline">
</a>

*SeaX 撥號盤狀態：離線*
</center>

通話中，系統將自動切換狀態為「通話中」，結束後自動恢復至先前狀態。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/11-status-in-the-call.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/11-status-in-the-call.png" alt="SeaX | Dialpad Status: On A Call">
</a>

*SeaX 撥號盤狀態：通話中*
</center>


### 認識循環響鈴

當用戶在 **號碼** 設定處，將進線電話預設接收人切換至人工客服後，SeaX 將依照以下規則，及客服狀態設定進行響鈴分配：

響鈴分配原則

* 僅對號碼成員中狀態為「在線」的人員進行響鈴。  
* 系統會依照客服的狀態與活躍時間，排序人員進行響鈴。  
* 每位客服都會依序被嘗試響鈴 10 秒，直到有人接聽為止。  
* 每輪響鈴會略過上一輪響過但未接聽的人，改由其他人接續。

並請注意，當只有一位客服在線時，並響鈴未接起後，系統將自動播放「客服皆忙線中」，並結束通話。