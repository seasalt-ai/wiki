---
title: "WhatsApp"
description: "Connect SeaChat to WhatsApp"
date: 2024-03-19T08:48:57+00:00
lastmod: 2024-03-19T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
   - /en/seachat/seachat-integrations/whatsapp/
   - /seachat/seachat-integrations/whatsapp/
   - /seachat/seachat-integrations/04-seachat-whatsapp-integration/
weight: 40
toc: true
---

## Quick Setup
> After logging onto SeaChat, you can navigate to "Agent Configuration" -> "Channels" -> "WhatsApp" to add the integration.

Get started by going to the [Meta Developer Site](https://developers.facebook.com/). Create an account or log in by clicking the green button on the top of the page.


## Create a new WhatsApp business app
1. After you log in, you will see your dashboard. Click on the **Create App** button.
2. On the **Add use case** page, select **Other**, then click **Next**.
3. On the **Select app type** page, select **Business**, then click **Next**.
4. On the next page, choose a name for your app, enter an email, and select your Business Account. You will need this connection to access all the bot features. Click **Create App**.
5. Find the **WhatsApp** box under the **Add products to your app** section, and click **Set up** to create your app.

<br/>
<a href="/images/product-updates/seachat/en/channels/whatsapp/create-a-new-whatsapp-app.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/create-a-new-whatsapp-app.png" alt="">
</a>
<br/>


## Find your page access token and phone number

On the left sidebar, find **WhatsApp** under the **Products** section and expand it. Click on **API Setup**.

Under the **Send and Receive Messages** section, first select the phone number you would like to send messages from, then enter the recipient's phone number in the field below.

On the top of this page, you can also find your **Temporary Access Token** and **Phone Number ID**. You will need to generate a new Temporary Access Token every 24 hours. Follow the instructions on the API Setup page if you would like to create a Permanent Access Token.

Copy the token and Phone Number ID. Go back to the SeaChat dashboard (this page), enter them in the form above, and click Submit. SeaChat will provide you with your **Callback URL** and a **Verify Token** below.


<br/>
<a href="/images/product-updates/seachat/en/channels/whatsapp/page-access-token-and-phone-number.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/page-access-token-and-phone-number.png" alt="">
</a>
<br/>

## Submit the form to receive a Webhook Callback URL

Back on the WhatsApp setup dashboard, click on the **Configuration** link under the left sidebar.

Click on **Edit**, then enter your Callback URL and Verify Token from SeaChat.

Under the **Webhook fields** section, click on **Manage**, then select **messages**.

<br/>
<a href="/images/product-updates/seachat/en/channels/whatsapp/set-up-your-agents-webhook-info.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/set-up-your-agents-webhook-info.png" alt="">
</a>
<br/>

## Prepare your bot for deployment
Back on the WhatsApp setup dashboard, click on the Configuration link under the left sidebar.

Click on Edit, then enter your Callback URL and Verify Token from SeaChat.

Under the Webhook fields section, click on Manage, then select messages.


### Support
Need assistance? Contact us at [seachat@seaslt.ai](mailto:seachat@seaslt.ai).

 