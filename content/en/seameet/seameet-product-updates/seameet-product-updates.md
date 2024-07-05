---
title: "SeaMeet Release History"
description: ""
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-07-03T08:48:57+00:00
draft: false
images: []
menu:
  seameet:
      parent: "seameet-product-updates"
aliases:
   - /en/seameet-product-updates/
   - /en/seameet/seameet-product-updates/
weight: 101
toc: true
---

### 06/27/2024
##### **<font color="#d66a60">Bugfix</font>**
- Resolved the issue where the bot could not properly end a meeting and start a new one if it
left due to reasons such as "not being permitted to join the meeting" or "no conversation in the meeting".
- Fixed the issue causing new users to repeat the registration process due to "login and registration process optimization."


### 06/20/2024
##### **<font color="#739963">New Features and Performance Optimization</font>** 
- Optimized the login and registration process.
- Updated the landing page.

##### **<font color="#d66a60">Bugfix</font>**
- Urgently fixed speaker recognition errors due to a temporary Google Meet update.
- Prevented duplicate speaker names from being created in meetings when using the "Change Speaker" feature.

### 06/13/2024
##### **<font color="#739963">New Features and Performance Optimization</font>** 
- Added "Change Speaker" feature - Adjust the speaker when multiple users using one Google Meet account to speak in a meeting.
- Updated "Free Plan" hours calculation - The 6-hour limit no longer resets monthly. Each account on the free plan has a total of 6 hours available. "Individual Plan" and "Team Plan" remain unaffected, with monthly resets.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed the issue where "Create New Meeting" button saved to a different workspace - Meetings were being saved to other workspaces you own.
- Resolved the issue where pressing Enter to "Create New Meeting" was unresponsive in some scenarios.
- Fixed "Delete Meeting" causing usage calculation inaccuracies.


### 06/06/2024
##### **<font color="#739963">New Features and Performance Optimization</font>** 
- Adjust the number of concurrent meetings supported by SeaMeet, update database frequency and sync speed, and implement error handling for re-join entries.
- Audio Download for Paid Users - Paid users can download audio files for meetings held after June 1st.
- Help Desk - SeaMeet users can chat with the support anytime for assistance.
- Contact Support - Users can book support sessions via Hubspot for help.

### 05/02/2024
##### **<font color="#739963">New Features</font>** 
- Extension Enhancement: Change meeting language within Google Meet extension during meetings.
- Invoice Downloads: Download subscription plan receipts on the billing page.

##### **<font color="#739963">Enhancement</font>**
- Error Status Messaging: Added error status messaging to extensions for better understanding of current bot error status.

##### **<font color="#d66a60">Bugfix</font>**
- Addressed issue with bots automatically exiting meetings.

### 04/11/2024
##### **<font color="#739963">New Features</font>** 

- Automatic Meeting Recording Reservation: After linking with Google Calendar, you can automatically reserve and record meetings from your calendar.
- Delete Scheduled Meetings: Admin or Owner can delete scheduled meetings, including those added through "Automatic Meeting Recording Reservation."

##### **<font color="#739963">Enhancement</font>**
- Workspace List: Modified the wording and presentation.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed the issue with automatic sharing of meeting recordings. Now, you can choose whether to automatically share meeting recordings with attendees from your calendar after the meeting ends.
- Fixed the issue where adjustments made to Google Calendar meetings were not immediately reflected in the SeaMeet meeting list.
- Corrected the issue with Google Calendar meeting recordings, where inviting via an extension resulted in a second copilot being added to the meeting.


### 03/28/2024
##### **<font color="#739963">Enhancement</font>**
- Update the signup page: enhance signup experience
- New Meeting Notification: Added a close button without forcing a refresh.


### 03/14/2024
##### **<font color="#739963">New Features</font>** 
- Onboarding optimization: Enhanced onboarding experience for workspace creation and initial meeting guidance.
- Unregistered user notifications: Notifying users when they have used an unregistered account to send meeting invitations to the copilot.
- Plan description translation: Added translation to Plan Description.

##### **<font color="#d66a60">Bugfix</font>**
- Resolved onboarding issue during workspace creation.

### 03/07/2024
##### **<font color="#739963">New Features</font>** 
- User status: Support adjusting team members status to active & inactive for better member list management.
- New STT model: The new STT model is now available, offering improved accuracy.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed error when joining a workspace.

### 02/22/2024
##### **<font color="#739963">New Features</font>** 
- Support for Google education account invitations: if you are using a Google Education account, please invite `meet@seasalt.ai` to your calendar invite to use SeaMeet
- Reduced workspace creation time
- Plan change notification
- Notification for plan upgrade options on browser extension
- SeaMeet Copilot can directly join if `meet@seaslt.ai` is invited as an attendee on Google Calendar

##### **<font color="#d66a60">Bugfix</font>**
- Improve app latency caused by payment plan restriction
- Paid plan banner will only appear in the free plan

### 02/01/2024
##### **<font color="#739963">New Feature</font>** 
- Released paid plan features

### 01/25/2024
##### **<font color="#739963">New Feature</font>** 
- Login: A brand new Sign-In option! In addition to using your Google account, you can now log in directly to SeaMeet using your email address with simple verification.

### 01/18/2024
##### **<font color="#739963">New Feature</font>** 
- More browser support: [SeaMeet Extension](https://chromewebstore.google.com/detail/seameet-take-chatgpt-meet/gkkhkniggakfgioeeclbllpihmipkcmn) is compatible with not only Chrome, but also Edge, Arc, and Brave browsers. This means you can have productive meetings (almost) anywhere now!
