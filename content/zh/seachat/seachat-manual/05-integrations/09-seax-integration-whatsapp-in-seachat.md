---
title: "SeaX 與 WhatsApp 整合"
description: "將 SeaX 與 SeaChat 整合，實現 WhatsApp 大量訊息發送與 AI 自動化客戶溝通。"
date: 2025-06-11T08:48:57+00:00
lastmod: 2025-06-11T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /zh/seachat/seachat-integrations/seax-integration-with-whatsapp-in-seachat/
url: /zh/seachat/integrations/seax-seachat-whatsapp/
weight: 408
toc: true
---

## 概述

[SeaX](https://seax.seasalt.ai) 讓企業能夠高效發送 WhatsApp 大量訊息，並管理大規模客戶互動活動。當與 SeaChat 整合後，SeaX 不僅可進行大規模外發訊息，還能利用 AI 自動回覆客戶來訊。此整合同時優化外發活動與來訊支援，特別適合處理高訊息量或希望自動化客戶互動的組織。

## 🎥 教學影片
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/WUwn2QoeBGA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## 主要功能

- **WhatsApp 大量訊息發送：** 直接從 SeaX 向大量 WhatsApp 聯絡人發送廣播訊息。
- **AI 自動回覆：** SeaChat 可自動接手來訊，利用先進語言模型自動回覆。
- **真人客服接管：** 隨時可在 AI 與真人客服間切換，提供個人化支援。
- **統一管理：** 於單一 SeaX 介面管理多個 WhatsApp 商業帳號與活動。
- **合規性：** 確保所有收件人均已同意接收 WhatsApp 訊息，符合 WhatsApp 政策。

---

## 先決條件

- 具備 API 權限的 WhatsApp 商業帳號。
- SeaX 與 SeaChat 帳號。
- 具備 Meta Business Suite 管理員權限以整合 WhatsApp。

---

## 步驟說明

### 1. 將 WhatsApp 連接至 SeaX

1. 於 SeaX 的 **Workspace** 下點選 **Channels**。
2. 選擇 **WhatsApp Business Platform**，依畫面指示以 Meta Business Suite 帳號連接 WhatsApp 商業帳號。
3. 連接成功後，WhatsApp 帳號將顯示於 SeaX Workspace 的 Channels。

### 2. 設定大量訊息發送

1. 前往 SeaX 的 **Conversations** 或 **Bulk Send/Call** 區塊。
2. 選擇已啟用 WhatsApp 的號碼並撰寫廣播訊息。
3. 匯入或選擇聯絡人清單，確保所有收件人均已同意接收訊息。
4. 發送或排程廣播，SeaX 將訊息發送至所有選定聯絡人。

### 3. 整合 SeaChat 以自動回覆

1. 於 SeaChat 前往 **Agent Configuration → Integrations**。
2. 啟用 WhatsApp 整合並連結至 SeaX 帳號。
3. 將用於大量訊息的 WhatsApp 號碼指派給 SeaChat AI Agent。
4. 回到 SeaX，編輯 WhatsApp 號碼設定並啟用「AI Agent 回答 WhatsApp」。
5. 儲存設定。

### 4. 測試整合

- 向您的商業 WhatsApp 號碼發送測試訊息。
- 確認來訊已由 SeaChat AI Agent 自動處理。
- 真人客服可隨時進入對話或點選「接管」按鈕接手。

---

## 管理多個 WhatsApp 帳號

SeaX 支援多個 WhatsApp 商業帳號管理。可於 **Channels → Add Account** 新增帳號，集中管理所有號碼與客服。可依需求指派不同客服給不同帳號，並於統一介面監控所有活動。

---

## 真人客服接管

如遇需真人介入的客戶問題，客服可隨時從 AI 手中接管。可手動觸發，或由客戶輸入指令（如 `/live_agent`）請求。轉接過程無縫，除非另行告知，客戶無法分辨對話對象為 AI 或真人。

---

## 最佳實踐

- **取得同意：** 僅向已同意接收 WhatsApp 訊息的用戶發送大量訊息。
- **訊息個人化：** 利用變數與範本提升訊息互動率。
- **監控活動：** 善用 SeaX 報表工具追蹤發送、回覆率與活動成效。
- **維持合規：** 遵循 WhatsApp 商業訊息政策，避免帳號受限。

---

## 疑難排解

- 請確保 WhatsApp API 整合使用永久存取權杖。
- 確認 WhatsApp 應用已設為 Live 模式。
- 檢查 Webhook 權限設定，確保訊息可正常發送與接收。
- 若自動回覆無法運作，請確認 WhatsApp 號碼已正確連結至 SeaX 與 SeaChat。

---

## 支援

如需協助，請聯絡 Seasalt AI 支援：seachat@seasalt.ai。
