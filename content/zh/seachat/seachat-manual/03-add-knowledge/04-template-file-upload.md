---
title: "上傳模板文件"
description: "探索如何使用CSV和JSON格式的模板文件來快速且有效地上傳數據到您的SeaChat知識庫。學習如何定制您的AI助理的知識庫，以提高對客戶查詢的響應速度和質量。"
lead: ""
date: 2024-04-18 10:43:51.069 +0100
lastmod: 2024-04-19 10:43:51.069 +0100
weight: 33
draft: false
images: []
aliases:
  - /zh/seachat/seachat-intro/03-add-knowledge/04-template-file-upload/
url: /zh/seachat/manual/add-knowledge/template-upload/
---
> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/seachat-manual/03-add-knowledge/file-size-rule/)了解更多資訊。


## 簡介
SeaChat 提供許多不同的方式讓您上傳文件到您助理的知識庫中。在本教學中，我們將專注於 **上傳試算表** 方法，到教學結束時，您的 SeaChat 助理程式將具有一個定制的知識庫，為您提供服務。

## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](https://wiki.seasalt.ai/zh/seachat/seachat-manual/02-create-agent/01-create-new-agent/) 找到創建AI助理的步驟。

## 開啟知識庫
在側邊欄中，選擇**AI助理配置**下的**知識庫**。單擊 **從模板文件上傳**。SeaChat 提供模板文件，您可以直接輸入並上傳。


<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/knowledge-base.png" alt="透過側邊欄菜單中的助理配置進入知識庫面板以顯示如何通過選擇從模板文件上傳來上傳 CSV 或 JSON 文件到助理程式。">

*知識庫面板*
</center>

## 模板文件
SeaChat 提供 CSV 和 JSON 模板文件，您可以下載並填入您的數據。填入模板文件後，您可以通過單擊拖放區域來將其上傳到您AI助理的知識庫。

###### 預覽示例：
```CSV```

<div style="overflow-x: auto;">
<table>
<tr>
  <th>id</th>
  <th>title</th>
  <th>text</th>
  <th>references</th>
  <th>reminder</th>
  <th>capture</th>
  <th>live_agent_transfer</th>
  <th>sample_key</th>
</tr>
<tr>
  <td>kb-1</td>
  <td>Sample KB Doc</td>
  <td>This is an example of a KB document.</td>
  <td>[{"title":"Seasalt.ai","url":"https://seasalt.ai"}]</td>
  <td>This is some reminder text!</td>
  <td>Email,Phone Number</td>
  <td>False</td>
  <td>sample value</td>
</tr>
</table>
</div>


```JSON```
```json
[{
  "id": "kb-1",
  "title": "Sample KB Doc",
  "text": "This is an example of a KB document.",
  "custom": {"sample_key": "sample value"},
  "actions": {
    "references": [
      {"title": "Seasalt.ai", "url": "https://seasalt.ai"},
      {"title": "SeaChat", "url": "https://chat.seasalt.ai/"}
    ],
    "reminder": "This is some reminder text!",
    "capture": ["Email", "Phone Number"],
    "live_agent_transfer": false
  }
}]
```

1. **id**: 文件的唯一識別碼。
2. **title**: 文件的標題。
3. **text**: AI助理將解釋的文件內容。
4. **custom**: AI 助理可以參考的附加信息。例如，當您需要改進知識庫回應時，可以向文件添加自訂的鍵值對供 AI 助理參考。
5. **references**: AI 助理可以提供的附加信息或連結。其中 title 是在界面中顯示的參考名稱，url 是連結。
6. **reminder**: AI 助理將在格式化的提醒橫幅中提供的附加信息。
7. **capture**: AI 助理將從用戶那裡捕獲的信息。舉例來說，當使用該特定的知識時，AI 助理會向用戶詢問並捕獲欄位中的值。
8. **live_agent_transfer**: 決定是否允許用戶在對話中轉接至真人客服。


## 送出文件前
SeaChat允許用戶批量上傳。您可以在拖放區域下方的部分查看每個上傳檔案的狀態。點擊**送出**後，知識庫會處理送出的文件並更新。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/before-submission.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/before-submission.png" alt="Interface of SeaChat showing the upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded, reminding users to verify file format and content before submission.">
</a>

*檢查已上傳文件*
</center>


## 已新增到知識庫
您已成功上傳新知識。要查看已上傳的檔案，您可以至頁面右上角的「**現有知識**」區塊，在那裡您可以在「**上傳檔案**」裡找到剛剛上傳的資料。
<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/existing-files.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*到「**現有知識**」中的「**上傳檔案**」*
</center>

## 檢查知識庫
點擊您剛剛上傳的檔案並檢視內容。大功告成！您已成功地將一份模板文件上傳到您的SeaChat助理中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。

<div style="display: flex; justify-content: space-between; align-items: center;">
  <div style="display: flex; flex-direction: column; text-align: center;">
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/csv-uploaded.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/csv-uploaded.png" alt="Example of a successfully uploaded csv.">
</a>
    <em>CSV 檔案</em>
  </div>

  <div style="display: flex; flex-direction: column; text-align: center;">
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/json-uploaded.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/json-uploaded.png" alt="Example of a successfully uploaded json.">
</a>
    <em>JSON 檔案</em>
  </div>
</div>


## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。
