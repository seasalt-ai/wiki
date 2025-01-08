---
title: "標籤自動化"
description: "學習如何在 SeaChat 中設置和使用 標籤自動化，以根據應用的標籤觸發操作。"
lead: ""
date: 2025-01-06T08:48:45+00:00
lastmod: 2024-01-06T08:48:45+00:00
weight: 90
draft: false
images: []
toc: true
url: /zh/seachat/manual/labeling/label-automation/
---

---

## 視頻教程

<iframe width="100%" height="400" src="https://www.youtube.com/embed/2SYYU1lQqrc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

**概覽**

標籤自動化 是 SeaChat 中的一項功能，允許用戶定義當標籤被應用或移除時觸發的操作。

此功能基於 [自動標記(https://wiki.seasalt.ai/seachat/manual/labeling/lauto-labeling/) 功能進一步拓展，通過引入工作流程來自動通知或升級重要事件。

本教程將帶您完成標籤自動化的設置，並提供增強工作流程的實用範例。

---

## 主要功能

<center>
<a href="/images/seachat/en/labeling/label-automation/feature-overview.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/feature-overview.png"  alt="功能概覽">
</a>

</center>

<br/>

1. **自動觸發操作**
   - 設置操作，例如發送電子郵件、簡訊或 API 請求。
   - 操作會在特定標籤被應用或移除時觸發。

2. **可自定義工作流程**
   - 定義針對個別標籤（如 **Code Red** 或 **Code Yellow**）的工作流程。
   - 根據使用場景（例如醫療分診或客戶服務警報）量身定制操作。

3. **內建自動化功能**
   - 使用 SeaChat 的內建功能，無需依賴像 Zapier 這樣的外部工具。

4. **手動與自動整合**
   - 標籤可通過 自動標記自動應用，或在對話中手動添加。

---

## 如何設置 標籤自動化

1. **進入整合**
   - 打開 **整合** 區域，選擇 **標籤自動化**。

<center>
<a href="/images/seachat/en/labeling/label-automation/navigation-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/navigation-ui.png"  alt="導航至 標籤自動化">
</a>

</center>

<br/>

2. **選擇標籤**
   - 選擇一個標籤，例如 **Code Red** 或 **Code Yellow**。
   - 範例：將 **Code Red** 用於嚴重情況。

<center>
<a href="/images/seachat/en/labeling/label-automation/choose-a-label.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/choose-a-label.png"  alt="選擇自動化標籤">
</a>

</center>

<br/>

3. **定義操作**
   - 為選定標籤添加操作：
      - **電子郵件**：指定收件人和消息內容。
      - **簡訊**：提供電話號碼和消息文本。
      - **API 請求**：配置自定義端點（適用於高級用戶）。


<center>
<a href="/images/seachat/en/labeling/label-automation/define-action.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/define-action.png"  alt="定義自動化操作">
</a>

</center>

<br/>

4. **保存並測試**
   - 保存配置並通過手動或自動應用標籤進行測試。

<center>
<a href="/images/seachat/en/labeling/label-automation/save-and-test.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/save-and-test.png"  alt="保存並測試操作">
</a>

</center>

<br/>

---

## 範例使用場景：醫療分診

如需查看完整範例，請觀看我們的標籤自動化視頻教程。

1. **Code Red - 嚴重情況**
   - **觸發條件**：將 **Code Red** 應用於涉及呼吸困難或嚴重出血等嚴重情況的對話。
   - **操作**：向相關醫療團隊發送電子郵件和簡訊。

2. **Code Yellow - 中度情況**
   - **觸發條件**：對中度疼痛或發燒等情況應用 **Code Yellow**。
   - **操作**：通過電子郵件通知相關人員。

3. **移除標籤**
   - **觸發條件**：當 **Code Red** 被移除時，發送電子郵件通知 **Alert Disarmed**。

---

## 工作流程範例

1. **定義 **Code Red** 的工作流程**
   - 設置電子郵件通知工作人員有關嚴重情況的消息。
   - 為冗餘配置 Google Voice 號碼以接收簡訊警報。

<center>
<a href="/images/seachat/en/labeling/label-automation/define-email-action.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/define-email-action.png"  alt="定義電子郵件操作">
</a>

</center>

<br/>

2. **手動觸發測試**
   - 在對話中手動應用 **Code Red** 並驗證操作是否觸發。
   - 檢查電子郵件和簡訊通知，確認它們是否正確執行。

<center>
<a href="/images/seachat/en/labeling/label-automation/conversation-example.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/conversation-example.png"  alt="對話範例">
</a>

</center>

<br/>

3. **結合自動標記自動觸發**
   - 與 自動標記功能結合，根據預定對話規則自動觸發 **Code Red**。

<center>
<a href="/images/seachat/en/labeling/label-automation/action-on-labeling.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/action-on-labeling.png"  alt="自動標記整合">
</a>

</center>

<br/>

---

**標籤自動化的優勢**

- **效率**：通過標籤觸發的自動化操作簡化工作流程。
- **靈活性**：支持手動和自動標籤應用。
- **整合性**：內建於 SeaChat 中，無需第三方工具。
- **客製化**：配置適合各種行業和使用場景的工作流程。

---

**進階功能**

- **API 整合**：適用於高級用戶，通過 API 請求觸發自定義工作流程。
- **結合自動化**：與 自動標記整合，創建無縫工作流程。

---

**結論**  
標籤自動化增強了 SeaChat 的功能，將應用的標籤轉化為可執行的事件。無論是管理醫療熱線還是簡化客戶服務，此功能都為自動化和優化流程提供了工具。嘗試將標籤自動化與 自動標記結合使用，以創建適合您需求的強大高效工作流程。
