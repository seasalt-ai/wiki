---
title: "工作區管理"
description: "SeaChat 工作區管理"
lead: ""
date: 2020-10-06T08:48:45+00:00
lastmod: 2024-06-27T08:48:45+00:00
weight: 91
draft: false
images: []
aliases:
  - /en/seachat/seachat-manual/workspace/01-workspace-management
  - /seachat/seachat-manual/workspace/01-workspace-management
---

## AI助理

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/agents.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/agents.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">助理管理</p>
</div>

這裡可以管理所有的AI助理。每一行代表一個AI助理及其名稱、電子郵件和狀態。您還可以看到未讀消息的數量，找到AI助理對話的 URL，直接啟動對話或新增AI助理。

## 成員

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/members.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/members.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">成員管理</p>
</div>

成員有不同的類型。根據成員類型，他們會有不同的權限。如果您是工作區的擁有者，可以新增成員並分配不同的角色。以下是一些可以分配給成員的角色：

1. 系統管理者：擁有工作區的全部訪問權限，可以管理所有設置，編輯 AI 助理的設置，管理知識庫，訪問助理對話並以人工助理的身份接管對話。
2. AI 助理開發者：可以編輯 AI 助理的設置，管理知識庫，訪問助理對話和測試。
3. 人工助理：可以訪問助理對話並以人工助理的身份接管對話。

### 編輯使用者

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/add-member.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/add-member.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">成員設置</p>
</div>

您可以將不同的助理分配給不同的成員。例如，將測試中的助理分配給您的 AI 助理開發者，將產線中的助理分配給您的人工助理。管理員可以訪問和監控這兩種類型的助理。

## 工作區偏好設置

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/preference.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/preference.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">偏好設置</p>
</div>

這裡可以管理工作區的通知設置。SeaChat 可以自動向您發送電子郵件，通知您新對話和新的人工助理請求。啟用您想接收的通知類型後，還可以設置通知的語言。

### 通知設置

SeaChat 提供不同語言的通知。您可以選擇接收通知的語言。雖然可以將語言設置為默認值（與外觀語言相同），但我們建議設置為您在對話中的預定語言。這有助於優化助理的性能並加快操作速度。

## 工作區 API 金鑰

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/workspace-api.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/workspace-api.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">SeaChat API 金鑰</p>
</div>

如果您希望以編程方式訪問您的工作區或助理，可以使用在 **工作區** 下找到的 API 金鑰。在這裡可以生成新的 API 金鑰，查看現有的金鑰並刪除它們。請確保在使用 API 金鑰之前設置以下兩個先決條件：

1. 工作區創建：如果尚未創建，請在 SeaChat 中創建工作區，並記下 URL 中的工作區 ID，格式為：`https://chat.seasalt.ai/gpt/workspace/{workspace-id}/bot/{bot-id}/`。
2. 訪問憑證：通過聯繫 seachat@seasalt.ai 獲取您的客戶端 ID 和訪問令牌。這些憑證對於驗證您的 API 請求至關重要。這是在 **API 金鑰** 部分應用訪問令牌的地方。

SeaChat API 使用 Bearer 驗證方法，因此必須在 API 請求的標頭中應用您的 bearer 令牌。例如，如果使用 curl，可以使用以下代碼片段來驗證您的 API 請求：

```curl
curl -X 'POST' \
  'https://chat.seasalt.ai/api/v1/public/bots' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer [access token]' \
  -H 'Content-Type: application/json' \
  -d '{
    "workspace_id": "XXXXX-XXX-XXXXXXXXX",
    "name": "SeaChat",
    "description": "string",
    "use_case": "Customer Service",
    "live_agent_transfer": false,
    "default_response_language": "default",
    "is_enabled": true
  }'
```

SeaChat API 是一個進階的工具，允許您以編程方式訪問您的工作區和助理。您可以使用 API 創建新AI助理，管理現有AI助理，並訪問對話歷史記錄。更多有關 SeaChat API 的信息，請參閱 [API 文檔](https://chat.seasalt.ai/redoc)。或通過 [seachat@seasalt.ai](mailto:seachat@seasalt.ai) 聯繫我們。