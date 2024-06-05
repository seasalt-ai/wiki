---
title: "AI助理記憶"
description: "SeaChat 記憶可以用來資格審查和追蹤客戶資料。「記憶」允許你定義對話中最重要的部分，並儲存標註在客戶檔案，提供之後查詢和再利用。"
lead: ""
date: 2024-04-26T08:48:45+00:00
lastmod: 2024-05-21T08:48:45+00:00
weight: 80
draft: false
images: []
toc: true
aliases:
   - /zh/seachat/seachat-manual/02-create-agent/03-agent-memory
---

<iframe width="100%" height="400" src="https://www.youtube.com/embed/?v=Msgg3U3lW4M&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=11" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

大型語言模型是基於LSTM（長短期記憶體架構）。但LSTM只在語言模型內部使用，不能實時紀錄現在對話的資訊。所以，我們需要一種方法來記住對話或用戶的某些特徵，我們稱之為「持久的記憶」，這樣每次對話重新開始時，大型語言模型仍能記住之前的狀態。例如，當客戶說明他吃素食，我們可以透過「記憶」在每次對談中讓大型語言模型記得客戶這項特質，藉以提供更好的回答。

「記憶」允許你定義對話中最重要的部分，並儲存標註在客戶檔案，提供之後查詢和再利用。

記憶的使用案例包括：
* 建立用戶形象，以便下次相同用戶回來時，AI 助理仍記得上次對話的要點。例如：`{married: yes, family: 2 kids, hobby: golf}`。
* 存儲問卷結果，然後通過 API 檢索這些結果以進行分析。例如：`{score: 2, feedback: wifi charging issue}`。
* 確認潛在買家，然後根據此觸發某些操作。例如：`{intent: buying an iPhone, lease or cash: cash, when: ASAP}`。

在本教學中，我們將涵蓋：

- 設計記憶欄位和描述，以便助理在每次對話中提取。
- 為每次對話提取記憶。

---

# 在進階設置中設置記憶

在本教學中，我們將介紹如何為您的助理有效地設置記憶欄位。我們將使用案例分為兩類：

1. 非問卷使用案例：助理設定需要手動定義其感興趣的記憶。
2. 問卷使用案例：記憶是從一系列問卷問題中自動提取的，不能修改。

## 非問卷使用案例的記憶設置

對於大多數助理，要設置記憶，我們將使用**進階設置**部分中提供的 UI。

1. 在**助理資訊**中，前往右上角的**進階設置**部分。

<center>
<a href="/images/seachat/zh/memory/general-setup.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/memory/general-setup.png" alt="">
</a>
r
<br/>

*助理資訊 → 進階設置*
</center>

<br/>

2. 在提供的部分中創建所需的欄位：
   - **欄位**：我們想要提取的記憶「變量」的名稱
      - 建議使用直觀名稱直觀。在理想情況下，您應該根據名稱知道這個欄位在監控什麼。
   - **內容**：此記憶欄位的預設值
      - 這是記憶欄位的初始值。通常情況下，這將是空的。
   - **描述**：欄位的定義
      - 用自然語言描述這個欄位是什麼以及要提取什麼類型的值。
      - 這裡需要描述性但簡潔。這將深深地影響提取的值。

<br/>

3. 使用頁面右側的加號（新增）和減號（移除）圖標根據需要新增或移除欄位。

<center>
<a href="/images/seachat/en/memory/add-and-remove.png" target="_blank">
<img width="20%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/add-and-remove.png" alt="">
</a>

<br/>

*加號（新增）和減號（移除）*
</center>

4. 最後，點擊頁面底部的儲存按鈕保存您的記憶設置。

<center>
<a href="/images/seachat/zh/memory/save-setting.png" target="_blank">
<img width="40%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/memory/save-setting.png" alt="">
</a>

<br/>

*儲存您的記憶設置*
</center>

## 問卷使用案例的記憶設置

對於問卷使用案例（CSAT，品牌認知，市場研究等），進階設置中的記憶窗格將根據描述部分動態設置。

1. 通過選擇其中一個使用案例，描述部分將包含一個空白問題部分（基本問卷使用案例）或一個預填寫的問題部分（模板問卷如 CSAT）。
   - 此部分由頂部的 **//QUESTIONS START** 和底部的 **//QUESTIONS END** 標記表示。
   - 格式為每行一個問題，所有問題位於 **//QUESTIONS START** 和 **//QUESTIONS END** 之間。
   - 隨意新增，移除或修改問題。

> :rotating_light: 注意 :rotating_light:
>
> 不要修改 **//QUESTIONS START** 和 **//QUESTIONS END** 標記。這對於正確填充此使用案例的記憶欄位至關重要。

2. 設置描述和問題部分後，按底部的儲存按鈕。

<center>
<a href="/images/seachat/en/memory/question-start.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/question-start.png" alt="">
</a>

<br/>

*問題部分*
</center>

3. 前往進階設置標籤以確保欄位設置正確。

> :rotating_light: 注意 :rotating_light:
>
> 使用問卷使用案例時，請勿更改記憶窗格中的任何部分。如果需要更改問題，請使用描述頁。

<center>
<a href="/images/seachat/en/memory/advanced-settings.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/advanced-settings.png" alt="">
</a>

<br/>

*進階設置*
</center>

## 對話中的記憶

每次對話的記憶將實時更新，我們可以從對話頁面檢查其值。

1. 從左側前往對話頁面。

<center>
<a href="/images/seachat/zh/memory/conversation-page.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/memory/conversation-page.png" alt="">
</a>

<br/>

*對話*
</center>

2. 從列表中找到所需的對話，並按該對話右下角的三點圖標 <mark>&#8942;</mark>。

<center>
<a href="/images/seachat/zh/memory/memory-btn.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/memory/memory-btn.png" alt="">
</a>

<br/>

*點擊**記憶***
</center>

3. 按下**記憶**將顯示該對話的最新提取值。

<center>
<a href="/images/seachat/zh/memory/extracted-value.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/memory/extracted-value.png" alt="">
</a>

<br/>

*最新提取值*
</center>

## 🤖 範例使用案例

假設我們有一個旨在增強客戶體驗管理的 AI 助理。該助理的有效性取決於其準確追蹤用戶偏好的能力，這我們可以利用特定的記憶欄位來建立此數據。

### 初始設置

在深入探討記憶欄位配置之前，確保您的 AI 助理已運行。如果您尚未設置助理，請參閱我們的[創建新助理](/zh/seachat/seachaat-manual/02-create-agent/01-create-new-agent/)指南以獲取詳細說明。

### 定義記憶

繼續前往**進階設置**標籤，在此您可以定義記憶欄位：

<center>
<a href="/images/seachat/zh/memory/example-advanced-setting.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/memory/example-advanced-setting.png" alt="">
</a>
<p style="margin-top: 20px; font-size: 15px">定義記憶</p>
</center>

1. **欄位**：例如，設置「產品」作為欄位，表示助理將專注於提取互動中提到的產品名稱信息。

2. **描述**：在此指定欄位應捕捉的信息。對於「產品」，描述將指導 AI 從對話中識別並記住產品名稱。我甚至提供了提取信息類型的範例。

3. **保存**：確保保存這些配置以應用它們。

### 監控對話記憶

AI 助理將實時監控對話，在檢測到相關信息時更新記憶欄位。這種動態更新使助理能夠根據提取的數據調整其回應。

<center>
<a href="/images/seachat/zh/memory/example-conversation.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/memory/example-conversation.png" alt="">
</a>
<p style="margin-top: 20px; font-size: 15px">監控對話記憶</p>
</center>

從對話中提取的值可以在系統內訪問。只需移至**對話**頁面，選擇所需的對話，然後點擊**記憶**按鈕以查看提取的值。再次閱讀[此處](#monitor-conversation-memory)以瞭解如何查看您的結果，如下圖所示。

<center>
<a href="/images/seachat/zh/memory/extracted-value.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/memory/extracted-value.png" alt="">
</a>
<p style="margin-top: 20px; font-size: 15px">提取的值</p>
</center>

# 檢索對話記憶

每次對話的記憶值可以通過 [API](https://wiki.seasalt.ai/seasaltapi/seasalt-api/01-seachat-api-intro/) 檢索以進行進一步處理。
