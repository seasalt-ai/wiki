---
title: "客制GPT工具"
description: ""
date: 2025-01-06T08:48:45+00:00
lastmod: 2024-01-06T08:48:45+00:00
draft: false
weight: 600
url: /zh/seachat/seachat-manual/automation/custom-gpt-tool

---

## 簡介

SeaChat 的 客制GPT工具 允許用戶通過將自定義操作直接整合到對話中來增強代理的回應能力。此功能使用戶能夠定義具體條件，以便代理在滿足條件時執行這些操作，提供量身定制的回應和基於實時資訊的智能支援。例如，您可以讓代理執行搜索或從您公司的 API 獲取數據，讓 SeaChat 能夠利用外部資源提供更豐富的答案。

## 影片教學

以下是簡單教程，展示如何調用兩個 APIs 以顯示單張圖片。我們演示了如何配置 API 端點，並在聊天中顯示可愛的狗狗圖片：

<iframe width="100%" height="400" src="https://www.youtube.com/embed/olWQTiPLHOc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第二個教程中，我們通過配置 API 參數調用天氣 API，並動態將地點名稱轉換為 GPS 座標以獲取準確的天氣資訊：

<iframe width="100%" height="400" src="https://www.youtube.com/embed/7v7zBr5j-So?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第三個教程中，我們演示了如何在聊天中獲取包含多張狗狗圖片的卡片輪播。我們展示了如何利用 **PATH** 參數來顯示特定狗品種的多張圖片：

<iframe width="100%" height="400" src="https://www.youtube.com/embed/wBGJyfB9hcY?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第四個教程中，我們展示了如何使用 SeaChat 的 客制GPT工具 設置電子郵件警報，檢測聊天中的敏感內容並自動發送電子郵件通知。

<iframe width="100%" height="400" src="https://www.youtube.com/embed/KhjHDbRTIJc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第五個教程中，我們展示了如何在 SeaChat 中設置簡訊 通知來監控用戶對話。例如，我們演示了如何在檢測到用戶對話中有抑鬱跡象時設置簡訊 警報。

<iframe width="100%" height="400" src="https://www.youtube.com/embed/Z7Zj6BWEXTc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

第六個教程中，我們展示了如何自動通過簡訊 向呼叫者發送資訊。

<iframe width="100%" height="400" src="https://www.youtube.com/embed/LNezPT4qzCs?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>


## 快速入門

要啟用此功能，登錄 SeaChat 後，導航至 **AI助理配置** \-\> **整合** \-\> **客制GPT工具**。

>
> SeaChat 目前支持四種類型的工具：
>
> - **搜尋和顯示**：允許 SeaChat 使用您的 API 執行外部搜索，並基於對話上下文獲取附加資訊。搜索結果將以純文本或卡片輪播形式顯示在 webchat 中。
> - **圖片搜尋**：類似於搜尋和顯示，但具有增強的圖片處理功能。此工具允許 SeaChat 接受用戶的圖片輸入，通過您的 API 處理它們，並以帶有自定義描述的卡片形式顯示結果。
> - **電子郵件**：根據您的指示自動發送電子郵件。請確保指定目的、收件人和條件。要向用戶發送電子郵件，請通過 webchat 表單收集他們的電子郵件地址。
> - **發送簡訊**：根據您的指示自動發送簡訊。定義目的、收件人和條件。要向用戶發送簡訊，請確保通過渠道或 webchat 表單獲取他們的電話號碼。
>
> <br/>
> <center>
> <a href="/images/seachat/en/gpt-tools/seachat-tool-options.png">
> <img height="100%" width="100%" src="/images/seachat/en/gpt-tools/seachat-tool-options.png"  alt="SeaChat 支援的工具類型">
> </a>
> <br/>
> </center>

## 配置 搜尋和顯示的步驟：

### 步驟 1：選擇工具類型

SeaChat 目前支持一種類型的工具：

* **搜尋和顯示**：這些工具允許 SeaChat 使用您的 API 執行外部搜索，並基於對話上下文獲取附加資訊。搜索結果將以純文本或卡片輪播形式顯示在 webchat 中。

我們計劃未來支持更多類型的工具。

### 步驟 2：添加必填字段

要配置客制 GPT 工具，您需要提供幾個關鍵信息：

* **啟用工具**：打開**啟用**開關。這將激活該工具，允許 SeaChat 在相關對話中自動開始使用它。
* **工具名稱**：輸入工具的名稱。應僅包含字母（A-Z，a-z）、數字（0-9）、下劃線（\_）或連字符（-），不含任何空格。
* **HTTP 方法**：根據您的 API 所需的操作，從可用的 HTTP 方法中選擇（`POST`、`PUT`、`GET`、`PATCH`、`DELETE`）。
* **端點 URL**：輸入 SeaChat 將發送請求的 API 端點的 URL。
* **描述**：提供工具和 API 端點的簡要描述，以便 GPT 理解工具的功能和用途。

您還應該配置要與 API 請求一起發送的參數：

* **固定值參數**：這些是由您定義的預填參數，將在每個 API 請求中完全按照輸入的內容發送。
* **動態變量參數**：這些是 SeaChat 從對話中動態提取的參數。對於每個參數，提供應提取的信息描述，SeaChat 將在發出 API 請求之前使用對話上下文生成值。

### 步驟 3：配置結果顯示

配置 API 後，您可以決定如何在聊天中顯示其結果。默認情況下，API 結果將顯示為純文本。如果 API 響應缺少有效的 URL 或按鈕，您可以通過填寫默認圖像 URL 和默認按鈕標題來設置要顯示的後備卡片。要啟用後備卡片，只需勾選相關複選框。

### 步驟 4：測試您的 API 配置

填寫必填字段後，將根據您指定的參數自動生成測試查詢。您可以使用此測試區域來驗證您的 API 配置是否正常運行，並在右側查看 API 響應。

### 步驟 5：保存並完成

確認您的客制 GPT 工具設置按預期工作後，您可以通過點擊保存按鈕來保存配置，永久保存您的客制 GPT 工具設置。

## 配置圖片搜尋工具的步驟：

### 步驟 1：選擇工具類型

**圖片搜尋**工具類型通過添加圖像處理功能來擴展搜尋和顯示工具的功能。此工具類型專門設計用於：

* 接受用戶的圖像輸入（作為 URL 或上傳的文件）
* 通過您的 API 端點處理這些圖像
* 以帶有增強描述的可自定義卡片格式顯示結果

### 步驟 2：添加必填字段

與其他客制 GPT 工具類似，您需要提供：

* **啟用工具**：打開**啟用**開關以激活該工具，以便在相關對話中自動使用。
* **工具名稱**：使用僅包含字母（A-Z，a-z）、數字（0-9）、下劃線（_）或連字符（-）輸入唯一名稱。
* **HTTP 方法**：選擇適當的 HTTP 方法（圖像處理通常使用 `POST`）。
* **端點 URL**：提供將處理圖像請求的 API 端點 URL。
* **描述**：編寫清晰的描述，以幫助 GPT 理解何時以及如何使用此圖片搜尋工具。

### 步驟 3：圖像輸入數據配置

圖片搜尋工具引入了新的**圖像輸入數據**部分，允許您配置如何將圖像發送到您的 API 端點：

* **圖像 URL 字符串**：如果您的 API 期望接收圖像作為 URL 字符串，請選擇此選項。用戶可以提供圖像 URL，SeaChat 將直接將它們傳遞到您的端點。
* **圖像數據**：如果您的 API 需要實際的圖像二進制數據，請選擇此選項。用戶可以直接上傳圖像文件，SeaChat 將編碼的圖像數據發送到您的端點。

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/image-tool-image-input-data-configuration.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/image-tool-image-input-data-configuration.png"  alt="圖像輸入數據配置">
</a>

<br/>

*範例：配置如何將圖像發送到您的 API - 作為 URL 字符串或作為二進制數據。*

</center>

### 步驟 4：帶有描述的卡片設置

圖片搜尋工具通過在卡片設置部分添加**卡片描述**字段來增強卡片顯示功能：

* **卡片描述**：此新字段允許您為結果中的每張卡片配置自定義描述。您可以使用佔位符根據 API 響應數據動態填充描述。
* **圖像 URL**：指定 API 響應中包含圖像 URL 的字段。
* **按鈕設置**：配置用於用戶交互的按鈕標題和 URL。

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/image-tool-card-settings.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/image-tool-card-settings.png"  alt="帶有描述的卡片設置">
</a>

<br/>

*範例：卡片設置顯示新的卡片描述字段，用於自定義結果的顯示方式。*

</center>

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/image-tool-example.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/image-tool-example.png"  alt="圖片搜尋卡片顯示">
</a>

<br/>

*範例：最終的卡片顯示，顯示圖像下方帶有自定義描述。*

</center>

### 步驟 5：測試您的 API 配置

圖片搜尋工具根據您的圖像輸入數據配置提供靈活的測試選項：

**對於圖像 URL 字符串配置：**
* 在測試區域中輸入測試圖像 URL
* SeaChat 將此 URL 發送到您的 API 端點
* 查看響應以確保正確處理

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/image-tool-test-with-image-url.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/image-tool-test-with-image-url.png"  alt="使用圖像 URL 測試">
</a>

<br/>

*範例：使用圖像 URL 字符串測試圖片搜尋工具。*

</center>

**對於圖像數據配置：**
* 直接上傳測試圖像文件
* SeaChat 將編碼並將圖像數據發送到您的 API
* 驗證 API 正確處理二進制數據

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/image-tool-test-with-image-file.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/image-tool-test-with-image-file.png"  alt="使用圖像上傳測試">
</a>

<br/>

*範例：通過上傳圖像文件測試圖片搜尋工具。*

</center>

### 步驟 6：保存並完成

成功測試您的圖片搜尋工具配置後，點擊保存按鈕以永久存儲您的設置。然後，該工具將可用於用戶提供圖像的對話中。

## 配置電子郵件發送或簡訊發送工具的步驟

### 步驟 1：添加必填字段

您需要提供幾個關鍵信息：

- **啟用工具**：打開啟用開關。這將激活該工具，允許 SeaChat 在相關對話中自動開始使用它。
- **工具名稱**：輸入工具的名稱。應僅包含字母（A-Z，a-z）、數字（0-9）、下劃線（_）或連字符（-），不含任何空格。
- **描述**：添加簡要描述，以幫助 GPT 理解觸發電子郵件或簡訊的條件。

### 步驟 2：配置電子郵件/簡訊內容和收件人

您需要定義以下字段來設置要通過電子郵件或簡訊發送的實際消息內容。

- **標題**：對於發送電子郵件工具，提供電子郵件的標題。
- **內容**：編寫您要發送的內容。
- **選項**：如果需要，勾選選項以在電子郵件/簡訊末尾包含 AI 代理的響應。
- **收件人**：輸入以逗號分隔的收件人列表。如果 SeaChat 從 webchat 表單收集這些值，請使用佔位符，例如簡訊的 `{{user_phone}}` 或電子郵件的 `{{user_email}}`。

> 📝 注意：
> 
> 對於電子郵件，發件人地址默認為 `no-reply@seasalt.ai`。
> 對於簡訊，發件人號碼在通話渠道中配置。

### 步驟 3：保存並測試

完成配置客制 GPT 工具電子郵件或簡訊設置後，點擊保存按鈕以保存您的更改。然後，您可以通過與 AI 代理交互來測試您的工具。

## 限制

為確保最佳性能，客制 GPT 工具設置適用某些限制：

* **字符限制**：工具名稱、描述、所有固定值參數（鍵和值）以及所有動態變量參數（鍵和描述）的組合字符數不得超過 1024 個字符。
* **工具執行限制**：SeaChat 每個傳入的用戶消息最多激活一個啟用的 GPT 工具。這包括與日曆或實時代理轉接的任何集成，確保為每個對話選擇最相關的工具。
