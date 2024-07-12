---
title: "LINE Official Account"
description: "Use SeaChat AI Chatbot for your LINE Official Account to enhance customer experience. SeaChat can work with LINE's auto-response feature to optimize customer interactions."
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-05-13T08:48:57+00:00
draft: false
images: []
menu:
seachat:
parent: "seachat-manual"
aliases:
  - /en/seachat/seachat-manual/04-channels/05-install-to-line/
weight: 50
toc: true
---


## :movie_camera: Integrate SeaChat with Your LINE Official Account

Follow the video tutorial to install SeaChat on your LINE Official Account and start responding to customer messages!

<iframe width="100%" height="400" src="https://www.youtube.com/embed/?listType=playlist&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


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

### The chat is in English but the UI is in Chinese. How do I change the UI language to English?

You should go to the **Webchat Widget** channel.

In **Channels**, find the **Webchat Widget** channel. Modify the language to English in the **Basic Settings**. This will then change the language of the UI in your LINE chat.

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/agent-information/webchat-settings-for-thrid-parties.png" target="_blank">
      <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/webchat-settings-for-thrid-parties.png" alt="image that displays the additional options in Chat Settings">
    </a>
  </div>
  <p style="margin-top: 20px; font-size: 15px">Webchat Chat Settings and Basic Settings</p>
</div>

