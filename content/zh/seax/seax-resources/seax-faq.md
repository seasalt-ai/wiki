---
title: "SeaX 常見問題 (FAQ)"
description: "SeaX | SMS 常見問題"
date: 2024-10-16T08:48:57+00:00
lastmod: 2024-10-16T08:48:57+00:00
draft: false
images: []
weight: 1
toc: true
---

## 1. 什麼是 Twilio 30007 錯誤？它如何影響大量簡訊發送？

Twilio 30007 錯誤發生在您的訊息被電信運營商過濾時。這可能會影響大量簡訊發送計畫。要了解如何避免此問題，請參閱這篇[部落格文章](https://seasalt.ai/blog/102-twilio-30007-errors/)。

## 2. SMS中是如何給聯繫人打上"DNC"標籤的？

當一個聯繫人回復SMS包含以下字眼時，就會自動被打上“DNC”標籤：

stop, cancel, end, quit, stopall, unsubscribe, remove me, stop sending me messages, wrong person, wrong number.


## 3. WhatsApp中是如何給聯繫人打上"DNC"標籤的？

和SMS一样，當一個聯繫人回復SMS包含以下字眼時，就會自動被打上“DNC”標籤：

WhatsApp還額外有一個"Stop Promotions"按鈕（屬於Quick Reply按鈕），當聯繫人點擊這個
按鈕時，也會被自動打上DNC標籤：


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-resources/stop-promotions.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-resources/stop-promotions.jpeg" alt="Stop Promotions to capture DNC">
</a>
</center>


WhatsApp Campaign的發送人可以在WhatsApp模板中設置這類按鈕，在Meta中叫做
“Marketing opt-out”:

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-resources/setup-stop-promotions.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-resources/setup-stop-promotions.jpeg" alt="Stop Promotions to capture DNC">
</a>
</center>


## 4. 為什麼我的 WhatsApp 行銷活動出現「付款方式 (payment method)」錯誤？

如果您看到錯誤訊息：「由於與您的付款方式相關的一項或多項錯誤，訊息發送失敗 (Message failed to send because there were one or more errors related to your payment method)」，這表示 Meta 無法收取主動發送訊息的費用。Meta 會針對每條由企業發起的訊息收取費用。

要解決此問題：
- 請確保您的 WhatsApp 帳戶已在 **Meta 企業管理平台 (Meta Business Suite)** 中綁定有效的信用卡。
- 在 **WhatsApp 管理員 (WhatsApp Manager)** 中驗證您的帳單資訊（這與您的 SeaX 訂閱是分開的）。

## 5. WhatsApp 中的「失敗（訊息無法送達）(failed (Message Undeliverable))」錯誤是什麼意思？

此錯誤通常表示 Meta 或收件者封鎖了您的訊息。最常見的情況是 Meta 的自動系統將該訊息標記為潛在垃圾訊息，尤其是當您向從未主動聯絡過您企業的「陌生」聯絡人發送訊息時。

## 6. 如何才能穩定地向 WhatsApp 上的「新」客戶發送訊息？

Meta 嚴格控制垃圾訊息行為，可能會封鎖發送給完全陌生人的訊息。為了提高送達率：
- **鼓勵主動聯絡**：請您的聯絡人先給您發送一條訊息。一旦他們發起了對話，Meta 就更有可能允許您發送行銷模板。
- **WhatsApp 共存 (WA Coexistence)**：您可以在行動裝置上登入您的 WhatsApp 商業帳戶 (WABA) 先與聯絡人取得聯繫。一旦他們接受並回覆後，您將來就可以透過 SeaX 向他們發送行銷活動訊息。

## 7. 如果 WhatsApp 繼續封鎖我的訊息該怎麼辦？

如果您在透過 WhatsApp 接觸新客戶時遇到困難，可以考慮切換到 **SMS 簡訊**。電信運營商通常不會像 Meta 那樣封鎖初始開發訊息，且在許多地區（如澳洲），發送 SMS 的成本與 WhatsApp 訊息相近。