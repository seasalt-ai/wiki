---
title: "SeaX 與 SeaChat 的群發簡訊/電話"
description: "掌握使用 SeaX 和 SeaChat 的群發訊息功能。了解如何設置 AI 助理、自動化活動並簡化通訊流程。"
date: 2024-07-22T08:48:57+00:00
lastmod: 2024-07-22T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-omni"
aliases:
  - /zh/seax/seax-messaging/seax-agent-bulk-send/
  - /zh/seax/seax-agent-bulk-send/
  - /seax/seax-agent-bulk-send/
url: /zh/seax/seax-omni/seax-agent-bulk-send/
weight: 30
toc: true
---

## SeaX 與 SeaChat 的群發簡訊/WhatsApp/電話

SeaX 的群發簡訊功能提供了一個強大的工具，可以從單一平台管理多個業務渠道的通訊。不僅可以向不同客戶發送訊息，還可以通過與 SeaChat 的整合，自動化這些對話。

本指南將引導您如何使用 SeaX 和 SeaChat 發送群發訊息和電話，幫助您簡化業務通訊。

## 🎥 Video Tutorial for Bulk Calling

A comprehensive video tutorial demonstrates step-by-step how to set up and use SeaX with phone calls, including both outbound campaigns and inbound call handling by AI agents.

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/An4n8JhhdvA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

See [cross reference with SeaChat]({{< ref "seachat/seachat-manual/05-integrations/08-seax-integration-bulk-phone-calls.md" >}})

## 🎥 Video Tutorial for Bulk WhatsApp Messaging (Campaigns)

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/WUwn2QoeBGA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

See [cross reference with SeaChat]({{< ref "seachat/seachat-manual/05-integrations/09-seax-integration-whatsapp-in-seachat.md" >}})

## 設置工作區

要將 SeaX 與 SeaChat 整合，您需要一個電話號碼來發送訊息，以及一個 AI 助理來處理對話。您可以在 SeaX 的 **工作區** 下的 **號碼** 部分找到電話號碼，並在 SeaChat 的 **工作區** 下的 **AI助理** 部分找到 AI 助理。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/seax-number.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/seax-number.png" alt="SeaX | SeaX Number Setup">
</a>

_SeaX 號碼_

</center>

> 🚨 注意 🚨
>
> 確保您在 SeaChat 和 SeaX 上操作相同的工作區，才能正確整合。AI 助理和電話號碼必須在同一個工作區內。

## 在 SeaChat 上創建 AI 助理

首先，在 SeaChat 上部署一個功能性 AI 助理，並設置 SeaX 的整合。由於 SeaX 主要是一個消息傳遞平台，因此您需要前往 SeaChat 配置 AI 助理。

詳情請參見 [SeaX 與 SeaChat 的整合](https://wiki.seasalt.ai/seachat/integrations/seax-seachat/)。

## 使用 SeaX 發送群發訊息

整合設置完成後，您可以開始使用 SeaX 發送群發訊息。SeaX 與 SeaChat 的整合提供了多種功能。我們先確保 SeaX 配置正確。

### 收件人

在發送群發訊息的第一步中，選擇收件人。由於可能涉及數千個聯絡人，可以使用 SeaX 的標籤功能來簡化過程。為不同的聯絡人群組創建標籤，並通過這些標籤選擇收件人。新增聯絡人時，直接分配相應的標籤即可。

在群發訊息的 **收件人** 部分可以查看所有標籤，並選擇用於群發訊息的標籤。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/recipient-step.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/recipient-step.png" alt="SeaX | Recipient Setup">
</a>

_收件人標籤_

</center>

### 聯絡人

選擇收件人標籤後，您將進入 **聯絡人** 部分。在這裡，您可以查看聯絡人姓名、電話號碼及其關聯的標籤。取消勾選您不希望包含在訊息中的聯絡人，然後繼續到 **撰寫** 部分。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/contact-step.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/contact-step.png" alt="SeaX | Contact">
</a>

_管理聯絡人_

</center>

### 為外發 SMS 和電話創建活動

活動是群發訊息的單位。在這裡配置活動的名稱、關聯的聯絡人標籤、執行方法及時間。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/compose-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/compose-dashboard.png" alt="SeaX | Campaign Dashboard">
</a>

_創建活動_

</center>

#### 活動名稱與標籤

創建活動時，請提供一個名稱並選擇關聯的標籤。注意，在 **撰寫** 頁面的標籤是用於在活動開始後新增到所選聯絡人的。如果希望向特定聯絡人發送訊息，需在 **收件人** 和 **聯絡人** 部分選擇相應標籤。

#### 外發 SMS 和電話

設置活動名稱和標籤後，選擇執行方法。選擇 **文字/語音AI助理**，讓 AI 助理處理外發訊息。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/campaign-execution.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/campaign-execution.png" alt="SeaX | Executing SeaX Campaign">
</a>

_執行活動_

</center>

> 🔖 注意
>
> 確保 AI 助理已在 SeaChat 上設置好，以處理外發和內發訊息。由於 SeaX 是消息平台，需要在 SeaChat 上配置 AI 助理的起始訊息、語音及其他設置。
>
> 點擊 SeaX 中所選助理旁的 **設定AI助理** 按鈕，在 SeaChat 平台上配置助理。
>
> 如果無法看到助理，表示 AI 助理尚未在 SeaChat 上設置。點擊 **AI助理配置** 設置助理，並記得保存設置。

#### 發送時間

設置計劃活動的發送時間。您可以選擇立即發送或安排在稍後發送。對於外發電話，設置截止時間以避免深夜打擾客戶。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/schedule-setting.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/schedule-setting.png" alt="SeaX | Schedule Setup">
</a>

_計劃設置_

</center>

> 額外設置 - 捕捉收件人按鍵和點擊追蹤
>
> SeaX 會追踪收件人與 AI 助理的互動。啟用 **捕獲收件人對您的訊息的按鍵操作** 記錄通話過程中的按鍵輸入，用於調查。
>
> 啟用 **點擊追踪** 追踪 SMS 中的點擊，例如鏈接點擊追踪。

### 發送者

選擇活動的發送者，並選擇發送訊息的電話號碼。

如需新增電話號碼，點擊 **購買電話號碼**，SeaSalt 將提供報價。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/sender.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/sender.png" alt="SeaX | Sender Setup">
</a>

_發送者設置_

</center>

### 審核

在發送活動前，請審核設置，確保一切正確配置。檢查活動名稱、SeaChat 訊息設置及發送者詳情。

#### 更新內發助理

對於 SMS 和電話活動，更新內發助理以處理進入的訊息。選擇在 SeaChat 上設置的助理來完成此目的。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/inbound-agent-update.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/inbound-agent-update.png" alt="SeaX | SeaX Number Setup">
</a>

_內發助理設置_

</center>

### 發送活動

點擊 **立刻開始** 啟動群發活動，開始通過 SeaX 發送訊息。在側欄的 **活動** 部分監控活動進展。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/campaign-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/campaign-dashboard.png" alt="SeaX | Send out Campaign">
</a>

_活動儀表板_

</center>

## SeaX 與 SeaChat 的對話同步

SeaX 和 SeaChat 是管理群發訊息與電話的強大組合。通過 SeaX，您可以向數千名客戶發送訊息，並借助 SeaChat 的 AI 助理自動化對話。兩個平台的對話同步，提供無縫的使用體驗，但有以下幾點差異：

- 所有由 SeaX 通過 SeaChat 助理啟動的外發通話都會顯示在 SeaChat 和 SeaX 的 **對話** 部分。然而，如果從 SeaChat 接收到來電，則不會同步至 SeaX。

- 如果用戶回覆來自 SeaX 的 SMS，該回覆不會同步到 SeaChat，除非該號碼在 SeaX 中是活躍 AI 助理活動的收件人。
