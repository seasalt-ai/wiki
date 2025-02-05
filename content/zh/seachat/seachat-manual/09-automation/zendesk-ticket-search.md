---
title: "Zendesk 工單搜尋工具"
description: ""
date: 2025-02-04-T00:22:19-07:00
date: 2025-02-04-T00:22:19-07:00
draft: false
weight: 54
url: zh/seachat/seachat-manual/automation/zendesk-ticket-search
---

SeaChat Zendesk 工單搜尋工具是 Seasalt.ai 提供的一項創新功能，透過將 複雜的 Zendesk 工單數據 轉換為 直接且具上下文關聯性的回應，優化客戶支援流程。為避免使用者在大量搜尋結果中篩選並手動開啟每張工單，SeaChat 會從完整的工單對話中擷取關鍵資訊，並在單次互動內提供精確的答案。

---

## 運作方式

SeaChat Zendesk 工單搜尋工具利用 Zendesk API 的強大功能，透過以下步驟來處理使用者查詢並提供最佳答案

&nbsp;&nbsp;&nbsp;&nbsp; **1. 關鍵字提取:**

當使用者提交查詢時，SeaChat 會自動解析輸入內容，並提取一個或多個關鍵字。這些關鍵字將用於向 Zendesk 搜尋 API 發送查詢請求。

&nbsp;&nbsp;&nbsp;&nbsp; **2. 透過 Zendesk 搜尋 API 查詢工單:**

SeaChat 透過 Zendesk 搜尋 API `/api/v2/search.json?query=xxx` 發送請求，並獲取符合搜尋條件的工單列表。值得注意的是，Zendesk 搜尋 API 的初始回應僅包含每張工單對話串的第一則留言（通常是工單的描述），作為工單內容的預覽。

&nbsp;&nbsp;&nbsp;&nbsp; **3. 檢索完整的工單互動:**

為了獲取更完整的資訊，SeaChat 會針對搜尋結果中的每張工單，進一步調用 Zendesk 工單留言 API `/api/v2/tickets/{id}/comments`。
此步驟可擷取該工單的所有留言，包括後續回覆，客服代理的回答，內部備註。

&nbsp;&nbsp;&nbsp;&nbsp; **4. 生成答案:**

SeaChat 透過自然語言處理（NLP）分析完整的工單對話內容，以找出最相關的資訊，並為使用者提供直接且可行的答案。若有多張工單的內容與查詢相關，SeaChat 會整合多個工單的資訊來提供最佳回應。

---

## 使用案例

SeaChat Zendesk 工單搜尋工具用途廣泛，可應用於多種客服與業務場景，提升工作效率並改善客戶體驗。以下是幾個最佳使用案例：

&nbsp;&nbsp;&nbsp;&nbsp; -- **加速客服回應:**
客服人員可以透過利用歷史工單資料快速擷取客戶問題的完整答案，從而減少手動搜尋工單所花費的時間。

&nbsp;&nbsp;&nbsp;&nbsp; -- **自動知識庫擴充:**
透過整合頻繁的查詢及其相應的解決方案，該工具可以幫助自動更新常見問題解答和知識庫文章，確保自助服務選項始終最新且準確。

&nbsp;&nbsp;&nbsp;&nbsp; -- **根本原因分析:**
支援經理可以利用該工具來分析工單對話中的模式（例如重複出現的問題或常見的故障排除步驟），以提高產品可靠性和客戶滿意度。

&nbsp;&nbsp;&nbsp;&nbsp; -- **高效數據整合:**
將 Zendesk 與其他系統（例如 CRM 平台或分析儀表板）整合時，該工具能夠提取全面的工單信息，從而實現更有效的跨平台數據分析和報告。

---

透過將 Zendesk 搜尋 API 的強大搜尋功能與工單評論 API 提供的詳細見解相結合，SeaChat 為傳統 Zendesk 搜尋 UI 提供了無縫且高效的替代方案。這種創新方法不僅加快了解決過程，還提高了支援回應的整體品質。

## **配置 Zendesk 工單搜尋工具的步驟:**

若要設定此功能，請登入 SeaChat 後，導覽至AI助理配置 \-\> 整合 \-\> 客制GPT工具。

### **步驟 1：選擇工具類型**

按一下 **「新增的自訂 GPT 工具」**，然後選擇 **Zendesk Ticket Search** 作為工具類型。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image1.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image1.png"  alt="Example of New Custom Tool">
</a>
<br/>
</center>

### **步驟 2：新增 Zendesk 帳戶信息**

要設定 Zendesk 工單搜尋工具，您需要提供幾個關鍵資訊：

- 啟用工具：開啟啟用開關。這將啟動該工具，允許 SeaChat 在相關對話中自動開始使用它。
- 工具名稱：輸入工具的名稱。它應只包含字母（A-Z、a-z）、數字（0-9）、底線（\_）或連字號（-），不包含任何空格。
- 描述：詳細描述 SeaChat 可以在 Zendesk 中找到哪些資料以及在什麼條件下應啟動此自訂工具。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image2.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image2.png"  alt="Example of New Custom Tool">
</a>
<br/>

_Example: 設定Zendesk工單搜尋工具來檢索工單、產品名稱和價格。_

</center>

您還需提供以下 Zendesk 帳戶信息，以允許 SeaChat 安全地存取和搜尋工單。

- **子網域**：您的 Zendesk 子網域是 Zendesk URL 的第一部分。例如Zendesk URL 是：*https://seasaltai9494.zendesk.com*，那麼子網域是 _seasaltai9494_。
- **電子郵件**：輸入與您的 Zendesk 帳戶關聯的電子郵件地址。這與您用於登入的電子郵件地址相同。
- **API Token**：它驗證 SeaChat 對您的 Zendesk 帳戶的存取權限，要產生 API Token，請按照以下步驟操作：

1. 登入您的 Zendesk 管理中心。
2. 在左側邊欄中，前往應用程式和整合 → Zendesk API。
3. 在「設定」標籤下，找到「Token存取」部分。
4. 切換啟用 API Token存取（如果尚未啟用）。
5. 點選新增 API Token。
6. （可選）新增 API Token的描述。
7. 複製產生的 API Token並安全儲存（不會再次顯示）。
8. 點選「儲存」。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image3.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image3.png"  alt="Example of New Custom Tool">
</a>
<br/>

_Example: 輸入 Zendesk 帳戶憑證來驗證 SeaChat 的 API 存取權。_

</center>

### **步驟 3：定義搜尋參數**

您可以自定義搜尋參數來控制 Zendesk 工單的擷取和顯示方式。

- **per_page：** 決定在單一請求中檢索的工單數量。建議將此值設為 1 到 20 之間，預設值為 5。對於每個檢索到的工單，SeaChat 將調用 Zendesk API 使用以下端點獲取其詳細資訊和評論：`GET https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_no}/comments`。由於 SeaChat 會檢索每個工單的所有評論，因此增加每個請求的工單數量可能會減慢回應時間。
- **sort_by**：定義檢索到的工單的排序標準。您可以選擇按工單的上次更新時間 (updated_at)、建立時間 (created_at)、優先權 (priority)、狀態 (status) 或類型 (ticket_type) 進行排序。預設情況下，排序基於相關性。
- **sort_order**：指定工單是否應按升序（asc）或降序（desc）排序。預設是降序。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image4.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image4.png"  alt="Example of New Custom Tool">
</a>
<br/>

_設置每次取得 10 張工單及其評論，並按更新順序降序排列（從最新到最舊）。_

</center>

### **步驟 4（可略）：測試您的設定**

在最終確定之前，您可以透過輸入關鍵詞（例如**產品名稱、訂單號或相關關鍵詞**）來測試工具。點擊**提交**發送測試請求。如果成功，您將看到即時 Zendesk 搜尋結果顯示在右側。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image5.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image5.png"  alt="Example of New Custom Tool">
</a>
<br/>

_使用產品名稱關鍵詞「452-ABC」進行測試，並成功檢索到與該產品相關的工單評論。_

</center>

### **步驟5：儲存設定**

點擊「儲存」，您的 Zendesk Ticket Search 工具就可以使用了。您的 SeaChat AI 代理現在可以檢索 Zendesk工單資料以增強客戶支援。
