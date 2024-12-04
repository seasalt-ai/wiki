---
title: "上下文抽取"
description: "SeaChat 上下文抽取可以用來資格審查和追蹤客戶資料。「上下文抽取」允許你定義對話中最重要的部分，並儲存標註在客戶檔案，提供之後查詢和再利用。"
lead: ""
date: 2024-04-26T08:48:45+00:00
lastmod: 2024-05-21T08:48:45+00:00
weight: 80
draft: false
images: []
toc: true
aliases:
   - /zh/seachat/seachat-manual/02-create-agent/03-agent-context-extraction
   - /zh/seachat/manual/create-agent/advanced-settings/agent-memory/
url: /zh/seachat/manual/create-agent/advanced-settings/context-extraction/
---
<div style="display: flex; align-self: flex-end; align-items: baseline">

`此功能僅適用於  `
   <div style="border-radius: 30%; 
    background: linear-gradient(90deg, #135f5c, #3a947b); 
    width: 5rem; 
    color: #ffffff; 
    padding: calc(min(100vw, 1366px)* 0.00439) calc(min(100vw, 1366px)* 0.00878);
    border-radius: calc(min(100vw, 1366px)* 0.01464);
    display: block;
    unicode-bidi: isolate;
    box-sizing: border-box;
   font-size: .8rem;
    align-content: center;
   ">
   <div>企業方案</div>
</div>
<div style="border-radius: 30%; 
    background: linear-gradient(90deg,#824a14,#886f40);
    width: 5rem; 
    color: #ffffff; 
    padding: calc(min(100vw, 1366px)* 0.00439) calc(min(100vw, 1366px)* 0.00878);
    border-radius: calc(min(100vw, 1366px)* 0.01464);
    display: block;
    unicode-bidi: isolate;
    box-sizing: border-box;
   font-size: .8rem;
   margin-left: .5rem;
        align-content: center;
   ">
   <div>高級方案</div>
</div>
</div>

<iframe width="100%" height="400" src="https://www.youtube.com/embed/?v=Msgg3U3lW4M&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=11" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>
<br/>


「上下文抽取」允許你定義對話中最重要的部分，並儲存標註在客戶檔案，提供之後查詢和再利用。

上下文抽取的使用案例包括：
* 建立用戶形象，以便下次相同用戶回來時，AI 助理仍記得上次對話的要點。例如：`{married: yes, family: 2 kids, hobby: golf}`。
* 存儲問卷結果，然後通過 API 檢索這些結果以進行分析。例如：`{score: 2, feedback: wifi charging issue}`。
* 確認潛在買家，然後根據此觸發某些操作。例如：`{intent: buying an iPhone, lease or cash: cash, when: ASAP}`。

在本教學中，我們將涵蓋：

- 設計上下文抽取欄位和描述，以便助理在每次對話中提取。
- 為每次對話提取上下文抽取。

---

# 在進階設置中設置上下文抽取

在本教學中，我們將介紹如何為您的助理有效地設置上下文抽取欄位。我們將使用案例分為兩類：

1. 非問卷使用案例：助理設定需要手動定義其感興趣的上下文抽取。
2. 問卷使用案例：上下文抽取是從一系列問卷問題中自動提取的，不能修改。

## 非問卷使用案例的上下文抽取設置

對於大多數助理，要設置上下文抽取，我們將使用**進階設置**部分中提供的 UI。

1. 在**助理資訊**中，前往右上角的**進階設置**部分。

<center>
<a href="/images/seachat/zh/context-extraction/general-setup.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/context-extraction/general-setup.png" alt="SeaChat | 上下文抽取 | 進階設置">
</a>

<br/>

*助理資訊 → 進階設置*
</center>

<br/>

2. 在提供的部分中創建所需的欄位：
   - **欄位**：我們想要提取的上下文抽取「變量」的名稱
      - 建議使用直觀名稱直觀。在理想情況下，您應該根據名稱知道這個欄位在監控什麼。
   - **內容**：此上下文抽取欄位的預設值
      - 這是上下文抽取欄位的初始值。通常情況下，這將是空的。
   - **描述**：欄位的定義
      - 用自然語言描述這個欄位是什麼以及要提取什麼類型的值。
      - 這裡需要描述性但簡潔。這將深深地影響提取的值。

<br/>

3. 使用頁面右側的加號（新增）和減號（移除）圖標根據需要新增或移除欄位。

[//]: # (<center>)

[//]: # (<a href="/images/seachat/en/context-extraction/add-and-remove.png" target="_blank">)

[//]: # (<img width="20%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/add-and-remove.png" alt="">)

[//]: # (</a>)

[//]: # ()
[//]: # (<br/>)

[//]: # ()
[//]: # (*加號（新增）和減號（移除）*)

[//]: # (</center>)

4. 最後，點擊頁面底部的儲存按鈕保存您的上下文抽取設置。

[//]: # (<center>)

[//]: # (<a href="/images/seachat/zh/context-extraction/save-setting.png" target="_blank">)

[//]: # (<img width="40%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/context-extraction/save-setting.png" alt="">)

[//]: # (</a>)

[//]: # ()
[//]: # (<br/>)

[//]: # ()
[//]: # (*儲存您的上下文抽取設置*)

[//]: # (</center>)

## 問卷使用案例的上下文抽取設置

對於問卷使用案例（CSAT，品牌認知，市場研究等），進階設置中的上下文抽取窗格將根據描述部分動態設置。

1. 通過選擇其中一個使用案例，描述部分將包含一個空白問題部分（基本問卷使用案例）或一個預填寫的問題部分（模板問卷如 CSAT）。
   - 此部分由頂部的 **//QUESTIONS START** 和底部的 **//QUESTIONS END** 標記表示。
   - 格式為每行一個問題，所有問題位於 **//QUESTIONS START** 和 **//QUESTIONS END** 之間。
   - 隨意新增，移除或修改問題。

> :rotating_light: 注意 :rotating_light:
>
> 不要修改 **//QUESTIONS START** 和 **//QUESTIONS END** 標記。這對於正確填充此使用案例的上下文抽取欄位至關重要。

2. 設置描述和問題部分後，按底部的儲存按鈕。

<center>
<a href="/images/seachat/en/context-extraction/question-start.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/question-start.png" alt="SeaChat | 上下文抽取 | 設置描述">
</a>

<br/>

*問題部分*
</center>

3. 前往進階設置標籤以確保欄位設置正確。

> :rotating_light: 注意 :rotating_light:
>
> 使用問卷使用案例時，請勿更改上下文抽取窗格中的任何部分。如果需要更改問題，請使用描述頁。

<center>
<a href="/images/seachat/en/context-extraction/advanced-settings.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/advanced-settings.png" alt="SeaChat | 上下文抽取 | 進階設置標籤">
</a>

<br/>

*進階設置*
</center>

## 對話中的上下文抽取

每次對話的上下文抽取將實時更新，我們可以從對話頁面檢查其值。

1. 從左側前往對話頁面。

<center>
<a href="/images/seachat/zh/context-extraction/conversation-page.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/context-extraction/conversation-page.png" alt="SeaChat | 上下文抽取 | 對話">
</a>

<br/>

*對話*
</center>

2. 從列表中找到所需的對話，並按該對話右下角的三點圖標 <mark>&#8942;</mark>。

<center>
<a href="/images/seachat/zh/context-extraction/extraction-btn.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/context-extraction/extraction-btn.png" alt="SeaChat | 上下文抽取 | 按鈕">
</a>

<br/>

*點擊**上下文抽取***
</center>

3. 按下**上下文抽取**將顯示該對話的最新提取值。

<center>
<a href="/images/seachat/zh/context-extraction/extracted-value.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/context-extraction/extracted-value.png" alt="SeaChat | 上下文抽取 | 最新提取值">
</a>

<br/>

*最新提取值*
</center>

## 🤖 範例使用案例

假設我們有一個旨在增強客戶體驗管理的 AI 助理。該助理的有效性取決於其準確追蹤用戶偏好的能力，這我們可以利用特定的上下文抽取欄位來建立此數據。

### 初始設置

在深入探討上下文抽取欄位配置之前，確保您的 AI 助理已運行。如果您尚未設置助理，請參閱我們的[創建新助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/)指南以獲取詳細說明。

### 定義上下文抽取

繼續前往**進階設置**標籤，在此您可以定義上下文抽取欄位：

<center>
<a href="/images/seachat/zh/context-extraction/example-advanced-setting.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/context-extraction/example-advanced-setting.png" alt="SeaChat | 上下文抽取 | 進階設置範例">
</a>
<p style="margin-top: 20px; font-size: 15px">定義上下文抽取</p>
</center>

1. **欄位**：例如，設置「產品」作為欄位，表示助理將專注於提取互動中提到的產品名稱信息。

2. **描述**：在此指定欄位應捕捉的信息。對於「產品」，描述將指導 AI 從對話中識別並記住產品名稱。我甚至提供了提取信息類型的範例。

3. **保存**：確保保存這些配置以應用它們。

### 監控對話上下文抽取

AI 助理將實時監控對話，在檢測到相關信息時更新上下文抽取欄位。這種動態更新使助理能夠根據提取的數據調整其回應。

<center>
<a href="/images/seachat/zh/context-extraction/example-conversation.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/context-extraction/example-conversation.png" alt="SeaChat | 上下文抽取 | 對話範例">
</a>
<p style="margin-top: 20px; font-size: 15px">監控對話上下文抽取</p>
</center>

從對話中提取的值可以在系統內訪問。只需移至**對話**頁面，選擇所需的對話，然後點擊**上下文抽取**按鈕以查看提取的值。再次閱讀[此處](#monitor-conversation-extraction)以瞭解如何查看您的結果，如下圖所示。

<center>
<a href="/images/seachat/zh/context-extraction/extracted-value.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/context-extraction/extracted-value.png" alt="SeaChat | 上下文抽取 | 提取值範例">
</a>
<p style="margin-top: 20px; font-size: 15px">提取的值</p>
</center>

# 檢索對話上下文抽取

每次對話的上下文抽取值可以通過 [API](https://wiki.seasalt.ai/zh/seasaltapi/seasalt-api/01-seachat-api-intro/) 檢索以進行進一步處理。
