---
title: "知識庫中的額外功能"
description: "了解如何在 SeaChat 知識庫中添加按鈕、圖片、視頻等額外功能，優化 AI 助理回應，並同步最新知識以提供精準支持。"
lead: ""
date: 2024-03-04 10:43:51.069 +0100
lastmod: 2024-06-17 10:43:51.069 +0100
weight: 500
draft: false
images: []
aliases:
  - /zh/seachat/seachat-manual/03-add-knowledge/10-additional-feature/01-additional-features-in-kb
url: /zh/seachat/manual/add-knowledge/additional-features-in-kb/
---

## 簡介

除了快速回應之外，SeaChat 提供更進階的功能來增強您的 AI 助理的回應。這些功能包括在回應中新增按鈕、圖片和視頻。本指南將引導您如何將這些功能添加到 AI 助理的回應中，確保您的用戶獲得最全面的支持。以下所有參數適用於您上傳到知識庫的每一條知識。

## 知識庫中的額外功能

首先，導航到知識庫儀表板並選擇要添加額外功能的現有知識。在左側邊欄的 **AI助理配置** 下找到 **知識庫**，然後點擊 **現有知識** 以查看已上傳到您的 AI 助理的所有知識。

打開您希望添加額外功能的知識，然後點擊 **編輯** 按鈕。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/kb-dashboard.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/kb-dashboard.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">前往 <strong>Existing</strong></p>
</div>

## 編輯知識中的額外功能

當您的 AI 助理需要回答問題時，它會在知識庫中搜索最相關的信息。AI 助理會查看 **文件標題** 以尋找相關性。SeaChat 利用這種行為，允許您向個別知識添加額外功能，因此每次助理從該特定知識中檢索信息時，都會記住在回應中包含這些額外功能。這允許 SeaChat 用戶向其客戶提供更詳細的信息。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/additional-settings.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/additional-settings.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">其他設置</p>
</div>

### 卡片消息

在向客戶提供信息時，提供信息來源或補充閱讀以便他們更好地了解是很有用的。SeaChat 允許您向回應中添加卡片和按鈕，以向用戶提供更全面的回應。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/card-info.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/card-info.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">知識設置</p>
</div>

卡片消息提供了您所提供信息的強大視覺效果。您可以為卡片消息添加標題、副標題和圖片。當您想要提供所提供信息的預覽時，此功能特別有用。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/card-msg.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/card-msg.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">上傳圖片到卡片消息</p>
</div>

### 按鈕消息

與卡片相比，按鈕更為簡單明了。您可以為按鈕消息添加標題和 URL。此功能特別有用，當您想提供信息來源的鏈接時，您可以向回應中添加任意多個按鈕。與卡片消息相比，此功能為您的用戶提供了更簡單的導航。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/btn-msg.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/btn-msg.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">知識設置</p>
</div>

### 文檔權重

文檔權重是一個參數，允許您優先考慮特定的知識。權重越高，當 AI 助理搜索相關信息時，知識越有可能被檢索到。當您有多個與相同問題相關的知識時，這個功能特別有用，您希望優先檢索最重要的知識。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/doc-weight.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/doc-weight.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">知識設置</p>
</div>

## 同步 URL 知識

如果知識是通過 URL 或站點地圖導入的，您可以將知識與來源 URL 進行同步。當知識頻繁更新時，這個功能特別有用，並且可以確保您知識庫中的知識始終是最新的。

此功能可以讓用戶在知識庫管理方面有更好的體驗。只要該 URL 仍存在，用戶就不需要重新將知識上傳到知識庫。

您現在只需點擊要與來源 URL 同步的知識旁邊的 **同步** 按鈕，SeaChat 會自動使用來源 URL 的最新信息更新該知識。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/sync-button.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/sync-button.png" alt="同步知識按鈕">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">同步知識</p>
</div>