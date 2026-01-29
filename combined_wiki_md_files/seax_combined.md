# Seax Documentation

*Combined documentation from content/en/seax (Hugo weight-ordered)*

---


### SeaX Introduction

<!-- Source: seax-omni/1-intro.md -->

<!-- Weight: 1 -->

*The Bulk Messaging & Calling Platform puts all the tools for SMS, WhatsApp and Phone Call marketing right at your fingertips.*


## What is SeaX?

**SeaX** is an omni-channel communication platform developed by Seasalt.ai that empowers businesses to conduct **bulk outreach**, **engage in two-way messaging**, and **automate responses using AI agents** — all from a single, unified interface.

Designed with marketers, customer experience teams, and operations leaders in mind, SeaX helps organizations reach thousands of users simultaneously through **SMS**, **WhatsApp**, and **Phone Calls**, with seamless support for **AI follow-up conversations** via SeaChat. It’s a modern communication hub for organizations that need to scale customer engagement without scaling human effort.

---

## Key Features

SeaX focuses on **three pillars of communication** functionality across each supported channel:

### 1. Bulk Messaging and Calling

SeaX enables you to send **high-volume campaigns** across all supported channels:

* **SMS Blasts** for time-sensitive promotions, alerts, and reminders
* **WhatsApp Campaigns** with rich content (images, buttons, quick replies)
* **Voice Broadcasts** with pre-recorded or text-to-speech content

Whether you're reaching out to 100 or 100,000 contacts, SeaX is optimized for scale. You can import your contact lists, personalize message content, and track delivery metrics in real time.

### 2. Two-Way Communication

Unlike many one-directional broadcast tools, SeaX supports **interactive conversations**. Customers can **reply directly** to your message or call, and you can continue the conversation within the SeaX dashboard — either manually or using an AI assistant.

This is crucial for:

* Lead qualification after a campaign
* Customer inquiries and support follow-ups
* Interactive surveys and opt-in confirmations

Each response is logged as a **conversation thread**, making it easy to monitor, manage, and resolve interactions as they unfold.

### 3. AI Agent Support (via SeaChat)

What happens when your campaign gets thousands of replies?

SeaX integrates natively with [SeaChat](https://chat.seasalt.ai), Seasalt.ai’s no-code AI agent platform. This enables an **AI-powered agent** to step in and carry on the conversation — instantly and at scale.

For example:

> You launch a WhatsApp campaign to 10,000 customers. 2,000 people reply with questions or intent to purchase. Rather than overwhelm your team, SeaX hands those conversations off to SeaChat agents who can qualify leads, book appointments, or answer FAQs — 24/7.

You can also choose to escalate from AI to a human agent when needed, creating a smooth **AI + human hybrid** experience.

---

## Supported Channels

SeaX currently supports the following communication channels, with more on the way:

* **SMS**
  Traditional text messaging with global reach and fast delivery. Perfect for alerts, reminders, and outreach where internet connectivity isn’t guaranteed.

* **WhatsApp**
  Engage customers with branded, verified messages that support media, quick replies, and more. SeaX connects with WhatsApp Business API to ensure compliant, scalable communication.

* **Phone Calls**
  SeaX supports both **automated voice campaigns** (using TTS or recorded messages) and **human agent dialers**. This includes:

  * **Outbound call campaigns**
  * **Inbound call handling**
  * **Click-to-call for human agents**
  * Optional AI agent support for voice interactions

Coming soon:

* **Facebook Messenger**
* **Instagram Messaging**
* **LINE**

Each channel shares the same three core capabilities: **bulk messaging**, **two-way interaction**, and **AI agent integration**.

---

## Voice Dialer for Human Agents

Beyond AI automation, SeaX includes a powerful **cloud dialer** that supports **manual outbound calling** and **inbound routing** for sales and support teams.

Agents can:

* Receive inbound calls routed from IVRs or campaigns
* Click to call from lead lists or CRM
* Record and tag calls for training and analytics
* Collaborate with SeaChat AI agents for pre-qualification or call wrap-up

This makes SeaX suitable not only for automated outreach, but also as a lightweight, flexible alternative to traditional call center platforms.

---

## Use Cases

SeaX is used across a wide range of industries and campaign types:

* **Sales & Lead Generation**
  Send outbound WhatsApp or SMS campaigns and qualify leads automatically using AI.

* **Customer Support**
  Let customers reply via chat or voice, and handle common issues with AI agents.

* **Appointment Reminders**
  Deliver reminders via SMS or voice, and allow customers to confirm or reschedule.

* **Nonprofit & Public Services**
  Send bulk notifications, health updates, and emergency alerts with two-way support.

* **E-commerce & Retail**
  Notify customers of order updates, promotions, and abandoned cart follow-ups.

---

## Summary

SeaX is the modern communication stack for teams that need to **broadcast at scale**, **converse intelligently**, and **automate efficiently** — across channels and across customer journeys. With built-in support for SMS, WhatsApp, and Phone Calls — and more on the way — SeaX helps you build meaningful conversations with the people who matter.

To learn more, visit: [https://seax.seasalt.ai/](https://seax.seasalt.ai/)


---


### SeaX FAQ

<!-- Source: seax-resources/seax-faq.md -->

<!-- Weight: 1 -->

*Bulk Messagign FAQ for SMS & WhatsApp*


## 1. What is the Twilio 30007 error, and how does it affect bulk messaging?
   
The Twilio 30007 error occurs when a carrier filters your message. This can disrupt bulk campaigns. To learn how to prevent this, check out this [blog](https://seasalt.ai/blog/102-twilio-30007-errors/).

## 2. How are "DNC" labels captured in SMS?

“DNC” labels are added to a recipient if they reply the following phrases: stop, cancel, end, quit, stopall, unsubscribe, remove me, stop sending me messages, wrong person and wrong number.


## 3. How are "DNC" labels captured in WhatsApp?

Same as SMS, “DNC” labels are added to a recipient if they reply the following phrases: stop, cancel, end, quit, stopall, unsubscribe, remove me, stop sending me messages, wrong person and wrong number.

Additionally, WhatsApp provides a button specifically to unsubscribe from marketing messages like the following “Stop Promotions” button:

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-resources/stop-promotions.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-resources/stop-promotions.jpeg" alt="Stop Promotions to capture DNC">
</a>
</center>


If a user clicks on it, then the “DNC” label will be applied to the user.

A marketer can insert this “Stop promotions” button by selecting the “Marketing opt-out” as the Quick Reply type button:

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-resources/setup-stop-promotions.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-resources/setup-stop-promotions.jpeg" alt="Stop Promotions to capture DNC">
</a>
</center>

---


### SeaX Release History

<!-- Source: seax-product-updates/seax-product-updates.md -->

<!-- Weight: 1 -->

*Stay tuned with SeaX's release history. Explore new features, performance optimizations, and bug fixes.*


### 1/8/2026

##### **<font color="#739963">New Features & Improvements</font>**

- Added automatic detection of Twilio call status and push notification failures to improve mobile-side debugging
- Call records now include call results for better review and analysis
- Outbound call logs now auto-fill agent names to prevent missing information
- Introduced a unified “All Conversations” view to browse messages across all channels
- Added channel tabs to the sidebar for quicker switching between channel-specific views

##### **<font color="#d66a60">Bug Fixes</font>**

- Fixed WhatsApp channel filtering to correctly display verified and connected statuses
- Updated the incorrect Instagram client ID for proper authentication
- Fixed incomplete AI agent list display when assigning to channels
- Corrected naming conflict errors when setting AI agents
- Fixed issue where phone number disappeared in dialpad after ending a call

### 12/29/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Improved Zoho integration with clearer error and warning indicators
- Optimized call routing logic across web and mobile devices to improve call distribution efficiency
- Automatically cleans up expired mobile device records to avoid extended ringing time
- Enhanced voice call logic to improve overall security and stability
- Push credentials for mobile devices are now automatically synced when the workspace is updated
- Added channel group settings and improved channel list management

##### **<font color="#d66a60">Bug Fixes</font>**

- Fixed incorrect page redirection after creating a new channel
- Improved error message display when Zoho sync encounters issues

### 12/18/2025

##### **<font color="#739963">New Features & Improvements</font>**

- App push credentials now auto-update when the workspace is modified
- Added CSAT metrics to the analytics page for quick agent performance review
- Conversation view shows unread badges for channel groups
- Display Zoho integration status directly in the UI
- Added push credential management: supports deletion and auto-upload
- WhatsApp template page now shows templates with headers
- After creating a new channel, system auto-redirects to the active view for smoother setup

##### **<font color="#d66a60">Bugfix</font>**

- Fixed missing plan block warning on conversation page
- Fixed scroll issue in “Get Started” guide mode
- Fixed incorrect conversation counts in channel group view

### 12/11/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Improved Zoho CRM integration with updated sync logic and clearer error handling
- Introduced CSAT scheduling for automated survey dispatch and response tracking
- Enhanced CSAT message format and frontend UI for better readability
- Backend support for "Views" to organize and categorize conversations by channel type
- Zoho phone field now supported in sync
- Added onboarding flow for new users with clearer setup steps

##### **<font color="#d66a60">Bugfix</font>**

- Fixed issue where CSAT was incorrectly sent to conversations handled by human agents
- Resolved onboarding event duplication and unintended re-triggering
- Fixed contact structure errors and Zoho phone update failures

### 12/4/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Optimized bulk contact upload performance with batch processing
- Added Zapier integration to automate SMS and WhatsApp workflows via SeaX
- Implemented backend SeaNotify event framework to support app push notifications
- Added call features and device preferences in the app to customize how users answer calls
- WhatsApp read indicators are now available in the mobile app to confirm message read status
- Contact notes now support multiple entries per contact for better knowledge tracking

##### **<font color="#d66a60">Bugfix</font>**

- Fixed issue where contact status was not synced to SeaChat
- Fixed default user status not set to offline
- Fixed integration errors when managing multiple Instagram accounts

### 11/21/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Support read receipt display on the client side when LINE and WhatsApp messages are read by the agent
- Added call statistics and integrated them into the total usage analytics dashboard
- Improved contact display to include multi-channel avatars, names, and ID information
- Backend support for multi-note structure for contacts
- Support showing the user's avatar and name by messaging channel in the conversation list
- Fixed Instagram integration issue when using multiple accounts
- Fixed WhatsApp messages not marked as read when the window is opened

### 11/13/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Adjusted read status visibility for messages on Facebook and Instagram
- Added profile fields for each messaging channel in contact data
- Updated Call Campaign result CSV fields with improved recipient and number display
- Added system message display when conversation status changes
- Revised channel creation rules for free plans and optimized UI for different user roles
- Improved wording for enabling AI agent in channel settings
- Adjusted auto-answer feature behavior and added countdown hint to improve experience
- Fixed inconsistent query conditions for unread message statistics
- Fixed issue where DNC contact messages were incorrectly forwarded to SeaChat
- Fixed issue where inbound messages failed to trigger SeaChat bot response
- Fixed contact name being overwritten during auto-dialer campaign process

### 11/6/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Added speech-to-text transcription support for voice messages in LINE, Messenger, and Instagram
- Improved contact avatar synchronization and added last-sync tracking
- Enabled linking LINE, Facebook, and Instagram channels to SeaChat bots
- Added phone number options in keyword reply and auto-reply settings
- Enabled auto-answer setting when IVR is used for inbound call handling
- Allowed users without paid plans to configure and use LINE, Messenger, and Instagram channels
- Fixed error when entering IVR settings after call transfer
- Fixed issue when editing phone numbers
- Fixed the missing WhatsApp channel issue in WhatsApp-only plans
- Fixed placeholder rendering issue in Instagram attachment messages

### 10/30/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Improved and enabled the display of profile pictures for LINE and Instagram channels
- Allowed users without a paid plan to create Messenger, Instagram, and LINE channels
- Added email notification toggle and delivery when assigning human agents
- Added display of message name for WhatsApp messages
- Fixed the issue where a pop-up blocked the screen after successfully saving a Webhook
- Fixed the incorrect error message when adding a new member
- Fixed inbound call errors after IVR setup

### 10/23/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Added backend support for Instagram messages and media attachments
- Added backend support for Facebook Messenger message handling
- Added backend support for LINE Official Account (LINE OA) integration
- Added support for LINE unfollow events with status updates via WebSocket
- Added message forwarding to SeaChat for bot processing
- Improved default agent assignment when adding channels
- Added logs for inbound voice calls to improve debugging efficiency
- Fixed an issue where the agent status became stuck on “On the Call” during inbound calls

### 10/09/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Fixed the error when enabling the SeaMeet feature
- Completed backend phases of Facebook Messenger integration: DB setup, settings management, and message handling
- Fixed the issue where the agent status was stuck on "on the call" during inbound ringing
- Fixed incorrect status color display during call ringing
- Improved status label wording for better clarity
- Fixed conversation display error

### 10/02/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Added support for displaying SeaChat AI Bot's name and reply timestamp in conversations
- Added support for assigning conversations to specific agents
- Added backend support for Bring Your Own Twilio configuration
- Added remedial logic to fix user status and end abnormal calls
- Added workspace timezone configuration to manage IVR business hours
- Fixed incorrect status color display during call ringing
- Fixed failure when exporting contact CSV files
- Fixed the contact selection issue when creating scheduled campaigns
- Fixed the incorrect calculation of unread conversation count

### 09/25/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Improved UI feedback after sending messages in Conversations, including button and message status
- Improved stability in user status handling
- Added data fields and transmission logic to sync workspaces with SeaMeet and support audio restoration
- Added remedial logic to automatically restore agent status and end abnormal calls
- Added support for converting inbound voice calls to voicemail
- Fixed and updated the display of campaign results
- Fixed the issue where recipient numbers were not displayed correctly in the WhatsApp campaign
- Disabled the auto-retry mechanism in the campaign to improve the experience
- Updated webhook subscription settings to include call-ended and meeting-ended events

### 09/18/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Fixed issue where calls during closed business hours were not logged
- Added agent status and duration display to the member page
- Introduced new agent status types: Wrap-up, Meal, Outbound, and Break
- Enabled backend support for assigning agents to conversations
- Added support for sending messages via WhatsApp Webhook
- Added human agent activity to the workspace analytics dashboard

### 09/12/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Added IVR management page with voice prompt and business hour settings
- Improved outbound call timeout to prevent early disconnection
- Enabled call logging during close hours
- Added structure to track agent status duration in real time
- Improved logic to keep agent status when reconnecting within 15 minutes

##### **<font color="#d66a60">Bugfix</font>**

- Fixed issue where WhatsApp campaigns used the wrong sending number

### 09/04/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Updated call status logs to include assigned agent name
- Increased service resource limits for CPU and memory
- Fixed user status incorrectly switching to offline after missed outbound calls
- Adjusted agent permissions for viewing the member list
- Improved outbound call timeout to prevent early disconnection

### 08/28/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Fixed issue where user online status incorrectly switched to offline
- Fixed CSV upload failure when importing contact files
- Fixed incorrect agent presence status showing as offline
- Fixed abnormal behavior when using the Dialpad
- Fixed duplicate call log entries in SeaMeet integration
- Fixed incorrect display of total message count in WhatsApp channel

### 08/21/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Improved workspace creation flow by making name and address optional
- Improved WhatsApp template search to support all categories
- Backend now supports contacts without phone numbers
- Improved onboarding flow and UI guidance
- Changed default UI theme from dark to light

### 08/18/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Improved new user onboarding with a phone number application entry
- Fixed conversation sorting and updated microphone permission request behavior
- Fixed message forwarding issue from SeaX to SeaChat when no bot messages are present
- Fixed attachment display issue in forwarded messages
- Added integration between SeaX and SeaMeet for call analytics

### 08/07/2025

##### **<font color="#739963">New Features & Improvements</font>**

- Refined call log layout and added visibility into the responsible agent for each call
- Improved workspace list behavior to hide UI when no invitations are present
- Added user activity logging during voice calls
- Fixed the dropdown menu UI overlapping issue
- Fixed issue preventing proper hang-up of inbound calls

### 07/31/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Improved contact label page and added conversation label feature
- Enhanced call tracking logs with status tracking functionality
- Improved phone number validation to support Argentina WhatsApp mobile number format
- Completed migration of Workspace API Key and event notification pages
- Fixed TwiML parsing error for outbound calls that caused call failures

### 7/24/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Added auto-answer feature for incoming calls to help agents handle calls more efficiently
- Added status change logging for live agents
- Added backend support for setting agent skills and assigning corresponding IVR menus
- Improved CSV contact import to support Ctrl+M as a line terminator
- Fixed issue with blank page display in some cases

### 7/17/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Added support for sending WhatsApp HSM campaigns with titles and multimedia files (images, documents, videos)
- Added mobile call settings for making and receiving calls
- Added a Skills page to create and assign skill groups
- Added user status overview in the member settings page
- Improved mobile interface for workspace browsing
- Fixed issue during WhatsApp binding

### 7/10/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Added support for attaching images, documents, videos, and titles in WhatsApp campaigns.
- Added support for syncing WhatsApp bulk send messages with the SeaChat AI agent.
- Added message synchronization between SeaX and SeaChat.
- Introduced a new API to fetch all templates from the user’s Meta Business Suite.
- Fixed incorrect status display issue in phone campaigns.

### 7/3/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Added support for sending media files via WhatsApp in a conversation
- Added support for sending MMS to US numbers in conversations
- Enabled backend support for attaching media files in WhatsApp campaigns
- Optimized campaign result CSV format and included fields for better readability
- Improved error display when WhatsApp message delivery fails
- Enhanced inbound call experience by preventing unnecessary busy-tone playback

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

##### **<font color="#739963">New Features & Improvements</font>**

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


---


### Bulk SMS

<!-- Source: seax-omni/5-bulk-messaging-features.md -->

<!-- Weight: 5 -->

*The SeaX Bulk Messaging Platform puts all the tools for SMS and MMS marketing right at your fingertips.*


## Overview
-------------------
The Bulk Messaging Platform puts all the tools you need for SMS and MMS marketing together in one convenient platform. On the Bulk Messaging Platform, you can:

**Send**
- Send bulk SMS and MMS messages
- Send now or schedule messages up to 7 days in advance
- Automatically filter 'Do Not Contact' customers out of send lists
- View delivery reports on bulk messaging waves
- Send messages from multiple phone numbers

**Receive**
- Capture auto opt-in and opt-out responses from customers
- Receive customer replies to bulk messaging
- Text back and continue conversations with customers

**Contact Management**
- Import and export contact lists
- Assign multiple labels to each contact
- Group contacts by label 

For an overview of the Bulk Messaging Platform, see the video below:
e

[//]: # (<iframe width="100%" height="400" src="https://www.youtube.com/embed/gztIIQcMU7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 10px;"></iframe>)
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/gztIIQcMU7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## 👥 Contacts & Customer Segments

SeaX offers several features for efficiently managing and engaging with a customer base. The contacts functionality allows users to upload customer phone numbers manually or import them from a CSV file, saving time and reducing errors. The platform also provides labeling capabilities to segment contacts based on criteria like demographics or purchase history, enabling targeted messaging. Additionally, users have the flexibility to export their contacts for backup or further analysis purposes.

[//]: # (  <iframe width="100%" height="400" src="https://www.youtube.com/embed/QQz7jRFcykA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 10px;"></iframe>)
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/QQz7jRFcykA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## 📲 Bulk Messaging & Scheduled Send

SeaX offers powerful bulk messaging functionality. Users can easily manage and organize customer information, import contacts from a CSV file, and select specific customer groups or all contacts for messaging campaigns. The platform allows users to choose the sending number, compose personalized messages with customer information fields and attachments, and review/schedule messages for sending. Additionally, users can monitor campaign progress, export campaign reports, and manage customer responses and conversations.

[//]: # (  <iframe width="100%" height="400" src="https://www.youtube.com/embed/WwiVe8URIJ8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 10px;"></iframe>)
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/WwiVe8URIJ8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## 💬 Conversations & 2-Way Texting

The SeaX platform offers a powerful Conversations feature that simplifies managing customer responses and engaging in real-time conversations. With neatly organized conversation threads, you can easily track individual exchanges and respond promptly. The platform also allows you to apply labels for categorization, filter conversations based on various criteria, and initiate personalized conversations effortlessly. Streamline your customer interactions and build strong relationships with SeaX.

[//]: # (  <iframe width="100%" height="400" src="https://www.youtube.com/embed/RKYqKkfLApo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 10px;"></iframe>)
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/RKYqKkfLApo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## 🤖 Keywords & Auto-Replies

SeaX's Keywords and Auto-Reply feature enables users to create custom responses based on specific keywords used by customers. This automation helps provide timely and relevant information while enhancing communication strategies. Users can set up default replies for messages without specific keywords and for users who want to opt-out, ensuring compliance and respectful communication. The feature also allows for the creation of custom keywords, auto-replies, and auto labels, facilitating efficient contact organization and segmentation.

[//]: # (  <iframe width="100%" height="400" src="https://www.youtube.com/embed/vzRzeruU-G0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 10px;"></iframe>)
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/vzRzeruU-G0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## 🏢 Agency/Franchise Mode

For clients with multiple businesses or multiple locations, SeaX offers workspaces. Workspaces are separate instances within the SeaX platform, allowing for data separation and management of multiple businesses or locations. Users can assign phone numbers to specific business locations, streamlining communication, enhancing customer experience, and enabling detailed analysis. The platform also provides user permissions, allowing for efficient access management and collaboration across the organization.

[//]: # (  <iframe width="100%" height="400" src="https://www.youtube.com/embed/pE7jgn-FeKg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 10px;"></iframe>)
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/pE7jgn-FeKg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## 🧑‍💻 API Access

SeaX API allows users to integrate and automate messaging workflows, providing the flexibility to manage campaigns programmatically. By utilizing the API, users can incorporate messaging capabilities into their own applications or systems, streamlining operations, automating processes, and efficiently scaling messaging efforts. The API documentation offers detailed information and guidance for seamless integration, and users can obtain their API key from the "Settings" tab to securely access the API functionalities.

[//]: # (  <iframe width="100%" height="400" src="https://www.youtube.com/embed/2mLc5mbTvYE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 10px;"></iframe>)
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/2mLc5mbTvYE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>


---


### WhatsApp Business Platform

<!-- Source: seax-omni/10-whatsapp-business-platform.md -->

<!-- Weight: 10 -->

*SeaX users can connect their WhatsApp Business Platform to SeaX to integrate WhatsApp Cloud API.*


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




---


### WhatsApp Coexistence

<!-- Source: seax-omni/11-whatsapp-coexistence.md -->

<!-- Weight: 11 -->

*Seasealt.ai users can connect their existing WhatsApp Business App to sealt.aieaX to integrate WhatsApp Cloud API features while retaining the native mobile app.*


WhatsApp Coexistence is a new offering from Meta that allows business owners to retain the native **WhatsApp Business App** on their phone while simultaneously gaining the enterprise capabilities of the **WhatsApp Cloud API** (WhatsApp Business Platform).

This feature solves the "scaling problem" faced by small businesses. Previously, moving to the API meant losing the mobile app interface. With Coexistence, businesses can keep the flexibility of the mobile app for personal use or on-the-go replies, while using Seasalt.ai to scale with unlimited agents, unified inboxes, and automation.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seax/en/whatsapp-coexistence/whatsapp-coexistence-diagram.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/whatsapp-coexistence/whatsapp-coexistence-diagram.png" alt="WhatsApp Coexistence Diagram">
</a>
</div>
</div>

## 🎥 Video Tutorial

<iframe width="100%" height="400" src="https://www.youtube.com/embed/JPCbcEBlA50?si=Y3MraDbobI_jcm-h" title="WhatsApp Coexistence Tutorial" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

This video tutorial demonstrates how to set up WhatsApp Coexistence, enabling you to sync messages between your phone's native app, the Seasalt.ai web dashboard, and the Seasalt.ai mobile app.

### What you will learn in this video: 
Small business owners often face a dilemma: keep the convenient WhatsApp Business App or upgrade to the powerful API and lose the native interface. This video introduces "WhatsApp Coexistence"—a beta offering that gives you the best of both worlds. Watch how SeaX enables you to break the 4-device limit, sync chats in real-time between your physical phone and the web platform, and let employees reply on the go, all while keeping your original Business App active.

### Timestamps: 
0:00 - The WhatsApp Scaling Problem: Convenience vs. Scale 

0:38 - Introducing WhatsApp Coexistence: Best of Both Worlds 

0:54 - The Solution: SeaX Unified Inbox 

1:29 - Step-by-Step Setup: Linking Your Native App to the Cloud 

3:25 - Understanding Data Sharing & Sync Rules 

4:50 - Live Demo: Real-Time Sync between Phone & Web Dashboard 

6:32 - The "Tri-Sync" Experience: Personal App, Business App, and Platform 

7:55 - Scaling Your Team: Agents on the Go with SeaX Mobile App 

9:05 - The Owner Experience: Total Control & Flexibility

### Prerequisites

Before setting up WhatsApp Coexistence, ensure you have:

**Device & Account Requirements**

* A smartphone with the **WhatsApp Business App** installed and active.
* A **Meta Business Suite** account (Facebook login).
* Admin access to the relevant Meta Business Portfolio.

**Platform Access**

* Active Seasalt.ai platform account.
* Access to the **Channels** configuration menu in Seasalt.ai.

### Connecting via Coexistence

#### Initial Setup Process

1. **Navigate to Channel Settings**
* Go to **Workspace** → **Channels** in Seasalt.ai.
* Click **Add New Channel**.
* Select the **WhatsApp Coexistence** option (Beta Offering).


2. **Confirm Coexistence**
* A confirmation modal will appear explaining the benefits (keeping your phone app active while using the API).
* Click **Confirm** to proceed.


3. **Log in with Facebook**
* A popup will appear asking you to log in with your Facebook/Meta account.
* Select your **Business Portfolio** (e.g., "Seasalt AI").
* Select your **WhatsApp Business Account**.



#### Selecting the Coexistence Option

This is the critical step that distinguishes Coexistence from a standard API connection.

1. **Choose "Connect a WhatsApp Business App"**
* In the setup screen, look for the option: **Connect a WhatsApp Business App**.
* *Note: This option only appears if Meta detects you are eligible for the Coexistence beta.*
* Do **not** select "Create a WhatsApp Business Account" if you wish to keep your app history.


2. **Enter Phone Number**
* Enter the phone number currently registered to your WhatsApp Business App.
* You can find this in your app under **Settings** → **Business Profile** → scroll down to phone number.
* Click **Next**.


3. **Verify Existing Account**
* Meta will detect the existing account. Click **Next** to proceed.
* You will be prompted to **Scan a QR Code** to link the app.



#### Linking the Device

1. **Scan QR Code**
* On your computer screen, a QR code will appear labeled "Connect to Business Platform."
* Open **WhatsApp Business App** on your phone.
* Go to **Settings** → **Linked Devices** → **Link a Device**.
* Scan the QR code displayed on your screen.


2. **Confirm Data Sharing**
* A prompt on your computer will ask about chat history syncing.
* You can share up to **6 months** of chat history (Note: strictly 1-on-1 chats; group chat history is not shared).
* Click **Confirm**.


3. **Double Confirmation**
* You may be asked to scan the QR code a second time for security confirmation.
* The system will process the connection (this may take a few minutes).


4. **Finalization**
* Once connected, you will receive a message from "Facebook Business" on your WhatsApp mobile app confirming the connection.
* In Seasalt.ai, click **Next** and **Confirm** to finish the setup.



### Features & Synchronization

Once connected, your business operates in a "Tri-Sync" state, synchronizing data between three points:

1. **Native WhatsApp Business App:** The app stays on your physical phone. You can use it as normal.
2. **Seasalt.ai Web Dashboard:** All incoming and outgoing messages appear here for your support team.
3. **Seasalt.ai Mobile App:** Employees can use the Seasalt.ai app to reply on the go without needing the owner's physical phone.

#### Synchronization Rules

* **Incoming Messages:** Appear instantly on the phone app, Seasalt.ai Web, and Seasalt.ai Mobile.
* **Outgoing Messages:**
* Replies sent from the **Phone App** appear in Seasalt.ai.
* Replies sent from **Seasalt.ai** (Web or Mobile) appear in the Phone App.


* **Chat History:** Up to 6 months of historical 1-on-1 chats are imported to Seasalt.ai. Group chats are not synced.
* **Connection Maintenance:** Meta requires you to open the WhatsApp Business App on your phone at least **once every 14 days** to keep the connection alive.

### Use Cases

**For the Business Owner:**

* Continue using the familiar native WhatsApp interface for personal oversight.
* No need to scan QR codes daily for web access.
* Retain full visibility of all agent activity on your personal device.

**For the Support Team:**

* **Unlimited Agents:** Assign multiple agents to handle conversations via Seasalt.ai; overcome the 4-device limit of the native app.
* **Agents on the Go:** Employees can download the **Seasalt.ai Mobile App** to answer customer queries from their own phones without accessing the owner's WhatsApp account directly.
* **Automation:** Enable SeaChat AI agents to handle queries during off-hours (requires configuration in Seasalt.ai).

### Troubleshooting

**Connection Status**

* If messages stop syncing, ensure the primary phone with the WhatsApp Business App has been opened within the last 14 days.
* Check the **Channels** tab in Seasalt.ai to ensure the number status is "Connected."

**Payment Methods**

* While the native app is free, using the Cloud API for marketing templates requires a payment method added to your WhatsApp Business Manager.
* You can add this during setup or later in the Meta Business Suite settings.

**History Syncing**

* If historical chats do not appear immediately, allow up to 24 hours for the initial sync to complete.
* Remember that media and messages from **Group Chats** are not supported in the Coexistence sync.

## Operational Workflow

Once connected, the synchronization works across three distinct platforms, creating a unified omni-channel experience.

### 1. The Business Owner (Native App)

The business owner retains their native **WhatsApp Business App** on their phone. They can send and receive messages normally. All activities performed here are mirrored instantly to the Seasalt.ai platform.

### 2. The Support Team (Web Dashboard)

Office employees utilize the **Seasalt.ai Web Dashboard**.

* **Unified Inbox:** Incoming WhatsApp messages appear alongside other channels (SMS, Instagram, etc.).
* **Assignment:** Managers can assign specific conversations to unlimited human agents or AI agents.
* **Scale:** Removes the 4-device limit, allowing hundreds of agents to work on the same WhatsApp number simultaneously.

### 3. Field Employees (Seasalt.ai Mobile App)

Employees on the go can use the **Seasalt.ai Mobile App** (distinct from the WhatsApp app).

* They can view assigned conversations and reply to customers.
* Messages sent from this app appear to the customer as coming from the business's WhatsApp number.
* These messages also sync back to the owner's native WhatsApp Business App.

## Feature Summary

| Feature | WhatsApp Business App | Cloud API (Standard) | **WhatsApp Coexistence** |
| --- | --- | --- | --- |
| **Device Limit** | 4 Devices | Unlimited | **Unlimited (via Seasalt)** |
| **Native Phone App** | Yes | No | **Yes** |
| **Chat History Sync** | N/A | No | **Yes (up to 6 months)** |
| **AI/Bot Integration** | Limited | Yes | **Yes** |
| **Setup Method** | Phone Number | API Key | **QR Code Scan** |


---


### WhatsApp Business App (Deprecated)

<!-- Source: seax-omni/20-seax-whatsapp-integration.md -->

<!-- Weight: 20 -->

*Integrate WhatsApp with SeaX for enhanced customer engagement. Follow our step-by-step guide to set up and manage WhatsApp campaigns.*


SeaX supports WhatsApp integration, allowing you to connect with your customers on WhatsApp. This guide will walk you through the steps to integrate WhatsApp with SeaX. Start leveraging the power of SeaX to engage with your customers on WhatsApp today!

---
## Connect WhatsApp with SeaX

Head to **Channels** under **Workspace** in the sidebar menu. Click on **WhatsApp Business App** to start the integration process.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/whatsapp-integration/channel-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/whatsapp-integration/channel-dashboard.png" alt="SeaX | WhatsApp | Channels Dashboard">
</a>

*Click on **WhatsApp Business App***
</center>

### Step 1: Connect Device to WhatsApp Business App

Follow the instructions to connect your device to the WhatsApp Business App using the QR code.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/whatsapp-integration/qr-code.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/whatsapp-integration/qr-code.png" alt="SeaX | WhatsApp | WhatsApp QR Code">
</a>

*Connect to WhatsApp using QR Code*
</center>


### Step 2: Follow the Instructions on WhatsApp App

Follow the Link and QR code instructions on your App to connect your device to WhatsApp. Check [here](https://faq.whatsapp.com/1317564962315842/?cms_platform=web) for more information.

### Step 3: Connect WhatsApp to SeaX

Once you have successfully connected your device, head back to **Channels** under **Workspace** in the sidebar menu. Now your account should be connected to WhatsApp, as stated in the image below.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/whatsapp-integration/connection-status.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/whatsapp-integration/connection-status.png" alt="SeaX | WhatsApp | Connection Status Notification">
</a>

*Connected Successfully*
</center>

## Test it Out!

Simply go to **Conversations** in the sidebar menu and start chatting with your customers on WhatsApp. You can now leverage the power of SeaX to engage with your customers on WhatsApp utilizing tools such as campaigns and bulk messages.

## Multiple WhatsApp Accounts

For business that have multiple Whatsapp business accounts, you will find this feature to be particularly useful as it allows you to collect all your accounts in one place. 

Traditionally, WhatsApp Business App only allows you to log into 4 devices that means only up to 4 people can chat in WhatsApp Business App. However, with SeaX, you can connect as many WhatsApp business accounts to SeaX as you want. 

You can connect them to SeaX by clicking on **Add Account** in the **WhatsApp** section of **Channels**. Follow the same steps above to connect your additional WhatsApp accounts to SeaX.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/whatsapp-integration/multiple-whatsapp-accounts.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/whatsapp-integration/multiple-whatsapp-accounts.png" alt="SeaX | WhatsApp | Multi. WhatsApp Accounts">
</a>

*Add Multiple WhatsApp Accounts*
</center>


Once all the accounts are connected, let's go to **Number** section by clicking on the **Number Settings** in the dropdown menu right next to your avatar. 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/whatsapp-integration/number-settings-shortcut.png" target="_blank">
<img width="50%" style="border-radius: 0.4rem" src="/images/seax/en/whatsapp-integration/number-settings-shortcut.png" alt="SeaX | WhatsApp | Channels Phone Number Setting Shortcut">
</a>

*Number Settings*
</center>

Not only can you edit all your connected accounts here, but you can also have a much better overview of all your connected accounts thanks to the detailed information and labeling provided the **Number** table.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/whatsapp-integration/number-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/whatsapp-integration/number-dashboard.png" alt="SeaX | WhatsApp | Number Dashboard">
</a>

*Find Connect Numbers*
</center>

From SMS to WhatsApp, you can assign different agents to different WhatsApp accounts or numbers, and all these will be managed in just one single user interface of SeaX. No longer do you need to switch between different devices or accounts to manage your business channels, and neither do you need to worry about the capacity of connecting devices in WhatsApp Business App.


## :dart: Troubleshooting

- Connection Issue: If your account failed to connect to WhatsApp after you logged in, please try to reconnect your device to WhatsApp Business App by clicking on **Reconnect** in the **WhatsApp Business App** dashboard.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/whatsapp-integration/reconnect-app.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem" src="/images/seax/en/whatsapp-integration/reconnect-app.png" alt="SeaX | WhatsApp | Reconnect WhatsApp">
</a>

*Reconnect App*
</center>










---


### SeaX Bulk Send/Call with SeaChat

<!-- Source: seax-omni/30-seax-agent-bulk-send.md -->

<!-- Weight: 30 -->

*Master bulk messaging with SeaX and SeaChat. Learn to set up AI agents, automate campaigns, and streamline communications.*


## SeaX Bulk Send SMS/WhatsApp/Call with SeaChat

SeaX bulk messaging offers a powerful way to manage communications across multiple business channels from a single platform. With SeaX, you can not only send messages to different customers but also automate these conversations by integrating with SeaChat.

This guide will walk you through the process of sending bulk messages and calls using SeaX and SeaChat, helping you streamline your business communication.

## 🎥 Video Tutorial for Bulk Calling

A comprehensive video tutorial demonstrates step-by-step how to set up and use SeaX with phone calls, including both outbound campaigns and inbound call handling by AI agents.

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/An4n8JhhdvA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

See [cross reference with SeaChat]({{< ref "seachat/seachat-manual/05-integrations/08-seax-integration-bulk-phone-calls.md" >}})

## 🎥 Video Tutorial for Bulk WhatsApp Messaging (Campaigns)

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/WUwn2QoeBGA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

See [cross reference with SeaChat]({{< ref "seachat/seachat-manual/05-integrations/09-seax-integration-whatsapp-in-seachat.md" >}})

## Set Up Workspace

To integrate SeaX with SeaChat, you'll need a phone number to send messages and an AI agent to handle the conversations. You can find phone numbers in the **Numbers** section under **Workspace** on SeaX and AI agents in the **Agents** section under **Workspace** on SeaChat.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/seax-number.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/seax-number.png" alt="SeaX | SeaX Number Setup">
</a>

_SeaX Numbers_

</center>

> 🚨 Attention 🚨
>
> Ensure you operate in the same workspace on both SeaChat and SeaX for proper integration. The AI agent and phone number must be within the same workspace.

## Create an AI Agent on SeaChat

First, deploy a functional AI agent on SeaChat and set up the SeaX integration. As SeaX is primarily a messaging platform, you will need to navigate to SeaChat to configure the AI agent.

For more information, see the [SeaX integration on SeaChat](https://wiki.seasalt.ai/seachat/integrations/seax-seachat/).

## Bulk Send with SeaX

Once the integration is set up, you can start sending bulk messages with SeaX. There are various features available with SeaX integration on SeaChat. Let’s first ensure SeaX is properly configured before starting.

### Recipients

In the initial step of sending a bulk message, select the recipients. With potentially thousands of contacts, use the labels feature in SeaX to simplify this process. Create labels for different contact groups and select these labels to choose the recipients. When adding new contacts, simply assign the appropriate labels.

All labels can be seen in the **Recipients** section under bulk messages, allowing you to select the label for bulk messaging.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/recipient-step.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/recipient-step.png" alt="SeaX | Recipient Setup">
</a>

_Labels of Recipients_

</center>

### Contacts

After selecting recipient labels, you'll be directed to the **Contacts** section. Here, you can view contact names, phone numbers, and their associated labels. Uncheck any contacts you do not wish to include in the message, and proceed to the **Compose** section.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/contact-step.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/contact-step.png" alt="SeaX | Contact">
</a>

_Manage Contacts_

</center>

### Compose a Campaign for Outbound SMS and Calls

A campaign is the unit for sending bulk messages. Configure the campaign’s name, associated contact labels, execution method, and timing here.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/compose-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/compose-dashboard.png" alt="SeaX | Campaign Dashboard">
</a>

_Compose a Campaign_

</center>

#### Campaign Name and Labels

When creating a campaign, provide a name and select the labels it will be associated with. Note that the labels on the **Compose** page are intended to be added to the selected contacts after this campaign was initiated. If you wish to send messages to specific contacts, you need to select the labels in the **Recipients** section and do so in the **Contacts** section.

#### Outbound SMS and Calls

After setting the campaign name and labels, choose the execution method. Select **Chat/Voice Agent** to allow the AI agent to handle outbound messages.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/campaign-execution.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/campaign-execution.png" alt="SeaX | Executing SeaX Campaign">
</a>

_Campaign Execution_

</center>

> 🔖 NOTE
>
> Ensure the AI agent is set up on SeaChat to handle outbound/ inbound messages. Since SeaX is a messaging platform, configure the AI agent’s starting message, voice, and other settings on SeaChat.
>
> Click **Configure AI Agent** next to your selected agent on SeaX to configure the agent on the SeaChat platform.
>
> If your agents are not visible, it means the AI agent is not set up on SeaChat. Click on **Configure AI Agent** to set up the AI agent and remember to save your configuration.

#### Sending Time

Set up the sending time for scheduled campaigns. You can choose to send the campaign immediately or schedule it for a later time. For outbound calls, set a cut-off time to avoid disturbing customers late at night.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/schedule-setting.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/schedule-setting.png" alt="SeaX | Schedule Setup">
</a>

_Scheduled Setting_

</center>

> Additional Setting - Capture Recipients' Key Presses (Outbound Calls) and Click Tracking (Outbound SMS)
>
> SeaX tracks interactions between recipients and the AI agent. Enable **Capture Recipients' Key Presses** to record key presses during calls, useful for surveys.
>
> Enable **Click Tracking** to monitor clicks on SMS messages, such as tracking link clicks.

### Senders

Select the sender for the campaign and choose the phone number to send messages from.

To add a new phone number, click **Quote for a New Number**, and Seasalt will provide a quote.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/sender.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/sender.png" alt="SeaX | Sender Setup">
</a>

_Senders Setting_

</center>

### Review

Before sending the campaign, review the settings to ensure everything is configured correctly. Check the campaign name, SeaChat message setup for the AI agent, and the sender details.

#### Update Inbound Agent

For SMS and call campaigns, update the inbound agent to handle incoming messages. Choose the agent set up on SeaChat for this purpose.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/inbound-agent-update.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/inbound-agent-update.png" alt="SeaX | SeaX Number Setup">
</a>

_Inbound Agent Setting_

</center>

### Send Out the Campaign

Click **Send Now** to activate the campaign and start sending messages through SeaX. Monitor the progress of your campaigns in the **Campaigns** section in the sidebar.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/seax-agent-bulk-send/campaign-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/seax-agent-bulk-send/campaign-dashboard.png" alt="SeaX | Send out Campaign">
</a>

_Campaign Dashboard_

</center>

## Conversation synchronized between SeaX and SeaChat

SeaX + SeaChat is a powerful combination for managing bulk messaging and calls. With SeaX, you can send messages to thousands of customers and automate conversations with the help of AI agents on SeaChat. The two conversations, one on SeaX and the other on SeaChat, are synchronized for a seamless experience. Yet, there are the following differences:

- All the outbound calls initiated by SeaX through SeaChat agents are listed in both the **Conversations** section on SeaChat and SeaX. However, if a call is received from on SeaChat, then it will not sync to SeaX.

- If the user replies to a SMS from SeaX, it will not be synced to SeaChat unless that same number in SeaX is a recipient of an active AI Agent Campaign.


---


### SeaX Inbound/Outbound Call with a Dialpad

<!-- Source: seax-omni/40-phone-call-dialpad.md -->

<!-- Weight: 40 -->

*Use SeaX to place phone calls for your Twilio phone number*


SeaX provides a comprehensive contact center solution that allows you to handle both inbound and outbound phone calls using an integrated dial pad interface. This feature complements SeaX's existing capabilities for large-scale outbound campaigns, WhatsApp messaging, and SMS communications.

## 🎥 Video Tutorial for Dialpad

A comprehensive video tutorial demonstrates step-by-step how to set up and use SeaX with phone calls, including both outbound and inbound calls handled by human agents.

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/1luD3EFnIu4?list=PL8K7_LTqly45pLJ1NAw3P3VlPseovylOC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


**Key Features Covered:**
- ✅ Dial pad setup and configuration
- ✅ Inbound call handling
- ✅ Outbound call management
- ✅ AI agent integration
- ✅ Multi-agent round robin system
- ✅ Contact management and call logs

### Prerequisites

Before using the dial pad feature, ensure you have:
- An active SeaX workspace
- Phone numbers configured for voice calls
- Proper audio devices (microphone and speakers) configured
- Agent status set to "Available"

### Setting Up Your Dial Pad

#### Agent Configuration

1. **Access the Dial Pad**: Navigate to your SeaX workspace and locate the dial pad interface
2. **Set Agent Status**: Change your status to "Available" to receive incoming calls
3. **Configure Audio Devices**: 
   - Select your preferred speaker (computer speaker or external device)
   - Choose your microphone input
   - Test audio settings before taking calls

#### Phone Number Setup

1. **Navigate to Numbers**: Go to **Workspace > Numbers** to view your available phone numbers
2. **Verify Voice Enablement**: Ensure your numbers are enabled for voice calls (you'll see options for SMS, MMS, and phone calls)
3. **Check Number Types**: SeaX supports various number types including:
   - WhatsApp-enabled numbers
   - SIP trunking for legacy PSTN lines
   - Standard phone numbers with SMS/MMS capabilities

### Handling Inbound Calls

#### Receiving Calls

When an inbound call arrives:
1. You'll hear an incoming call notification
2. Click to answer the call through your browser interface
3. Use the on-screen keypad during calls if needed for IVR navigation

#### Call Management Features

- **Call Logs**: Access detailed logs of all incoming and outbound calls
- **Contact Integration**: Numbers registered in your contacts will display associated names
- **Multi-Channel Integration**: The same number can be used for both voice calls and WhatsApp messaging

### Making Outbound Calls

#### Manual Dialing

1. **Open Dial Pad**: Access the dial pad interface
2. **Search Contacts**: Use the search function to find existing contacts
3. **Select Number**: Choose the appropriate number if multiple options are available
4. **Initiate Call**: Click to start the outbound call

#### AI-Assisted Dialing

SeaX offers AI agent integration for outbound calls:
1. **Select AI Agent**: Choose from available voice AI agents configured in SeaChat
2. **Enter Target Number**: Input the recipient's phone number
3. **Start AI Dial**: The AI agent will make the call on your behalf
4. **Use Cases**: Perfect for job interviews, appointment scheduling, or follow-up calls

### Advanced Configuration

#### Number Assignment

For each phone number, you can configure:
- **Multiple Agent Assignment**: Assign several agents to handle calls for a single number
- **Default Inbound Agents**: Set whether humans or AI agents handle incoming calls by default
- **Channel-Specific Settings**: Configure different agents for SMS vs. voice calls

#### Round Robin System

When multiple agents are assigned to a number:
- Calls are distributed to available agents in round-robin fashion
- Each agent receives a 10-second ring before the call moves to the next available agent
- System prioritizes agents with "least busy" status
- If no human agents are available, calls can automatically transfer to AI agents

### Integration with Other SeaX Features

The dial pad functionality integrates seamlessly with:
- **Large-scale outbound campaigns**
- **WhatsApp Business messaging**
- **SMS and MMS communications**
- **SeaChat AI agents for omnichannel support**

### Best Practices

1. **Agent Availability**: Keep your status updated to ensure proper call routing
2. **Audio Quality**: Use quality headsets for better call experience
3. **Contact Management**: Maintain updated contact lists for efficient outbound calling
4. **AI Backup**: Configure AI agents as backup for when human agents are unavailable
5. **Call Logging**: Regularly review call logs for performance insights

### Troubleshooting

**Common Issues:**
- **Audio Echo**: Adjust microphone and speaker settings to prevent feedback
- **Missed Calls**: Ensure agent status is set to "Available" and audio notifications are enabled
- **Number Configuration**: Verify phone numbers are properly enabled for voice calls in the Numbers section

This dial pad feature transforms SeaX into a complete human-AI native contact center solution, allowing seamless transitions between automated campaigns and personal customer interactions.

## 📷 Tutorial for Dialpad with Product Pictures

### Overview

SeaX integrates both internal and external phone communication into a single platform. On this platform, you can:

**Making and Receiving Calls**

* Search or type a number to start a call right from the platform  
* Pick up incoming calls without switching apps  
* Choose from different outbound numbers or let an AI agent handle the call for you.

**Call Management**

* All inbound, outbound, and missed calls are logged automatically  
* Saved contacts appear by name in your call history, not just as numbers.  
* Easily search call logs to follow up or check history

**Contact Management**

* Import and export contact lists  
* Assign multiple tags to each contact  
* Group contacts by tags for easier organization

### Dialpad Calling

SeaX provides a built-in dialpad, enabling users to make and receive calls directly through the platform—no external devices or apps required.

#### How to Make an Outbound Call

Click the dialpad icon at the top right to open the dialpad. Enter a number manually or search by name or number to quickly place a call.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/1-dialpad.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/1-dialpad.png" alt="SeaX | Dialpad">
</a>

*SeaX Dialpad*
</center>


#### How to Answer an Inbound Call

When there’s an inbound call, a notification card will appear in the top right corner. Click to answer or decline the call.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/2-dialpad-inbound-call.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/2-dialpad-inbound-call.png" alt="SeaX | Dialpad Inbound Call">
</a>

*SeaX Dialpad Inbound Call*
</center>


#### Calling with an AI Agent

Click the arrow next to the call button in the dialpad to select an AI agent. Then enter or search for the contact’s number to place the call.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/3-dialpad-ai-agent.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/3-dialpad-ai-agent.png" alt="SeaX | Dialpad Calling with an AI Agent">
</a>

*SeaX Dialpad Calling with an AI Agent*
</center>


#### Call Log Overview

All inbound and outbound calls are logged in the call history panel on the left, where users can view or search by time, duration, contact, and more.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/4-call-logs.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/4-call-logs.png" alt="SeaX | Dialpad Call Logs">
</a>

*SeaX Dialpad Call Logs*
</center>


### Agent Status Settings

SeaX provides a status switching feature so agents can control their availability. The system routes calls based on current status.

Status Types

* Available  
* Away  
* Do Not Disturb  
* Offline  
* On a Call

#### How to Change Your Status

1. Click your profile icon at the top right after logging in to SeaX


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/5-status-menu.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/5-status-menu.png" alt="SeaX | Dialpad Status Menu">
</a>

*SeaX Dialpad Status Menu*
</center>


2. Find the status panel showing your current availability


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/6-status-menu-open.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/6-status-menu-open.png" alt="SeaX | Dialpad Status Menu Open">
</a>

*SeaX DialpadStatus Menu Open*
</center>


3. Click your current status to view all options (Available, Away, Do Not Disturb, Offline). Select your preferred status, and SeaX will update it immediately.

#### Status Effects:

Available: Green – able to receive calls  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/7-status-available.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/7-status-available.png" alt="SeaX | Dialpad Status Green">
</a>

*SeaX Dialpad Status: Available*
</center>


Away: Orange – no new calls will be routed  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/8-status-away.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/8-status-away.png" alt="SeaX | Dialpad Status Away">
</a>

*SeaX Dialpad Status: Away*
</center>


Do Not Disturb: Red – no new calls will be routed  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/9-status-do-not-disturb.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/9-status-do-not-disturb.png" alt="SeaX | Dialpad Status: DND">
</a>

*SeaX Dialpad Status: DND*
</center>

Offline: Gray – completely inactive  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/10-status-offline.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/10-status-offline.png" alt="SeaX | Dialpad Status: Offline">
</a>

*SeaX Dialpad Status: Offline*
</center>


On a Call: Automatically activated during a call and reverts after ending

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/11-status-in-the-call.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/11-status-in-the-call.png" alt="SeaX | Dialpad Status: On A Call">
</a>

*SeaX Dialpad Status: On A Call*
</center>



### Understanding Round Robin

When a phone number is set to route inbound calls to human agents, SeaX applies the following ring assignment rules based on agent status:

Ringing Logic

* Only agents with Available status will be called  
* Agents are sorted by activity time to determine the ringing order  
* Each agent is tried for 10 seconds before the system moves to the next  
* In each round, agents who were already rung but didn’t answer are skipped

Note: If only one agent is online and doesn’t answer, the system will play a busy message to the caller and end the call.

---


### Zapier Integration

<!-- Source: seax-omni/45-zapier-integration.md -->

<!-- Weight: 45 -->

*Use Seasalt.ai's Zapier integration to connect with 8000+ apps.*


# Seasalt.ai Agentic Send: Simplified Zapier Automation Guide

---

## Prerequisites
* A **Zapier** account.
* A **Seasalt.ai** account (connected to your messaging channels like SMS or WhatsApp).
* A trigger app (e.g., Google Calendar, Google Sheets, Typeform).

---



The **Seasalt.ai Agentic Send** is a powerful feature designed to radically simplify complicated, multi-step Zapier automation workflows. It collapses typically fragile, multi-step configurations (which might otherwise involve five, ten, or even seventeen steps) into a **single action step**—resulting in a workflow of **one trigger and one action**.

This tool utilizes a large language model agent to read and process raw data based on a simple prompt, automating complex data extraction, formatting, and matching tasks. The Agentic Send is compatible with all 8,000+ trigger apps available through Zapier, extending its usefulness beyond simple calendar reminders.

Find out what triggers and actions Seasalt.ai offers on Zapier: [https://zapier.com/apps/seasaltai/integrations](https://zapier.com/apps/seasaltai/integrations)

## Overview: Traditional vs. Agentic Workflow

Normally, sending an automated SMS/WhatsApp reminder from a calendar event requires a fragile, 5-step process:
1.  **Trigger:** Event Starts.
2.  **Formatter:** Extract phone number from description.
3.  **Path:** Check if the number exists.
4.  **Path Condition:** Check if the number is valid.
5.  **Action:** Send the text.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/zapier-integration/zapier-5-step.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/zapier-integration/zapier-5-step.jpeg" alt="Seasalt.ai | Zapier Integration">
</a>

*Traditional Workflow -- 5 steps*
</center>


**With Agentic Send, this is reduced to 2 steps:**
1.  **Trigger:** Event Starts.
2.  **Action:** Agentic Send (AI handles extraction, validation, and formatting).


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/zapier-integration/zapier-2-step.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/zapier-integration/zapier-2-step.jpeg" alt="Seasalt.ai | Zapier Integration">
</a>

*Agentic Workflow -- 2 steps*
</center>



## Step-by-Step Instructions

This guide outlines how to configure a Zapier workflow using the Seasalt.ai Agentic Send feature.

### Step 1: Set Up the Trigger

The trigger defines the starting point of the automation.

1.  **Select the Trigger App:** Choose the application that initiates the workflow (e.g., Google Calendar, Google Sheets, Typeform, Jotform, Google Form, Microsoft Form, or Mailchimp).
2.  **Define the Event:** Configure the specific event that activates the Zap (e.g., a new or updated row in Google Sheets, or 15 minutes before a Google event starts).
3.  **Test the Trigger:** Execute the trigger to retrieve an example payload, which will contain the raw data output.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/zapier-integration/zapier-triggers.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/zapier-integration/zapier-triggers.jpeg" alt="Seasalt.ai | Zapier Integration">
</a>

*Choose any of 8000+ Zapier triggers*
</center>



### Step 2: Implement the Agentic Send Action

This step replaces all necessary formatters, paths, and manual data matching steps.

1.  **Add the Action Step:** Immediately following the trigger, select the **Agentic Send** action offered by Seasalt.ai.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/zapier-integration/zapier-agentic-send-1.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/zapier-integration/zapier-agentic-send-1.jpeg" alt="Seasalt.ai Agentic Send Zapier Integration">
</a>

*Seasalt.ai Agentic Send Zapier Integration*
</center>



### Step 3: Define the Task using a System Prompt

The core simplification is achieved by telling the agent what to do, rather than manually configuring each task.

1.  **Write the System Prompt:** Input a simple, descriptive prompt detailing the desired action. The language model agent will use this prompt to guide its execution.
    *   *Example 1:* "I want to send a reminder to the Google calendar event participant about upcoming meeting."
    *   *Example 2:* "Extract the phone numbers from the participant list then send a SMS to remind them."

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/zapier-integration/zapier-agentic-send-2.jpeg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/zapier-integration/zapier-agentic-send-2.jpeg" alt="Seasalt.ai Agentic Send Zapier Integration">
</a>

*Seasalt.ai Agentic Send Zapier Integration*
</center>

### Step 4: Input the Data Payload

The Agentic Send agent automatically processes the raw data from the trigger output.

1.  **Input the Entire JSON Output:** Take the entire JSON payload dump from the preceding trigger step (e.g., the full Google Calendar output) and input it into the Agentic Send action. You do not need to manually parse individual fields from the payload.
2.  **Automated Processing:** The language model agent reads the entire dump and figures out the necessary next steps, including:
    *   Extracting phone numbers from the data.
    *   Guaranteeing format compliance, such as ensuring phone numbers use the **e.164 format** (even if the user did not originally put in the country code, which often causes conventional SMS/WhatsApp sending to fail).
    *   Figuring out the **contextual SMS** that needs to be sent out.
    *   Matching the payloads between the initial output and the specific SMS/WhatsApp sending tool.

### Step 5: Configure Communication Details

Specify the tool and settings for sending the message.

1.  **Select IDs/Phone Numbers:** Select necessary identifiers such as the WhatsApp ID, workspace ID, and the specific phone number used for sending.
2.  **Select Template (if using WhatsApp):** If sending via WhatsApp, select the meta-approved template name.

### Step 6: Test and Run the Zap

1.  **Test the Action:** Test the Agentic Send step to confirm the output.
2.  **Run the Zap:** Activate the workflow. The Agentic Send is a "lifesaver and a timesaver for a lot of very very complicated events" by reducing configuration errors and simplifying complexity.

## Why Use Agentic Send?

| Feature | Traditional Zapier Setup | Seasalt.ai Agentic Send |
| :--- | :--- | :--- |
| **Complexity** | High (5+ steps) | Low (2 steps) |
| **Data Extraction** | Requires "Formatter" steps | AI extracts data automatically |
| **Error Handling** | Breaks on bad formatting | AI fixes formatting (e.g., adding +1) |
| **Logic** | Requires "Paths" (If/Then) | AI decides if a number exists |


## Common Use Cases

The **Agentic Send** feature is trigger-agnostic, meaning it works with any of the 7,000+ apps on Zapier.

* **Google Sheets:** Detect a new row (e.g., a pharmacy order) and parse the row to send a pick-up notification.
* **Typeform / Jotform:** Instantly text a lead after they submit a contact form, even if they formatted their number weirdly.
* **Mailchimp:** Trigger an SMS when a user is added to a specific email list.




---


### Zoho Integration

<!-- Source: seax-omni/46-zoho-integration.md -->

<!-- Weight: 46 -->

*Use Seasalt.ai's Zoho integration to connect with your contact center.*



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

---


### SeaX Widget

<!-- Source: seax-omni/50-seax-widget.md -->

<!-- Weight: 50 -->

*The SeaX Widget allows you to integrate a widget button that your customers can click on and directly send a message to your SeaX account.*


## Overview
In this article, we will introduce the SeaX Widget, a feature of the SeaX platform that allows you to integrate a widget button that your customers can click on and directly send a message to your SeaX account. You will learn how you can set up the SeaX Widget and integrate it into your website or app.

-------------------
## Why SeaX Widget?
Providing a seamless experience for your customers is crucial for any business. SeaX Widget can be integrated into your website or app to provide your customer the means to message your SeaX account directly. By integrating the SeaX Widget into your website or app, your customer is only one click away from getting the help they need. As a business owner, you can then unify all your customer interactions in SeaX, making it easier for you to manage and respond to your customers.

## Find the Webchat Widget Dashboard
Let's first find the Webchat Widget Dashboard in the SeaX. In your sidebar menu, click on **Webchat Widget** to access the Webchat Widget Dashboard.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/widget-dashboard.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/widget-dashboard.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Webchat Widget Dashboard</p>
</div>
</div>

## Setting up your SeaX Widget
In the Webchat Widget Dashboard, you can customize the appearance of your SeaX Widget. You can change the color, size, and image of the widget button to match your website or app's design. You can also set the greeting message that your customers will see when they use the widget. Let's go over each one of these settings.

> :bulb: **Reminder**:
> 
> Every time you make a change, remember to click on the **Save** button to apply the changes.

### Bubble
The bubble setting allows you to customize the appearance of the widget button. This is what your customers will see on your website or app. By pasting the URL into the **Widget Logo**, you can change the widget's icon so that it matches your brand's design. Remember to write a friendly **Widget Popup Message** to set the greeting message. Your customers will see this message when the bubble button shows up.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/bubble-input.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/bubble-input.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Customize your bubble's design</p>
</div>
</div>

This is what your bubble button with custom greeting message will look like:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/bubble-result.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/bubble-result.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Bubble Widget</p>
</div>
</div>

### Popout

In Popout, you can customize the appearance of the chat interface that your customers will use to communicate with you via SeaX. You must provide **Widget Title** and colors for the chat interface. 

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/popout-input.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/popout-input.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Customize the style of your popout chat</p>
</div>
</div>


Scroll further on the same page to set up your chat. Make sure to provide an opening message to greet your customers when they start a chat with you via SeaX.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/chat-setup.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/chat-setup.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Chat setup</p>
</div>
</div>

That's it. Simply click on **Preview** window to see how your SeaX Widget will look like on your website or app. Once you are satisfied with the design, click on **Save** to apply the changes.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/popout-preview.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/popout-preview.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Preview your design</p>
</div>
</div>

### Custom Forms
Custom form is a powerful feature that allows you to collect information from your new customers before they start a chat with you via SeaX. You can create a form with different types of fields such as text, email, and phone number. SeaX will record these form responses as well the entire conversation history on SeaX. To create a custom form, click on **Add New Form** in the dashboard.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/zh/form-setup.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/zh/form-setup.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Customize the style of your custom forms</p>
</div>
</div>

#### Set up Form

1. **Enable This Form** - Turn on the switch to enable the form. Here you can also set the form's name and the title that the user will see.
2. **Consent Checkbox** - You can add a consent checkbox to your form. If you wish to redirect the user to the privacy policy page, you can add a link to the checkbox by enabling **Add a URL**.
3. **Submission Message** - Customize the message that the user will see after submitting the form.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/form-view.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/form-view.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Custom form</p>
</div>
</div>

#### Form Design
Set up the layout of your form. You can add different types of fields such as text, email, and phone number. You can allow different fields to be required or optional. You can also add a placeholder text to guide the user on what to input. If the default fields are not enough for you, you can add a custom field by clicking on **Plus Button** to insert additional field.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/form-design.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/form-design.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Design the input fields</p>
</div>
</div>

Once you are done setting up your form, click on **Preview** to load the latest updates, and if the form is good to go remember to click on **Save** to save your changes. 

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/form-preview.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/form-preview.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Preview custom form</p>
</div>
</div>

> :pushpin: **Note**:
>
>  Please beware that you cannot delete an active form.

## Installation

Now, all is left is to install the SeaX Widget on your website or app. You can do this by copying the code snippet provided in the **Install Widget** tab and pasting it at the end of the  <body> tag of your website or app's HTML code.

1. Find the body tag of your website or app's HTML code. 
```html
   <body> ... insert code right before the end </body>
```
2. Paste the code snippet provided in the **Install Widget** tab at the end of the body tag.

**Example:**
```html

<div id="messaging-webchat-tooltip"><div id="messaging-webchat-tooltip--inner"></div></div>
<button id="messaging-webchat-btn"></button>
<iframe id="messaging-webchat" src="https://seax.seasalt.ai/form/3de4426f-dd03-4fe6-a242-2a2d6ddb4e02"></iframe>
<style>
  /* Add your custom CSS here */
</style>
<script>
    var script = document.createElement('script');
    script.src = "https://seax.seasalt.ai/messaging/installWidget.js";
    script.onload = function() {
        init("https://seax.seasalt.ai",  "3de4426f-dd03-4fe6-a242-2a2d6ddb4e02");
    };
    document.head.appendChild(script);
</script>
```

By now you should notice the SeaX widget that is in the bottom-right corner of the page of **Install Widget**. Click on the widget to try out the chat interface that we have just built. That's it! You have successfully set up the SeaX Widget on your website or app.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/widget-done.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/widget-done.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Preview widget</p>
</div>
</div>

## Test SeaX Widget

To properly test the widget, we recommend using the **Test Widget** button in the lower right hand corner on your SeaX dashboard. This will allow you to test the widget on your website or app without having to install it.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 80%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seax/en/seax-widget/test-widget.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/seax-widget/test-widget.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Test SeaX widget interface</p>
</div>
</div>



---


### Customer Satisfaction (CSAT) Survey

<!-- Source: seax-omni/60-seax-CSAT.md -->

<!-- Weight: 60 -->

*Configure, send, and interpret Customer Satisfaction (CSAT) surveys across all connected channels to measure customer experience and agent performance.*


Collect actionable feedback with customizable, automated, and manually-triggered post-conversation surveys.

Customer Satisfaction (CSAT) surveys help you understand how customers feel about their interaction with your support team. With SeaX, you can configure a custom CSAT message, let agents send it manually, or automate delivery based on your own timing rules. The system intelligently parses customer replies and ensures feedback collection is smooth and unobtrusive.

---

## Why CSAT Matters

CSAT surveys provide measurable insights into customer experience. By using CSAT, support teams can:

- Track satisfaction trends over time
- Identify low-rated conversations and root causes
- Drive agent coaching and quality improvements
- Automate feedback collection to reduce manual work
- Maintain compliance with channel-specific messaging rules

---

## Where to Configure CSAT in the UI

1. Navigate to: **Side Menu → Workspace → Channels**

2. Click the card to open a configuration popup where CSAT settings can be enabled.

CSAT surveys are available for these channels: LINE, WhatsApp, Instagram, and Messenger. Don't see a channel you need? Contact our support team to discuss your requirements at [info@seasalt.ai](mailto:info@seasalt.ai).
<br/>

<center>
<a href="/images/seax/en/csat/CSAT_Entry.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Entry.png" alt="CSAT Entry">
</a>

</center>

<br/>

---

## Enabling and Customizing CSAT Surveys

Inside the channel configuration popup:

### 1. Enable CSAT

Toggle **Enable Customer Satisfaction Survey**.

### 2. Write the CSAT Message

Enter the message you want customers to receive.

Important guidelines:

- Only replies **1, 2, 3, 4, or 5** are counted as valid CSAT ratings.
- Your message should clearly instruct customers to reply with a single digit.  
   Example:  
   “Please rate your experience from 1–5 by replying with a number.”
  <br/>

<center>
<a href="/images/seax/en/csat/CSAT_Config_Manual.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Config_Manual.png" alt="CSAT Configuration Manual">
</a>

</center>

<br/>

### 3. Save Changes

Once saved, CSAT becomes available for both manual and automated sending for this channel.

## Manually Sending CSAT Surveys

Agents can send a CSAT survey anytime during a conversation.

How:

1. Open a conversation
2. Click the **CSAT icon** in the **top-right corner** of the conversation window
   <br/>

<center>
<a href="/images/seax/en/csat/CSAT_Send_Btn.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Send_Btn.png" alt="CSAT Send Button">
</a>

</center>

<br/>

### Meta Channel Restrictions

For Instagram, Messenger, and WhatsApp:

- The customer must have sent a message within the **last 24 hours**
- If outside the 24-hour window, the CSAT icon is **disabled** per Meta policy

You may manually send CSAT surveys as many times as needed. Manual sending doesn't have any limit.

---

## Automatically Sending CSAT Surveys

### 1. Enable Auto-Send

Toggle **Automatically send the survey after a set delay**.

### 2. Configure Delay Time

Set the number of minutes to wait after the **customer’s last inbound message** before automatically sending the CSAT survey.

<br/>

<center>
<a href="/images/seax/en/csat/CSAT_Config_Auto.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Config_Auto.png" alt="CSAT Configuration Auto">
</a>

</center>

<br/>

### How Auto-Sending Works

- A countdown begins after each inbound user message
- When the delay expires, the survey is automatically sent
- If the customer does not respond with a valid rating, the system will **retry sending** after each delay window, always based on the most recent inbound message
- Auto-sending triggers **once per conversation**, but retries continue until a valid rating is received
- Manual sending remains available at all times

---

## How CSAT Reply Parsing Works

Understanding how the system reads customer replies is critical to setting expectations.

### When a CSAT survey is sent:

The system monitors the **immediate next inbound customer message** and interprets it as follows:

---

## Case 1 — Customer replies with a valid rating (1–5)

- The system successfully parses the rating
- The rating is recorded as the CSAT score
- All automatic resend attempts stop
- No further messages will be considered CSAT replies

<br/>

<center>
<a href="/images/seax/en/csat/CSAT_Demo.gif" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Demo.gif" alt="CSAT Demo">
</a>

</center>

<br/>

---

## Case 2 — Customer replies with an invalid message

Examples:

- “Thank you!”
- “Okay.”
- emojis

System behavior:

1. The system **cannot parse** a valid rating
2. The message is treated as a **normal inbound message**
3. Auto-sending will continue retrying as configured until a valid rating is received
4. Agents may manually resend a CSAT survey at any time

This ensures the conversation flow remains natural and customers are never stuck in “survey mode.”

<br/>

<center>
<a href="/images/seax/en/csat/CSAT_Demo_Invalid.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seax/en/csat/CSAT_Demo_Invalid.png" alt="CSAT Demo Invalid">
</a>

</center>

<br/>

---

## Case 3 — Customer does not reply at all

- As soon as new inbound message arrives, the countdown timer restarts
- Auto-send will retry sending the CSAT survey after the delay expires
- Agents may manually send CSAT whenever appropriate


---


### SeaX Enterprise Contact Center (Twilio Flex)

<!-- Source: seax-enterprise/seax-features.md -->

<!-- Weight: 102 -->

*The SeaX Collaborative Contact Center boasts robust and customizable features that give your agents and supervisors the exact functionality that they need.*


## Basic Features
-------------------
The SeaX Collaborative Contact Center (Twilio Flex) puts all of your call center's tools right at your agents' fingertips in one easy interface, while automating repetitive tasks to allow your agents to focus on the ones that really need their attention.

### Omni-channel Messaging

Agents on SeaX can handle incoming requests from all of your business's platforms at once in the same interface.


[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/usb-RK7sHlA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/usb-RK7sHlA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

SeaX can handle messages from numerous platforms, including Facebook, SMS, Google Maps, WhatsApp, and Line.

#### Google Business Messages

Google Maps integration allows access to many more features, including the ability to automatically gather information about your business's amenities from its Google Maps listing.

For an overview of additional Google Maps features, please see this video below:

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/xe2Y9kmRR3M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/xe2Y9kmRR3M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

#### WhatsApp Messaging

Finally, here we show the WhatsApp integration:

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/TzToP_Ka4zM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/TzToP_Ka4zM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

### Warm and Cold Transfer

SeaX has built-in features that allow agents to transfer calls and message internally to other agents.

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/TzToP_Ka4zM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/TzToP_Ka4zM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

### Supervisor Monitor and Barge-in

Administrators on SeaX can also monitor and join in on calls for training and supervising purposes.

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/1NwEIi_8xIw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/1NwEIi_8xIw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

### Holidays and Offline Messages

SeaX is customizable to the needs of your contact center, including setting operation hours and automatic offline messages for each of your contact center phone numbers.

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/cwKanUGEHOI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/cwKanUGEHOI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

### Voicemail

SeaX records customer voicemails and assigns them to agents, ensuring quick callbacks from agents. Administrators can also recieve notification when new voicemails come in.

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/zJ9U_YnfhHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/zJ9U_YnfhHQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## Advanced Features
-------------------

The SeaX Collaborative Contact Center also has a number of advanced features that you can add to power up your contact center.

### SeaX Virtual Agent

The SeaX Virtual Agent is a chat and voice agent that can handle a wide range of basic questions about your business, addressing topics such as:

* location
* hours
* contact information
* amenities
* menu

For more complex questions that the agent cannot answer, the SeaX interface allows customers to request a **live agent**, or a human customer service representative available within the SeaX Collaborative Contact Center.

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/j75YPzA0GlI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/j75YPzA0GlI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  allowfullscreen style="border-radius: 30px;"></iframe>

### AI Knowledge Base

The AI Knowledge Base automatically searches your knowledge base about your business to give your agents the information they need in real time while talking to your customers.

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/C_e_gaZHSFA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/C_e_gaZHSFA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

For more information about our AI Knowledge Base, please see our [blog post](https://seasalt.ai/blog/22-seax-knowledge-base/) and our [webinar](https://youtu.be/FOqQ01fpKQ4) on the subject.

### AI-Powered Agent Coach

The SeaX Agent Coach provides agents with conversation objectives to meet while on their calls and checks them off in real time to help them keep track.

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/CzfCf8Pcp5A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/CzfCf8Pcp5A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

### Case Management Demo

The SeaX Case Management system allows you to store all your customer information and track open cases directly in the SeaX interface.

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/yf1REVZtRa8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/yf1REVZtRa8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

For more information about our Case Management System, please see our [blog post](https://seasalt.ai/blog/23-seax-case-management/) and our [webinar](https://youtu.be/VhD_2TV2BOM) on the subject.

### Auto Dialer

SeaX has two avaiable auto dialers: the Message Drop Dialer and the Progressive Dialer.

#### Message Drop Dialer

The Message Drop Dialer allows you to quickly deliver messages to your customers over the phone by automatically dialing and playing a message when the call is picked up.

[//]: # (<iframe width="100%" height="400" src="https://www.youtube.com/embed/8PCSHNnbqno" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
<iframe width="100%" height="400" src="https://www.youtube.com/embed/8PCSHNnbqno" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

#### Progressive Dialer

The Progressive Dialer helps your agents make outbound calls by automatically dialing and leaving voicemails, only passing the call through to the agent when a person picks up the phone.

[//]: # (<iframe width="100%" height="400" src="https://www.youtube.com/embed/2ETvOvOIRAk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
<iframe width="100%" height="400" src="https://www.youtube.com/embed/2ETvOvOIRAk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  allowfullscreen style="border-radius: 30px;"></iframe>

### SeaMeet Copilot

View statistics and analytics on your calls and meetings through the SeaMeet Dashboard. Contact centers can also review agent performance with customizable AI-powered performance metrics.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/QdA7l8F6LBk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

## Integrations
-------------------

### HubSpot Integration

Here we see the HubSpot CRM integrated into SeaX, including automatic call information syncing back to HubSpot:

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/vdieQdXH5IM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/vdieQdXH5IM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

Here we see automated inbound and outbound appointment scheduling in SeaX, integrated with the HubSpot CRM:

[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/Bth5rMlFf8s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/Bth5rMlFf8s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

### Discord Integration

Here we provide automated customer support and case tracking in Discord, using SeaX and the HubSpot CRM:


[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/iUK4YkGYI6Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/iUK4YkGYI6Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

### Salesforce Integration

Besides the usual "click-to-dial" Salesforce integration, SeaX can do the following extra automation:

* Auto create Salesforce cases
* Call recording and call logs
* Auto CSAT survey
* CSAT survey report


[//]: # (   <iframe width="100%" height="400" src="https://www.youtube.com/embed/T_L5YykYkBs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)
   <iframe width="100%" height="400" src="https://www.youtube.com/embed/T_L5YykYkBs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

---
