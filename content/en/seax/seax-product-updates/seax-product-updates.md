---
title: "SeaX Release History"
description: "Stay tuned with SeaX's release history. Explore new features, performance optimizations, and bug fixes."
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-12-10T08:48:57+00:00
draft: false
images: []
menu:
  seax:
      parent: "seax-product-updates"
aliases:
   - /en/seax-product-updates/
   - /en/seax/seax-product-updates/
# NOTE: All product update pages should follow the URL format: https://wiki.seasalt.ai/${language}/${product}/product-updates/
url: /en/seax/product-updates/
weight: 1
toc: true
---
### 6/26/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added a Human Agent option in number settings to automatically forward inbound calls to a live agent.
- Added a shortcut menu to quickly view “Sent” messages.
- Added detailed error messages when message delivery fails.
- Improved the alert message for failed WhatsApp delivery after 24 hours.
- Improved the outbound call flow.
- Fixed an issue where some users were occasionally unable to switch their current status.
- Backend now supports document, audio, video, and image messages on WhatsApp.

### 6/19/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Improved contact CSV import with dynamic parsing of WhatsApp and phone number fields.
- Added a user status selection menu to help users quickly select between Available and Away.
- Improved the onboarding flow for first-time WhatsApp setup.
- Fixed an issue where the sidebar failed to navigate to the portal. 
- Fixed an issue that caused incoming calls to fail and play an error message.

### 6/12/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Improved the display of contact search results in the dialpad.
- Inbound calls will now automatically cycle through available agents if unanswered for 10 seconds.
- Fixed an issue where making calls after entering from the workspace list view could result in an error.
- Fixed a bug that prevented WhatsApp Only plan users from accessing services until the subscription end date after cancellation.
- Fixed a plan-switching display issue when accessing the subscription page via certain links.
- Optimized conversation sorting and improved performance.
- Fixed occasional CSV upload failures.
- Fixed an issue where the SeaChat bot failed to send WhatsApp template messages.

### 6/5/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Adjusted conversation sorting logic to prioritize the latest inbound message.

### 6/1/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added WhatsApp support check before workspace import/export.
- Supported importing contact with WhatsApp fields.
- Enabled contact search in dialpad with matched contact names displayed.
- Allowed use of dialpad during active calls for input.
- Updated plan descriptions on the product landing page.
- Enhanced error messages when WhatsApp campaign sending fails.
- Filtered WhatsApp Business template with headers.
- Disabled call recording for outbound calls via dialpad.
- Adjusted WhatsApp template limit to 200.

### 5/22/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Removed the deprecated Call Analysis tab.
- Fixed issue where outbound calls couldn’t be canceled before being answered.
- Resolved issue where inbound calls did not trigger the dial pad.
- Adjusted height of the template editor.
- Fixed a bug where expired data caused call reception to fail.

### 5/15/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added detection for authorized recording devices when launching SeaX.
- Automatically fills in the default device when SeaX starts.
- Automatically sets human agent status to offline when websocket disconnects, and restores it to online upon reconnection.

### 5/6/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Updated the call logs list.
- Fixed an issue where empty chats were generated when creating new contacts.
- Resolved a memory leak issue.
- Fixed Twilio sub-account verification errors.

### 4/24/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Optimized performance for bulk message sending.  
- Synchronized phone_capability with SeaContact.

### 4/10/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Fixed issue where WhatsApp message templates could not be retrieved.  
- Fixed issue preventing message updates in SeaContact.

### 4/2/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Updated DNC keywords for Spanish.  
- Fixed missing plan title issue in the pricing section.  
- Enhanced outbound and inbound calling via dialpad.  
- Improved outbound call functionality via AI Agent.

### 3/27/2025 
##### **<font color="#739963">New Features and Improvements</font>**
- Updated "Keywords and Auto-replies" to support WhatsApp messages.  
- Fixed an issue with DNC keywords.  
- Updated chatbot bubble title.  
- Added product chatbot to the landing page.

### 3/20/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Fixed the application process and procedure for purchasing numbers.

### 3/13/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Adjusted the display of failed WhatsApp campaigns to show failure reasons for all messages.
- Enabled WhatsApp message template activation.
- Fixed an issue causing errors in the campaign initiation process.

### 3/04/2025
##### **<font color="#739963">New Features and Improvements</font>**
- MMS now correctly displays images in the conversation window.
- Fixed timestamp errors caused by daylight saving time adjustments.
- Fixed an issue where phone numbers were required to start with a "+".

### 2/27/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Displayed MegaSend count in the list.
- Added timestamp logging for label matching.
- Fixed an issue where the contact field no longer checks for case sensitivity.

### 2/20/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added MegaSend feature.
- Implemented Do Not Contact label check during MegaSend.
- Fixed an issue where loading the AI agent list took too long.

### 2/13/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Integrated SeaChat with WhatsApp Business Platform, enabling synchronization of WhatsApp Business messages to SeaChat.  
- Added AI agent assignment for WhatsApp at the numbers page, with the ability to take over or reactivate conversations from SeaX.  
- Added campaign failed status for WhatsApp campaign cards when campaign delivery fails.  

### 2/6/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added contact search functionality to the dial pad.  
- Fixed the timing of success and failure notifications for contact uploads.  

### 1/22/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added options to select "Input Device" and "Output Device" in the dial pad.  
- Adjusted the display of "Unverified Numbers" in the WhatsApp Business Platform number list.  
- Updated phone call display icons.  


### 1/16/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Introduced call logs list displaying call outcomes for inbound and outbound calls.  
- Updated campaign and channel icons for the WhatsApp Business Platform.  


### 1/9/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Fixed an issue requiring double API calls for Webhook campaigns to trigger.  
- Corrected data reporting errors in campaign cards.  
- Removed the mandatory name field requirement for contact entries.  


### 1/2/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added functionality to answer inbound calls and make outbound calls via the dial pad.  
- Fixed inaccuracies in the recipient count displayed on activity cards.  
- Corrected text content on campaign cards.  
- Adjusted reply rate calculations for sent campaigns.  
- Fixed navigation issues in the WhatsApp Business Platform message template steps.  

### 12/5/2024
##### **<font color="#d66a60">Bugfix</font>**
- Fixed an issue causing errors when generating new conversations

### 11/14/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Synchronized status displays for live agent interventions in conversations
- Updated billing breakdown
- Removed Chinese-language bot from the landing page

### 11/7/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Renamed "Memory" feature to "Extraction"
- Fixed issue with WhatsApp Business Platform where country codes lacked "+" sign


### 10/31/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Added support for binding WhatsApp Business Platform accounts and sending/receiving messages.
- Updated enable and disabled statuses for AI agent on individual numbers.
- Enhanced retrieval of AI assistant responses to queries.

### 10/24/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Added batch deletion for multiple labels.
- Optimized behavior logic across options when editing numbers.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed issues with auto label.

### 10/03/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Added dynamic loading for WhatsApp messages to avoid errors from loading too many messages.

##### **<font color="#d66a60">Bugfix</font>**
- Added a feature allowing cancel campaigns from the SeaX customer support.
- Fixed issue where "unsent messages" caused the conversations to display as blank.
- Fixed issue where SMS campaign end time was earlier than the start time.

### 09/26/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Added WhatsApp and Omni-Channel pricing plans.
- Updated plan descriptions on the landing page.
- Implemented a mechanism to prevent duplicate campaign bookings.

### 09/12/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Added the "Business Caller ID" binding feature, allowing purchased numbers to be linked with verified "Business Caller IDs" for outbound calls.
- Introduced dynamic loading for WhatsApp messages to improve overall loading efficiency and user experience.
- Added a history log for purchased numbers.
- Conversations with deleted contacts are retained and linked when contacts are re-added.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed the issue where AI agents failed to handle incoming calls.

### 09/05/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Updated the SeaX product landing page and URL.
- Introduced user registration and login processes.
- New users can create workspaces independently.
- Added the ability to forward numbers to other specified numbers.

### 08/22/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Added the feature to purchase phone numbers.
- Introduced error checking and prompts for Excel uploads.
- Added a new use case for Excel uploads, allowing batch message sending to contacts via Excel.
- Introduced background loading for WhatsApp messages to speed up message loading.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed the issue with unread message count display.

### 07/17/2024
##### **<font color="#d66a60">Bugfix</font>**
- Fixed filtering for "unread" and "replied" messages in conversations


### 06/27/2024
##### **<font color="#d66a60">Bugfix</font>**
- Fixed formatting issues with Canadian numbers.
- Resolved the issue where the count of unread messages was incorrect.
- Corrected the display issue for sending times in bulk messaging campaigns.
- Ensured the last unread message is properly displayed.
- Fixed the problem where the conversation thread would jump back to a specific conversation during loading.

### 06/20/2024
##### **<font color="#d66a60">Bugfix</font>**
- Added a "Loading" status effect when setting up mass messaging campaigns to prevent multiple creation clicks.
- Disabled Twilio AMD detection to speed up AI customer service interactions.
- Fixed the issue where workspace icons could not be replaced.
- Fixed errors in contact uploads.

### 06/13/2024
##### **<font color="#739963">New Feature</font>** 
- Added "Members" sorting functionality - Sort by account email, username, permissions, etc.


### 06/06/2024
##### **<font color="#739963">New Feature</font>** 
- Help Desk - Users can chat with the support bot anytime for assistance.
- Contact Support - Users can book support sessions via Hubspot for help.
- WhatsApp Fix - Users can edit phone numbers on the contact page.

### 05/02/2024
##### **<font color="#739963">New Feature</font>** 
- Added WhatsApp Channel: Bind WhatsApp numbers and send WhatsApp messages via SeaX.

### 03/28/2024
##### **<font color="#739963">Enhancement</font>** 
- Enhanced SeaX campaign icon: display whether the campaign is sent instantly or scheduled.

##### **<font color="#d66a60">Bugfix</font>**
- Fix bugs on widget experience, including adding a test widget button, enabling country code search in the form, adding a scroll bar to the form, and implementing URL checking.

### 03/14/2024
##### **<font color="#739963">New Feature</font>** 
- Added translation to the Plan Description.

##### **<font color="#d66a60">Bugfix</font>**
- Rectified the disappearance of the "Edit Contact's add label" button.
- Addressed the issue with the campaign page getting stuck when there are no campaigns.

### 03/07/2024
##### **<font color="#739963">New Feature</font>** 
- Webchat widget: Adding agent icon to popup message

##### **<font color="#d66a60">Bugfix</font>**
- Fix the 404 error message popup
- Adjusted widget color settings. User reply messages and checkboxes will align with the main color.

### 02/01/2024
##### **<font color="#739963">New Feature</font>** 
- Schedule send to a single contact

<center>
<img width="100%" style="border-radius: 0.4rem" src="/images/product-updates/seax/en/20240201-single-schedule-send.png" alt="SeaX - Send scheduled message to single contact">
</center>

### 01/25/2024
##### **<font color="#739963">New Feature</font>** 
- Add support for viewing Scheduled Campaigns
