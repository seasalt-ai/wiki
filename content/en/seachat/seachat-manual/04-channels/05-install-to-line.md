---
title: "LINE Official Account"
description: "Enhance your LINE Official Account by integrating auto-response in LINE with SeaChat AI agents."
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-05-13T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /en/seachat/seachat-manual/04-channels/05-install-to-line/
  - /seachat/seachat-manual/05-install-to-line-and-web/
  - /seachat/seachat-manual/04-channels/05-install-to-line/
url: /en/seachat/manual/channels/install-to-line/  
weight: 501
toc: true
---


## :movie_camera: Integrate SeaChat with Your LINE Official Account

Follow the video tutorial to install SeaChat on your LINE Official Account and start responding to customer messages!

<iframe  width="100%" height="400" src="https://www.youtube.com/embed/5YCiO8GEAu0?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>


## Utilize SeaChat and LINE's Auto-Response Messaging Functionality Together

You can use SeaChat as an AI assistant providing useful information, capable of understanding various questions and answering based on the knowledge base, while the LINE keyword auto-response function is mainly used to trigger actions and send media messages such as coupons, card messages, and videos. By combining the functionalities of SeaChat and LINE auto-response, you can effectively enhance user experience and strengthen interaction with customers.

|                                  | Line Automatic Response                                                                                  | SeaChat AI Assistant                                                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Natural Language Understanding**            | None                                                                                                     | Yes                                                                                                                                                                              |
| **Data Setup/Training**          | One-time keyword setup                                                                                   | Supports multiple file formats                                                                                                                                                   |
| **Message Types**                | Images, Text, Videos, etc.                                                                               | AI Text Messages                                                                                                                                                                 |
| **Keyword Setup**                | Yes                                                                                                      | Yes                                                                                                                                                                              |
| **Summary of Customer Conversations** | No                                                                                                       | Yes                                                                                                                                                                              |
| **Switch to Human Customer Service**  | No                                                                                                       | Yes                                                                                                                                                                              |
| **Suitable Scenarios**           | Fixed responses for brand/product related keyword-triggered basic responses                              | Highly contextual answers based on knowledge base, flexible and personalized responses, can be used for product recommendations, customer service, and collecting customer information, etc. |

<br/>
<center>

*LINE Automatic Response v.s. SeaChat AI Assistant*
</center>
<br/>

### Configuration Steps

1. Choose "Manual chat + auto-response" for LINE responses setting.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/choose-manual-chat-plus-auto-response-for-line-responses-setting.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/choose-manual-chat-plus-auto-response-for-line-responses-setting.png" alt="Choose manual chat plus auto-response for LINE responses setting">
</a>

*Choose manual chat plus auto-response for LINE response setting*
</center>
<br/>

2. To avoid duplicate responses, change LINE's auto-response to keyword response by going to [LINE Business](https://manager.line.biz/) > Auto-Response Messages > Click on Keyword Response.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/change-lines-auto-response-to-keyword-response.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/change-lines-auto-response-to-keyword-response.png" alt="Change LINE's auto-response to keyword response">
</a>

*Change LINE's auto-response to keyword response*
</center>
<br/>

3. Add the desired keywords to the keyword response and set up the messages, for example - the keyword for business hours could be: store hours, business hours, etc. And in the message setting, input: "We are open Monday to Friday, 9am to 6pm."

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/add-keywords-to-keyword-response.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/add-keywords-to-keyword-response.png" alt="Add keywords to keyword response">
</a>

*Add keywords to keyword response*
</center>
<br/>

4. Open SeaChat and add a knowledge base document.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/seachat-knowledge-base.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/seachat-knowledge-base.png" alt="Add knowledge to SeaChat knowledge base">
</a>

*Add knowledge to SeaChat knowledge base*
</center>
<br/>

5. Enter these keywords into the document title of SeaChat and provide additional explanations in the document text: You can write additional messages, such as appointment links, transferring to customer service, etc., and adjust the weight to 75.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/enter-keyword-response-into-seachat-knowledge-base.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/enter-keyword-response-into-seachat-knowledge-base.png" alt="Enter keyword response into SeaChat knowledge base">
</a>

*Enter keyword response into SeaChat knowledge base*
</center>
<br/>

6. SeaChat AI Assistant will not repeat responses on LINE, and can help expand knowledge for your customers to improve their experience. LINE messages can be set as images, videos, and for more contexual responses, you can rely on SeaChat.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/LINE-text-messages-you-can-rely-on-seachat.png" target="_blank">
<img height="100%" width="50%" src="/images/seachat/en/channels/line/LINE-text-messages-you-can-rely-on-seachat.png" alt="LINE text messages you can rely on SeaChat">
</a>

*Respond to Customers using SeaChat and LINE auto-responses*
</center>
<br/>

## Managing LINE and SeaChat Integration

### Option 1: Completely Disable LINE Live Chat

**Step 1:** Disable the LINE live chat feature.

**After Disabling:**

* You can then use SeaChat's features to replace LINE's auto-reply and live chat functions, with all conversation records being saved in SeaChat.

### Option 2: Using Both Platforms Simultaneously

In this setup, both LINE and SeaChat can respond to incoming messages. However, special attention is needed when managing replies from each platform. Users can switch between the LINE backend or the SeaChat backend for live chat.

#### Auto-Reply:

* SeaChat can automatically respond to messages. These replies will appear in both the LINE backend and the SeaChat backend.

#### Live Reply from LINE Backend:

**Advantages:**

* Live replies will be fully displayed in the LINE backend.

**Disadvantages:**

* Live replies will not be shown in the SeaChat backend.
* SeaChat won't be aware that a live reply has been sent from LINE, so it will continue to send its own reply. This may result in the user receiving two responses: the SeaChat reply (usually the first) and the live reply from the LINE backend.
* Using SeaChat to reply incurs a cost of approximately NT$0.3 per message (GPT-3.5) or NT$0.18 per message (GPT-4o-mini).

#### Live Reply from SeaChat:

**Advantages:**

* Live replies will be fully displayed in the SeaChat backend.

**Disadvantages:**

* Live replies will not be shown in the LINE backend.
* These replies will count against LINE's monthly message limit (200 messages per month for free users). If the monthly limit is reached, you won't be able to send additional messages without upgrading your plan.

## LINE's Pricing Strategy

* Live replies sent through the LINE Official Account Manager do not count toward the free message quota.
* For detailed pricing, refer to the official pricing information: [LINE Official Account Manager Pricing](https://tw.linebiz.com/column/LINEOA-2023-Price-Plan/)

### Which Types of Messages Are Charged?

* Only "Broadcast Messages," "Push API Messages from the Advanced Features of the Messaging API," and "Progressive Messages" are counted toward the message limit. The following types of messages are considered "free":
    * Welcome messages for new friends.
    * One-on-one live chat messages.
    * Auto-reply messages.
    * AI auto-reply messages.
    * Messaging API's Reply API.

<br/>


## Limits of LINE Button Messages

When users are using the LINE channel with SeaChat, they may encounter issues where the button message is cut off when the message button is clicked. This is due to the character limit for the LINE button message.

Here is a summary of the current limits for our button templates and postback buttons:

- **Message character limit**: 200 characters

- **Postback button content character limit**: 300 characters across all buttons

- **Postback button number limit**: Up to 4 buttons

For detailed reference, please visit the following sections on LINE's developer documentation:

Button template message character limit and number of buttons limit under the [Buttons Template](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages) section.

Postback Button’s content character limit under the [Postback Action](https://developers.line.biz/en/docs/messaging-api/actions/) section.

SeaChat has a solution for this issue. Utilize the feature of KB ID to avoid the message being cut off. Please check out our wiki about [KB ID](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/webpage-link/#kb-ids) for more information on how to avoid the message being cut off.

## LINE's AI Auto-Reply Function Will Be Discontinued Soon

[LINE's AI auto-response function](https://tw.linebiz.com/manual/line-official-account/oa-manager-smartchat/) will be discontinued in May 2024.

If you are still using the AI auto-response function, make sure to arrange alternative solutions soon.

## 🔖 FAQ

### How do the customers know that the Live Agent has left the chat?

When the Live Agent finishes a conversation, he/she can click on the **Complete** button. The customer will see a message saying that **the Live Agent has left the conversation.**

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/faq-1.png" target="_blank">
<img height="50%" width="100%" src="/images/seachat/en/channels/line/faq-1.png" alt="LINE text messages you can rely on SeaChat">
</a>

</center>
<br/>

### Can I set an activation time for my AI Agent to start the conversation automatically? 

Currently, we do not support setting an activation time for the AI Agent to start the conversation automatically. However, you can easily turn on the AI Agent by clicking on **Complete** button in a conversation once you have finished your conversation. Refer to our [tutorial](/en/seachat/seachat-manual/02-create-agent/02-live-agent-transfer) for more information.

### Can I see the response of the AI Agent in the LINE chat?

Yes, you can see both the agent's and live agent's responses. You will have a complete overview of the chat. However, we recommend using SeaChat's conversation platform to have a better overview and control of all the conversations.

### Why does my button says "Live Agent" in my LINE Channel? How can I change it to Chinese?

To change the language of your button from English to Chinese in the UI of your LINE channel, you should go to the **Webchat Widget** channel.

In **Channels**, find the **Webchat Widget** channel. Modify the language to Chinese in the **Basic Settings**. This will then change the language of the buttons in the UI of your LINE chat. Now it should say **真人客服** instead of **Live Agent**.

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/agent-information/webchat-settings-for-thrid-parties.png" target="_blank">
      <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/webchat-settings-for-thrid-parties.png" alt="image that displays the additional options in Chat Settings">
    </a>
  </div>
  <p style="margin-top: 20px; font-size: 15px">Webchat Chat Settings and Basic Settings</p>
</div>
