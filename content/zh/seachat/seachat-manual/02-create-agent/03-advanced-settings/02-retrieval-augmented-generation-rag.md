---
title: "檢索增強生成 (RAG)"
description: "探索 SeaChat 的進階設置，包括助理記憶和檢索增強生成 (RAG)。了解如何優化您的 AI 助理的性能和即時用戶互動。"
lead: ""
date: 2024-05-29T08:48:45+00:00
lastmod: 2024-05-29T08:48:45+00:00
weight: 50
draft: false
images: []
toc: true
aliases:
  - /zh/seachat/seachat-manual/02-create-agent/03-advanced-settings/02-retrieval-augmented-generation-rag
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
