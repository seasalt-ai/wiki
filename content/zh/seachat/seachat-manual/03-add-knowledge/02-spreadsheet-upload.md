---
title: "上傳試算表"
description: "上傳試算表檔案和表格到您的SeaChat AI機器人。詳細的教學,教您如何調教SeaChat AI助理根據上傳的文件內容回答客戶問題。"
lead: ""
date: 2024-03-11 10:43:51.069 +0100
lastmod: 2024-04-19 10:43:51.069 +0100
weight: 31
draft: false
images: []
aliases:
  - /zh/seachat/seachat-manual/03-add-knowledge/02-spreadsheet-upload
url: /zh/seachat/manual/add-knowledge/csv-upload/
---
> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。


## 簡介
SeaChat 提供多種方法來上傳文件到您的AI助理知識庫。在本教學中，我們將專注於**上傳試算表**的方法，在本教學結束時，您的 SeaChat 助理將擁有一個客製的知識庫為您服務。

## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/) 找到創建AI助理的步驟。


## 開啟知識庫
在側邊欄中，選擇**AI助理配置**下的**知識庫**。選擇**上傳試算表**，您就可以上傳 .csv 或 .xlsx 等電子試算表文件到您的AI助理知識庫。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step2.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step2.png" alt="知識庫面板">
</a>

*知識庫面板*
</center>

## 上傳檔案
點擊**上傳您的試算表**的區塊，您就可以從多種文件格式[^1]中選擇想要提交給AI助理的文件。送出後，知識庫會處理送出的文件並更新。
[^1]: SeaChat 支援 .csv, .xls, .xlsx, .xlsm, .xlsb, .odf, .ods 和 .odt 等文件。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step3.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step3.png" alt="SeaChat知識庫的試算表上傳功能介面">
</a>

*上傳檔案*
</center>

> :rotating_light: **注意事項** :rotating_light:
>
> 上傳文件前，請檢查文件是否符合以下兩個要求：
> - 表格必須在第一行有標題。
> - 單一行的內容不得超過 2000 個tokens。
> 參考**表格上傳準則**以獲取更多信息。

## 選擇上傳模式

我們現在支援兩種模式來上傳試算表或表格到知識庫。

- **將表格中每一行上傳為單獨的知識庫文件**: 當您表格中的每一行都包含一個自成一體的資訊時，請選擇這個模式。例如,如果每一行都是關於一個產品的相關資訊,可以選擇這個模式,將每個產品說明分開儲存在知識庫中。

- **將表格上傳為單一知識庫文件**:當整個表格中的資訊是互相關聯的時候,請使用這個選項。例如,如果您有一個全天活動時程表的表格,我們建議將整個表格作為單一KB文件上傳,以確保AI助理在檢索知識庫時能一併參考整個時程表。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240507-spreadsheet-upload-mode.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240507-spreadsheet-upload-mode.png" alt="選擇SeaChat試算表上傳模式">
</a>

*請選擇適合您表格內容的上傳模式*
</center>


## 送出文件前
SeaChat允許用戶批量上傳。您可以在拖放區域下方的部分查看每個上傳檔案的狀態。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step4.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step4.jpg" alt="已上傳檔案預覽">
</a>

*已上傳檔案預覽*
</center>

向下滾動以查看專用的預覽窗口，該窗口將列出您的試算表格的前10行。一旦確認所有要上傳的檔案無誤，您可以點擊**繼續**按鈕進行上傳。

> :construction: **嵌入 Excel 的圖片**
>
> 目前，SeaChat 不支援上傳嵌入在 Excel 文件中的圖片。如果您希望包含圖片資料，請將圖片分別上傳到特定的知識中。
>
> 例如，如果您想在某個知識中包含卡片的圖片，您可以先上傳 Excel 文件，然後將圖片分別上傳到卡片知識中。


###### 預覽範例:
<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step4-table-example.jpg" alt="預覽範例">
</center>

## 已添加到知識庫

您已成功上傳新知識。要查看已上傳的檔案，您可以至頁面右上角的「**現有知識**」區塊，在那裡您可以在「**上傳檔案**」裡找到剛剛上傳的資料。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step5.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step5.jpg" alt="在現有知識中查找文件">
</a>

*在 **現有知識** 中查找文件*
</center>

## 檢查知識庫

點擊您剛剛上傳的檔案並檢視內容。大功告成！您已成功地將一份試算表格上傳到您的SeaChat助理中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step6.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/02-spreadsheet/20240313-spreadsheet-tutorial-step6.jpg" alt="審核上傳的試算表">
</a>

*審核上傳的試算表*
</center>

## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seasalt.ai](mailto:seachat@seasalt.ai).



 