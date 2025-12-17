---
title: "Zoho Integration"
description: "Use Seasalt.ai's Zoho integration to connect with your contact center."
date: 2025-12-16T08:48:57+00:00
lastmod: 2025-12-16T08:48:57+00:00
draft: false
images: []
menu:
  seax:
    parent: "seax-omni"
url: /en/seax/seax-omni/zoho-integration-with-contacts-sync/
weight: 46
toc: true
---


This guide outlines the steps to integrate Zoho CRM with your Seasalt.ai (SeaX) workspace. This integration allows you to synchronize contact information between SeaX and Zoho CRM seamlessly.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qTT-JTFZfqc?si=A0Y6DeTtSVQrEmIm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Prerequisites
* A Seasalt.ai (SeaX) Workspace account.
* A Zoho CRM account (Free, Standard, Professional, or Enterprise).

## Step-by-Step Integration Guide

### 1. Access Integration Settings in SeaX1. Log in to your SeaX workspace.
2. Navigate to **Workspace** > **Integrations** in the left-hand menu.
3. Select **Zoho** from the list of CRM Integrations.

### 2. Create a Client in Zoho API Console

1. Open a new browser tab and go to [api-console.zoho.com](https://api-console.zoho.com).
2. Click **Add Client**.
3. Select **Server-based Applications** as the client type.
4. **Client Name:** Enter a name for the integration (e.g., `Seasalt.ai`).
5. **Homepage URL:** Go back to the SeaX integration page, copy the **Homepage URL** provided in Step 3, and paste it into the Zoho console.
6. **Authorized Redirect URIs:** Copy the **Authorized Redirect URI** from the SeaX integration page and paste it into the Zoho console.
7. Click **Create**.

### 3. Enter Credentials

1. Once the client is created in Zoho, a **Client Secret** tab will appear displaying your **Client ID** and **Client Secret**.
2. Copy the **Client ID** from Zoho and paste it into the corresponding field in the SeaX Zoho integration page (Step 2).
3. Copy the **Client Secret** from Zoho and paste it into the corresponding field in SeaX.

### 4. Authorize Connection
1. In SeaX, click the **Zoho CRM Connect** button.
2. A pop-up window from Zoho will appear asking for access permissions. Click **Accept**.
3. You should see a "Connection Successful" message in SeaX.

## How to Use the Integration

Once connected, you can sync contacts directly from the conversation view.

1. Go to **Conversations** in SeaX.
2. Open a conversation with a contact.
3. Click the **Edit Contact** icon (pencil) next to the user's details.
4. Click the **Sync Zoho** button.
* **Sync to CRM:** If you have updated details (like a name) in SeaX, click **Save & Sync to CRM** to push the data to Zoho.
* **Sync from CRM:** If the phone number exists in Zoho, the integration can pull the contact's name and details into SeaX.


## Pro Tip: Zoho CRM Free Edition
If you are a small business owner, Zoho offers a hidden **Free Edition** that supports this integration.

1. Go to the Zoho CRM Pricing page.
2. Scroll all the way to the bottom of the page.
3. Look for the "Zoho CRM Free Edition" section.
4. This version includes:
* 3 Free Users.
* 5,000 API calls per day (sufficient for most small business syncing needs).