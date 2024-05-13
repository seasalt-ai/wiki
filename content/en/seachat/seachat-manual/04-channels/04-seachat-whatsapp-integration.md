---
title: "WhatsApp"
description: "Unlock seamless WhatsApp automation with Seasalt.ai's SeaChat platform. Streamline your business communication by integrating a ChatGPT-powered chatbot, manage conversations effortlessly, and enhance customer support with live agent connectivity. Perfect for high-volume messaging and personalized experiences."
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

## 🎥 Video Tutorial
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/?v=qpNlWtGP9jw&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

## Overview
In this section, we will dive deeper into the process of setting up a ChatGPT-powered chatbot or chat agent on WhatsApp. By the end of this section, you will have a clear understanding of how to:
1. **Automate responses to user messages**: 
  - Connect your WhatsApp business account to the SeaChat agent platform.
  - Train the AI Agent using ChatGPT's advanced language model to generate natural language responses to a wide range of user queries.
  - Configure the chat agent to automatically respond to incoming messages based on your knowledge base.
2. **Access all conversations with users through SeaChat**:
  - Use SeaChat, a user-friendly interface, to access and monitor all conversations between users and your AI agent.
  - Review chat transcripts, analyze user behavior, and identify areas for improvement in the chat agent's responses.
  - Manage and organize conversations efficiently to ensure seamless communication with users.
3. **Enable users to request live agent assistance**:
  - Implement a special command that allows users to request assistance from a real human agent if they have complex queries or require personalized support.
  - Seamlessly transfer conversations from the AI chat agent to live human agents, ensuring a smooth and efficient transition.
  - Empower users to choose the level of support they need, enhancing the overall customer experience.

Before embarking on the setup process, it's essential to keep in mind a few key points:

**WhatsApp Business App limitations**:
  - Once you integrate SeaChat with WhatsApp, you will no longer be able to use the regular WhatsApp Business App.
  - The SeaChat AI agent is designed to respond to incoming messages only and cannot initiate conversations on its own.
  - However, you as the agent creator will still be able to talk with the users once a live human agent is requested.

**Who benefits from this integration**:
  - Businesses and organizations with a high volume of incoming WhatsApp messages that require automation.
  - Companies looking to provide personalized and engaging customer support experiences.
  - Customer service departments seeking to reduce the burden on human agents by automating routine inquiries.
---

## WhatsApp Setup
Setting up WhatsApp can be a straightforward process with the right guidance. Here's a short version of the steps involved. You can also click on the titles to see a more detailed explanation of each step:

1. **[Create a WhatsApp App](#create-a-whatsapp-app)**:
- Go to the Meta Developer Site.
- Click on **My Apps** in the top-right corner.
- Select **Create App** from the dropdown menu.

2. **[Choose App Type](#choose-app-type)**:
- Choose **Other** under **App Type**.
- Enter a unique app name, avoiding the use of **WhatsApp** in the name.

3. **[Add WhatsApp Product](#add-whatsapp-product)**:
- Scroll down to the bottom of the app list.
- Find **WhatsApp** and select it to add the product to your app.

4. **[Connect to Business](#connect-to-business)**:
- Associate the WhatsApp app with your business.
- This step is necessary to utilize the **WhatsApp Business Platform API**.

5. **[Configure WhatsApp Application](#configure-whatsapp-application)**:
- Carefully review the information on the configuration page.
- Follow the instructions to provide necessary details, such as business name, address, and contact information.
- Ensure that all required fields are filled out correctly.

6. **[Generate Access Token](#lets-set-up-a-permanent-token)**:
- Once the configuration is complete, generate a permanent access token.
- This token is essential for using the WhatsApp Business API.

7. **[Test and Launch](#test-your-seachat-agent-via-whatsapp)**:
- Test your WhatsApp app to ensure it works as intended.
- Make any necessary adjustments based on the test results.
- Once satisfied with the performance, launch your app for public use.

8. **[Remove Your Messenger Integration](#remove-your-whatsapp-integration)**:
- Properly remove the page access from your Meta app
- Click the Remove button inside SeaChat

> :books: **Recommended Reading**:
> 
> Remember to adhere to the [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp/) policies and guidelines to maintain compliance and avoid any potential issues.


The following is an elaborated explanation that walks you through the process step-by-step:

### Create a WhatsApp app

You’ll first need to go to [Meta Developer Site](https://developers.facebook.com/) and create a new WhatsApp app by clicking **My Apps** in the top right corner, and then selecting **Create App** from the dropdown menu.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/product-updates/seachat/en/channels/whatsapp/create-new-whatsapp-app.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/create-new-whatsapp-app.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Create a New WhatsApp</p>
</div>
</div>

### Choose App Type
Create an **Other** app because we’ll just use this App for accessing your WhatsApp account. On the **Select app type page**, select **Business** for the type, then click **Next**.

<br/>
<div style="display: flex; flex-direction: column; align-items: center;">
    <div style="width: 100%; height:100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/choose-app-type-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/choose-app-type-1.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Create an <strong>Other</strong> app</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/choose-app-type-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/choose-app-type-2.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Fill Up App Details</p>
    </div>
</div>

<br/>

Here we created an app called **Seasalt.ai WA**, note that Meta doesn’t allow the app to have **WhatsApp** in the name.


### Add WhatsApp Product

After creating the App, let’s add the WhatsApp product. Find the WhatsApp box under the **Add products to your app** section, and click **Set up** to create your app.

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/product-updates/seachat/en/channels/whatsapp/whatsApp-integration.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/whatsApp-integration.svg" alt="">
    </a>
    <p style=" font-size: 15px">Add WhatsApp to Your App</p>
</div>
</div>


### Connect to Business
The WhatsApp app needs to be associated with your own business as it needs to utilize the [WhatsApp Business Platform API](https://developers.facebook.com/docs/whatsapp/). Select a business portfolio and click continue. Now back to your app dashboard, you should see the WhatsApp product added to your app. Click on **Start using the API** to start configuring.

<br/>
<div style="display: flex; flex-direction: column; align-items: flex-start;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/connect-to-business-1.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/connect-to-business-1.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Select a Business Portfolio</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/connect-to-business-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/connect-to-business-2.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Click <strong>Start Using the API</strong></p>
    </div>
</div>

## How to Configure WhatsApp Application
> :rotating_light: **Warning** :rotating_light:
>
> Here is where things get a bit more complicated.  If you are not careful enough and miss a step, you might not be able to successfully configure your WhatsApp application. So, let's carefully go through the following instruction together.

If you click on **Start using the API** from above, it’ll bring you to **API Setup** like below. However, we do not need to pay too much attention to the information here. What really matters here is **Step 3: Configure webhooks**.

<br/>
<div style="display: flex; flex-direction: column; align-items: center; justify-content: space-between">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/configure-whatsApp-application-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/configure-whatsApp-application-1.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">API Setup</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/configure-whatsApp-application-2.svg" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/configure-whatsApp-application-2.svg" alt="">
        </a>
        <p style="font-size: 15px"><strong>Configure Webhooks</strong></p>
    </div>
</div>

It will bring you to **Configuration** under **WhatsApp** on the left. From here we’ll first need to configure the Webhook and tokens provided by SeaChat.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/product-updates/seachat/en/channels/whatsapp/configure-whatsApp-application-3.svg" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/configure-whatsApp-application-3.svg" alt="">
    </a>
    <p style=" font-size: 15px">Configuration Dashboard</p>
</div>
</div>

<br/>

For the configuration of the webhook, we will look at **Step 1** in the picture above. Here is all you have to do. Go to SeaChat, navigate to **Agent Configuration → Channels → WhatsApp** to get the **Callback URL** and **Verify token**. 

Copy SeaChat’s Step 1 and paste it to corresponding parts on WhatsApp dashboard like the picture below 


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/product-updates/seachat/en/channels/whatsapp/configure-whatsApp-application-4.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/configure-whatsApp-application-4.svg" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Copy SeaChat info to configure</p>
</div>
</div>

<br/>

> :point_down: **Don’t forget to use set Webhook fields!** :point_down:
>
> We’ll need to give messages permission to the API, so that the SeaChat agent will be able to receive any incoming messages from WhatsApp.
>
> 
> <div style="display: flex; flex-direction: column; align-items: center;">
> <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
>   <a href="/images/product-updates/seachat/en/channels/whatsapp/dont-forget-to-use-set-Webhook-fields.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank"><img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/dont-forget-to-use-set-Webhook-fields.svg" alt=""></a>
>     <p style="margin-top: 10px; font-size: 15px">Webhook Fields</p>
> </div>
> </div>
> 


### Let’s set up a permanent token

[Step 2](#perma-token-webhook) is to obtain a **WhatsApp Access Token** to pass it back to SeaChat.

You might have seen the temporary access token before from API Setup:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
 <a href="/images/product-updates/seachat/en/channels/whatsapp/permanent-token-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/permanent-token-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Temporary Access Token</p>
</div>
</div>

<br/> 

<p>:point_up: As stated by Meta, this token is only valid for 24 hours. So let’s not use it.</p>

<br/> 



### 1. Creating System Users

you should get a permanent token by generating a [System User Access Token](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens). 

Here are the steps to create a system user:

1. Sign in to the [Meta Business Suite](https://business.facebook.com/).
2. Locate your business account in the top-left dropdown menu and click its **Settings** (gear) icon.
3. Click **Business settings**.
4. Navigate to **Users** → **System users**
5. Click the **Add** button and create either an admin or employee system user.


### 2. Generating System User Access Tokens

To generate a System User access token after creating a system user:
1. Sign in to the [Meta Business Suite](https://business.facebook.com/).
2. Locate your business account in the top-left dropdown menu and click its **Settings** (gear) icon.
3. Click **Business settings**.
4. Navigate to **User** → **System** users.
5. Select the appropriate system user from the list of system users.
6. ~~Click the Generate new token button~~. → **Do Not Do this Yet**. See [Assign Assets](#assign-assets) below. 
7. Select the app that will use the token.
8. Select any permissions the app needs to function properly and generate the token.

##### Assign Assets
We stop you at Step 6 above, because you’ll need to assign your WhatsApp app as the **Asset** first to get the proper scopes for the token. Please follow the steps below to assign your WhatsApp app as the Asset:

1. In System Users, click on [**Assign Asset**](#assign-assets-step-1).
2. Then go to **Apps** and select the app you created, and give it [**Full control**](#assign-assets-step-2).
3. Click **Generate new token** and select ***whatsapp_business_messaging*** and ***whatsapp_business_management*** in **Permissions**. It should look like [this](#assign-assets-step-3).
4. Once the token is generated, a [pop-up](#assign-assets-step-4) will show up to show you the information of the generated token. Copy the token.
5. Now click on the token, it’ll open the [**Access Token Debugger**](#assign-assets-step-5) and show you the correct Scope. Here you need to make sure you have ***whatsapp_business_messaging*** and ***whatsapp_business_management***.
6. Copy and paste the token to [SeaChat](#assign-assets-step-6).
7. Turn on your [**App Mode**](#assign-assets-step-7) to be **Live**.
8. Add your business phone number to your WhatsApp app by going back to [**WhatsApp** →  **Configuration**](#assign-assets-step-8) and add your WhatsApp number there. It should show at least 1 production number.

<div style="display: flex; flex-direction: column; width:100%  ; align-items: center;">
    <div id="assign-assets-step-1" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-1.svg" target="_blank" style=" width: 100%; height: 10%; display: flex; justify-content: center; align-items: center; overflow: hidden; padding: 0">
            <img style="max-width: 100%; max-height: 50%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-1.svg" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 1: Click on <strong>Assign Asset</strong></p>
    </div>
    <div id="assign-assets-step-2" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-2.svg" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-2.svg" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 2: Give App <strong>Full control</strong></p>
    </div>
</div>
<div id="assign-assets-step-3" style="display: flex; flex-direction: column; width:100%; align-items: center;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-3.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-3.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 3: <strong>Generate token</strong> and set up <strong>Permission</strong></p>
    </div>
    <div id="assign-assets-step-4" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-4.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-4.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 4: Copy token</p>
    </div>
</div>
<div style="display: flex; flex-direction: column; width:100% ; align-items: center;">
    <div id="assign-assets-step-5" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-5.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-5.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 5: Open the <strong>Access Token Debugger</strong></p>
    </div>
    <div id="assign-assets-step-6" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-6.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-6.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 6: Paste token to SeaChat</p>
    </div>
</div>
<div style="display: flex; flex-direction: column; width:100% ; align-items: center;">
    <div id="assign-assets-step-7" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-7.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-7.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 7: Set <strong>App Mode</strong> to <strong>Live</strong></p>
    </div>
    <div id="assign-assets-step-8" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-8.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/assign-asset-8.png" alt="">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 8: Add business number</p>
    </div>
</div>

## Test your SeaChat agent via WhatsApp

Finally, we are all set up! Once your agent is set up, try to send a few messages and expect a reply from SeaChat:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/product-updates/seachat/en/channels/whatsapp/test-whatsapp-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/test-whatsapp-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">WhatsApp Conversation</p>
</div>
</div>

<br/> 

From the **Conversations** view in SeaChat, you can see the same conversation with the user/sender’s name.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/product-updates/seachat/en/channels/whatsapp/test-whatsapp-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/test-whatsapp-2.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">SeaChat Conversation</p>
</div>
</div>

### Properly Decorating your WhatsApp Business Account


The above screenshot shows a pretty rudimentary WhatsApp account, which does not even have a profile picture. In the competitive digital landscape, having a strong online presence is crucial for businesses of all sizes. WhatsApp, with its massive user base and widespread popularity, offers a powerful platform for businesses to connect with their customers. However, setting up and managing a WhatsApp Business account effectively can be a daunting task.

One of the essential aspects of managing a WhatsApp Business account is setting up the profile properly. A well-optimized profile creates a professional image, instills trust, and enhances visibility. Unfortunately, many businesses overlook the importance of profile setup or struggle to find the right settings.

Let's properly set up WhatsApp account profile by going to [Meta WhatsApp Business Manager](https://business.facebook.com/wa/manage) to do this. Or if you are still in the Meta for Developers website, navigate to **WhatsApp → Quickstart → WhatsApp Business** and click **Account information**:


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/product-updates/seachat/en/channels/whatsapp/deploy-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/deploy-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Account information</p>
</div>
</div>

<br/> 

This will bring you to the correct account under **WhatsApp Business Manager**. Here, you can make necessary changes, upload a profile picture, and save the updates. It may take a few minutes for the changes to take effect. Once they do, you'll notice the updated profile information when you access your WhatsApp business account's info page on your mobile device.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/product-updates/seachat/en/channels/whatsapp/deploy-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/deploy-2.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Make Changes to Account</p>
</div>
</div>



<br/> 

After a few minutes, if you click your WhatsApp business account’s info page on your WhatsApp app on your phone, it’ll reflect the change:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/product-updates/seachat/en/channels/whatsapp/deploy-3.png" target="_blank">
<img width="50%" height="auto" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/deploy-3.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">WhatsApp Business Account Info</p>
</div>
</div>

<br/> 

Optimizing your WhatsApp Business profile goes beyond just adding a profile picture. Here are some additional tips to enhance your profile:

2. **Use a Clear and Professional Profile Picture**:
Choose a high-quality image that represents your brand or business. Avoid blurry or low-resolution images, as they can create a negative impression.

3. **Add Relevant Contact Information**:
Ensure that your phone number, email address, and website (if applicable) are prominently displayed in your profile. This makes it easy for customers to reach you through their preferred channels.

4. **Use Labels and Tags**:
Organize your contacts and conversations using labels and tags. This helps you categorize and manage customer interactions effectively, making it easier to track and respond to specific inquiries or requests.

By following these tips, you can properly democratize your WhatsApp Business account, create a professional profile, and enhance your overall customer engagement.

# Engage with a real human agent
Did you notice in the above picture that I used /live_agent to request a human agent? If an agent happened to be online by setting their online status:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/product-updates/seachat/en/channels/whatsapp/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/live-agent-status.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent status
</p>
</div>
</div>

<br/> 

They can directly talk with the user!

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/product-updates/seachat/en/channels/whatsapp/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/live-agent-interaction.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent interaction
</p>
</div>
</div>

<br/> 

If an agent is not online, they can turn on Email notification to receive real-time emails when a user initiates a chat, or request a live agent:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/product-updates/seachat/en/channels/whatsapp/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/ai-agent-preference.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent preference
</p>
</div>
</div>

<br/> 

## Remove your WhatsApp Integration

If you want to remove the WhatsApp integration, you need to do it in two places:

1. Properly remove the webhook from your Meta app
2. Click the Remove button inside SeaChat

For Step 1, please go to your [Meta Business app](https://developers.facebook.com/) → WhatsApp → Configuration → Callback URL → Edit → Remove webhook

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/product-updates/seachat/en/channels/whatsapp/remove-app-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/channels/whatsapp/remove-app-1.png" alt="">
</a>
    <p style="margin-top: 20px; font-size: 15px">Remove integration</p>
</div>
</div>

<br/> 

## :dart: Troubleshooting

If you have not received responses from SeaChat Agent on WhatsApp, you should verify the following settings that users tend to overlook:
- Are you utilizing a **temporary access token** that is valid for only 24 hours? A System User's [**Permanent Access Token**](#1-creating-system-users) should be used instead. 
- Has your WhatsApp application been set to [**Live mode**](#assign-assets)? Be sure that it is not operating in Development mode.
- Did you configure the [**webhook fields**](#perma-token-webhook) to allow the **message permission**? If this permission is not properly granted, SeaChat will be unable to receive messages from WhatsApp.
- Did your SeaChat agent receive a message, but you cannot see the reply from your WhatsApp? It might be that when you generated the permanent token, you did not [**Assign Assets**](#assign-assets) first.




## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 
