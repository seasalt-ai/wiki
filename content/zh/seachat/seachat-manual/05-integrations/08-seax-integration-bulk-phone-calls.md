---
title: "Voice AI大規模外撥電話與自動來電處理"
description: "將 SeaX 與 SeaChat 整合，實現大規模電話外撥與來電自動化。用 AI 自動化客戶語音溝通。"
date: 2025-06-12T08:48:57+00:00
lastmod: 2025-06-12T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /zh/seachat/seachat-integrations/seax-integration-with-phone-calls/
url: /zh/seachat/integrations/seax-seachat-phone-calls/
weight: 407
toc: true
---



## 概述

[SeaX](https://seax.seasalt.ai) 讓企業能夠利用 AI 智能客服進行大規模外撥與來電活動。整合 SeaChat 後，SeaX 不僅可自動外撥（如問卷、客戶聯繫），還能 24/7 由 AI 智能客服接聽來電。這項整合非常適合希望自動化語音互動、提升客戶參與度並確保每通來電都能被即時處理的企業。

## 🎥 教學影片

下方影片將完整示範如何設定與使用 SeaX 電話外撥與 AI 來電處理。

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/An4n8JhhdvA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

## 主要功能

**大規模外撥電話：**  
直接從 SeaX 發起數百或數千筆外撥電話活動。可用 AI 智能客服自動執行問卷、訪談或通知。

**AI 來電自動接聽：**  
設定 AI 智能客服 24 小時自動接聽來電，隨時即時回覆客戶問題。

**統一管理介面：**  
於單一 SeaX 介面管理所有外撥/來電活動、電話號碼與 AI 智能客服。SeaX 與 SeaChat 智能客服同步，設定更簡單。

**即時語音轉錄與摘要：**  
自動將通話內容轉錄並產生摘要，方便回顧互動紀錄與萃取重點。


## 先決條件

- 需有 SeaX 與 SeaChat 帳號。
- 至少在 SeaX 配置一組電話號碼（市話或免付費）。
- 具備管理員權限以設定整合與 AI 智能客服。

## 步驟說明

### 1. 指派並設定電話號碼

- 登入 SeaX，前往 **Workspace → Numbers**。
- 選擇或新增一組用於外撥/來電的電話號碼。
- 點擊該號碼的 **Edit**。
- 啟用 **AI Agent to answer the phone** 選項。
- 指派 SeaChat 工作區的 AI 智能客服來接聽來電。

### 2. 同步 AI 智能客服

- 確認 SeaX 與 SeaChat 工作區已同步。
- 所有在 SeaChat 建立的 AI 智能客服都可於 SeaX 指派，確保跨通路行為一致。

### 3. 設定來電自動接聽

- 在 SeaChat 前往 **Integrations**，選擇電話整合。
- 將電話號碼連結至指定 AI 智能客服。
- 設定語言、語音（如「Jessica」TTS）與來電問候語。
- 儲存設定。

### 4. 測試來電

- 撥打測試電話至設定號碼。
- AI 智能客服會以預設問候語接聽，並依設定回覆問題。
- 通話轉錄與摘要可於 SeaX 與 SeaChat 查閱。

### 5. 設定外撥電話活動

- 在 SeaX 前往 **Bulk Send/Call** 或 **Campaigns**。
- 選擇已啟用電話的號碼。
- 匯入或選擇聯絡人名單（避免重複）。
- 設定 AI 智能客服的外撥腳本或問卷（如招募活動的面試問題）。
- 排程或啟動外撥活動。AI 智能客服將依設定逐一撥打並對話。
- 即時監控活動進度，並於系統中查閱通話摘要與回覆內容。

### 6. 管理來電回撥

- 若收件人回撥未接來電，AI 智能客服（或另行設定者）會自動接聽並延續對話。
- 所有來電/外撥資料、轉錄與摘要皆可於 SeaX 與 SeaChat 查閱。

## 多號碼管理

SeaX 支援多組電話號碼，可用於不同活動或部門。可依需求指派不同 AI 智能客服，並於統一介面集中管理。

## 最佳實踐

**避免重複聯絡人：**  
請確保每個電話號碼僅出現在名單一次，避免重複撥打。
