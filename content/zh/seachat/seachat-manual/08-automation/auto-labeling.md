---
title: "自動標記"
description: "了解如何設定和使用 自動標記功能，以自動化和簡化對話標籤化的過程。"
lead: ""
date: 2024-12-29T00:00:00-07:00
lastmod: 2024-12-29T00:00:00-07:00
weight: 80
draft: false
images: []
toc: true
url: /zh/seachat/manual/labeling/auto-labeling/
---

---

## 影片教學

<iframe width="100%" height="400" src="https://www.youtube.com/embed/2lZcfofYQj4?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  allowfullscreen style="border-radius: 30px";></iframe>

---

**簡介**  
自動標記是 Seasalt.ai 工具套件整合中的重要組成部分。此功能能夠智能且自動地將標籤應用於對話，簡化了如客戶服務和醫療保健等使用場景的流程。

我們歡迎您查看我們的 [標籤自動化](https://wiki.seasalt.ai/zh/seachat/manual/labeling/label-automation/) 功能，以實現基於自動標記的更高級工作流程。

**什麼是自動標記**  
自動標記是一個系統，能根據預定義規則和 AI 驅動的分析自動將標籤應用於對話或其他數據點。用戶無需手動標記，可設置條件在符合規則時動態添加或移除標籤。

---

## 主要功能


<center>
<a href="/images/seachat/en/labeling/auto-labeling/auto-labeling-feat-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/auto-labeling-feat-ui.png"  alt="自動標記介面概覽">
</a>

</center>

<br/>

1. **自動標籤應用**  
   - 根據對話內容添加標籤，例如```Escalated```或```Low Priority```。  
   - 同時處理多個標籤。

2. **動態規則系統**  
   - 用戶可以定義標籤觸發條件，例如特定的關鍵字或短語。  
   - 支援自動添加和移除標籤的功能。

3. **自定義使用場景**  
   - 例如，醫療熱線中 ```Escalated``` 可用於表示嚴重疼痛，而 ```Low Priority```可用於輕微疼痛。

4. **可視化反饋**  
   - 標籤會顯示在對話歷史中，提供其分類的即時見解。

---

## 如何設置 自動標記
1. **前往整合**
   - 打開 ```整合```區域，選擇 **自動標記**


<center>
<a href="/images/seachat/en/labeling/auto-labeling/navigation-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/navigation-ui.png"  alt="Navigation to Auto Labeling">
</a>

</center>

<br/>

2. **創建規則**  
   - 定義添加或移除標籤的觸發條件。  
   - 例如，對於醫療熱線：
     - ```Extreme pain``` 觸發 ```Escalated``` 標籤。  
     - ```Minor aches``` 觸發 ```Low Priority``` 標籤。

<center>

<a href="/images/seachat/en/labeling/auto-labeling/define-rules.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/define-rules.png"  alt="定義標籤規則">
</a>
</center>

<br/>


3. **測試規則**  
   - 模擬對話以檢查標籤是否正確應用。  
   - 例如，輸入 "I feel so much pain, I need a doctor’s attention" 以觸發 ```Escalated```。
  

<center>
<a href="/images/seachat/en/labeling/auto-labeling/test-rules.png">
<img height="100%" width="80%" src="/images/seachat/en/labeling/auto-labeling/test-rules.png"  alt="測試對話中的標籤規則">
</a>


</center>

<br/>

4. **調整和保存**  
   - 修改規則以提升準確性，並保存配置。  


<center>
<a href="/images/seachat/en/labeling/auto-labeling/save-rules.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/save-rules.png"  alt="定義標籤規則">
</a>

</center>

<br/>

---

**高級使用場景**  

1. **醫療分診系統**  
   - 使用標籤如 ```Green```、 ```Yellow``` 和 ```Red```
 根據病情嚴重程度進行分類。  
     - ```Red```：嚴重問題，例如呼吸困難或大量出血。  
     - ```Yellow```：中度疼痛或發燒。  
     - ```Green```：輕微疼痛或感冒。  


<center>
<a href="/images/seachat/en/labeling/auto-labeling/advanced-rules.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/advanced-rules.png"  alt="定義標籤規則">
</a>

</center>

<br/>

2. **標籤自動化**  
   - 將操作與特定標籤聯繫起來：
        - 當 ```Escalated```被應用時觸發電子郵件或 SMS。  
        - 自動跟進 ```Low Priority```案例。
   - 查看我們的 [標籤自動化](https://wiki.seasalt.ai/seachat/manual/labeling/label-automation/) 教學了解更多細節。


---

**自動標記的優勢**  

- **效率**：減少手動標籤的工作量。  
- **可擴展性**：處理大量數據。  
- **準確性**：確保規則應用一致。  
- **客製化**：適用於多種行業和使用場景。  

---

**結論**  
自動標記徹底改變了企業管理對話和數據的方式。從醫療保健中的動態分診到簡化客戶支持，這個工具簡化並加速了流程，同時確保準確性。未來的教程將深入探討移除標籤和利用標籤自動化以實現更高級的工作流程，敬請期待！
