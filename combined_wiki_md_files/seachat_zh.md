# Seachat Documentation

*Combined documentation from content/zh/seachat/ (Hugo weight-ordered)*

---


### 簡介

<!-- Source: getting-started/01-seachat-intro.md -->

<!-- Weight: 1 -->

*在僅需10分鐘內創建您的專屬AI聊天助理。我們的AI助理能夠無縫轉接至真人客服，確保每一位客戶都得到最適切的支援。深入了解如何利用SeaChat增強您的商業互動，改善客戶體驗。*


SeaChat能讓你在10分鐘做出專屬AI聊天助理，能進行溫暖自然的對話。運用在推薦產品、售前諮詢、售後服務等等場景，幫助你提升客戶滿意度，並可隨時轉接真人。


<iframe width="100%" height="350px" src="https://www.youtube.com/embed/II697TMK-Jw?list=PL8K7_LTqly449uOg_uBWOPfFyL1fJRjkE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

---


### 快速入門

<!-- Source: getting-started/02-quick-start.md -->

<!-- Weight: 2 -->

*在10分鐘內設置您專屬的SeaChat AI助理！這份快速入門指南將逐步引導您創建工作區並配置一個符合您業務需求的AI助理，並大幅提升客戶互動與滿意度。*

---
* 在不到10分鐘的時間內，您就可以設置好自己的定制AI助理，隨時協助您的客戶。
* 如需更詳細的指導，請查閱[SeaChat說明書](https://wiki.seasalt.ai/zh/seachat/getting-started/01-seachat-intro/)。如果遇到任何問題或有疑問，我們的[支援團隊](#support)隨時待命協助您。請隨時聯繫我們。
---

在本教學中，我們將從頭開始創建一個SeaChat助理。這個AI助理將回答客戶有台北市公園的相關問題。我們將引導您完成創建AI助理的過程，向其知識庫添加知識，測試和調整助理，以確保它準備好回答客戶的所有來信問題！在本教學結束時，你將會擁有一個準備好部署的AI助理。

## 步驟1：創建工作區
如果這是您第一次登錄SeaChat，您將需要創建一個工作區來開始過程。點擊 **建立** 以創建您的第一個工作區。我將我的新工作區命名為**Seasalt.ai**。您可以為您的工作區取一個不同的名稱！

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/choose-workspace.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/choose-workspace.png" alt="示意圖顯示創建工作區的儀表板。">
</a>

*創建第一個工作區*
</center>

> **什麼是工作區？**
>
>  工作區包含了您所有資料、助理詳情、設定、知識庫，提供您的助理、成員和API金鑰的總覽，用來區隔您的不同專案或組織。您可以選擇為自己創建一個新的工作區，或通過向管理員請求邀請加入現有的一個工作區。

## 步驟2：您的第一個SeaChat助理
點擊**新增AI助理**來配置您的新助理。如果您已經有一個工作區和一個助理，您可以通過點擊位於右上角靠近您個人頭像的下拉選單來創建一個新的助理。

> :books: **AI助理和真人助理**
>
>您將在整個教學中一直看到**助理**這個詞。**AI助理**本質上是一個具有自定義知識庫的AI助手，我們使用這個詞是為了強調它協助您的客戶的能力，就像一個真人助理一樣。而**真人助理**則指的是與客戶實時互動的實際客服人員。

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/create-agent.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/create-agent.png" alt="圖片顯示如何導航到助理創建儀表板。">
</a>

*新增AI助理*
</center>

接下來，讓我們選擇**一鍵開始**創建一個新的代理。如果您有偏好的使用案例，也可以選擇從**使用案例模板**開始。

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/choose-agent-create.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/choose-agent-create.png" alt="一個顯示如何進入代理創建儀表板的圖片。">
</a>

*選擇 **一鍵開始***

</center>
<br/>

<br/>

在**新AI助理**中，給您的助理添加一些關於其角色和功能的背景，然後選擇其使用情境和回覆語言。在本教學中，我將選擇**FAQ**作為用例，因為這個助理將用於回答常見問題，並選擇**繁體中文**作為回覆語言。
<br/>

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/new-agent-info.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/new-agent-info.png" alt="圖片顯示助理配置界面。">
</a>

*AI助理配置*
</center>

<br/>

<br/>

> :bulb: **注意**
>
> 真人助理功能將要求一個真人客服人員介入。如果您選擇此選項，客戶將有機會在聊天中請求轉接真人助理，請安排至少一個真人客服人員來回應正在進行的對話。
>

## 步驟3：新增知識
為了充分利用您的SeaChat助理的功能，我們需要向其知識庫添加知識。SeaChat為您的助理知識庫上傳內容提供了多種選擇。通過導航到側邊選單中的**知識庫**儀表板，找到您助理的知識庫。

你可以自由嘗試不同的知識上傳方式。為了本教學的目的，我們將使用**上傳試算表**方法。然而，如果您對探索其他知識上傳方式感興趣，我們邀請您查看我們用戶手冊中的[知識庫](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/intro/)部分，以獲取全面的指導和建議。

歡迎下載本教學的[試算表範本](/sample-files/TaipeiParkFacility_Arcade.xlsx)，並自己試試看如何上傳到AI助理的知識庫中。

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/choose-upload-method.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem;cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/choose-upload-method.png" alt="圖片建議用戶選擇上傳試算表方法來上傳至助理的知識庫。">
</a>

*選擇一種上傳方式*
</center>

<br/>

## 步驟4：將文件上傳至知識庫
上傳試算表很簡單，只需點擊上傳圖標並選擇所需的試算。一旦您在拖放部分下方的預覽部分看到您上傳的文件，點擊**繼續**按鈕確認。

在上傳文件後，我們可以在預覽部分看到每個標題及其對應的數據。現在，我的AI助理現在準備好進行下一步了。

要查看已上傳的數據，我們只需導航到儀表板右上角的**現有知識**部分，一旦您的文件成功上傳即可。

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/upload-document.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/upload-document.png" alt="圖片顯示文件上傳成功的消息。">
</a>

*文件上傳*
</center>

<br/>

就這麼簡單。現在，我的AI助理已經處理了上傳的數據，讓我們進行測試，看看是否需要進一步調整。點擊位於右下角的**測試AI助理**按鈕。讓我們嘗試與我的AI助助理聊天，看看是否可以優化其性能！

`<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem;cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/review-upload.png" alt="圖片指示測試AI助理按鈕的位置。">
</a>

*點擊**測試AI助理***
</center>

<br/>`

## 步驟5：測試您的SeaChat助理

在使用我們剛剛建立的AI助理投入前，通過測試和調整來訓練它是非常重要的。想象自己是與AI助理互動的客戶。您現在可以開始提問，看看您的SeaChat助理如何回應。

隨著知識庫的更新，我的AI助理現在已經準備好進行測試。在點擊**測試AI助理**後的對話框中，您可以開始提問，看看您的助理如何回應。這是我跟我助理的對話。

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/agent-conversation.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/agent-conversation.png" alt="圖片展示與AI助理的對話。">
</a>

*與AI助理的對話*
</center>

<br/>

要審查消息，請將游標停在該消息上，如果您希望為您的助理提供正面回饋，給它一個讚。如果消息需要進一步審查，給它一個負評。

哎呀，看來我的AI助理需要一些調整。我將在這裡給它一個負評來提供回饋。

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/conversation-feedback.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/conversation-feedback.png" alt="圖片顯示如何審查助理的回答。">
</a>

*審查助理的回應*
</center>

<br/>

## 步驟6：SeaChat助理微調

SeaChat為您提供了一套先進的工具，讓您能夠將您的助理調整到完美狀態。您可以在左側側邊選單的**檢視對話**部分找到這些功能。在這裡，您可以審查已收到您回饋的回應。

看起來獨角獸公園的信息並沒出現在我的AI助理的知識庫中。點擊**新增知識庫文章**來新增相關知識。
<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/review-feedback.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/review-feedback.png" alt="圖片指示修改助理知識數據的按鈕。">
</a>

*審查助理的回應*
</center>

<br/>

在**新增知識庫文章**中，您可以為您的助理添加新的知識。在這裡，我將添加有關獨角獸公園的信息。您也可以在這裡添加附加訊息和連結按鈕。

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/edit-response.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/edit-response.png" alt="圖片顯示如何微調您的AI助理的回應。">
</a>

*修改相關文件*
</center>

<br/>

現在，一旦您確定已上傳的信息，請點擊保存。不要忘記點擊**移至已審查**來完成您的更改。
您可以切換到**已審查**部分查看您所做的更改。全部完成！現在，讓我們再次測試助理，看看它是否有所改善。

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/move-reviewed-response.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/move-reviewed-response.png" alt="圖片提醒用戶將審查過的消息標記為已審查。">
</a>

*標記對話為已審查*
</center>

<br/>

你看！我的AI助理現在能給出正確的信息了。就是這麼簡單！您現在可以自己嘗試，看看您的助理表現如何。

<br/>
<center>
<a href="/images/seachat/zh/tutorial-intro/finetune-result.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/tutorial-intro/finetune-result.png" alt="圖片展示AI助理的優化表現。">
</a>

*經過微調的優化回應*
</center>

<br/>

微調您的AI助理是一個至關重要且持續的過程。我們建議您查看我們用戶手冊中的**進階**部分，以獲得更全面的解釋並了解參與微調過程的不同參數和功能。


## 定制AI助理為您服務

親眼見證SeaChat AI助理如何提升您的運營。從客戶服務和市場營銷到擔任協作協調者，SeaChat使您能夠輕鬆自動化工作流程以實現最佳效率。
在本教學中，我們已經引導您完成了設置並微調您的第一個AI助理的步驟。然而，要完全釋放SeaChat AI助理的力量，還有一些方面需要您掌握。我們誠摯地邀請您探索我們詳細的[說明書](/zh/seachat/seachat-manual/)，以了解SeaChat的真正潛力，或者您可以直接聯繫我們的[支援團隊](#support)獲得更多信息和協助。

## 需要幫忙
需要協助？請聯繫我們：[seachat@seasalt.ai](mailto:seachat@seasalt.ai)。



---


### 免費真人客服模式

<!-- Source: getting-started/01-seachat-free-agent-mode.md -->

<!-- Weight: 3 -->

*免費使用真人客服模式，隨時準備好後再升級*

---


<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/tYLpWa3LeCM?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


## 如何免費開始使用 SeaChat？

### 第一步

在 [SeaChat](https://chat.seasalt.ai/?utm_source=wiki) 開設帳戶。不需要信用卡！我們的新手指南將引導您創建第一個 SeaChat 客服助理系統。要免費使用 SeaChat 而不產生額外費用，只需在 **對話處理模式** 選項中選擇 **僅真人客服模式(Human Agent Only)** 即可。

<br/>
<center>
<a href="/images/seachat/zh/getting-started/free-human-agent-mode.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/getting-started/free-human-agent-mode.png" alt="顯示對話處理模式選項（Human Only 模式）的圖片">
</a>

*選擇僅真人客服模式*
</center>

**您將開始使用免費方案。若需要使用 AI 驅動的回應功能時，才需要升級為付費方案。**

真人客服模式包含：
- 支援多渠道接收消息（網頁聊天 — 您的網站小工具、Facebook Messenger、WhatsApp、LINE）
- 通過統一的對話面板進行手動回應（您將親自回應所有消息）
- 配額：1 名客服人員（1 個用戶帳戶），1 個工作區
- 無隱藏費用或使用限制，可以無限聊天並保持所有對話記錄


### 第二步

將您的新 SeaChat 客服系統安裝到 [網站](https://wiki.seasalt.ai/zh/seachat/manual/channels/webpage/)、[Facebook Messenger](https://wiki.seasalt.ai/zh/seachat/manual/channels/facebook-messenger/), [WhatsApp](https://wiki.seasalt.ai/zh/seachat/integrations/whatsapp/), 或 [LINE](https://wiki.seasalt.ai/en/seachat/manual/channels/install-to-line/)。

### 第三步

在不花費客服機器人費用的情況下擴展您的業務——直到您需要時再考慮升級。

---
## 什麼時候需要付費？
只要您需要手動跨渠道回應客戶消息，我們都支持您免費使用，幫助您擴展業務。

我們的用戶通常會在以下情況下選擇升級為付費 SeaChat 方案：

- 需要回應大量客戶詢問
- 提供即時、智能、自動化的回應
- 根據自定義知識庫回答問題
- 提供 24/7 客戶支持
- 接聽客戶電話
- 將重心放在更重要的業務上，而非處理重複性請求

- 使用 SeaChat，您可以隨時啟用或停用 AI 支持，而無需更改現有的多渠道設置。享受按需 AI 支持的靈活性！

---


#### 建立新助理

<!-- Source: seachat-manual/02-create-agent/01-create-new-agent.md -->

<!-- Weight: 100 -->

*使用 SeaChat 輕鬆建立新的 AI 助理。按照用戶指南從頭開始設置助理或選擇預定義的使用案例。立即開始吧！*


## 建立新的 AI 助理

如果這是您第一次使用 SeaChat，您將需要建立一個新的助理。在創建工作區或被邀請加入工作區後，SeaChat 會將您帶到助理創建頁面。請查看我們[AI助理資訊](https://wiki.seasalt.ai/zh/seachat/manual/create-agent/agent-information/)的教學，以深入了解AI助理。

有時您可能希望為不同的使用案例、語言或不同的助理描述創建新的助理。SeaChat 允許用戶從頭開始創建助理或應用預定義的使用案例。現在，讓我們來看看如何使用這兩種不同的方法來創建新的助理。

首先，讓我們使用在您的頭像旁邊的 **新增AI助理** 按鈕開始。

<div style="display: flex; flex-direction: column; align-items: center;">

<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/create-a-new-agent/create-new-agent-shortcut.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/create-a-new-agent/create-new-agent-shortcut.png" alt="SeaChat | 創建新助理快捷">
</a>
    <p style="margin-top: 20px; font-size: 15px">創建新助理快捷方式</p>

</div>
</div>


<br/>

## 助理創建設置

在我們開始配置助理之前，我們首先需要選擇創建助理的方法。您可以從頭開始創建助理或選擇適合您助理用途的使用案例。

<div style="display: flex; flex-direction: column; align-items: center;">

<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">

  <a href="/images/seachat/zh/create-a-new-agent/choose-creation-method.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">

<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/create-a-new-agent/choose-creation-method.png" alt="SeaChat | 選擇助理創建方法">

</a>
    <p style="margin-top: 20px; font-size: 15px">選擇助理創建方法</p>

</div>

</div>


<br/>

### 名稱和回覆語言

為您的助理選擇一個名稱。您可以選擇一個描述助理負責的任務的名稱。例如，我有一個叫做客服助理的助理。

在**預設回覆語言**中，選擇助理將用來回答客戶的語言。在本教學中，我選擇了繁體中文。如果你希望助理能用多國語言回答，請使用「以用戶輸入的語言回答」。

### 真人客服
最後，您可以通過勾選**用戶可以在聊天期間要求與客服人員對話**來啟用[真人客服](https://wiki.seasalt.ai/zh/seachat/live-agent-transfer/)功能。

### 使用案例和描述

根據您選擇的創建助理的方法，助理的設置會略有不同。

一般來說，您選擇的使用案例將幫助助理了解它將與客戶進行的對話類型。而您的描述將幫助助理了解對話的背景。

我們將探討這兩種方法的區別：

## 自定義 AI 助理：一鍵開始

如果您希望配置您的助理以適應您現有的提示描述或全新的定義，您可能希望從頭開始創建，因為這樣可以完全控制助理的描述。對於已經有指示的用戶，這是最佳選擇。

為您的助理選擇一個使用案例，然後簡單地輸入描述該助理行為的描述。完成設置後，點擊**建立**來完成過程。

<div style="display: flex; flex-direction: column; align-items: center;">

<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">

  <a href="/images/seachat/zh/create-a-new-agent/start-from-scratch.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">

<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/create-a-new-agent/start-from-scratch.png" alt="SeaChat | 選擇從頭開始創建 AI 助理">

</a>
    <p style="margin-top: 20px; font-size: 15px">從頭開始創建 AI 助理</p>

</div>
</div>


<br/>

## 快速開始：選擇使用案例模板

使用案例可以幫助您快速設置助理並開始對話。選擇適合您助理用途的使用案例，剩下的就是進一步定義助理的描述。

<div style="display: flex; flex-direction: column; align-items: center;">

<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">

  <a href="/images/seachat/zh/create-a-new-agent/pick-a-use-case.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">

<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/create-a-new-agent/pick-a-use-case.png" alt="SeaChat | 選擇使用案例">

</a>
    <p style="margin-top: 20px; font-size: 15px">選擇使用案例</p>

</div>

</div>


<br/>

與從頭開始不同，使用案例帶有 SeaChat 為您準備的預定義指示。您可以輸入自己的描述，這些描述將稍後附加到這些指示中。通過這樣做，您可以在預定義指示的基礎上為助理提供上下文。

<div style="display: flex; flex-direction: column; align-items: center;">

<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">

  <a href="/images/seachat/zh/create-a-new-agent/choose-a-use-case.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">

<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/create-a-new-agent/choose-a-use-case.png" alt="SeaChat | 定義助理描述">

</a>
    <p style="margin-top: 20px; font-size: 15px">定義助理描述</p>

</div>

</div>


<br/>




---


#### AI助理資訊

<!-- Source: seachat-manual/02-create-agent/01-agent-information.md -->

<!-- Weight: 101 -->

*AI助理資訊是SeaChat助理的核心，包括名稱、描述和進階設置。這篇文章詳細介紹如何配置您的AI助理，以及如何使用進階功能如助上下文抽取和檢索增強生成(RAG)。*


# 簡介

**助理資訊**是您的 AI 助理的核心。它包含有關您的助理的所有必要資訊，包括其名稱、描述和其他進階設置，如上下文抽取。在本教學中，我們將帶您了解**助理資訊**下的**助理配置**中的每個參數。

---

## 基本設置

SeaChat 允許您配置您的 AI 助理的資訊，例如名稱、使用案例和描述。在**基本設置**中，用戶可以設置以下參數：

### 名稱
您的 AI 助理的名稱。此名稱將顯示在對話窗口中。

> :page_facing_up: **備註**
>
> 這將是您的助理用於管理助理的名稱。如果您希望更改助理整合中顯示的名稱，請參閱[網頁整合](/zh/seachat/seachat-manual/04-channels/08-install-to-webpage/)。

### 使用情境
您的 AI 助理的使用案例。這將幫助您對助理進行分類。SeaChat 提供了一系列可供選擇的使用案例。根據您的需求，您可以選擇最適合您的 AI 助理的使用案例。不同的使用案例可能需要不同的描述設置，但在導入使用案例時，您可以簡單地按照描述部分的說明進行操作。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/use-case-examples.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/use-case-examples.png" alt="助理使用情境">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">選擇適合的使用情境</p>
</div>

### 描述
關於您的 AI 助理的簡要描述，詳細說明您的助理的行為及其參考資料。您在描述欄位中輸入的任何內容都將顯示在頁面右側的助理指導中。然後，此描述將用於提示語言模型生成回覆。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/description-preview.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/description-preview.png" alt="AI 助理的簡要描述">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent Description</p>
</div>

### 回覆語言

透過選擇回應語言，您可以幫助設定對話的語境，並確保 AI 助理以正確的語言回應。這對於擁有多語言用戶的情況中特別實用。

透過選擇回覆語言，您可以確保 AI 助理以正確的語言進行回應。這對有多種語言的用戶的企業們，十分有用。以中文為例，繁體中文和簡體中文在許多方面都有細微差別。透過將回覆語言設定為繁體中文，AI 助理將以繁體中文的回應。

操作方式如下：

- 如果使用者有偏好的回應語言，應選擇**使用使用者的語言回應**。

- 如果使用者未指定偏好的回應語言，但希望 AI 助理以與使用者訊息相同的語言回應，則應選擇無，並勾選**始終與用選定的語言回應**。

如果使用者訊息中包含多種語言，AI 助理將以訊息中出現最頻繁或最主要的語言回應。
 
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/response-language.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/response-language.png" alt="使用使用者的語言回應選項">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent's Response Language</p>
</div>

### 真人客服
真人客服功能允許人類客服在需要時介入對話。如果啟用此功能，您的客戶將在聊天對話期間有請求真人客服的選擇。這需要您提供一名實際的人類客服來監控和回覆用戶。

您可以取消選中該框以禁用此功能，從而使您的用戶無法在對話期間請求真人客服，但是真人客服仍可以從**對話**儀表板接管對話。您可以訪問我們的[真人客服教學](https://wiki.seasalt.ai/zh/seachat/manual/create-agent/agent-information/)以獲得有關該功能的更詳細說明。

> :page_facing_up: **注意**
>
> 如果沒有真人助理在線，客戶可以留言。真人可以在工作時間查看對話摘要並回覆。


### 與 AI 助理互動
您可以立即與您剛建立的 AI 助理進行互動。在**AI助理網址**中，您可以點擊 URL 以在獨立窗口中與您的 AI 助理進行互動。

或者，如果您希望將 AI 助理集成到您的網站中，您還可以在**API 金鑰**部分訪問您的 API 金鑰。請查看[網頁機器人](https://wiki.seasalt.ai/zh/seachat/manual/channels/webpage/)以獲得有關如何將您的 AI 助理以編程方式集成到您的網站的更多信息。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/additional-options.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/additional-options.png" alt="基本設定選項">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Additional Options in Basic Settings</p>
</div>

## 聊天設計風格

### 風格設置

SeaChat允許您設計自己的網頁聊天小工具。您可以自訂聊天小工具以符合您的品牌色彩和風格。您可以從多種顏色和風格中選擇，以創建符合您品牌美學的聊天小工具。每次更改時，您都可以通過點擊**預覽**按鈕實時預覽聊天小工具在網站上的外觀。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/style-setting.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/style-setting.png" alt="顯示風格設置中額外選項的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">可自訂的網頁聊天小工具</p>
</div>

### 聊天設置

除了風格設置外，您還可以自訂聊天設置。這個功能可以減少您的AI助理編輯器在基本對話訓練上花費的時間。您可以設置聊天設置，自動設置對話流程，例如問候語、對話開始消息和對話結束消息。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/agent-information/chat-setting.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-information/chat-setting.png" alt="顯示聊天設置中額外選項的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">客制化聊天設置</p>
</div>


## 進階設置

我們建議您參閱[**進階設置**](https://wiki.seasalt.ai/zh/seachat/manual/create-agent/advanced-settings/rag/)教學，以了解 SeaChat 中提供的進階功能。對於上下文抽取和檢索增強生成（RAG）等功能，您可以在助理資訊下的進階設置部分找到它們。

---


#### 真人客服

<!-- Source: seachat-manual/02-create-agent/02-live-agent-transfer.md -->

<!-- Weight: 102 -->

*學習如何在與 SeaChat 的聊天對話中轉接至真人客服。同時探索如何、管理對話，確保順暢的客戶支援體驗。探索在不同頻道（如 WebChat 和 LINE）上轉接真人客服的步驟。*


真人客服在需要時可以接管 AI 助理的對話。真人客服不僅可以接管對話，還可以為AI助理提供新知識，並通過測試和微調AI助理的回應來幫助培訓AI助理。

SeaChat 提供許多集成配置和頻道，可能需要不同的配置才能啟用真人客服功能。 我們建議您參考 [第三方整合](https://wiki.seasalt.ai/zh/seachat/seachat-manual/05-integrations/01-seachat-google-calendar-integration/) 或 [頻道](https://wiki.seasalt.ai/zh/seachat/manual/channels/webpage/) 以了解如何正確設置您的真人助理模式。

在本教學中，我們將向您展示如何在聊天對話中轉接至真人客服，以及如何使用 SeaChat 提供的不同方法設置它。

## 助理設定

在將自定義 AI 助理集成到工作環境之前，我們需要確保您的 SeaChat 帳戶中已啟用了真人客服功能。 到側邊欄選單中的**AI助理配置**下的**AI助理資訊**。 您可以看到您的 AI 助理的所有基本設置。 如果您想重新配置您的助理，您都可以在這裡完成。

在屏幕底部，您可以看到一個勾選框，上面寫著***用戶可以在聊天期間要求與客服人員對話***。 請務必勾選此框以啟用真人客服功能。

> :exclamation: **重要提示** :exclamation:
>
> 如果您選擇啟用真人客服功能，您的客戶現在將在聊天對話期間有轉接真人客服的選項。 這需要您提供一位真人客服定期值班，該客服將檢查新對話並即時回答用戶。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-1.png" alt="在SeaChat基本設定頁面開啟真人客服">
</a>
</center>
<br/>

## 以真人客服身份與客戶交談
點開在左側選單的**對話**部分。 在這裡，您可以查看 AI 助理與客戶之間的所有對話。 您可以查看對話歷史和對話狀態，這是您的真人客服對話的控制中心。

如果客戶在聊天對話期間轉接真人客服，人類助理將看到一個指示轉接的彈出通知。 如果對話列表過長，只需點擊**真人客服**按鈕即可查看真人客服需要完成的對話列表。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-2.png" alt="真人客服查看對話">
</a>
</center>
<br/>
<br/>

就是這麼簡單。 您現在已為您的 SeaChat AI 助理設置了真人客服轉接功能。 您可以讓真人客服接管對話，以進一步協助您的客戶。 一旦真人客服完成客戶的轉接，真人客服必須點擊**完成**按鈕將對話交還給 AI 助理。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-3.png" target="_blank">
<img width="70%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-3.png" alt="與真人客服對話">
</a>
</center>
<br/>
<br/>

一旦真人客服完成對話，對話將標記為已完成，並通知客戶對話已完成。 在需要時，真人客服也可以重新啟動對話。 只需點擊**重新啟用**按鈕即可重新開始對話。

### Markdown 支援

SeaChat 對話在其網頁頻道中支援 URL 和 Markdown 格式。無論是您的真人助理還是用戶，都可以在聊天對話中插入連結和 Markdown 文字。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/live-agent-transfer/markdown-support-in-response.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/markdown-support-in-response.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">助理回應中的 Markdown 支援</p>
</div>
</div>

<br/> 

對話將以輸入時的相同格式顯示。這個功能在需要保持信息的原始格式以便於閱讀時特別有用。您可以輕鬆地將信息複製並貼上到對話中，而不會丟失格式。目前，Markdown 支援僅適用於網頁聊天整合。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/live-agent-transfer/markdown-response-in-web-ui.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/markdown-response-in-web-ui.png" alt="SeaChat | Markdown 支援">
</a>
    <p style="margin-top: 20px; font-size: 15px">WebChat UI 中的 Markdown 支援</p>
</div>
</div>

<br/> 


## 如何在 WebChat 上轉接真人客服

> :open_book: **備註** :open_book:
>
> WebChat widget 可以同時嵌入在你的自製網站或者你的**Shopify**、**Squarespace**、**Wix**網站中。可以查看[網頁機器人](https://wiki.seasalt.ai/zh/seachat/manual/channels/webpage/)和[第三方整合](https://wiki.seasalt.ai/zh/seachat/seachat-manual/05-integrations/01-seachat-google-calendar-integration/) 以獲取更多把Webchat widget嵌入到網站的相關信息。


WebChat 頻道讓您在網站上嵌入 SeaChat 對話小工具。這個頻道是企業用於提供客戶支援的最常見頻道。

聊天對話將向您的客戶顯示目前有多少真人客服可用，他們可以在聊天對話期間通過點擊***轉接真人***按鈕轉接真人客服。若沒有真人客服在線上，客戶也可以選擇留言，客服人員上班時可以查看並回覆訊息。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-web-widget-1.png" alt="若沒有真人客服在線上，客戶也可以選擇留言，客服人員上班時可以查看並回覆訊息。">
</a>
</center>
<br/>

如果您的AI助理程式部署到非網頁聊天頻道（例如 Messenger 和 WhatsApp），它們將無法顯示該按鈕。使用者可以像下面這樣口頭請求人工客服轉接：

<br/>
<a href="/images/seachat/zh/live-agent-transfer/ask-to-chat-with-live-agent-zh.jpeg" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/ask-to-chat-with-live-agent-zh.jpeg" alt="Request Live Agent | SeaChat Live Agent Transfer">
</a>
<br/>


這項功能可以單獨打開，或者和真人轉接按鈕一起使用：

<br/>
<a href="/images/seachat/zh/live-agent-transfer/settings-ask-to-chat-with-live-agent-zh.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/settings-ask-to-chat-with-live-agent-zh.png" alt="Request Live Agent | SeaChat Live Agent Transfer">
</a>
<br/>


## 如何在 LINE 上轉接真人客服

一旦您集成了 LINE 頻道並開啟真人客服服務，您的客戶將在 LINE 聊天的底部看到 **Live Agent** 按鈕。 客戶可以在聊天對話期間點擊**Live Agent**按鈕轉接真人客服。

<br/>
<center>
<a href="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-line-channel.png" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/20240325-live-agent-transfer-line-channel.png" alt="集成 LINE 頻道並開啟真人客服服務">
</a>
</center>
<br/>

## 混合模式 (AI 助理 + 真人客服)

除了僅由真人客服或僅由 AI 助理提供服務的模式，SeaChat 還提供一種混合模式，讓真人客服與 AI 助理能夠協同合作，共同提供客戶支援。

混合模式 (AI 助理 + 真人客服) 結合了真人客服和 AI 助理的優勢，大大提升了提供客戶支援的靈活性。

基於這種靈活性，以下是僅在混合模式下可用的功能選項：

### 1. 不允許客戶主動請求真人客服

若選擇此選項，**顯示摘要** 和 **自動切換至 AI 助理** 功能將隱藏或顯示為灰色，且用戶在對話期間無法請求真人客服。

<center>
<a href="/images/seachat/zh/live-agent-transfer/do-not-request.png" target="_blank" alt="不允許客戶主動請求真人客服">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/do-not-request.png" alt="不允許客戶主動請求真人客服">
</a>
</center>
<br/>


### 2. 顯示摘要
若選擇此功能，對話中的所有人都可以查看對話的摘要。

<center>
<a href="/images/seachat/zh/live-agent-transfer/remove-live-agent.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/remove-live-agent.png" alt="SeaChat | 自動切換">
</a>
</center>
<br/>

### 3. 自動切換至 AI 助理

有時候，真人客服可能需要同時處理大量對話，可能會忘記點擊 **完成** 按鈕，將對話交回給 AI 助理。為了防止這種情況發生，可以設定真人客服功能的自動超時。若對話在一段時間內無活動，系統將自動完成對話。

<center>
<a href="/images/seachat/zh/live-agent-transfer/auto-timeout.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/live-agent-transfer/auto-timeout.png" alt="Auto Transfer Back to AI Agent"">
</a>
</center>
<br/>

## :dart: 疑難排解

### 移除真人客服功能
若要停用真人客服功能，只需在 **基本設定** 的 **對話處理模式** 中取消勾選 ***不允許客戶主動請求真人客服***。這將停用真人客服功能，客戶在對話期間將無法請求真人客服，也無法看到 **真人客服** 按鈕。


> :pushpin: 注意
>
> 若有真人客服可用，他們仍然可以在 **對話** 中監控並接管對話。取消勾選此選項僅會移除客戶請求真人客服的選項。


## 需要幫忙?
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。


---


#### 助理版本控制

<!-- Source: seachat-manual/02-create-agent/03-agent-duplication.md -->

<!-- Weight: 103 -->

*了解如何在 SeaChat 中高效地複製和取代 AI 助理，以便於無縫測試和開發，並管理不同版本的助理以簡化您的生產工作流程。*


## 複製AI助理

> 📍複製AI助理時，什麼資料被複製了？
> 
> 當AI助理被複製或取代時，會涉及AI助理的基本資訊、進階設置、知識庫和網頁小工具。頻道無法被複製或替換。

當您想要創建一個與現有助理設置相似的新助理時，複製AI助理是一個非常有用的功能，允許您基於現有助理創建新的助理。

要複製助理，請在**工作區**下的**助理**中點擊您想要複製的助理旁邊的**複製此AI助理**按鈕。這將創建一個名為**{助理名稱} (COPY)**的新助理，該助理與原助理具有相同的設置。您可以點擊**編輯**來修改設置或直接進入**助理信息**。

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/create-a-new-agent/agent-duplication-btn.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
      <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/create-a-new-agent/agent-duplication-btn.png" alt="SeaChat | 複製AI助理按鈕">
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
      <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/create-a-new-agent/duplication-confirmation.png" alt="SeaChat | AI助理複製確認">
    </a>
    <p style="margin-top: 20px; font-size: 15px">複製確認</p>
  </div>
</div>

<br/>

對於與原助理連接的整合或渠道，用戶需要更新整合以包含新的助理複本，因為助理複本仍然是一個新的助理。

## AI助理取代

> 📍取代AI助理時，什麼資料被取代了？
> 
> 當AI助理被複製或取代時，會涉及AI助理的基本資訊、進階設置、知識庫和網頁小工具。頻道無法被複製或替換。


助理取代功能提供了一種有效管理不同版本助理的方式。

這在您想要開發現有助理而不影響原始版本時特別有用。通過使用此功能，助理編輯者可以對原始助理的副本進行更改，而不是直接修改原始助理。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/create-a-new-agent/replace-button.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/create-a-new-agent/replace-button.png" alt="SeaChat | 取代AI助理按鈕">
</a>

**取代助理**
</center>

一個常見的使用情境可能如下所示：

1. 複製原始的助理 A 並將副本命名為助理 B（助理 A 的副本）。
2. 向助理 B 添加新功能並進行測試。
3. 開發完成後，用助理 B 取代助理 A。
4. 現在，新助理正在生產環境中運行，具有助理 A 的原始設定和助理 B 實施的新功能。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/create-a-new-agent/replacement-workflow.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/create-a-new-agent/replacement-workflow.jpg" alt="SeaChat | 取代工作流程">
</a>

**助理取代工作流程**
</center>

通過遵循此過程，您可以在開發和測試新版本的同時，保持原始助理在生產環境中的運行。


---


#### 助理對話

<!-- Source: seachat-manual/02-create-agent/04-seachat-conversation.md -->

<!-- Weight: 104 -->

*透過 SeaChat 助理對話，輕鬆管理和回應所有進行中的對話，並有效提升互動效率。瞭解如何查看對話歷史並下載音訊記錄。*


## 對話列表

對話列表是您可以查看和管理所有助理正在處理的對話的地方。您可以查看每個對話的詳細資訊，檢查對話歷史記錄，並手動回答用戶的問題。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/seachat-conversation/conversation-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/seachat-conversation/conversation-dashboard.png" alt="SeaChat | 助理對話頁面">
</a>

**助理對話**
</center>

用戶可以在所有對話和真人助理對話之間切換。在真人助理對話中，用戶可以查看由真人助理處理的對話。

在每個對話行中，都會有一個圖標指示對話頻道，如LINE或網頁機器人。您可以通過這些圖標輕鬆識別對話的溝通渠道。

## 下載音訊對話

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/seachat-conversation/download-audio.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/seachat-conversation/download-audio.png" alt="SeaChat | 下載音訊對話">
</a>

**下載音訊對話**
</center>

對於帶有電話圖標的對話，您可以通過點擊對話內的下載圖標來下載音訊對話。音訊對話將以 `mp3` 格式下載。這是功能在品質保管理和培訓目的上非常有用，因為您可以收聽助理和用戶之間的對話，並提供回饋以改善助理的回應。


## 下載助理對話歷史記錄

如果您希望下載某些助理對話的歷史記錄，您可以前往 **工作區** -> **AI助理**。

點擊 **下載對話**，然後選擇您想下載的對話歷史記錄的年份。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/seachat-conversation/download-conversation-history.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/seachat-conversation/download-conversation-history.png" alt="SeaChat | 下載對話歷史記錄">
</a>

**下載對話歷史記錄**
</center>

根據對話歷史記錄的大小，這個過程可能需要一些時間。當下載準備好時，您會收到系統通知，內容為「AI助理對話歷史導出成功,請點擊或複製連結至瀏覽器下載,該連結有效期為 24 小時。」

點擊連結以下載以壓縮檔格式保存的對話歷史記錄。

您將會看到以 CSV 檔案格式保存的對話歷史記錄。CSV 檔案包含以下欄位：

| Sender type | Channel type | Sender name | Time in GMT | Message | Data |
|-------------|--------------|-------------|-------------|---------|------|


- **發送者類型 (Sender type)**：發送者的類型。您可以識別發送者是AI助理、系統通知、用戶等。
- **頻道類型 (Channel type)**：對話的通訊通道。您可以識別對話是來自 WebChat、WhatsApp、電話等。以下為頻道類型的列表：
  - `系統（這指的是系統訊息）`
  - `WebChat`
  - `SeaAuth（這通常用於驗證目的）`
  - `Line`
  - `WhatsApp`
  - `Messenger`
  - `Instagram`
  - `語音（這指的是電話通話）`
  - `第三方客戶端`
  - `AgentPhone（這指的是來自 SeaChat 語音助理的電話通話，通常用於驗證 token）`
  - `SeaX_Call（這指的是透過 SeaX 進行的電話通話）`
  - `SeaX_SMS（這指的是透過 SeaX 發送的 SMS）`
- **發送者名稱 (Sender name)**：發送者的名稱。如果發送者是真人用戶，您會在此欄位找到發送者的 ID 或電子郵件。否則，將會顯示系統的識別碼。
- **GMT 時間 (Time in GMT)**：訊息的 GMT 格式時間戳。
- **訊息 (Message)**：對話的訊息內容。大部分情況下，這個欄位包含純文字訊息。然而，它也可以包含特定的指令類型，例如：
  - `/live_agent: 使用者要求將對話轉接至 live agent。`
  - `/submit_form: 使用者提交表單。如果涉及實體，指令會顯示為 /submit_form{"entity_name":"entity_value"}。`
  - `/clear_history: 使用者要求 bot 忘記對話記錄並重新開始。`
  - `/ai_agent: 使用者要求將對話轉接至 AI agent。`
- **資料 (Data)**：以JSON格式呈現的對話資料內容。如果對話中沒有資料內容，這個欄位將會是空的。當資料存在時，它可能包含但不限於以下類型：
  - `在訊息中傳送的圖片 URL。`
  - `語音通話的錄音檔案 URL。`
  - `使用者在聊天過程中填寫的表單。`


---


#### 數據分析

<!-- Source: seachat-manual/02-create-agent/06-analytics.md -->

<!-- Weight: 105 -->

*監控AI智能助理和工作區的對話與訊息統計數據。*


## SeaChat 數據分析儀表板

### 概覽

SeaChat 提供兩個全面的分析儀表板，幫助您監控和優化 AI 智能助理的表現：

1. **AI 智能助理分析儀表板** - 提供個別 AI 智能助理表現的詳細洞察，包括對話、活動趨勢、標籤使用和客戶滿意度指標。

2. **工作區分析儀表板** - 提供整個工作區內所有 AI 智能助理、對話和團隊績效指標的組織級視圖。

這兩個儀表板都能讓您追蹤關鍵績效指標、衡量參與度、優化 AI 智能助理回應，並做出數據驅動的決策。導航至 `AI助理配置` 下方的 `AI助理分析` 選項卡查看特定 AI 智能助理的分析，或從工作區儀表板訪問工作區分析。

## 主要功能

📊 **追蹤效能** - 監控所有頻道的對話、獨立訪客和訊息活動

📈 **衡量趨勢** - 比較不同時間範圍的數據以識別使用模式和成長

🏷️ **標籤分析** - 分析標籤的使用和關聯性以了解對話分類

🤖 **優化回應** - 追蹤 AI 智能助理與真人客服的表現以改善自動化

⭐ **客戶滿意度** - 監控 CSAT 評分和反饋以提升服務品質

📅 **年度洞察** - 查看完整的年度績效指標和季節性模式

## 分析部分

### 1. 對話部分

追蹤不同頻道和時間段的對話量、訊息數量和用戶互動。監控 AI 智能助理與真人客服的參與度，以優化您的支援策略。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/analytics/analytics-conversation-section.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/analytics/analytics-conversation-section.png" alt="SeaChat 分析對話部分">
</a>

**對話分析儀表板**
</center>

關鍵指標包括：
- 總對話數
- 訊息量和趨勢
- 用戶參與模式
- AI 智能助理與真人客服分配
- 頻道表現比較

### 2. 活動趨勢部分

監控 AI 智能助理和真人客服在不同時間段的活動模式。追蹤訊息和通話以了解工作負荷分配並識別高峰時段。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/analytics/analytics-activity-trend-section.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/analytics/analytics-activity-trend-section.png" alt="SeaChat 分析活動趨勢">
</a>

**活動趨勢分析**
</center>

功能包括：
- **通話和訊息標籤** - 切換查看通話活動或訊息活動
- **時間單位選擇** - 選擇按日、月或年查看趨勢
- **客服比較** - 比較 AI 智能助理與真人客服的活動水平
- **高峰時段識別** - 識別繁忙時段以進行更好的資源規劃

### 3. 標籤使用概覽

了解每個標籤附加到多少對話，幫助您理解客戶互動的分類。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/analytics/analytics-label-usage-overview-section.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/analytics/analytics-label-usage-overview-section.png" alt="SeaChat 分析標籤使用概覽">
</a>

**標籤使用概覽**
</center>

此部分顯示每個標籤的總對話數


### 4. 按時期的標籤使用

通過按日、月或年的詳細分析，分析標籤使用隨時間的變化。追蹤標籤趨勢並識別對話分類的模式。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/analytics/analytics-label-usage-by-period-section.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/analytics/analytics-label-usage-by-period-section.png" alt="SeaChat 分析按時期的標籤使用">
</a>

**隨時間的標籤使用趨勢**
</center>

功能包括：
- 基於時間的標籤趨勢分析
- 標籤使用模式比較
- 識別季節性或重複問題
- 數據導出以進行更深入的分析

### 5. 標籤關係分析

分析不同標籤如何一起出現在對話中。選擇兩個標籤以發現重疊模式、共現率和關係洞察，以更好地組織標籤。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/analytics/analytics-label-relationship-section.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/analytics/analytics-label-relationship-section.png" alt="SeaChat 分析標籤關係分析">
</a>

**標籤關係分析 - 範例：新用戶和已解決標籤**
</center>

此分析幫助您：
- 了解標籤共現
- 識別相關對話主題
- 優化標籤分類
- 發現客戶互動中的隱藏模式

### 6. 客戶滿意度 (CSAT)

*注意：此部分僅在 AI 智能助理分析儀表板中可用，因為 CSAT 評分是特定於每個 AI 智能助理的。*

通過星級評分和反饋評論追蹤客戶滿意度。監控滿意率、評分分佈和最近的客戶反饋以提升服務品質。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/analytics/analytics-csat-section.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/analytics/analytics-csat-section.png" alt="SeaChat 分析 CSAT 儀表板">
</a>

**客戶滿意度分析**
</center>

CSAT 指標包括：
- 整體滿意度分數
- 評分分佈（1-5 星）
- 最近的反饋評論
- 滿意度趨勢隨時間變化
- 特定頻道的滿意率
- 含有評價的對話連結

### 7. 年度概覽

查看您的完整年度績效指標，包括總對話數、訊息數和每月趨勢，以了解您的年度增長和季節性模式。

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/analytics/analytics-yearly-overview-section.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/analytics/analytics-yearly-overview-section.png" alt="SeaChat 分析年度概覽">
</a>

**年度績效概覽**
</center>

年度洞察包括：
- 年度總對話數
- 每個對話的平均訊息數
- 月度趨勢視覺化
- 年度比較
- 季節性模式識別
- 成長指標和里程碑

### 時區配置
選擇您偏好的數據展示時區，以確保準確的基於時間的分析。


## 最佳實踐

1. **定期監控** - 每週檢查您的分析儀表板以了解趨勢
2. **標籤一致性** - 使用一致的標籤以從標籤分析中獲得有意義的洞察
3. **CSAT 跟進** - 及時回應客戶反饋以提高滿意度分數
4. **高峰時段規劃** - 使用活動趨勢在繁忙時段安排真人客服
5. **頻道優化** - 根據對話數據將資源集中在表現優秀的頻道上


---


##### 檢索增強生成 (RAG)

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/02-retrieval-augmented-generation-rag.md -->

<!-- Weight: 106 -->

*探索 SeaChat 的進階設置，包括助理記憶和檢索增強生成 (RAG)。了解如何優化您的 AI 助理的性能和即時用戶互動。*


## 簡介

檢索增強生成 (RAG) 是 SeaChat 中一個進階功能，增強了知識檢索和 AI 助理互動的準確性。通過提供您調整查詢模式、選擇檢索方法和定義知識庫檢索數量的能力，優化了 AI 助理的性能。

---

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-rag-ui" href="/images/seachat/zh/agent-advanced-settings/rag-dashboard.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/rag-dashboard.png" alt="檢索增強生成 (RAG) 在 SeaChat 中的設置圖">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">SeaChat 中的 RAG 設置</p></p>
</div>

## [檢索查詢模式](#seachat-rag-ui)

無論您需要全面的上下文、專注的互動，還是快速、精確的回應，SeaChat 靈活的查詢模式確保了優化的聊天體驗，以滿足您的偏好。

以下是客戶與停車場 FAQ AI 助理之間的示例對話，知識庫中包含數百個停車場的資料：

---

👨 (上一用戶提問)：西雅圖太空針塔附近有停車場嗎？

🤖️ (AI助理機器人回應)：是的，您可以停在位於 123rd Ave NE 的 ABC 停車場。該停車場有 50 個車位。停車費每小時 $10 起，全天最多 $60。

👨 (當前用戶提問)：我會在那附近工作，可以每月租一個停車位嗎？

---

### 前一用戶提問 &#8594; 機器人回應 &#8594; 當前用戶提問

通過結合對話的前三輪提供全面的上下文。在這種情況下，完整的對話（上一用戶提問 + 機器人回應 + 當前用戶提問）將用於查詢知識庫並生成機器人對當前用戶提問的下一個回應。

### 上一用戶提問 &#8594; 當前用戶提問

更加關注用戶的請求，不受機器人回應的影響。它包括最近兩個用戶輸入（上一用戶提問 和 當前用戶提問）來查詢知識庫並生成機器人對下一個回應。

### 當前用戶提問

只考慮用戶的最新提問，即當前用戶提問，用於生成機器人的下一個回應。這對於一次性對話或用戶頻繁切換主題的情況非常理想。然而，在多輪對話中討論相同主題時，它可能會忽略重要的上下文。

## [檢索方法](#seachat-rag-ui)

您可以通過選擇不同的知識庫檢索方法來優化知識庫檢索：

### Keyword Search (關鍵字檢索)

根據用戶提供的關鍵字來匹配知識庫，以提供相關結果。當您有唯一標識符如產品名稱、地點、ID 等時，這種方法效果很好，但在用戶沒有說出精確的關鍵字時（例如使用同義詞或不同語言）可能會錯過。

### Vector Search (向量檢索)

利用文本嵌入的能力來增強相關資料的檢索。向量檢索可以跨語言工作，即使沒有匹配的關鍵字也能檢索到相似的文檔。然而，對於稀有標識符如產品名稱、地點或 ID 可能會有困難。

### Hybrid Search (混合檢索)

結合關鍵字檢索和向量檢索方法，優化資料檢索。

## [知識庫擷取計數](#seachat-rag-ui)

此欄位允許您指定要檢索的知識庫文件(片段)數量，以確保有效的資料檢索。理想的數量是很彈性的，取決於令牌限制和文檔類型。

### 知識庫擷取計數的考慮因素

- **參考知識庫文件(文件片段)太少**

您可能會錯過關鍵資料，導致 GPT 的回應不完整或不準確。

- **參考知識庫文件(文件片段)太多**

重要資料可能會被不相關的細節淹沒，使 GPT 更難提供準確的回應。

- **上下文限制**

每次請求的上下文是有限制的。如果檢索到的文檔超過此限制，SeaChat 將使用在限制內能夠適應的文檔。

通過調整知識庫檢索數量，您可以優化資料深度和資源使用之間的平衡，確保準確且高效的回應。

## 知識庫搜索優化

SeaChat 現在提供一個名為知識庫搜索優化的進階功能，讓您能夠進一步提升檢索資訊的質量。此功能使 AI 能夠在生成回應前對初步搜索結果進行二次分析。

### 配置知識庫搜索優化

您可以在AI Agent 資訊的進階設定頁面中啟用此功能：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement" href="/images/seachat/zh/agent-advanced-settings/kb-refinement.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/kb-refinement.png" alt="SeaChat 中的知識庫搜索優化功能圖">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">SeaChat 中的知識庫搜索優化設置</p></p>
</div>

### 可選的知識庫優化指令

對於大多數用例來說，只需啟用此功能而無需任何附加說明就足夠了。系統將使用預設的優化策略自動優化搜尋結果。自訂指令是可選的，但可以顯著提高特定場景的效能。

為了更精確地控制 LLM 如何優化搜索結果，您可以在文本欄位中提供自定義指令。這些指令指導 AI：

- 如何評估文檔相關性
- 優先處理哪些類型的資訊
- 如何處理模糊查詢
- 針對您特定知識領域的特殊考慮

#### 指令示例

以下是一些有效的優化指令示例：

- "當用戶詢問產品規格時，優先考慮包含特定產品代碼的文檔。"
- "對於停車相關查詢，專注於包含與用戶提及區域匹配的位置資訊的文檔。"
- "處理技術支援問題時，優先考慮最新文檔而非舊版本。"
- "對於多部分問題，確保包含能夠解答查詢所有部分的文檔。"
- "總結對話歷史記錄時，如果可以從討論中推斷出分支名稱，請包括分支名稱，確保它反映用戶在上次查詢中想要的分支，即使沒有明確提及。"
- "在識別相關文章時，排除那些與摘要中提到的分支不同的分支相關的文章，前提是摘要指定了分支名稱。"

### 知識庫搜索優化的好處

啟用此功能可以顯著提升您的 AI 助理性能：

- 提供更準確和相關的回應
- 減少複雜知識庫中的資訊過載
- 更有效地處理模糊查詢
- 提升對用戶問題的上下文理解
- 提供更簡潔和專注的答案

通過微調您的知識庫搜索優化設置，您可以創建一個更智能、更靈敏的 AI 助理，更好地理解和解決用戶的特定需求。

### 📌 範例 1：透過知識庫搜尋優化功能處理多分店資訊
想像你經營一間擁有五家分店的餐廳。在你的知識庫中，你使用試算表記錄了每家分店的菜單、服務細節、營業時間與優惠資訊。當使用者詢問特定分店的問題時，你會希望 AI 智能助理能回應出正確、對應該分店的資訊。

要提升 AI 助理對使用者問題的理解與回應品質，有兩個有效的方法可以強化知識庫的處理方式：

**1. 在知識庫內容中標示分店名稱**

在你的 Excel 試算表中，為每一列或每一格的內容加上該資訊所屬的分店名稱。

<div style="display: flex; flex-direction: column; align-items: center;"> <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center"> <a id="seachat-kb-refinement" href="/images/seachat/zh/agent-advanced-settings/kb-refinement-example.png" target="_blank"> <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/kb-refinement-example.png" alt="An example spreadsheet contains five restaurant branches"> </a> </div> <p style="margin-top: 20px; font-size: 15px">範例試算表：包含分店標籤的多分店知識庫</p> </div>
這樣可以幫助 AI 助理在閱讀知識庫內容時正確理解該資訊屬於哪一家分店，進一步提升回應的準確性與相關性。

**2. 上傳試算表**

透過 **上傳試算表** 卡片將此試算表上傳到您的知識庫。選擇此選項將表格中的每一行上傳為單獨的知識庫文件。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement" href="/images/seachat/zh/agent-advanced-settings/kb-refinement-upload2.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/kb-refinement-upload2.png" alt="Upload each row as an individual kb article">
    </a>
</div>
</div>
<br/>

**3. 使用知識庫搜尋優化功能過濾不相關資料**

啟用知識庫搜尋優化功能，並加入自訂的優化指令，例如：`從使用者的問題中擷取分店名稱。排除與該分店無關的文章或資料列。`

有了這些指令，即使初步的知識庫搜尋結果涵蓋了多家分店，AI 助理也能自動篩選出與使用者查詢分店相關的內容，提供更精準、聚焦且有幫助的回應。

這樣的作法特別適用於：
- 內容交錯重疊的大型知識庫
- 擁有多個據點的企業或品牌
- 回答分店資訊需具高度準確性的場景

透過良好的知識庫結構（標示分店名稱）與搜尋優化邏輯結合，你可以打造一個更聰明、更貼近需求的 AI 助理。


### 📌 範例 2：使用知識庫搜尋優化管理產品資訊

假設您管理一個擁有數千種產品的電子商務平台。您的知識庫包含了多個試算表，記錄著詳細的產品資訊，包括規格、價格、庫存狀態和客戶回饋。當客戶詢問特定產品時，您希望 AI 助理能提供準確的產品專屬資訊。

**1. 在知識庫條目中加入產品名稱**

在試算表的每個儲存格中，加入產品名稱以清楚識別資訊：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement-product" href="/images/seachat/zh/agent-advanced-settings/kb-refinement-product.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/kb-refinement-product.png" alt="一個包含產品資訊的試算表範例">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">範例試算表：附有產品專屬標籤的產品知識庫</p></p>
</div>

這種結構化的試算表確保當 AI 助理處理知識庫時，能準確地將資訊與特定產品關聯起來。

**2. 上傳試算表**

透過 **上傳試算表** 卡片將此試算表上傳到您的知識庫。選擇此選項將表格中的每一行上傳為單獨的知識庫文件。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement" href="/images/seachat/zh/agent-advanced-settings/kb-refinement-upload2.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/agent-advanced-settings/kb-refinement-upload2.png" alt="Upload each row as an individual kb article">
    </a>
</div>
</div>
<br/>

**3. 設定知識庫搜尋優化指令**

啟用知識庫搜尋優化功能，並加入以下具體指令：

```
從用戶的查詢中提取產品名稱。
優先考慮完全匹配的結果，其次才考慮產品變體或相關型號。
除非用戶特別要求比較功能，否則排除其他產品的資訊。
```

透過這些指令，您的 AI 助理可以：
- 識別正在討論的特定產品
- 專注於相關的產品細節
- 僅在適當時機包含相關產品資訊
- 在多次查詢中保持對同一產品的上下文理解

這種方法特別適用於：
- 擁有大量相似商品的產品目錄
- 需要精確產品資訊的技術支援場景
- 產品比較和推薦查詢
- 處理客戶對產品規格和可用性的詢問

透過實施這種結構，您的 AI 助理能夠有效地瀏覽大量產品資訊，並為客戶查詢提供準確且具有上下文關聯的回應。


---


##### 上下文抽取

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/03-context-extraction.md -->

<!-- Weight: 107 -->

*SeaChat 上下文抽取可以用來資格審查和追蹤客戶資料。「上下文抽取」允許你定義對話中最重要的部分，並儲存標註在客戶檔案，提供之後查詢和再利用。*

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

<iframe width="100%" height="400" src="https://www.youtube.com/embed/Msgg3U3lW4M?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>
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


---


##### 時間意識與上下文

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/04-time-awareness-context.md -->

<!-- Weight: 108 -->

*了解 SeaChat AI 的時間意識與上下文功能，提升助理在時間敏感回應中的控制能力。*


---

## 簡介

除了 [檢索增強生成 (RAG)](https://wiki.seasalt.ai/zh/seachat/manual/create-agent/advanced-settings/rag/) 功能和 [上下文抽取](https://wiki.seasalt.ai/zh/seachat/manual/create-agent/advanced-settings/context-extraction/)，SeaChat AI 還提供了多種進階設定選項，讓用戶可以進一步控制助理們行為。

雖然這些功能不如 RAG 和上下文抽取那麼複雜，但在某些情況下，它們提供相當的價值。本文將簡單介紹這些功能。

---

## 時間意識

<br/>

<center>
<a href="/images/seachat/zh/time-awareness-context/time-awareness-ui.png">
<img height="100%" width="100%" src="/images/seachat/zh/time-awareness-context/time-awareness-ui.png"  alt="時間意識功能介面">
</a>

</center>

<br/>

時間感知功能讓 AI 助理能夠理解特定時區的當前時間。這對於向客戶提供與時間相關的資訊非常有幫助。

<br/>

<center>
<a href="/images/seachat/zh/time-awareness-context/time-awareness-kb.png">
<img height="100%" width="100%" src="/images/seachat/zh/time-awareness-context/time-awareness-kb.png"  alt="時間意識使用實例的知識提示">
</a>

</center>

<br/>

例如，如果企業用戶在營業時間和非營業時間有兩個不同的客戶服務電話號碼（分別是 02-37284471 和 02-37222231），時間感知的 AI 助理可以根據當前時間提供相應的號碼。

如果客戶在營業時間聯絡 AI 助理，助理可以提供第一個號碼（02-37284471）。如果在非營業時間聯絡，助理則會提供第二個號碼（02-37222231）。這項功能為 AI 助理的回應增添了個性化的層次。
<br/>

<center>
<a href="/images/seachat/zh/time-awareness-context/time-awareness-example.png">
<img height="100%" width="100%" src="/images/seachat/zh/time-awareness-context/time-awareness-example.png"  alt="時間意識使用實例">
</a>

</center>

<br/>

## 上下文

上下文功能允許用戶設置 AI 助理在生成回應時應參考的最大對話輪數。當您希望提供具有上下文感知的回應，但又不想引用整個對話歷史時，這個功能非常有用。

通過限制對話輪數，用戶可以減少回應延遲，並避免 AI 助理被過多的信息所淹沒。


---


##### 在聊天中啟用引用

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/05-kb-references.md -->

<!-- Weight: 109 -->

*Seasalt.ai 提供的 SeaChat 知識庫引用功能為使用者提供了一種便捷且高效的方式，讓聊天回應可以連結回其使用的相關文件。啟用此功能後，每個聊天回應都會包含引用部分，列出來源文件，使使用者能夠清楚了解哪些資訊被用來生成回應內容。*


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


---


##### AI 助理回應排程

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/06-ai-agent-response-schedule.md -->

<!-- Weight: 110 -->

*為 AI 助理設定回應客戶的時間排程 — 非常適合處理非工作時間、假期或任何自訂時間範圍內的詢問。*


## 概述

SeaChat 的 AI 助理回應排程功能讓您可以設定 AI 助理主動回應客戶詢問的特定時間範圍。這項強大功能非常適合需要在非工作時間、假期、週末或任何自訂時間範圍內處理客戶互動的企業，同時保持對自動化回應發送時機的控制。

在排程回應時間之外，對話將遵循您配置的對話處理模式和真人客服轉接設定，確保客戶服務的無縫連續性。

## 如何配置 AI 助理回應排程

要設定 AI 助理回應排程，請按照以下步驟操作：

### 步驟 1：進入進階設定

在您的 SeaChat 儀表板中導航至 **助理資訊 → 進階設定** 標籤。

### 步驟 2：配置排程

<center>
<a href="/images/seachat/zh/agent-advanced-settings/ai-agent-schedule-1.png">
<img height="100%" width="100%" src="/images/seachat/zh/agent-advanced-settings/ai-agent-schedule-1.png" alt="AI 助理回應排程配置">
</a>
<br/>
</center>

1. **啟用開關**：切換 AI 助理回應排程功能以啟動它。

2. **選擇時區**：為您的業務營運選擇適當的時區。這確保排程按照您的當地時間運作。

3. **新增時間和日期設定**：配置您希望 AI 助理活躍的特定時間範圍和日期。您可以在一週內設定多個時間區塊，以適應不同的業務需求。

4. **選擇 AI 助理行為**：選擇 AI 助理在排程時間內應如何表現：
   - **正常回應**：使用標準的 SeaChat AI 助理功能
   - **回覆固定訊息**：向客戶發送預設的訊息

<center>
<a href="/images/seachat/zh/agent-advanced-settings/ai-agent-schedule-2.png">
<img height="100%" width="100%" src="/images/seachat/zh/agent-advanced-settings/ai-agent-schedule-2.png" alt="AI 助理回應排程選項">
</a>
<br/>
</center>

## 使用案例

AI 助理回應排程功能在以下情況下特別有價值：

### **24/7 客戶支援**
- **非工作時間覆蓋**：確保客戶在夜間和週末人工客服不在線時能立即獲得回應
- **假期支援**：在您的團隊休假時維持客戶服務
- **全球時區支援**：無需全天候人力配置即可服務不同時區的國際客戶

### **營業時間管理**
- **午休時間覆蓋**：在員工午休或會議期間保持客戶服務活躍
- **高峰時段管理**：在高流量期間使用 AI 助理減少等待時間
- **緊急時段**：在正常營業時間外為緊急詢問提供基本支援

### **季節性業務營運**
- **季節性企業**：在淡季期間維持客戶參與度
- **活動支援**：在特殊活動、促銷或宣傳期間提供自動化回應
- **維護窗口**：在系統維護或更新期間，讓客戶隨時了解最新資訊

### **成本效益營運**
- **小企業支援**：無需聘請額外員工即可提供延長時間的專業客戶服務
- **新創公司效率**：在建立團隊的同時維持 24/7 客戶參與
- **資源優化**：在改善客戶滿意度的同時降低營運成本

### **多通道支援**
- **網站整合**：在指定時間內為您的網站提供一致支援
- **社交媒體管理**：在繁忙期間自動化社交平台的初始回應
- **電子郵件跟進**：在指定時間範圍內處理電子郵件詢問

### **特殊應用場景**
- **醫療健康服務**：在非診療時間提供基本健康諮詢和預約排程
- **教育機構**：為學生提供課外時間的學習支援和常見問題解答
- **電子商務**：在促銷活動期間提供即時的產品資訊和購買協助
- **金融服務**：在交易時間外提供基本的帳戶查詢和服務資訊
- **旅遊業**：為不同時區的客戶提供 24/7 的行程諮詢和緊急支援

透過實施 AI 助理回應排程，企業可以確保一致的客戶服務交付，同時優化資源配置並維持所有客戶接觸點的專業標準。此功能有助於創建自動化和人工支援的無縫融合，適應您特定的業務需求和客戶期望。


---


#### 如何加入知識

<!-- Source: seachat-manual/03-add-knowledge/01-add-knowledge-intro.md -->

<!-- Weight: 200 -->

*Seasalt.ai Seachat 提供了一份詳細的教學指南，深入探討如何將知識添加到您的知識庫中。這份指南將引導您完成每個步驟，並提供實用小技巧。*


## 簡介
這份教學指南將會深入的探討，如何添加知識到你的知識庫。我們將會引導你完成每一個步驟，並且在過程中強調一些小技巧。

## 開始之前
開始加入知識前，請先註冊SeaChat。如果您已經是SeaChat用戶，你現在手邊應該已經有一個準備好接收新知識的 SeaChat 助理。如果你還沒有建立助理，我們建議你參考我們詳細的教學指南 [如何創建AI助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/)。

<br/>


<iframe width="100%" height="400" src="https://www.youtube.com/embed/uaUlFVjDe98?list=PL8K7_LTqly449uOg_uBWOPfFyL1fJRjkE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

---


#### 上傳試算表

<!-- Source: seachat-manual/03-add-knowledge/02-spreadsheet-upload.md -->

<!-- Weight: 201 -->

*上傳試算表檔案和表格到您的SeaChat AI機器人。詳細的教學,教您如何調教SeaChat AI助理根據上傳的文件內容回答客戶問題。*

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



 

---


#### 上傳影片/音頻檔案

<!-- Source: seachat-manual/03-add-knowledge/03-multimedia-upload.md -->

<!-- Weight: 202 -->

*學習如何將影片和音頻文件直接上傳到您的SeaChat知識庫。本全面指南將詳細介紹如何有效地轉錄和上傳多媒體內容到您的AI助理，包括所有必要的檔案格式和長度要求。*


> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。


## 簡介
加入多媒體檔到SeaChat助理的知識庫中，不再需要將影片和音檔轉錄成文本，SeaChat替您省去了將語音轉錄成文字的步驟。現在，你可直接上傳多媒體檔案到知識庫中！

SeaChat 提供許多不同的方式讓您上傳文件到您助理。在本教學中，我們將專注於**轉錄音訊/影訊**的方法，在本教學結束時，您的 SeaChat 助理將擁有一個客製的知識庫為您服務。

## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/) 找到創建AI助理的步驟。

## 開啟知識庫
在側邊欄中，選擇**AI助理配置**下的**知識庫**。選擇**轉錄音訊/影訊**，您就可以上傳音訊或影訊檔案到您的AI助理知識庫。
<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/03-multimedia/20240319-multimedia-tutorial-step2.png" alt="知識庫面板">

*知識庫面板*
</center>

## 上傳檔案
點擊「檔案上傳」的區塊，您就可以從多種文件格式[^1]中選擇想要提交給AI助理的文件。送出後，知識庫會處理送出的文件並更新。
[^1]: SeaChat 支援 .wav, .flac, .aac, .opus, .mp3, .mp4, .ogg, .m4a 等檔案.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/03-multimedia/20240319-multimedia-tutorial-step3.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/03-multimedia/20240319-multimedia-tutorial-step3.png" alt="檔案上傳">
</a>

*檔案上傳*
</center>

> :rotating_light: **提醒** :rotating_light:
>
> 上傳文件前，請檢查文件是否符合以下要求:
> - 媒體內容必須是英文或中文。
> - 文件的時長不得超過15分鐘。
> - (多人影片/音頻的限制)當音頻/視頻文件上傳後，SeaChat 將把它們進行語音轉文字處理，轉換為文本格式。目前，SeaChat 在影片/音頻轉錄中沒有發言者識別功能。如果您需要在您的轉錄中進行發言者識別，請用別的服務轉錄成文字後，再將文本直接上傳到知識庫。

## 檢查語言

選擇欲上傳的多媒體檔案。目前SeaChat支援英文和繁體中文。一旦您確認了所有上傳的文件，您可以點擊**提交**按鈕進行上傳。

請注意，選擇語言後，我們將把您上傳的音頻/視頻文件轉錄成相應的語言。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/03-multimedia/20240319-multimedia-tutorial-step4.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/03-multimedia/20240319-multimedia-tutorial-step4.png" alt="Interface of SeaChat showing the bulk upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded and a preview section for the spreadsheet data, reminding users to verify file format and content before submission.">
</a>

*文件語言*
</center>

## 已添加到知識庫

您已成功上傳新知識。要查看已上傳的檔案，您可以至頁面右上角的「**現有知識**」區塊，在那裡您可以在「**上傳檔案**」裡找到剛剛上傳的資料。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/03-multimedia/20240319-multimedia-tutorial-step5.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/03-multimedia/20240319-multimedia-tutorial-step5.jpg" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Submit' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*在 **現有知識** 中查找文件*
</center>

## 檢查知識庫

點擊您剛剛上傳的檔案並檢視內容。大功告成！您已成功地將影片/音頻轉成文字後上傳到您的SeaChat助理中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/03-multimedia/20240319-multimedia-tutorial-step6.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/03-multimedia/20240319-multimedia-tutorial-step6.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Next' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*審核上傳的音訊/影訊*
</center>

## :brain: 運作原理

使用這個功能時請注意以下幾點:

1. SeaChat不對視頻文件的內容做任何處理. 它單純從視頻中提取音軌，並將音頻轉錄為文本，這些文本可以拿在知識庫中使用。
2. 對於每個轉錄的音頻和視頻，您可以在現有知識庫中檢查轉錄品質。
3. 如果您有其他語言的多媒體文件，請先將它們轉錄為文本，然後上傳到SeaChat而達到相同的目的。
4. 對於音頻/視頻文件，SeaChat會預設文件中只有一位發言者。也就是說，SeaChat不進行話者分離或話者識別。如果您有一個包含對話的音頻文件（例如，一個兩人的廣播），您應該首先將其轉錄並在每句發言者的開頭加上發言者的名字。

## 為什麼你需要上傳音頻/視頻？

許多SeaChat客戶會通過以往的客戶服務對話建立他們的知識庫。其中有許多來自WhatsApp和Facebook Messenger對話的音頻文件，通常是包含一個發言者且少於1分鐘的音頻檔案。多媒體上傳功能是這一需求的自然延伸。

如果您有以往的客戶對話的音頻或視頻文件格式，請試試將其上傳到知識庫。您的AI代理可以從過去的客戶服務對話中學習，以生成高質量的回應。

## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seasalt.ai](mailto:seachat@seasalt.ai).


---


#### 上傳模板文件

<!-- Source: seachat-manual/03-add-knowledge/04-template-file-upload.md -->

<!-- Weight: 203 -->

*探索如何使用CSV和JSON格式的模板文件來快速且有效地上傳數據到您的SeaChat知識庫。學習如何定制您的AI助理的知識庫，以提高對客戶查詢的響應速度和質量。*

> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。


## 簡介
SeaChat 提供許多不同的方式讓您上傳文件到您助理的知識庫中。在本教學中，我們將專注於 **上傳試算表** 方法，到教學結束時，您的 SeaChat 助理程式將具有一個定制的知識庫，為您提供服務。

## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/) 找到創建AI助理的步驟。

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
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/before-submission.png" alt="檢查已上傳文件">
</a>

*檢查已上傳文件*
</center>


## 已新增到知識庫
您已成功上傳新知識。要查看已上傳的檔案，您可以至頁面右上角的「**現有知識**」區塊，在那裡您可以在「**上傳檔案**」裡找到剛剛上傳的資料。
<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/existing-files.png" alt="上傳檔案">
</a>

*到「**現有知識**」中的「**上傳檔案**」*
</center>

## 檢查知識庫
點擊您剛剛上傳的檔案並檢視內容。大功告成！您已成功地將一份模板文件上傳到您的SeaChat助理中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。

<div style="display: flex; justify-content: space-between; align-items: center;">
  <div style="display: flex; flex-direction: column; text-align: center;">
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/csv-uploaded.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/csv-uploaded.png" alt="CSV 檔案範例">
</a>
    <em>CSV 檔案</em>
  </div>

  <div style="display: flex; flex-direction: column; text-align: center;">
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/json-uploaded.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/04-template-upload/json-uploaded.png" alt="JSON 檔案範例">
</a>
    <em>JSON 檔案</em>
  </div>
</div>


## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。


---


#### 上傳文件

<!-- Source: seachat-manual/03-add-knowledge/05-document-upload.md -->

<!-- Weight: 204 -->

*探索如何在SeaChat上將超過20種文件格式，如DOCX、MP3、PNG等，有效地上傳至您AI助理的知識庫，以及如何利用這些文件提升AI助理的回答能力。*

> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。


## 簡介
SeaChat 提供許多不同的方式讓您上傳文件到您助理的知識庫中。在本教學中，我們將專注於 **上傳文件** 方法，到教學結束時，您的 SeaChat 助理程式將具有一個客制的知識庫，為您提供服務。

## 創建 SeaChat 助理程式
如果您尚未擁有 SeaChat 帳戶，您可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！您可以在 [創建助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/) 中找到創建基於知識的 AI 助理程式所需的所有信息。

## 打開知識庫
通過側邊欄選單中的 **AI助理配置** 下的 **知識庫** 面板找到您助理程式的知識庫。選擇 **上傳文件**，準備好 20 多種類型的文件即可上傳到您的助理程式。

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/05-document-upload/choose-document-upload.png" alt="透過側邊欄選單中的助理配置進入知識庫面板以顯示如何通過選擇從模板文件上傳來上傳 CSV 或 JSON 文件到助理程式。">

*知識庫面板*
</center>

## 文件類型
SeaChat 可以讓您上傳超過 20 種[^1]的文件類型。在本教學中，我們將向您展示如何上傳 DOCX 文件到您助理的知識庫中。


> :rotating_light: **注意** :rotating_light:
>
> 針對圖片文件，例如 png，我們僅支持英文文件。至於音頻文件，我們建議您使用 [音頻/視頻上傳](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/multimedia-upload/)。

[^1]: SeaChat 支援 .doc、.docx、.eml、.epub、.gif、.jpg、.json、.html、.mp3、.msg、.odt、
.ogg、.pdf、.png、.pptx、.ps、.rtf、.tiff、.txt、.wav、.zip 等文件。

## 送出文件前
SeaChat允許用戶批量上傳。您可以在拖放區域下方的部分查看每個上傳檔案的狀態。點擊**送出**後，知識庫會處理送出的文件並更新。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/05-document-upload/file-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/05-document-upload/file-upload.png" alt="SeaChat 界面顯示上傳功能，其中包含一個拖放區域以及下方的部分，用於監視正在上傳的每個文件的狀態，提醒用戶在送出之前驗證文件格式和內容。一個成功的消息表示上傳成功">
</a>

*文件上傳成功*
</center>


## 送出到現有知識庫
文件成功上傳後，您將看到一個成功的消息。您已成功的為您的 AI 助理程式，增加了新的知識。要查看已上傳的文件，您可以到頁面右上角的 **現有知識** ，在那裡您可以在 **上傳檔案** 中找到新的上傳數據。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/05-document-upload/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/05-document-upload/existing-files.png" alt="視覺指南突出顯示位於屏幕右上角的 '現有' 部分，其中突出顯示了 '文件' 部分中的上傳文件。">
</a>

*在 **現有知識** 中查找文件*
</center>

## 檢查知識庫
點擊您剛剛上傳的檔案並檢視內容。大功告成！您已成功地將一份DOCX文件上傳到您的SeaChat助理中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/05-document-upload/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/05-document-upload/review-upload.png" alt="在下拉視圖中審核上傳的信息">
</a>

*審核上傳的 DOCX 文件*
</center>


## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。



---


#### 匯入網址

<!-- Source: seachat-manual/03-add-knowledge/06-import-urls.md -->

<!-- Weight: 205 -->

*探索如何在SeaChat平台上將網址直接匯入至您的AI助理知識庫。無論是專業文章、博客或其他信息豐富的網站導入內容，本指南都將幫助您快速上手。*

> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。


## 簡介
SeaChat 提供多種方法將文件上傳到您AI助理的知識庫。在本教程中，我們將專注於 **匯入網址** 方法。讓我們以一篇部落格文章作為例子，向您展示如何將網址匯入到您的助理。

## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/) 找到創建AI助理的步驟。

## 打開知識庫
通過側邊欄選單中的 **AI助理配置** 下的 **知識庫** 面板找到您的助理的知識庫。選擇 **匯入網址**，並準備好要上傳到您的助理的網址。

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/06-import-urls/choose-import-urls.png" alt="通過側邊欄選單中的助理配置進入知識庫面板以顯示如何通過匯入網址進行上傳。">

*知識庫面板*
</center>

## 輸入網址
SeaChat 支持將網址匯入到您的助理。將網址複製並粘貼到相應的輸入框中。一旦您確定輸入的網址，點擊 **新增** 以確認。

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/06-import-urls/enter-urls.png" alt="知識庫界面的圖像，我們引導用戶插入他們希望從中匯入文本的網頁的 url。">

*輸入要從網頁匯入文本的網頁的網址*
</center>

現在，您應該注意到用戶界面右側的額外選項，**我想從此頁面上連結的頁面導入文本**，該選項允許您從匯入文本中的連結上導入該文本。您需要提供要抓取的頁面並輸入網站頁面的網址。

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/06-import-urls/enter-urls-2.png" alt="知識庫界面的圖像，我們引導用戶插入他們希望從連結在此頁面上的頁面中匯入文本的頁面的 url。">

*輸入從此頁面上連結的頁面導入文本的網址*
</center>


新增了網址後，您可以單擊 **送出** 按鈕將內容上傳到您的助理的知識庫。 SeaChat 將開始從您提供的網址匯入文本。


## 送出到現有知識庫
文件成功上傳後，您將看到一個成功的消息。您已成功的為您的 AI 助理，增加了新的知識。要查看已上傳的文件，您可以到頁面右上角的 **現有知識** ，在那裡您可以在 **網頁** 中找到新的上傳數據。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/06-import-urls/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/06-import-urls/existing-files.png" alt="視覺指南突出顯示位於屏幕右上角的 '現有' 部分，其中突出顯示了 '文件' 部分中的上傳文件。">
</a>

*在 **現有知識** 中查找文件*
</center>

## 檢查知識庫
單擊您剛上傳的文件以查看內容。您網站上的文本現在已經被加入到您的知識庫中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/06-import-urls/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/06-import-urls/review-upload.png" alt="在下拉視圖中審核上傳的信息">
</a>

*審核上傳的網站文本*
</center>


## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。


---


#### 匯入站點地圖

<!-- Source: seachat-manual/03-add-knowledge/07-import-sitemap.md -->

<!-- Weight: 206 -->

*探索如何利用SeaChat將站點地圖直接匯入到您AI助理的知識庫中。本教學詳細介紹了將站點地圖內容完整匯入助理的全部步驟，以及如何提取XML文件中的所有網址。*

> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。


## 簡介
SeaChat 提供許多不同的方式讓您上傳文件到您助理的知識庫中。在本教學中，我們將專注於 **匯入站點地圖** 方法。讓我們以站點地圖向您展示如何將網址匯入到您的助理的知識庫。

## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/) 找到創建AI助理的步驟。

## 打開知識庫
通過側邊欄選單中的 **AI助理配置** 下的 **知識庫** 面板找到您的助理的知識庫。選擇 **匯入站點地圖**，並準備好要上傳到您的助理的 XML 文件。

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/choose-import-sitemaps.png" alt="通過側邊欄選單中的助理進入知識庫面板以顯示如何通過匯入網址進行上傳。">

*知識庫面板*
</center>

## 輸入站點地圖
通過匯入站點地圖，您可以跳過逐一添加網址的過程。您的站點地圖，通常是 XML 文件，將包含您匯入的網站中的所有連結。

將網址複製並粘貼到相應的輸入框中。一旦您確定包含的網址，點擊 **新增** 以確認。

> :rotating_light: **注意** :rotating_light:
>
> 請注意，並非所有網站都有站點地圖。取得定位網站的 XML 站點地圖的最常見（且簡單）方法之一是手動檢查。您需要做的是在瀏覽器中輸入您的網站 URL，然後在 URL 的末尾添加 `sitemap.xml`，例如 www.YourWebsiteUrl.com/sitemap.xml。如果出現站點地圖（看起來像 XML 文件），則該網站具有站點地圖。有更多定位您的站點地圖的方法，請參閱 [此文章](https://seocrawl.com/en/how-to-find-a-sitemap/) 以了解更多信息。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/enter-url.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/enter-url.png" alt="">
</a>

*插入站點地圖的 URL*
</center>

## 提交之前
一旦您添加了站點地圖，SeaChat 將自動解析 XML 文件並提取網址。您可以在提交到您的助理的知識庫之前檢查這些網址。


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/before-submission.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/before-submission.png" alt="SeaChat 的介面顯示了用於監控正在上傳的每個文件狀態的上傳部分，提醒用戶在提交之前驗證文件格式和內容。">
</a>

*檢查已上傳的文件*
</center>

## 送出到現有知識庫
文件成功上傳後，您將看到一個成功的消息。您已成功的為您的 AI 助理，增加了新的知識。要查看已上傳的文件，您可以到頁面右上角的 **現有知識** ，在那裡您可以在 **網站地圖** 中找到新的上傳數據。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/existing-files.png" alt="視覺指南突出顯示位於屏幕右上角的 '現有' 部分，其中突出顯示了 '網站地圖' 部分中的上傳文件。">
</a>

*在 **現有知識** 中查找文件*
</center>

## 檢查知識庫
單擊您剛上傳的文件以查看內容。您站點地圖上的文本現在已經被加入到您的知識庫中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/07-import-sitemaps/review-upload.png" alt="視覺指南突出顯示位於屏幕右上角的 '現有' 部分，其中突出顯示了 '網站地圖' 部分中的上傳文件。">
</a>

*審核上傳的站點地圖*
</center>


## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。


---


#### 手動輸入

<!-- Source: seachat-manual/03-add-knowledge/08-manual-upload.md -->

<!-- Weight: 206 -->

*探索如何直接手動輸入數據到您的SeaChat AI助理知識庫中。學習如何設置文件標題、內文，並利用額外的設置如按鈕導向和回應後附加訊息來增強互動性。*

> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。


## 簡介
SeaChat 提供許多不同的方式讓您上傳文件到您助理的知識庫中。在本教學中，我們將專注於 **手動輸入** 方法，向您展示如何手動輸入數據到您的AI助理。

## 創建 SeaChat 助理

如果你還沒有 Seachat 帳號，你可以在 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！並在 [創建助理](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/) 找到創建AI助理的步驟。

## 打開知識庫
通過側邊欄選單中的 **AI助理配置** 下的 **知識庫** 面板找到您的AI助理的知識庫。在 **手動輸入** 下選擇 **編寫新的知識庫文件**，並開始輸入要上傳到您的AI助理的數據。


<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/08-manual-entry/choose-manual-entry.png" alt="通過側邊欄選單中的助理配置進入知識庫面板以顯示如何通過導入網址進行上傳。">

*知識庫面板*
</center>

## 什麼時候應該使用手動輸入？
當您有一些片段的、或不存在文件內的重要信息想要包含到知識庫中，您可以選擇手動輸入。這可以是一個簡短的產品描述，或者是一個常見問題。手動輸入是一種可快速迭代、快速拓展 AI 助理的好方法。

## 輸入數據
本篇教學，我們不會詳細介紹所有的欄位，如果您想了解更多信息，可以查看我們進階教學的部分。現在，讓我們介紹各個欄位，將數據新增到我們的知識庫中。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/08-manual-entry/empty-manual-entry.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/08-manual-entry/empty-manual-entry.png" alt="視覺指南突出了屏幕右上角的“現有”部分，展示了“文件”部分中上傳文件的內容。">
</a>

*填寫 **手動輸入** 中的輸入格*
</center>

### 文件標題和文件內文
為您的文件選擇一個標題，在文件內文區域中編寫文件的文本描述。此文件標題，將顯示在您的知識庫中作為知識項目的標題。您可以在文件內文輸入格中輸入詳細的內容。文件標題和文件內文將在知識提取時，提供 AI 助理使用。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/08-manual-entry/title-text.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/08-manual-entry/title-text.png" alt="視覺指南突出了屏幕右上角的“現有”部分，展示了“文件”部分中上傳文件的內容。">
</a>

*文件標題和內文*
</center>

### (非必要) 其他設置

您還可以設置文件為提醒，並為用戶提供 URL。

- **按鈕**：您可以添加按鈕，將用戶重導向到特定 URL。在相輸入格中輸入引用的URL以及顯示的標題。
- **AI聊天助理回應後的附加訊息**：在 **提醒** 中，輸入您想在助理使用此文件作出回應時向最終用戶顯示的額外信息。
- **文件權重**：使用文件權重來控制文件的重要性。權重越高，文件越重要，因此助理越有可能使用此文件來回應用戶。

完成後，點擊 **送出** 按鈕將內容上傳到您的助理的知識庫中。SeaChat 將導入您提供的信息。


## 送出到現有知識庫
文件成功上傳後，您將看到一個成功的消息。您已成功的為您的 AI 助理程式，增加了新的知識。要查看已上傳的文件，您可以到頁面右上角的 **現有知識** ，在那裡您可以在 **手動輸入** 中找到新上傳的知識資料。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/08-manual-entry/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/08-manual-entry/existing-files.png" alt="視覺指南突出顯示位於屏幕右上角的 '現有' 部分，其中突出顯示了 '文件' 部分中的上傳文件。">
</a>

*在 **現有知識** 中查找文件*
</center>

## 檢查知識庫
點擊您剛剛上傳的檔案並檢視內容。大功告成！您已成功地將一份手動輸入資料上傳到您的SeaChat助理中。您現在可以使用知識庫來測試您的助理。SeaChat還有更多設置能用來客制您的知識庫，我們將在教學的下一部分繼續探索這些進階功能。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/tutorial-add-knowledge/08-manual-entry/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/tutorial-add-knowledge/08-manual-entry/review-upload.png" alt="在下拉視圖中審核上傳的信息">
</a>

*審核上傳的手動輸入內容*
</center>


## 需要幫忙
需要幫忙？歡迎聯絡我們 [seachat@seaslt.ai](mailto:seachat@seaslt.ai)。




---


#### 新增URL按鈕到知識庫回應

<!-- Source: seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers.md -->

<!-- Weight: 207 -->

*學習如何在 SeaChat AI 助理的回應中新增參考 URL，為用戶提供更詳細的信息。通過新增 URL，您的 AI 助理將能夠提供更全面的客戶支援。*


> 🧭 **檔案大小規則**
>
> 您的每個上傳文件的檔案大小限制會根據您的訂閱計畫而有所不同。如果超過檔案上傳限制，您將收到錯誤訊息。請在再次上傳前減小檔案大小。請參考[檔案大小規則](https://wiki.seasalt.ai/zh/seachat/file-size-rule/)了解更多資訊。

# 簡介

您可以在 AI 助理的回應中包含相關的參考 URL，讓用戶可以訪問更詳細的內容。在 **現有知識** 頁面中，您可以找到相關知識並將參考 URL 新增到 AI 助理的回應中。此功能通過在用戶尋找特定信息時提供額外的信息和資源來增強用戶體驗。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/new-kb-ui.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/new-kb-ui.png" alt="展示如何撰寫助理描述的圖像">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">知識附加設置</p>
</div>

## [知識庫中的其他設置](#additional-setting-ui)

在**AI助理配置**下找到**知識庫**並點擊開啟已上傳的知識，找到**編輯**按鈕，並新增URL按鈕到該知識上。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/choose-knowledge.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/choose-knowledge.png" alt="選擇要新增URL按鈕的知識項目">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">選擇要新增URL按鈕的知識項目</p>
</div>

## [按鈕](#additional-setting-ui)

SeaChat 提供了不同的方法來向助理的回應中添加額外信息。選擇「按鈕」選項，將 URL 按鈕添加到助理的回應中。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/choose-button.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/choose-button.png" alt="選擇按鈕類型以新增URL按鈕">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">選擇按鈕類型以新增URL按鈕</p>
</div>

## 新增 URL 按鈕到知識庫回應

知識庫是我們的助理將尋找信息以回應用戶查詢的地方。一個非常強大的用例將是 FAQ 助理，助理可以提供對常見問題的回答。在這種情況下，您可以將 URL 新增到助理的回答中，為用戶提供更詳細的信息。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/url-to-answer.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/url-to-answer.png" alt="URL 已新增到助理的答案中">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">URL 已新增到助理的答案中</p>
</div>

### 按鈕訊息的限制

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/kb-id-problem.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/kb-id-problem.png" alt="因字元限制所造成的訊息中斷">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">因字元限制所造成的訊息中斷</p>
</div>
<br/>

以下是我們按鈕模板和回傳按鈕的目前的限制摘要：

- 訊息字元限制：200 字元
- 回傳按鈕內容字元限制：所有按鈕共 300 字元
- 回傳按鈕數量限制：最多 4 個按鈕

### KB ID

KB ID 是每個知識庫項目中的知識的唯一識別碼。您可以通過點擊該知識項目下的 **更多** 按鈕中的 **複製 KB ID** 按鈕，將知識項目的 ID 複製到剪貼板。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/kb-id.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/kb-id.png" alt="使用 KB ID 完整消息">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">使用 KB ID 完整消息</p>
</div>

> 🚨注意 🚨
>
> 出於安全考量，AI 助理無法訪問來自其他 AI 助理知識庫中的 KB ID。KB ID 是該指定 AI 助理知識庫中的知識的唯一識別碼，無論它們是否位於同一工作區。

## 從試算表中新增URL按鈕到助理的回應

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/url-button/spreadsheet-example.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/url-button/spreadsheet-example.png" alt="試算表範例">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">試算表範例</p>
</div>


---


#### 檔案大小規則

<!-- Source: seachat-manual/03-add-knowledge/file-size-rule.md -->

<!-- Weight: 208 -->

*本文詳細說明了根據不同訂閱方案所適用的文件大小和詞元數量限制，幫助用戶了解各方案的具體規則。根據不同的訂閱方案，文件大小和詞元數量皆有不同的限制規則。*


根據您的訂閱方案，您可以上傳一定大小的檔案。如果超過檔案大小限制，您將收到錯誤訊息。

要了解不同方案的具體功能，請參考[定價方案](https://wiki.seasalt.ai/zh/seachat/seachat-payments/pricing-plans/)。

各方案的檔案大小規則如下：

- **免費** - 知識庫最多包含 10 份文件（最大 200KB）和 20 萬個詞元
- **標準** - 知識庫最多包含 100 份文件（最大 1 MB）和 100 萬個詞元
- **高級** - 知識庫最多包含 500 份文件（最大 10 MB）和 500 萬個詞元


### 如何檢查您的詞元數量

當文件上傳到知識庫後，該文件將被標記並從您的帳戶中扣除相應的詞元數量。您可以在側邊欄選單中導航到 **知識庫** 儀表板來檢查已使用的詞元數量。每個上傳到知識庫的文件都會顯示已使用的詞元數量。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/pricing-plans/check-tokens.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/pricing-plans/check-tokens.png" alt="">
</a>

**如何檢查詞元**
</center>

> 一個估算試算表詞元數量的法則：
>
> 對於 4.0 模型，每個試算表的列是 8K 詞元，而對於 3.5 模型，每列是 2K 詞元。

---


##### 知識庫中的額外功能

<!-- Source: seachat-manual/03-add-knowledge/10-addtional-feature/01-additional-features-in-kb.md -->

<!-- Weight: 210 -->

*了解如何在 SeaChat 知識庫中添加按鈕、圖片、視頻等額外功能，優化 AI 助理回應，並同步最新知識以提供精準支持。*


## 簡介

除了快速回應之外，SeaChat 提供更進階的功能來增強您的 AI 助理的回應。這些功能包括在回應中新增按鈕、圖片和視頻。本指南將引導您如何將這些功能添加到 AI 助理的回應中，確保您的用戶獲得最全面的支持。以下所有參數適用於您上傳到知識庫的每一條知識。

## 知識庫中的額外功能

首先，導航到知識庫儀表板並選擇要添加額外功能的現有知識。在左側邊欄的 **AI助理配置** 下找到 **知識庫**，然後點擊 **現有知識** 以查看已上傳到您的 AI 助理的所有知識。

打開您希望添加額外功能的知識，然後點擊 **編輯** 按鈕。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/kb-dashboard.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/kb-dashboard.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">前往 <strong>Existing</strong></p>
</div>

## 編輯知識中的額外功能

當您的 AI 助理需要回答問題時，它會在知識庫中搜索最相關的信息。AI 助理會查看 **文件標題** 以尋找相關性。SeaChat 利用這種行為，允許您向個別知識添加額外功能，因此每次助理從該特定知識中檢索信息時，都會記住在回應中包含這些額外功能。這允許 SeaChat 用戶向其客戶提供更詳細的信息。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/additional-settings.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/additional-settings.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">其他設置</p>
</div>

### 卡片消息

在向客戶提供信息時，提供信息來源或補充閱讀以便他們更好地了解是很有用的。SeaChat 允許您向回應中添加卡片和按鈕，以向用戶提供更全面的回應。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/card-info.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/card-info.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">知識設置</p>
</div>

卡片消息提供了您所提供信息的強大視覺效果。您可以為卡片消息添加標題、副標題和圖片。當您想要提供所提供信息的預覽時，此功能特別有用。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/card-msg.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/card-msg.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">上傳圖片到卡片消息</p>
</div>

### 按鈕消息

與卡片相比，按鈕更為簡單明了。您可以為按鈕消息添加標題和 URL。此功能特別有用，當您想提供信息來源的鏈接時，您可以向回應中添加任意多個按鈕。與卡片消息相比，此功能為您的用戶提供了更簡單的導航。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/btn-msg.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/btn-msg.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">知識設置</p>
</div>

### 文檔權重

文檔權重是一個參數，允許您優先考慮特定的知識。權重越高，當 AI 助理搜索相關信息時，知識越有可能被檢索到。當您有多個與相同問題相關的知識時，這個功能特別有用，您希望優先檢索最重要的知識。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/doc-weight.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/doc-weight.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">知識設置</p>
</div>

## 同步 URL 知識

如果知識是通過 URL 或站點地圖導入的，您可以將知識與來源 URL 進行同步。當知識頻繁更新時，這個功能特別有用，並且可以確保您知識庫中的知識始終是最新的。

此功能可以讓用戶在知識庫管理方面有更好的體驗。只要該 URL 仍存在，用戶就不需要重新將知識上傳到知識庫。

您現在只需點擊要與來源 URL 同步的知識旁邊的 **同步** 按鈕，SeaChat 會自動使用來源 URL 的最新信息更新該知識。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/sync-button.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/knowledge-advanced-features/knowledge-additional-features/sync-button.png" alt="同步知識按鈕">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">同步知識</p>
</div>

---


#### WhatsApp

<!-- Source: seachat-manual/04-channels/04-seachat-whatsapp-integration.md -->

<!-- Weight: 300 -->

*利用Seasalt.ai的SeaChat平台解鎖WhatsApp自動化功能。透過整合ChatGPT驅動的聊天AI，輕鬆管理對話，並通過真人助理連接提升客戶支持。*


## 🎥影片教學
<iframe width="100%" height="400" src="https://www.youtube.com/embed/qpNlWtGP9jw?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

## 簡介
在本節中，我們將深入探討如何在**WhatsApp**上設置一個**ChatGPT**驅動的聊天機器人或聊天助理。完成本節後，您將清楚了解如何：
1. **自動回應用戶訊息**:
- 將您的**WhatsApp**企業帳戶連接到**SeaChat**助理平台。
- 使用**ChatGPT**的先進語言模型訓練AI助理，生成自然語言回應以應對各種用戶查詢。
- 配置聊天助理，根據您的知識庫自動回應來訊消息。
2. **通過SeaChat訪問所有與用戶的對話**:
- 使用**SeaChat**這個用戶友好的界面，訪問和監控用戶與您的AI助理之間的所有對話。
- 查看聊天記錄，分析用戶行為，識別聊天助理回應中的改進空間。
- 高效管理和組織對話，確保與用戶的無縫通信。
3. **允許用戶請求真人助理協助**:
- 實施特殊指令，讓用戶在遇到複雜查詢或需要個性化支持時請求真人助理的幫助。
- 將對話從AI聊天助理無縫轉移到真人助理，確保順利且高效的過渡。
- 賦予用戶選擇所需支持級別的權利，提升整體客戶體驗。

在開始設置過程之前，請記住以下幾點關鍵：

**WhatsApp Business App限制**:
- 一旦您將**SeaChat**與**WhatsApp**集成，您將無法再使用常規的**WhatsApp Business App**。
- **SeaChat AI**助理僅設計用於回應來訊消息，無法自行發起對話。
- 不過，作為助理創建者，一旦請求真人助理，您仍然可以與用戶對話。

**誰能從此集成中受益**:
- 擁有大量來訊**WhatsApp**消息並需要自動化的企業和組織。
- 希望提供個性化和引人入勝的客戶支持體驗的公司。
- 希望通過自動化常規查詢來減輕真人助理負擔的客戶服務部門。
---

## WhatsApp 設定
在有正確指引的情況下，設定**WhatsApp**可以是一個簡單的過程。以下是步驟的簡短版本。你也可以點擊標題來查看每個步驟的詳細說明：

1. **[建立 WhatsApp 應用](#create-a-whatsapp-app)**:
- 前往**Meta Developer Site**。
- 點擊右上角的**My Apps**。
- 從下拉選單中選擇**Create App**。

2. **[選擇應用類型](#choose-app-type)**:
- 在**App Type**下選擇**Other**。
- 輸入一個獨特的應用名稱，避免使用**WhatsApp**在名稱中。

3. **[添加 WhatsApp 產品](#add-whatsapp-product)**:
- 向下滾動到應用列表底部。
- 找到**WhatsApp**並選擇它來添加產品到你的應用。

4. **[連接到企業](#connect-to-business)**:
- 將**WhatsApp**應用與你的企業關聯。
- 這一步是利用**WhatsApp Business Platform API**所必需的。

5. **[配置 WhatsApp 應用](#configure-whatsapp-application)**:
- 仔細檢查配置頁面上的信息。
- 按照說明提供必要的詳細信息，如企業名稱、地址和聯繫信息。
- 確保所有必填字段都正確填寫。

6. **[生成訪問token](#lets-set-up-a-permanent-token)**:
- 完成配置後，生成一個永久訪問token。
- 此token對使用**WhatsApp Business API**至關重要。

7. **[測試和發布](#test-your-seachat-agent-via-whatsapp)**:
- 測試你的**WhatsApp**應用以確保其按預期工作。
- 根據測試結果進行必要的調整。
- 一旦對性能滿意，公開發布你的應用。

8. **[移除訊息整合](#remove-your-whatsapp-integration)**:
- 正確移除你的**Meta**應用中的頁面訪問
- 點擊**SeaChat**內的移除按鈕

> :books: **推薦閱讀**:
>
> 記得遵守[**WhatsApp Business API**](https://developers.facebook.com/docs/whatsapp/)的政策和指南，以保持合規並避免潛在問題。

以下將逐步引導你完成過程的詳細說明：

### 建立 WhatsApp 應用

首先，您需要前往 [Meta Developer Site](https://developers.facebook.com/) 並點擊右上角的 **My Apps**，然後從下拉選單中選擇 **Create App**，來建立一個新的 WhatsApp 應用。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/channels/whatsapp/create-new-whatsapp-app.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/create-new-whatsapp-app.png" alt="SeaChat | WhatsApp | 創建新的 WhatsApp">
    </a>
    <p style="margin-top: 20px; font-size: 15px">創建新的 WhatsApp</p>
</div>
</div>

### 選擇應用類型
建立一個 **Other** 應用，因為我們只使用這個應用來訪問您的 WhatsApp 帳戶。在 **Select app type page** 頁面上，選擇 **Business** 類型，然後點擊 **Next**。

<br/>
<div style="display: flex; flex-direction: column; align-items: center;">
    <div style="width: 100%; height:100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/choose-app-type-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/choose-app-type-1.png" alt="SeaChat | WhatsApp | 創建Other App">
        </a>
        <p style="margin-top: 20px; font-size: 15px">創建 <strong>Other</strong> app</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/choose-app-type-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/choose-app-type-2.png" alt="SeaChat | WhatsApp | 填寫 App Details">
        </a>
        <p style="margin-top: 20px; font-size: 15px">填寫 App Details</p>
    </div>
</div>

<br/>

這裡我們創建了一個名為 **Seasalt.ai WA** 的應用，請注意 Meta 不允許應用名稱中包含 **WhatsApp**。



### 新增 WhatsApp 產品

建立應用後，讓我們新增 WhatsApp 產品。在 **Add products to your app** 區域下找到 WhatsApp 框，然後點擊 **Set up** 來建立您的應用。

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/zh/channels/whatsapp/whatsApp-integration.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/whatsApp-integration.svg" alt="SeaChat | WhatsApp | 新增 WhatsApp 到您的 App">
    </a>
    <p style=" font-size: 15px">新增 WhatsApp 到您的 App</p>
</div>
</div>

### 連接到企業帳戶
WhatsApp 應用需要與您的企業相關聯，因為它需要使用 [WhatsApp Business Platform API](https://developers.facebook.com/docs/whatsapp/)。選擇一個企業投資組合並點擊繼續。回到您的應用儀表板，您應該會看到已添加的 WhatsApp 產品。點擊 **Start using the API** 開始配置。

<br/>
<div style="display: flex; flex-direction: column; align-items: flex-start;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/connect-to-business-1.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/connect-to-business-1.png" alt="SeaChat | WhatsApp | 選擇 Business Portfolio">
        </a>
        <p style="margin-top: 20px; font-size: 15px">選擇 Business Portfolio</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/connect-to-business-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/connect-to-business-2.png" alt="SeaChat | WhatsApp | 點擊Start Using the API">
        </a>
        <p style="margin-top: 20px; font-size: 15px">點擊 <strong>Start Using the API</strong></p>
    </div>
</div>


## 如何配置 WhatsApp 應用程式
> :rotating_light: **警告** :rotating_light:
>
> 這部分會比較複雜。如果您不夠小心並且漏掉某個步驟，可能無法成功配置您的 WhatsApp 應用程式。所以，讓我們一起仔細地進行以下說明。

如果您從上方點擊 **Start using the API**，它會將您帶到如下的 **API Setup**。但是，我們不需要過多關注這裡的信息。真正重要的是 **Step 3: Configure webhooks**。

<br/>
<div style="display: flex; flex-direction: column; align-items: center; justify-content: space-between">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-1.png" alt="SeaChat | WhatsApp | API 設置">
        </a>
        <p style="margin-top: 20px; font-size: 15px">API 設置</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-2.svg" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-2.svg" alt="SeaChat | WhatsApp | 配置 Webhooks">
        </a>
        <p style="font-size: 15px"><strong>配置 Webhooks</strong></p>
    </div>
</div>

這會將您帶到左側的 **Configuration** 下的 **WhatsApp**。從這裡，我們首先需要配置由 SeaChat 提供的 Webhook 和 token。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-3.svg" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-3.svg" alt="SeaChat | WhatsApp | 配置儀表板">
    </a>
    <p style=" font-size: 15px">配置儀表板</p>
</div>
</div>

<br/>

對於 Webhook 的配置，我們會參考上圖中的 **Step 1**。這是您需要做的所有事情。前往 SeaChat，導航到 **Agent Configuration → Channels → WhatsApp** 來獲取 **Callback URL** 和 **Verify token**。

複製 SeaChat 的 Step 1 並將其貼上到 WhatsApp 儀表板上的相應部分，如下圖所示。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-4.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/configure-whatsApp-application-4.svg" alt="SeaChat | WhatsApp | 複製 SeaChat 內容並貼上至 Webhook 配置">
</a>
    <p style="margin-top: 20px; font-size: 15px">複製 SeaChat 內容並貼上至 Webhook 配置</p>
</div>
</div>

<br/>

> :point_down: **不要忘記使用設定的 Webhook 欄位！** :point_down:
>
> 我們需要給 API 訊息許可權，這樣 SeaChat 助理才能接收來自 WhatsApp 的任何傳入訊息。
>
>
> <div style="display: flex; flex-direction: column; align-items: center;">
> <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
>   <a href="/images/seachat/zh/channels/whatsapp/dont-forget-to-use-set-Webhook-fields.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank"><img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/dont-forget-to-use-set-Webhook-fields.svg" alt="SeaChat | WhatsApp | Webhook 欄位"></a>
>     <p style="margin-top: 10px; font-size: 15px">Webhook 欄位</p>
> </div>
> </div>
>



### 設置一個永久 token

[Step 2](#perma-token-webhook) 是獲取一個 **WhatsApp Access Token** 並將其傳遞給 SeaChat。

您可能在 API 設置中見過臨時訪問 token：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
 <a href="/images/seachat/zh/channels/whatsapp/permanent-token-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/permanent-token-1.png" alt="SeaChat | WhatsApp | 臨時訪問 token">
</a>
    <p style="margin-top: 20px; font-size: 15px">Temporary Access Token</p>
</div>
</div>

<br/> 

<p>:point_up: 如 Meta 所述，此 token 僅有效 24 小時。所以我們不使用它。</p>

<br/> 



### 1. 創建系統用戶

您應該通過生成一個 [System User Access Token](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) 來獲取永久 token。

以下是創建系統用戶的步驟：

1. 登錄 [Meta Business Suite](https://business.facebook.com/)。
2. 在左上角下拉選單中找到您的業務帳戶並點擊其 **Settings**（齒輪）圖標。
3. 點擊 **Business settings**。
4. 導航到 **Users** → **System users**
5. 點擊 **Add** 按鈕，創建一個 admin 或 employee 系統用戶。


### 2. 生成系統用戶訪問 token

創建系統用戶後，生成系統用戶訪問 token：

1. 登錄 [Meta Business Suite](https://business.facebook.com/)。
2. 在左上角下拉選單中找到您的業務帳戶並點擊其 **Settings**（齒輪）圖標。
3. 點擊 **Business settings**。
4. 導航到 **User** → **System** 用戶。
5. 從系統用戶列表中選擇適當的系統用戶。
6. ~~點擊生成新 token 按鈕~~。→ **暫不要這樣做**。請參閱下文 [Assign Assets](#assign-assets)。
7. 選擇將使用 token 的應用。
8. 選擇應用正常運行所需的任何許可權並生成 token。

##### Assign Assets
我們在第 6 步停止，因為您需要先將您的 WhatsApp 應用指定為 **Asset** 以獲取正確的 token 範圍。請按照以下步驟將您的 WhatsApp 應用指定為 Asset：

1. 在 System Users 中，點擊 [**Assign Asset**](#assign-assets-step-1)。
2. 然後轉到 **Apps** 並選擇您創建的應用，並賦予其 [**Full control**](#assign-assets-step-2)。
3. 點擊 **Generate new token** 並選擇 ***whatsapp_business_messaging*** 和 ***whatsapp_business_management*** 在 **Permissions**。應如下圖所示 [this](#assign-assets-step-3)。
4. token 生成後，將彈出一個 [pop-up](#assign-assets-step-4) 顯示生成的 token 信息。複製 token。
5. 現在點擊 token，將打開 [**Access Token Debugger**](#assign-assets-step-5) 並顯示正確的 Scope。這裡您需要確保擁有 ***whatsapp_business_messaging*** 和 ***whatsapp_business_management***。
6. 複製並粘貼 token 到 [SeaChat](#assign-assets-step-6)。
7. 將您的 [**App Mode**](#assign-assets-step-7) 設置為 **Live**。
8. 通過返回 [**WhatsApp** →  **Configuration**](#assign-assets-step-8) 並將您的 WhatsApp 號碼添加到 WhatsApp 應用中。它應顯示至少一個生產號碼。

<div style="display: flex; flex-direction: column; width:100%  ; align-items: center;">
    <div id="assign-assets-step-1" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-1.svg" target="_blank" style=" width: 100%; height: 10%; display: flex; justify-content: center; align-items: center; overflow: hidden; padding: 0">
            <img style="max-width: 100%; max-height: 50%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-1.svg" alt="SeaChat | WhatsApp | 點擊Assign Asset">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 1: 點擊 <strong>Assign Asset</strong></p>
    </div>
    <div id="assign-assets-step-2" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-2.svg" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-2.svg" alt="SeaChat | WhatsApp | 選擇Full control">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 2: 選擇 <strong>Full control</strong></p>
    </div>
</div>
<div id="assign-assets-step-3" style="display: flex; flex-direction: column; width:100%; align-items: center;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-3.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-3.png" alt="SeaChat | WhatsApp | Generate token及設置Permission">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 3: <strong>Generate token</strong> 及設置 <strong>Permission</strong></p>
    </div>
    <div id="assign-assets-step-4" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-4.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-4.png" alt="SeaChat | WhatsApp | 複製 token">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 4: 複製 token</p>
    </div>
</div>
<div style="display: flex; flex-direction: column; width:100% ; align-items: center;">
    <div id="assign-assets-step-5" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-5.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-5.png" alt="SeaChat | WhatsApp | 開啟Access Token Debugger">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 5: 開啟 <strong>Access Token Debugger</strong></p>
    </div>
    <div id="assign-assets-step-6" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-6.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-6.png" alt="SeaChat | WhatsApp | 將 token 貼上至 SeaChat">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 6: 將 token 貼上至 SeaChat</p>
    </div>
</div>
<div style="display: flex; flex-direction: column; width:100% ; align-items: center;">
    <div id="assign-assets-step-7" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-7.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-7.png" alt="SeaChat | WhatsApp | 將App Mode設定成Live>
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 7: 將 <strong>App Mode</strong> 設定成 <strong>Live</strong></p>
    </div>
    <div id="assign-assets-step-8" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/channels/whatsapp/assign-asset-8.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/assign-asset-8.png" alt="SeaChat | WhatsApp | 新增企業號碼">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 8: 新增企業號碼</p>
    </div>
</div>


## 測試您的 SeaChat 助理通過 WhatsApp

終於設置完成了！一旦您的助理設置好後，試著發送幾條消息並期待 SeaChat 的回覆：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/test-whatsapp-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/test-whatsapp-1.png" alt="SeaChat | WhatsApp | WhatsApp 對話">
</a>
    <p style="margin-top: 20px; font-size: 15px">WhatsApp 對話</p>
</div>
</div>

<br/> 

在 SeaChat 的 **Conversations** 視圖中，您可以看到相同的對話以及用戶/發送者的名字。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/test-whatsapp-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/test-whatsapp-2.png" alt="SeaChat | WhatsApp | SeaChat 對話">
</a>
    <p style="margin-top: 20px; font-size: 15px">SeaChat 對話</p>
</div>
</div>

### 正確設置您的 WhatsApp 商業帳戶

上述截圖顯示了一個非常基本的 WhatsApp 帳戶，甚至沒有個人資料圖片。在競爭激烈的數字環境中，擁有強大的在線形象對各種規模的企業都至關重要。WhatsApp 擁有龐大的用戶群和廣泛的知名度，為企業提供了一個強大的平台來與客戶聯繫。然而，有效地設置和管理 WhatsApp 商業帳戶可能是一項艱巨的任務。

管理 WhatsApp 商業帳戶的一個重要方面是正確設置個人資料。一個優化良好的個人資料能夠創造專業形象，建立信任，並提高可見度。不幸的是，許多企業忽視了個人資料設置的重要性，或難以找到正確的設置。

讓我們通過訪問 [Meta WhatsApp Business Manager](https://business.facebook.com/wa/manage) 來正確設置 WhatsApp 帳戶個人資料。或者，如果您仍在 Meta for Developers 網站，導航到 **WhatsApp → Quickstart → WhatsApp Business** 並點擊 **Account information**：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/deploy-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/deploy-1.png" alt="SeaChat | WhatsApp | Account information">
</a>
    <p style="margin-top: 20px; font-size: 15px">Account information</p>
</div>
</div>

<br/> 

這將帶您進入 **WhatsApp Business Manager** 下的正確帳戶。在這裡，您可以進行必要的更改，上傳個人資料圖片，並保存更新。這些更改可能需要幾分鐘才能生效。一旦生效，當您訪問 WhatsApp 商業帳戶的信息頁面時，您會注意到更新的個人資料信息。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/deploy-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/deploy-2.png" alt="SeaChat | WhatsApp | 編輯帳戶">
</a>
    <p style="margin-top: 20px; font-size: 15px">編輯帳戶</p>
</div>
</div>

<br/> 

幾分鐘後，如果您在手機上的 WhatsApp 應用中點擊您的 WhatsApp 商業帳戶的信息頁面，它將反映出這些更改：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/zh/channels/whatsapp/deploy-3.png" target="_blank">
<img width="50%" height="auto" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/deploy-3.png" alt="SeaChat | WhatsApp | WhatsApp Business Account Info">
</a>
    <p style="margin-top: 20px; font-size: 15px">WhatsApp Business Account Info</p>
</div>
</div>

<br/> 


優化您的 WhatsApp 商業個人資料不僅僅是添加個人資料圖片。以下是一些增強個人資料的額外提示：

2. **使用清晰專業的個人資料圖片**：
選擇能代表您的品牌或業務的高質量圖片。避免模糊或低解析度的圖片，因為它們會給人負面印象。

3. **添加相關聯絡信息**：
確保您的電話號碼、電子郵件地址和網站（如適用）在個人資料中顯眼顯示。這讓客戶可以通過他們喜歡的渠道輕鬆聯繫您。

4. **使用標籤和標記**：
使用標籤和標記來組織您的聯絡人和對話。這有助於您有效地分類和管理客戶互動，使您更容易跟踪和回應特定查詢或請求。

通過遵循這些提示，您可以正確地優化您的 WhatsApp 商業帳戶，創建專業的個人資料，並增強整體的客戶參與度。

# 與真人助理互動
您是否注意到在上面的圖片中我使用 /live_agent 來請求真人助理？如果助理通過設置他們的在線狀態在線：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/live-agent-status.png" alt="SeaChat | WhatsApp | 真人助理狀態">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理狀態
</p>
</div>
</div>

<br/> 

他們可以直接與用戶對話！

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/live-agent-interaction.png" alt="SeaChat | WhatsApp | Live agent 互動">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent 互動
</p>
</div>
</div>

<br/> 

如果助理不在線，他們可以打開電子郵件通知，在用戶啟動聊天或請求真人助理時接收實時電子郵件：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/ai-agent-preference.png" alt="SeaChat | WhatsApp | 真人助理偏好設定">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理偏好設定
</p>
</div>
</div>

<br/>

## WhatsApp 的訊息回傳 (Postback)
當你設定好 Messenger 的整合後，你就可以使用 SeaChat 的[按鈕功能](http://localhost:1313/zh/seachat/manual/add-knowledge/webpage-link/)來與客戶互動。這允許你在答案中以按鈕的形式加入網址或其他附加資訊。

現在，客戶可以點擊按鈕來獲取更多資訊或導航到網頁。

每次按鈕被點擊時，會觸發 SeaChat API 與 WhatsApp API 的訊息回傳。

### WhatsApp 按鈕限制
WhatsApp 對於訊息回傳有一些限制。請在創建按鈕時注意以下事項，以避免任何問題。

限制條件如下：

- WhatsApp 的訊息 API 支援每條訊息最多**3個互動按鈕**。
- 每個按鈕的文字（標題）限制為**20個字元**。
- 按鈕被點擊時傳送的回傳資料或回傳訊息限制為**200個字元**。
- 這些限制適用於每個按鈕，並非所有按鈕的總和。
- [開發者文件](https://developers.facebook.com/docs/whatsapp/guides/interactive-messages/)

[//]: # (用戶可以使用 SeaChat 的 **[KB ID]&#40;https://wiki.seasalt.ai/zh/seachat/seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers/#kb-id&#41;** 功能，來改善這些限制所帶來的不便，請參閱連結以獲取更多資訊。)


## 移除您的 WhatsApp 整合

如果您想移除 WhatsApp 整合，您需要在兩個地方進行操作：

1. 從您的 Meta 應用程式中正確移除 webhook
2. 點擊 SeaChat 內的移除按鈕

對於步驟 1，請前往您的 [Meta Business app](https://developers.facebook.com/) → WhatsApp → Configuration → Callback URL → Edit → Remove webhook

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/whatsapp/remove-app-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/whatsapp/remove-app-1.png" alt="SeaChat | WhatsApp | 移除整合">
</a>
    <p style="margin-top: 20px; font-size: 15px">移除整合</p>
</div>
</div>

<br/>

## :dart: 疑難排解

如果您沒有收到來自 SeaChat Agent 在 WhatsApp 上的回應，您應該檢查用戶容易忽略的以下設置：
- 您是否使用了僅有效 24 小時的 **temporary access token**？應該使用系統用戶的 [**Permanent Access Token**](#1-creating-system-users)。
- 您的 WhatsApp 應用程式是否已設置為 [**Live mode**](#assign-assets)？確保它沒有在開發模式下運行。
- 您是否配置了 [**webhook fields**](#perma-token-webhook) 以允許 **message permission**？如果此權限未正確授予，SeaChat 將無法接收來自 WhatsApp 的消息。
- 您的 SeaChat agent 是否收到消息，但您無法在 WhatsApp 上看到回覆？這可能是因為在生成永久token時，您沒有先進行 [**Assign Assets**](#assign-assets)。

## 支援
需要幫助？請聯繫我們 [seachat@seasalt.ai](mailto:seachat@seasalt.ai)。


 


---


#### LINE官方帳號

<!-- Source: seachat-manual/04-channels/05-install-to-line.md -->

<!-- Weight: 301 -->

*將SeaChat無縫整合到您的LINE官方帳號。這份詳盡的指南將引導您完成SeaChat的安裝過程，並展示如何與LINE的自動回應功能協同工作，以優化客戶互動。*


## 將SeaChat串接到你的LINE官方帳號

請按照影片教學，安裝SeaChat到你的LINE官方帳號，開始回覆客戶訊息！

<iframe width="100%" height="400" src="https://www.youtube.com/embed/OZsxazjy5-c?list=PL8K7_LTqly449uOg_uBWOPfFyL1fJRjkE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>


## 同時使用SeaChat和LINE的自動回應訊息功能

您可以將SeaChat定義為提供專業資訊的AI助理，能理解各式各樣的問題並根據知識庫回答的問題，而LINE則主要用於觸發關鍵字相關的活動，以及發送媒體訊息，如優惠券、卡片訊息和視頻。透過結合這兩者的功能，您可以有效地提升用戶體驗，並加強與客戶的互動。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line/line-自動回應-vs-seachat-智能助理.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat-channels/line/line-自動回應-vs-seachat-智能助理.png" alt="SeaChat | Line | LINE自動回應 vs. SeaChat智能助理">
</a>

*LINE自動回應 vs. SeaChat智能助理*
</center>
<br/>

### 設定步驟

1. 將LINE回應設定選擇手動聊天+自動回應

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line/將line回應設定選擇手動聊天加自動回應.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat-channels/line/將line回應設定選擇手動聊天加自動回應.png" alt="SeaChat | Line | 將LINE回應設定選擇手動聊天加自動回應">
</a>

*將LINE回應設定選擇手動聊天加自動回應*
</center>
<br/>

2. 為避免LINE一直回應重複訊息，請將LINE的自動回應改為關鍵字回應，到[LINE Bussiness](https://manager.line.biz/) > 自動回應訊息> 點選關鍵字回應

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line/將LINE自動回應改為關鍵字回應.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat-channels/line/將LINE自動回應改為關鍵字回應.png" alt="SeaChat | Line | 將LINE的自動回應改為關鍵字回應">
</a>

*將LINE的自動回應改為關鍵字回應*
</center>
<br/>

3. 將您想要的關鍵字新增於關鍵字回應內，並將訊息設定完成，例如 - 營業時間關鍵字可以為 : 營業時間、營業、開門時間等。 並且在訊息設定中填入 : "服務時間：週一至週五，辦公時間：8:00-17:00，中午休息時間：12:00-13:00"


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line/新增關鍵字於關鍵字回應內.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat-channels/line/新增關鍵字於關鍵字回應內.png" alt="SeaChat | Line | 新增關鍵字於關鍵字回應內">
</a>

*新增關鍵字於關鍵字回應內*
</center>
<br/>

4. 開啟SeaChat，在知識庫中增設一則知識庫文檔

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line/seachat-知識庫.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat-channels/line/seachat-知識庫.png" alt="SeaChat | Line | 新增知識到SeaChat知識庫內">
</a>

*新增知識到SeaChat知識庫內*
</center>
<br/>

5. 將這些關鍵字輸入到SeaChat的文件標題中，並提供補充說明於文件內文 : 您可以撰寫額外訊息，如預約連結、轉接客服等等，並將權重調到75。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line/將關鍵字應答輸入到SeaChat知識庫.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat-channels/line/將關鍵字應答輸入到SeaChat知識庫.png" alt="SeaChat | Line | 將關鍵字應答輸入到SeaChat知識庫">
</a>

*將關鍵字應答輸入到SeaChat知識庫*
</center>
<br/>

6. SeaChat AI 助理在LINE上就不會重複回答，並且可以幫你的客戶擴充知識提高體驗。LINE的訊息可以設定為圖片、影片，而文字訊息您可以放心交給SeaChat

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line/LINE文字訊息您可以放心交給SeaChat.png" target="_blank">
<img height="100%" width="50%" src="/images/seachat-channels/line/LINE文字訊息您可以放心交給SeaChat.png" alt="SeaChat | Line | LINE文字訊息您可以放心交給SeaChat">
</a>

*LINE文字訊息您可以放心交給SeaChat*
</center>
<br/>

本節將說明在整合 LINE 和 SeaChat 時的步驟與考量，包括完全取代 Line 的真人聊天功能或同時使用兩個平台的選項。

## 管理 LINE 和 SeaChat 的整合

### 選項 1：完全關閉 LINE 的真人聊天功能

**步驟 1：** 關閉 LINE 的真人聊天功能。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line//turn-off-live-chat.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat-channels/line//turn-off-live-chat.png" alt="SeaChat | Line | 關閉 LINE 的真人聊天功能">
</a>

**關閉 LINE 的真人聊天功能**
</center>

**關閉後：**

* 此時，您可以使用 SeaChat 的功能來取代 LINE 的自動回覆和真人聊天功能，所有對話記錄都將保存在 SeaChat 中。

### 選項 2：同時使用兩個平台

在此設置中，LINE 和 SeaChat 都可以對來訊作出回應。不過，需要注意處理每個平台回覆的相關事項。用戶均可從Line後台或SeaChat後台切換真人

#### 自動回覆：

* SeaChat 可以自動回覆訊息。這些回覆會同時顯示在 LINE 後台和 SeaChat 後台。

#### 從 Line 後台真人回覆：

**優點：**

* 真人回覆的訊息會完整展示在 LINE 後台。

**缺點：**

* 真人回覆的訊息不會顯示在 SeaChat 後台。
* SeaChat 不會知道 LINE 已經有真人回覆訊息，因此 SeaChat 仍會照常回覆，這可能導致用戶收到兩則回覆：SeaChat 的回覆（通常是第一條）以及 Line 後台的真人回覆。
* 使用 SeaChat 回覆會產生費用，每則訊息大約花費新台幣 $0.3（GPT-3.5）或 $0.18（GPT-4o-mini）。

#### 從 SeaChat 真人回覆：

**優點：**

* 真人回覆的訊息會完整展示在 SeaChat 後台。

**缺點：**

* 真人回覆的訊息不會顯示在 LINE 後台。
* 這些回覆會占用 LINE 的每月訊息數量限額（免費用戶每月 200 則）。若當月用完，則無法發送訊息，必須升級方案。

## LINE 的收費策略

* 透過 LINE 官方帳號管理員真人回覆不會佔用免費訊息數量。
* 參考官方定價詳情：[LINE 官方帳號管理員定價](https://tw.linebiz.com/column/LINEOA-2023-Price-Plan/)

### 哪些訊息類型會列入計費？

* 只有「群發訊息」、「Messaging API 進階功能的 Push API 訊息」以及「漸進式訊息」會列入計費。以下訊息類型屬於「免付費」訊息：
    * 加入好友的歡迎訊息。
    * 一對一的真人聊天訊息。
    * 自動回覆訊息。
    * AI 自動回覆訊息。
    * Messaging API 的 Reply API。

<br/>
* 請參考以下LINE 的可用訂閱方案，並詳細說明了各個訊息限額的定價。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line/line-reply-pricing.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat-channels/line/line-reply-pricing.png" alt="SeaChat | Line | LINE 推廣方案細節">
</a>

**LINE 推廣方案細節**
</center>

## LINE 按鈕訊息的限制

當用戶在使用 SeaChat 的 LINE 頻道時，可能會遇到按鈕訊息在點擊按鈕後被截斷的問題。這是由於 LINE 按鈕訊息的字符限制所致。

以下是我們目前按鈕模板和回傳按鈕的字符限制總結：

- **訊息字符限制**：200 字符

- **回傳按鈕內容字符限制**：300 字符（所有按鈕總計）

- **回傳按鈕數量限制**：最多 4 個按鈕

如需詳細參考，請訪問 LINE 開發者文檔中的以下部分：

在 [按鈕模板](https://developers.line.biz/en/reference/messaging-api/#template-messages) 部分下查閱按鈕模板訊息字符限制和按鈕數量限制。

在 [回傳動作](https://developers.line.biz/en/reference/messaging-api/#action-objects) 部分下查閱回傳按鈕內容的字符限制。

SeaChat 為此問題提供了解決方案。利用 KB ID 功能來避免訊息被截斷。請查看我們的 Wiki 關於 [KB ID](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/webpage-link/#kb-id) 的更多信息，以了解如何避免訊息被截斷。

## 🚨 LINE的AI自動回覆功能即將停用

[LINE的AI自動回覆功能](https://tw.linebiz.com/manual/line-official-account/oa-manager-smartchat/)將在2024年5月停止服務。

如果你還在使用AI自動回覆功能，需要盡快安排替代方案。

## 🎯 常見問題

### 客戶如何知道真人客服已經離開聊天？

當真人客服結束對話後，他/她可以點擊 **完成** 按鈕。客戶會看到一條訊息，告訴他們「真人客服已完成對話」。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-channels/line/faq-1.png" target="_blank">
<img height="50%" width="100%" src="/images/seachat-channels/line/faq-1.png" alt="SeaChat | Line | 真人客服已完成對話訊息">
</a>

</center>
<br/>

### 我可以設定指定運作時間讓我的 AI 助理自動開始對話嗎？

目前，我們不支持設定指定運作時間來讓 AI 助理自動開始對話。不過，您可以在完成對話後，通過點擊 **完成** 按鈕來輕鬆啟動 AI 助理。請參考我們真人客服的[教學](https://wiki.seasalt.ai/zh/seachat/live-agent-transfer/)。

### 我可以在 LINE 聊天中看到 AI 助理的回應嗎？

當然可以，您不只可以在 LINE 聊天中看到 AI 助理的回應，真人助理的回應也看得到！不過，我們建議使用 SeaChat 的對話平台，以便更好地瀏覽和控制所有對話。

### 為什麼我的按鈕在 LINE 頻道中顯示 "Live Agent"？如何把它更改為中文？

要在 LINE 頻道的 UI 中將按鈕的語言從英文改為中文，您需要前往 **網頁AI助理** 頻道。

在 **頻道** 中，找到 **網頁AI助理** 頻道。在 **基本設定** 中將語言修改為中文。這將更改 LINE 聊天 UI 中按鈕的語言。現在應該顯示 **真人客服** 而不是 **Live Agent**。

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/agent-information/webchat-settings-for-thrid-parties.png" target="_blank">
      <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/webchat-settings-for-thrid-parties.png" alt="SeaChat | Line | 聊天小工具基本設定">
    </a>
  </div>
  <p style="margin-top: 20px; font-size: 15px">聊天小工具基本設定</p>
</div>



---


#### Messenger嵌入式登錄

<!-- Source: seachat-manual/04-channels/09-seachat-messenger-integration-embedded-signup.md -->

<!-- Weight: 302 -->

*利用本指南或YouTube視頻教程，探索如何將SeaChat AI助理集成到Facebook Messenger，設置自動回應，並管理真人客服交接。*

本指南將引導您如何使用 Facebook 嵌入式註冊將您的 Facebook 專頁連接至 SeaChat。

### ✨ 為什麼要使用嵌入式註冊？
相較於舊方法，SeaChat 的 Messenger 整合搭配嵌入式註冊更簡單、更快速、更強大。以下是原因：

✅ 無縫設定體驗
您不再需要離開 SeaChat 介面或切換分頁。所有操作都在 SeaChat 中完成 — 登入、權限核准和專頁連接。

✅ 無需 Meta 開發者帳號
使用嵌入式註冊，您不需要建立自己的 Meta 應用程式或通過 Meta 的應用程式審查流程。我們已經為您處理好了。

<!-- ✅ 突破 <a href="https://developers.facebook.com/docs/messenger-platform/send-messages/?locale=en_US" target="_blank">Meta 的 24 小時規則</a>限制。透過 SeaChat 的 Messenger 整合，用戶可以隨時向您的專頁發送訊息 — SeaChat 會立即接收。由於我們的應用程式已獲得 Meta 認證並具有真人客服權限，您的支援團隊可以在 24 小時時限之後回覆訊息，無需使用訊息範本或額外審批。您不需要建立自己的 Meta 應用程式或通過應用程式審查 — SeaChat 已為您處理所有事項，讓您專注於協助客戶。 -->


### 只需兩步驟即可連接您的 Facebook 專頁
前往您的 SeaChat Channels 頁面中的 Messenger With Embedded Signup 卡片。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-1.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 


**步驟 1：登入 Facebook 並選擇 Facebook 專頁**

- 點擊連接按鈕，會出現 Facebook 登入彈窗。
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-2.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

- 使用管理該專頁的 Facebook 帳號登入。
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-2-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-2-1.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

- 選擇您要連接的專頁並授予所有請求的權限。請注意，我們每個 AI 助理僅支援一個專頁。如果您想連接多個專頁，需要為每個專頁建立新的 SeaChat AI 助理。
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-2-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-2-2.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

**步驟 2：選擇頻道特定語言**

定義語音訊息的語言，以便 SeaChat 可以將其轉錄為文字，並以相同語言回覆。這也適用於系統訊息（例如，當用戶點擊 🧹新主題 後）。

🚀 設定完成！
完成後，SeaChat 將透過您的 SeaChat AI 助理開始處理訊息。您可以立即傳送訊息到已連接的專頁進行測試。

### 已經用舊方式連接 Messenger？
如果您先前透過我們的舊方法整合了 Messenger，以下是切換方式：
前往您的 SeaChat 中的 Messenger 整合頁面。

- 找到「Messenger Integration(不推薦使用)」卡片。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/facebook-messenger/messenger-integration-embedded-signup-3.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

- 點擊右上角的「移除」以移除舊的整合。
- 然後，前往新的 Messenger With Embedded Signup 卡片，依照更新後的步驟重新連接。

🙋 需要遷移協助嗎？ <br/>
📧 請聯絡我們： seachat@seasalt.ai  <br/> 


# 與真人助理互動
您是否注意到在上圖中我使用了`/live_agent`來請求真人助理？如果助理恰好在線並設置了他們的在線狀態：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 40%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" alt="SeaChat | Messenger | 真人助理狀態">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理狀態
</p>
</div>
</div>

<br/> 

他們可以直接與用戶對話！

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" alt="SeaChat | Messenger | 真人助理互動">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理互動
</p>
</div>
</div>

<br/> 

如果助理不在線，他們可以開啟電子郵件通知以在用戶發起聊天或請求真人助理時收到當時的電子郵件：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" alt="SeaChat | Messenger | 真人助理偏好">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理偏好
</p>
</div>
</div>

<br/> 

## 移除您的Messenger集成

如果您想要移除Messenger集成，您需要在兩個地方進行操作：
1. 從您的MetaApp中正確移除頁面訪問權限
2. 在SeaChat內點擊移除按鈕

對於第1步，請前往您的**[Meta商業App](https://developers.facebook.com/)** → **Messenger** → **Messenger API Settings** → **Generate access tokens** → 移除

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" alt="SeaChat | Messenger | 移除集成">
</a>
    <p style="margin-top: 20px; font-size: 15px">移除集成</p>
</div>
</div>

<br/> 


## 回應語音剪輯
您知道SeaChat也支持語音消息嗎？如果用戶發送語音剪輯，SeaChat可以將其轉錄為文字，並通過文字回應！

目前，它支持英語語音到文字轉錄，但如果您需要更多語言支持，請告訴我們。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" alt="SeaChat | Messenger | 語音剪輯轉錄和SeaChat回應">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Facebook Messenger語音剪輯轉錄和SeaChat回應</strong></p>
</div>
</div>

<br/> 

## Messenger 的訊息回傳 (Postback)
當你設定好 Messenger 的整合後，你就可以使用 SeaChat 的[按鈕功能](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/webpage-link/)來與客戶互動。這允許你在答案中以按鈕的形式加入網址或其他附加資訊。

要啟動此功能，請進入 Messenger 的 **Edit Page Subscription** 頁面。


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" alt="SeaChat | Messenger | Edit Page Subscription">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Edit Page Subscription</strong></p>
</div>
</div>

<br/> 

### Messenger 按鈕限制

按照上述步驟操作後，你現在可以在整合後的 Messenger 中使用 SeaChat 的按鈕功能。然而，由於我們仍在使用 Messenger 提供的 API，因此在建立按鈕時有一些限制需要注意，以避免任何問題。

以下是限制條件：

兒每個訊息範本最多允許**3個回傳按鈕**。
- 每個按鈕的回傳資料最多可達**1000個字元**，按下時將傳送回你的webhook。
- 按鈕標題限制為**20個字元**。
- 這些限制適用於每個按鈕，因此你可以每個訊息擁有 3 個按鈕，每個按鈕擁有各自的 1000 字元回傳資料與 20 字元的標題。
- [開發者文件](https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback)

用戶可以使用 SeaChat 的 **[KB ID](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/webpage-link/#kb-id)** 功能，來改善這些限制所帶來的不便，請參閱連結以獲取更多資訊。

## :dart: 故障排除

如果您沒有收到來自SeaChat助理的Messenger回應，您應該驗證以下容易被忽略的設置：
- 您的MessengerApp是否已設置為[**真人模式**](#live-mode)？確保它不是在開發模式下運行。
- 您是否配置了[**webhook字段**](#perma-token-webhook)以允許**消息權限**？如果未正確授予此權限，SeaChat將無法接收來自Messenger的消息。


## 支持
需要協助？聯繫我們：[seachat@seasalt.ai](mailto:seachat@seasalt.ai).



---


#### Messenger (不推薦使用)

<!-- Source: seachat-manual/04-channels/06-seachat-messenger-integration.md -->

<!-- Weight: 303 -->

*利用本指南或YouTube視頻教程，探索如何將SeaChat AI助理集成到Facebook Messenger，設置自動回應，並管理真人客服交接。*

## 注意：此 Messenger 整合已不再推薦使用。請改用[嵌入式註冊的 Messenger 整合](/zh/seachat/seachat-manual/04-channels/09-seachat-messenger-integration/)。


## 🎥 影片教學

<iframe width="100%" height="400" src="https://www.youtube.com/embed/aFruY5bwG00?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


## 簡介
在這教學中，我們將深入探討在Facebook Messenger上設置由ChatGPT驅動的聊天機器人（AI助理）的過程。從本教學，您將清楚了解如何：
1. **自動回App戶消息**：
- 將您的Messenger商業帳號連接到SeaChat聊天機器人/AI助理平台。
- 使用ChatGPT等先進大語言模型訓練聊天機器人，以生成對廣泛用戶查詢的自然語言回應。
- 配置聊天助理，根據您的知識庫自動回應訊息。
2. **通過SeaChat管理所有與用戶的對話**：
- 使用SeaChat，掌握用戶和您的聊天機器人之間的所有對話。
- 查看聊天記錄，分析用戶行為，並識別聊天助理回應中的需要改進的部分。
- 管理對話，確保與用戶的無縫溝通。
3. **用戶能夠請求真人客服協助**：
- 允許用戶在他們有更進階需求或需要個性化支援時請求真人客服的協助。
- 順暢地將對話從AI聊天助理轉移到真人客服。
- 用戶可選擇他們需要的客服支援層級，增強整體客戶體驗。

到本教學結束時，您將擁有一個由SeaChat驅動的Facebook Messenger機器人以及一個SeaChat控制台來查看所有消息，如下所示：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/facebook-messenger-integration.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/facebook-messenger-integration.png" alt="SeaChat | Messenger | Facebook Messenger集成">
</a>
    <p style="margin-top: 20px; font-size: 15px">使用SeaChat的ChatGPT驅動的聊天機器人與Facebook Messenger集成</p>
</div>
</div>

<br/>

在開始設置過程之前，有幾個關鍵點需要記住：

**Messenger的限制**：
- SeaChat AI助理設計只能回應訊息，不能自行主動開始對話。
- 作為SeaChat管理員的您仍然能夠與用戶進行對話，但請事先安排真人助理。

**誰需要Messenger頻道**：
- 需要自動化處理大量Messenger訊息的企業和組織。
- 尋求提供個性化和更好客戶體驗的公司。
- 通過自動化常規查詢來減輕人力負擔的客戶服務部門。

---

## Facebook Messenger設置
設置Facebook Messenger需要仔細照著以下步驟設定，往下滑可看到逐步詳細指南：

1. **[創建MessengerApp](###創建Facebook-MessengerApp)**:
- 轉到Meta Developer網站。
- 點擊右上角的**MyApps**。
- 從下拉選單選擇**CreateApp**。

2. **[選擇App類型](###選擇App類型)**:
- 在**App Type**下選擇**Other**。
- 輸入一個全新的App名稱，避免使用**MessengerApp**或**Facebook**等難以辨識的名稱。

3. **[添加Messenger產品](###添加Messenger產品)**:
- 滾動到App列表的底部。
- 找到**Messenger**並選擇它以將該產品添加到您的App中。

5. **[配置MessengerApp](#如何配置messengerapp)**:
- 仔細閱讀配置頁面上的信息。
- 按照指示提供必要的細節，例如商業名稱、地址和聯繫信息。
- 確保正確填寫所有必填欄位。

6. **[生成訪問金鑰](#步驟2生成訪問金鑰)**:
- 配置完成後，生成一個永久的訪問金鑰。
- 此金鑰對於使用Messenger API至關重要。

7. **[移除您的Messenger集成](#移除您的messenger集成)**:
- 從您的MetaApp中正確移除頁面訪問權限
- 在SeaChat內點擊移除按鈕

> :books: **推薦閱讀**:
>
> 記得遵守[Messenger API](https://developers.facebook.com/docs/messenger/)政策和指南，以維持合規並避免任何潛在問題。

以下將逐步引導您完成過程並配上詳細操作指南：

### 創建Facebook MessengerApp

您首先需要前往[Meta Developer網站](https://developers.facebook.com/)，點擊右上角的**我的App**，然後從下拉選單中選擇**創建App**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/facebook-messenger/create-new-messenger-app.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/create-new-messenger-app.png" alt="SeaChat | Messenger | 創建新的Messenger App">
    </a>
<br/>
    <p style="margin-top: 20px; font-size: 15px">創建新的Messenger App</p>
</div>
</div>

### 選擇App類型

創建一個**Other** App，因為我們將僅使用此App來訪問您的Messenger帳戶。在**Selectapp type page**上，選擇**Business**作為類型，然後點擊**Next**。

<br/>
<div style="display: flex; flex-direction: column; align-items: center;">
    <div style="width: 100%; height:100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-1.png" alt="SeaChat | Messenger | 創建一個 Other App">
        </a>
        <p style="margin-top: 20px; font-size: 15px">創建一個 <strong>Other</strong> app</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-2.png" alt="SeaChat | Messenger | 選擇Business">
        </a>
        <p style="margin-top: 20px; font-size: 15px">選擇<strong>Business</strong></p>
    </div>
</div>

<br/>

在這裡，我們創建了一個名為**Seasalt.aiApp**的App，請注意，Meta不允許App名稱中包含**Facebook**或**Messenger**。在選擇App名稱時，請仔細閱讀警告消息。

<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-3.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-3.png" alt="SeaChat | Messenger | 創建App">
        </a>
        <p style="margin-top: 20px; font-size: 15px">創建App</p>
    </div>
<br/>

### 添加Messenger產品

創建App後，讓我們添加[Messenger產品](https://developers.facebook.com/docs/messenger/)。在**Add products to yourapp**部分下找到Messenger框，並點擊**Set up**以創建您的App。

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/facebook-messenger/add-messenger-product.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/add-messenger-product.png" alt="SeaChat | Messenger | 將Messenger添加到您的App<">
    </a>
<br/>
    <p style=" font-size: 15px">將Messenger添加到您的App</p>
</div>
</div>


## 如何配置MessengerApp
> :rotating_light: **警告** :rotating_light:
>
> 這裡的事情可能會變得有些複雜。如果您不夠小心並且錯過了一步，可能無法成功配置您的MessengerApp。所以，讓我們一起仔細地遍歷以下指示。

### 步驟1：配置Webhooks

在左側的**Messenger**下找到**Messenger API**。從這裡，我們首先需要配置Webhook和SeaChat提供的金鑰。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-1.png" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-1.png" alt="SeaChat | Messenger | Verify token">
    </a>
<br/>
    <p style=" font-size: 15px">Verify token</p>
</div>
</div>


您只需要做以下操作。前往SeaChat，導航至**Agent Configuration → Channels → Messenger**以獲取**Callback URL**和**Verify token**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-2.png" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-2.png" alt="SeaChat | Messenger | 導航至SeaChat的Messenger">
    </a>
<br/>
    <p style=" font-size: 15px">導航至SeaChat的<strong>Messenger</strong></p>
</div>
</div>
``
將SeaChat的步驟1的信息複製並貼上到Messenger儀表板的相應部分。


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-3.png" alt="SeaChat | Messenger | 將SeaChat信息配置到儀表板">
</a>
    <p style="margin-top: 20px; font-size: 15px">將SeaChat信息配置到儀表板</p>
</div>
</div>

<br/>

將**Callback URL**和**Verify token**貼上到Messenger儀表板的相應字段中：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-4.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-4.png" alt="SeaChat | Messenger | 貼上URL和金鑰">
</a>
    <p style="margin-top: 20px; font-size: 15px">貼上URL和金鑰</p>
</div>
</div>

<br/>

之後，我們需要正確配置**Webhook Fields**，以授予webhook回調URL適當的權限：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-5.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-5.png" alt="SeaChat | Messenger | Webhook Fields配置">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Webhook Fields</strong>配置</p>
</div>
</div>

<br/>

選擇**messages**並點擊**Subscribe**：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-6.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-6.png" alt="SeaChat | Messenger | 訂閱選擇的消息">
</a>
    <p style="margin-top: 20px; font-size: 15px">訂閱選擇的消息</p>
</div>
</div>

<br/>

您的webhook最終配置應如下所示：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-7.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-7.png" alt="SeaChat | Messenger | Webhook配置">
</a>
    <p style="margin-top: 20px; font-size: 15px">Webhook配置</p>
</div>
</div>

<br/>

### 步驟2：生成訪問金鑰

MetaApp需要訪問某個Facebook頁面，以便能夠接收從該頁面發送的消息。因此，在步驟2中，您首先需要授權它訪問您的公共Facebook頁面。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-1.png" alt="SeaChat | Messenger | 生成訪問金鑰">
</a>
    <p style="margin-top: 20px; font-size: 15px">生成訪問金鑰</p>
</div>
</div>

<br/>

在授權Facebook頁面後，您可以進一步**Add Subscriptions**：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-2.png" alt="SeaChat | Messenger | 添加訂閱">
</a>
    <p style="margin-top: 20px; font-size: 15px">點擊<strong>添加訂閱</strong></p>
</div>
</div>

<br/>

同樣，我們要訂閱**messages**：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-3.png" alt="SeaChat | Messenger | 選擇messages">
</a>
    <p style="margin-top: 20px; font-size: 15px">選擇<strong>messages</strong></p>
</div>
</div>

<br/>

最後，讓我們生成訪問金鑰：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-4.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-4.png" alt="SeaChat | Messenger | 金鑰生成">
</a>
    <p style="margin-top: 20px; font_size: 15px">金鑰生成</p>
</div>
</div>

<br/>

一旦生成了金鑰，我們需要複製該金鑰：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-5.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-5.png" alt="SeaChat | Messenger | 金鑰詳情">
</a>
    <p style="margin-top: 20px; font-size: 15px">金鑰詳情</p>
</div>
</div>

<br/>

將其貼上到SeaChat Messenger設置的第二步：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-6.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-6.png" alt="SeaChat | Messenger | 將金鑰貼上到SeaChat">
</a>
    <p style="margin-top: 20px; font-size: 15px">將金鑰貼上到SeaChat</p>
</div>
</div>

<br/>

現在將您的App模式設為**Live**，您就可以與機器人對話了：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a id="live-mode" href="/images/seachat/en/channels/facebook-messenger/access-token-7.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-7.png" alt="SeaChat | Messenger | "真人模式>
</a>
    <p style="margin-top: 20px; font-size: 15px">真人模式</p>
</div>
</div>

<br/>

### 步驟3：替代完成App審查

到目前為止，您的Messenger機器人只會對您這位App創建者做出回應。如果您將其交給其他人，他們將得不到任何回應。按照Facebook的指示完成“步驟3. 完成App審查”可能很誘人：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/app-review-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/app-review-1.png" alt="SeaChat | Messenger | App審查">
</a>
    <p style="margin-top: 20px; font-size: 15px">App審查</p>
</div>
</div>

<br/> 

然而，完成App審查可能需要多達5天的時間，而且過程非常繁瑣。例如，Meta會要求您錄製MetaApp的影片演示。

替代方法是將頁面分配給您在Meta擁有的業務。為此，前往[Meta商業套件](https://business.facebook.com/)，選擇您創建MetaApp的業務，然後轉到**Accounts** → **Pages**，並確保您的聊天機器人連接的Facebook頁面出現在那裡：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/facebook-pages.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/facebook-pages.png" alt="SeaChat | Messenger | Facebook頁面">
</a>
    <p style="margin-top: 20px; font-size: 15px">確保Facebook頁面在您的業務下顯示
</p>
</div>
</div>

<br/> 

您現在應該已經全部設置完成了！

# 與真人助理互動
您是否注意到在上圖中我使用了`/live_agent`來請求真人助理？如果助理恰好在線並設置了他們的在線狀態：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 40%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" alt="SeaChat | Messenger | 真人助理狀態">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理狀態
</p>
</div>
</div>

<br/> 

他們可以直接與用戶對話！

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" alt="SeaChat | Messenger | 真人助理互動">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理互動
</p>
</div>
</div>

<br/> 

如果助理不在線，他們可以開啟電子郵件通知以在用戶發起聊天或請求真人助理時收到當時的電子郵件：

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" alt="SeaChat | Messenger | 真人助理偏好">
</a>
    <p style="margin-top: 20px; font-size: 15px">真人助理偏好
</p>
</div>
</div>

<br/> 

## 移除您的Messenger集成

如果您想要移除Messenger集成，您需要在兩個地方進行操作：
1. 從您的MetaApp中正確移除頁面訪問權限
2. 在SeaChat內點擊移除按鈕

對於第1步，請前往您的**[Meta商業App](https://developers.facebook.com/)** → **Messenger** → **Messenger API Settings** → **Generate access tokens** → 移除

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" alt="SeaChat | Messenger | 移除集成">
</a>
    <p style="margin-top: 20px; font-size: 15px">移除集成</p>
</div>
</div>

<br/> 


## 回應語音剪輯
您知道SeaChat也支持語音消息嗎？如果用戶發送語音剪輯，SeaChat可以將其轉錄為文字，並通過文字回應！

目前，它支持英語語音到文字轉錄，但如果您需要更多語言支持，請告訴我們。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" alt="SeaChat | Messenger | 語音剪輯轉錄和SeaChat回應">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Facebook Messenger語音剪輯轉錄和SeaChat回應</strong></p>
</div>
</div>

<br/> 

## Messenger 的訊息回傳 (Postback)
當你設定好 Messenger 的整合後，你就可以使用 SeaChat 的[按鈕功能](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/webpage-link/)來與客戶互動。這允許你在答案中以按鈕的形式加入網址或其他附加資訊。

要啟動此功能，請進入 Messenger 的 **Edit Page Subscription** 頁面。


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" alt="SeaChat | Messenger | Edit Page Subscription">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Edit Page Subscription</strong></p>
</div>
</div>

<br/> 

### Messenger 按鈕限制

按照上述步驟操作後，你現在可以在整合後的 Messenger 中使用 SeaChat 的按鈕功能。然而，由於我們仍在使用 Messenger 提供的 API，因此在建立按鈕時有一些限制需要注意，以避免任何問題。

以下是限制條件：

兒每個訊息範本最多允許**3個回傳按鈕**。
- 每個按鈕的回傳資料最多可達**1000個字元**，按下時將傳送回你的webhook。
- 按鈕標題限制為**20個字元**。
- 這些限制適用於每個按鈕，因此你可以每個訊息擁有 3 個按鈕，每個按鈕擁有各自的 1000 字元回傳資料與 20 字元的標題。
- [開發者文件](https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback)

用戶可以使用 SeaChat 的 **[KB ID](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/webpage-link/#kb-id)** 功能，來改善這些限制所帶來的不便，請參閱連結以獲取更多資訊。

## :dart: 故障排除

如果您沒有收到來自SeaChat助理的Messenger回應，您應該驗證以下容易被忽略的設置：
- 您的MessengerApp是否已設置為[**真人模式**](#live-mode)？確保它不是在開發模式下運行。
- 您是否配置了[**webhook字段**](#perma-token-webhook)以允許**消息權限**？如果未正確授予此權限，SeaChat將無法接收來自Messenger的消息。


## 支持
需要協助？聯繫我們：[seachat@seasalt.ai](mailto:seachat@seasalt.ai).



---


#### 電話

<!-- Source: seachat-manual/04-channels/07-seachat-voicebot.md -->

<!-- Weight: 303 -->

*了解如何在 SeaChat 設置語音助理，處理來電語音和對外撥話，並使用免費電話號碼提供客戶支援。快速上手設置並測試您的語音助理。*


SeaChat 不僅可以處理文字對話，還可以處理電話。SeaChat 允許您創建一個基於語音的對話助理來接聽所有來電，或者外撥至客戶電話。這個語音助理可以處理來電語音，回答客戶查詢，並提供客戶支援。SeaChat 語音助理還可以在需要時轉接給真人助理。在接下來的章節中，我們將向您展示設置 SeaChat 語音助理有多容易，以及您如何通過實際通話來測試您的助理。

--- 
## 設置 SeaChat 語音助理

首先，我們需要一個新的助理來處理語音來電。創建一個新的語音助理，請點擊您的頭像旁邊的助理下拉選單。您可以看到您已創建的助理列表。點擊 **新增AI助理** 按鈕來創建一個新助理。

在我的助理描述中，我確保包含了這個助理是用於語音接聽。這樣，我就可以輕鬆地辨認哪個助理是用於語音對話，哪個助理是用於文字對話。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/agent-description.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/agent-description.png" alt="SeaChat | 新增AI助理">
</a>

*新增AI助理*
</center>

一旦我們創建了我們的語音助理，讓我們開始設置語音助理以處理來電語音。在 **AI助理設定** 的 **頻道** 下找到 **電話**。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/choose-inbound-calls.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/choose-inbound-calls.png" alt="SeaChat | 設置電話頻道">
</a>

*設置 **電話** 頻道*
</center>

### 免費電話號碼

在 **電話** 通道中，我們需要首先購買一個免費電話號碼。選擇您想要購買免費電話號碼和電話號碼的國家。一旦您選擇了理想的設定，點擊 **確認購買** 按鈕。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/buy-a-number.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/buy-a-number.png" alt="SeaChat | 購買免費電話號碼">
</a>

*購買免費電話號碼*
</center>

購買完成後，您可以看到您選擇的免費電話號碼。如果您對號碼不滿意，您可以隨時**取消號碼**並購買新號碼。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/toll-free-number.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/toll-free-number.png" alt="SeaChat | 免費電話號碼詳細信息">
</a>

*免費電話號碼詳細信息*
</center>

### 助理設定

購買免費電話號碼後，我們需要設定助理以處理來電語音。在 **設定AI語音助理** 部分，您可以設置語音助理來處理來電。

您可以像任何其他 SeaChat 助理一樣為您的語音助理啟用真人助理功能。請確保您有一位真人客服在用戶啟用真人助理功能時監視並回應用戶。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/configure-agent.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/configure-agent.png" alt="SeaChat | 語音助理設定">
</a>

*語音助理設定*
</center>

如上圖所示，有一些參數需要設置才能完全設定語音助理。如果您不確定設定，您可以從選擇語言開始，SeaChat 將自動為您設置其餘的設定。如下圖所示，我為我的語音助理選擇了繁體中文和 SeaVoice模型。現在點擊 **儲存設定** 以確定您的設置。

> :mag_right: SeaChat 語言模型：**SeaVoice**
> 
> SeaChat 目前提供 SeaVoice 和 SeaVoice-2 作為語音助理的語言模型。我們建議在大多數情況下使用 SeaVoice，因為它是語音助理中最穩定可靠的語言模型，而 SeaVoice-2 則是我們新開發的模型，仍處於實驗階段。


## 測試語音助理

現在我們已經設置了語音助理，我們可以開始測試我們的助理，看看它是否能夠處理來電語音以及對外撥話。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/configuration-done.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/configuration-done.png" alt="SeaChat | 設定完成">
</a>

*設定完成*
</center>

### 來電語音以及對外撥話

測試語音助理有兩種方法。您可以撥打您購買的免費電話號碼，以查看語音助理如何處理來電，或者為您的語音助理提供一個要撥打的號碼，來測試對外撥話。由於這兩種方法可能需要在助理設置中進行不同的設定，請選擇最適合您的方法。

<br/>
<center>
  <a href="/images/seachat/zh/channels/voicebot/test-agent.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/voicebot/test-agent.png" alt="SeaChat | 測試您的助理">
</a>

*測試您的助理*
</center>

大功告成。現在，您已經設置了 SeaChat 語音助理以處理來電語音或對外撥話。您現在可以通過實際通話來測試您的助理，並查看您的語音助理如何處理來電。

## 支援
需要幫助嗎？請聯繫我們：[seachat@seasalt.ai](mailto:seachat@seasalt.ai)。


---


#### Instagram 登錄使用

<!-- Source: seachat-manual/04-channels/10-instagram-oauth.md -->

<!-- Weight: 304 -->

*按照以下步驟將 Instagram 與您的應用程式整合，並建立AI agent的訊息。*


## 前置需求

- **Instagram Professional Account**：您需要擁有 **Business** 或 **Creator** 帳戶才能設定 **Instagram Messaging**。如果您目前的帳戶類型不符，可以在 **Instagram settings** 中 [切換到 Professional Account](https://www.facebook.com/business/help/502981923235522)。

### 只需兩步完成 Instagram 整合

前往 SeaChat 通道頁面中的 `Instagram` 卡片。
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/instagram/instagram-card.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/instagram/instagram-card.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

**步驟 1: 登入你的 Instagram 帳號**

點擊 `Connect` 按鈕，將出現 Instagram 登入弹窗。授予所有權限並點擊 `允許`

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/instagram/instagram-step-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/instagram/instagram-step-1.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 


**步驟 2: 選擇訊息輸入語言**

設定輸入訊息的語言，SeaChat 將以相同語言轉錄並回應。這個設定同樣適用於系統訊息（例如點擊 🧹開始新話題時）


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/instagram/instagram-step-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/instagram/instagram-step-2.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

🚀 完成啦！整合完成後，SeaChat 將開始以你的 AI 智能助理處理 Instagram 訊息，你可以立即測試發送訊息。

### 曾使用舊方式連線 Instagram？

如果你過去是用舊方式連線，現在需要分成兩步重新設定：

#### 步驟 1: 從 SeaChat 移除
- 前往 SeaChat 的 Instagram 連線頁面，在 Deprecated 區塊中找到舊會訊卡片
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/zh/channels/instagram/instagram-card-deprecated.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/channels/instagram/instagram-card-deprecated.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

<br/> 

- 點擊右上角的 `移除` 按鈕刪除
- 然後前往新的 `Instagram` 卡片，依照新步驟重新連線

#### 步驟 2: 從 Meta App 移除認證
正確從 Meta App 中移除帳號認證
前往 **Meta Business App** → **Instagram API setup with Instagram login** → **Generate access tokens** → 垃圾桶圖示 → **Remove Account**

🙋 需要遷移協助嗎？ <br/>
📧 請聯絡我們： seachat@seasalt.ai  <br/> 


---


#### Instagram (不推薦使用)

<!-- Source: seachat-manual/04-channels/08-instagram.md -->

<!-- Weight: 305 -->

*按照以下步驟將 Instagram 與您的應用程式整合，並建立AI agent的訊息。*


注意：此 Instagram 整合已不再推薦使用。請改用[Instagram 登錄使用](/zh/seachat/manual/channels/instagram/)。

## 前置需求

- **Instagram Professional Account**：您需要擁有 **Business** 或 **Creator** 帳戶才能設定 **Instagram Messaging**。如果您目前的帳戶類型不符，可以在 **Instagram settings** 中 [切換到 Professional Account](https://www.facebook.com/business/help/502981923235522)。

## 操作指引

### 步驟 1：建立 **Instagram App**

1. 訪問 [Meta Developer Site](https://developers.facebook.com/) 並點擊右上角的 **My Apps**。
2. 在下拉選單中選擇 **Create App** 開始建立。

- 輸入應用程式的相關資訊，如 **App Name** 和 **Contact Email**，然後點擊 **Next**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-name.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-name.png" alt="App Creation">
    </a>
</div>
</div>

<br/>

- 選擇一個使用案例，選擇 **Other**，然後點擊 **Next**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/use-cases.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/use-cases.png" alt="App Use Case Selection">
    </a>
</div>
</div>

<br/>

- 將 **App Type** 設定為 **Business**，然後點擊 **Next**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-type.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-type.png" alt="App Type Selection">
    </a>
</div>
</div>

<br/>

- 檢查應用程式的詳細資訊後，點擊 **Create App**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/business-details.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/business-details.png" alt="App Review and Creation">
    </a>
</div>
</div>

<br/>

### 步驟 2：將 **Instagram Product** 加入應用程式

- 在 **Add Products to Your App** 區域中選擇 **Instagram**。
- 點擊 **Set Up** 按鈕將其新增至應用程式。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/add-instagram.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/add-instagram.png" alt="Add Instagram Product">
    </a>
</div>
</div>

<br/>

### 步驟 3：連結 **Instagram Account**

- 前往 **API Setup with Instagram** 頁面。
- 在步驟 1 點擊 **Add Account**，連結您的 **Instagram Account**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/instagram-connect.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/instagram-connect.png" alt="Connect Instagram Account">
    </a>
</div>
</div>

<br/>

### 步驟 4：配置 **Webhook**

1. 在 **SeaChat** 獲取 **Webhook URL**。
    - 前往 **Agent Configuration** → **Channels** → **Instagram** 查看 **Callback URL** 和 **Verify Token**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/seachat-channel.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/seachat-channel.png" alt="SeaChat Webhook Details">
    </a>
</div>
</div>

<br/>

2. 點擊步驟 1 中的 **Set Up Verify Token**。完成後，會彈出提示框確認 Token 已成功儲存。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/verify-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/verify-token.png" alt="Verify Token Confirmation">
    </a>
</div>
</div>

<br/>

3. 回到 **Instagram App Dashboard**，將 **Webhook URL** 和 **Verify Token** 貼入相應欄位並點擊 **Save**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/callback-url.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/callback-url.png" alt="Webhook URL and Tokens">
    </a>
</div>
</div>

<br/>

- 點擊 **Manage**，啟用所有必要的 **Webhook Events**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/manage-webhook.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/manage-webhook.png" alt="Webhook Configuration">
    </a>
</div>
</div>

<br/>

### 步驟 5：生成 **Access Token**

- 在 **Generate Access Token** 區域中點擊 **Generate Token** 按鈕。
- 在彈出窗口中勾選 **I Understand**，然後複製 **Access Token**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/generated-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/generated-token.png" alt="Generate Access Token">
    </a>
</div>
</div>

<br/>

- 將複製的 **Token** 貼到 **SeaChat Instagram Setup Interface** 的步驟 2，然後點擊 **Save**。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/save-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/save-token.png" alt="Access Token Setup">
    </a>
</div>
</div>

<br/>

完成所有步驟後，您已經成功在 **SeaChat** 中設置 **Instagram Integration**！

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/seachat-setup.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/seachat-setup.png" alt="Integration Complete">
    </a>
</div>
</div>

<br/>


---


#### 網頁機器人

<!-- Source: seachat-manual/04-channels/08-install-to-webpage.md -->

<!-- Weight: 306 -->

*發掘如何利用SeaChat將AI助理整合到您的網站和LINE通訊平台。這份指南將詳細介紹安裝網頁助理的完整過程，包括如何將提供的程式碼嵌入您的網頁HTML中。*


## :movie_camera: 在网页上集成 SeaChat 小部件

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/5YCiO8GEAu0?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube 视频播放器" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## 自定义您的公司网页小部件

网页小部件是一个强大的工具，可让您将 SeaChat 集成到您的网站中。此功能使您能够提供实时客户支持并与网站访客互动。小部件可以根据您的品牌标识和网站设计进行定制。您还可以创建表单以收集访客信息和反馈。

## SeaChat 小部件配置

SeaChat 小部件提供多种自定义选项，帮助您创建无缝的客户体验。您可以调整小部件的外观和行为以满足您的需求。

### 基本设置和聊天设置

在这里，您可以定义小部件的名称、描述，并在 **基本设置** 中选择小部件的 UI 语言。向下滚动查看 **聊天设置**，在这里您可以定义助理在聊天中的行为。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/basic-settings.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/basic-settings.png" alt="SeaChat 的基本设置">
</a>

_样式的基本设置_

</center>
<br/>

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/chat-settings.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/chat-settings.png" alt="SeaChat 的聊天设置">
</a>

_助理回答的聊天设置_

</center>
<br/>

每次更改后，您可以通过点击 **预览** 按钮在预览窗口中查看更改。一旦对更改满意，请点击 **保存** 按钮。

> :warning: 注意
>
> 请注意，只有点击 **保存** 按钮后更改才会保存。我们建议您点击 **预览** 按钮查看更改，只有在保存更改后才能点击 **测试 AI 助理**。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/preview-widget-chat.png" target="_blank">
<img height="100%" width="70%" style="border-radius: 5px" src="/images/seachat/zh/channels/webpage-widget/preview-widget-chat.png" alt="SeaChat 的基本设置">
</a>

_预览窗口_

</center>
<br/>

### 卡片设置

除了完全可定制的小部件外，您还可以创建卡片向客户显示信息。卡片可用于在用户首次访问您的网站时提供信息。您还可以将链接附加到卡片上，将用户引导到特定页面。要添加更多卡片，请点击 **加号** 按钮。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/card-setting.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/card-setting.png" alt="SeaChat 的聊天设置">
</a>

_设计您的卡片_

</center>
<br/>

### 自定义表单：聊天前用户信息收集表单

有时您可能希望收集客户信息。您可以创建自定义表单以收集信息，例如姓名、电子邮件和电话号码。这些信息可用于为客户提供个性化支持。根据您的使用场景，我们可以定义新表单并重复使用旧表单。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/custom-forms.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/custom-forms.png" alt="SeaChat 的自定义表单设置">
</a>

_选择或创建客户表单_

</center>
<br/>

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/custom-forms2.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/custom-forms2.png" alt="SeaChat 的自定义表单设置">
</a>

_聊天开始前选择_

</center>
<br/>

要编辑表单，请点击 **编辑** 按钮后点击 **&#8942;**。您还可以通过点击 **删除** 按钮删除表单。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/access-edit-forms.png" target="_blank">
<img height="100%" width="60%" src="/images/seachat/zh/channels/webpage-widget/access-edit-forms.png" alt="SeaChat 的自定义表单设置">
</a>

_选择或创建客户表单_

</center>
<br/>

### 自定义表单：客户满意度调查表单

现在，您可以通过客户满意度调查表单轻松收集客户反馈——就像设置用户信息收集表单一样！当访客尝试关闭 WebChat 小部件时，表单会自动弹出，允许访客留下星级评分并可选择写评论。

设置步骤：

1. 点击添加新表单按钮并选择客户满意度调查卡片。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/custom-forms2.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/custom-forms2.png" alt="SeaChat 的自定义表单设置">
</a>

_选择客户满意度调查_

</center>
<br/>

2. 配置表格

- 打开启用开关。
- 根据您的需求自定义字段，包括：表单名称、调查标题、调查描述，并选择启用或禁用评论框（用于书面反馈）。如果启用，您还可以自定义评论框中的占位符文本。完成后点击保存。

3. 按以下 [安装步骤](/zh/seachat/manual/channels/webpage/#安装) 将更新的小部件代码安装到您的网站。

4. 查看调查结果

   现在，当访客与您的 AI 助理聊天并点击右下角图标关闭小部件时，客户满意度调查表单会弹出。如果访客提交反馈，您可以进入 SeaChat 的会话页面，通过点击会话头像查看星级评分和评论。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/csat-demo.gif" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/csat-demo.gif" alt="SeaChat 的自定义表单设置">
</a>

_展示访客如何留下反馈_

</center>
<br/>

<br/>

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/csat-form-result.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/csat-form-result.png" alt="SeaChat 的自定义表单设置">
</a>

_查看客户满意度调查结果_

</center>

<br/>

## 安装

现在您已经自定义了小部件，可以将其安装到您的网站。只需从 **安装小部件** 中复制提供的代码片段，并将其粘贴到您网站的 HTML 代码中。也就是当前 `<body>{...}</body>` 标签的末尾。

小部件将显示在您的网站上，使您能够为客户提供实时支持。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/installation-code.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/installation-code.png" alt="SeaChat 界面指导用户安装网页小部件">
</a>

_遵循安装步骤_

</center>
<br/>

## 支持

需要帮助？请联系我们：[seachat@seasalt.ai](mailto:seachat@seasalt.ai)。


---


#### Google Calendar

<!-- Source: seachat-manual/05-integrations/01-seachat-google-calendar-integration.md -->

<!-- Weight: 400 -->

*了解如何透過 SeaChat 的 AI 聊天和語音助理與 Google Calendar之間的整合，自動化會議安排，以便有效管理預約。*


## 簡介
> 登入 SeaChat 後，導航到 **AI助理配置** -> **整合** -> **Google Calendar** 來添加整合。

## Google Calendar 整合

<br/>
<center>
  <a href="/images/seachat-integrations/google-calendar/zh/google-calendar-ui.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/google-calendar/zh/google-calendar-ui.png" alt="SeaChat | Google Calendar 整合介面">
</a>

*Google Calendar 整合介面*
</center>

透過 Google Calendar 整合，您的 SeaChat 助理可以透過聊天或語音互動為您預約。這個過程非常簡單，只需兩個步驟。按照螢幕上的指示將 SeaChat 與您的 Google Calendar 整合。

首先，授權 SeaChat 連接您的 Google Calendar。接下來，設置工作時間，讓 SeaChat 助理知道何時安排預約。

## 會議邀請

一旦整合完成，您的 SeaChat 助理就可以代您預約會議。助理將向用戶發送會議邀請並自動將活動添加到您的 Google Calendar 中。客戶將直接收到助理發送的會議邀請。

然而，會議邀請的格式會根據所使用的助理類型而有所不同：

- **語音助理**: 包含日曆連結的 SMS 將發送到客戶的電話號碼。請注意，由於邀請不會通過電子郵件發送，客戶可能會忘記參加會議。因此建議再次致電提醒他們。

- **聊天助理**: 請確保在 SeaChat 中啟用了電子郵件收集功能，導航至 **頻道** → **網頁AI助理** → **客製表單**，新增或編輯現有表單，確保 **電子郵件** 欄位被標記為 **必填** 和 **啟用**。如果預約會議，日曆邀請將發送到所收集的電子郵件地址。

### 支援
需要協助？請聯繫我們：[seachat@seasalt.ai](mailto:seachat@seasalt.ai)。


---


#### Shopify

<!-- Source: seachat-manual/05-integrations/02-seachat-shopify-integration.md -->

<!-- Weight: 401 -->

*本指南將說明如何把SeaChat AI助理整合到您的Shopify商店中。將AI助理程式碼嵌入到Shopify模板的中，確保您可以輕鬆地增強您的電商平台功能。*


此頁教學將詳細說明嵌入整合SeaChat AI助理到您Shopify商店前端的過程。

## 步驟1：建立一個SeaChat帳戶
如果您還沒有SeaChat帳戶， 您可以在 [SeaChat網站](https://chat.seasalt.ai/)免費註冊！ 然後您可以將訓練好的AI助理，移至您的Shopify網站上。

## 步驟2：開啟Shopify
前往您的Shopify儀表板，從選單中點擊「Online Store」。

<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step1.png" alt="前往您的Shopify儀表板，並從選單中點擊 Online Store。">

## 步驟3：在Shopify上編輯程式
點擊您目前主題旁邊的刪節號圖標<mark>•••</mark>，選擇「Edit Code」並開始編輯。

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step2.png" alt="點擊您目前主題旁邊的刪節號圖標並選擇 Edit Code 開始編輯。">

## 步驟4：點擊theme.liquid
點擊左側面板上的「</> theme.liquid」。

<img width="40%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step3.png" alt="在左側面板上點擊 theme.liquid。">

## 步驟5：複製SeaChat程式代碼
您需要登入SeaChat才能查看此程式片段。您可至[SeaChat](https://chat.seasalt.ai/)免費註冊。在SeaChat儀表板的工作區內找到「AI助理配置」->「頻道」，並在Shopify頻道下，來取得所需的程式片段。

將從Seachat上的Shopify整合設置中獲得的SeaChat程式片段貼上到<head>。您可以在開頭的<head>標籤和結尾的</head>標籤之間的任何位置貼上它。

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step4.png" alt="將SeaChat程式片段貼到 head 標籤內。您可以將它貼到 <head> 和 </head> 之間的任何位置。">

## 步驟6：儲存並預覽

點擊右上方的「Save」按鈕。接著點擊「Preview Store」來測試AI助理。當您準備好時，記得再次啟動商店！

**非常重要**: 如果你想要設定網頁助理的外觀和樣式，請前往「頻道」->「網頁AI助理」->「基本設置」。在設定好外觀和樣式後，你的所有網頁將共享相同的設計。

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step5.png" alt="點擊右上角的 Save 按鈕，然後點擊 Preview Store 測試AI助理。當您準備好時，記得重新啟動商店！">

## 步驟7：（Optional）移除其他聊天機器人
請移除任何其他的聊天機器人服務，如Shopify Inbox，以避免混淆。Shopify的用戶們，請將您網站的自定頁面切換成禁用「Apps embeds」。最後，如果您之前的聊天機器人服務是通過程式嵌入整合的，請小心移除。

### 協助支援
需要協助？歡迎聯絡我們 [seachat@seasalt.ai](mailto:seachat@seasalt.ai).


---


#### Squarespace

<!-- Source: seachat-manual/05-integrations/03-seachat-squarespace-integration.md -->

<!-- Weight: 402 -->

*本指南將引導您將SeaChat AI助理整合到Squarespace網站的每個步驟，例如在Squarespace上進行程式碼注入，以及如何自定AI助理的設定等等。*


此頁教學將詳細說明嵌入整合SeaChat AI助理到您Squarespace網站的過程。

## 步驟1：創建一個SeaChat帳戶
如果您還沒有SeaChat帳戶， 您可以在 [SeaChat網站](https://chat.seasalt.ai/)免費註冊！ 然後您可以將構建好的AI助理，移至您的Squarespace網站上。


## 步驟2：開啟Squarespace
前往您的Squarespace網站的儀表板上。在側邊選單上選擇「Website」。

<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step1.png" alt="SeaChat | 前往您的Squarespace儀表板，並從選單中點擊 Website。">


## 步驟3：開啟網站工具
接著，在側邊選單中選擇「Website Tools」。


<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step2.png" alt="SeaChat | 在Squarespace上點擊 Website Tools。">

## 步驟4：開啟程式注入
在側邊選單中選擇「Code Injection」。


<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step3.png" alt="SeaChat | 在側邊選單中選擇 Code Injection。">


## 步驟5：複製SeaChat程式代碼
您需要登入SeaChat才能查看此程式片段。您可至[SeaChat](https://chat.seasalt.ai/)免費註冊。在SeaChat儀表板的工作區內導航至「AI助理配置」->「頻道」，並在Squarespace頻道下，來取得所需的程式片段。

從Seachat上的Squarespace整合設置中取得的SeaChat程式片段，並貼上到HEADER文本框中。記得按「Save」。

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step4.png" alt="SeaChat | 將SeaChat程式碼片段貼到HEADER文本框中，記得點擊 SAVE。">

## 步驟6：儲存並預覽

使用Squarespace上的「Preview」功能來測試AI助理。當您準備好時，記得重新啟動網站！

**非常重要**: 如果您想要配置小工具的樣式，請前往「頻道」->「網頁AI助理」->「基本設置」。您的AI助理將在您的網頁聊天掛件頻道中共享相同的樣式。

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step5.png" alt="SeaChat | 在網站上預覽SeaChat助理。">


## 步驟7：（Optional）移除其他聊天機器人

請移除任何其他的聊天機器人服務，以避免混淆。如果您之前的聊天機器人服務是通過程式嵌入整合的，請小心從「Code Injection」部分移除。

### 協助支援
需要協助？歡迎聯絡我們 [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 

---


#### Wix

<!-- Source: seachat-manual/05-integrations/04-seachat-wix-integration.md -->

<!-- Weight: 403 -->

*學習如何將SeaChat AI助理整合到您的Wix網站的每一步。從註冊SeaChat帳戶到程式碼嵌入和元件調整，確保您的AI助理在網站上無縫運行。*


此頁教學將詳細說明嵌入整合SeaChat AI助理到您Wix網站的過程。

## 步驟1：創建一個SeaChat帳戶
如果您還沒有SeaChat帳戶， 您可以在 [SeaChat網站](https://chat.seasalt.ai/)免費註冊！ 然後您可以將構建好的AI助理，移至您的Wix網站上。


## 步驟2：開啟Wix
前往您的Wix網站的儀表板上。在右上角選單選擇「Design Site」。

<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step1.png" alt="SeaChat | 前往您的Wix儀表板，並從右上角選單中點擊 Design Site。">

## 步驟3：開啟網站工具
接著，在側邊選單中選擇「Add Elements」。

<img width="50%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step2.png" alt="SeaChat | 在Wix上點擊 Add Elements。">

## 步驟4：開啟程式注入
在側邊選單中選擇「Embed Code」 -> 「Embed HTML」。

<img width="50%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step3.png" alt="SeaChat | 選擇 Embed Code 然後 Embed HTML。">


## 步驟5：複製SeaChat程式代碼
您需要登入SeaChat才能查看此程式片段。您可至[SeaChat](https://chat.seasalt.ai/)免費註冊。在SeaChat儀表板的工作區內導航至「AI助理配置」->「頻道」，並在Wix頻道下，來取得所需的程式片段。

從Seachat上的Wix整合設置中取得的SeaChat程式片段，並貼上到文本框中。記得按「Update」。

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step4.png" alt="SeaChat | 將SeaChat程式片段貼到HEADER文本框中。記得點擊 SAVE。">

## 步驟6：調整嵌入元件大小

調整嵌入元件的大小，以保證對話開啟後網頁上保留足夠空間給對話框。我調整大小為`W: 700, H:600`。調整大小過後，將元件拖曳到你喜歡的地方，一般來說會放在網頁右下角。

<img width="80%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step5.png" alt="SeaChat | 調整聊天元件大小">


## 步驟7：固定元件位置

我們建議固定SeaChat元件的位置，以便在訪客滾動頁面時元件不會到處移動。選擇SeaChat元件 > 右鍵點擊 > 選擇「Pin to Screen」。然後此組件將固定在角落並浮動。

<img width="60%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-pin-to-screen.png" alt="SeaChat | 調整聊天元件位置">

您可以調整邊距。我們建議將垂直(Vertial)和水平(horizontal)設置都設為20。

<img width="60%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-offset-margin.png" alt="SeaChat | 調整聊天元件邊距">


 ## 步驟8：儲存並預覽

使用Wix上的「Preview」功能來測試AI助理。當您準備好時，記得重新啟動網站！

**非常重要**: 如果您想要配置小工具的樣式，請前往「頻道」->「網頁AI助理」->「基本設置」。您的AI助理將在您的網頁聊天掛件頻道中共享相同的樣式。

<img width="60%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step6.png" alt="SeaChat | 在網站上預覽SeaChat助理。>


## 步驟8：（Optional）移除其他聊天機器人

請移除任何其他的聊天機器人服務，以避免混淆。如果您之前的聊天機器人服務是通過程式嵌入整合的，請小心移除。

### 協助支援
需要協助？歡迎聯絡我們 [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 

---


#### MailerLite

<!-- Source: seachat-manual/05-integrations/05-seachat-mailerlite-integration.md -->

<!-- Weight: 404 -->

*將 SeaChat 與 MailerLite 整合，讓表單自動將客戶信箱加入郵件名單。學習如何產生 API 金鑰以進行郵件行銷。*


本頁將詳細說明如何將 MailerLite 與 SeaChat 整合。完成整合後，您可以利用 SeaChat 表單自動收集客戶信箱與資訊，並自動加入 [MailerLite](https://www.mailerlite.com/) 郵件名單。

如需視覺化教學，請參考下方影片：<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/xTnJ9L1sVC4?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## 步驟 1：建立 SeaChat 帳戶
如果您尚未擁有 SeaChat 帳戶，可前往 [SeaChat 網站](https://chat.seasalt.ai/) 免費註冊！註冊後即可建立 AI 助理並整合 MailerLite。

## 步驟 2：開啟「Integrations」
進入 MailerLite 後台，於左側選單點選「Integrations」。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 50%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/add-mailerlite-integrations.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/add-mailerlite-integrations.png" alt="前往 Mailerlite 後台並點選 Integrations。">
</a>
</div>
</div>

## 步驟 3：選擇「API」
點擊「Use」選擇「API」。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/select-mailerlite-api.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/select-mailerlite-api.png" alt="在 MailerLite 選擇 API">
</a>
    <p style="margin-top: 20px; font-size: 15px">在 MailerLite 產生新金鑰
</div>
</div>

## 步驟 4：產生新金鑰
點擊「Generate new token」。為此 API 金鑰命名，並同意 API 金鑰規範後，點擊「Create token」。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/generate-new-token-mailerlite.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/generate-new-token-mailerlite.png" alt="在 MailerLite 產生新金鑰">
</a>
    <p style="margin-top: 20px; font-size: 15px">在 MailerLite 產生新金鑰
</div>
</div>

<br>

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/give-api-token-name-mailerlite.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/give-api-token-name-mailerlite.png" alt="為新金鑰命名">
</a>
    <p style="margin-top: 20px; font-size: 15px">為新金鑰命名
</div>
</div>

## 步驟 5：複製 API 金鑰
請妥善保存您的 API 金鑰，然後回到 SeaChat 的 MailerLite 整合頁面完成整合。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/copy-and-save-mailerlite-api-key.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/copy-and-save-mailerlite-api-key.png" alt="複製並保存 MailerLite API 金鑰">
</a>
    <p style="margin-top: 20px; font-size: 15px">複製並保存 MailerLite API 金鑰
</div>
</div>

## 步驟 6：（選填）查找 Group ID
若您希望將聯絡人加入特定 MailerLite 群組，可於「Developer API」頁面底部查詢所有 Group ID。提示：可將聯絡人加入多個群組。

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/get-mailerlite-group-id.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/get-mailerlite-group-id.png" alt="查找 MailerLite 群組 ID">
</a>
    <p style="margin-top: 20px; font-size: 15px">查找 MailerLite 群組 ID
</div>
</div>

### 支援
需要協助？請聯絡 [seachat@seasalt.ai](mailto:seachat@seasalt.ai)。


---


#### Wordpress

<!-- Source: seachat-manual/05-integrations/06-seachat-wordpress-integration.md -->

<!-- Weight: 405 -->

*學習如何將SeaChat AI助理整合到Wordpress網站，用線上AI聊天機器人跟你的網站訪問者即時對話，線上客服24小時在線服務。*


此頁教學將詳細說明嵌入整合SeaChat AI助理到 Wordpress 網站的過程。

## 步驟1：創建一個SeaChat帳戶

如果您還沒有SeaChat帳戶， 您可以在 [SeaChat網站](https://chat.seasalt.ai/)免費註冊！ 然後您可以將構建好的AI助理，移至您的 Wordpress 網站上。

## 步驟2：開啟Wordpress

前往您的 Wordpress 網站的儀表板。在右方選單選擇「外觀」。

<img width="100%" style="border-radius: 0.4rem" src="/images/seachat/zh/integrations/wordpress/wordpress-seachat-dashboard.png" alt="前往您的 Wordpress 網站的儀表板。在右方選單選擇「外觀」。">

## 步驟3：複製SeaChat程式代碼

您需要登入SeaChat才能查看此程式片段。您可至[SeaChat](https://chat.seasalt.ai/)免費註冊。在SeaChat儀表板的工作區內導航至「AI助理配置」->「頻道」，並在Wordpress頻道下，來取得所需的程式片段。

從Seachat上的Wordpress 第三方整合設置中複製SeaChat程式片段。

## 步驟4：打開「佈景主題檔案編輯器」並貼上SeaChat程式碼

打開左方功能選單的「佈景主題檔案編輯器」 -> 右方選單的「Theme Footer」。在程式碼中貼上SeaChat程式碼（在`<body>`和`</body>`之間。最後，點擊「更新檔案」。

<img width="100%" style="border-radius: 0.4rem" src="/images/seachat/zh/integrations/wordpress/wordpress-seachat-add-widget-code.png" alt="打開「佈景主題檔案編輯器」並貼上SeaChat程式碼">

## 步驟5：預覽

## 步驟8：儲存並預覽

現在訪問你的網站，即可看到SeaChat網頁聊天機器人在右下角。

**非常重要**: 如果您想要配置小工具的樣式，請前往「頻道」->「網頁AI助理」->「基本設置」。您的AI助理將在您的網頁聊天掛件頻道中共享相同的樣式。

## 排障提醒：SeaChat 小工具未在網頁載入？

如果您使用的 WordPress 最佳化外掛會消除 render-blocking CSS，請注意，這可能會導致 SeaChat 網頁聊天小工具無法正常載入您的網站。

#### **🔍 原因**

某些最佳化外掛可能會延遲或移除關鍵 CSS，這可能影響 SeaChat 小工具的呈現方式，導致以下問題：

- 小工具無法顯示在您的網站上。
- 聊天小工具出現異常的 UI 問題。

#### **🛠️ 修復方法**

如果您啟用了效能最佳化外掛，請按照以下步驟操作：

1. 檢查您的外掛設定是否包含 「消除 Render-Blocking CSS」 或 「最佳化 CSS 傳遞」 選項。
2. 停用此特定最佳化設定，以防影響聊天小工具的正常運作。
3. 清除快取並重新載入您的網站，以確保聊天小工具能夠正確運作。

#### **外掛示例: WP Rocket**

我們以 **WP Rocket** 這款廣泛使用的網站效能最佳化外掛為例。在 **「檔案最佳化」**（File Optimization）標籤下，請勿勾選 **「最佳化 CSS 傳遞」**（Optimize CSS Delivery）選項，以確保 SeaChat 網頁聊天小工具能順利載入。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image2.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wordpress/wordpress-seachat-wp_rocket.png" alt="WP Rocket Settings">
</a>
</center>

<br/>

如果您需要進一步協助，歡迎隨時聯絡 [seachat@seasalt.ai](mailto:seachat@seasalt.ai).！🚀


---


#### SeaX 與 SMS & 語音通話整合

<!-- Source: seachat-manual/05-integrations/07-seax-integration-sms-calll-in-seachat.md -->

<!-- Weight: 406 -->

*將 SeaX 與 SeaChat 整合，實現大量簡訊發送與自動語音通話處理。用 AI 自動化客戶溝通。*


## 概述

本教學將帶您完成在 SeaChat 中設置 Seasalt 大量訊息平台 SeaX 的流程。SeaX 是一個強大的全通路平台，讓您能在單一介面管理所有業務通路。

更多資訊請參閱 [SeaX 文件](https://wiki.seasalt.ai/seax/seax-messaging/bulk-messaging-features/)。

整合 SeaX 至 SeaChat 後，您不僅能手動管理客戶對話，還能讓 SeaChat AI 智能客服自動回覆。SeaX 整合所有業務通路（如 WhatsApp、電話、SMS），並將這些通路導向 SeaChat 進行 AI 驅動的回應。

## SeaX 大量通話/發送

SeaX 為您的 AI 智能客服提供與客戶溝通的通道。完成與 SeaChat 的整合後，您即可透過 SeaX 向客戶發送大量訊息。

SeaChat 與 SeaX 無縫協作執行大量訊息發送。SeaX 會依序撥打名單上的每位客戶（約每秒一通）。當客戶接聽後，AI 智能客服會接手對話，您只需前往 **Conversations** 儀表板查看對話內容。

SeaChat 並不知曉您撥打的客戶名單，也無法主動發起通話。SeaChat 僅在對話啟動後負責對話內容；SeaX 則負責發起通話與發送訊息。

您可建立 **活動（Campaigns）**，向客戶發送 SMS 或語音留言。這些活動將透過 SeaX 發送，並由 SeaChat 上的專屬 AI 智能客服處理後續對話。

## 外撥通話活動

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/call-integration.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/call-integration.png" alt="Outbound/ Inbound Calls Integration">
    </a>
<br/>
    <p style="font-size: 15px">外撥/來電整合</p>
</div>
</div>

外撥通話是主動聯繫客戶的有效方式。透過 SeaX，您可自動化這些通話。

1. **語言選擇**：選擇語言及對應模型。建議使用 SeaVoice，穩定且適合正式環境。
2. **語音選擇**：選擇偏好的語音，並可點擊播放鍵預聽。
3. **外撥開場訊息**：當客戶接聽時，將播放此訊息，AI 智能客服隨後接手對話。您可於 **Conversations** 儀表板查看對話內容。

## 來電整合

來電是提供客戶服務的可靠方式。AI 智能客服可接聽來電並擔任語音接待員。

設定步驟與[外撥通話整合](#outbound-calls-integration)相同，包含語言、語音與問候語設置。

## SMS 整合

SMS 是行銷推廣的有效工具。發起或接收 SMS 對話都很簡單，只需設定開場訊息，AI 智能客服會自動處理後續對話。

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/sms.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/sms.png" alt="SMS Setup">
    </a>
<br/>
    <p style="font-size: 15px">SMS 設定</p>
</div>
</div>

## 測試整合

完成 SeaX 與 SeaChat 的整合後，您可透過發送訊息給 SeaChat AI 智能客服來測試。建議在正式大量發送前，先於各頁面使用指定按鈕進行本地測試。

測試無誤後，即可開始透過 SeaX 向客戶大量發送訊息，並由 SeaChat 智能客服接手後續對話。

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/find-seax.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/find-seax.png" alt="SeaX Messages in SeaChat">
    </a>
<br/>
    <p style="font-size: 15px">SeaX 訊息於 SeaChat</p>
</div>
</div>

## :dart: 疑難排解

1. **來電與 SMS 無可用號碼，如何正確設定？**

<div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <a href="/images/seachat-integrations/seax/no-phone-available.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/no-phone-available.png" alt="No Phone Available Warning">
    </a>
<br/>
    <p style="font-size: 15px;">無可用號碼警告</p>
</div>
</div>

如出現上述警告，表示您需為 AI 智能客服提供一組電話號碼，讓其作為管理來電與 SMS 的通道。當有人撥打此號碼或發送 SMS，AI 智能客服將自動處理對話。

請先於 SeaX 設定，並先向 SeaChat 智能客服發送一次外撥通話或 SMS。詳細操作請參閱 [SeaX 文件](https://wiki.seasalt.ai/seax/seax-messaging/bulk-messaging-features/)。

具體步驟：

1. SeaX -> 外撥通話給智能客服 -> 設定客服來電號碼
2. SeaX -> 外撥 SMS 給智能客服 -> 設定客服 SMS 號碼

如不確定智能客服是否已收到通話或 SMS，可於 **Conversations** 儀表板查詢對話紀錄。


---


#### Voice AI大規模外撥電話與自動來電處理

<!-- Source: seachat-manual/05-integrations/08-seax-integration-bulk-phone-calls.md -->

<!-- Weight: 407 -->

*將 SeaX 與 SeaChat 整合，實現大規模電話外撥與來電自動化。用 AI 自動化客戶語音溝通。*




## 概述

[SeaX](https://seax.seasalt.ai) 讓企業能夠利用 AI 智能客服進行大規模外撥與來電活動。整合 SeaChat 後，SeaX 不僅可自動外撥（如問卷、客戶聯繫），還能 24/7 由 AI 智能客服接聽來電。這項整合非常適合希望自動化語音互動、提升客戶參與度並確保每通來電都能被即時處理的企業。

## 🎥 教學影片

下方影片將完整示範如何設定與使用 SeaX 電話外撥與 AI 來電處理。

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/An4n8JhhdvA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

## 主要功能

**大規模外撥電話：**  
直接從 SeaX 發起數百或數千筆外撥電話活動。可用 AI 智能客服自動執行問卷、訪談或通知。

**AI 來電自動接聽：**  
設定 AI 智能客服 24 小時自動接聽來電，隨時即時回覆客戶問題。

**統一管理介面：**  
於單一 SeaX 介面管理所有外撥/來電活動、電話號碼與 AI 智能客服。SeaX 與 SeaChat 智能客服同步，設定更簡單。

**即時語音轉錄與摘要：**  
自動將通話內容轉錄並產生摘要，方便回顧互動紀錄與萃取重點。


## 先決條件

- 需有 SeaX 與 SeaChat 帳號。
- 至少在 SeaX 配置一組電話號碼（市話或免付費）。
- 具備管理員權限以設定整合與 AI 智能客服。

## 步驟說明

### 1. 指派並設定電話號碼

- 登入 SeaX，前往 **Workspace → Numbers**。
- 選擇或新增一組用於外撥/來電的電話號碼。
- 點擊該號碼的 **Edit**。
- 啟用 **AI Agent to answer the phone** 選項。
- 指派 SeaChat 工作區的 AI 智能客服來接聽來電。

### 2. 同步 AI 智能客服

- 確認 SeaX 與 SeaChat 工作區已同步。
- 所有在 SeaChat 建立的 AI 智能客服都可於 SeaX 指派，確保跨通路行為一致。

### 3. 設定來電自動接聽

- 在 SeaChat 前往 **Integrations**，選擇電話整合。
- 將電話號碼連結至指定 AI 智能客服。
- 設定語言、語音（如「Jessica」TTS）與來電問候語。
- 儲存設定。

### 4. 測試來電

- 撥打測試電話至設定號碼。
- AI 智能客服會以預設問候語接聽，並依設定回覆問題。
- 通話轉錄與摘要可於 SeaX 與 SeaChat 查閱。

### 5. 設定外撥電話活動

- 在 SeaX 前往 **Bulk Send/Call** 或 **Campaigns**。
- 選擇已啟用電話的號碼。
- 匯入或選擇聯絡人名單（避免重複）。
- 設定 AI 智能客服的外撥腳本或問卷（如招募活動的面試問題）。
- 排程或啟動外撥活動。AI 智能客服將依設定逐一撥打並對話。
- 即時監控活動進度，並於系統中查閱通話摘要與回覆內容。

### 6. 管理來電回撥

- 若收件人回撥未接來電，AI 智能客服（或另行設定者）會自動接聽並延續對話。
- 所有來電/外撥資料、轉錄與摘要皆可於 SeaX 與 SeaChat 查閱。

## 多號碼管理

SeaX 支援多組電話號碼，可用於不同活動或部門。可依需求指派不同 AI 智能客服，並於統一介面集中管理。

## 最佳實踐

**避免重複聯絡人：**  
請確保每個電話號碼僅出現在名單一次，避免重複撥打。

**活動內容個人化：**  
根據活動目的（如問卷、預約提醒、客戶通知）調整外撥腳本，提升互動效果。

**監控與檢視：**  
善用 SeaX 報表工具追蹤通話發送、回覆率與活動成效，並定期檢查通話轉錄與摘要以確保品質。

**遵循法規：**  
請遵守自動撥號相關電信法規，並確保收件人已同意接聽來電。

## 疑難排解

- 若 AI 未能接聽來電，請確認該電話號碼已在 SeaX 與 SeaChat 正確連結至 AI 智能客服。
- 若外撥有問題，請檢查聯絡人名單格式並確保無重複。
- 請確認您的電話號碼已在 SeaX 配置並啟用。

## 支援

如需協助，請聯絡 Seasalt AI 支援：seachat@seasalt.ai。


---


#### SeaX 與 WhatsApp 整合

<!-- Source: seachat-manual/05-integrations/09-seax-integration-whatsapp-in-seachat.md -->

<!-- Weight: 408 -->

*將 SeaX 與 SeaChat 整合，實現 WhatsApp 大量訊息發送與 AI 自動化客戶溝通。*


## 概述

[SeaX](https://seax.seasalt.ai) 讓企業能夠高效發送 WhatsApp 大量訊息，並管理大規模客戶互動活動。當與 SeaChat 整合後，SeaX 不僅可進行大規模外發訊息，還能利用 AI 自動回覆客戶來訊。此整合同時優化外發活動與來訊支援，特別適合處理高訊息量或希望自動化客戶互動的組織。

## 🎥 教學影片
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/WUwn2QoeBGA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## 主要功能

- **WhatsApp 大量訊息發送：** 直接從 SeaX 向大量 WhatsApp 聯絡人發送廣播訊息。
- **AI 自動回覆：** SeaChat 可自動接手來訊，利用先進語言模型自動回覆。
- **真人客服接管：** 隨時可在 AI 與真人客服間切換，提供個人化支援。
- **統一管理：** 於單一 SeaX 介面管理多個 WhatsApp 商業帳號與活動。
- **合規性：** 確保所有收件人均已同意接收 WhatsApp 訊息，符合 WhatsApp 政策。

---

## 先決條件

- 具備 API 權限的 WhatsApp 商業帳號。
- SeaX 與 SeaChat 帳號。
- 具備 Meta Business Suite 管理員權限以整合 WhatsApp。

---

## 步驟說明

### 1. 將 WhatsApp 連接至 SeaX

1. 於 SeaX 的 **Workspace** 下點選 **Channels**。
2. 選擇 **WhatsApp Business Platform**，依畫面指示以 Meta Business Suite 帳號連接 WhatsApp 商業帳號。
3. 連接成功後，WhatsApp 帳號將顯示於 SeaX Workspace 的 Channels。

### 2. 設定大量訊息發送

1. 前往 SeaX 的 **Conversations** 或 **Bulk Send/Call** 區塊。
2. 選擇已啟用 WhatsApp 的號碼並撰寫廣播訊息。
3. 匯入或選擇聯絡人清單，確保所有收件人均已同意接收訊息。
4. 發送或排程廣播，SeaX 將訊息發送至所有選定聯絡人。

### 3. 整合 SeaChat 以自動回覆

1. 於 SeaChat 前往 **Agent Configuration → Integrations**。
2. 啟用 WhatsApp 整合並連結至 SeaX 帳號。
3. 將用於大量訊息的 WhatsApp 號碼指派給 SeaChat AI Agent。
4. 回到 SeaX，編輯 WhatsApp 號碼設定並啟用「AI Agent 回答 WhatsApp」。
5. 儲存設定。

### 4. 測試整合

- 向您的商業 WhatsApp 號碼發送測試訊息。
- 確認來訊已由 SeaChat AI Agent 自動處理。
- 真人客服可隨時進入對話或點選「接管」按鈕接手。

---

## 管理多個 WhatsApp 帳號

SeaX 支援多個 WhatsApp 商業帳號管理。可於 **Channels → Add Account** 新增帳號，集中管理所有號碼與客服。可依需求指派不同客服給不同帳號，並於統一介面監控所有活動。

---

## 真人客服接管

如遇需真人介入的客戶問題，客服可隨時從 AI 手中接管。可手動觸發，或由客戶輸入指令（如 `/live_agent`）請求。轉接過程無縫，除非另行告知，客戶無法分辨對話對象為 AI 或真人。

---

## 最佳實踐

- **取得同意：** 僅向已同意接收 WhatsApp 訊息的用戶發送大量訊息。
- **訊息個人化：** 利用變數與範本提升訊息互動率。
- **監控活動：** 善用 SeaX 報表工具追蹤發送、回覆率與活動成效。
- **維持合規：** 遵循 WhatsApp 商業訊息政策，避免帳號受限。

---

## 疑難排解

- 請確保 WhatsApp API 整合使用永久存取權杖。
- 確認 WhatsApp 應用已設為 Live 模式。
- 檢查 Webhook 權限設定，確保訊息可正常發送與接收。
- 若自動回覆無法運作，請確認 WhatsApp 號碼已正確連結至 SeaX 與 SeaChat。

---

## 支援

如需協助，請聯絡 Seasalt AI 支援：seachat@seasalt.ai。


---


#### 以程式設計方式在 WebChat 中預先填寫聯絡表格

<!-- Source: seachat-manual/05-integrations/10-seachat-prefill-contact-forms.md -->

<!-- Weight: 409 -->

*SeaChat 支援透過偵測網路聊天 URL 中的查詢字串來預先填入網路聊天表單中使用者資訊。這允許您的網站和聊天小部件之間的無縫集成，您的客戶不需要手動輸入他們的詳細資訊。*


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
- **帳戶ID:** 9876

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


---


### 設定SeaChat語言和外觀

<!-- Source: seachat-manual/07-appearance-setting.md -->

<!-- Weight: 500 -->

*探索如何定義您的SeaChat AI助理的語言和外觀。這個指南將帶您了解如何在網頁助理的設定頁面中調整AI助理，以及如何調整其名稱和界面以符合您的品牌風格。*


你能夠指定AI助理使用的主要語言，並且調整AI助理的名稱和外觀。在**網頁助理**的頁面你可以在相關欄位進行設定，把AI助理調成你想要的模樣。


<iframe width="100%" height="400" src="https://www.youtube.com/embed/-JidvSmTqUg?list=PL8K7_LTqly449uOg_uBWOPfFyL1fJRjkE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>


---


#### 如何測試和改善回答品質

<!-- Source: seachat-manual/07-test-and-improve-ai-agent/improve-agent.md -->

<!-- Weight: 501 -->

*了解如何有效測試並改善您的SeaChat AI助理的回答品質。透過本指南，您將學會如何精細調整知識庫，以確保AI助理能夠提供準確和有用的回應。*


加入知識之後，你可以開始測試你的AI助理，你可以準備一系列的問答題庫來模擬使用者可能會問的問題，並且參照答案來評斷AI助理是不是提供好的回覆。


<iframe width="100%" height="400"  src="https://www.youtube.com/embed/XciOXWI6e4c?list=PL8K7_LTqly449uOg_uBWOPfFyL1fJRjkE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  allowfullscreen style="border-radius: 30px;"></iframe>

---


#### 連上 SeaChat 後 - 成功營運的 SOP

<!-- Source: seachat-manual/07-test-and-improve-ai-agent/post-launch-sop.md -->

<!-- Weight: 502 -->

*連上 SeaChat 後，請遵循此標準作業程序 (SOP) 指南，以優化日常運營並改善團隊工作流程，提高工作效率。*


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
            <img style="width: auto; height: 200px; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/post-launch-sop/web-widget.png" alt="SeaChat | 網頁聊天小工具中的自定義表單">
        </a>
        <p style="margin-top: 20px; font-size: 15px">網頁聊天小工具中的自定義表單</p>
    </div>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/zh/post-launch-sop/web-widget-form.png" target="_blank" style="width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: auto; height: 200px; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/post-launch-sop/web-widget-form.png" alt="SeaChat | 網頁聊天小工具中的自定義表單">
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


---


#### 評估：透過測試集增強 AI智能助理響應準確性

<!-- Source: seachat-manual/07-test-and-improve-ai-agent/evaluation.md -->

<!-- Weight: 503 -->

*透過測試集增強 AI智能助理響應準確性*


## **1\. 概述**

SeaChat 中的 **評估** 功能可讓使用者透過將實際回應與預先定義的黃金回應進行比較來系統化測試其 AI智能助理程式的效能。它使用大型語言模型來評估測試集並分配正確性分數來確定反應品質。它可以幫助企業**監控、測試和改進**其AI智能助理的效能。

- 它透過將即時助理答案與黃金標準進行比較來確保高品質的回應。
- 使用者可以透過定期測試回應和調整知識庫內容來完善他們的AI智能助理模型。
- 與真實客戶對話的無縫整合允許用戶動態改進AI智能助理。

## **2\. 使用案例**

### **📌用例 1：AI智能助理程式回應的品質保證**

**電子商務公司**的客戶支援團隊希望確保他們的AI智能助理商提供**準確的退貨政策資訊**。

- 他們創建了一個**測試集**，其中包含**常見的退貨相關問題**。
- 他們根據公司政策輸入**黃金回應**。
- 測試運行後，他們發現 **30% 的反應不正確**。
- 他們更新**知識庫**並重新運行測試，提高AI智能助理的準確性。

✅ **結果：** AI智能助理現在提供 **正確的退貨政策答案**，減少 **客戶糾紛升級**。

---

### **📌用例 2：AI智能助理效能監控**

一家使用 SeaChat 的 SaaS 公司希望透過**產品故障排除查詢**追蹤 AI 效能。

- 每個月，他們都會執行**包含 100 多個常見問題的測試集**。
- 他們比較一段時間內的正確性分數以**跟踪改進**。
- 當分數下降時，他們會分析**錯誤的反應和知識庫差距**。

✅ **結果：** 主動監控可防止 **客戶滿意度下降** 並 **提高支援效率**。

---

### **📌用例 3：改進 AI智能助理程式以實現多語言支援**

一家**全球航空公司**想要測試其AI智能助理處理**不同語言的客戶查詢**的能力。

- 他們為**英語、西班牙語和法語**查詢建立測試集。
- 他們使用**由人工翻譯驗證的黃金回應**。
- 測試運行顯示AI智能助理在處理**法國航班重新安排查詢**時遇到困難。
- 他們改進**法語語言知識庫**並重新測試。

✅ **結果：**AI智能助理提供**準確的多語言支援**，減少**溝通不良**。

---

### **📌用例 4：訓練 AI智能助理程式以獲得行業特定知識**

**醫療保健提供者**使用 SeaChat **自動化患者常見問題解答**。

- 他們創建了一個**包含醫療保險問題的測試集**。
- 他們添加了**由醫療專業人員撰寫的黃金回應**。
- 測試結果顯示**關於覆蓋範圍限制的答案不一致**。
- 他們完善**AI智能助理描述和知識庫並重新運行測試**以確保正確性。

✅ **結果：**AI智能助理現在提供**可信的醫療指導**，確保**合規性和準確性**。

## **3\.如何設定**

### **第 1 步：導覽至「評估」標籤**

1. 登入**SeaChat**。
2. 點選左側邊欄中的**評估**標籤。

### **步驟 2：建立新的測試集**

1. 點選評估標籤中的 **三點選單** (⋮)。
2. 選擇**「新增測試集」**。
3. 輸入**測試集名稱**。
4. 設定 **單一測試樣本成功閾值** 和 **測試集成功閾值**（值介於 **0 和 1** 之間）。這些閾值決定響應是否正確。
5. 按一下**確認**建立測試集。

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/2add-a-new-set.png"  alt="Add a new set">
</a>

_點擊 +新增 以添加_

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/3new-set-input.png"  alt="Add new test configurations">
</a>

_配置被認為正確的集合名稱和閾值_

</center>

### **步驟 3：新增測試樣本**

1. 點選測試集中的 **「新增樣本」** 按鈕。
2. **配置測試樣本：**
   - **對話歷史記錄：** 新增與過去的 **使用者/助理訊息** 相關的上下文。
   - **使用者測試查詢：** 將測試的確切使用者訊息。
   - **黃金特工回應：** 用於比較的理想 AI 生成回應。
3. 按一下「**儲存**」以新增測試樣本。

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/4add-sample.png"  alt="Add a new test sample">
</a>

_範例：向問答測試集新增使用者測試查詢和助理黃金回應_

</center>

### **步驟 4：執行測試集**

1. 點擊測試集旁邊的**運行**圖標，然後點擊彈出視窗中的確認按鈕
2. 導覽至 **測試運行** 標籤以查看結果。

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/5run-set.png"  alt="Click Run button to run">
</a>

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/6confirm-run.png"  alt="Click Run button to run">
</a>

</center>

### **第 5 步：查看測試運行結果**

1. 在 **測試運行** 標籤中查看所有測試運行

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/7test-run-page.png"  alt="Navigate to Test Runs tab to view results">
</a>

</center>

<br/>

2. 點選已完成的測試運行即可查看：
   - 測驗集的**整體正確性分數**。
   - **每個測驗樣本的正確性分數**。
   - **實際 AI智能助理響應與黃金響應**。
   - AI智能助理引用的 **知識庫文章**。
3. 如果需要，**編輯知識庫文章**以改進AI智能助理回應。

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/8test-run-result.png"  alt="Click one item to view the results in detail">
</a>

\_範例：第一個查詢的正確性分數為 19.55%，第二個查詢的分數為 65.47%，整體正確性為 43.51%。

</center>

### **步驟 6：新增真實對話的測試樣本**

1. 在即時對話期間，如果 AI智能助理提供了有待改進或異常的回應，請按一下 **點贊/不喜歡** 按鈕。
2. 回覆將顯示在 **「需求審核」** 標籤下。
3. 按一下回應，然後選擇 **“+ 新增至測試集”**。
4. 選擇 **測試集名稱** 並配置：
   - **對話歷史記錄**
   - **使用者測試查詢**
   - **黃金特工回應**
5. 點選**儲存**。現在，測試樣本已添加到測試集中以供將來評估。
6. 重複**步驟 4 和步驟 5** 重新執行測試並完善AI智能助理回應。
   <br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/11needs-review-page.png"  alt="Click Add to Test Set button to add to a test set">
</a>

_範例：在需求審核頁面中，按一下 + 新增至測試集按鈕將助理回應新增至測試集_。

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/12add needs review message to a test set.png"  alt="Modify sample to be added to the test set">
</a>

_範例：新增使用者訊息並修改助理黃金回應，然後將此範例新增至問答測試集中。_

</center>

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/13new sample in test set.png"  alt="View the newly added test sample">
</a>

_範例：導覽至評估頁面，這條問題已新增至測試集中_。

</center>

## **3\.定價**

測試運行會消耗AI智能助理回應條數，並將相應地計費。測試集中的每個測試案例價格為 **$0.01美金**。

## **4\.匯入和匯出評估測試集**

有效管理評估測試集對於優化 AI 模型效能至關重要。該系統允許使用者**匯出**測試集以進行備份、編輯或共享，並**匯入**它們以進行批量更新。請依照下列說明**匯出**或**匯入**測試集。

### **使用案例**

匯入和匯出評估測試集在多種場景中都有好處，例如：

1. **資料備份和復原** - 定期匯出測試集以建立備份，確保不會遺失關鍵測試資料。
   - 如果評估測試集被意外刪除或修改，使用者可以透過匯入先前儲存的 JSON 檔案輕鬆恢復。
2. **協作和共享** - 從事 AI 模型評估的團隊可以透過將測試集匯出到 JSON 檔案並在不同環境中共享來共享測試集。
   - 當不同的團隊需要使用相同的測試案例驗證或基準測試 AI 模型時，這特別有用。
3. **批次管理和編輯** - 使用者可以**匯出**測試集，批次編輯JSON文件，然後**匯入**回系統，而不用手動逐一新增測試樣本。
   - 這加快了測試集的更新和修改，確保一致性並減少手動工作。
4. **跨環境遷移測試集** - 使用者可以透過從一個環境匯出測試集並將其匯入到另一個環境中，在**暫存、開發和生產環境**之間移動測試集。
   - 這確保了人工智慧模型在不同環境中得到一致的測試。
5. **AI 模型基準測試** - 使用者可以建立標準化測試集，以對 AI 模型隨時間的改進進行基準測試。
   - 匯出和匯入測試集允許重複使用相同的評估集來有效追蹤進度。

## **如何匯出評估測試集**

1. 導覽至 **評估** 標籤。
2. 點選要匯出的評估測試集旁邊的**三點選單** (⋮)。
3. 從下拉式選單中選擇 **匯出此集**。

<center>
<a href="/images/seachat/en/evaluation/export-import-menu.png">
<img height="100%" width="40%" src="/images/seachat/en/evaluation/export-import-menu.png"  alt="Option menu">
</a>

</center>

4. 將出現一個通知窗口，其中包含 JSON 檔案的連結。
5. 按一下連結 — 它將在新分頁中開啟 JSON 檔案。
6. 右鍵單擊新選項卡並選擇 **另存為** 以下載 JSON 檔案。

<center>
<a href="/images/seachat/en/evaluation/export-success.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/export-success.png"  alt="Export success message">
</a>

</center>

### **匯出的 JSON 檔案範例：**

```{
  "id": "baded98d44024b63964a866c5c1670d3",
  "name": "customerQ&A",
  "set_success_threshold": 0.8,
  "sample_success_threshold": 0.8,
  "samples": [
    {
      "id": "8be53adf616a451d8282a6455f3f346d",
      "user_test_query": "What products do you offer?",
      "agent_gold_response": "We offer SeaX Messaging, SeaMeet, SeaChat, SeaVoice (including Discord bot), and SeaX Enterprise contact center solution.",
      "conversation_history": { "messages": [] }
    },
    {
      "id": "a6455f3f346d8be53adf616a451d8282",
      "user_test_query": "I need to use it with LINE, do you support it?",
      "agent_gold_response": "Yes, SeaChat can be integrated with LINE to respond to customer messages effectively.",
      "conversation_history": {
        "messages": [
          { "role": "user", "content": "Tell me all about SeaChat" },
          {
            "role": "assistant",
            "content": "SeaChat is an AI-powered intelligent chatbot that automates responses to customer queries and transitions to human support when needed."
          }
        ]
      }
    }
  ]
}
```

## **如何從檔案匯入**

1. 導覽至 **評估** 標籤。
2. 點選**三點選單** (⋮) 並選擇 **「從檔案匯入」**。
3. 點選選擇 JSON 檔案或將其拖曳到上傳視窗中。
4. 上傳後，按一下 **「完成」** 完成該過程。

<center>
<a href="/images/seachat/en/evaluation/import-success.png">
<img height="100%" width="50%" src="/images/seachat/en/evaluation/import-success.png"  alt="Export success message">
</a>

</center>

### **用於匯入的範例 JSON 檔案：**

```{
  "name": "customerQ&A",
  "set_success_threshold": 0.8,
  "sample_success_threshold": 0.8,
  "samples": [
    {
      "user_test_query": "What products do you offer?",
      "agent_gold_response": "We offer SeaX Messaging, SeaMeet, SeaChat, SeaVoice (including Discord bot), and SeaX Enterprise contact center solution.",
      "conversation_history": { "messages": [] }
    },
    {
      "user_test_query": "I need to use it with LINE, do you support it?",
      "agent_gold_response": "Yes, SeaChat can be integrated with LINE to respond to customer messages effectively.",
      "conversation_history": {
        "messages": [
          { "role": "user", "content": "Tell me all about SeaChat" },
          {
            "role": "assistant",
            "content": "SeaChat is an AI-powered intelligent chatbot that automates responses to customer queries and transitions to human support when needed."
          }
        ]
      }
    }
  ]
}
```

如果您需要進一步協助，請隨時聯絡[seachat@seasalt.ai](mailto:seachat@seasalt.ai)！ 🚀


---


#### 客制GPT工具

<!-- Source: seachat-manual/09-automation/gpt-tools.md -->

<!-- Weight: 600 -->


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

* 接受用戶上傳的圖像文件
* 通過您的 API 端點處理這些圖像
* 可選：以帶有增強描述的可自定義卡片格式顯示結果

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

### 步驟 4（可選）：帶有描述的卡片設置

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

<center>
<a href="/images/seachat/zh/gpt-tools/image-tool-example.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/image-tool-example.png"  alt="圖片搜尋卡片顯示">
</a>

<br/>

*範例：用戶上傳圖像後，工具返回基於上傳圖像的響應。*

</center>


## 額外訊息設定

**額外訊息設定** 此部分適用於所有搜尋和顯示工具和圖片搜尋工具，允許您配置工具成功執行後應發送的額外訊息。每當您的 AI 助理使用客制 GPT 工具執行後的 API 回應進行回覆時，這些訊息會自動發送。此功能使您能夠在工具執行後提供後續指導、行動呼籲或其他資訊。

### 概述

額外訊息設定支援三種不同的訊息格式：

* **純文字**：發送簡單的文字訊息
* **卡片**：發送帶有圖片和按鈕的豐富卡片
* **按鈕**：發送不含圖片的按鈕

### 配置步驟

#### 步驟 1：存取額外訊息設定

建立或編輯客制 GPT 工具時，向下滾動找到**額外訊息設定**部分。

#### 步驟 2：選擇訊息類型

從三種可用的訊息類型中選擇：

**純文字訊息：**

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/extra_message_text.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/extra_message_text.png"  alt="額外訊息純文字配置">
</a>

<br/>

*配置工具執行後發送的純文字訊息*

</center>

**卡片訊息（帶圖片和按鈕）：**

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/extra_message_card.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/extra_message_card.png"  alt="額外訊息卡片配置">
</a>

<br/>

*配置帶有圖片和按鈕的豐富卡片訊息*

</center>

**僅按鈕訊息：**

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/extra_message_buttons.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/extra_message_buttons.png"  alt="額外訊息按鈕配置">
</a>

<br/>

*配置用於快速操作的僅按鈕訊息*

</center>

#### 步驟 3：配置訊息內容

**對於純文字訊息：**
- 在訊息欄位中輸入您想要的文字
- 您可以根據需要包含佔位符或動態內容

**對於卡片訊息：**
- **標題**：為您的卡片輸入標題
- **描述**：為卡片添加描述性文字
- **圖片 URL**：提供卡片圖片的 URL
- **按鈕**：配置按鈕文字和URL

**對於僅按鈕訊息：**
- **按鈕**：添加一個或多個具有自定義文字和操作的按鈕
- 每個按鈕可以連接到 URL

#### 步驟 4：保存並測試

配置額外訊息設定後，保存您的客制 GPT 工具配置。額外訊息現在將在您的工具在對話中執行時自動發送。

### 使用範例

以下是額外訊息在實際對話中出現的範例：

**純文字範例：**

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/extra_message_example_text.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/extra_message_example_text.png"  alt="純文字額外訊息範例">
</a>

<br/>

*範例：工具執行後提供額外指導的純文字額外訊息*

</center>

**卡片範例：**

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/extra_message_example_card.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/extra_message_example_card.png"  alt="卡片額外訊息範例">
</a>

<br/>

*範例：帶有圖片和操作按鈕的豐富卡片額外訊息*

</center>

**按鈕範例：**

<br/>

<center>
<a href="/images/seachat/zh/gpt-tools/extra_message_example_buttons.png">
<img height="100%" width="100%" src="/images/seachat/zh/gpt-tools/extra_message_example_buttons.png"  alt="按鈕額外訊息範例">
</a>

<br/>

*範例：用於快速用戶操作的基於按鈕的額外訊息*

</center>

### 使用場景

額外訊息設定特別適用於：

* **後續操作**：在檢索資訊後提供下一步操作
* **行動呼籲**：鼓勵用戶採取特定行動
* **額外資源**：提供相關連結或資源
* **反饋收集**：添加快速反饋按鈕
* **導航**：幫助用戶探索更多選項

### 最佳實踐

* 保持額外訊息簡潔並與工具功能相關
* 對於受益於圖片的視覺豐富內容使用卡片
* 對於明確的行動呼籲或導航選項使用按鈕
* 測試您的額外訊息以確保它們為用戶體驗提供價值
* 在設計額外訊息時考慮工具將使用的上下文


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

* **工具執行限制**：SeaChat 每個傳入的用戶消息最多激活一個啟用的 GPT 工具。這包括與日曆或實時代理轉接的任何集成，確保為每個對話選擇最相關的工具。


---


#### 自動標記

<!-- Source: seachat-manual/09-automation/auto-labeling.md -->

<!-- Weight: 601 -->

*了解如何設定和使用 自動標記功能，以自動化和簡化對話標籤化的過程。*


---

## 影片教學

<iframe width="100%" height="400" src="https://www.youtube.com/embed/2lZcfofYQj4?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  allowfullscreen style="border-radius: 30px";></iframe>

---

**簡介**  
自動標記是 Seasalt.ai 工具套件整合中的重要組成部分。此功能能夠智能且自動地將標籤應用於對話，簡化了如客戶服務和醫療保健等使用場景的流程。

我們歡迎您查看我們的 [標籤自動化](https://wiki.seasalt.ai/zh/seachat/manual/labeling/label-automation/) 功能，以實現基於自動標記的更高級工作流程。

**什麼是自動標記**  
自動標記是一個系統，能根據預定義規則和 AI 驅動的分析自動將標籤應用於對話或其他數據點。用戶無需手動標記，可設置條件在符合規則時動態添加或移除標籤。

---

## 主要功能


<center>
<a href="/images/seachat/en/labeling/auto-labeling/auto-labeling-feat-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/auto-labeling-feat-ui.png"  alt="自動標記介面概覽">
</a>

</center>

<br/>

1. **自動標籤應用**  
   - 根據對話內容添加標籤，例如```Escalated```或```Low Priority```。  
   - 同時處理多個標籤。

2. **動態規則系統**  
   - 用戶可以定義標籤觸發條件，例如特定的關鍵字或短語。  
   - 支援自動添加和移除標籤的功能。

3. **自定義使用場景**  
   - 例如，醫療熱線中 ```Escalated``` 可用於表示嚴重疼痛，而 ```Low Priority```可用於輕微疼痛。

4. **可視化反饋**  
   - 標籤會顯示在對話歷史中，提供其分類的即時見解。

---

## 如何設置 自動標記
1. **前往整合**
   - 打開 ```整合```區域，選擇 **自動標記**


<center>
<a href="/images/seachat/en/labeling/auto-labeling/navigation-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/navigation-ui.png"  alt="Navigation to Auto Labeling">
</a>

</center>

<br/>

2. **創建規則**  
   - 定義添加或移除標籤的觸發條件。  
   - 例如，對於醫療熱線：
     - ```Extreme pain``` 觸發 ```Escalated``` 標籤。  
     - ```Minor aches``` 觸發 ```Low Priority``` 標籤。

<center>

<a href="/images/seachat/en/labeling/auto-labeling/define-rules.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/define-rules.png"  alt="定義標籤規則">
</a>
</center>

<br/>


3. **測試規則**  
   - 模擬對話以檢查標籤是否正確應用。  
   - 例如，輸入 "I feel so much pain, I need a doctor’s attention" 以觸發 ```Escalated```。
  

<center>
<a href="/images/seachat/en/labeling/auto-labeling/test-rules.png">
<img height="100%" width="80%" src="/images/seachat/en/labeling/auto-labeling/test-rules.png"  alt="測試對話中的標籤規則">
</a>


</center>

<br/>

4. **調整和保存**  
   - 修改規則以提升準確性，並保存配置。  


<center>
<a href="/images/seachat/en/labeling/auto-labeling/save-rules.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/save-rules.png"  alt="定義標籤規則">
</a>

</center>

<br/>

---

**高級使用場景**  

1. **醫療分診系統**  
   - 使用標籤如 ```Green```、 ```Yellow``` 和 ```Red```
 根據病情嚴重程度進行分類。  
     - ```Red```：嚴重問題，例如呼吸困難或大量出血。  
     - ```Yellow```：中度疼痛或發燒。  
     - ```Green```：輕微疼痛或感冒。  


<center>
<a href="/images/seachat/en/labeling/auto-labeling/advanced-rules.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/advanced-rules.png"  alt="定義標籤規則">
</a>

</center>

<br/>

2. **標籤自動化**  
   - 將操作與特定標籤聯繫起來：
        - 當 ```Escalated```被應用時觸發電子郵件或 SMS。  
        - 自動跟進 ```Low Priority```案例。
   - 查看我們的 [標籤自動化](https://wiki.seasalt.ai/seachat/manual/labeling/label-automation/) 教學了解更多細節。


---

**自動標記的優勢**  

- **效率**：減少手動標籤的工作量。  
- **可擴展性**：處理大量數據。  
- **準確性**：確保規則應用一致。  
- **客製化**：適用於多種行業和使用場景。  

---

**結論**  
自動標記徹底改變了企業管理對話和數據的方式。從醫療保健中的動態分診到簡化客戶支持，這個工具簡化並加速了流程，同時確保準確性。未來的教程將深入探討移除標籤和利用標籤自動化以實現更高級的工作流程，敬請期待！


---


#### 標籤自動化

<!-- Source: seachat-manual/09-automation/label-automation.md -->

<!-- Weight: 602 -->

*學習如何在 SeaChat 中設置和使用 標籤自動化，以根據應用的標籤觸發操作。*


---

## 視頻教程

<iframe width="100%" height="400" src="https://www.youtube.com/embed/2SYYU1lQqrc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

---

**簡介**

標籤自動化 是 SeaChat 中的一項功能，允許用戶定義當標籤被應用或移除時觸發的操作。

此功能基於 [自動標記](https://wiki.seasalt.ai/seachat/manual/labeling/auto-labeling/) 功能進一步拓展，通過引入工作流程來自動通知或升級重要事件。

本教程將帶您完成標籤自動化的設置，並提供增強工作流程的實用範例。

---

## 主要功能

<center>
<a href="/images/seachat/en/labeling/label-automation/feature-overview.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/feature-overview.png"  alt="功能概覽">
</a>

</center>

<br/>

1. **自動觸發操作**
   - 設置操作，例如發送電子郵件、簡訊或 API 請求。
   - 操作會在特定標籤被應用或移除時觸發。

2. **可自定義工作流程**
   - 定義針對個別標籤（如 **Code Red** 或 **Code Yellow**）的工作流程。
   - 根據使用場景（例如醫療分診或客戶服務警報）量身定制操作。

3. **內建自動化功能**
   - 使用 SeaChat 的內建功能，無需依賴像 Zapier 這樣的外部工具。

4. **手動與自動整合**
   - 標籤可通過 自動標記自動應用，或在對話中手動添加。

---

## 如何設置 標籤自動化

1. **進入整合**
   - 打開 **整合** 區域，選擇 **標籤自動化**。

<center>
<a href="/images/seachat/en/labeling/label-automation/navigation-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/navigation-ui.png"  alt="導航至 標籤自動化">
</a>

</center>

<br/>

2. **選擇標籤**
   - 選擇一個標籤，例如 **Code Red** 或 **Code Yellow**。
   - 範例：將 **Code Red** 用於嚴重情況。

<center>
<a href="/images/seachat/en/labeling/label-automation/choose-a-label.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/choose-a-label.png"  alt="選擇自動化標籤">
</a>

</center>

<br/>

3. **定義操作**
   - 為選定標籤添加操作：
      - **電子郵件**：指定收件人和消息內容。
      - **簡訊**：提供電話號碼和消息文本。
      - **API 請求**：配置自定義端點（適用於高級用戶）。


<center>
<a href="/images/seachat/en/labeling/label-automation/define-action.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/define-action.png"  alt="定義自動化操作">
</a>

</center>

<br/>

4. **保存並測試**
   - 保存配置並通過手動或自動應用標籤進行測試。

<center>
<a href="/images/seachat/en/labeling/label-automation/save-and-test.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/save-and-test.png"  alt="保存並測試操作">
</a>

</center>

<br/>

---

## 範例使用場景：醫療分診

如需查看完整範例，請觀看我們的標籤自動化視頻教程。

1. **Code Red - 嚴重情況**
   - **觸發條件**：將 **Code Red** 應用於涉及呼吸困難或嚴重出血等嚴重情況的對話。
   - **操作**：向相關醫療團隊發送電子郵件和簡訊。

2. **Code Yellow - 中度情況**
   - **觸發條件**：對中度疼痛或發燒等情況應用 **Code Yellow**。
   - **操作**：通過電子郵件通知相關人員。

3. **移除標籤**
   - **觸發條件**：當 **Code Red** 被移除時，發送電子郵件通知 **Alert Disarmed**。

---

## 工作流程範例

1. **定義 **Code Red** 的工作流程**
   - 設置電子郵件通知工作人員有關嚴重情況的消息。
   - 為冗餘配置 Google Voice 號碼以接收簡訊警報。

<center>
<a href="/images/seachat/en/labeling/label-automation/define-email-action.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/define-email-action.png"  alt="定義電子郵件操作">
</a>

</center>

<br/>

2. **手動觸發測試**
   - 在對話中手動應用 **Code Red** 並驗證操作是否觸發。
   - 檢查電子郵件和簡訊通知，確認它們是否正確執行。

<center>
<a href="/images/seachat/en/labeling/label-automation/conversation-example.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/conversation-example.png"  alt="對話範例">
</a>

</center>

<br/>

3. **結合自動標記自動觸發**
   - 與 自動標記功能結合，根據預定對話規則自動觸發 **Code Red**。

<center>
<a href="/images/seachat/en/labeling/label-automation/action-on-labeling.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/action-on-labeling.png"  alt="自動標記整合">
</a>

</center>

<br/>

---

**標籤自動化的優勢**

- **效率**：通過標籤觸發的自動化操作簡化工作流程。
- **靈活性**：支持手動和自動標籤應用。
- **整合性**：內建於 SeaChat 中，無需第三方工具。
- **客製化**：配置適合各種行業和使用場景的工作流程。

---

**進階功能**

- **API 整合**：適用於高級用戶，通過 API 請求觸發自定義工作流程。
- **結合自動化**：與 自動標記整合，創建無縫工作流程。

---

**結論**  
標籤自動化增強了 SeaChat 的功能，將應用的標籤轉化為可執行的事件。無論是管理醫療熱線還是簡化客戶服務，此功能都為自動化和優化流程提供了工具。嘗試將標籤自動化與 自動標記結合使用，以創建適合您需求的強大高效工作流程。


---


#### Zendesk 工單搜尋工具

<!-- Source: seachat-manual/09-automation/zendesk-ticket-search.md -->

<!-- Weight: 603 -->


SeaChat Zendesk 工單搜尋工具是 Seasalt.ai 提供的一項創新功能，透過將 複雜的 Zendesk 工單數據 轉換為 直接且具上下文關聯性的回應，優化客戶支援流程。為避免使用者在大量搜尋結果中篩選並手動開啟每張工單，SeaChat 會從完整的工單對話中擷取關鍵資訊，並在單次互動內提供精確的答案。

---

<iframe width="100%" height="400" src="https://www.youtube.com/embed/PJYiC-jKDnU?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px";></iframe>

## 運作方式

SeaChat Zendesk 工單搜尋工具利用 Zendesk API 的強大功能，透過以下步驟來處理使用者查詢並提供最佳答案

&nbsp;&nbsp;&nbsp;&nbsp; **1. 關鍵字提取:**

當使用者提交查詢時，SeaChat 會自動解析輸入內容，並提取一個或多個關鍵字。這些關鍵字將用於向 Zendesk 搜尋 API 發送查詢請求。

&nbsp;&nbsp;&nbsp;&nbsp; **2. 透過 Zendesk 搜尋 API 查詢工單:**

SeaChat 透過 Zendesk 搜尋 API `/api/v2/search.json?query=xxx` 發送請求，並獲取符合搜尋條件的工單列表。值得注意的是，Zendesk 搜尋 API 的初始回應僅包含每張工單對話串的第一則留言（通常是工單的描述），作為工單內容的預覽。

&nbsp;&nbsp;&nbsp;&nbsp; **3. 檢索完整的工單互動:**

為了獲取更完整的資訊，SeaChat 會針對搜尋結果中的每張工單，進一步調用 Zendesk 工單留言 API `/api/v2/tickets/{id}/comments`。
此步驟可擷取該工單的所有留言，包括後續回覆，客服代理的回答，內部備註。

&nbsp;&nbsp;&nbsp;&nbsp; **4. 生成答案:**

SeaChat 透過自然語言處理（NLP）分析完整的工單對話內容，以找出最相關的資訊，並為使用者提供直接且可行的答案。若有多張工單的內容與查詢相關，SeaChat 會整合多個工單的資訊來提供最佳回應。

---

## 使用案例

SeaChat Zendesk 工單搜尋工具用途廣泛，可應用於多種客服與業務場景，提升工作效率並改善客戶體驗。以下是幾個最佳使用案例：

&nbsp;&nbsp;&nbsp;&nbsp; -- **加速客服回應:**
客服人員可以透過利用歷史工單資料快速擷取客戶問題的完整答案，從而減少手動搜尋工單所花費的時間。

&nbsp;&nbsp;&nbsp;&nbsp; -- **自動知識庫擴充:**
透過整合頻繁的查詢及其相應的解決方案，該工具可以幫助自動更新常見問題解答和知識庫文章，確保自助服務選項始終最新且準確。

&nbsp;&nbsp;&nbsp;&nbsp; -- **根本原因分析:**
支援經理可以利用該工具來分析工單對話中的模式（例如重複出現的問題或常見的故障排除步驟），以提高產品可靠性和客戶滿意度。

&nbsp;&nbsp;&nbsp;&nbsp; -- **高效數據整合:**
將 Zendesk 與其他系統（例如 CRM 平台或分析儀表板）整合時，該工具能夠提取全面的工單信息，從而實現更有效的跨平台數據分析和報告。

---

透過將 Zendesk 搜尋 API 的強大搜尋功能與工單評論 API 提供的詳細見解相結合，SeaChat 為傳統 Zendesk 搜尋 UI 提供了無縫且高效的替代方案。這種創新方法不僅加快了解決過程，還提高了支援回應的整體品質。

## **配置 Zendesk 工單搜尋工具的步驟:**

若要設定此功能，請登入 SeaChat 後，導覽至AI助理配置 \-\> 整合 \-\> 客制GPT工具。

### **步驟 1：選擇工具類型**

按一下 **「新增的自訂 GPT 工具」**，然後選擇 **Zendesk 工單搜尋** 作為工具類型。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image1.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image1.png"  alt="Example of New Custom Tool">
</a>
<br/>
</center>

### **步驟 2：新增 Zendesk 帳戶信息**

要設定 Zendesk 工單搜尋工具，您需要提供幾個關鍵資訊：

- 啟用工具：開啟啟用開關。這將啟動該工具，允許 SeaChat 在相關對話中自動開始使用它。
- 工具名稱：輸入工具的名稱。它應只包含字母（A-Z、a-z）、數字（0-9）、底線（\_）或連字號（-），不包含任何空格。
- 描述：詳細描述 SeaChat 可以在 Zendesk 中找到哪些資料以及在什麼條件下應啟動此自訂工具。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image2.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image2.png"  alt="Example of New Custom Tool">
</a>
<br/>

_Example: 設定Zendesk工單搜尋工具來檢索工單、產品名稱和價格。_

</center>

您還需提供以下 Zendesk 帳戶信息，以允許 SeaChat 安全地存取和搜尋工單。

- **子網域**：您的 Zendesk 子網域是 Zendesk URL 的第一部分。例如Zendesk URL 是：*https://seasaltai9494.zendesk.com*，那麼子網域是 _seasaltai9494_。
- **電子郵件**：輸入與您的 Zendesk 帳戶關聯的電子郵件地址。這與您用於登入的電子郵件地址相同。
- **API Token**：它驗證 SeaChat 對您的 Zendesk 帳戶的存取權限，要產生 API Token，請按照以下步驟操作：

1. 登入您的 Zendesk 管理中心。
2. 在左側邊欄中，前往應用程式和整合 → Zendesk API。
3. 在「設定」標籤下，找到「Token存取」部分。
4. 切換啟用 API Token存取（如果尚未啟用）。
5. 點選新增 API Token。
6. （可選）新增 API Token的描述。
7. 複製產生的 API Token並安全儲存（不會再次顯示）。
8. 點選「儲存」。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image3.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image3.png"  alt="Example of New Custom Tool">
</a>
<br/>

_Example: 輸入 Zendesk 帳戶憑證來驗證 SeaChat 的 API 存取權。_

</center>

### **步驟 3：定義搜尋參數**

您可以自定義搜尋參數來控制 Zendesk 工單的擷取和顯示方式。

- **per_page：** 決定在單一請求中檢索的工單數量。建議將此值設為 1 到 20 之間，預設值為 5。對於每個檢索到的工單，SeaChat 將調用 Zendesk API 使用以下端點獲取其詳細資訊和評論：`GET https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_no}/comments`。由於 SeaChat 會檢索每個工單的所有評論，因此增加每個請求的工單數量可能會減慢回應時間。
- **sort_by**：定義檢索到的工單的排序標準。您可以選擇按工單的上次更新時間 (updated_at)、建立時間 (created_at)、優先權 (priority)、狀態 (status) 或類型 (ticket_type) 進行排序。預設情況下，排序基於相關性。
- **sort_order**：指定工單是否應按升序（asc）或降序（desc）排序。預設是降序。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image4.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image4.png"  alt="Example of New Custom Tool">
</a>
<br/>

_設置每次取得 10 張工單及其評論，並按更新順序降序排列（從最新到最舊）。_

</center>

### **步驟 4（可略）：測試您的設定**

在最終確定之前，您可以透過輸入關鍵詞（例如**產品名稱、訂單號或相關關鍵詞**）來測試工具。點擊**提交**發送測試請求。如果成功，您將看到即時 Zendesk 搜尋結果顯示在右側。

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image5.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image5.png"  alt="Example of New Custom Tool">
</a>
<br/>

_使用產品名稱關鍵詞「452-ABC」進行測試，並成功檢索到與該產品相關的工單評論。_

</center>

### **步驟5：儲存設定**

點擊「儲存」，您的 Zendesk 工單搜尋 工具就可以使用了。您的 SeaChat AI 代理現在可以檢索 Zendesk工單資料以增強客戶支援。


---


#### 工作區管理

<!-- Source: seachat-manual/06-workspace/01-workspace-management.md -->

<!-- Weight: 700 -->

*學習如何在 SeaChat 中管理工作區，包含 AI 助理與成員管理、通知設置及 API 金鑰使用。探索多重工作區的功能，提升工作效率。*


工作區是您管理所有助理和成員的控制中心。我們首先導航到**工作區**部分，以找到本文將介紹的所有功能。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div height="10%" style="width: 50%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/workspace-sidebar.png" target="_blank">
    <img height="10%" width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/workspace-sidebar.png" alt="SeaChat | 側邊選單中的工作區">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">側邊選單中的工作區</p>
</div>


## AI助理

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/agents.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/agents.png" alt="SeaChat | 助理管理">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">助理管理</p>
</div>

這裡可以管理所有的AI助理。每一行代表一個AI助理及其名稱、電子郵件和狀態。您還可以看到未讀消息的數量，找到AI助理對話的 URL，直接啟動對話或新增AI助理。

## 成員

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/members.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/members.png" alt="SeaChat | 成員管理">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">成員管理</p>
</div>

成員有不同的類型。根據成員類型，他們會有不同的權限。如果您是工作區的擁有者，可以新增成員並分配不同的角色。以下是一些可以分配給成員的角色：

1. 系統管理者：擁有工作區的全部訪問權限，可以管理所有設置，編輯 AI 助理的設置，管理知識庫，訪問助理對話並以真人助理的身份接管對話。
2. AI 助理開發者：可以編輯 AI 助理的設置，管理知識庫，訪問助理對話和測試。
3. 真人助理：可以訪問助理對話並以真人助理的身份接管對話。

### 編輯使用者

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/add-member.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/add-member.png" alt="SeaChat | 成員設置">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">成員設置</p>
</div>

您可以將不同的助理分配給不同的成員。例如，將測試中的助理分配給您的 AI 助理開發者，將產線中的助理分配給您真人助理。管理員可以訪問和監控這兩種類型的助理。

> **🤖 助理與 👨 成員**
>
> 在本文中，“助理”和“機器人”這兩個詞可以互換使用。如您所見，大多數URL參數使用“bot”(機器人)，而文中大多使用“agent”(助理)。
>
> Seasalt.ai 正在為普通“聊天機器人”增加更多推理和執行功能，因此我們更喜歡使用“助理”一詞，這意味著助理可以執行機器人無法完成的任務。
>
> 然而，在“助理”或“真人助理”的情境下，這可能會讓人混淆。因此，在這些情況下，我們將使用“AI助理”來指代自主助理，而“真人助理”指代人類助理。
> 
> 反觀成員一詞，一律代表真人成員。


[//]: # (## 工作區偏好設置)

[//]: # ()
[//]: # (<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">)

[//]: # (<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">)

[//]: # (    <a href="/images/seachat/zh/workspace/01-workspace-management/preference.png" target="_blank">)

[//]: # (    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/preference.png" alt="SeaChat | ">)

[//]: # (    </a>)

[//]: # (</div>)

[//]: # (    <p style="margin-top: 20px; font-size: 15px">偏好設置</p>)

[//]: # (</div>)

[//]: # ()
[//]: # (這裡可以管理工作區的通知設置。SeaChat 可以自動向您發送電子郵件，通知您新對話和新的人工助理請求。啟用您想接收的通知類型後，還可以設置通知的語言。)

### 通知設置

SeaChat 提供不同語言的通知。您可以選擇接收通知的語言。雖然可以將語言設置為默認值（與外觀語言相同），但我們建議設置為您在對話中的預定語言。這有助於優化助理的性能並加快操作速度。

## 工作區 API 金鑰

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/workspace-api.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/workspace-api.png" alt="SeaChat | API 金鑰">
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

## 多重工作區

工作區的概念是指一組AI助理和成員。在一個工作區下，你可以擁有多個AI助理和成員。如果你擁有多個工作區，你可以通過點擊螢幕左上角的工作區名稱切換到別的工作區，或直接前往至**工作區儀表板**操作。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/access-workspace-dashboard.png" target="_blank">
    <img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/access-workspace-dashboard.png" alt="SeaChat | 工作區儀表板">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">前往工作區儀表板</p>
</div>

一旦進入工作區儀表板，您可以訪問所有的工作區。如果您希望創建新的工作區，可以點擊**建立**按鈕來完成。

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/zh/workspace/01-workspace-management/create-workspace.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/workspace/01-workspace-management/create-workspace.png" alt="SeaChat | 建立新的工作區">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">建立新的工作區</p>
</div>

你可以在一個工作區中建立多個AI助理，每個助理有不同的使用情境、語言和助理描述。這些AI助理可以在單一工作區中為不同的客戶服務於不同的頻道或整合。利用多重工作區功能的一個實際例子是新助理的測試和開發。你可以創建一個獨立的工作區進行測試和開發，另一個用於產線。這樣可以在不影響生產環境的情況下測試新助理。

## 工作區上限

不同的計畫對您可以建立的工作區數量有不同的上限。如果您已達到上限，您可以升級您的計畫以建立更多的工作區。如果您對定價有任何疑問，請參考[定價方案](https://wiki.seasalt.ai/seachat/seachat-payments/pricing-plans/)。

以下是根據您訂閱的計畫可以建立的工作區數量：

- **免費方案** - 1 個工作區
- **標準方案** -  1 個工作區
- **高級方案** -  2 個工作區
- **企業方案** -  多個工作區


---


### 來電轉接

<!-- Source: inbound-voice-agent/tutorial.md -->

<!-- Weight: 800 -->

*SeaChat 來電轉接教學*



---

以下是上述18分鐘教程的視頻，無需編程技能即可部署AI語音助理：

<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/Hh04t_Qg8-I?list=PL8K7_LTqly449uOg_uBWOPfFyL1fJRjkE" title="YouTube Video Player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## 來電轉接簡介及運作原理

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/inbound-voice-agent/call-forwarding/call-forwarding-diagram.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; background-color: #ffffff" src="/images/seachat/zh/inbound-voice-agent/call-forwarding/call-forwarding-diagram.png" alt="來電轉接示意圖">
</a>

**來電轉接**
</center>

來電轉接是一種電信功能，允許用戶將來電從一個號碼轉接到另一個號碼。這確保即使您無法接聽主要電話時，重要的電話也不會錯過。來電轉接主要有兩種類型：無條件來電轉接，即轉接所有來電，和有條件來電轉接，即只在特定情況下（如忙線或無應答時）進行轉接。

通常，企業和個人偏好使用有條件來電轉接，確保只有在必要時才轉接來電，而不是每次來電都進行轉接。設置這項功能通常很簡單，不同的電信提供商和VoIP服務都提供簡單的方法來通過設置或在電話上撥打特定代碼來配置來電轉接。

---


## 將來電轉接到AI助理
一旦您在電信服務商處配置了來電轉接後，您可以通過將來電轉接到您的SeaChat語音助理來簡化您的應答服務。您的SeaChat助理可以幫助您管理預約，並在繁忙時段或您無法接聽時生成來電摘要。

以下教程將指導您完成所有必要步驟，以設置您的電話號碼來轉接到您的SeaChat助理。成功設置來電轉接後，您可以訪問我們的[wiki](https://wiki.seasalt.ai/zh/)或在Seasalt.ai的YouTube頻道上觀看我們的教程視頻，進一步了解如何將SeaChat的不同功能應用到您的生產環境中。

## 準備步驟
在進行來電轉接設置之前，讓我們確保AI助理已準備好接收來電。


- **步驟1** – **創建一個SeaChat助理**:
  - 如果這是您首次登錄SeaChat，您需要先創建一個新的助理才能繼續後續步驟。歡迎訪問我們的[wiki](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/)，以獲取更詳細的說明。
- **步驟2** – **部署語音AI助理**:
  - 我們需要為語音AI助理分配一個電話號碼，這樣我們才能將其部署到生產環境中進行來電應答。按照以下說明完成此步驟，或您可以查看我們的[wiki](https://wiki.seasalt.ai/zh/seachat/manual/channels/voicebot/)，以獲取更全面的指南——來電通道配置。
    - ***步驟2.1*** – ***導航到來電配置頁面***。
      - 在左側側邊欄中前往“Channel -> Calls”下的助理配置部分。
    - ***步驟2.2*** – ***購買一個免付費號碼並將AI助理部署到該號碼***。
      - 按照SeaChat UI上的步驟購買一個免付費號碼，該AI助理將部署到該號碼。
      - 配置AI助理並設置您希望助理具備的正確行為。
    - ***步驟2.3*** – ***測試您的AI助理***。
      - 您應該在將AI助理部署到生產環境之前進行測試。微調和調整助理的配置，以實現您需要的最佳性能。

  



---


#### Android/ iPhone

<!-- Source: inbound-voice-agent/call-forwarding-setup/android-and-iphone.md -->

<!-- Weight: 802 -->

*SeaChat 功能教學｜來電轉接設定(Android/iPhone)*


## 確認準備步驟是否完成
要繼續進行來電轉接的設定，我們需要確認是否已經部署了一個由 SeaChat AI 助理接聽的電話號碼。如果您尚未完成此步驟，請參閱我們的[教學](https://wiki.seasalt.ai/zh/seachat/inbound-voice-agent/tutorial/)來了解如何操作。

## 將個人來電轉接到SeaChat（Android）
要將您的個人來電轉接到Seasalt.ai，我們需要配置您的個人手機和指定的SeaChat AI助理。您可以按照以下步驟完成設置：


- **步驟1** – **配置手機的來電轉接功能**:
  - 現在我們需要在您的設備上配置您的號碼，以啟用來電轉接功能。請注意，iOS系統與Android系統的配置方式不同。本節將側重於Android設備的配置。
    - ***步驟1.1*** – ***打開電話應用程式***。
      - 在您的設備上找到電話應用程式。這通常是帶有電話圖標的應用程式。
    - ***步驟1.2*** – ***進入來電設置***。
      - 在電話應用程式中找到設置選項。通常可以通過點擊菜單圖標來找到它。
    - ***步驟1.3*** – ***找到並啟用來電轉接***。
      - 在設置中搜索來電轉接。在該部分中找到關鍵詞“來電轉接”或“轉接”，可能會出現在“通話”或“高級設置”下。
    - ***步驟1.4*** – ***輸入AI助理的號碼***。
      - 現在您應該會看到如下圖像，允許您將來電轉接到AI助理的號碼。將號碼輸入到您希望AI助理接手的字段中。對於有條件轉接，我們將側重於“忙線時”、“無應答時”和“無法接通時”這些字段。
    - ***步驟1.5*** – ***在目標字段中輸入AI號碼***。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/inbound-voice-agent/call-forwarding/enter-number-android.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/inbound-voice-agent/call-forwarding/enter-number-android.png" alt="Android輸入電話號碼UI">
</a>

**輸入要轉接的電話號碼**
</center>

- **步驟2** – **保存設置**:
  - 一旦您輸入了SeaChat助理的電話號碼，點擊保存或確定按鈕以保存來電轉接設置。現在，您的Android設備上的來電將被轉接到您的SeaChat助理。
- **步驟3** – **測試來電轉接**:
  - 現在您應該已經成功設置來電轉接功能到您的SeaChat助理。測試一下，看看這個功能是否有效。如果無效，請再次檢查以上每個步驟，看看是否有遺漏的地方。

## 將個人來電轉接到SeaChat from Seasalt.ai（iPhone）
要將您的個人來電轉接到Seasalt.ai，我們需要配置您的iPhone和指定的SeaChat AI助理。您可以按照以下步驟完成設置：

- **步驟1** – **在iOS設備上配置來電轉接**:  
  本節將指導您在iOS設備上設置來電轉接，該過程與Android稍有不同。
  - ***步驟1.1*** – ***打開設置應用程式***。
    - 在您的iPhone上找到並打開設置應用程式。這是您找到所有電話設置的地方，包括來電轉接選項。
  - ***步驟1.2*** – ***進入電話設置***。
    - 在設置應用程式中向下滾動，點擊“電話”。這將打開與您設備通話功能相關的設置。
  - ***步驟1.3*** – ***找到並啟用來電轉接***。
    - 在電話設置中，點擊“來電轉接”。切換開關以啟用該功能。啟用後，將出現一個標有“轉接至”的字段，允許您輸入應該轉接來電的號碼。
  - ***步驟1.4*** – ***輸入AI助理的號碼***。
    - 在“轉接至”字段中，輸入您的AI應答服務提供的電話號碼。這將在您無法接聽時將來電轉接到AI助理。如有必要，請確保包含正確的國家代碼。
  - ***步驟1.5*** – ***保存設置***。
    - 輸入AI助理的號碼後，點擊“返回”或“完成”以保存更改。這將確認您的來電現在已轉接。

- **步驟2** – **測試來電轉接**:  
  為了確保來電轉接設置正確，您可以要求某人撥打您的電話進行測試。如果來電轉接到您的AI助理，則說明過程成功。如果沒有，請檢查設置過程中是否有遺漏或需要調整的部分。

現在來電轉接功能將您的來電轉接到SeaChat助理，當有條件轉接設置完成後即可生效。根據您的電信服務提供商的政策，啟用此功能可能需要額外步驟。我們建議您先與您的電信服務提供商確認是否有額外要求，如需要進行現場登記等。


---


#### 商業來電 - US, VoIP, Taiwan, Singapore

<!-- Source: inbound-voice-agent/call-forwarding-setup/business.md -->

<!-- Weight: 803 -->

*SeaChat 功能教學｜來電轉接設定（企業 - 美國、VoIP、台灣、新加坡*


## 確認準備步驟是否完成
要繼續進行來電轉接的設定，我們需要確認是否已經部署了一個由 SeaChat AI 助理接聽的電話號碼。如果您尚未完成此步驟，請參閱我們的[教學](https://wiki.seasalt.ai/zh/seachat/inbound-voice-agent/tutorial/)來了解如何操作。

## 將商業來電轉接到SeaChat

轉接商業來電可能比轉接個人來電更為複雜。建議您查閱官方文檔或聯繫電信商客服獲得幫助以進行具體設置。請謹慎按照以下說明進行操作，以避免潛在問題。

## 美國電信商

### AT&T
- **無條件來電轉接:**  
  拿起電話聽筒，撥打 ```*72```（或 ```72#```），然後輸入您想要轉接來電的號碼。長途電話需包括 1 + 10位數字的號碼。  
  本地電話只需使用區號和7位數字號碼，或對於不需要區號的電話直接使用7位數字號碼。  
  當您聽到確認音後，來電轉接即已啟用。
- **無應答來電轉接:**  
  撥打 ```*92```，然後輸入10位數轉接號碼並按 #。等待確認音。
- **忙線來電轉接:**  
  撥打 ```*90```，然後輸入10位數轉接號碼並按 #。確認音表示來電轉接已激活。
- **選擇性來電轉接:**  
  撥打 ```*63``` 並按照提示轉接特定預選號碼。
- **取消來電轉接:**  
  無條件轉接：撥打 ```*73#```。  
  無應答轉接：撥打 ```*93#```。  
  忙線轉接：撥打 ```*91#```。

### Frontier
- **無條件來電轉接:**  
  撥打 ```*72``` 並輸入10位數轉接號碼。等待電話接通並聽到確認音。  
  例外情況：在某些地區（如印第安納州、伊利諾伊州、賓夕法尼亞州），撥打```72#```。對於康涅狄格州的Frontier語音用戶，撥打```72```後接號碼。
- **無應答來電轉接:**  
  撥打 ```*92``` 並設置轉接前的鈴響次數。然後，輸入10位數轉接號碼。  
  例外情況：在Seneca Gorham撥打```52```；在Rochester撥打```44```。您還可以通過撥打```40```來更改鈴響持續時間，並設置轉接前的秒數。
- **忙線來電轉接:**  
  撥打 ```*90```，輸入10位數號碼並按 #。  
  例外情況：在Seneca Gorham撥打```50```；在Rochester撥打```48```。
- **選擇性來電轉接:**  
  撥打 ```*63``` 並按照語音指示管理您的轉接清單。
- **取消來電轉接:**  
  無條件轉接：撥打 ```*73``` 並按**通話**。  
  無應答：撥打 ```*93``` 並按**通話**。  
  忙線：撥打 ```*91``` 並按**通話**。

### US Mobile
- **無條件來電轉接:**  
  在您的電話撥號盤上，輸入 ```*72```。然後，輸入要轉接來電的10位數號碼（包括區號）（例如 ```*72-908-123-4567```）。點擊通話按鈕並等待確認音或消息。掛斷電話以啟用來電轉接。
- **無應答來電轉接:**  
  在您的電話撥號盤上，輸入 ```*71```。輸入包括區號在內的10位數轉接號碼（例如 ```*71-908-123-4567```）。點擊通話按鈕並等待確認音或消息。確認後，來電轉接將被激活。
- **忙線來電轉接:**  
  與無應答來電轉接相似，在您的電話撥號盤上，輸入 ```*71```，後接您希望轉接來電的10位數號碼。點擊通話並等待確認音。當轉接確認後，掛斷電話。
- **取消來電轉接:**  
  要取消任何類型的來電轉接，請在您的電話上撥打 ```*73```。點擊通話，並在聽到確認音後掛斷電話以停用來電轉接。

### T-Mobile
- **無條件來電轉接:**  
  撥打 ```**21*```，然後輸入10位數轉接號碼並按下通話按鈕。等待確認音以完成設置。
- **無應答來電轉接:**  
  撥打 ```**61*```，然後輸入10位數轉接號碼並按下通話按鈕。當聽到確認音後，轉接將激活。
- **忙線來電轉接:**  
  撥打 ```**67*```，然後輸入10位數轉接號碼並按下通話按鈕。當您聽到確認音後，來電轉接即被激活。
- **無法接通時的來電轉接:**  
  撥打 ```**62*```，然後輸入10位數轉接號碼並按下通話按鈕。當您聽到確認音後，來電轉接即被激活。
- **取消來電轉接:**  
  無條件來電轉接：撥打 ```##21#```，按下通話按鈕，並等待確認音以關閉。  
  無應答來電轉接：撥打 ```##61#```並按下通話按鈕。  
  忙線來電轉接：撥打 ```##67#```並按下通話按鈕。  
  無法接通來電轉接：撥打 ```##62#```並按下通話按鈕。  
  所有有條件來電轉接：撥打 ```##004#``` 停用所有有條件來電轉接。

### Comcast（商務用戶）
- **無條件來電轉接:**  
  在拿起聽筒或按下**通話**鍵前，撥打 ```*72```。然後，撥打您希望轉接來電的10位數號碼。按下**通話**鍵以啟用來電轉接，這將通過一個音調和消息得到確認。
- **無應答來電轉接:**  
  在拿起聽筒或按下**通話**鍵前，撥打 ```*71```。然後，輸入10位數轉接號碼並按下**通話**鍵。來電轉接將在確認音後激活。
- **忙線來電轉接:**  
  在拿起聽筒或按下**通話**鍵前撥打 ```*90```，然後輸入10位數轉接號碼。按下**通話**鍵並等待確認音。
- **選擇性來電轉接:**  
  拿起聽筒並撥打 ```*63```。按照語音提示選擇要轉接的號碼，並在確認碼後激活。
- **取消來電轉接:**  
  無條件來電轉接：撥打 ```*73```，等待確認音，然後掛斷電話。  
  無應答來電轉接：撥打 ```*93```，等待提示音，然後掛斷電話。  
  忙線來電轉接：撥打 ```*91```，等待確認音，然後掛斷電話。  
  選擇性來電轉接：撥打 ```*83```，輸入規則詳細信息，並保存以停用。

### Xfinity Mobile（Comcast消費者）
- **無條件來電轉接:**  
  拿起聽筒，聽取撥號音，並按 ```*72```。輸入您的應答服務提供的10位數轉接號碼。當聽到確認音後，來電轉接即被激活。
- **無應答來電轉接:**  
  拿起聽筒，聽取撥號音，並按 ```*92```。輸入10位數轉接號碼。當聽到確認碼後，來電轉接即被激活。
- **忙線來電轉接:**  
  拿起聽筒，聽取撥號音，並按 ```*90```。輸入10位數號碼。當聽到確認音後，來電轉接即被激活。
- **選擇性來電轉接:**  
  拿起聽筒，聽取撥號音，並按 ```*63```。輸入您要轉接的10位數號碼。當聽到確認音後，服務即被激活。
- **取消來電轉接:**  
  無條件來電轉接：撥打 ```*73``` 以關閉服務。等待確認音。  
  無應答來電轉接：撥打 ```*93``` 停用。等待確認音。  
  忙線來電轉接：撥打 ```*91``` 以禁用。等待確認音。  
  選擇性來電轉接：撥打 ```*83``` 並按下 ```3``` 停用選擇性轉接。等待確認音。

### Verizon
- **無條件來電轉接:**  
  拿起聽筒，聽取撥號音，撥打 ```*72```，後接10位數轉接號碼（例如 ```*72-999-555-4567```）。等待一系列嗶聲後，電話將自動結束，確認來電轉接已啟動。
- **無應答來電轉接:**  
  拿起聽筒，聽取撥號音，撥打 ```*71```，後接10位數轉接號碼（例如 ```*71-999-555-4567```）。如果在3到6次鈴響後無應答，來電將被轉接。當聽到嗶聲後，電話將自動結束，確認激活成功。
- **忙線來電轉接:**  
  撥打 ```*71``` 並輸入您希望在忙線時轉接來電的10位數號碼。當聽到嗶聲後，電話將結束，激活此功能。
- **取消來電轉接:**  
  要關閉來電轉接，撥打 ```*73```。等待確認音，服務將被停用。

### RingCentral
- **無法接通時的來電轉接:**  
  當您的電話處於離線狀態時，來電將被轉接到另一位用戶的分機或外部號碼。這可以根據不同的呼叫處理規則進行配置：
  - 用戶/工作時間
  - 非工作時間
  - 自定義應答規則  
    一旦電話服務恢復，來電將自動恢復響鈴至原始電話。

- **要求:**
  - 分機必須至少分配有一個具有DigitalLine的桌面電話。
  - 在響鈴列表中必須禁用桌面和移動應用程式。
  - 在響鈴列表中還應該關閉PSTN號碼。
- **條件:**
  - 分機綁定的所有桌面電話都必須無法接通才能激活此功能。
  - 如果轉接來電至其他電話，所有轉接設備必須無法接通才能觸發此功能。
  - 在響鈴列表中啟用PSTN號碼或桌面和移動應用程式將阻止此功能生效。
- **啟用無法接通的來電轉接:**  
  登錄您的RingCentral在線帳戶。
  - ***非管理員用戶***：  
    點擊頂部菜單中的設置。打開呼叫處理部分，選擇您的呼叫規則（工作時間、非工作時間或自定義）。
  - ***管理員用戶***：  
    點擊頂部菜單中的用戶。從具有分機的用戶列表中選擇一個用戶。打開呼叫處理部分，選擇所需的呼叫規則。  
    在工作時間選項卡中，點擊“無法接通時的來電轉接”下的編輯。切換“來電重定向”功能。  
    選擇您希望轉接來電的地方：
    - 分機
    - 其他號碼
- **點擊保存以激活轉接規則。**

### Vonage
- **無條件來電轉接:**
  - 拿起聽筒，撥打 ```*72```，然後輸入您希望轉接來電的10位數號碼。按下```1```以確認，並等待確認音。
  - 在線設置：您還可以通過您的在線帳戶或Vonage Enterprise門戶進行來電轉接設置，導航至**摘要標籤** > **我的號碼** > **呼叫功能** > **來電轉接**，並按照提示輸入轉接號碼和所需的轉接前響鈴時長。
- **無應答來電轉接:**
  - 登錄您的在線帳戶或Vonage Enterprise門戶。導航至呼叫功能，選擇來電轉接，並設置轉接前的秒數。輸入轉接號碼並保存設置。
- **忙線來電轉接:**
  - 對於住宅用戶，登錄您的在線帳戶，轉到呼叫功能，並輸入轉接號碼。保存設置。
  - 對於企業用戶，進入Vonage Enterprise門戶中的**語音設置** > **常規**以啟用忙線來電轉接。
- **選擇性來電轉接:**
  - 在在線帳戶或企業門戶中，導航至呼叫功能，設置選擇性轉接的條件，並輸入轉接號碼。保存設置。

### Google Voice
#### Android:
- **無條件來電轉接:**  
  打開Google Voice應用程式。點擊**菜單** > **設置**，在自定義來電轉接下，選擇管理規則。選擇要轉接來電的聯絡人，並輸入您希望轉接來電的號碼。保存後，該規則將應用。
- **無應答來電轉接:**  
  在Google Voice應用程式中，點擊**菜單** > **設置** > **管理規則**。為特定聯絡人或群組設置規則，並選擇在無應答時轉接來電。指定轉接號碼。
- **忙線來電轉接:**  
  在Google Voice的設置中，訪問管理規則。選擇您希望轉接來電的聯絡人，並創建在忙線時轉接來電的規則。輸入轉接號碼並保存規則。
- **選擇性來電轉接:**  
  在Google Voice設置中的自定義來電轉接下，點擊管理規則。選擇特定聯絡人或聯絡人群組，將其來電轉接到不同號碼。保存後，該規則即被激活。
- **取消來電轉接:**  
  要關閉特定聯絡人的自定義來電轉接，進入Google Voice設置中的管理規則。找到您想要禁用的聯絡人或規則，並相應地刪除或編輯規則。

#### iPhone/iOS:
- **無條件來電轉接:**  
  打開Google Voice應用程式。點擊菜單 > 設置，然後導航至自定義來電轉接並選擇管理規則。選擇聯絡人或聯絡人群組，並輸入您要轉接來電的號碼。保存後，該規則將生效。
- **無應答來電轉接:**  
  在Google Voice應用程式中，前往菜單 > 設置 > 管理規則。創建無應答時轉接來電的規則，並輸入轉接號碼。保存規則後，來電轉接將激活。
- **忙線來電轉接:**  
  訪問Google Voice設置中的管理規則。設置在忙線時轉接來電的規則。輸入轉接號碼並保存更改。
- **選擇性來電轉接:**  
  在Google Voice中，前往自定義來電轉接下的管理規則。設置規則來轉接特定聯絡人或群組的來電，並指定轉接號碼。保存後，該服務將激活。
- **取消來電轉接:**  
  要關閉特定聯絡人或群組的自定義來電轉接，進入Google Voice中的管理規則，找到您要禁用的規則，並相應地刪除或編輯規則。

## 台灣電信商
### 中華電信
- **立即來電轉接:**  
  要激活，撥打 ```*77``` 後接轉接號碼，然後掛斷電話。  
  要停用，撥打 ```#77```。
- **忙線來電轉接:**  
  要激活，撥打 ```*76``` 後接轉接號碼，然後掛斷電話。  
  要停用，撥打 ```#76```。
- **無應答來電轉接:**  
  要激活，撥打 ```*75``` 後接轉接號碼，然後掛斷電話。  
  要停用，撥打 ```#75```。

### 台灣大哥大
- **無條件來電轉接:**  
  轉接至市話：撥打 ```**21*```，後接區號和號碼，然後 ```*11#```，並按發送。  
  轉接至手機：撥打 ```**21*```，後接手機號碼，然後 ```*11#```，並按發送。  
  視訊轉接至手機：撥打 ```**21*```，後接手機號碼，然後 ```*24#```，並按發送。
- **無應答來電轉接:**  
  轉接至市話：撥打 ```**61*```，後接區號和號碼，然後 ```*11#```，並按發送。  
  轉接至手機：撥打 ```**61*```，後接手機號碼，然後 ```*11#```，並按發送。  
  視訊轉接至手機：撥打 ```**61*```，後接手機號碼，然後 ```*24#```，並按發送。
- **無法接通時的來電轉接:**  
  轉接至市話：撥打 ```**62*```，後接區號和號碼，然後 ```*11#```，並按發送。  
  轉接至手機：撥打 ```**62*```，後接手機號碼，然後 ```*11#```，並按發送。  
  視訊轉接至手機：撥打 ```**62*```，後接手機號碼，然後 ```*24#```，並按發送。
- **忙線來電轉接:**  
  轉接至市話：撥打 ```**67*```，後接區號和號碼，然後 ```*11#```，並按發送。  
  轉接至手機：撥打 ```**67*```，後接手機號碼，然後 ```*11#```，並按發送。  
  視訊轉接至手機：撥打 ```**67*```，後接手機號碼，然後 ```*24#```，並按發送。
- **取消來電轉接:**  
  要取消個別轉接設置，撥打 ## 後接具體服務代碼（21/61/62/67），然後 #，並按發送。  
  要取消所有來電轉接，撥打 ##002# 並按發送。

## 新加坡電信商
### Singtel
- **無條件來電轉接:**  
  拿起聽筒，等待撥號音，然後撥打 ```#210YYYYYYYY#```，其中 ```YYYYYYYY``` 是您希望轉接來電的號碼。等待重複音，然後掛斷電話。您的來電轉接現在已啟動。
- **取消無條件來電轉接:**  
  拿起聽筒，等待撥號音，然後撥打 ```#211#```。等待重複音，然後掛斷電話。
- **無應答時來電轉接:**  
  拿起聽筒，等待撥號音，然後撥打 ```#220YYYYYYYY#```，其中 ```YYYYYYYY``` 是無應答時轉接的號碼。等待重複音，然後掛斷電話。
- **取消無應答時來電轉接:**  
  拿起聽筒，等待撥號音，然後撥打 ```#221#```。等待重複音，然後掛斷電話。
- **忙線時來電轉接:**  
  拿起聽筒，等待撥號音，然後撥打 ```#230YYYYYYYY#```，其中 ```YYYYYYYY``` 是忙線時轉接的號碼。等待重複音，然後掛斷電話。
- **取消忙線時來電轉接:**  
  拿起聽筒，等待撥號音，然後撥打 ```#231#```。等待重複音，然後掛斷電話。



---


### 定價方案

<!-- Source: seachat-payments/pricing-plans.md -->

<!-- Weight: 900 -->

*探索 SeaChat 的多樣定價方案，選擇最符合您業務需求的計劃，並了解不同方案的功能、模型定價與支援選項，助您高效管理 AI 助理與知識庫。*


SeaChat 提供一系列符合您業務需求的定價方案。從我們靈活的方案中選擇，立即開始使用 SeaChat。

每個方案都包含一組滿足不同業務需求的功能。您可以隨時升級或降級您的方案以適應您的業務需求。

在這裡，我們將介紹 SeaChat 的不同定價方案。

## 免費試用

- 終身 100 條免費文字回覆
- 1 個 AI 助理
- 知識庫包含最多 10 份文件（最大 200KB）和 20 萬詞元（tokens）
- 1 個管理員和 1 個工作區
- 每個AI助理回應費用 $0.01 美元
- 使用ChatGPT-3.5-turbo模型

## 標準方案

- 2 個 AI 助理
-  知識庫包含最多 100 份文件（最大 1 MB）和 100 萬詞元（tokens）
- 1 個管理員、1 個使用者成員和 1 個工作區
- 每個AI助理回應費用 $0.01 美元
- 使用ChatGPT-3.5-turbo模型

## 高級方案

- 10 個 AI 助理
- 知識庫包含最多 500 份文件（最大 10 MB）和 500 萬詞元（tokens）
- 1 個管理員、3 個使用者成員和 2 個工作區
- 每個AI助理回應費用 $0.006 美元起
- 可替換 LLM 模型，每個模型價格不一，請參考官網定價（包括GPT-4o mini, GPT-4o, GPT-4-turbo, ChatGPT-3.5-turbo, Mistral）
- 可添加電話語音助理（每分鐘起價 $0.15 美元）
- 進階功能：上下文抽取 / API / 移除 SeaChat 品牌字樣 / 語音助理

## 模型定價

高級和企業用戶可以為他們的 AI 助理選擇多種模型。每種模型都有不同的定價結構。請參考 SeaChat 官方網站了解詳細定價信息，或查看下方的定價信息。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/pricing-plans/pricing-model.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/pricing-plans/pricing-model.png" alt="SeaChat | 模型定價">
</a>

**模型定價**
</center>

## 支援方案

對於使用場景複雜的客戶，我們建議訂閱我們的 **啟動支援方案**。部署 LLM 驅動的 AI 助理需要廣泛的領域知識、技術支援和謹慎的設計決策。SeaChat 團隊觀察到許多因為缺乏對 LLM 和 RAG 運作理解而失敗的部署。此外，語音應用受到電信當局和 FCC 的嚴格監管。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/pricing-plans/pricing-support.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/pricing-plans/pricing-support.png" alt="SeaChat | 啟動支援方案">
</a>

**啟動支援方案**
</center>



---


#### Inline.app 助理

<!-- Source: seachat-manual/05-integrations/09-seachat-inline-restaurant-assistant.md -->

<!-- Weight: 900 -->

*將 SeaChat AI 助理與 Inline.app 助理整合，實現無縫餐廳營運管理。透過 AI 驅動的協助處理訂單、預訂和客戶諮詢。*


## 簡介
> 登入 SeaChat 後，導航到 **AI助理配置** -> **AI助理資訊** -> 選擇使用案例：**Inline.app Restaurant Assistant** 來添加整合。

## Inline.app 助理整合

Inline.app 助理整合讓您的 SeaChat 助理能夠透過 AI 驅動的對話無縫管理營運。我們目前支援無縫預訂管理，是現代企業的必備工具。
<center>
  <a href="/images/seachat/en/inline/inline_settings_staging.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/inline/inline_card.png" alt="SeaChat | Inline Restaurant Assistant | Staging Settings">
</a>

**Inline.app 助理**
</center>

## 預訂系統
簡化您的預訂流程：
- 即時座位可用性檢查
- 預訂預約和確認
- 修改和取消處理
- 客戶偏好追蹤

## 設定流程

### 步驟 1：存取整合設定
1. 登入您的 SeaChat 控制台
2. 導航至 **AI助理配置**
3. 選擇 **使用案例**
4. 選擇 **Inline.app Restaurant Assistant**
5. 按照通知視窗的指示，點擊 **確認** 重新導向到配置頁面。

<center>
  <a href="/images/seachat/zh/inline/inline_settings_staging.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/inline/inline_notify_seasalt_to_finish.png" alt="SeaChat | Inline 餐廳助理 | 測試環境設定">
</a>

*Inline.app 助理配置通知*
</center>

### 步驟 2：環境配置

<br/>
<center>
  <a href="/images/seachat/zh/inline/inline_settings_staging.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/inline/inline_settings_staging.png" alt="SeaChat | Inline 餐廳助理 | 測試環境設定">
</a>

*Inline 助理生測試環境配置*
</center>

<center>
  <a href="/images/seachat/zh/inline/inline_settings_production.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/inline/inline_settings_production.png" alt="SeaChat | Inline 餐廳助理 | 生產環境設定">
</a>

*Inline 助理生產環境設定*
</center>

配置您的環境設定：
- **生產環境**：用於實際營運
- **測試環境**：用於測試和開發




### 提示：時間感知功能

<br/>
<center>
  <a href="/images/seachat/zh/inline/inline_timeawareness.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/zh/inline/inline_timeawareness.png" alt="SeaChat | Inline 餐廳助理 | 時間感知">
</a>

*時間感知配置*
</center>

為了獲得精密的時間感知功能，我們建議在進階設定中啟用時間感知並設定您的時區。


---


### 方案與帳務

<!-- Source: seachat-payments/subscription-and-billing.md -->

<!-- Weight: 901 -->

*了解如何在 SeaChat 內管理方案與帳務，查看訂閱方案詳情、編輯帳單信息、查詢使用量以及下載歷史發票，確保您的帳務管理更高效。*


您可以在 SeaChat 的方案與帳務找到所有有關資費和帳務的信息。請在儀表板的左側邊欄找到 **方案與帳務**。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/billing-and-subscription/billing-and-subscription.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/billing-and-subscription/billing-and-subscription.png" alt="SeaChat | 方案與帳務">
</a>

**方案與帳務***
</center>

## 訂閱方案

在 **方案** 區，您可以查看當前訂閱方案的詳細資訊。點擊 **編輯方案** 按鈕可以編輯您的方案。


### 帳單明細

點擊 **費用明細** 於 **下個帳單週期** 下方，查看根據您的訂閱和使用情況的下一帳單詳情。

### 帳單收件人

在 **帳單收件人** 區段，您可以查看帳單收件人的詳細資訊。點擊 **更換收件人** 以修改帳單收件人。如果有組織名稱(統一編號)，您可以在此添加。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/billing-and-subscription/billing-recipients.png" target="_blank">
<img width="60%" style="border-radius: 0.4rem" src="/images/seachat/zh/billing-and-subscription/billing-recipients.png" alt="SeaChat | 帳單收件人">
</a>

**修改組織名稱(統一編號)**
</center>

## 餘額詳情

在 **餘額** 區段，您可以查看您的使用詳情。您的每月使用量是根據現在的方案期間的總對話數計算的。

## 帳單歷史 - 發票

在 **帳單歷史** 區段，您可以查看過去帳單的詳細資訊。點擊下載圖示以下載 PDF 格式的發票。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/billing-and-subscription/invoices.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/zh/billing-and-subscription/invoices.png" alt="SeaChat | 發票">
</a>

**下載發票**
</center>


---


## Seachat Manual

<!-- Source: seachat-manual/_index.md -->

<!-- Weight: 999 (default) -->

---
title : "SeaChat 說明書"
description: "探索 SeaChat 的完整使用指南：從入門、頻道整合，到進階 AI 功能與平台設置，以提升個人以及團隊上的工作生產力。"
lead: ""
date: 2020-10-06T08:48:45+00:00
lastmod: 2020-10-06T08:48:45+00:00
weight: 150
draft: false
images: []
toc: true
aliases:
  - /zh/seachat/seachat-manual/
---

---


### 02 Create Agent

<!-- Source: seachat-manual/02-create-agent/_index.md -->

<!-- Weight: 999 (default) -->

---
title: "創建AI助理"
description: "SeaChat: 創建AI助理"
lead: ""
date: 2024-05-08T08:48:45+00:00
lastmod: 2024-05-21T08:48:45+00:00
weight: 20
draft: false
images: []
toc: true
---

---


### 提示指令範例

<!-- Source: seachat-resources/prompt-examples.md -->

<!-- Weight: 1000 -->

*學習如何使用提示指令範例來有效訓練 SeaChat 助理，提供多元情境範例，幫助您精確控制 AI 回應，提升客戶服務品質。*


## 簡介

本教學的目的是提供如何有效且高效地訓練您的 SeaChat 助理的範例。提示指令範例僅僅是範例，並不應被視為訓練助理的唯一方法。這裡提供的範例旨在作為用戶達成某些效果的參考。然而，如果用戶有更具體的需求，他們應該根據需要微調提示指令，以達到期望的結果。

## 在定義的情境內限制機器人回答

您可以提供定義好的情境來限制 AI 助理的回答。一個好的做法是列出這些情境並詳細說明。

指示範例：

```markdown
你是{公司名稱}的客服專員，你說話親切友善而且很主動的想要幫助用戶解決問題。

你要使用口語化的詞彙，並且不可以重複使用一樣的句子回覆，要使用多元活潑的表達方式。

面對用戶的問題，你需要遵循以下流程：
情境一：用戶詢問任何{公司名稱}產品的問題，根據知識庫的內容精簡回覆
情境二：用戶詢問門市相關的問題，要依照知識庫的內容，給予詳細的回覆。
情境三：用戶詢問退換貨的問題，要依照知識庫的內容，給予詳細的回覆。如果客戶不能理解，要請他轉接客服人員。
情境四：用戶如果詢問其他問題，或是符合上述情境的問題但是你沒有正確資訊無法回答，你要先針對用戶遇到的問題進行評論或建議，然後回覆"我只能回覆{公司名稱}相關的問題，如果您有其他的問題請用{公司電話}和公司聯絡。
```

---


### SeaChat API

<!-- Source: seachat-resources/seachat-api.md -->

<!-- Weight: 1001 -->


SeaChat RESTful API 讓用戶能夠整合和自動化 AI 助理的工作流程，提供以程式化方式管理 AI 助理的靈活性。歡迎參考[API 文檔](https://wiki.seasalt.ai/zh/seasaltapi/seasalt-api/01-seachat-api-intro/)以獲取詳細資訊和無縫整合的指導。


---


### SeaChat 常見問題

<!-- Source: seachat-resources/seachat-faq.md -->

<!-- Weight: 1002 -->

*有關 SeaChat 的常見問題，這是一個 AI 聊天和語音助理平台。找到關於 SeaChat 功能、渠道等常見問題的答案。*


## 1. **我該如何更改 Seasalt 產品的密碼？**

所有 Seasalt 產品使用相同的密碼管理機制。我們只支援透過電子郵件發送登入代碼的方式來登入，每次登入時都會發送一個登入代碼，因此我們並沒有提供更改密碼的功能。

這種方式可以防止您忘記密碼或不小心洩露密碼。要登入任何 Seasalt 產品，只需輸入您的登入電子郵件，然後您將收到一個登入代碼。使用此代碼即可登入。

## 2. **LINE 按鈕將訊息截斷。如何發布完整的訊息？**

當用戶在 SeaChat 中使用 LINE 頻道時，可能會遇到訊息被截斷的問題，這通常發生在用戶點擊訊息按鈕以獲取信息時。這是由於 LINE 按鈕訊息的字符限制所致。

SeaChat 提供了解決此問題的方法。利用 KB ID 的功能可以避免訊息被截斷。您可以了解如何使用 [KB ID](https://wiki.seasalt.ai/zh/seachat/manual/add-knowledge/webpage-link/#kb-id) 功能來避免訊息被截斷。

請參閱我們的 [LINE 頻道](https://wiki.seasalt.ai/zh/seachat/manual/channels/install-to-line/#line-按鈕訊息的限制)，以了解更多有關 LINE 所施加的訊息限制的信息。

## 3. **部署 SeaChat 後，我該如何吸引更多對話**

為了吸引更多使用者，你可以採取以下兩個方法：

1. 將小工具圖示（widget icon）設為 GIF 動畫

2. 加入一個對話氣泡（bubble），若使用者在 2 秒內未點擊，則自動跳出提示（或設定其他時間）

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/seachat-resources/seachat-bubble-with-gif.gif" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/seachat-resources/seachat-bubble-with-gif.gif" alt="SeaChat 透過對話氣泡和 GIF 圖示來吸引更多使用者。">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">SeaChat 透過對話氣泡和 GIF 圖示來吸引更多使用者。</p>
</div>



你可以在「頻道 --> 網頁AI助理 --> 氣泡（第一個分頁）」中找到氣泡的設定選項。




---


### SeaChat 版本發布資訊

<!-- Source: seachat-product-updates/seachat-product-updates.md -->

<!-- Weight: 1100 -->

*掌握 SeaChat 最新版本發布資訊，了解新增功能、效能優化及錯誤修復，確保您隨時使用最穩定、最先進的 AI 助理功能。*


### 12/10/2025
##### **<font color="#739963">新功能與改進</font>**
- 於 Twilio 通話新增「閒置等待秒數」設定，可定義在無活動狀態下自動掛斷前的等待秒數。
- 新增語音信箱偵測示例；當語音助理聽到與這些示例相似的句子時，會判定為已進入使用者的語音信箱並依此採取後續動作。

### 12/04/2025
##### **<font color="#739963">新功能與改進</font>**
- 修復了在語音轉文字（STT）語言於同一語言類別內變更時，文字轉語音（TTS）語言會被錯誤同步變更的問題。

### 11/27/2025
##### **<font color="#739963">新功能與改進</font>**
- 新增會話自動超時回傳至 AI 助理時所使用的訊息設定，內容可自訂。

### 11/20/2025
##### **<font color="#739963">新功能與改進</font>**
- 分析頁面新增通話工作階段相關統計。
- 分析頁面新增可自訂的日期範圍選擇器，提供更彈性的資料分析。
- 優化通話結束後的摘要，納入更多細項與整體總結。
- 在 Twilio 通話通道與 SeaX 通話整合新增音量控制設定。

### 11/13/2025
##### **<font color="#739963">新功能與改進</font>**
- 新增 SeaX 整合類型：LINE、Messenger、Instagram。
- 優化標籤自動化所自動寄出的電子郵件內容，加入更多細節。

### 11/06/2025
##### **<font color="#739963">新功能與改進</font>**
- 新增歡迎訊息設定，可自訂新對話的起始訊息；可為文字、按鈕，或附圖的事件卡。

### 10/30/2025
##### **<font color="#739963">新功能與改進</font>**
- 修正訊息配額用盡時的處理行為：電話通話會依進階設定朗讀已用盡配額的提示訊息。

### 10/23/2025
##### **<font color="#739963">新功能與改進</font>**
- 在 SeaX 通話整合新增 TTS（文字轉語音）語言設定。
- 修正對話列表未讀數的計算，準確反映具意義對話的未讀訊息數量。
- 優化入站訊息處理速度。

### 10/16/2025
##### **<font color="#739963">新功能與改進</font>**
- 優化訊息緩衝設定功能，將可調整的延遲時間由 1–10 秒擴充至 1–20 秒

### 10/09/2025
##### **<font color="#739963">新功能與改進</font>**
- 自動標籤同時適用於當前會話標籤與對話層級標籤。
- 啟用「閒置後自動轉回 AI」時，重新啟用的舊對話不會再立即超時。

### 10/02/2025
##### **<font color="#739963">新功能與改進</font>**
- 可至AI助理資訊設計風格頁面選擇隱藏右上角選單的「在新分頁開啟聊天」；也支援上傳自訂的「新話題」圖示。
- 可至「網路聊天小工具支援全通路」頁面啟用行動版小工具的全螢幕模式。
- AI 回覆時段排程：設定 AI 回覆的時間。非排程時間則依既有對話處理模式與真人轉接設定辦理。

##### **<font color="#d66a60">問題修復</font>**
- 電話通話缺少語音轉文字的問題。
- Messenger Webhook 去重：重複通知只會被處理一次；後續仍會推出更多優化。

### 09/25/2025
##### **<font color="#739963">新功能與改進</font>**
- Messenger：支援真人客服在 24 小時之後、7 天人工作業視窗內主動發送訊息。
- LINE：真人客服可正常傳送圖片給 LINE 使用者。

##### **<font color="#d66a60">問題修復</font>**
- 評測資料集：修正了在有關聯結果存在時，無法刪除測試樣本的問題。
- 分析報表：更正真人客服訊息的來源統計。

### 09/18/2025
##### **<font color="#739963">新功能與改進</font>**
- 新增 Inline.app 助理整合設定頁面，並支援測試和正式環境的配置同時保存。

### 09/12/2025
##### **<font color="#739963">新功能與改進</font>**
- 新增 Inline.app 餐廳助手用例：可將 AI Agent 與 inline 訂位管理系統整合，支援自動訂位確認，協助餐廳提升效率並降低錯誤率。
- 自定義 GPT 工具新增「額外訊息」設定：AI Agent 完成工具呼叫與回覆後，可再自動發送一則使用者自定義的補充訊息（如下一步引導、提醒等）。

##### **<font color="#d66a60">錯誤修復</font>**
- 在 Webchat 中，使用者點擊選單卡片發送會話的第一則訊息後，卡片會消失的問題。

### 09/04/2025
##### **<font color="#739963">新功能與改進</font>**
- 在AI agent 基礎設定頁面，添加向客戶隱藏真人客服身份的選項。若啟用，真人客服仍可回覆客戶，但系統會隱藏訊息是來自AI還是真人，且主動客服請求功能將被停用。
- 修復了KB上傳url，並文件數量超過當前訂閱方案上線頁面持續加載的漏洞。
- 添加了AI助理分析儀表板和工作區分析儀表板。請見[分析教程](/zh/seachat/manual/analytics/)。

### 08/28/2025
##### **<font color="#739963">新功能與改進</font>**
- 新增自定義GPT工具，可透過上傳圖片進行商品探索。請見[客製GPT工具教程](/zh/seachat/seachat-manual/automation/custom-gpt-tool/#配置圖片搜尋工具的步驟)。
- 新增Messenger, Instagram存取權杖自動更新功能，避免存取權杖失效問題。

### 08/21/2025
##### **<font color="#739963">新功能與改進</font>**
- SeaX 通話整合新增自動掛斷功能設定
- 修復元件程式碼中的錯誤
- 更新對話閒置後的自動轉接機制：現在會依照最後一次對話後的設定時間，自動切回 AI 助理，而不再僅限於使用者傳送最後一則訊息時才進行切換。

### 08/15/2025
##### **<font color="#739963">新功能與改進</font>**
- 修正了當客製 GPT 工具開啟時，與 AI 智能助理對話出現錯誤訊息的漏洞。
- 對話頁面的篩選下拉選單，增加了根據用戶反饋表分數從高或從低開始排序對話的功能。

### 08/07/2025
##### **<font color="#739963">新功能與改進</font>**
- Meta 系列的應用（Messenger、Instagram、WhatsApp）的用戶，現在可以對 live agent 和 bot 的訊息添加表情回應，我們的 UI 也能顯示這些表情回應。
- 在 Webchat 或 Widget 中開啟對話時，第一則用戶訊息會有透明度效果，提升用戶體驗，提示對話正在加載。
- SeaChat Analytics 頁面新增 CSAT 區塊，可查看所選時間範圍內的評分，並可下載該時間範圍內所有客戶的評價內容。
- Twilio集成和SeaX電話集成新增日語與印尼語的語音聲音選項。

### 7/24/2025
##### **<font color="#739963">新功能與改進</font>**
- 調整AI助理在 Instagram 和 Messenger 的回應行為。當用戶在 Instagram上對您的Instagram Story做出反應時，不再觸發AI助理的回覆。
- 優化了SeaChat後台切換客服在線狀態的功能，使其更為即時和反應性。
- SeaX電話整合添加了真人客服轉接的功能，當用戶設置了SeaX電話號碼，並啟用了SeaChat AI智能助理時，用戶可以在SeaX電話中與真人客服進行轉接。

### 7/17/2025
##### **<font color="#739963">新功能與改進</font>**
- 修正了 Messenger 發送者傳送圖片時無法正常顯示的問題。
- 修正了在 Messenger 和 Instagram 上，當未開啟轉接摘要功能時仍顯示空白摘要標題的問題。

### 7/10/2025
##### **<font color="#739963">新功能與改進</font>**
- 工作區頁面支援移動設備顯示：用戶現在可在移動設備上登錄SeaChat，並可在工作區列表中瀏覽及管理AI助理對話。
- 調整AI助理在 Instagram 和 Messenger 的回應行為：當用戶在 Instagram 或 Messenger 上對AI助理的訊息做出反應時，不再觸發AI助理的回覆。這是優化的第一步，未來將持續推出更多改進。

### 7/3/2025
##### **<font color="#739963">新功能與改進</font>**
- 圖片上傳現已新增限制：為確保 AI agent 能準確理解圖片內容並維持良好聊天體驗，單次最多可上傳 20 張圖片。
- LINE 集成新增提醒機制：當 LINE 訊息數量用盡時，系統將自動發送提醒郵件給工作區擁有者。
- 優化 Messenger 與 Instagram 的多圖片訊息處理：修正多圖訊息拆分問題，現在所有圖片會整合為單一訊息，確保每張圖片皆能被正確識別與理解。

### 6/26/2025
##### **<font color="#739963">新功能與改進</font>**
- 新增「Deploy（佈署）」按鈕，快速整合各類平台：於後台介面上方新增「佈署」按鈕，整合並列出支援的整合平台與通訊渠道。使用者可透過此功能快速導向相關設定頁面，便捷地將 AI Agent 佈署至網站、社群平台或即時通訊工具等目標渠道。
- 全新多圖片訊息顯示介面： 多圖片訊息 UI 設計可於單則訊息中清楚呈現，提升瀏覽體驗與上下文理解的清晰度。同時，系統也優化了多張圖片的傳輸效能，讓傳送更加順暢高效。
- 優化知識庫文章上傳穩定性： 修復部分導致知識庫文章上傳不穩定的問題。

### 6/19/2025
##### **<font color="#739963">新功能與改進</font>**
- 優化 CSAT 滿意度表單顯示： 使用者現在可以直接在對話視窗中查看滿意度評分與留言內容。
- 修正登入信箱格式驗證錯誤： 解決 SeaChat 登入時，即使輸入正確的信箱格式仍被判定為錯誤的問題。
- 修正帳單頁面錯誤碼 10002： 解決新註冊用戶進入帳單頁時，顯示「找不到付費帳戶」的錯誤訊息問題。
- 修復 Twilio 無法購買電話號碼的問題：解決用戶無法透過 Twilio 購買電話號碼的錯誤。

### 6/12/2025

##### **<font color="#739963">新功能與改進</font>**

- 自訂 CSAT 表單以安裝於 Widget：您現在可以將 CSAT（顧客滿意度）表單附加至你的網頁AI助理。當使用者透過網頁AI助理互動時，表單可自動跳出，您也能從對話介面中直接查看每則對話所對應的回饋內容。請參閱[教程](/zh/seachat/manual/channels/webpage/#自定义表单客户满意度调查表单)。
- WebChat 支援多張圖片發送：SeaChat 現在支援在一次訊息中發送多張圖片，當顧客與 AI助理 聊天時，SeaChat AI助理將能夠整體理解所有圖片的內容，提供更具上下文、也更準確的回應，而非逐一處理。
- 提升時間感知準確性：修復了啟用時間感知功能時，AI助理無法正確提供在地化時間的問題。
- LINE 格式修正：解決了AI助理傳送訊息到 LINE 時，每個句子前面都會多出不必要空白字元的問題。

### 6/5/2025
##### **<font color="#739963">新功能與改進</font>**
- Instagram 登入整合：透過 OAuth 認證機制，簡化登入流程，讓您能更輕鬆地登入並將 Instagram 帳號與 SeaChat AI 助理連結。請參閱[教程](/zh/seachat/manual/channels/instagram/)。
- 圖片上傳容量提升：人工客服對話中的圖片上傳大小上限已提升至 20MB，讓您在與客戶分享視覺內容時擁有更大的彈性。

### 6/1/2025
##### **<font color="#739963">新功能與改進</font>**
- 自動標籤邏輯優化: 修正了自動標籤原本會錯誤地「取代」標籤的行為。更新後，標籤將正確地以「補丁方式」新增，讓多個標籤可以共存，而不會互相覆蓋。
- GA4 自訂支援: 您現在可以在 AI 助理資訊 > 設計樣式 > 聊天設定 中直接填入您的 GA4 Measurement ID。設定完成後，SeaChat 將開始將小工具互動資料（如發送訊息、按鈕點擊、轉接真人客服等）傳送至您的 GA4 資產，協助您深入了解使用者行為並監控效能。
- 真人客服轉接方式可自訂: 我們更新了真人客服轉接選項，讓您可以自由選擇觸發轉接的方式。現在您可以選擇：由使用者點擊按鈕提出轉接、在與 AI 對話中表達轉接意圖，或兩者皆可。
- 對話上傳圖片容量上限提升: 我們已將圖片上傳的容量上限提升至 20MB。您現在可以在對話中上傳更大、更清晰、更高畫質的圖片，分享更方便。

### 5/22/2025
##### **<font color="#739963">新功能與改進</font>**
- 真人客服轉接優化：新增無縫的真人客服轉接功能。啟用後，客戶傳送給 AI 助理的訊息將可順暢地轉接至真人客服。
- 網路對話卡片改進：新增網路對話的訊息卡片支援。當用戶點擊這些卡片時，系統會自動向您的 AI 助理發送預設問題，自動開始對話。
- LINE 訊息範本優化：改進了 LINE 範本訊息的處理方式，現在系統會將快速操作按鈕以獨立的文字訊息發送，確保按鈕在整個對話過程中保持可見。

### 5/15/2025
##### **<font color="#739963">新功能與改進</font>**
- 改進文件知識庫上傳處理：修復了上傳大型文件時導致伺服器超時的錯誤。現在用戶可以上傳大型文件，系統會將上傳作為背景處理程序，同時用戶可以處理其他事務。
- Messenger 整合 FB 嵌入式註冊：我們支援 FB 嵌入式註冊，用戶可以直接使用其 FB 帳號登錄，並選擇要與其 SeaChat AI 助理連接的 FB 頁面。請參閱[教程](/zh/seachat/manual/channels/facebook-messenger-embedded-signup/#-為什麼要使用嵌入式註冊)。

### 5/8/2025
##### **<font color="#739963">新功能與改進</font>**
- 帳單頁面的費用明細新增多語言支援，可顯示下期帳單資訊。

### 5/1/2025
##### **<font color="#739963">新功能與改進</font>**
- 優化 Messenger 對話標題顯示：修復了 Messenger 對話無法正確顯示發信者姓名的問題。現在，來自 Messenger 的對話標題會自動更新並包含發信者姓名，使對話更易識別和管理。
- 擴充 AI 助理描述字數限制：根據不同大語言模型的特性，調整並擴大了 AI 助理描述的字數上限。用戶現可更完整地描述 AI 助理的功能與特性。
- 修復語音對話錄音下載：解決了語音對話錄音下載失敗的問題，確保用戶能順利下載並存取語音對話記錄。

### 4/24/2025
##### **<font color="#739963">新功能與改進</font>**
- 上下文抽取功能優化：我們優化了`上下文抽取`功能，使 AI 助理能更精準地從用戶對話中識別並提取關鍵資訊。
- Google 日曆時區問題修復：修復了 Google 日曆整合時的默認時區設定問題。系統現在會正確識別並使用用戶瀏覽器的時區並設定正確值，避免之前因時區代碼錯誤導致的 AI 助理無法正常回覆的問題。

### 4/16/2025
##### **<font color="#739963">新功能與改進</font>**

- 人工客服模式自動禁用自動超時：在人工客服專用模式下，系統將禁用自動超時功能，這樣可以確保客服人員有充足的時間處理客戶問題。
- 移動小工具顯示優化：修正了移動端小工具的顯示問題，當只配置了一個小工具時，確保在移動設備上，只顯示一個小工具圖標。

##### **<font color="#739963">新功能與改進</font>**

- AI 助理參考資訊顯示功能優化：當用戶啟用了「顯示參考資訊」功能，且設置了 Zendesk 工單搜尋工具時，如果 AI 助理的回答引用了 Zendesk 工單內容，系統會在參考區域中顯示相關工單的編號和標題，方便追蹤資訊來源。

### 4/9/2025

##### **<font color="#739963">新功能與改進</font>**

- AI 助理參考資訊顯示功能優化：當用戶啟用了「顯示參考資訊」功能，且設置了 Zendesk 工單搜尋工具時，如果 AI 助理的回答引用了 Zendesk 工單內容，系統會在參考區域中顯示相關工單的編號和標題，方便追蹤資訊來源。


### 4/1/2025

##### **<font color="#739963">新功能與改進</font>**

- 知識庫優化：用戶現在可以在代理資訊的進階設定頁面中配置是否要優化知識庫搜尋結果，並為大型語言模型（LLM）自訂指令，說明如何優化這些結果，從而提升 AI 代理在回答用戶查詢時的表現。請參閱[教程](/zh/seachat/manual/create-agent/advanced-settings/rag/#知識庫搜索優化)。

### 3/20/2025

##### **<font color="#739963">新功能與改進</font>**

- 網頁聊天小工具氣泡功能：使用者現在可以在網頁聊天小工具旁添加引人注目的氣泡，使其在視覺上更加突出且吸引人。此功能可在網頁聊天小工具設定頁面中進行配置。

### 3/13/2025

##### **<font color="#739963">新功能與改進</font>**

- 電子郵件格式驗證：在網頁聊天表單中新增電子郵件格式驗證功能，確保客戶提供正確的電子郵件地址。
- 增強通話結束功能：當語音通話進行中時，對話詳情視窗右上角的按鈕將作為結束通話按鈕，使用者可以點擊該按鈕來終止進行中的通話。

### 3/5/2025

##### **<font color="#739963">新功能與改進</font>**

- 改善行動裝置體驗： 修正對話頁面的行動版樣式，讓使用者能更方便地查看對話並回覆客戶。
- Google 行事曆整合更新： 設定 Google 行事曆整合時，系統將自動啟用 AI 代理的時間感知功能，並使用所選時區。

### 2/26/2025

##### **<font color="#739963">新功能與改進</font>**

- 測試集導入與導出: 使用者現在可以將測試集導出為 JSON 檔案，方便備份與編輯。此外，使用者也可以透過上傳 JSON 檔案來導入測試集數據，實現更高效的批量管理。請見[教程](/zh/seachat/seachat-manual/07-test-and-improve-ai-agent/evaluation/#如何匯出評估測試集)
- 對話指派通知電子郵件: 當對話被指派給真人客服時，系統現在會自動發送電子郵件通知該客服，確保客服能夠及時收到通知並迅速處理對話。
- 可配置的語音通話自動掛斷: 使用者現在可以設定是否啟用語音通話的自動掛斷功能，當來電者說出「再見」等表達離開意圖的語句時，系統可自動結束通話，以提升通話處理效率與使用者體驗。

### 2/19/2025

##### **<font color="#739963">新功能與改進</font>**

- 評估測試：使用者現在可以透過提供測試集來評估AI智能助理的回應，每個測試樣本包含使用者查詢、標準回應，以及可選的對話歷史。AI智能助理的回應將與標準回應進行比對，測試結果顯示整體正確率和個別樣本的準確性。使用者可以調整AI智能助理並執行測試，以持續提升其效能。
- 對話標籤編輯：使用者現在可以直接在「標籤」頁面建立、編輯和刪除對話標籤。
- 知識庫 (KB) 匯出：使用者現在可以前往 知識庫 → 現有內容 → 檢視全部，並選擇匯出為 CSV 或 JSON。檔案可編輯後透過「從範本檔案上傳」重新上傳更新內容。

### 2/13/2025

##### **<font color="#739963">新功能與改進</font>**

- 自動填入聯絡表單：SeaChat 現可透過 URL 查詢字串自動填寫 WebChat 表單，無需手動輸入。請見[教程](/zh/seachat/integrations/seachat-prefill-contact-forms/)
- 修復 Instagram 空對話：防止因點讚或限時動態標記導致的錯誤通知。
- 優化 WebChat 介面：開啟對話時，改為顯示關閉圖示，取代原先的標誌，以提升清晰度。

### 2/6/2025

##### **<font color="#739963">新功能與改進</font>**

- 選擇分頁中的每頁顯示數量：分頁功能新增下拉選單，允許您選擇每頁顯示的項目數量，以便更高效地進行批量操作。
- 知識庫標題排序：您現在可以點擊排序圖示即可將文章按標題升序排列。
- 快速客戶通話：對話詳情視窗右上角新增 **呼叫客戶** 按鈕。如果客戶是透過語音頻道來電，您現在可以快速回撥給他們。
- 更新的對話歷史檔案命名格式：下載的對話歷史檔案現在遵循標格式：`含用戶名的對話標題 – 對話開始時間 – 頻道.csv`。

### 1/16/2025

##### **<font color="#739963">新功能與改進</font>**

- 頻道特定語言支援：SeaChat 現在支援為語音訊息定義每個頻道的語言。這使平台能夠將語音訊息轉錄為文字並以相同語言回覆。此設置允許用戶根據不同語言受眾的需求，調整在各種平台（包括 LINE、WhatsApp、Messenger 和 Instagram）上的溝通。此設置也適用於系統訊息，例如當用戶點擊 🧹「新話題」時發送的訊息。
- 新增語音通話小工具：聊天小工具中新增了語音通話小工具。用戶可以嵌入 HTML 代碼或 URL 到表單以接收客戶的通話。當客戶點擊通話圖標時，將彈出包含嵌入 HTML 的 iframe，或者如果提供了 URL，則會重定向到指定的表單。

### 1/9/2025

##### **<font color="#739963">新功能與改進</font>**

- 轉錄 WhatsApp 和 LINE 的語音訊息：SeaChat AI 助理現在支援轉錄通過 WhatsApp 和 LINE 發送的語音訊息。當您的客戶發送語音訊息時，SeaChat 會將其轉錄，讓您的 AI 助理能夠準確理解並回應他們的查詢。
- 新自訂 GPT 工具：Zendesk 工單搜尋：我們在自訂 GPT 工具庫中新增了一個 Zendesk 工單搜尋工具。您可以提供您的 Zendesk 帳戶資訊，以使 SeaChat 獲取工單詳情和評論，從而讓 SeaChat 根據相關工單回答用戶查詢。
- 輸入框檢測輸入語言：SeaChat 現在支援在助理的輸入框和客戶的網頁聊天輸入框中自動檢測語言。無論是從右到左 (RTL) 還是從左到右 (LTR) 的語言，輸入都會自動處理。

### 12/26/2024

##### **<font color="#739963">新功能與改進</font>**

- Instagram 小工具：用戶現在可以通過簡單地輸入 Instagram 連結並複製在 Channels 中自動生成的 HTML 代碼片段，將 Instagram 小工具嵌入到他們的網站中。
- 網頁聊天選單調整：用戶現在可以選擇隱藏「獲取 SeaChat」選項。請到AI助理設計選項中調整。
- 實時自動標籤更新：現在，自動標籤變化會立即反映在使用者介面。

### 12/19/2024

##### **<font color="#739963">新功能與改進</font>**

- 自動標籤：SeaChat 現在可以根據對話的內容自動添加或刪除標籤。用戶可以定義觸發條件，提供詳細的描述以確保準確性，並選擇要管理的標籤。
- 標籤自動化：用戶可以配置在對話中標籤變化時自動觸發的動作。用戶可以定義哪些標籤應該觸發這些動作，並配置一個或多個自動化工作流程。SeaChat 將在標籤有改動時自動執行預定義的動作。
- 現支持Instagram：SeaChat 現在支持 Instagram ，允許用戶連接他們的 Instagram 帳戶，並直接在平台中管理訊息。

### 12/11/2024

##### **<font color="#739963">新功能與改進</font>**

- 自訂 GPT 工具限制：用戶現在可以創建超過五個自訂 GPT 工具。但是，同一時間只能啟用最多五個工具。如果用戶在達到此限制後嘗試創建新工具，則該工具將成功創建，但自動停用。要啟用它，用戶需要刪除或停用當前已啟用的工具之一。
- 查看和管理長期記憶：用戶現在可以通過右鍵單擊任何對話並選擇“用戶記憶”選項來查看用戶的長期記憶。要使此選項可用，必須先在進階設置中啟用“用戶記憶”功能。
- 客服郵件可見性更新：現在，網頁聊天中將不再顯示客服郵件。相反，只會顯示客服的名稱。客服可以通過在 SeaChat 的個人資料設置中自訂顯示給客戶的名稱。

##### **<font color="#d66a60">錯誤修復</font>**

- 對話歷史下載：我們已解決了生成對話歷史下載鏈接的問題。用戶現在可以成功下載他們的對話歷史。

### 11/27/2024

##### **<font color="#739963">新功能與改進</font>**

- 擴展語言支援：在網頁聊天小工具中支援更多語言，包括英語、西班牙語、法語、日語、韓語、俄語、葡萄牙語、波蘭語、簡體中文和繁體中文。小工具中的可配置訊息會根據所選語言自動翻譯。用戶仍可根據需要自訂訊息。
- 增強自訂 GPT 工具的自動化操作：新增了兩個自訂 GPT 工具 - 發送電子郵件和發送簡訊。這些工具使 SeaChat 能夠根據您的指示自動發送電子郵件或簡訊。
- 長期用戶記憶：SeaChat 現在為 AI 助理提供長期記憶功能，使其能夠保留客戶的關鍵資訊，如偏好、過往問題和興趣。即使用戶在很長時間後回來與助理對話，AI 助理仍能記得這些資訊。
- 改進對話關鍵字搜尋：對話關鍵字搜尋現在包含對話標題，讓用戶可以通過標題搜尋，獲得更全面和準確的結果。

### 11/21/2024

##### **<font color="#739963">新功能與改進</font>**

- 回應語言設定：用戶現在可以指定 SeaChat 回應語言。使用偏好回應語言設定時，SeaChat 會偵測用戶的語言並相應回應，如果無法確定用戶的語言，則默認使用所選語言。使用強制回應語言設置時，無論用戶使用什麼語言，SeaChat 都會始終使用所選語言回應。
- 混合對話處理模式：在混合模式下，用戶現在可以設定是否允許客戶主動請求真人客服。如果啟用，客戶將在網頁聊天中看到「轉接真人客服」按鈕，或在 WhatsApp、Messenger 和 LINE 中看到快捷鍵。
- 表單完成訊息設定：用戶現在可以在網頁聊天小工具自訂表單頁面中設定用戶完成表單後發送的訊息，例如「我同意剛才提交的隱私政策」。
- 語音機器人填充詞設定：用戶現在可以在通話整合頁面和 SeaX 通話整合頁面中啟用語音機器人的填充詞功能，以獲得更快的回應，並調整其回覆中包含填充詞的機率。

### 11/14/2024

##### **<font color="#739963">新功能與改進</font>**

- Messenger 和 WhatsApp 按鈕顯示限制：我們已解決平台按鈕數量超過限制時造成的顯示問題。現在，如果按鈕數量超過限制，我們將只顯示平台允許的最大按鈕數量。
- 免費歡迎訊息和用戶表單：歡迎訊息和用戶表單填寫不再計入每月訊息配額，完全免費。
- 增強對話處理模式相容性：對話處理模式現在可以在 LINE、Messenger 和 WhatsApp 以及網頁聊天上無縫運作。當您切換到純人工客服模式時，所有客戶訊息將直接發送給您的真人客服。切換到純 AI 助理模式時，客戶訊息將完全由您的 AI 助理處理。切換到混合模式時，將保持當前對話狀態不變，但您的客戶可以通過請求返回 AI 助理或轉接真人客服來改變互動模式。

### 11/07/2024

##### **<font color="#739963">新功能和改進</font>**

- 自訂 GPT 工具結果顯示選項：用戶現在可以在編輯自訂 GPT 工具頁面中選擇工具結果在網頁聊天中的顯示方式 — 以卡片或純文字形式呈現。
- 新增 SeaChat 對話處理模式：用戶可以選擇如何管理與客戶的對話，三種模式分別為：
  - 混合模式 AI助理＋真人客服：AI 助理先處理互動，但用戶可以在需要時請求轉接真人客服。
  - 純 AI 助理模式：AI 助理獨立處理所有對話。
  - 純人工客服模式：由人工客服專門處理所有對話，此模式終身免費。
- 更新網頁聊天選單卡片的文字訊息行為：當用戶點擊選單卡片時，卡片名稱將作為用戶訊息發送，機器人將回應卡片中儲存的完整預設訊息。含有 URL 的卡片行為則維持不變。

### 10/31/2024

##### **<font color="#739963">新功能與改進</font>**

- 使用自訂 GPT 工具自動化操作：此新功能使 SeaChat AI 助理能夠查詢用戶的 API 並根據定義的條件執行自訂操作。GPT 將在適當的時間自動觸發這些操作。
- 「記憶」更名為「上下文抽取」：AI 助理的高級設置頁面中的「記憶」功能現在稱為「上下文抽取」，其功能沒有變化。
- 改善工作區列表顯示，方便用戶更好地管理配額：用戶現在可以在工作區儀表板上看到兩個工作區列表。一個是「您的工作區」，顯示用戶創建的工作區數量（第一個數字）和用戶方案允許的工作區限制（第二個數字）。另一個是「加入的工作區」，顯示當前用戶加入的其他用戶擁有的工作區。

### 10/17/2024

##### **<font color="#739963">新功能與改進</font>**

- 顯示未讀對話數量：用戶現在可以在對話標籤中看到兩個不同的通知，並且可以將滑鼠停在每個對話數量上以了解其用途。左側數字顯示總未讀訊息數量。右側數字顯示專門分配給用戶的未讀訊息，確保客服人員可以輕鬆識別其責任。
- 增強 AI 對回傳按鈕內容的理解：您的 AI 助理現在可以訪問客戶點擊的按鈕內容。這確保了 AI 助理可以準確地回應後續查詢。
- 改進網頁聊天表單和選單卡的自訂選項：用戶現在可以自訂表單中提交按鈕的文字顯示。用戶還可以選擇啟用選單卡片始終顯示。此外，選單卡片支援在點擊時向 AI 助理發送文字訊息，除了重定向到 URL，現在還有選項可以移除選單卡片的圖片。

### 10/15/2024

##### **<font color="#739963">新功能與改進</font>**

- 增加顯示Sitemap上傳進度：我們改進了用戶界面，添加了上傳進度條，讓用戶能夠實時看到Sitemap正在上傳 URL 或網站地圖。
- SeaChat 網頁聊天機器人和手機版優化：當用戶點擊網頁聊天小工具圖標時，AI 助理的網頁聊天現在將在當前標籤頁中全螢幕打開。已經解決設備屏幕上的顯示問題已得到解決，確保網頁機器人在手機上能夠完整顯示。

### 10/03/2024

##### **<font color="#739963">新功能與改進</font>**

- 人工客服分配：此功能引入了一個簡化的介面，允許用戶輕鬆分配人工客服來回應客戶。此外，新增了一個篩選器，幫助用戶快速找到已分配給他們的對話。
- 改善用量頁面：改善用量頁面，提升用戶體驗，能更詳細地看到文字和語音使用的模型和用量資訊。
- 對話標題一致性：對話標題現在與用戶的全名一致，確保對話顯示的準確性。
- Messenger 互動流程：已改進，以確保每條訊息後都能快速回覆，從而實現更順暢和更高效的通信。

### 09/27/2024

##### **<font color="#739963">新功能與改進</font>**

- AI 助理時間意識：對於每條訊息，AI 助理現在能知道當前時間，例如：「當前時間是 2024 年 9 月 11 日，星期三，太平洋標準時間上午 9:41」，以確保 AI 助理能夠更準確地回應用戶關於營業時間和其他時間相關的問題。
- SeaX 整合頁面重新設計：SeaX 整合頁面已重新設計，以提升用戶體驗。

##### **<font color="#d66a60">錯誤修復</font>**

- 網頁聊天圖標可點擊：修復了網頁聊天小工具安裝代碼導致網頁聊天圖標無法點擊的問題。

### 09/20/2024

##### **<font color="#739963">新功能與改進</font>**

- 語言支援：新增包括法語在內的多種語言支援，擴展了 SeaChat 的本地化能力。此更新提升了多語言環境下的用戶體驗。
- 年費方案：用戶現在可以訂閱新推出的年費方案，提供更靈活的計費選擇，並能利用年度方案節省費用。
- 導出對話歷史：用戶現在可以導出他們的對話歷史數據，用於自己的分析或管理目的，提供更多對通信數據和分析的控制。

##### **<font color="#d66a60">錯誤修復</font>**

- 修復 Messenger 實時客服轉接問題：解決了 Facebook Messenger 實時客服轉接快速回覆按鈕功能的問題，確保 AI 和真人客服之間的順暢過渡。

### 09/11/2024

##### **<font color="#739963">新功能與改進</font>**

- Messenger 卡片支援：您現在可以在 Messenger 上使用預設訊息按鈕和包含圖片和按鈕的卡片來增強用戶互動，為您的受眾提供更豐富、更動態的體驗。
- 跨平台圖片支援：SeaChat 網頁聊天、WhatsApp 和 LINE 整合現在支援發送和接收圖片，實現更視覺化和吸引人的跨平台溝通。
- 分析頁面：我們的新分析頁面現已向所有用戶開放。輕鬆追蹤您的 AI 助理活動，並深入了解其表現和互動情況。
- 人工客服的電子郵件偏好設置：人工客服現在可以配置他們的電子郵件偏好以接收電子郵件通知，確保更加個性化和高效的工作流程。

### 09/04/2024

##### **<font color="#739963">新功能與改進</font>**

- 增強的知識庫搜尋：現有知識庫文章的搜尋功能現採用與 RAG 搜尋方法相同的策略，提升了搜尋的準確性與效率。
- 支援 WebP 格式：現在可以上傳 WebP 格式的圖片作為圖標，提供更靈活的圖片選項。
- Google 日曆整合：用戶現在可以選擇要使用的 Google 日曆來預約，提供更多排程控制。
- 可自訂的網頁聊天小工具圖標：現在可以上傳任何圖片作為網頁聊天小工具的圖標，為您提供更多的自訂選項。
- 簡化的網頁聊天小工具安裝：所有整合頁面的網頁聊天小工具安裝代碼塊已更新，您現在可以輕鬆地複製並貼上一個代碼塊，來安裝多個小工具至您的整合渠道。

### 08/28/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 訊息配額管理：使用者現在可以在進階設定頁面設置AI助理發送的聊天和語音訊息的特定配額。
- 增強的SeaX通話整合頁面：改進了對通話速度和語音信箱設置的控制。
- 更新的UI與新標籤樣式：全新的標籤設計，提升了使用者介面的互動體驗。
- LINE實時助理訊息上限通知：當實時助理通過SeaChat發送訊息至LINE接近LINE限制時，現在會在SeaChat中收到通知。
- 增加助理描述的字數上限：助理描述現在可以包含最多3000個詞元(tokens)，允許更詳細的說明。
- 簡化的入門流程：新使用者只需上傳一個小文件或網站URL即可建立他們的第一個智能AI助理。

### 08/21/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 輕鬆複製知識庫ID：現在可以從文件的右鍵選單快速複製知識庫ID，並將其用作按鈕內容。
- 強制記憶欄位字符限制：記憶欄位現在有1024個詞元(tokens)的嚴格限制。
- 知識庫配額頁面：推出知識庫配額頁面，有助於您高效地追踪和優化文件及詞元(tokens)的使用情況。
- 更新的標籤樣式：享受全新設計的標籤樣式，更直觀、現代的介面。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 修正電子郵件中的聊天參與者名稱：修正了一個問題，該問題導致在「收到新訊息」的電子郵件中顯示隨機值，而不是正確的聊天參與者名稱。

### 08/15/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 替換AI助理更簡單：現在可以在助理管理頁面中直接替換AI助理，使開發更加便捷。
- 改進測試AI助理按鍵位子：移動「測試 AI 助理」按鈕到頁面上方，測試更方便。
- 擴展上下文窗口：為先進的大型語言模型（如 GPT-4o、GPT-4o mini 和 Mistral Large）開啟 128K 上下文窗口(context window)。
- 增強知識庫內容管理：使用 $KB*ID* 標頭和知識庫文檔 ID 作為按鈕內容，以便通過按鈕交互直接簡化訪問知識條。

### 08/08/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 引入卡片式助理列表頁面：全新設計，以更直觀和有條理的方式瀏覽助理。
- 新增語言模型模型切換功能：用戶現在可以直接從界面切換不同的大型語言模型，包括 GPT-4o mini、GPT-4o 和 Mistral Large。
- 自動轉接回 AI 助理：若真人客服不回應，則在自定義分鐘後，自動轉回 AI 助理。
- 自定義「真人客服已離開對話」消息：用戶可以設計真人客服退出聊天時出現的消息。
- 自定義真人客服轉接特定短語：允許用戶設置特定短語，以觸發從 AI 助理無縫轉接到真人客服的對話。

### 08/01/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 安裝各種頻道的圖示到網站上：只需複製並粘貼一段程式碼，即可輕鬆在您的網站上安裝多個對話圖示：SeaChat AI Agent 網頁聊天、LINE、WhatsApp 和 Facebook Messenger。
- 改進彈出窗口：體驗更友好的彈出窗口，幫助您輕鬆追蹤知識庫配額限制的使用情況。
- 未讀訊息通知：新的瀏覽器標籤頁通知讓未讀消息更為醒目。
- 高級 Twilio 通話設置：為進出電話配置速度調整，並可選擇在外撥語音信箱中發送可自定義的語音信箱訊息或自動掛斷。

### 07/25/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 知識庫限制：針對不同SeaChat方案進行知識庫用量限制，包括文件大小、文件數量和令牌數量的限制。
- 改進方案降級流程：用戶會收到通知，建議他們刪除多餘的AI助理、文件和工作區成員，讓用戶能在降級生效之前進行必要的資料清理。

### 07/19/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 增加了播放和下載錄音音頻的支持
- 進階方案功能：啟用記憶的選項僅適用於進階方案
- 進階方案提示：新的提示，用於管理多個進階功能，包括添加成員、AI助理、工作空間、啟用記憶和設置語音助理
- 純文本URL現在在網頁聊天中可點擊

### 07/11/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 為新用戶自動創建工作區
- 允許進階方案隱藏Seasalt.ai SeaChat 品牌字樣

### 07/04/2024

##### **<font color="#739963">新功能和效能優化</font>**

- AI助理列表頁面：為了保持一致性，只顯示第一行提示。
- SeaChat 產品頁面現在支援葡萄牙語、韓語、俄語、西班牙語和越南語。
- 新增了一個中文的語音合成（TTS）聲音：Tongtong聲音。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 修復了AI助理設計樣式無法保存的錯誤。

### 06/26/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 現在用戶只需點擊一下即可創建工作區
- 使用頻道圖標標籤對話
- 改善試算表格上傳選項的用戶介面
- 免費方案中的免費消息數量修訂為終身使用100條消息

### 06/13/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 支援 LINE 卡片訊息及按鈕訊息，豐富您的對話內容。
- 增強用戶體驗：改進增加按鈕到列表的行為。
- 訊息回應支援網址連結：支持 URL 和 Markdown 格式。

### 06/04/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 介面調整：在 AI 助理資訊中增加設計風格，讓您更好地設計對話介面。
- 新增 WordPress 整合：您現在可以將 AI 助理部署到 WordPress 上。
- 新增 MailerLite 整合：您現在可以將 AI 助理蒐集到的客戶資訊同步到MailerLite。
- 新增整合頁面與頻道設計：提供新的整合選項和更佳的頻道設計。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 修復多個知識庫錯誤：包括刪除知識庫和文件錯誤訊息的問題。

### 05/30/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 知識庫文件：現在您可以直接覆蓋具有重複名稱的文件，讓更新文件更加便捷。
- 新增聊天窗口刷新按鈕：當WebSocket斷線時，您可以點擊按鈕刷新聊天窗口。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 修復創建工作區的錯誤：已解決在創建工作區過程中遇到的錯誤。

### 05/24/2024

##### **<font color="#739963">新功能和效能優化</font>**

- 資料庫更新：改善資料庫的文件名稱，讓您更好地查看文件。
- 自動覆蓋檔案：當您上傳重複的檔案名稱時，您可以選擇覆蓋原先的檔案進行更新。
- 優化資料庫切換流暢性：增強資料庫切換的流暢度。
- 新增客戶服務入口：我們在服務介面的左側增加了客戶服務入口，如您有任何問題，隨時可以聯繫我們，提供最佳體驗是我們的最大動力。
- 電子郵件模板調整：為SeaChat電子郵件，我們修改了郵件模板，使您更容易查看信件。

### 05/18/2024

##### **<font color="#739963">新功能</font>**

- 新增郵件語言設置，並使郵件通知更易讀（現在您可以通過 SeaChat@seasalt.ai 接收聊天郵件通知）
- 增設RAG（檢索增強生成）查詢模式、檢索方法和檢索計數，以增強資料檢索和AI助理回應的準確性。
- 增加當用戶清空對話時自動清除 Memory 資訊。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 修正上傳 CSV 和 Excel 文件的問題，解決上傳失敗以及白畫面問題。
- 修復遺失的知識庫資料及回答相關資料。
- 修復回覆訊息中連結失效的問題。
- 修正字串問題，並更新了使用案例庫。

### 05/02/2024

##### **<font color="#739963">新功能</font>**

- 上傳表格優化：在上傳表格頁面，用戶現在可以選擇將每一行資料作為單獨的知識庫文件上傳，或作為單一文件一起上傳。
- 新增 Wix 頻道：您現在可以將您的 Agent 部署至 Wix 平台。
- 資料庫增強：重構知識庫資料，優化資料擷取與解讀。
- Shopify 與 Squarespace 頻道介面優化：增強用戶介面，使這些平台上的操作更加流暢。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 修正自動填入 Survey use case 的Agent的描述。
- 修正在 Survey Use Case 模板中的 Live Agent 轉接行為。

### 05/02/2024

##### **<font color="#739963">新功能</font>**

- 上傳表格優化：在上傳表格頁面，用戶現在可以選擇將每一行資料作為單獨的知識庫文件上傳，或作為單一文件一起上傳。
- 新增 Wix 頻道：您現在可以將您的 Agent 部署至 Wix 平台。
- 資料庫增強：重構知識庫資料，優化資料擷取與解讀。
- Shopify 與 Squarespace 頻道介面優化：增強用戶介面，使這些平台上的操作更加流暢。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 修正自動填入 Survey use case 的Agent的描述。
- 修正在 Survey Use Case 模板中的 Live Agent 轉接行為。

### 04/19/2024

##### **<font color="#739963">新功能</font>**

- 新增用例庫頁面：便於您輕鬆創建 AI 機器人。
- 增強客戶資料連接：您現在可以在對話紀錄列表中快速複製客戶的郵件。
- 更新 WhatsApp/Messenger 設置流程：改善頻道綁定的體驗。
- 新增進階功能“記憶”：記錄歷史對話的重點資訊，並結合調查類型的使用案例模板，可通過對話幫助您調研用戶需求與特性。

### 04/09/2024

##### **<font color="#739963">新功能</font>**

- 為 WhatsApp 和 Meta Facebook Messenger 頻道增加了移除按鈕，讓用戶可以輕鬆解綁帳號。
- 新增功能，於完成電子郵件表單後顯示終端用戶的電子郵件，提升用戶互動。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 修正創建AI助理過程中的錯誤，使AI助理創建更加流暢。
- 解決編輯AI助理時的相關錯誤，確保修改和更新更加順暢。

### 04/02/2024

##### **<font color="#739963">新功能</font>**

- 新建立創建AI助理門戶網站，使創建您的助理變得更加容易。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 改善 WhatsApp 的回應，減少錯誤亂碼回應的情況。
- 改善 AI Agent 回應停滯與無法回應的狀況。

### 03/28/2024

##### **<font color="#739963">新功能</font>**

- 支援新的社交媒體渠道： 新增 Meta Facebook Messenger 和 WhatsApp 渠道，讓 AI Agent助理能夠拓展到更多平台。
- 支援新的網站架設平台： 新增對 [Shopify](https://wiki.seasalt.ai/seachat/seachat-manual/05-integrations/02-seachat-shopify-integration/) 和 [Squarespace](https://wiki.seasalt.ai/seachat/seachat-manual/05-integrations/03-seachat-squarespace-integration/) 的支援。
- 新增使用案例： 新增 5 個使用案例，讓創建 Agent 變得更加便利。
- 登錄流程優化： 使用 Google 帳號註冊流程更加輕鬆。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 支援 LINE 貼圖，提供更好的客戶答覆體驗。
- 在 WhatsApp 和 Meta Facebook Messenger 中增加 `/live_agent` 轉接功能。
- 修正 Live agent 狀態顯示錯誤。
- 修正 Live agent 回應錯誤信息的問題。

### 03/14/2024

##### **<font color="#739963">新功能</font>**

語言模型優化：

- 升級 SeaChat 助理模型。
- 改善預約服務提示詞流程。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 修正摘要的隨機語言顯示問題。

### 03/07/2024

##### **<font color="#739963">新功能</font>**

- 知識庫：支持視頻、音頻和試算表文件，使內容分享和協作更加全面。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 增加對較長視頻和音頻文件的支持，最長持續時間為15分鐘。
- 修復了上傳試算表功能不正常的問題。
- 在成員設定中調整AI助理指派時，不再顯示角色變更的付款提示。

### 03/04/2024

##### **<font color="#739963">新功能</font>**

- 賬單歷史現在提供發票下載選項。

### 02/23/2024

##### **<font color="#739963">新功能</font>**

- 新增郵件通知設定，用於接收即時客服請求和新用戶對話。
- 用戶可在與即時客服互動後切換回 AI 客服。

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 大幅縮短創建新工作區所需時間。

### 01/24/2024

##### **<font color="#739963">新功能</font>**

- 設定預設回覆語言: 想讓你的AI助理用適合的口吻和語言回答客戶問題嗎？現在可在「AI助理配置」功能表設定預設回覆語言，確保助理回覆品質，現支持美式英文、英式英文、繁體中文、簡體中文。

<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/zh/20240124-preferred-response-lang.png" alt="Set up a separate text channel just for live transcriptions from SeaVoice STT.">
</center>

##### **<font color="#d66a60">改進與錯誤修復</font>**

- 預覽AI助理網頁外觀: 修正網頁助理外觀預覽顏色bug。


---
