---
title: "複製AI助理"
description: "學習如何在 SeaChat 中有效地複製 AI 助理，讓您能夠建立具有相似設置的新助理，以進行流暢的測試和優化。"
lead: "發現 SeaChat 的助理複製功能的強大之處，利用現有設置創建新助理，非常適合原型設計和優化您的 AI 助理。"
date: 2024-07-10T08:48:45+00:00
lastmod: 2024-07-10T08:48:45+00:00
weight: 20
draft: false
images: []
toc: true
aliases:
  - /zh/seachat/seachat-manual/02-create-agent/03-agent-duplication
---

## 複製AI助理

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