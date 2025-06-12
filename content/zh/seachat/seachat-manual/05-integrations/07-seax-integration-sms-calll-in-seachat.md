---
title: "SeaX 與 SMS & 語音通話整合"
description: "將 SeaX 與 SeaChat 整合，實現大量簡訊發送與自動語音通話處理。用 AI 自動化客戶溝通。"
date: 2024-07-16T08:48:57+00:00
lastmod: 2024-07-16T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /zh/seachat/seachat-integrations/seax-integration-in-seachat/
url: /zh/seachat/integrations/seax-seachat-sms-phone-calls/
weight: 406
toc: true
---

## 概述

本教學將帶您完成在 SeaChat 中設置 Seasalt 大量訊息平台 SeaX 的流程。SeaX 是一個強大的全通路平台，讓您能在單一介面管理所有業務通路。

更多資訊請參閱 [SeaX 文件](https://wiki.seasalt.ai/seax/seax-messaging/bulk-messaging-features/)。

整合 SeaX 至 SeaChat 後，您不僅能手動管理客戶對話，還能讓 SeaChat AI 智能客服自動回覆。SeaX 整合所有業務通路（如 WhatsApp、電話、SMS），並將這些通路導向 SeaChat 進行 AI 驅動的回應。

## SeaX 大量通話/發送

SeaX 為您的 AI 智能客服提供與客戶溝通的通道。完成與 SeaChat 的整合後，您即可透過 SeaX 向客戶發送大量訊息。

SeaChat 與 SeaX 無縫協作執行大量訊息發送。SeaX 會依序撥打名單上的每位客戶（約每秒一通）。當客戶接聽後，AI 智能客服會接手對話，您只需前往 **Conversations** 儀表板查看對話內容。

SeaChat 並不知曉您撥打的客戶名單，也無法主動發起通話。SeaChat 僅在對話啟動後負責對話內容；SeaX 則負責發起通話與發送訊息。

您可建立 **活動（Campaigns）**，向客戶發送 SMS 或語音留言。這些活動將透過 SeaX 發送，並由 SeaChat 上的專屬 AI 智能客服處理後續對話。

## 外撥通話活動

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/call-integration.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/call-integration.png" alt="Outbound/ Inbound Calls Integration">
    </a>
<br/>
    <p style="font-size: 15px">外撥/來電整合</p>
</div>
</div>

外撥通話是主動聯繫客戶的有效方式。透過 SeaX，您可自動化這些通話。

1. **語言選擇**：選擇語言及對應模型。建議使用 SeaVoice，穩定且適合正式環境。
2. **語音選擇**：選擇偏好的語音，並可點擊播放鍵預聽。
3. **外撥開場訊息**：當客戶接聽時，將播放此訊息，AI 智能客服隨後接手對話。您可於 **Conversations** 儀表板查看對話內容。

## 來電整合

來電是提供客戶服務的可靠方式。AI 智能客服可接聽來電並擔任語音接待員。

設定步驟與[外撥通話整合](#outbound-calls-integration)相同，包含語言、語音與問候語設置。

## SMS 整合

SMS 是行銷推廣的有效工具。發起或接收 SMS 對話都很簡單，只需設定開場訊息，AI 智能客服會自動處理後續對話。

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/sms.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/sms.png" alt="SMS Setup">
    </a>
<br/>
    <p style="font-size: 15px">SMS 設定</p>
</div>
</div>

## 測試整合

完成 SeaX 與 SeaChat 的整合後，您可透過發送訊息給 SeaChat AI 智能客服來測試。建議在正式大量發送前，先於各頁面使用指定按鈕進行本地測試。

測試無誤後，即可開始透過 SeaX 向客戶大量發送訊息，並由 SeaChat 智能客服接手後續對話。

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/find-seax.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/find-seax.png" alt="SeaX Messages in SeaChat">
    </a>
<br/>
    <p style="font-size: 15px">SeaX 訊息於 SeaChat</p>
</div>
</div>

## :dart: 疑難排解

1. **來電與 SMS 無可用號碼，如何正確設定？**

<div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <a href="/images/seachat-integrations/seax/no-phone-available.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/no-phone-available.png" alt="No Phone Available Warning">
    </a>
<br/>
    <p style="font-size: 15px;">無可用號碼警告</p>
</div>
</div>

如出現上述警告，表示您需為 AI 智能客服提供一組電話號碼，讓其作為管理來電與 SMS 的通道。當有人撥打此號碼或發送 SMS，AI 智能客服將自動處理對話。

請先於 SeaX 設定，並先向 SeaChat 智能客服發送一次外撥通話或 SMS。詳細操作請參閱 [SeaX 文件](https://wiki.seasalt.ai/seax/seax-messaging/bulk-messaging-features/)。

具體步驟：

1. SeaX -> 外撥通話給智能客服 -> 設定客服來電號碼
2. SeaX -> 外撥 SMS 給智能客服 -> 設定客服 SMS 號碼

如不確定智能客服是否已收到通話或 SMS，可於 **Conversations** 儀表板查詢對話紀錄。
