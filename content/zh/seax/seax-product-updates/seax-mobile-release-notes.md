---
title: "SeaX Mobile 版本發布資訊"
description: "即時掌握 SeaX Mobile 最新版本發布、效能優化與錯誤修復。"
date: 2026-01-08T08:48:57+00:00
lastmod: 2026-01-08T08:48:57+00:00
draft: false
images: []
menu:
  seameet:
    parent: "seax-product-updates"
aliases:
  - /zh/seax-mobile-release-notes/
  - /zh/seax/seax-mobile-release-notes/
# NOTE: All product update pages should follow the URL format: https://wiki.seasalt.ai/${language}/${product}/product-updates/
url: /zh/seax-mobile/product-updates/
weight: 410
toc: true
---

專注於 SeaX Mobile 的功能迭代與修復。如需查看完整的 SeaX 全通路更新，請前往 [SeaX 版本發布資訊](/zh/seax/product-updates/)。

### 0.0.2

##### **<font color="#739963">新功能與改善</font>**

- MessageBubble 重新設計，為音訊／影片／未同步媒體加入方向標籤、動態時間戳、佔位圖與錄音卡片，並以在地化字串顯示「Inbound / Outbound」與 WhatsApp 同步限制。
- ConversationDetail / ConversationList hook 具備網路狀態感知、Twilio 專屬排序欄位與重試、WebSocket 生命週期記錄，降低離線復原時的錯誤。
- 對話畫面整合 route 與 store 的 workspace / phone fallback，並採用 KeyboardAvoidingViewCompat、handlingStatus、ChannelIcon、ContactAvatar 改善標頭與輸入體驗。
- DialerScreen 大幅重構，導入 MD3 DialPad、PhoneSelectField、工作區電話 lazy load、全螢幕搜尋／聯絡人建議、麥克風權限提醒、DEV 診斷面板與跨畫面預填號碼。
- ActiveCallScreen 能依 Twilio call parameters 與 workspace 聯絡人解析顯示名稱；CallLog / IncomingCall / PhoneSelection 共用 PhoneSelectField 與 loadWorkspacePhones，確保一致的電話資訊。
- Android 新增 EarlyInitProvider 與 ReactNativeInitializer，並更新 AppProviders、StatusBarBackground、useOptionalNetInfo 及 package / babel / metro / jest / i18n，提升啟動穩定度。

##### **<font color="#d66a60">問題修正</font>**

- Conversation sockets 依網路連線與 Twilio 排序自動重試，避免重新連線後訊息重複或順序錯亂。
- CallLog、PhoneSelection、ActiveCallScreen 若無法載入 workspace phone meta，會記錄錯誤並顯示 fallback 描述，避免畫面空白。
- Android 開機預載 React Native 與 Twilio Voice，修復背景通知服務偶發無法連線的情況。
- 微調 KeyboardAvoidingViewCompat 在 iOS / Android 的 offset，防止對話輸入列被系統鍵盤遮蔽。

### 0.0.1

##### **<font color="#739963">新功能與改善</font>**

- 建立 Seasalt rebrand 基礎版，將行銷版本與 build number 重置為 0.0.1，統一 bundle identifier 並更新 scripts、環境檔與文件。
- 完成初版 React Native 體驗：登入、workspace 選擇、對話列表與詳情、Twilio Voice 通話、推播與 Caller ID 設定。

##### **<font color="#d66a60">問題修正</font>**

- 統一 MARKETING_VERSION / versionName 以及 build number 起點，消除 iOS 與 Android 版本衝突。
