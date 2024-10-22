---
title: "電話"
description: "了解如何在 SeaChat 設置語音助理，處理來電語音和對外撥話，並使用免費電話號碼提供客戶支援。快速上手設置並測試您的語音助理。"
date: 2024-04-30T08:48:57+00:00
lastmod: 2024-04-30T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /zh/seachat/seachat-manual/04-channels/07-seachat-voicebot/
url: /zh/seachat/manual/channels/voicebot/
weight: 70
toc: true
---

SeaChat 不僅可以處理文字對話，還可以處理電話。SeaChat 允許您創建一個基於語音的對話助理來接聽所有來電，或者外撥至客戶電話。這個語音助理可以處理來電語音，回答客戶查詢，並提供客戶支援。SeaChat 語音助理還可以在需要時轉接給真人助理。在接下來的章節中，我們將向您展示設置 SeaChat 語音助理有多容易，以及您如何通過實際通話來測試您的助理。

--- 
## 設置 SeaChat 語音助理

首先，我們需要一個新的助理來處理語音來電。創建一個新的語音助理，請點擊您的頭像旁邊的助理下拉選單。您可以看到您已創建的助理列表。點擊 **新增AI助理** 按鈕來創建一個新助理。

在我的助理描述中，我確保包含了這個助理是用於語音接聽。這樣，我就可以輕鬆地辨認哪個助理是用於語音對話，哪個助理是用於文字對話。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/agent-description.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/agent-description.png" alt="">
</a>

*新增AI助理*
</center>

一旦我們創建了我們的語音助理，讓我們開始設置語音助理以處理來電語音。在 **AI助理設定** 的 **頻道** 下找到 **電話**。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/choose-inbound-calls.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/choose-inbound-calls.png" alt="">
</a>

*設置 **電話** 頻道*
</center>

### 免費電話號碼

在 **電話** 通道中，我們需要首先購買一個免費電話號碼。選擇您想要購買免費電話號碼和電話號碼的國家。一旦您選擇了理想的設定，點擊 **確認購買** 按鈕。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/buy-a-number.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/buy-a-number.png" alt="">
</a>

*購買免費電話號碼*
</center>

購買完成後，您可以看到您選擇的免費電話號碼。如果您對號碼不滿意，您可以隨時**取消號碼**並購買新號碼。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/toll-free-number.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/toll-free-number.png" alt="">
</a>

*免費電話號碼詳細信息*
</center>

### 助理設定

購買免費電話號碼後，我們需要設定助理以處理來電語音。在 **設定AI語音助理** 部分，您可以設置語音助理來處理來電。

您可以像任何其他 SeaChat 助理一樣為您的語音助理啟用真人助理功能。請確保您有一位真人客服在用戶啟用真人助理功能時監視並回應用戶。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/configure-agent.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/configure-agent.png" alt="">
</a>

*語音助理設定*
</center>

如上圖所示，有一些參數需要設置才能完全設定語音助理。如果您不確定設定，您可以從選擇語言開始，SeaChat 將自動為您設置其餘的設定。如下圖所示，我為我的語音助理選擇了繁體中文和 SeaVoice模型。現在點擊 **儲存設定** 以確定您的設置。

> :mag_right: SeaChat 語言模型：**SeaVoice**
> 
> SeaChat 目前提供 SeaVoice 和 SeaVoice-2 作為語音助理的語言模型。我們建議在大多數情況下使用 SeaVoice，因為它是語音助理中最穩定可靠的語言模型，而 SeaVoice-2 則是我們新開發的模型，仍處於實驗階段。


## 測試語音助理

現在我們已經設置了語音助理，我們可以開始測試我們的助理，看看它是否能夠處理來電語音以及對外撥話。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/configuration-done.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/configuration-done.png" alt="">
</a>

*設定完成*
</center>

### 來電語音以及對外撥話

測試語音助理有兩種方法。您可以撥打您購買的免費電話號碼，以查看語音助理如何處理來電，或者為您的語音助理提供一個要撥打的號碼，來測試對外撥話。由於這兩種方法可能需要在助理設置中進行不同的設定，請選擇最適合您的方法。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/test-agent.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/test-agent.png" alt="">
</a>

*測試您的助理*
</center>

大功告成。現在，您已經設置了 SeaChat 語音助理以處理來電語音或對外撥話。您現在可以通過實際通話來測試您的助理，並查看您的語音助理如何處理來電。

## 支援
需要幫助嗎？請聯繫我們：[seachat@seasalt.ai](mailto:seachat@seasalt.ai)。
