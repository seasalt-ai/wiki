---
title: "助理版本控制"
description: "了解如何在 SeaChat 中高效地複製和取代 AI 助理人。本指南涵蓋了如何基於現有助理人創建新助理人，以便於無縫測試和開發，並管理不同版本的助理人以簡化您的生產工作流程。"
lead: "探索 SeaChat 強大的助理人複製與取代功能，設計用於創建和管理不同版本的 AI 助理人。非常適合原型設計、測試以及從開發到生產的平滑過渡。"
date: 2024-07-10T08:48:45+00:00
lastmod: 2024-07-10T08:48:45+00:00
weight: 20
draft: false
images: []
toc: true
aliases:
  - /zh/seachat/seachat-manual/02-create-agent/03-agent-duplication-replacement
---

## 複製AI助理

> 📍複製AI助理時，什麼資料被複製了？
> 
> 當AI助理被複製或取代時，會涉及AI助理的基本資訊、進階設置、知識庫和網頁小工具。頻道無法被複製或替換。

當您想要創建一個與現有助理設置相似的新助理時，複製AI助理是一個非常有用的功能，允許您基於現有助理創建新的助理。

要複製助理，請在**工作區**下的**助理**中點擊您想要複製的助理旁邊的**複製此AI助理**按鈕。這將創建一個名為**{助理名稱} (COPY)**的新助理，該助理與原助理具有相同的設置。您可以點擊**編輯**來修改設置或直接進入**助理信息**。

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/create-a-new-agent/agent-duplication-btn.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
      <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/create-a-new-agent/agent-duplication-btn.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">複製AI助理按鈕</p>
  </div>
</div>

<br/>

這個功能對於助理編輯者在新助理的原型設計設置和分離開發與生產線助理以進行測試和優化時非常強大。

根據助理的複雜性，這個過程可能需要一些時間。一旦您看到成功消息，您就可以開始訓練您的助理。所有設置，包括知識庫和助理資訊，都已設置完畢。

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/create-a-new-agent/duplication-confirmation.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
      <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/create-a-new-agent/duplication-confirmation.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">複製確認</p>
  </div>
</div>

<br/>

對於與原助理連接的整合或渠道，用戶需要更新整合以包含新的助理複本，因為助理複本仍然是一個新的助理。

## AI助理取代

> 📍取代AI助理時，什麼資料被取代了？
> 
> 當AI助理被複製或取代時，會涉及AI助理的基本資訊、進階設置、知識庫和網頁小工具。頻道無法被複製或替換。


助理取代功能提供了一種有效管理不同版本助理的方式。

這在您想要開發現有助理而不影響原始版本時特別有用。通過使用此功能，助理編輯者可以對原始助理的副本進行更改，而不是直接修改原始助理。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/create-a-new-agent/replace-button.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/create-a-new-agent/replace-button.png" alt="">
</a>

**取代助理**
</center>

一個常見的使用情境可能如下所示：

1. 複製原始的助理 A 並將副本命名為助理 B（助理 A 的副本）。
2. 向助理 B 添加新功能並進行測試。
3. 開發完成後，用助理 B 取代助理 A。
4. 現在，新助理正在生產環境中運行，具有助理 A 的原始設定和助理 B 實施的新功能。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/create-a-new-agent/replacement-workflow.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/create-a-new-agent/replacement-workflow.jpg" alt="">
</a>

**助理取代工作流程**
</center>

通過遵循此過程，您可以在開發和測試新版本的同時，保持原始助理在生產環境中的運行。
