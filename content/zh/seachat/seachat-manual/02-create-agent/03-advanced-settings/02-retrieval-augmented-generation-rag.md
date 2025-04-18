---
title: "檢索增強生成 (RAG)"
description: "探索 SeaChat 的進階設置，包括助理記憶和檢索增強生成 (RAG)。了解如何優化您的 AI 助理的性能和即時用戶互動。"
lead: ""
date: 2024-05-29T08:48:45+00:00
lastmod: 2024-05-29T08:48:45+00:00
weight: 106
draft: false
images: []
toc: true
aliases:
  - /zh/seachat/seachat-manual/02-create-agent/03-advanced-settings/02-retrieval-augmented-generation-rag
url: /zh/seachat/manual/create-agent/advanced-settings/rag
---

## 簡介

檢索增強生成 (RAG) 是 SeaChat 中一個進階功能，增強了知識檢索和 AI 助理互動的準確性。通過提供您調整查詢模式、選擇檢索方法和定義知識庫檢索數量的能力，優化了 AI 助理的性能。

---

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-rag-ui" href="/images/seachat/zh/agent-advanced-settings/rag-dashboard.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/rag-dashboard.png" alt="檢索增強生成 (RAG) 在 SeaChat 中的設置圖">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">SeaChat 中的 RAG 設置</p></p>
</div>

## [檢索查詢模式](#seachat-rag-ui)

無論您需要全面的上下文、專注的互動，還是快速、精確的回應，SeaChat 靈活的查詢模式確保了優化的聊天體驗，以滿足您的偏好。

以下是客戶與停車場 FAQ AI 助理之間的示例對話，知識庫中包含數百個停車場的資料：

---

👨 (上一用戶提問)：西雅圖太空針塔附近有停車場嗎？

🤖️ (AI助理機器人回應)：是的，您可以停在位於 123rd Ave NE 的 ABC 停車場。該停車場有 50 個車位。停車費每小時 $10 起，全天最多 $60。

👨 (當前用戶提問)：我會在那附近工作，可以每月租一個停車位嗎？

---

### 前一用戶提問 &#8594; 機器人回應 &#8594; 當前用戶提問

通過結合對話的前三輪提供全面的上下文。在這種情況下，完整的對話（上一用戶提問 + 機器人回應 + 當前用戶提問）將用於查詢知識庫並生成機器人對當前用戶提問的下一個回應。

### 上一用戶提問 &#8594; 當前用戶提問

更加關注用戶的請求，不受機器人回應的影響。它包括最近兩個用戶輸入（上一用戶提問 和 當前用戶提問）來查詢知識庫並生成機器人對下一個回應。

### 當前用戶提問

只考慮用戶的最新提問，即當前用戶提問，用於生成機器人的下一個回應。這對於一次性對話或用戶頻繁切換主題的情況非常理想。然而，在多輪對話中討論相同主題時，它可能會忽略重要的上下文。

## [檢索方法](#seachat-rag-ui)

您可以通過選擇不同的知識庫檢索方法來優化知識庫檢索：

### Keyword Search (關鍵字檢索)

根據用戶提供的關鍵字來匹配知識庫，以提供相關結果。當您有唯一標識符如產品名稱、地點、ID 等時，這種方法效果很好，但在用戶沒有說出精確的關鍵字時（例如使用同義詞或不同語言）可能會錯過。

### Vector Search (向量檢索)

利用文本嵌入的能力來增強相關資料的檢索。向量檢索可以跨語言工作，即使沒有匹配的關鍵字也能檢索到相似的文檔。然而，對於稀有標識符如產品名稱、地點或 ID 可能會有困難。

### Hybrid Search (混合檢索)

結合關鍵字檢索和向量檢索方法，優化資料檢索。

## [知識庫擷取計數](#seachat-rag-ui)

此欄位允許您指定要檢索的知識庫文件(片段)數量，以確保有效的資料檢索。理想的數量是很彈性的，取決於令牌限制和文檔類型。

### 知識庫擷取計數的考慮因素

- **參考知識庫文件(文件片段)太少**

您可能會錯過關鍵資料，導致 GPT 的回應不完整或不準確。

- **參考知識庫文件(文件片段)太多**

重要資料可能會被不相關的細節淹沒，使 GPT 更難提供準確的回應。

- **上下文限制**

每次請求的上下文是有限制的。如果檢索到的文檔超過此限制，SeaChat 將使用在限制內能夠適應的文檔。

通過調整知識庫檢索數量，您可以優化資料深度和資源使用之間的平衡，確保準確且高效的回應。

## 知識庫搜索優化

SeaChat 現在提供一個名為知識庫搜索優化的進階功能，讓您能夠進一步提升檢索資訊的質量。此功能使 AI 能夠在生成回應前對初步搜索結果進行二次分析。

### 配置知識庫搜索優化

您可以在AI Agent 資訊的進階設定頁面中啟用此功能：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement" href="/images/seachat/zh/agent-advanced-settings/kb-refinement.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/kb-refinement.png" alt="SeaChat 中的知識庫搜索優化功能圖">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">SeaChat 中的知識庫搜索優化設置</p></p>
</div>

### 可選的知識庫優化指令

對於大多數用例來說，只需啟用此功能而無需任何附加說明就足夠了。系統將使用預設的優化策略自動優化搜尋結果。自訂指令是可選的，但可以顯著提高特定場景的效能。

為了更精確地控制 LLM 如何優化搜索結果，您可以在文本欄位中提供自定義指令。這些指令指導 AI：

- 如何評估文檔相關性
- 優先處理哪些類型的資訊
- 如何處理模糊查詢
- 針對您特定知識領域的特殊考慮

#### 指令示例

以下是一些有效的優化指令示例：

- "當用戶詢問產品規格時，優先考慮包含特定產品代碼的文檔。"
- "對於停車相關查詢，專注於包含與用戶提及區域匹配的位置資訊的文檔。"
- "處理技術支援問題時，優先考慮最新文檔而非舊版本。"
- "對於多部分問題，確保包含能夠解答查詢所有部分的文檔。"
- "總結對話歷史記錄時，如果可以從討論中推斷出分支名稱，請包括分支名稱，確保它反映用戶在上次查詢中想要的分支，即使沒有明確提及。"
- "在識別相關文章時，排除那些與摘要中提到的分支不同的分支相關的文章，前提是摘要指定了分支名稱。"

### 知識庫搜索優化的好處

啟用此功能可以顯著提升您的 AI 助理性能：

- 提供更準確和相關的回應
- 減少複雜知識庫中的資訊過載
- 更有效地處理模糊查詢
- 提升對用戶問題的上下文理解
- 提供更簡潔和專注的答案

通過微調您的知識庫搜索優化設置，您可以創建一個更智能、更靈敏的 AI 助理，更好地理解和解決用戶的特定需求。

### 📌 範例：透過知識庫搜尋優化功能處理多分店資訊
想像你經營一間擁有五家分店的餐廳。在你的知識庫中，你使用試算表記錄了每家分店的菜單、服務細節、營業時間與優惠資訊。當使用者詢問特定分店的問題時，你會希望 AI 智能助理能回應出正確、對應該分店的資訊。

要提升 AI 助理對使用者問題的理解與回應品質，有兩個有效的方法可以強化知識庫的處理方式：

**1. 在知識庫內容中標示分店名稱**

在你的 Excel 試算表中，為每一列或每一格的內容加上該資訊所屬的分店名稱。

<div style="display: flex; flex-direction: column; align-items: center;"> <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center"> <a id="seachat-kb-refinement" href="/images/seachat/zh/agent-advanced-settings/kb-refinement-example.png" target="_blank"> <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/kb-refinement-example.png" alt="An example spreadsheet contains five restaurant branches"> </a> </div> <p style="margin-top: 20px; font-size: 15px">範例試算表：包含分店標籤的多分店知識庫</p> </div>
這樣可以幫助 AI 助理在閱讀知識庫內容時正確理解該資訊屬於哪一家分店，進一步提升回應的準確性與相關性。

**2. 上傳試算表**

透過 **上傳試算表** 卡片將此試算表上傳到您的知識庫。選擇此選項將表格中的每一行上傳為單獨的知識庫文件。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement" href="/images/seachat/zh/agent-advanced-settings/kb-refinement-upload2.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/kb-refinement-upload2.png" alt="Upload each row as an individual kb article">
    </a>
</div>
</div>
<br/>

**3. 使用知識庫搜尋優化功能過濾不相關資料**

啟用知識庫搜尋優化功能，並加入自訂的優化指令，例如：`從使用者的問題中擷取分店名稱。排除與該分店無關的文章或資料列。`

有了這些指令，即使初步的知識庫搜尋結果涵蓋了多家分店，AI 助理也能自動篩選出與使用者查詢分店相關的內容，提供更精準、聚焦且有幫助的回應。

這樣的作法特別適用於：
- 內容交錯重疊的大型知識庫
- 擁有多個據點的企業或品牌
- 回答分店資訊需具高度準確性的場景

透過良好的知識庫結構（標示分店名稱）與搜尋優化邏輯結合，你可以打造一個更聰明、更貼近需求的 AI 助理。

