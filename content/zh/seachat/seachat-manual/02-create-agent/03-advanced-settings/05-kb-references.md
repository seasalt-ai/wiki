---
title: "在聊天中啟用引用"
description: "Seasalt.ai 提供的 SeaChat 知識庫引用功能為使用者提供了一種便捷且高效的方式，讓聊天回應可以連結回其使用的相關文件。啟用此功能後，每個聊天回應都會包含引用部分，列出來源文件，使使用者能夠清楚了解哪些資訊被用來生成回應內容。"
lead: ""
date: 2025-02-11T08:48:45+00:00
lastmod: 2025-02-11T08:48:45+00:00
weight: 109
draft: false
images: []
toc: true
aliases:
  - /zh/seachat/seachat-manual/02-create-agent/03-advanced-settings/05-kb-references
  - /zh/seachat/manual/create-agent/advanced-settings/kb-references/
url: /zh/seachat/manual/create-agent/advanced-settings/kb-references/
---

#### 概述

Seasalt.ai 提供的 SeaChat 知識庫引用功能為使用者提供了一種便捷且高效的方式，讓聊天回應可以連結回其使用的相關文件。啟用此功能後，每個聊天回應都會包含引用部分，列出來源文件，使使用者能夠清楚了解哪些資訊被用來生成回應內容。

#### 如何啟用知識庫引用功能

請按照以下步驟啟用此功能：

1. **進入 助理資訊 \-\> 進階設定 標籤頁**
2. **切換 知識庫引用 開關**
   - 找到知識庫引用設定，將其打開以啟用該功能。

<center>
<a href="/images/seachat/zh/kb-references/image01.png">
<img height="100%" width="100%" src="/images/seachat/zh/kb-references/image01.png"  alt="KB References Section in the Advanced Settings Page">
</a>
<br/>

</center>

啟用後，AI 智能助理的回應下方將顯示引用部分，列出 SeaChat 在生成答案時使用的知識庫文件名稱。如果來源是可點擊的 URL，則會顯示為連結，方便使用者快速訪問。這樣可以幫助使用者驗證來源，更清楚了解AI 智能助理回應的形成過程。

#### 哪些知識庫條目會顯示為引用？

可作為知識庫引用的條目類型包括：

#### **1\. 基於 URL 的條目**

添加到知識庫的網頁或可公開訪問的文章。當AI 智能助理從 URL 檢索資訊時，引用部分會顯示一個可點擊的連結

<center>
<a href="/images/seachat/zh/kb-references/image02.png">
<img height="100%" width="100%" src="/images/seachat/zh/kb-references/image02.png"  alt="AI agent response displays two clickable urls">
</a>
<br/>

_範例：AI 智能助理的回應顯示兩條可點擊的網址連結_

</center>

#### **2\. 手動新增的知識庫條目**

手動添加的自定義文本條目。通常是SeaChat「新增知識庫文件」頁面中撰寫的短文件或 FAQ。在引用部分，將顯示手動添加的 KB 條目的標題。

<center>
<a href="/images/seachat/en/kb-references/image03.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image03.png"  alt="A Manual KB entry">
</a>
<br/>
</center>
<br/>
<center>
<a href="/images/seachat/en/kb-references/image04.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image04.png"  alt="AI agent response displays a citation from the Manual KB entry">
</a>
<br/>

_範例：AI 智能助理的回應顯示手動添加的 KB 條目 引用_

</center>

#### **3\. 上傳至知識庫的文件**

使用者上傳至知識庫的各種文件類型。當AI 智能助理生成的回應參考了這些上傳文件時，文件名稱將顯示在引用部分。支援的文件格式：

- Excel 文件 (.csv, .xls, .xlsx, .xlsm, .xlsb, .odf, .ods and .odt)

- 文本文件 (.doc, .docx, .eml, .epub, .gif, .jpg, .json, .html, .msg, .odt, .ogg, .pdf, .png, .pptx, .ps, .rtf, .tiff, .txt, .zip)

<center>
<a href="/images/seachat/en/kb-references/image05.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image05.png"  alt="A document">
</a>
<br/>
</center>
<br/>
<center>
<a href="/images/seachat/en/kb-references/image06.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image06.png"  alt="AI agent response displays a citation from the document">
</a>
<br/>

_範例：AI 智能助理的回應顯示手動文本文件的引用_

</center>

<center>
<a href="/images/seachat/en/kb-references/image07.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image07.png"  alt="An Excel file">
</a>
<br/>
</center>
<br/>
<center>
<a href="/images/seachat/en/kb-references/image08.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image08.png"  alt="AI agent response displays a citation from a worksheet: renewable_energy-xlsx">
</a>
<br/>

_範例：AI 智能助理的回應顯示手動Excel文件的引用_

</center>

#### 應用場景

以下是幾個知識庫引用應用場景：

- **客戶支援 & 服務中心**
  - 人工客服可以快速確認AI 智能助理的回應是否符合官方文件
  - 客戶可以查看資訊來源，確保透明度與可信度
- **內部知識共享**
  - 員工可以透過 SeaChat 查找公司政策或技術指南，並檢查引用來源的準確性
  - 新員工培訓變得更加高效，他們可以直接追溯AI 智能助理回應所依據的內部知識庫文件
- **教育 & 研究**
  - 學生與研究人員可以使用 SeaChat 進行學術查詢，並驗證所使用來源的可靠性
  - 教師可以透過引用資料引導學生獲取特定的參考材料

啟用知識庫引用功能後，使用者可以更了解AI 智能助理回覆的來源、增加對AI 智能助理回應的信任，並更好地控制AI 智能助理生成的內容。🚀
