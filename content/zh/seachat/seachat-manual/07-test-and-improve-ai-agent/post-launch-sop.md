---
title: "連上 SeaChat 後 - 成功營運的 SOP"
description: "連上 SeaChat 後，請遵循此標準作業程序 (SOP) 指南，以優化日常運營並改善團隊工作流程，提高工作效率。"
date: 2024-09-02T00:22:19-07:00
lastmod: 2024-09-02T00:22:19-07:00
draft: false
weight: 1
aliases:
  - /zh/seachat/seacaht-manual/07-test-and-improve-ai-agent/post-launch-sop
---

恭喜您成功將 SeaChat 部署到選定的頻道 – 網站、WhatsApp 或其他平台。我們只完成了一半的工作。本指南將引導您完成剩餘步驟，以確保日常運營的成功。

## 設置

### 1. 向工作區添加更多成員

<br/>

<center>``
<a href="/images/seachat/zh/post-launch-sop/add-members.png">
<img height="100%" width="40%" src="/images/seachat/zh/post-launch-sop/add-members.png"  alt="通過 SeaChat 的工作區和成員管理區域添加更多成員。">
</a>

*工作區 → 成員*

</center>

如果您尚未添加，您可以前往 *工作區* → *成員* 將您的團隊添加進去。

請注意，成員有 [三種角色](https://wiki.seasalt.ai/zh/seachat/workspace/workspace-management/#members): 管理員、AI 助理編輯者和人工客服。

人工客服無法看到您如何配置 AI 助理，他們只負責回覆收到的訊息。

您的 AI 助理編輯者可以修改 AI 助理，因此請謹慎分配這些角色。

如果您有 **多個 AI 助理**，您可以為不同的 AI 助理分配不同的人工客服。

### 2. 啟用郵件通知

您應該要求每個客服在 *工作區* → *偏好設置* 啟用郵件通知。

<center>
<a href="/images/seachat/zh/post-launch-sop/enable-email-notification.png">
<img height="100%" width="80%" src="/images/seachat/zh/post-launch-sop/enable-email-notification.png"  alt="在 SeaChat 平台上啟用郵件通知以跟蹤聊天對話。">
</a>

*在 SeaChat 上啟用郵件通知*

</center>

這樣，當有人開始與您的 AI 助理聊天時，您會立即收到通知，然後您可以選擇是否要參與其中。

### 3. 考慮在網頁小工具上啟用表單

如果您使用網頁聊天小工具，訪客可能不會留下他們的電話號碼、姓名或電子郵件。這樣您將無法知道您正在與誰聊天。此時，您可以前往 *頻道* → *網頁聊天小工具* → *自定義表單*，強制訪客在聊天前填寫聯絡資訊：

<div style="display: flex; flex-direction: row; align-items: center; justify-content: space-between; gap: 20px;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/post-launch-sop/web-widget.png" target="_blank" style="width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: auto; height: 200px; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/post-launch-sop/web-widget.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">網頁聊天小工具中的自定義表單</p>
    </div>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/post-launch-sop/web-widget-form.png" target="_blank" style="width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: auto; height: 200px; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/post-launch-sop/web-widget-form.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">創建網頁聊天小工具</p>
    </div>
</div>

## 日常流程

### 人工客服應該做什麼

每天，您的客服應該做兩件事：

- 進入對話頁面並回覆收到的詢問
- 對 AI 助理未能很好回答的問題標記 👎
- 對人工客服回答得很好的問題標記 👍

### AI 助理編輯者和管理員應該做什麼

每天，您的 AI 助理編輯者或管理員應該做三件事：

- 進入對話頁面，查看 AI 助理和人工客服是如何回覆客戶的
- 對人工客服未能很好回答的問題標記 👎
- 對人工客服回答得很好的問題標記 👍

當 AI 助理編輯者或管理員發現需要改進的地方後，他們可以進入 *需要審核* 區域，開始添加或修改知識庫：

<center>
<a href="/images/seachat/zh/post-launch-sop/need-review.png">
<img height="100%" width="80%" src="/images/seachat/zh/post-launch-sop/need-review.png"  alt="AI 助理編輯者和管理員應該每天審查 '需要審核' 區域中的對話，以改善聊天質量">
</a>

*需要審核的對話*

</center>

## 每週流程

每週花費 30 分鐘至 1 小時，管理員應該與 AI 助理編輯者合作進行以下工作：

*改善知識庫*
- 審查 *需要審核* 區域，並修改知識庫
- 知識庫的修改不僅包括添加新內容，還包括刪除過時的文章。

*利用知識庫改善您的網站*
- 討論最近添加到知識庫的內容
- 如果有常見問題，可以考慮將其添加到您的網站上。

*利用您的網站改善知識庫*
- 如果您最近撰寫了更多文件，並希望 AI 助理知道，可以將其導入到知識庫中。
- 如果您的網站有變更，您可以通過點擊 *立即同步* 按鈕重新導入。

<center>
<a href="/images/seachat/zh/post-launch-sop/knowledge-base.png">
<img height="100%" width="80%" src="/images/seachat/zh/post-launch-sop/knowledge-base.png"  alt="每週更新您的 AI 助理知識庫，以提高其回覆的效率。">
</a>

*更新知識庫以提高性能*

</center>

## 反覆程序

AI 助理了解兩件事：
- 他們被訓練來了解您的業務
- 一些常識和事實的世界知識

您有責任每天和每週對其進行改進，這樣您的人工客服就會越來越少工作！
