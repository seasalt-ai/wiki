---
title: "WhatsApp Business Platform 商業平台"
description: "SeaX 使用者可以將 WhatsApp 商業平台 連接至 SeaX，以整合 WhatsApp Cloud API。"
date: 2024-12-21T08:48:57+00:00
lastmod: 2024-12-21T08:48:57+00:00
draft: false
images: []
url: /zh/seax/seax-omni/seax-whatsapp-business-platform/
weight: 10
toc: true
---

SeaX 使用者可以將 WhatsApp 商業平台 連接至 SeaX，以整合 Meta Cloud API。

此功能允許使用者存取其 Meta Business Manager 帳戶，並直接從 SeaX 管理客戶通訊管道。

在 Meta Business Manager 上運營的高級使用者終於可以體驗真正的全通路溝通，將所有客戶互動統一在一個平台上。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/wa-business-platform-ui.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/wa-business-platform-ui.png" alt="WhatsApp 商業平台 UI">
    </a>
</div>
</div>

## 🎥 視頻教程 (英文)

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/3cqNHzvlZ1k?list=PL8K7_LTqly45pLJ1NAw3P3VlPseovylOC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

⏰ **時間戳記：**
- 00:00 介紹與平台概覽
- 00:24 WhatsApp Business Platform 需求
- 01:59 了解 WhatsApp 應用程式類型
- 03:06 將 WhatsApp 連接到 SeaX 平台
- 04:18 驗證連接狀態
- 04:32 設定批量發送行銷活動
- 05:01 上傳聯絡人與 CSV 模板
- 07:24 創建和管理訊息模板
- 09:19 模板同步
- 09:38 行銷活動設定與審查
- 10:09 發送您的行銷活動
- 10:32 接收和回覆訊息
- 11:45 監控行銷活動結果
- 12:42 總結與最佳實務
- 13:54 SeaChat AI 整合預覽

本指南提供使用 SeaX 平台創建和管理 WhatsApp 批量行銷活動的逐步說明。

### 先決條件

在開始您的 WhatsApp 行銷活動之前，請確保您擁有：

**WhatsApp Business Platform 設定**
- 已註冊的 WhatsApp Business Platform 帳戶 (Meta Cloud API)
- 狀態為「已連接」且品質評級為「高」的電話號碼
- Meta 核准的訊息模板

**平台存取權限**
- 有效的 SeaX 平台帳戶
- 在您的工作區中已連接的 WhatsApp Business Platform

### 連接 WhatsApp Business Platform

#### 初始連接流程

1. **導航到工作區設定**
   - 前往 **工作區** → **頻道**
   - 選擇 **WhatsApp Business Platform**

2. **新增您的帳戶**
   - 點擊 **新增帳戶** 按鈕
   - 使用您的 Meta Business Suite 憑證登入
   - 選擇您的商業帳戶（例如「Seasalt AI」）
   - 選擇您已註冊的 WhatsApp Business 號碼
   - 完成連接流程

3. **驗證連接狀態**
   - 確保所有號碼顯示「已連接」狀態並有綠色指示器
   - 在 Meta Business Manager 中驗證品質評級為「高」

### 模板管理

#### 在 Meta 中創建模板

WhatsApp Business Platform 要求所有訊息模板都必須經過 Meta 預先核准。

1. **存取 Meta WhatsApp Manager**
   - 前往 **管理模板** 部分
   - 點擊 **創建模板** 按鈕

2. **模板配置**
   - 選擇模板類別（例如行銷）
   - 新增模板名稱和內容
   - 使用雙括號包含變數：`{{name}}`
   - 如需要，新增媒體範例（圖片、影片、文件）
   - 配置操作按鈕（網站造訪等）

3. **提交審查**
   - 點擊 **提交審查**
   - 等待 Meta 核准後使用

#### 將模板同步到 SeaX

一旦模板在 Meta 中獲得核准：

1. 導航到 **頻道** → **WhatsApp Business Platform**
2. 點擊 **從 WhatsApp 同步** 按鈕
3. 已核准的模板將出現在您的 SeaX 模板庫中

### 聯絡人管理

#### 個別聯絡人創建

1. 前往 **聯絡人** 部分
2. 點擊 **新增聯絡人**
3. 輸入聯絡人詳細資訊：
   - 姓名
   - E.164 格式的 WhatsApp 號碼（例如 +1234567890）
   - 用於分群的標籤
   - 其他備註

#### 批量聯絡人上傳

**CSV 模板方法：**

1. **下載模板**
   - 點擊 **從 CSV 匯入**
   - 下載聯絡人模板檔案

2. **準備您的資料**
   - 填入必填欄位：姓名、WhatsApp 號碼、標籤
   - 所有電話號碼使用 E.164 格式
   - 多個標籤用逗號分隔
   - 包含其他欄位：地址、商業電子郵件等

3. **上傳流程**
   - 將您的 CSV 檔案拖放到上傳區域
   - 系統將處理並驗證聯絡人
   - 透過標籤篩選器審查已上傳的聯絡人

### 創建批量行銷活動

#### 行銷活動設定流程

1. **存取批量發送**
   - 導航到 **批量發送和通話**
   - 選擇 **WhatsApp** 選項

2. **選擇收件人**
   - 選擇聯絡人標籤（例如「WA1」、「WA2」）
   - 預覽選定的聯絡人
   - 點擊 **繼續**

3. **配置發送者**
   - 選擇您的 WhatsApp Business 號碼
   - 新增包含日期的行銷活動名稱以便追蹤

4. **選擇模板**
   - 從已同步的模板中選擇
   - 預覽包含變數替換的模板
   - 審查前幾個聯絡人的訊息內容

#### 發送您的行銷活動

1. **最終審查**
   - 驗證收件人數量和模板內容
   - 檢查變數替換的準確性

2. **發送流程**
   - 點擊 **立即發送**
   - 系統提供 10 秒的取消視窗
   - 行銷活動立即開始處理

### 監控行銷活動效果

#### 即時追蹤

**行銷活動儀表板：**
- 存取 **行銷活動** → **WhatsApp** 部分
- 檢視傳送統計：已傳送、失敗等
- 在 **記錄** 中監控個別訊息狀態

**訊息狀態類型：**
- **已傳送**：收件人成功接收
- **失敗**：傳送不成功（附錯誤詳情）
- **已讀**：收件人已開啟訊息

#### 管理回覆

**24 小時回覆視窗：**
- WhatsApp Business Platform 在客戶聯絡後提供 24 小時的回覆視窗
- 回覆出現在 **對話** 標籤中
- 可在回覆視窗內發送手動回覆

**自動回覆整合：**
- 考慮使用 SeaChat AI 進行 24/7 自動回覆
- 與 WhatsApp 行銷活動無縫整合

### 最佳實務

**聯絡人管理：**
- 維護乾淨、分段的聯絡人清單並使用相關標籤
- 所有電話號碼一致使用 E.164 格式
- 定期更新和驗證聯絡人清單

**模板策略：**
- 為不同的行銷活動類型創建模板
- 使用變數進行個人化
- 確保符合 Meta 規範以獲得核准

**行銷活動優化：**
- 監控傳送率並調整策略
- 追蹤回覆率以評估模板效果
- 為目標訊息分群受眾

### 疑難排解

**常見問題：**
- **傳送失敗**：檢查電話號碼格式和收件人 WhatsApp 狀態
- **模板同步問題**：驗證 Meta 核准狀態並重新同步
- **連接問題**：在 Meta Business Manager 中確認 WhatsApp Business Platform 狀態

**平台限制：**
- SeaX 平台對聯絡人上傳無限制
- 無論聯絡人數量多少，定價保持一致
- 模板必須經過 Meta 預先核准


## (圖片版) 如何將 WhatsApp 商業平台 連接到 SeaX

前往 **Workspace** 下的 **Channel**，然後點擊 WhatsApp 商業平台 標籤。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/choose-icon.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/choose-icon.png" alt="選擇 WhatsApp 商業平台 圖示">
    </a>
</div>
</div>

點擊 **Add Account** 以將您的 Meta Business Manager 帳戶連接到 SeaX。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/add-account-btn.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/add-account-btn.png" alt="新增帳戶按鈕">
    </a>
</div>
</div>

## 新增 Meta Business Manager 帳戶

按照系統自動生成的步驟，將您的 Meta Business Manager 帳戶連接至 SeaX。

1. 登入您的 Facebook 帳戶。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/meta-step-1.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/meta-step-1.png" alt="Meta WhatsApp Cloud API | 步驟 1">
    </a>
</div>
</div>

2. 連接您的帳戶至 Seasalt AI LLC。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/meta-step-2.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/meta-step-2.png" alt="Meta WhatsApp Cloud API | 步驟 2">
    </a>
</div>
</div>

3. 填寫企業資訊：請確保正確填寫企業資訊，並確保 Business Portfolio 中包含您要連接的可用號碼。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/meta-step-3.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/meta-step-3.png" alt="Meta WhatsApp Cloud API | 步驟 3">
    </a>
</div>
</div>

4. 創建 WhatsApp Business Profile。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/meta-step-4.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/meta-step-4.png" alt="Meta WhatsApp Cloud API | 步驟 4">
    </a>
</div>
</div>

## WhatsApp 訊息傳送規則

1. **客戶發起對話**  
   客戶可以主動與企業聯繫，企業可在 24 小時內自由回覆這些訊息。

2. **企業發起對話**  
   企業無法直接向客戶發送新訊息，除非使用 **預先核准的範本訊息**。

3. **範本訊息**  
   範本訊息允許企業向客戶發送第一條訊息，並開啟 24 小時的自由對話窗口，期間可發送額外的自由格式訊息。

4. **支付方式要求**  
   發送範本訊息需要有效的支付方式，否則無法發送範本訊息。

## 進一步了解 WhatsApp 商業平台

如需更深入瞭解 WhatsApp 商業平台 的 API 功能或訊息政策，Meta 提供了詳細的指南與資源。請造訪 [Meta for Business Help Center](https://www.facebook.com/business/help/2640149499569241) 以探索：

- 使用 WhatsApp 商業平台 與客戶交流的最佳實踐。
- 訊息政策的詳細資訊，包括對話窗口與範本訊息規則。
- 提高每日訊息傳送限制和驗證企業的方法。
- 排解常見問題並理解品質評分系統。

此資源對於希望充分利用 WhatsApp 商業平台 並符合 Meta 政策的企業與解決方案提供者而言非常有價值。

## 從 WhatsApp 同步數據

添加您的 Meta Business Manager 帳戶後，您可以將 WhatsApp 號碼和帳戶同步到 SeaX。點擊 **Sync from WhatsApp**，SeaX 會自動同步您的 WhatsApp 號碼和帳戶。

現在，您可以直接從 SeaX 存取 Meta Business API 的功能，並統一管理所有客戶互動。

## 與 SeaChat 和 SeaX 的進一步整合

SeaX 使用者現在可以在 Meta Business Manager 上完全處理其業務邏輯，並透過 SeaX 與客戶進行溝通。此外，透過進一步整合 SeaChat，企業可以自動化客戶互動並提升業務運營效率。
