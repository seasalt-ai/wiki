---
title: "Facebook Messenger"
description: "Set up a ChatGPT-powered bot on Facebook Messenger. Follow our guide to create a Meta app, configure webhooks, and launch your bot for seamless communication."
date: 2024-04-08T08:48:57+00:00
lastmod: 2024-04-08T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /en/seachat/seachat-manual/04-channels/06-seachat-messenger-integration/
  - /seachat/seachat-integrations/03-seachat-facebook-messenger-integration/
url: /en/seachat/manual/channels/facebook-messenger/
weight: 60
toc: true
---

## 🎥 Video Tutorial
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/?v=aFruY5bwG00&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


## Overview
In this section, we will dive deeper into the process of setting up a ChatGPT-powered chatbot or chat agent on Facebook Messenger. By the end of this section, you will have a clear understanding of how to:
1. **Automate responses to user messages**: 
  - Connect your Messenger business account to the SeaChat chatbot and agent platform.
  - Train the chatbot using ChatGPT's advanced language model to generate natural language responses to a wide range of user queries.
  - Configure the chat agent to automatically respond to incoming messages based on your knowledge base.
2. **Access all conversations with users through SeaChat**:
  - Use SeaChat, a user-friendly interface, to access and monitor all conversations between users and your chatbot.
  - Review chat transcripts, analyze user behavior, and identify areas for improvement in the chat agent's responses.
  - Manage and organize conversations efficiently to ensure seamless communication with users.
3. **Enable users to request live agent assistance**:
  - Implement a special command that allows users to request assistance from a real human agent if they have complex queries or require personalized support.
  - Seamlessly transfer conversations from the AI chat agent to live human agents, ensuring a smooth and efficient transition.
  - Empower users to choose the level of support they need, enhancing the overall customer experience.

By the end of this tutorial, you’ll have a SeaChat agent powered Facebook Messenger bot and also a SeaChat console to view all messages, as shown below:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/facebook-messenger-integration.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/facebook-messenger-integration.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">ChatGPT-powered chatbot integration with Facebook Messenger using SeaChat</p>
</div>
</div>

<br/> 

Before embarking on the setup process, it's essential to keep in mind a few key points:

**Messenger limitations**:
  - The SeaChat AI agent is designed to respond to incoming messages only and cannot initiate conversations on its own.
  - However, you as the agent creator will still be able to talk with the users once a live human agent is requested.

**Who benefits from this integration**:
  - Businesses and organizations with a high volume of incoming Messenger messages that require automation.
  - Companies looking to provide personalized and engaging customer support experiences.
  - Customer service departments seeking to reduce the burden on human agents by automating routine inquiries.

---

## Facebook Messenger Setup
Setting up Facebook Messenger can be a straightforward process with the right guidance. Here's a short version of the steps involved. You can also click on the titles to see a more detailed explanation of each step:

1. **[Create a Messenger App](#create-a-facebook-messenger-app)**:
- Go to the Meta Developer Site.
- Click on **My Apps** in the top-right corner.
- Select **Create App** from the dropdown menu.

2. **[Choose App Type](#choose-app-type)**:
- Choose **Other** under **App Type**.
- Enter a unique app name, avoiding the use of **Messenger App** or **Facebook** in the name.

3. **[Add Messenger Product](#add-messenger-product)**:
- Scroll down to the bottom of the app list.
- Find **Messenger** and select it to add the product to your app.

5. **[Configure Messenger Application](#step-1-configure-webhooks)**:
- Carefully review the information on the configuration page.
- Follow the instructions to provide necessary details, such as business name, address, and contact information.
- Ensure that all required fields are filled out correctly.

6. **[Generate Access Token](#step-2-generate-access-token)**:
- Once the configuration is complete, generate a permanent access token.
- This token is essential for using the Messenger API.

7. **[Remove Your Messenger Integration](#remove-your-messenger-integration)**:
- Properly remove the page access from your Meta app
- Click the Remove button inside SeaChat

> :books: **Recommended Reading**:
> 
> Remember to adhere to the [Messenger API](https://developers.facebook.com/docs/messenger/) policies and guidelines to maintain compliance and avoid any potential issues.


The following is an elaborated explanation that walks you through the process step-by-step:

### Create a Facebook Messenger App

You’ll first need to go to [Meta Developer Site](https://developers.facebook.com/) and create a new Facebook Messenger app by clicking **My Apps** in the top right corner, and then selecting **Create App** from the dropdown menu.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/facebook-messenger/create-new-messenger-app.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/create-new-messenger-app.png" alt="">
    </a>
<br/>
    <p style="margin-top: 20px; font-size: 15px">Create a New Messenger</p>
</div>
</div>

### Choose App Type
Create an **Other** app because we’ll just use this App for accessing your Messenger account. On the **Select app type page**, select **Business** for the type, then click **Next**.

<br/>
<div style="display: flex; flex-direction: column; align-items: center;">
    <div style="width: 100%; height:100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-1.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Create an <strong>Other</strong> app</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-2.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Choose <strong>Business</strong></p>
    </div>
</div>

<br/>

Here we created an app called **Seasalt.ai App**, note that Meta doesn’t allow the app to have **Facebook** or **Messenger** in the name. Carefully read through warning messages when choosing the app name.

<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-3.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-3.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Create App</p>
    </div>
<br/>

### Add Messenger Product

After creating the App, let’s add the [Messenger product](https://developers.facebook.com/docs/messenger/). Find the Messenger box under the **Add products to your app** section, and click **Set up** to create your app.

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/facebook-messenger/add-messenger-product.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/add-messenger-product.png" alt="">
    </a>
<br/>
    <p style=" font-size: 15px">Add Messenger to Your App</p>
</div>
</div>

## How to Configure Messenger Application
> :rotating_light: **Warning** :rotating_light:
>
> Here is where things get a bit more complicated.  If you are not careful enough and miss a step, you might not be able to successfully configure your Messenger application. So, let's carefully go through the following instruction together.

### Step 1: Configure webhooks

Find **Messenger API** under **Messenger** on the left. From here we’ll first need to configure the Webhook and tokens provided by SeaChat.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-1.png" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-1.png" alt="">
    </a>
<br/>
    <p style=" font-size: 15px">Verify Token</p>
</div>
</div>


Here is all you have to do. Go to SeaChat, navigate to **Agent Configuration → Channels → Messenger** to get the **Callback URL** and **Verify token**. 

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-2.png" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-2.png" alt="">
    </a>
<br/>
    <p style=" font-size: 15px">Navigate to <strong>Messenger</strong> on SeaChat</p>
</div>
</div>


Copy SeaChat’s Step 1 and paste it to corresponding parts on Messenger dashboard.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-3.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Copy SeaChat info to configure</p>
</div>
</div>

<br/>

Paste the **Callback URL** and **Verify token** to the corresponding fields on the Messenger dashboard:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-4.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-4.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Paste the URL and token</p>
</div>
</div>

<br/>

After this, we’ll need to properly configure **Webhook Fields** to give the right permission to the webhook callback URL:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-5.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-5.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Webhook Fields</strong> configuration</p>
</div>
</div>

<br/>

Select **messages** and click **Subscribe**:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-6.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-6.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Subscribe selected messages</p>
</div>
</div>

<br/>

So your final configuration of webhook would look like this:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-7.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-7.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Webhook configuration</p>
</div>
</div>

<br/>

### Step 2: Generate Access Token

The Meta app needs to access a certain Facebook Page to be able to receive messages sent from that Page. So in Step 2, you’ll first need to authorize it to access your public Facebook Page.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Generate Access Token</p>
</div>
</div>

<br/>

After authorizing with a Facebook Page, you can further **Add Subscriptions**:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-2.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Click on <strong>Add Subscription</strong></p>
</div>
</div>

<br/>

Again, we want to subscribe to **messages**:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-3.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Choose <strong>messages</strong></p>
</div>
</div>

<br/>

Finally, let’s generate the access token:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-4.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-4.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Token generation</p>
</div>
</div>

<br/>

Once the token is generated, we need to copy the token:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-5.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-5.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Token details</p>
</div>
</div>

<br/>

Paste it to Step 2 of SeaChat Messenger setup:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-6.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-6.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Paste Token to SeaChat</p>
</div>
</div>

<br/>

Now turn on your App Mode to be **Live** and you can chat with the bot:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a id="live-mode" href="/images/seachat/en/channels/facebook-messenger/access-token-7.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-7.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live mode</p>
</div>
</div>

<br/>

### Step 3: Alternative to  Complete App Review

So far your messenger bot will respond **only to you**, the app creator. If you pass it to others, they will not get a response at all. It might be tempting to do “Step 3. Complete App Review” per Facebook’s instructions:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/app-review-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/app-review-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">App review</p>
</div>
</div>

<br/> 

However, It might take up to 5 days to complete the App Review and the process is very cumbersome. For instance, it requires you to take a video walkthrough of the Meta app.

An alternative way is to assign the page to the business you have with Meta. To do so, go to [Meta Business Suite](https://business.facebook.com/), select the business your Meta app was created under, and then go to **Accounts** → **Pages**, and make sure that the Facebook Page your chatbot is connected to is there:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/facebook-pages.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/facebook-pages.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Make sure the Facebook Page shows up under your business 
</p>
</div>
</div>

<br/> 

You should now be all set!

# Engage with a real human agent
Did you notice in the above picture that I used /live_agent to request a human agent? If an agent happened to be online by setting their online status:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 40%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent status
</p>
</div>
</div>

<br/> 

They can directly talk with the user!

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent interaction
</p>
</div>
</div>

<br/> 

If an agent is not online, they can turn on Email notification to receive real-time emails when a user initiates a chat, or request a live agent:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent preference
</p>
</div>
</div>

<br/> 

## Remove your Messenger Integration

If you want to remove the Messenger integration, you need to do it in two places:
1. Properly remove the page access from your Meta app
2. Click the Remove button inside SeaChat

For Step 1, please go to your **[Meta Business app](https://developers.facebook.com/)** → **Messenger** → **Messenger API Settings** → **Generate access tokens** → remove

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Remove integration</p>
</div>
</div>

<br/> 

## Respond to Voice Clips
Do you know that SeaChat supports audio messages too? If a user sends a voice clip, SeaChat can transcribe it to text, and respond via text!

Currently, it supports English speech to transcription, but let us know if you want more languages supported.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Facebook Messenger voice clip transcription and response by SeaChat</strong></p>
</div>
</div>

<br/> 

## Messages Postback on Messenger

Once you have set up your Messenger integration, you will be able to interact with your customers using the [button feature](https://wiki.seasalt.ai/seachat/seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers/) of SeaChat. This allows you to add urls or additional information to your answers in the form of buttons.

To activate, simply go on the page of **Edit Page Subscription** on Messenger. 

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Enable Postback on Edit Page Subscription</strong></p>
</div>
</div>

<br/> 

### Button limits on Messenger

After following the above steps, you can now use the button feature on SeaChat integrated with Messenger. However, since we are still using the API provided by Messenger, there are some limitations to keep in mind when creating your buttons to avoid any issues.

The following are the limitations:

- The button template allows up to **3 postback buttons** per message template.
- Each button can have a **payload of up to 1000 characters**, which is sent back to your webhook when clicked.
- The **button title** is limited to **20 characters**.
- These limits apply to each individual button, so you can have 3 buttons per message, each with its own 1000-character payload and 20-character title.
- [Developer Documentation](https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback)

A good solution to reduce the effect of these limitations is to use SeaChat's **[KB ID](https://wiki.seasalt.ai/seachat/seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers/#kb-ids)** feature. Please check out the link for more information.

## :dart: Troubleshooting

If you have not received responses from SeaChat Agent on Messenger, you should verify the following easily missed settings:
- Has your Messenger application been set to [**Live mode**](#live-mode)? Be sure that it is not operating in Development mode.
- Did you configure the [**webhook fields**](#perma-token-webhook) to allow the **message permission**? If this permission is not properly granted, SeaChat will be unable to receive messages from messenger.


## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).
