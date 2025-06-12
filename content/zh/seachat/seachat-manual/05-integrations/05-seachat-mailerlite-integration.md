---
title: "MailerLite"
description: "將 SeaChat 與 MailerLite 整合，讓表單自動將客戶信箱加入郵件名單。學習如何產生 API 金鑰以進行郵件行銷。"
date: 2024-04-23T08:48:57+00:00
lastmod: 2024-04-23T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /zh/seachat/seachat-integrations/mailerlite/
  - /seachat/seachat-manual/05-integrations/05-seachat-mailerlite-integration/
url: /zh/seachat/integrations/mailerlite/  
weight: 404
toc: true
---

本頁將詳細說明如何將 MailerLite 與 SeaChat 整合。完成整合後，您可以利用 SeaChat 表單自動收集客戶信箱與資訊，並自動加入 [MailerLite](https://www.mailerlite.com/) 郵件名單。

如需視覺化教學，請參考下方影片：<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/xTnJ9L1sVC4?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## 步驟 1：建立 SeaChat 帳戶
如果您尚未擁有 SeaChat 帳戶，可前往 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！註冊後即可建立 AI 助理並整合 MailerLite。

## 步驟 2：開啟「Integrations」
進入 MailerLite 後台，於左側選單點選「Integrations」。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 50%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/add-mailerlite-integrations.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/add-mailerlite-integrations.png" alt="前往 Mailerlite 後台並點選 Integrations。">
</a>
</div>
</div>

## 步驟 3：選擇「API」
點擊「Use」選擇「API」。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/select-mailerlite-api.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/select-mailerlite-api.png" alt="在 MailerLite 選擇 API">
</a>
    <p style="margin-top: 20px; font-size: 15px">在 MailerLite 產生新金鑰
</div>
</div>

## 步驟 4：產生新金鑰
點擊「Generate new token」。為此 API 金鑰命名，並同意 API 金鑰規範後，點擊「Create token」。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/generate-new-token-mailerlite.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/generate-new-token-mailerlite.png" alt="在 MailerLite 產生新金鑰">
</a>
    <p style="margin-top: 20px; font-size: 15px">在 MailerLite 產生新金鑰
</div>
</div>

<br>

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/give-api-token-name-mailerlite.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/give-api-token-name-mailerlite.png" alt="為新金鑰命名">
</a>
    <p style="margin-top: 20px; font-size: 15px">為新金鑰命名
</div>
</div>

## 步驟 5：複製 API 金鑰
請妥善保存您的 API 金鑰，然後回到 SeaChat 的 MailerLite 整合頁面完成整合。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/copy-and-save-mailerlite-api-key.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/copy-and-save-mailerlite-api-key.png" alt="複製並保存 MailerLite API 金鑰">
</a>
    <p style="margin-top: 20px; font-size: 15px">複製並保存 MailerLite API 金鑰
</div>
</div>

## 步驟 6：（選填）查找 Group ID
若您希望將聯絡人加入特定 MailerLite 群組，可於「Developer API」頁面底部查詢所有 Group ID。提示：可將聯絡人加入多個群組。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/get-mailerlite-group-id.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/get-mailerlite-group-id.png" alt="查找 MailerLite 群組 ID">
</a>
    <p style="margin-top: 20px; font-size: 15px">查找 MailerLite 群組 ID
</div>
</div>

### 支援
需要協助？請聯絡 [seachat@seasalt.ai](mailto:seachat@seasalt.ai)。
