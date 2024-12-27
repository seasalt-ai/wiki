---
title: "Instagram"
description: "Follow these steps to integrate Instagram with your app and build a messaging AI agent."
date: 2024-12-24T08:00:00+00:00
lastmod: 2024-12-24T08:00:00+00:00
weight: 60
draft: false
toc: true
---

## Prerequisites

- **Instagram Professional Account**: You need either a Business or Creator account to set up Instagram Messaging. If your current account is not of this type, you can switch it to a Professional account in Instagram settings.

## Instructions

### Step 1: Create an Instagram App

1. Visit the [Meta Developer Site](https://developers.facebook.com/) and click on **My Apps** in the top-right corner.
2. From the dropdown menu, select **Create App** to begin.

- Enter your app details, such as App Name and Contact Email, then click **Next**.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-name.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-name.png" alt="App Creation">
    </a>
</div>
</div>

<br/>

- Select a Use Case, choose **Other**, and click **Next**.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/use-cases.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/use-cases.png" alt="App Use Case Selection">
    </a>
</div>
</div>

<br/>

- Set the App Type to Business and click **Next**.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-type.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-type.png" alt="App Type Selection">
    </a>
</div>
</div>

<br/>

- Review your app details and click **Create App**.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/business-details.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/business-details.png" alt="App Review and Creation">
    </a>
</div>
</div>

<br/>


### Step 2: Add the Instagram Product to Your App

- Under the **Add Products to Your App** section, select Instagram.
- Click the **Set Up** button to add it to your app.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/add-instagram.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/add-instagram.png" alt="Add Instagram Product">
    </a>
</div>
</div>

<br/>

### Step 3: Connect Instagram Account

- Navigate to the API Setup with Instagram business login page.
- Click **Add Account** in Step 1 to connect to your Instagram account.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/instagram-connect.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/instagram-connect.png" alt="Connect Instagram Account">
    </a>
</div>
</div>

<br/>

### Step 4: Configure Webhook

1. Navigate to SeaChat to get the webhook URL.
   - Go to **Agent Configuration** → **Channels** → **Instagram** to find the Callback URL and Verify Token.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/seachat-channel.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/seachat-channel.png" alt="SeaChat Webhook Details">
    </a>
</div>
</div>

<br/>

2. Click **Set Up Verify Token** in Step 1. Once completed, a popup will confirm the token has been saved successfully.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/verify-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/verify-token.png" alt="Verify Token Confirmation">
    </a>
</div>
</div>

<br/>

3. Return to the Instagram app dashboard, paste the Webhook URL and Verify Token into the respective fields, and click **Save**.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/callback-url.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/callback-url.png" alt="Webhook URL and Tokens">
    </a>
</div>
</div>

<br/>

- Enable all necessary webhook events by clicking the **Manage** button to configure webhook fields.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/manage-webhook.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/manage-webhook.png" alt="Webhook Configuration">
    </a>
</div>
</div>

<br/>

### Step 5: Generate Access Token

- Click the **Generate Token** button in the Generate Access Token section.
- Check the **I Understand** checkbox in the popup to copy the access token.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/generated-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/generated-token.png" alt="Generate Access Token">
    </a>
</div>
</div>

<br/>

- Paste the copied token into Step 2 of the SeaChat Instagram setup interface and click **Save**.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/save-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/save-token.png" alt="Access Token Setup">
    </a>
</div>
</div>

<br/>

Now you’ve finished all steps to set up Instagram integration in SeaChat!


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/seachat-setup.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/seachat-setup.png" alt="Integration Complete">
    </a>
</div>
</div>

<br/>

### Step 6: Add Privacy Policy URL, Icon, and Category

1. Go to **App Settings** → **Basic**.
2. Add a Privacy Policy URL, Icon, and Category, then click **Save Changes**.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-setting.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-setting.png" alt="App Settings Update">
    </a>
</div>
</div>

<br/>

### Step 7: (Optional - Business Accounts) Complete App Review

Instagram requires successful completion of the app review process to access live data. Submit your app review request for advanced permissions when you're ready.

### Step 8: Set App to Live

- Toggle the **App Status** to Live.

Congratulations! You’ve successfully set up an Instagram Messaging AI agent. 🎉

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/set-app-to-live.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/set-app-to-live.png" alt="App Live Status">
    </a>
</div>
</div>

<br/>

### Step 9: Remove your Instagram Integration

If you want to remove the Instagram integration, you need to do it in two places:

- Properly remove the page access from your Meta app
  - Go to your **Meta Business app** → **Instagram** → **API setup with Instagram login** → **Generate access tokens** → **trash can icon** → **Remove Account**
- Click the **Remove** button inside SeaChat


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/remove-on-seachat.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/remove-on-seachat.png" alt="Remove Instagram channel on SeaChat">
    </a>
</div>
</div>

<br/>