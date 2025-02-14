---
title: "Wordpress"
description: "學習如何將SeaChat AI助理整合到Wordpress網站，用線上AI聊天機器人跟你的網站訪問者即時對話，線上客服24小時在線服務。"
date: 2024-05-20T08:48:57+00:00
lastmod: 2024-05-20T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /zh/seachat/seachat-integrations/wordpress/
url: /zh/seachat/integrations/wordpress/
weight: 404
toc: true
---

此頁教學將詳細說明嵌入整合SeaChat AI助理到 Wordpress 網站的過程。

## 步驟1：創建一個SeaChat帳戶

如果您還沒有SeaChat帳戶， 您可以在 [SeaChat網站](https://chat.seasalt.ai/)免費註冊！ 然後您可以將構建好的AI助理，移至您的 Wordpress 網站上。

## 步驟2：開啟Wordpress

前往您的 Wordpress 網站的儀表板。在右方選單選擇「外觀」。

<img width="100%" style="border-radius: 0.4rem" src="/images/seachat/zh/integrations/wordpress/wordpress-seachat-dashboard.png" alt="前往您的 Wordpress 網站的儀表板。在右方選單選擇「外觀」。">

## 步驟3：複製SeaChat程式代碼

您需要登入SeaChat才能查看此程式片段。您可至[SeaChat](https://chat.seasalt.ai/)免費註冊。在SeaChat儀表板的工作區內導航至「AI助理配置」->「頻道」，並在Wordpress頻道下，來取得所需的程式片段。

從Seachat上的Wordpress 第三方整合設置中複製SeaChat程式片段。

## 步驟4：打開「佈景主題檔案編輯器」並貼上SeaChat程式碼

打開左方功能選單的「佈景主題檔案編輯器」 -> 右方選單的「Theme Footer」。在程式碼中貼上SeaChat程式碼（在`<body>`和`</body>`之間。最後，點擊「更新檔案」。

<img width="100%" style="border-radius: 0.4rem" src="/images/seachat/zh/integrations/wordpress/wordpress-seachat-add-widget-code.png" alt="打開「佈景主題檔案編輯器」並貼上SeaChat程式碼">

## 步驟5：預覽

## 步驟8：儲存並預覽

現在訪問你的網站，即可看到SeaChat網頁聊天機器人在右下角。

**非常重要**: 如果您想要配置小工具的樣式，請前往「頻道」->「網頁AI助理」->「基本設置」。您的AI助理將在您的網頁聊天掛件頻道中共享相同的樣式。

## 排障提醒：SeaChat 小工具未在網頁載入？

如果您使用的 WordPress 最佳化外掛會消除 render-blocking CSS，請注意，這可能會導致 SeaChat 網頁聊天小工具無法正常載入您的網站。

#### **🔍 原因**

某些最佳化外掛可能會延遲或移除關鍵 CSS，這可能影響 SeaChat 小工具的呈現方式，導致以下問題：

- 小工具無法顯示在您的網站上。
- 聊天小工具出現異常的 UI 問題。

#### **🛠️ 修復方法**

如果您啟用了效能最佳化外掛，請按照以下步驟操作：

1. 檢查您的外掛設定是否包含 「消除 Render-Blocking CSS」 或 「最佳化 CSS 傳遞」 選項。
2. 停用此特定最佳化設定，以防影響聊天小工具的正常運作。
3. 清除快取並重新載入您的網站，以確保聊天小工具能夠正確運作。

#### **外掛示例: WP Rocket**

我們以 **WP Rocket** 這款廣泛使用的網站效能最佳化外掛為例。在 **「檔案最佳化」**（File Optimization）標籤下，請勿勾選 **「最佳化 CSS 傳遞」**（Optimize CSS Delivery）選項，以確保 SeaChat 網頁聊天小工具能順利載入。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image2.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wordpress/wordpress-seachat-wp_rocket.png" alt="WP Rocket Settings">
</a>
</center>

<br/>

如果您需要進一步協助，歡迎隨時聯絡 [seachat@seasalt.ai](mailto:seachat@seasalt.ai).！🚀
