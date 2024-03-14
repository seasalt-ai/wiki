---
title: "Shopify"
description: "Bring SeaChat to your Shopify storefront"
date: 2022-11-22T08:48:57+00:00
lastmod: 2022-11-22T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
   - /en/seachat/seachat-integrations/shopify/
   - /seachat/seachat-integrations/shopify/
weight: 10
toc: true
---


此頁教學將詳細說明嵌入整合SeaChat AI助理到您Shopify商店前端的過程。

## 步驟1：創建一個SeaChat帳戶
如果您還沒有SeaChat帳戶， 您可以在 [SeaChat網站](https://chat.seasalt.ai/)免費註冊！ 然後您可以將構建好的AI助理，移至您的Shopify網站上。

## 步驟2：開啟Shopify
前往您的Shopify儀表板，從選單中點擊「Online Store」。

<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step1.png" alt="Go to your Shopify dashboard and click on Online Store from the menu.">


## 步驟3：在Shopify上編輯程式
點擊您目前主題旁邊的刪節號圖標<mark>•••</mark>，選擇「Edit Code」並開始編輯。


<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step2.png" alt="Start editing by clicking the ellipsis icon next to your current theme and choosing Edit code.">

## 步驟4：點擊theme.liquid
點擊左側面板上的「</> theme.liquid」。


<img width="40%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step3.png" alt="Click on “theme.liquid” on the left side panel.">


## 步驟5：複製SeaChat程式
您需要登入SeaChat才能查看此程式片段。您可至[SeaChat](https://chat.seasalt.ai/)免費註冊。在SeaChat儀表板的工作區內導航至「AI助理配置」->「頻道」，並在Shopify頻道下，來取得所需的程式片段。



將從Seachat上的Shopify整合設置中獲得的SeaChat程式片段貼上到<head>。您可以在開頭的<head>標籤和結尾的</head>標籤之間的任何位置貼上它。

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step4.png" alt="Paste the SeaChat code snippet in the head; section. You can paste it anywhere between the opening head tag and the closing /head tag">


## 步驟6：儲存並預覽

點擊右上方的「儲存」按鈕。接著點擊「預覽商店」來測試AI助理。當您準備好時，記得再次啟動商店！

**非常重要**: 如果您想要設定掛件的樣式，請前往「頻道」->「網頁AI助理」->「基本設置」。您的AI助理將在您的網頁聊天掛件頻道中共享相同的樣式。

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step5.png" alt="Click “Save” button on top right. Click “Preview Store” to test the AI agent. Remember to launch the store again when you are ready!">


## 步驟7：（Optional）移除其他聊天機器人
請移除任何其他的聊天機器人服務，如Shopify Inbox，以避免混淆。對於Shopify用戶們，請在您的網站的自定頁面切換成禁用「Apps embeds」。如果您之前的聊天機器人服務是通過程式嵌入整合的，請小心移除。

### 協助支援
需要協助？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai).


 
 