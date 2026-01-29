---
title: "WhatsApp 共存模式 (Coexistence)"
description: "Seasalt.ai 使用者可以將現有的 WhatsApp 商業應用程式 (Business App) 連結至 SeaX，在保留原生手機 App 的同時，整合 WhatsApp 雲端 API (Cloud API) 的強大功能。"
date: 2026-01-27T14:33:00-08:00
lastmod: 2026-01-27T14:33:00-08:00
draft: false
images: []
menu:
  seax:
    parent: "seax-omni"
aliases:
   - /seax/seax-messaging/whatsapp-coexistence/
url: /zh/seax/seax-omni/whatsapp-coexistence/
weight: 11
toc: true
---

**WhatsApp 共存模式 (WhatsApp Coexistence)** 是 Meta 推出的全新功能，讓企業主能夠在保留手機上原生 **WhatsApp 商業應用程式 (Business App)** 的同時，獲得 **WhatsApp 雲端 API (WhatsApp 商業平台)** 的企業級功能。

這項功能解決了小型企業面臨的「擴展難題」。過去，升級到 API 意味著必須放棄手機 App 的介面。透過共存模式，企業可以保留手機 App 的靈活性供個人使用或在外回覆，同時利用 Seasalt.ai 進行擴展，享受無限客服人數、整合收件匣和自動化功能。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-coexistence-illustration.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-coexistence-illustration.png" alt="WhatsApp 共存模式示意圖">
    </a>
</div>
</div>

## 🎥 影片教學

<iframe width="100%" height="400" src="https://www.youtube.com/embed/JPCbcEBlA50?si=Y3MraDbobI_jcm-h" title="WhatsApp 共存模式教學" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

本教學影片將示範如何設定 WhatsApp 共存模式，讓您能在手機原生 App、Seasalt.ai 網頁版儀表板以及 Seasalt.ai 手機 App 之間同步訊息。

### 本影片學習重點：
小型企業主常面臨兩難：保留方便的 WhatsApp 商業 App，還是升級到功能強大但失去原生介面的 API？本影片介紹的「WhatsApp 共存模式」是一項 Beta 版功能，讓您魚與熊掌兼得。觀看 SeaX 如何助您打破 4 個裝置的限制，在實體手機與網頁平台間即時同步聊天記錄，並讓員工能行動辦公，同時保持原本的商業 App 運作。

### 時間軸：
0:00 - WhatsApp 擴展難題：便利性 vs. 規模化

0:38 - 介紹 WhatsApp 共存模式：兩全其美的方案

0:54 - 解決方案：SeaX 整合收件匣

1:29 - 詳細設定步驟：將原生 App 連結至雲端

3:25 - 了解資料分享與同步規則

4:50 - 實機演示：手機與網頁儀表板即時同步

6:32 - 「三方同步」體驗：個人 App、商業 App 與平台

7:55 - 擴展您的團隊：使用 SeaX 手機 App 行動辦公

9:05 - 企業主體驗：完全掌控與靈活運用

### 先決條件

在設定 WhatsApp 共存模式之前，請確保您具備以下條件：

**裝置與帳號需求**
* 一支已安裝並啟用 **WhatsApp 商業應用程式 (Business App)** 的智慧型手機。
* 一個 **Meta Business Suite** 帳號 (使用 Facebook 登入)。
* 相關 Meta 企業管理平台 (Business Portfolio) 的管理員權限。

**平台存取權限**
* 有效的 Seasalt.ai 平台帳號。
* Seasalt.ai 中 **頻道 (Channels)** 設定選單的存取權限。

### 透過共存模式進行連線

#### 初始設定流程

1. **前往頻道設定**
   * 在 Seasalt.ai 中前往 **工作區 (Workspace)** → **頻道 (Channels)**。
   * 點擊 **新增頻道 (Add New Channel)**。
   * 選擇 **WhatsApp Coexistence** 選項 (Beta 版功能)。

2. **確認共存模式**
   * 系統會跳出確認視窗，說明此功能的好處 (在使用 API 的同時保持手機 App 運作)。
   * 點擊 **確認 (Confirm)** 繼續。

3. **使用 Facebook 登入**
   * 彈出視窗將要求您登入 Facebook/Meta 帳號。
   * 選擇您的 **企業管理平台 (Business Portfolio)** (例如 "Seasalt AI")。
   * 選擇您的 **WhatsApp 商業帳號**。

#### 選擇共存選項

這是區分共存模式與標準 API 連線的關鍵步驟。

1. **選擇「連結 WhatsApp 商業應用程式」(Connect a WhatsApp Business App)**
   * 在設定畫面中，尋找此選項：**Connect a WhatsApp Business App**。
   * *注意：此選項僅在 Meta 偵測到您符合共存模式 Beta 版資格時才會出現。*
   * 如果您希望保留 App 的聊天記錄，請 **不要** 選擇「建立 WhatsApp 商業帳號 (Create a WhatsApp Business Account)」。

2. **輸入電話號碼**
   * 輸入目前註冊在您 WhatsApp 商業 App 上的電話號碼。
   * 您可以在 App 的 **設定** → **商業檔案** → 向下滑動找到電話號碼。
   * 點擊 **下一步 (Next)**。

3. **驗證現有帳號**
   * Meta 會偵測到現有帳號。點擊 **下一步** 繼續。
   * 系統將提示您 **掃描 QR Code** 以連結 App。

#### 連結裝置

1. **掃描 QR Code**
   * 電腦螢幕上會出現標示為「連結至商業平台 (Connect to Business Platform)」的 QR Code。
   * 打開手機上的 **WhatsApp 商業應用程式**。
   * 前往 **設定** → **已連結裝置 (Linked Devices)** → **連結裝置**。
   * 掃描螢幕上顯示的 QR Code。

2. **確認資料分享**
   * 電腦上會提示詢問關於聊天記錄同步的事項。
   * 您可以分享最多 **6 個月** 的聊天記錄 (注意：僅限一對一聊天；群組聊天記錄不會被分享)。
   * 點擊 **確認 (Confirm)**。

3. **雙重確認**
   * 系統可能會要求您再次掃描 QR Code 進行安全確認。
   * 系統將開始處理連線 (這可能需要幾分鐘)。

4. **完成設定**
   * 連線成功後，您的 WhatsApp 手機 App 會收到來自 "Facebook Business" 的確認訊息。
   * 在 Seasalt.ai 中，點擊 **下一步** 和 **確認** 以完成設定。

### 功能與同步

連線完成後，您的業務將進入「三方同步 (Tri-Sync)」狀態，資料將在以下三個端點間同步：

1. **原生 WhatsApp 商業 App：** App 保留在您的實體手機上，您可以照常使用。
2. **Seasalt.ai 網頁版儀表板：** 所有接收和發送的訊息都會出現在這裡，供您的客服團隊使用。
3. **Seasalt.ai 手機 App：** 員工可以使用 Seasalt.ai App 在外回覆，無需使用老闆的實體手機。

#### 同步規則

* **接收訊息：** 會立即出現在手機原生 App、Seasalt.ai 網頁版以及 Seasalt.ai 手機 App 上。
* **發送訊息：**
  * 從 **原生手機 App** 發送的回覆會出現在 Seasalt.ai 中。
  * 從 **Seasalt.ai** (網頁或手機 App) 發送的回覆會出現在原生手機 App 中。
* **聊天記錄：** 最多 6 個月的一對一歷史聊天記錄會匯入 Seasalt.ai。群組聊天不會同步。
* **連線維護：** Meta 要求您每 **14 天** 至少打開手機上的 WhatsApp 商業 App 一次，以保持連線有效。

### 使用情境

**對於企業主：**
* 繼續使用熟悉的原生 WhatsApp 介面進行個人監控。
* 無需每天掃描 QR Code 登入網頁版。
* 在個人裝置上保留對所有客服活動的完整可視性。

**對於客服團隊：**
* **無限客服人數：**透過 Seasalt.ai 指派多位客服人員處理對話；突破原生 App 的 4 個裝置限制。
* **行動辦公：** 員工可以下載 **Seasalt.ai 手機 App**，用自己的手機回答客戶問題，無需直接存取老闆的 WhatsApp 帳號。
* **自動化：** 啟用 SeaChat AI 代理在非營業時間處理查詢 (需在 Seasalt.ai 中設定)。

### 疑難排解

**連線狀態**
* 如果訊息停止同步，請確認安裝 WhatsApp 商業 App 的主手機在過去 14 天內曾被開啟過。
* 檢查 Seasalt.ai 中的 **頻道 (Channels)** 分頁，確保號碼狀態為「已連線 (Connected)」。

**付款方式**
* 雖然原生 App 是免費的，但若要使用雲端 API 發送行銷範本訊息，需在 WhatsApp 企業管理平台中新增付款方式。
* 您可以在設定過程中或稍後在 Meta Business Suite 設定中新增。

**歷史訊息同步**
* 如果歷史聊天記錄沒有立即出現，請等待最多 24 小時讓初始同步完成。
* 請記住，共存模式不支援同步 **群組聊天 (Group Chats)** 的媒體和訊息。

## 運作流程

連線後，同步功能將在三個不同的平台上運作，創造統一的全通路體驗。

### 1. 企業主 (原生 App)
企業主在手機上保留原本的 **WhatsApp 商業 App**。他們可以正常發送和接收訊息。在此進行的所有活動都會即時鏡像同步到 Seasalt.ai 平台。

### 2. 客服團隊 (網頁版儀表板)
辦公室員工使用 **Seasalt.ai 網頁版儀表板**。
* **整合收件匣：** WhatsApp 訊息會與其他頻道 (簡訊、Instagram 等) 一起顯示。
* **指派功能：** 管理者可以將特定對話指派給無限數量的真人客服或 AI 代理。
* **規模化：** 解除 4 個裝置的限制，允許數百名客服人員同時在同一個 WhatsApp 號碼上工作。

### 3. 外勤員工 (Seasalt.ai 手機 App)
在外奔波的員工可以使用 **Seasalt.ai 手機 App** (與 WhatsApp App 不同)。
* 他們可以查看被指派的對話並回覆客戶。
* 從此 App 發送的訊息，在客戶端看起來就像是來自企業的 WhatsApp 號碼。
* 這些訊息也會同步回老闆的原生 WhatsApp 商業 App。

## 功能摘要

| 功能 | WhatsApp 商業 App | 雲端 API (標準版) | **WhatsApp 共存模式** |
| --- | --- | --- | --- |
| **裝置限制** | 4 個裝置 | 無限制 | **無限制 (透過 SeaX)** |
| **原生手機 App** | 有 | 無 | **有** |
| **聊天記錄同步** | 不適用 | 無 | **有 (最多 6 個月)** |
| **AI/機器人整合** | 有限 | 有 | **有** |
| **設定方式** | 電話號碼 | API 金鑰 | **掃描 QR Code** |