---
title: "AI助理資訊"
description: "AI助理資訊是SeaChat助理的核心，包括名稱、描述和進階設置。這篇文章詳細介紹如何配置您的AI助理，以及如何使用進階功能如助上下文抽取和檢索增強生成(RAG)。"
lead: ""
date: 2024-04-26T08:48:45+00:00
lastmod: 2024-05-29T08:48:45+00:00
weight: 12
draft: false
images: []
toc: true
aliases:
  - /zh/seachat/seachaat-manual/02-create-agent/03-advanced-settings/01-agent-information/
url: /zh/seachat/manual/create-agent/agent-information/
---

# 簡介

**助理資訊**是您的 AI 助理的核心。它包含有關您的助理的所有必要資訊，包括其名稱、描述和其他進階設置，如上下文抽取。在本教學中，我們將帶您了解**助理資訊**下的**助理配置**中的每個參數。

---

## 基本設置

SeaChat 允許您配置您的 AI 助理的資訊，例如名稱、使用案例和描述。在**基本設置**中，用戶可以設置以下參數：

### 名稱
您的 AI 助理的名稱。此名稱將顯示在對話窗口中。

> :page_facing_up: **備註**
>
> 這將是您的助理用於管理助理的名稱。如果您希望更改助理整合中顯示的名稱，請參閱[網頁整合](/zh/seachat/seachat-manual/04-channels/08-install-to-webpage/)。

### 使用情境
您的 AI 助理的使用案例。這將幫助您對助理進行分類。SeaChat 提供了一系列可供選擇的使用案例。根據您的需求，您可以選擇最適合您的 AI 助理的使用案例。不同的使用案例可能需要不同的描述設置，但在導入使用案例時，您可以簡單地按照描述部分的說明進行操作。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/use-case-examples.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/use-case-examples.png" alt="image that display the use case options available in SeaChat">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">選擇適合的使用情境</p>
</div>

### 描述
關於您的 AI 助理的簡要描述，詳細說明您的助理的行為及其參考資料。您在描述欄位中輸入的任何內容都將顯示在頁面右側的助理指導中。然後，此描述將用於提示語言模型生成回覆。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/description-preview.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/description-preview.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent Description</p>
</div>

### 回覆語言
AI 助理將用於回覆用戶的語言。如果需要AI助理以多國語言回答問題，您可以選擇**以用戶輸入的語言回答**。

透過選擇回覆語言，您可以確保 AI 助理以正確的語言進行回應。這對有多種語言的用戶的企業們，十分有用。以中文為例，繁體中文和簡體中文在許多方面都有細微差別。透過將回覆語言設定為繁體中文，AI 助理將以繁體中文的回應。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/response-language.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/response-language.png" alt="image showcases the options of response language">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent's Response Language</p>
</div>

### 真人客服
真人客服功能允許人類客服在需要時介入對話。如果啟用此功能，您的客戶將在聊天對話期間有請求真人客服的選擇。這需要您提供一名實際的人類客服來監控和回覆用戶。

您可以取消選中該框以禁用此功能，從而使您的用戶無法在對話期間請求真人客服，但是真人客服仍可以從**對話**儀表板接管對話。您可以訪問我們的[真人客服教學](https://wiki.seasalt.ai/zh/seachat/manual/create-agent/agent-information/)以獲得有關該功能的更詳細說明。

> :page_facing_up: **注意**
>
> 如果沒有真人助理在線，客戶可以留言。真人可以在工作時間查看對話摘要並回覆。


### 與 AI 助理互動
您可以立即與您剛建立的 AI 助理進行互動。在**AI助理網址**中，您可以點擊 URL 以在獨立窗口中與您的 AI 助理進行互動。

或者，如果您希望將 AI 助理集成到您的網站中，您還可以在**API 金鑰**部分訪問您的 API 金鑰。請查看[網頁機器人](https://wiki.seasalt.ai/zh/seachat/manual/channels/webpage/)以獲得有關如何將您的 AI 助理以編程方式集成到您的網站的更多信息。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/additional-options.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/additional-options.png" alt="image that displays the additional options in Basic Settings">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Additional Options in Basic Settings</p>
</div>

## 聊天設計風格

### 風格設置

SeaChat允許您設計自己的網頁聊天小工具。您可以自訂聊天小工具以符合您的品牌色彩和風格。您可以從多種顏色和風格中選擇，以創建符合您品牌美學的聊天小工具。每次更改時，您都可以通過點擊**預覽**按鈕實時預覽聊天小工具在網站上的外觀。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/style-setting.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/style-setting.png" alt="顯示風格設置中額外選項的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">可自訂的網頁聊天小工具</p>
</div>

### 聊天設置

除了風格設置外，您還可以自訂聊天設置。這個功能可以減少您的AI助理編輯器在基本對話訓練上花費的時間。您可以設置聊天設置，自動設置對話流程，例如問候語、對話開始消息和對話結束消息。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/chat-setting.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/chat-setting.png" alt="顯示聊天設置中額外選項的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">客制化聊天設置</p>
</div>


## 進階設置

我們建議您參閱[**進階設置**](https://wiki.seasalt.ai/zh/seachat/manual/create-agent/advanced-settings/rag/)教學，以了解 SeaChat 中提供的進階功能。對於上下文抽取和檢索增強生成（RAG）等功能，您可以在助理資訊下的進階設置部分找到它們。