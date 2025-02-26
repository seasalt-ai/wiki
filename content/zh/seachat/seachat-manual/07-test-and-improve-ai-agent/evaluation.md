---
title: "評估：透過測試集增強 AI智能助理響應準確性"
description: "透過測試集增強 AI智能助理響應準確性"
date: 2025-02-25T00:22:19-07:00
lastmod: 2025-02-25T00:22:19-07:00
draft: false
weight: 503
aliases:
  - /zh/seachat/seacaht-manual/07-test-and-improve-ai-agent/evaluation
---

## **1\. 概述**

SeaChat 中的 **評估** 功能可讓使用者透過將實際回應與預先定義的黃金回應進行比較來系統化測試其 AI智能助理程式的效能。它使用大型語言模型來評估測試集並分配正確性分數來確定反應品質。它可以幫助企業**監控、測試和改進**其AI智能助理的效能。

- 它透過將即時助理答案與黃金標準進行比較來確保高品質的回應。
- 使用者可以透過定期測試回應和調整知識庫內容來完善他們的AI智能助理模型。
- 與真實客戶對話的無縫整合允許用戶動態改進AI智能助理。

## **2\. 使用案例**

### **📌用例 1：AI智能助理程式回應的品質保證**

**電子商務公司**的客戶支援團隊希望確保他們的AI智能助理商提供**準確的退貨政策資訊**。

- 他們創建了一個**測試集**，其中包含**常見的退貨相關問題**。
- 他們根據公司政策輸入**黃金回應**。
- 測試運行後，他們發現 **30% 的反應不正確**。
- 他們更新**知識庫**並重新運行測試，提高AI智能助理的準確性。

✅ **結果：** AI智能助理現在提供 **正確的退貨政策答案**，減少 **客戶糾紛升級**。

---

### **📌用例 2：AI智能助理效能監控**

一家使用 SeaChat 的 SaaS 公司希望透過**產品故障排除查詢**追蹤 AI 效能。

- 每個月，他們都會執行**包含 100 多個常見問題的測試集**。
- 他們比較一段時間內的正確性分數以**跟踪改進**。
- 當分數下降時，他們會分析**錯誤的反應和知識庫差距**。

✅ **結果：** 主動監控可防止 **客戶滿意度下降** 並 **提高支援效率**。

---

### **📌用例 3：改進 AI智能助理程式以實現多語言支援**

一家**全球航空公司**想要測試其AI智能助理處理**不同語言的客戶查詢**的能力。

- 他們為**英語、西班牙語和法語**查詢建立測試集。
- 他們使用**由人工翻譯驗證的黃金回應**。
- 測試運行顯示AI智能助理在處理**法國航班重新安排查詢**時遇到困難。
- 他們改進**法語語言知識庫**並重新測試。

✅ **結果：**AI智能助理提供**準確的多語言支援**，減少**溝通不良**。

---

### **📌用例 4：訓練 AI智能助理程式以獲得行業特定知識**

**醫療保健提供者**使用 SeaChat **自動化患者常見問題解答**。

- 他們創建了一個**包含醫療保險問題的測試集**。
- 他們添加了**由醫療專業人員撰寫的黃金回應**。
- 測試結果顯示**關於覆蓋範圍限制的答案不一致**。
- 他們完善**AI智能助理描述和知識庫並重新運行測試**以確保正確性。

✅ **結果：**AI智能助理現在提供**可信的醫療指導**，確保**合規性和準確性**。

## **3\.如何設定**

### **第 1 步：導覽至「評估」標籤**

1. 登入**SeaChat**。
2. 點選左側邊欄中的**評估**標籤。

### **步驟 2：建立新的測試集**

1. 點選評估標籤中的 **三點選單** (⋮)。
2. 選擇**「新增測試集」**。
3. 輸入**測試集名稱**。
4. 設定 **單一測試樣本成功閾值** 和 **測試集成功閾值**（值介於 **0 和 1** 之間）。這些閾值決定響應是否正確。
5. 按一下**確認**建立測試集。

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/2add-a-new-set.png"  alt="Add a new set">
</a>

_點擊 +新增 以添加_

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/3new-set-input.png"  alt="Add new test configurations">
</a>

_配置被認為正確的集合名稱和閾值_

</center>

### **步驟 3：新增測試樣本**

1. 點選測試集中的 **「新增樣本」** 按鈕。
2. **配置測試樣本：**
   - **對話歷史記錄：** 新增與過去的 **使用者/助理訊息** 相關的上下文。
   - **使用者測試查詢：** 將測試的確切使用者訊息。
   - **黃金特工回應：** 用於比較的理想 AI 生成回應。
3. 按一下「**儲存**」以新增測試樣本。

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/4add-sample.png"  alt="Add a new test sample">
</a>

_範例：向問答測試集新增使用者測試查詢和助理黃金回應_

</center>

### **步驟 4：執行測試集**

1. 點擊測試集旁邊的**運行**圖標，然後點擊彈出視窗中的確認按鈕
2. 導覽至 **測試運行** 標籤以查看結果。

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/5run-set.png"  alt="Click Run button to run">
</a>

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/6confirm-run.png"  alt="Click Run button to run">
</a>

</center>

### **第 5 步：查看測試運行結果**

1. 在 **測試運行** 標籤中查看所有測試運行

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/7test-run-page.png"  alt="Navigate to Test Runs tab to view results">
</a>

</center>

<br/>

2. 點選已完成的測試運行即可查看：
   - 測驗集的**整體正確性分數**。
   - **每個測驗樣本的正確性分數**。
   - **實際 AI智能助理響應與黃金響應**。
   - AI智能助理引用的 **知識庫文章**。
3. 如果需要，**編輯知識庫文章**以改進AI智能助理回應。

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/8test-run-result.png"  alt="Click one item to view the results in detail">
</a>

\_範例：第一個查詢的正確性分數為 19.55%，第二個查詢的分數為 65.47%，整體正確性為 43.51%。

</center>

### **步驟 6：新增真實對話的測試樣本**

1. 在即時對話期間，如果 AI智能助理提供了有待改進或異常的回應，請按一下 **點贊/不喜歡** 按鈕。
2. 回覆將顯示在 **「需求審核」** 標籤下。
3. 按一下回應，然後選擇 **“+ 新增至測試集”**。
4. 選擇 **測試集名稱** 並配置：
   - **對話歷史記錄**
   - **使用者測試查詢**
   - **黃金特工回應**
5. 點選**儲存**。現在，測試樣本已添加到測試集中以供將來評估。
6. 重複**步驟 4 和步驟 5** 重新執行測試並完善AI智能助理回應。
   <br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/11needs-review-page.png"  alt="Click Add to Test Set button to add to a test set">
</a>

_範例：在需求審核頁面中，按一下 + 新增至測試集按鈕將助理回應新增至測試集_。

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/12add needs review message to a test set.png"  alt="Modify sample to be added to the test set">
</a>

_範例：新增使用者訊息並修改助理黃金回應，然後將此範例新增至問答測試集中。_

</center>

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/13new sample in test set.png"  alt="View the newly added test sample">
</a>

_範例：導覽至評估頁面，這條問題已新增至測試集中_。

</center>

## **3\.定價**

測試運行會消耗AI智能助理回應條數，並將相應地計費。測試集中的每個測試案例價格為 **$0.01美金**。

## **4\.匯入和匯出評估測試集**

有效管理評估測試集對於優化 AI 模型效能至關重要。該系統允許使用者**匯出**測試集以進行備份、編輯或共享，並**匯入**它們以進行批量更新。請依照下列說明**匯出**或**匯入**測試集。

### **使用案例**

匯入和匯出評估測試集在多種場景中都有好處，例如：

1. **資料備份和復原** - 定期匯出測試集以建立備份，確保不會遺失關鍵測試資料。
   - 如果評估測試集被意外刪除或修改，使用者可以透過匯入先前儲存的 JSON 檔案輕鬆恢復。
2. **協作和共享** - 從事 AI 模型評估的團隊可以透過將測試集匯出到 JSON 檔案並在不同環境中共享來共享測試集。
   - 當不同的團隊需要使用相同的測試案例驗證或基準測試 AI 模型時，這特別有用。
3. **批次管理和編輯** - 使用者可以**匯出**測試集，批次編輯JSON文件，然後**匯入**回系統，而不用手動逐一新增測試樣本。
   - 這加快了測試集的更新和修改，確保一致性並減少手動工作。
4. **跨環境遷移測試集** - 使用者可以透過從一個環境匯出測試集並將其匯入到另一個環境中，在**暫存、開發和生產環境**之間移動測試集。
   - 這確保了人工智慧模型在不同環境中得到一致的測試。
5. **AI 模型基準測試** - 使用者可以建立標準化測試集，以對 AI 模型隨時間的改進進行基準測試。
   - 匯出和匯入測試集允許重複使用相同的評估集來有效追蹤進度。

## **如何匯出評估測試集**

1. 導覽至 **評估** 標籤。
2. 點選要匯出的評估測試集旁邊的**三點選單** (⋮)。
3. 從下拉式選單中選擇 **匯出此集**。

<center>
<a href="/images/seachat/en/evaluation/export-import-menu.png">
<img height="100%" width="40%" src="/images/seachat/en/evaluation/export-import-menu.png"  alt="Option menu">
</a>

</center>

4. 將出現一個通知窗口，其中包含 JSON 檔案的連結。
5. 按一下連結 — 它將在新分頁中開啟 JSON 檔案。
6. 右鍵單擊新選項卡並選擇 **另存為** 以下載 JSON 檔案。

<center>
<a href="/images/seachat/en/evaluation/export-success.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/export-success.png"  alt="Export success message">
</a>

</center>

### **匯出的 JSON 檔案範例：**

```{
  "id": "baded98d44024b63964a866c5c1670d3",
  "name": "customerQ&A",
  "set_success_threshold": 0.8,
  "sample_success_threshold": 0.8,
  "samples": [
    {
      "id": "8be53adf616a451d8282a6455f3f346d",
      "user_test_query": "What products do you offer?",
      "agent_gold_response": "We offer SeaX Messaging, SeaMeet, SeaChat, SeaVoice (including Discord bot), and SeaX Enterprise contact center solution.",
      "conversation_history": { "messages": [] }
    },
    {
      "id": "a6455f3f346d8be53adf616a451d8282",
      "user_test_query": "I need to use it with LINE, do you support it?",
      "agent_gold_response": "Yes, SeaChat can be integrated with LINE to respond to customer messages effectively.",
      "conversation_history": {
        "messages": [
          { "role": "user", "content": "Tell me all about SeaChat" },
          {
            "role": "assistant",
            "content": "SeaChat is an AI-powered intelligent chatbot that automates responses to customer queries and transitions to human support when needed."
          }
        ]
      }
    }
  ]
}
```

## **如何從檔案匯入**

1. 導覽至 **評估** 標籤。
2. 點選**三點選單** (⋮) 並選擇 **「從檔案匯入」**。
3. 點選選擇 JSON 檔案或將其拖曳到上傳視窗中。
4. 上傳後，按一下 **「完成」** 完成該過程。

<center>
<a href="/images/seachat/en/evaluation/import-success.png">
<img height="100%" width="50%" src="/images/seachat/en/evaluation/import-success.png"  alt="Export success message">
</a>

</center>

### **用於匯入的範例 JSON 檔案：**

```{
  "name": "customerQ&A",
  "set_success_threshold": 0.8,
  "sample_success_threshold": 0.8,
  "samples": [
    {
      "user_test_query": "What products do you offer?",
      "agent_gold_response": "We offer SeaX Messaging, SeaMeet, SeaChat, SeaVoice (including Discord bot), and SeaX Enterprise contact center solution.",
      "conversation_history": { "messages": [] }
    },
    {
      "user_test_query": "I need to use it with LINE, do you support it?",
      "agent_gold_response": "Yes, SeaChat can be integrated with LINE to respond to customer messages effectively.",
      "conversation_history": {
        "messages": [
          { "role": "user", "content": "Tell me all about SeaChat" },
          {
            "role": "assistant",
            "content": "SeaChat is an AI-powered intelligent chatbot that automates responses to customer queries and transitions to human support when needed."
          }
        ]
      }
    }
  ]
}
```

如果您需要進一步協助，請隨時聯絡[seachat@seasalt.ai](mailto:seachat@seasalt.ai)！ 🚀
