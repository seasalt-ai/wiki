---
title: "數據分析"
description: "監控一段時間內與AI智能助理的對話和訊息的統計數據。"
date: 2025-02-14T08:48:57+00:00
lastmod: 2025-02-14T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /zh/seachat/seachat-manual/analytics/
url: /zh/seachat/manual/analytics/
weight: 105
toc: true
---

## SeaChat 數據分析

### 總結

SeaChat 數據分析功能提供有關用戶與AI智能助理互動的寶貴見解。這款儀表板可讓您追蹤一段時間內的關鍵績效指標，幫助衡量參與度、優化AI智能助理效能並做出數據驅動的決策。導航至 `助理配置`下方的 `分析`選項卡，查看特定AI智能助理的分析頁面。

📊 追蹤AI智能助理的表現
監控對話數量、唯一訪客和訊息活動，以了解用戶如何與您的AI智能助理互動。

📈 衡量成長和趨勢
比較不同時間範圍（過去 7 天、過去 30 天等）的數據，以確定AI智能助理使用和使用者行為的趨勢。

🤖 優化AI智能助理回應
分析AI智能助理訊息統計數據，了解聊AI智能助理處理對話的效率，並優化回應以提高用戶滿意度。

👥 提高客戶參與度
透過追蹤真人客服請求和用戶交互，企業可以發現增強客戶支援和自動化策略的機會。

🔄 數據驅動決策
使用即時分析來完善AI智能助理工作流程，提高回應準確性，並根據實際使用模式優化使用者體驗

### 設定

在頁面頂部，您可以配置一些設定。首先，選擇您希望顯示資料的時區。例如，如果使用者開啟網路聊天並閱讀歡迎訊息，但沒有發送訊息，則仍會建立對話並顯示在對話統計資料中。如果您選取該設定框，像這樣沒有使用者訊息的對話將從統計資料中 _排除_。

預設情況下，儀表板資料每小時更新一次。如果您想按需刷新數據，請按一下`刷新數據`按鈕。

### 分析指標

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/01-seachat-analytics-settings-metrics.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/01-seachat-analytics-settings-metrics.png" alt="SeaChat Analytics Basic Metrics">
</a>

**SeaChat 數據分析指標**

</center>

SeaChat 數據分析中的指標部分提供了AI智能助理在選定時間範圍內的表現的詳細細分。您可以透過選擇來自訂日期範圍：

- 最後一天
- 過去 7 天
- 過去 30 天
- 過去 90 天
- 過去 180 天

選擇時間範圍後，SeaChat 會將AI智能助理在該時間內的表現與先前相同的時間長度進行比較。例如：

> 如果您選擇過去 7 天，顯示的指標會將過去 7 天與之前 7 天的時間段進行比較。

> 如果您選擇過去 30 天，它將比較過去 30 天和之前的 30 天。

#### 了解指標

顯示的關鍵績效指標 (KPI) 包括：

- 對話 – 在選定時間內發起的AI智能助理互動的總數。
- 獨立訪客 – 與AI智能助理互動的獨立使用者數量。
- 收到的訊息 – 用戶傳送給AI智能助理的訊息數量。
- 發送的AI智能助理訊息 – AI智能助理產生的回應數量。
- 即時客服請求 – 用戶要求人工客服的次數。
- 發送的座席訊息 – 即時座席在對話中發送的訊息數。

每個指標都包含一個百分比變化指示器，顯示與先前的同等時間段相比如何增加或減少。綠色箭頭表示正成長，而紅色箭頭（如果適用）表示下降。

這種比較可以幫助企業追蹤AI智能助理隨時間的效能趨勢、評估改進並確定需要優化的領域。

### 年度對話概覽

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/02-seachat-analytics-conversations-by-year.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/02-seachat-analytics-conversations-by-year.png" alt="SeaChat Analytics Conversation Yearly Overview">
</a>

**年度對話概覽**

</center>

SeaChat 數據分析中的「對話概述」部分提供了選定年份的AI智能助理互動的高級摘要。用戶可以從下拉式選單中選擇特定年份，以查看該期間AI智能助理參與度的關鍵統計數據。

- 對話總數 – 顯示所選年份的AI智能助理對話總數。
  每個對話的平均訊息數 – 顯示每個對話交換的平均訊息數，幫助評估使用者參與度。
- 每月訊息總數

在關鍵指標下方，線圖直觀地顯示了每月與AI智能助理交換的訊息總數。這允許用戶：

- 確定AI智能助理活動隨時間變化的趨勢。
- 發現參與度的季節性波動或高峰。
- 評估業務活動或AI智能助理改進對對話量的影響。

### 對話和訊息細分

按天、時間和管道細分的對話部分允許用戶分析自訂日期範圍內跨各種管道和時間段的AI智能助理互動。透過選擇特定的開始和結束日期，企業可以詳細了解大多數互動發生的時間和地點。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/03-seachat-analytics-conversation-breakdown-by-channel.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/03-seachat-analytics-conversation-breakdown-by-channel.png" alt="SeaChat Analytics Channel Breakdown">
</a>

**頻道細分**

</center>

通道細分錶顯示每個通道的以下資料：

- 頻道 – 使用者與AI智能助理互動的不同通訊管道（例如，網路聊天、LINE、WhatsApp、Voice、Messenger 等）。 SeaChat 提供的所有頻道一旦有流量就會自動出現在表格中。
- 獨立訪客 – 在選定時間範圍內透過每個特定管道與AI智能助理互動的獨立使用者數量。
- 收到的入站訊息 – 在選定日期範圍內使用者透過每個管道傳送的訊息總數。

#### 設定子頻道追蹤

SeaChat 網路聊天 小工具可讓您直接在自己的網站中安裝聊天視窗。
一些客戶將網路聊天小部件添加到多個站點，並希望能夠單獨追蹤每個站點上小部件的流量​​。
預設情況下，頻道細分會將所有網路聊天流量集中到一個名為`網路聊天`的頻道類型。
但是，透過對 網路聊天 小部件程式碼進行簡單的自訂，您可以為小部件的每個實例提供特定的`子通道`名稱並單獨追蹤流量。
使用子頻道資訊自訂網路聊天小工具後，所有後續流量將在表格中顯示為`網路聊天 - {subchannel}`。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/06-seachat-widget-subchannel-setup.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/06-seachat-widget-subchannel-setup.png" alt="SeaChat Analytics 網路聊天 Subchannel Setup">
</a>

**網路聊天 子通道設定**

</center>

導航至 `頻道` -> `網路聊天` -> `安裝小部件` 以尋找 網路聊天 小工具程式碼。
在此程式碼區塊中，有四個AI智能助理的網路聊天 URL 實例 - 如下所示：`https://chat.seasalt.ai/chat/{chat_config_id}`。
要區分不同的子頻道，只需將以下內容附加到 URL 末尾：`?channel={subchannel_name}`。
例如，假設您想要將 網路聊天 小工具新增到您的主頁以及 wiki 網站。
您可以將 URL `https://chat.seasalt.ai/chat/aaaabbbbccccdddd` 更新為 `https://chat.seasalt.ai/chat/aaaabbbbccccdddd?channel=homepage` 並將小工具程式碼新增至您的主頁。
然後您可以再次將 URL 更新為`https://chat.seasalt.ai/chat/aaaabbbbccccdddd?channel=wiki`並將程式碼新增至您的 wiki 網站。
在頻道細分中，您將看到來自兩個獨立管道的流量：`網路聊天 - homepage` 和 `網路聊天 - wiki`。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/04-seachat-analytics-messages-by-day-of-week.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/04-seachat-analytics-messages-by-day-of-week.png" alt="SeaChat Analytics Day of the Week Breakdown">
</a>

**按天細分**

</center>

透過「一周中的某一天」細分，您可以查看一周中的每一天向您的AI智能助理發送了多少用戶訊息。這使您可以確定用戶與您的AI智能助理互動的趨勢。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/05-seachat-analytics-messages-by-hour-of-day.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/05-seachat-analytics-messages-by-hour-of-day.png" alt="SeaChat Analytics Hour of the Day Breakdown">
</a>

**按小時細分**

</center>

透過「一天中的時間」細分，您可以查看用戶在一天中的什麼時間向您的AI智能助理發送訊息。這使您可以識別用戶與您的AI智能助理互動的趨勢，並可能有助於做出決策，例如何時讓即時代理在線。
