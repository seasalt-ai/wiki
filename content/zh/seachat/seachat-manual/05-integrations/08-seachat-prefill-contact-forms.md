---
title: "以程式設計方式在 WebChat 中預先填寫聯絡表格"
description: "SeaChat 支援透過偵測網路聊天 URL 中的查詢字串來預先填入網路聊天表單中使用者資訊。這允許您的網站和聊天小部件之間的無縫集成，您的客戶不需要手動輸入他們的詳細資訊。"
date: 2024-07-16T08:48:57+00:00
lastmod: 2024-07-16T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /zh/seachat/seachat-integrations/seachat-prefill-contact-forms/
url: /zh/seachat/integrations/seachat-prefill-contact-forms/
weight: 405
toc: true
---

SeaChat 支援透過偵測網路聊天 URL 中的查詢字串來預先填入網路聊天表單中使用者資訊。這允許您的網站和聊天小部件之間的無縫集成，您的客戶不需要手動輸入他們的詳細資訊。

<center>
<a href="/images/seachat-integrations/widget/demo1.gif">
<img height="800px" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/demo1.gif" alt="Demo GIF of prefilling">
</a>
</center>

<br/>

這主要用於最終用戶已登入您的系統的情況，然後您可以使用他們的登入資訊自動填寫聯絡表單。在這種情況下：

1. 使用者無需再次手動填寫聯絡表，從而節省時間。
2. 防止使用者在聯絡表單中輸入錯誤或虛假資訊。

### **使用案例**

在網路聊天表單中預先填寫使用者詳細資訊的功能在以下場景中特別有用：

1. 客戶支援與服務台  
   當使用者從客戶支援入口網站發起聊天時，可以自動填寫他們的詳細資料（姓名、電子郵件、電話）以節省時間。
2. 網站和應用程式上的登入用戶  
   如果用戶已經登錄，他們的詳細資訊可以自動注入到網路聊天表單中。

3. 電子商務與銷售查詢表  
   如果客戶正在瀏覽產品並需要支持，他們的帳戶詳細資訊可以傳遞到聊天中。

4. 預訂和預訂系統  
   在線上預訂或預約安排中，人工智慧代理可以預先填寫客戶信息，以更快地確認他們的詳細資訊。

5. 潛在客戶捕獲和行銷活動  
   在執行電子郵件活動或廣告時，預先填寫的聊天表單可確保潛在客戶在與人工智慧代理商互動時無需重新輸入資訊。

---

### 如何設置

#### 步驟 1: 新增要在 WebChat 中顯示的聯絡表單

1. 登入 SeaChat 並前往 **頻道** 標籤。
2. 點選 **網頁AI助理** 卡
3. 轉到右上角的 **客製表單** 選項卡
4. 點選**\+ 新增表單**
5. 透過開啟頁面頂部的開關來啟用表單
6. 如果您允許使用者跳過表單，**允許使用者跳過表單**
7. 如果您想客製，請編輯表單
8. 編輯完成後，點選**儲存**

<center>
<a href="/images/seachat-integrations/widget/webchat form configuration.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/webchat form configuration.png" alt="webchat form configuration">
</a>
</center>

<br/>

#### 步驟 2: 檢索您的網路聊天小工具程式碼

1. 登入 **SeaChat** 並導航至 **頻道** 選項卡。
2. 點選 **讓您的網路聊天小工具支援全通路** 按鈕。
3. 複製**小工具程式碼**並將其整合到您的網站。

<center>
<a href="/images/seachat-integrations/widget/widget code page.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/widget code page.png" alt="widget code page">
</a>
</center>

<br/>

#### 步驟 3: 將查詢參數附加到 Webchat URL

您將在小工具程式碼中找到以下格式的網路聊天 URL：

`https://chat.seasalt.ai/chat/uuid`

若要預先填寫使用者詳細資料（例如姓名、電子郵件和電話號碼），您應該將查詢參數附加到小工具代碼中的所有網路聊天 URL。

<center>
<a href="/images/seachat-integrations/widget/widge code highlight url.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/widge code highlight url.png" alt="widge code highlight url">
</a>
</center>

<br/>

##### 字段格式：

| 使用者資訊 | 查詢參數 |
| :--------- | :------- |
| **郵箱**   | `_EMAIL` |
| **姓名**   | `_NAME`  |
| **電話**   | `_PHONE` |

##### 範例：使用使用者姓名、電子郵件和電話號碼預先填寫網路聊天表單

您的原始網頁聊天 URL 是：

```
https://chat.seasalt.ai/chat/uuid
```

您應該如下修改您的網頁聊天 URL：

```
https://chat.seasalt.ai/chat/uuid?_NAME=JohnDoe&_EMAIL=johndoe@example.com&_PHONE=123456
```

當網路聊天載入修改後的 URL 時，表單將自動填入所提供的使用者詳細資料：

- **姓名:** John Doe
- **郵箱:** [johndoe@example.com](mailto:johndoe@example.com)
- **電話:** 123456

<center>
<a href="/images/seachat-integrations/widget/demo1.gif">
<img height="800px"style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/demo1.gif" alt="Demo GIF of prefilling">
</a>
</center>

<br/>

### 新增自訂字段

SeaChat 也支援在網路聊天表單中預先填寫自訂欄位。

#### 如何將自訂欄位新增至網頁聊天表單：

1. 登入 **SeaChat** 並導航至 **頻道** 選項卡。
2. 前往 **網頁AI助理** 卡。
3. 導覽至 **自訂表單** 標籤並編輯您的表單。
4. 按一下**\+新增** 新增新的自訂欄位。
   - 當您新增第一個自訂欄位時，它將使用`VAR_0001`。
   - 如果您添加更多字段，它們將使用 `VAR_0002`、`VAR_0003`等。

##### Custom Field Format:

| 使用者資訊     | 查詢參數   |
| :------------- | :--------- |
| **自訂欄位 1** | `VAR_0001` |
| **自訂欄位 2** | `VAR_0002` |

##### 範例：使用使用者名稱和帳號 ID 預先填寫網頁聊天表單

如果您想在網頁聊天表單中預先填寫 **帳戶 ID**（使用`VAR_0001`標識）字段，則更新後的網路聊天 URL 將如下所示：

```
https://chat.seasalt.ai/chat/uuid?_NAME=JohnDoe&_EMAIL=johndoe@example.com&_PHONE=123456&VAR_0001=9876
```

當網路聊天載入時，表單將自動填寫：

- **姓名:** John Doe
- **郵箱:** [johndoe@example.com](mailto:johndoe@example.com)
- **電話:** 123456
- **帳戶ID:**9876

<center>
<a href="/images/seachat-integrations/widget/demo2.gif">
<img height="800px"style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/demo2.gif" alt="Demo GIF of prefilling">
</a>
</center>

<br/>

## **概括**

- 從 SeaChat 檢索並整合 **網路聊天小工具程式碼**。
- 使用`_NAME`, `_EMAIL`, 和 `_PHONE` **網路聊天 URL**。
- 使用`VAR_0001`, `VAR_0002`等新增**自訂欄位**。
- 當使用者開啟網路聊天時，表格會**自動預先填寫**。
