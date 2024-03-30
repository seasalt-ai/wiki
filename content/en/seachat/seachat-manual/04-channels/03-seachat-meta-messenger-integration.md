---
title: "Facebook Messenger"
description: "Connect SeaChat to Facebook Messenger"
date: 2024-03-19T08:48:57+00:00
lastmod: 2024-03-19T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /en/seachat/seachat-integrations/meta-messenger/
  - /seachat/seachat-integrations/meta-messenger/
  - /seachat/seachat-integrations/03-seachat-meta-messenger-integration/
weight: 30
toc: true
---

## Quick Setup
> After logging onto SeaChat, you can navigate to "Agent Configuration" -> "Channels" -> "Messenger" to add the integration.

---

## Sign up for a Facebook Meta Developer Account
Get started by going to the [Facebook Meta Developer Site](https://developers.facebook.com/). Create an account or log in by clicking the green button on the top of the page.

## Create a New Messenger App
1. After you log in, you will see your dashboard. Click on the **Create App** button.
2. On the **Add use case page**, select **Other**, then click **Next**.
3. On the **Select app type** page, select **Business**, then click **Next**.
4. On the next page, choose a name for your app, enter an email, and select your Business Account. You will need this connection to access all the bot features. Click **Create App**.
5. Find the **Messenger** box under the **Add products to your app** section, and click **Set up** to create your app.

For more information on Messenger functionality and limitations, read the [Overview](https://developers.facebook.com/docs/messenger-platform/overview).

<br/>
<a href="/images/product-updates/seachat/en/channels/meta-messenger/create-a-new-messenger-app.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/meta-messenger/create-a-new-messenger-app.png" alt="">
</a>
<br/>

## Configure the Messenger App
After creating your app, you will now arrive at your **Dashboard**. Ensure you are on the **Messenger API Settings** page under the Messenger section of the sidebar.

**Skip** the first step called Configure Webhooks for now.

Scroll down to the second step called "**Generate Access Tokens**." Click on the button in that section, and a pop-up will appear. Continue on to the next section for more instructions.

<br/>
<a href="/images/product-updates/seachat/en/channels/meta-messenger/configure-the-messenger-app.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/meta-messenger/configure-the-messenger-app.png" alt="">
</a>
<br/>

## Set up Your Agent's API Settings and Link It to SeaChat
1. In the pop-up box, select the Facebook Meta Page that you would like the bot to connect to, and click on Continue. Note: You will need a page for your business on the Facebook Meta site before it will appear here. For instructions on how to create a Facebook Meta page, refer to this guide.
2. Your page will be added to the "Generate Access Tokens" section. Click on the Generate button under Token.
3. Read the text in the pop-up and check the box, then copy the token.
4. Return to the SeaChat configuration page (this page), and under the Facebook Meta Access Token field in the form above, paste the token, and submit the form. A webhook URL and verify token will appear. Hold onto this information for the next step.

<br/>
<a href="/images/product-updates/seachat/en/channels/meta-messenger/set-up-your-agents-API.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/meta-messenger/set-up-your-agents-API.png" alt="">
</a>
<br/>

## Set up Your Agent's Webhook Info
1. Under the **Messenger API Settings** page, go to section one, **Configure Webhooks**. Click on **Configure** and enter both the Callback URL and Verify Token that you received from this page after submitting the form in the fields on the pop-up.
2. Return to section 2, the Generate Access Tokens section. Under **Webhook Subscription**, click on **Add Subscription**, and check all the boxes **except** "messaging_game_plays", "message_reads", and "message_echoes". Refer to the visual guide in step 4.

<br/>
<a href="/images/product-updates/seachat/en/channels/meta-messenger/set-up-your-agents-webhook-info.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/meta-messenger/set-up-your-agents-webhook-info.png" alt="">
</a>
<br/>

## Prepare Your Agent for Deployment
On the left sidebar, navigate to **App Settings**, and click on **Basic**. In the form, the Privacy Policy URL, App Icon, and Category sections must be filled out before your bot can be deployed.

We recommend submitting your bot for verification under the **App Review** section on the dashboard. Follow the steps on the page to submit a request to Facebook Meta. Unverified apps may only send and receive messages to test users.

Your bot is now ready to go live! On the top of the dashboard page, toggle the **App Mode** to **Live**, and your bot will now respond to user messages in the chat box on your Facebook Meta page.

### Support
Need assistance? Contact us at [seachat@seaslt.ai](mailto:seachat@seaslt.ai).

 