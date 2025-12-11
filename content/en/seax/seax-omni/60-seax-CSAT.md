---
title: "Customer Satisfaction (CSAT) Survey"
description: "Configure, send, and interpret Customer Satisfaction (CSAT) surveys across all connected channels to measure customer experience and agent performance."
date: 2024-12-10T08:48:57+00:00
lastmod: 2024-12-10T08:48:57+00:00
draft: false
images: []
menu:
  seax:
    parent: "seax-omni"
aliases:
  - /en/seax/csat/
  - /seax/csat/
  - /seax/seax-messaging/csat/
url: /en/seax/seax-omni/csat/
weight: 60
---

Collect actionable feedback with customizable, automated, and manually-triggered post-conversation surveys.

Customer Satisfaction (CSAT) surveys help you understand how customers feel about their interaction with your support team. With SeaX, you can configure a custom CSAT message, let agents send it manually, or automate delivery based on your own timing rules. The system intelligently parses customer replies and ensures feedback collection is smooth and unobtrusive.

---

## Why CSAT Matters

CSAT surveys provide measurable insights into customer experience. By using CSAT, support teams can:

- Track satisfaction trends over time
- Identify low-rated conversations and root causes
- Drive agent coaching and quality improvements
- Automate feedback collection to reduce manual work
- Maintain compliance with channel-specific messaging rules

---

## Where to Configure CSAT in the UI

1. Navigate to: **Side Menu → Workspace → Channels**

2. Click the card to open a configuration popup where CSAT settings can be enabled.

CSAT surveys are available for these channels: LINE, WhatsApp, Instagram, and Messenger. Don't see a channel you need? Contact our support team to discuss your requirements at [info@seasalt.ai](mailto:info@seasalt.ai).
<br/>

<center>
<a href="/images/seax/en/csat/CSAT_Entry.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Entry.png" alt="An image that shows how to navigate to the dashboard of agent creation.">
</a>

</center>

<br/>

---

## Enabling and Customizing CSAT Surveys

Inside the channel configuration popup:

### 1. Enable CSAT

Toggle **Enable Customer Satisfaction Survey**.

### 2. Write the CSAT Message

Enter the message you want customers to receive.

Important guidelines:

- Only replies **1, 2, 3, 4, or 5** are counted as valid CSAT ratings.
- Your message should clearly instruct customers to reply with a single digit.  
   Example:  
   “Please rate your experience from 1–5 by replying with a number.”
  <br/>

<center>
<a href="/images/seax/en/csat/CSAT_Config_Manual.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Config_Manual.png" alt="An image that shows how to navigate to the dashboard of agent creation.">
</a>

</center>

<br/>

### 3. Save Changes

Once saved, CSAT becomes available for both manual and automated sending for this channel.

## Manually Sending CSAT Surveys

Agents can send a CSAT survey anytime during a conversation.

How:

1. Open a conversation
2. Click the **CSAT icon** in the **top-right corner** of the conversation window
   <br/>

<center>
<a href="/images/seax/en/csat/CSAT_Send_Btn.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Send_Btn.png" alt="An image that shows how to navigate to the dashboard of agent creation.">
</a>

</center>

<br/>

### Meta Channel Restrictions

For Instagram, Messenger, and WhatsApp:

- The customer must have sent a message within the **last 24 hours**
- If outside the 24-hour window, the CSAT icon is **disabled** per Meta policy

You may manually send CSAT surveys as many times as needed.

---

## Automatically Sending CSAT Surveys

### 1. Enable Auto-Send

Toggle **Automatically send the survey after a set delay**.

### 2. Configure Delay Time

Set the number of minutes to wait after the **customer’s last inbound message** before automatically sending the CSAT survey.

<br/>

<center>
<a href="/images/seax/en/csat/CSAT_Config_Auto.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Config_Auto.png" alt="An image that shows how to navigate to the dashboard of agent creation.">
</a>

</center>

<br/>

### How Auto-Sending Works

- A countdown begins after each inbound user message
- When the delay expires, the survey is automatically sent
- If the customer does not respond with a valid rating, the system will **retry sending** after each delay window, always based on the most recent inbound message
- Auto-sending triggers **once per conversation**, but retries continue until a valid rating is received
- Manual sending remains available at all times

---

# How CSAT Reply Parsing Works

Understanding how the system reads customer replies is critical to setting expectations.

### When a CSAT survey is sent:

The system monitors the **immediate next inbound customer message** and interprets it as follows:

---

## Case 1 — Customer replies with a valid rating (1–5)

- The system successfully parses the rating
- The rating is recorded as the CSAT score
- All automatic resend attempts stop
- No further messages will be considered CSAT replies

<br/>

<center>
<a href="/images/seax/en/csat/CSAT_Demo.gif" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Demo.gif" alt="An image that shows how to navigate to the dashboard of agent creation.">
</a>

</center>

<br/>

---

## Case 2 — Customer replies with an invalid message

Examples:

- “Thank you!”
- “Okay.”
- emojis

System behavior:

1. The system **cannot parse** a valid rating
2. The message is treated as a **normal inbound message**
3. The system **will not** treat any future messages as CSAT replies
4. Auto-sending will continue retrying as configured
5. Agents may manually resend a CSAT survey at any time

This ensures the conversation flow remains natural and customers are never stuck in “survey mode.”

<br/>

<center>
<a href="/images/seax/en/csat/CSAT_Demo_Invalid.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Demo_Invalid.png" alt="An image that shows how to navigate to the dashboard of agent creation.">
</a>

</center>

<br/>

---

## Case 3 — Customer does not reply at all

- Auto-send will retry sending the CSAT survey after new inbound message arrives
- Agents may manually send CSAT whenever appropriate
