---
title: "SeaX FAQ"
description: "Bulk Messagign FAQ for SMS & WhatsApp"
date: 2024-10-16T08:48:57+00:00
lastmod: 2024-10-16T08:48:57+00:00
draft: false
images: []
aliases:
   - /seax/seax-resources/seax-faq/
url: /en/seax/seax-resources/seax-faq/
weight: 1
toc: true
---

## 1. What is the Twilio 30007 error, and how does it affect bulk messaging?
   
The Twilio 30007 error occurs when a carrier filters your message. This can disrupt bulk campaigns. To learn how to prevent this, check out this [blog](https://seasalt.ai/blog/102-twilio-30007-errors/).

## 2. How are "DNC" labels captured in SMS?

“DNC” labels are added to a recipient if they reply the following phrases: stop, cancel, end, quit, stopall, unsubscribe, remove me, stop sending me messages, wrong person and wrong number.


## 3. How are "DNC" labels captured in WhatsApp?

Same as SMS, “DNC” labels are added to a recipient if they reply the following phrases: stop, cancel, end, quit, stopall, unsubscribe, remove me, stop sending me messages, wrong person and wrong number.

Additionally, WhatsApp provides a button specifically to unsubscribe from marketing messages like the following “Stop Promotions” button:

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-resources/stop-promotions.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-resources/stop-promotions.jpeg" alt="Stop Promotions to capture DNC">
</a>
</center>


If a user clicks on it, then the “DNC” label will be applied to the user.

A marketer can insert this “Stop promotions” button by selecting the “Marketing opt-out” as the Quick Reply type button:

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-resources/setup-stop-promotions.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-resources/setup-stop-promotions.jpeg" alt="Stop Promotions to capture DNC">
</a>
</center>


## 4. Why am I getting a "payment method" error in my WhatsApp campaign?

If you see the error: "Message failed to send because there were one or more errors related to your payment method," it means Meta was unable to charge for the proactive message. Meta charges a fee per business-initiated message sent.

To fix this:
- Ensure you have a valid credit card associated with your WhatsApp account in the **Meta Business Suite**.
- Verify your billing information in the **WhatsApp Manager** (this is separate from your SeaX subscription).

## 5. What does the "failed (Message Undeliverable)" error mean in WhatsApp?

This error typically means that either Meta or the recipient has blocked your message. Most often, Meta's automated systems flag the message as potential spam, especially if you are sending to "cold" contacts who have not messaged your business first.

## 6. How can I reliably send messages to "new" customers on WhatsApp?

Meta strictly controls spamming behavior and may block messages to complete strangers. To improve deliverability:
- **Encourage Inbound**: Ask your contact to send you a message first. Once they initiate the conversation, Meta is much more likely to allow your marketing templates.
- **WhatsApp Coexistence**: You can use your WhatsApp Business Account (WABA) on a mobile device to reach out to a contact first. Once they accept and respond, you can send future campaigns to them via SeaX.

## 7. What if WhatsApp continues to block my messages?

If you are having difficulty reaching new customers via WhatsApp, you can switch to **SMS**. Carriers generally do not block initial outreach in the same way Meta does, and in many regions (like Australia), the cost of sending SMS is similar to WhatsApp.