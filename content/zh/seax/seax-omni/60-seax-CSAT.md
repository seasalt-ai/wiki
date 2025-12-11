---
title: "客戶滿意度（CSAT）調查"
description: "在所有連結頻道上配置、發送並解讀客戶滿意度（CSAT）調查，以衡量客戶體驗與客服人員表現。"
date: 2024-12-10T08:48:57+00:00
lastmod: 2024-12-10T08:48:57+00:00
draft: false
images: []
menu:
  seax:
    parent: "seax-omni"
aliases:
  - /zh/seax/csat/
  - /zh/seax/seax-messaging/csat/
url: /zh/seax/seax-omni/csat/
weight: 60
---

使用可自訂、可自動與可手動觸發的對話後調查，輕鬆蒐集可行回饋。

客戶滿意度（CSAT）調查能夠幫助您了解客戶對支援互動的感受。透過 SeaX，您可以設定自訂的 CSAT 訊息、讓客服人員在需要時手動發送，或依照您指定的規則自動發送。系統會智慧解析客戶回覆，確保蒐集回饋的流程順暢且不打擾對話體驗。

---

## 為什麼 CSAT 很重要

CSAT 調查能提供可量化的客戶體驗洞察。支援團隊可以藉由 CSAT：

- 追蹤滿意度的長期趨勢
- 找出低分對話與其根本原因
- 驅動人員訓練與品質改善
- 自動化蒐集回饋以降低手動工作量
- 依各頻道的訊息規範維持合規

---

## 在介面中設定 CSAT 的位置

1. 前往：**側邊選單 → 工作區（Workspace） → 頻道（Channels）**

2. 點擊頻道卡片，會開啟設定視窗，您可以在其中啟用 CSAT 設定。

CSAT 調查可用的頻道包含：LINE、WhatsApp、Instagram、Messenger。找不到您需要的頻道？歡迎聯絡我們的支援團隊：[info@seasalt.ai](mailto:info@seasalt.ai)。
<br/>

<center>
<a href="/images/seax/zh/csat/CSAT_Entry.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/zh/csat/CSAT_Entry.png" alt="顯示如何前往 CSAT 設定入口的畫面。">
</a>

</center>

<br/>

---

## 啟用與自訂 CSAT 調查

在頻道設定視窗內：

### 1. 啟用 CSAT

切換 **啟用客戶滿意度調查（Enable Customer Satisfaction Survey）**。

### 2. 撰寫 CSAT 訊息

輸入您希望客戶收到的調查訊息。

重要指引：

- 僅回覆 **1、2、3、4 或 5** 會被視為有效的 CSAT 評分。
- 訊息應清楚指示客戶以單一數字回覆。  
  範例：  
  「請以 1–5 的數字回覆，為本次服務評分。」
  <br/>

<center>
<a href="/images/seax/zh/csat/CSAT_Config_Manual.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/zh/csat/CSAT_Config_Manual.png" alt="顯示 CSAT 手動發送設定的畫面。">
</a>

</center>

<br/>

### 3. 儲存變更

完成儲存後，該頻道即可同時支援手動與自動發送 CSAT 調查。

## 手動發送 CSAT 調查

客服人員可以在對話進行期間的任何時間點發送 CSAT 調查。

操作方式：

1. 開啟某段對話
2. 點擊對話視窗 **右上角** 的 **CSAT 圖示**
   <br/>

<center>
<a href="/images/seax/zh/csat/CSAT_Send_Btn.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/zh/csat/CSAT_Send_Btn.png" alt="顯示手動發送 CSAT 按鈕位置的畫面。">
</a>

</center>

<br/>

### Meta 頻道限制

適用於 Instagram、Messenger 與 WhatsApp：

- 客戶必須在 **最近 24 小時** 內傳過訊息
- 超出 24 小時視窗時，CSAT 圖示會依 Meta 政策被 **停用**

您可以視需要多次手動發送 CSAT 調查。

---

## 自動發送 CSAT 調查

### 1. 啟用自動發送

切換 **在設定的延遲時間後自動發送調查（Automatically send the survey after a set delay）**。

### 2. 設定延遲時間

設定在 **客戶最後一則入站訊息** 之後，系統自動發送 CSAT 調查所需的等待分鐘數。

<br/>

<center>
<a href="/images/seax/zh/csat/CSAT_Config_Auto.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/zh/csat/CSAT_Config_Auto.png" alt="顯示 CSAT 自動發送設定的畫面。">
</a>

</center>

<br/>

### 自動發送的運作方式

- 每次收到入站使用者訊息後即啟動倒數計時
- 當延遲時間到達時，系統會自動發送調查
- 若客戶未以有效評分回覆，系統會在每個延遲視窗結束後 **重新嘗試發送**，並一律以最近一次入站訊息為基準
- 自動發送在每段對話中 **僅觸發一次**，但會持續重試直到收到有效評分
- 期間隨時可手動發送

---

# CSAT 回覆解析方式

了解系統如何讀取客戶回覆，有助於設定正確的期待值。

### 當 CSAT 調查被發送時：

系統會監控 **客戶下一則入站訊息**，並依下列規則解讀：

---

## 情境一: 客戶以有效評分（1–5）回覆

- 系統成功解析評分
- 評分會被記錄為 CSAT 分數
- 所有自動重發嘗試停止
- 後續訊息不再被視為 CSAT 回覆

<br/>

<center>
<a href="/images/seax/zh/csat/CAST_Send_Msg.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/zh/csat/CAST_Send_Msg.png" alt="顯示有效評分流程的示意畫面。">
</a>

</center>

<br/>

---

## 情境二: 客戶以無效訊息回覆

範例：

- 「謝謝！」
- 「好的。」
- 表情符號（Emoji）

系統行為：

1. 系統 **無法解析** 有效評分
2. 該訊息會被視為 **一般入站訊息**
3. 系統 **不會** 將任何未來訊息視為 CSAT 回覆
4. 自動發送會依設定持續重試
5. 客服人員可隨時手動重新發送 CSAT 調查

此設計可確保對話流程維持自然，客戶不會被困在「調查模式」。

<br/>

<center>
<a href="/images/seax/zh/csat/CSAT_Demo_Invalid.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/zh/csat/CSAT_Demo_Invalid.png" alt="顯示無效回覆情境的示意畫面。">
</a>

</center>

<br/>

---

## 情境三: 客戶完全沒有回覆

- 當有新的入站訊息到達後，自動發送會再次嘗試發送 CSAT 調查
- 客服人員可視需要在任何時間手動發送 CSAT 調查
