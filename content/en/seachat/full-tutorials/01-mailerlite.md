---
title: "Mailerlite"
description: "SeaChat Intro and getting started"
lead: ""
date: 2024-04-24 15:12:51.069 +0100
lastmod: 2024-04-24 15:12:51.069 +0100
weight: 200
draft: false
images: []
aliases:
  - /en/seachat/full-tutorials/01-mailerlite/
  - /seachat/full-tutorials/01-mailerlite/
toc: true
---

## What is Mailerlite

Mailerlite is a service that you can use to collect your user's emails and add them to automated mailing lists that you can use to push promotions and updates to your users. SeaChat offers a way to seamlessly integrate your mailerlite mailing lists with our AI Webchat Agent. With this integration, you can set it up so that anyone who interacts with one of your SeaChat Agents will be prompted to provide their email and other details that you can decide to include. This ensures that you wont miss out on any leads that talk to your agent, and will keep all of your users in the loop.  

## How to set up Mailerlite with SeaChat!
In this tutorial, we will walk you through every step you need to connect your mailerlite with SeaChat Forms

## Step 1: Navigate to Mailerlite setup
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/navigate-to-mailerlite-setup.png" alt="Navigate to the mailerlite setup page.">
With your workspace and agent selected, navigate to the "Agent Configuration" drop down on the left action bar and select "Plugins". From the Plugins page you can select the Mailerlite card to access the setup page.

## Step 2: Configuring your form
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/mailerlite-main-page.png" alt="mailerlite setup page.">
On the Mailerlite setup page you will see two extendable cards. The first card contains configuration settings for the form that will be sent to the user when starting a webchat conversation. The second card contains configuration settings for your specific Mailerlite integration.
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/mailerlite-form-setup.png" alt="mailerlite form setup page.">
The form configuration card has your settings on the left, as well as a preview of your current form on the right. Lets go over each of the settings and how they affect the form:

**Enable This Form:** This switch enables and disables the form. When it is enabled, the form you configure will appear at the beginning of a new conversation with your SeaChat Agent. Keep in mind that you can only have one form attached to an agent at a time, so when you enable this, all other forms will disabled for the current agent. If you would like to use another form, this form must be disabled. 

**Allow users to skip form:** When enabled this switch will allow users to skip your form by means of an **X** button that will appear in the top right of the form. When disabled, the **X** will not appear.

**Form Name:** This is the name that the form will be saved under.

**Form Title:** This is the Title that will appear at the top of the form when it appears to the user.

**Form Design Fields:** These fields will appear on your form and will be what users fill out to submit information. The Email Field is required to add users to your Mailerlite mailing list and cannot be configured, but the other fields can be configured individually. Each of these field's name can be changed by clicking on the field itself. To the right of each of these fields are two checkboxes for additional configuration. If "Required" is checked the
field must be filled before the user can submit the form; this will be indicated by an asterisk(*) next to the name of the field. The "Enabled" checkbox determines whether or not the field will appear on the form at all. If "Enabled" is unchecked, the field will not appear to user when they recieve the form. All fields except for Email are enabled and not required by default.


<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/mailerlite-integration-setup.png" alt="mailerlite integration setup page.">
There are two fields in the Mailerlite integration settings card. The first is your API Key, which is what connects your form submissions to your Mailerlite account. If you are unsure of how to find your Mailerlite API Key you can follow this link for instructions: [How to get Mailerlite API Key](/seachat/seachat-manual/05-integrations/05-seachat-mailerlite-integration/). There is also a link at the bottom of this card. 

The second field, "Group ID" is optional. If you want users to be added to specific groups in your mailing list you can add their ids here (separated by comma if multiple). 

## Step 3: Test Your Form