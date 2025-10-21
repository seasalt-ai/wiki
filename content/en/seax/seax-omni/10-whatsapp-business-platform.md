---
title: "WhatsApp Business Platform"
description: "SeaX users can connect their WhatsApp Business Platform to SeaX to integrate WhatsApp Cloud API."
date: 2024-12-21T08:48:57+00:00
lastmod: 2024-12-21T08:48:57+00:00
draft: false
images: []
menu:
  seax:
    parent: "seax-omni"
aliases:
   - /seax/seax-messaging/whatsapp-business-platform/
url: /en/seax/seax-omni/whatsapp-business-platform/
weight: 10
toc: true
---

SeaX users can connect their WhatsApp Business Platform to SeaX to integrate Meta Cloud API.

This feature allows users to access their Meta Business Manager account and manage customer channels directly from SeaX.

Power users that are operating on the Meta Business Manager can finally have a true experience of omnichannel communication that unifies all your customer interactions in one place.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/wa-business-platform-ui.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/wa-business-platform-ui.png" alt="WhatsApp Business Platform UI">
    </a>
</div>
</div>

## 🎥 Video Tutorial
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/3cqNHzvlZ1k?list=PL8K7_LTqly45pLJ1NAw3P3VlPseovylOC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


This video guide provides step-by-step instructions for creating and managing bulk WhatsApp campaigns using the SeaX platform.

### Prerequisites

Before starting your WhatsApp campaign, ensure you have:

**WhatsApp Business Platform Setup**
- A registered WhatsApp Business Platform account (Meta Cloud API)
- Phone numbers with "Connected" status and "High" quality rating
- Approved message templates from Meta

**Platform Access**
- Active SeaX platform account
- Connected WhatsApp Business Platform in your workspace

### Connecting WhatsApp Business Platform

#### Initial Connection Process

1. **Navigate to Workspace Settings**
   - Go to **Workspace** → **Channels**
   - Select **WhatsApp Business Platform**

2. **Add Your Account**
   - Click **Add Account** button
   - Login with your Meta Business Suite credentials
   - Select your business account (e.g., "Seasalt AI")
   - Choose your registered WhatsApp Business numbers
   - Complete the connection process

3. **Verify Connection Status**
   - Ensure all numbers show "Connected" status with green indicators
   - Verify quality ratings are "High" in Meta Business Manager

### Template Management

#### Creating Templates in Meta

WhatsApp Business Platform requires all message templates to be pre-approved by Meta.

1. **Access Meta WhatsApp Manager**
   - Go to **Manage Templates** section
   - Click **Create Template** button

2. **Template Configuration**
   - Select template category (e.g., Marketing)
   - Add template name and content
   - Include variables using double brackets: `{{name}}`
   - Add media samples (images, videos, documents) if needed
   - Configure action buttons (website visits, etc.)

3. **Submit for Review**
   - Click **Submit for Review**
   - Wait for Meta approval before use

#### Synchronizing Templates to SeaX

Once templates are approved in Meta:

1. Navigate to **Channels** → **WhatsApp Business Platform**
2. Click **Synchronize from WhatsApp** button
3. Approved templates will appear in your SeaX template library

### Contact Management

#### Individual Contact Creation

1. Go to **Contacts** section
2. Click **Add Contact**
3. Enter contact details:
   - Name
   - WhatsApp number in E.164 format (e.g., +1234567890)
   - Labels for segmentation
   - Additional notes

#### Bulk Contact Upload

**CSV Template Method:**

1. **Download Template**
   - Click **Import from CSV**
   - Download the contact template file

2. **Prepare Your Data**
   - Fill in required fields: Name, WhatsApp Number, Labels
   - Use E.164 format for all phone numbers
   - Separate multiple labels with commas
   - Include additional fields: Address, Business Email, etc.

3. **Upload Process**
   - Drag and drop your CSV file into the upload area
   - System will process and validate the contacts
   - Review uploaded contacts by label filters

### Creating Bulk Campaigns

#### Campaign Setup Process

1. **Access Bulk Send**
   - Navigate to **Bulk Send and Call**
   - Select **WhatsApp** option

2. **Select Recipients**
   - Choose contact labels (e.g., "WA1", "WA2")
   - Preview selected contacts
   - Click **Continue**

3. **Configure Sender**
   - Select your WhatsApp Business number
   - Add campaign name with date for tracking

4. **Choose Template**
   - Select from synchronized templates
   - Preview template with variable substitution
   - Review message content for first few contacts

#### Sending Your Campaign

1. **Final Review**
   - Verify recipient count and template content
   - Check variable substitution accuracy

2. **Send Process**
   - Click **Send Now**
   - System provides 10-second cancellation window
   - Campaign begins processing immediately

### Monitoring Campaign Performance

#### Real-time Tracking

**Campaign Dashboard:**
- Access **Campaigns** → **WhatsApp** section
- View delivery statistics: Delivered, Failed, etc.
- Monitor individual message status in **Logs**

**Message Status Types:**
- **Delivered**: Successfully received by recipient
- **Failed**: Delivery unsuccessful (with error details)
- **Read**: Message opened by recipient

#### Managing Responses

**24-Hour Response Window:**
- WhatsApp Business Platform provides 24-hour window for replies after customer contact
- Responses appear in **Conversations** tab
- Manual replies can be sent within the response window

**Automated Response Integration:**
- Consider SeaChat AI for automated 24/7 responses
- Seamless integration with WhatsApp campaigns

### Best Practices

**Contact Management:**
- Maintain clean, segmented contact lists with relevant labels
- Use E.164 format consistently for all phone numbers
- Regular contact list updates and validation

**Template Strategy:**
- Create templates for different campaign types
- Use variables for personalization
- Ensure Meta compliance for approval

**Campaign Optimization:**
- Monitor delivery rates and adjust strategies
- Track response rates for template effectiveness
- Segment audiences for targeted messaging

### Troubleshooting

**Common Issues:**
- **Failed Deliveries**: Check phone number format and recipient WhatsApp status
- **Template Sync Issues**: Verify Meta approval status and re-synchronize
- **Connection Problems**: Confirm WhatsApp Business Platform status in Meta Business Manager

**Platform Limitations:**
- No contact upload limits on SeaX platform
- Pricing remains consistent regardless of contact volume
- Templates must be pre-approved by Meta


## With pitcures: How to Connect WhatsApp Business Platform to SeaX

Go to **Channel** under **Workspace** and then click on the WhatsApp Business Platform tab.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/choose-icon.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/choose-icon.png" alt="Choose WhatsApp Business Platform Icon">
    </a>
</div>
</div>

Click on **Add Account** to connect your Meta Business Manager account to SeaX.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/add-account-btn.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/add-account-btn.png" alt="Add Account Button">
    </a>
</div>
</div>

## Add Meta Business Manager Account

Follow the steps automatically generated by the system to connect your Meta Business Manager account to SeaX.

1. Login in to your facebook account.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/meta-step-1.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/meta-step-1.png" alt="Meta WhatsApp Cloud API | Step 1">
    </a>
</div>
</div>

2. Connect your account to SeaX.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/meta-step-2.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/meta-step-2.png" alt="Meta WhatsApp Cloud API | Step 2">
    </a>
</div>
</div>

3. Fill in business information: Make sure to fill in the business information correctly, and the Business Portfolio should have available numbers that you want to connect to. 

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/meta-step-3.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/meta-step-3.png" alt="Meta WhatsApp Cloud API | Step 3">
    </a>
</div>
</div>

4. Create a WhatsApp Business Profile.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/meta-step-4.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/meta-step-4.png" alt="Meta WhatsApp Cloud API | Step 4">
    </a>
</div>
</div>

5. Add a phone number for WhatsApp: You can use the free WhatsApp number provided or add your own number. 
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/add-business-number.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/add-business-number.png" alt="Add WhatsApp Business Number">
    </a>
</div>
</div>

6. Verify your phone number
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/whatsapp-business-platform/verify-numbers.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-business-platform/verify-numbers.png" alt="Verify Business Number">
    </a>
</div>
</div>

## Key Messaging Rules

1. **Customer-Initiated Conversations**  
   Customers can initiate conversations with businesses. Businesses can respond to these messages freely within a 24-hour messaging window.

2. **Business-Initiated Conversations**  
   Businesses cannot send new messages to customers unless using pre-approved **template messages**.

3. **Template Messages**  
   Template messages allow businesses to initiate conversations with customers. Sending a template message opens a 24-hour conversation window during which additional free-form messages can be sent.

4. **Payment Method Requirement**  
   Sending template messages requires a valid payment method. Without this, businesses cannot send template messages.

## Learn More About WhatsApp Business Platform

For readers who wish to dive deeper into the WhatsApp Business Platform, its API features, or messaging policies, Meta provides comprehensive guidance and resources. Visit the [Meta for Business Help Center](https://www.facebook.com/business/help/2640149499569241) to explore:

- Best practices for messaging customers using the WhatsApp Business Platform.
- Detailed information on messaging policies, including conversation windows and template messages.
- Steps for increasing daily messaging limits and verifying your business.
- Troubleshooting common issues and understanding quality ratings.

This resource is valuable for businesses and solution providers aiming to make the most of their integration with WhatsApp Business Platform while maintaining compliance with Meta's policies.



## Sync from WhatsApp

After adding your Meta Business Manager account, you can sync your WhatsApp numbers and accounts to SeaX. Click on "Sync from WhatsApp", and SeaX will automatically sync your WhatsApp numbers and accounts. 

Now you can manage all your customer interaction on SeaX with the accessibility to features of Meta Business API directly from SeaX. 

## Further Integration with SeaChat and SeaX

Now SeaX users can handle their business logic exclusively on Meta Business Manager and communicate with customers on SeaX with the further integrability of SeaChat for automation.


