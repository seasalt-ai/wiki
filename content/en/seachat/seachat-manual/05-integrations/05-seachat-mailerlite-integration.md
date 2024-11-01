---
title: "MailerLite"
description: "Integrate SeaChat with MailerLite to automatically add customer emails from forms to your lists. Learn how to generate an API token for email marketing."
date: 2024-04-23T08:48:57+00:00
lastmod: 2024-04-23T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /en/seachat/seachat-integrations/mailerlite/
  - /seachat/seachat-manual/05-integrations/05-seachat-mailerlite-integration/
url: /en/seachat/integrations/mailerlite/  
weight: 50
toc: true
---

This page details the process for setting up MailerLite integration with SeaChat. After setting up this integration, you can use SeaChat forms to collect customer emails and information, and add them to your email lists on [MailerLite](https://www.mailerlite.com/) automatically.

For a visual guide on how to integrate SeaChat with MailerLite, you can watch the tutorial video below:
<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/?v=xTnJ9L1sVC4&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=14" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## Step 1: Create a SeaChat account
If you do not have a SeaChat account, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! Then you can build your AI agent and integrate with MailerLite.


## Step 2: Open "Integrations"
Go to your MailerLite dashboard and click on "Integrations" from left panel.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 50%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/add-mailerlite-integrations.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/add-mailerlite-integrations.png" alt="Go to your Mailerlite dashboard and click on Design Site from top right menu.">
</a>
</div>
</div>


## Step 3: Select "API"
Select "API" by clicking on "Use".


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/select-mailerlite-api.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/select-mailerlite-api.png" alt="Select API on MailerLite">
</a>
    <p style="margin-top: 20px; font-size: 15px">Generate new token on MailerLite
</div>
</div>



## Step 4: Generate new token
Click on "Generate new token". Give this API key a self-explanatory name and accept the API token requirements. Click on "Create token".

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/generate-new-token-mailerlite.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/generate-new-token-mailerlite.png" alt="Generate new token on MailerLite">
</a>
    <p style="margin-top: 20px; font-size: 15px">Generate new token on MailerLite
</div>
</div>

<br>

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/give-api-token-name-mailerlite.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/give-api-token-name-mailerlite.png" alt="Give the new token a name on MailerLite">
</a>
    <p style="margin-top: 20px; font-size: 15px">Give the new token a name on MailerLite
</div>
</div>

## Step 5: Copy API key
Save a copy of your API key. Then, go back to SeaChat integration page for MailerLite to finish integration.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/copy-and-save-mailerlite-api-key.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/copy-and-save-mailerlite-api-key.png" alt="Copy and save MailerLite API key">
</a>
    <p style="margin-top: 20px; font-size: 15px">Copy and save MailerLite API key
</div>
</div>



## Step 6: (Optional) Find your Group IDs
If you want to add contacts to specific MailerLite Group. You can find all the Group IDs under your account at the bottom of “Developer API” page. Hint: you can add a contact to multiple groups.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/get-mailerlite-group-id.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/get-mailerlite-group-id.png" alt="Get MailerLite group ID">
</a>
    <p style="margin-top: 20px; font-size: 15px">Get MailerLite group ID
</div>
</div>


### Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 