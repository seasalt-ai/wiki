---
title: "Zoho 整合"
description: "使用 Seasalt.ai 的 Zoho 整合功能連接您的聯絡中心。"
date: 2025-12-16T08:48:57+00:00
lastmod: 2025-12-16T08:48:57+00:00
draft: false
images: []
menu:
  seax:
    parent: "seax-omni"
url: /zh/seax/seax-omni/zoho-integration-with-contacts-sync/
weight: 46
toc: true
---


本指南概述了將 Zoho CRM 與您的 Seasalt.ai (SeaX) 工作區整合的步驟。此整合允許您在 SeaX 和 Zoho CRM 之間無縫同步聯絡人資訊。

<iframe width="560" height="315" src="https://www.youtube.com/embed/qTT-JTFZfqc?si=A0Y6DeTtSVQrEmIm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 先決條件
* 一個 Seasalt.ai (SeaX) 工作區帳號。
* 一個 Zoho CRM 帳號（免費版、標準版、專業版或企業版）。

## 整合步驟指南

### 1. 進入 SeaX 的整合設定
1. 登入您的 SeaX 工作區。
2. 在左側選單中，前往 **Workspace** > **Integrations**。
3. 從 CRM Integrations (CRM 整合) 列表中選擇 **Zoho**。

### 2. 在 Zoho API Console 建立客戶端

1. 開啟新的瀏覽器分頁並前往 [api-console.zoho.com](https://api-console.zoho.com)。
2. 點擊 **Add Client** (新增客戶端)。
3. 選擇 **Server-based Applications** 作為客戶端類型。
4. **Client Name:** 輸入整合名稱（例如：`Seasalt.ai`）。
5. **Homepage URL:** 返回 SeaX 整合頁面，複製步驟 3 中提供的 **Homepage URL**，並將其貼上至 Zoho 控制台。
6. **Authorized Redirect URIs:** 從 SeaX 整合頁面複製 **Authorized Redirect URI**，並將其貼上至 Zoho 控制台。
7. 點擊 **Create** (建立)。

### 3. 輸入憑證

1. 在 Zoho 建立客戶端後，會出現 **Client Secret** 分頁，顯示您的 **Client ID** 和 **Client Secret**。
2. 從 Zoho 複製 **Client ID**，並將其貼上至 SeaX Zoho 整合頁面的對應欄位（步驟 2）。
3. 從 Zoho 複製 **Client Secret**，並將其貼上至 SeaX 的對應欄位。

### 4. 授權連線
1. 在 SeaX 中，點擊 **Zoho CRM Connect** 按鈕。
2. Zoho 將彈出視窗詢問存取權限。點擊 **Accept** (接受)。
3. 您應該會在 SeaX 中看到「Connection Successful」(連線成功) 的訊息。

## 如何使用此整合

連線後，您可以直接從對話視圖同步聯絡人。

1. 前往 SeaX 的 **Conversations** (對話)。
2. 開啟與聯絡人的對話。
3. 點擊使用者詳細資料旁邊的 **Edit Contact** (編輯聯絡人) 圖示（鉛筆形狀）。
4. 點擊 **Sync Zoho** 按鈕。
* **Sync to CRM (同步至 CRM):** 如果您在 SeaX 中更新了詳細資料（例如姓名），請點擊 **Save & Sync to CRM** 將資料推送到 Zoho。
* **Sync from CRM (從 CRM 同步):** 如果該電話號碼已存在於 Zoho 中，此整合可以將聯絡人的姓名和詳細資料拉取到 SeaX。


## 專業提示：Zoho CRM 免費版
如果您是小型企業主，Zoho 提供了一個隱藏的 **Free Edition** (免費版)，同樣支援此整合功能。

1. 前往 Zoho CRM 定價頁面。
2. 捲動至頁面最底部。
3. 尋找「Zoho CRM Free Edition」區塊。
4. 此版本包含：
* 3 位免費使用者。
* 每日 5,000 次 API 呼叫（足以滿足大多數小型企業的同步需求）。