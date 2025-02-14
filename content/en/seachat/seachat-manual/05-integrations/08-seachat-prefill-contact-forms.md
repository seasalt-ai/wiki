---
title: "Programmatically Pre-Fill Contact Forms in WebChat"
description: "SeaChat supports pre-filling user information in the webchat form by detecting query strings in the webchat URL. This allows seamless integration between your website and the chat widget, so your customers don’t need to enter their details manually.
"
date: 2024-07-16T08:48:57+00:00
lastmod: 2024-07-16T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /en/seachat/seachat-integrations/seachat-prefill-contact-forms/
url: /seachat/integrations/seachat-prefill-contact-forms/  
weight: 607
toc: true
---

SeaChat supports pre-filling user information in the webchat form by detecting query strings in the webchat URL. This allows seamless integration between your website and the chat widget, so your customers don’t need to enter their details manually.

<center>
<a href="/images/seachat-integrations/widget/demo1.gif">
<img height="800px" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/demo1.gif" alt="Demo GIF of prefilling">
</a>
</center>

<br/>

Why is this important? This is mostly used in scenarios where your end users have already logged into your system, then you can use their login info to auto fill in the contact form. In this case:

1. Users save time by not manually filling the contact form once again.
2. You prevent users from inputting wrong or fake information in the contact form.

### **Use Cases**

The ability to pre-fill user details in the webchat form is particularly useful in the following scenarios:

1. Customer Support & Helpdesk  
   When users initiate a chat from a customer support portal, their details (name, email, phone) can be auto-filled to save time.
2. Logged-In Users on Websites & Apps  
   If users are already logged in, their details can be automatically injected into the webchat form.

3. E-Commerce & Sales Inquiry Forms  
   If a customer is browsing a product and needs support, their account details can be passed into the chat.

4. Booking & Reservation Systems  
   In online booking or appointment scheduling, AI agents can pre-fill customer information to confirm their details faster.

5. Lead Capture & Marketing Campaigns  
   When running email campaigns or ads, a pre-filled chat form ensures that potential leads don't have to re-enter information when engaging with the AI agent.

---

### How It Works

#### Step 1: Add a contact form to display in WebChat

1. Login to SeaChat and go to **Channels** tab.
2. Click the **Webchat Widget** card
3. On top right, go to the **Custom Forms** tab
4. Click **\+ Add New Form**
5. Enable the form by turning of the switch on top of the page
6. If you allow users to skip the form, **Allow users to skip the form** too
7. Edit the form if you would like customize
8. When finish editing, click **Save**

<center>
<a href="/images/seachat-integrations/widget/webchat form configuration.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/webchat form configuration.png" alt="webchat form configuration">
</a>
</center>

<br/>

#### Step 2: Retrieve Your Webchat Widget Code

1. Log in to **SeaChat** and navigate to the **Channels** tab.
2. Click the **Make your webchat widget support omni-channel** button.
3. Copy the **widget code** and integrate it to your website.

<center>
<a href="/images/seachat-integrations/widget/widget code page.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/widget code page.png" alt="widget code page">
</a>
</center>

<br/>

#### Step 3: Append Query Parameters to Webchat URL

You will find your webchat URL in this format in your widget code:

`https://chat.seasalt.ai/chat/uuid`

To pre-fill user details such as name, email, and phone number, you should append query parameters to all webchat URLs in your widget code.

<center>
<a href="/images/seachat-integrations/widget/widge code highlight url.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/widge code highlight url.png" alt="widge code highlight url">
</a>
</center>

<br/>

##### Field Format:

| User Information | Query Parameter |
| :--------------- | :-------------- |
| **Email**        | `_EMAIL`        |
| **Name**         | `_NAME`         |
| **Phone**        | `_PHONE`        |

##### Example: Pre-fill webchat form with user’s name, email and phone number

Your original webchat URL is:

```
https://chat.seasalt.ai/chat/uuid
```

You should modify your webchat URL as the follows:

```
https://chat.seasalt.ai/chat/uuid?_NAME=JohnDoe&_EMAIL=johndoe@example.com&_PHONE=123456
```

When the webchat loads with the modified URL, the form will be automatically populated with the provided user details:

- **Name:** John Doe
- **Email:** [johndoe@example.com](mailto:johndoe@example.com)
- **Phone:** 123456
<center>
<a href="/images/seachat-integrations/widget/demo1.gif">
<img height="800px" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/demo1.gif" alt="Demo GIF of prefilling">
</a>
</center>

<br/>

### Adding Custom Fields

SeaChat also supports pre-filling custom fields in the webchat form.

#### How to Add Custom Fields to webchat form:

1. Log in to **SeaChat** and navigate to the **Channels** tab.
2. Go to the **Webchat Widget** card.
3. Navigate to the **Custom Forms** tab and edit your form.
4. Click **\+Add** to add a new custom field.
   - When you add the first custom field, it will use `VAR_0001`.
   - If you add more fields, they will use `VAR_0002`, `VAR_0003`, and so on.

##### Custom Field Format:

| User Information        | Query Parameter |
| :---------------------- | :-------------- |
| **Custom Field Name 1** | `VAR_0001`      |
| **Custom Field Name 2** | `VAR_0002`      |

##### Example: Pre-fill webchat form with user’s name and account ID

If you want to pre-fill an **Account ID** (identified using `VAR_0001`) field in your webchat form, your updated webchat URL will look like this:

```
https://chat.seasalt.ai/chat/uuid?_NAME=JohnDoe&_EMAIL=johndoe@example.com&_PHONE=123456&VAR_0001=9876
```

When the webchat loads, the form will be auto-filled with:

- **Name:** John Doe
- **Email:** [johndoe@example.com](mailto:johndoe@example.com)
- **Phone:** 123456
- Account ID: 9876

<center>
<a href="/images/seachat-integrations/widget/demo2.gif">
<img height="800px"style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/demo2.gif" alt="Demo GIF of prefilling">
</a>
</center>

<br/>

## **Summary**

- Retrieve and integrate the **webchat widget code** from SeaChat.
- Modify the **webchat URL** with `_NAME`, `_EMAIL`, and `_PHONE` parameters.
- Add **custom fields** using `VAR_0001`, `VAR_0002`, etc.
- When users open the webchat, the form is **pre-filled automatically**.

🚀 **That’s it\! Your webchat is now set up to accept user details programmatically.**
