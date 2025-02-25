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