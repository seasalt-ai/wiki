---
title: "SeaMeet Release History"
description: "Stay tuned with SeaMeet's release history. Explore new features, performance optimizations, and bug fixes."
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-12-10T08:48:57+00:00
draft: false
images: []
menu:
  seameet:
      parent: "seameet-product-updates"
aliases:
   - /en/seameet-product-updates/
   - /en/seameet/seameet-product-updates/
url: /en/seameet/seameet-product-updates/   
weight: 400
toc: true
---

### 6/5/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Enhanced audio upload with automatic speaker count detection and improved overall transcript generation efficiency.
- Updated interface for audio upload, including support for regenerating transcripts in different languages.
- Fixed an issue where new users registering via the extension were not correctly directed to the onboarding flow.
- Resolved an issue where newly invited users were not guided through the proper onboarding steps, and added redirect logic to complete onboarding.
- Refined onboarding flow to improve clarity and accuracy during sign-up and login

### 6/1/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added OTP login option via extension; removed the password login.
- Fixed an issue where clicking the extension too early when entering a meeting could block bot invitation.
- Resolved a registration flow allowing users to exit the process unexpectedly.
- Updated titles and button descriptions on the meeting share page for clarity.
- Removed individual call analytics page previously integrated with Twilio Flex.

### 5/22/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Fixed delays in transcript updates.
- Resolved audio file loss and added an automatic recovery mechanism upon error.
- Added email notification option when audio is still processing.
- Fixed occasional subscription failure when clicking the “Subscription” button in the sidebar.
- Ensured users complete registration when accessing the share page to prevent permission issues.
- Shortened the signup and onboarding flow; improved onboarding after extension installation.
- Adjusted the default time when uploading audio files.
- Fixed an issue where the wrong account was displayed when connecting Google Calendar.
- Corrected hour calculations when uploading audio scheduled for another month.
- Fixed missing error alerts when uploading unsupported audio formats.


### 5/15/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Updated audio player UI.
- Added the "Download Transcript" button to the audio player bar.
- Fixed an issue where adding a viewer to the list didn't trigger a notification email.
- Fixed a bug where disabled workspaces were still shown in the extension.
- Fixed an issue where free plan users couldn't retry diarization after an audio upload failed.
- Shortened the signup and onboarding flow.


### 5/8/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Fixed an issue where some meetings incorrectly showed audio file does not exist.
- Improved audio file retention mechanism for better stability.
- Adjusted pricing description in the subscription plan section.
- Fixed a crash issue caused by uploading audio files exceeding the length limit.
- Enhanced UX: Added a link to the SeaMeet product wiki in the browser extension.
- Enhanced UX: Updated the default theme color for newly registered users.

### 5/6/2025
##### **<font color="#739963">New Features and Improvements</font>**
 - Fixed an issue where user status could be changed before joining a workspace.
- Resolved layout issues caused by dropdown menus in popups.
- Streamlined the signup and login process.
- Clicking the "Plan" label in the sidebar now redirects to the Billing page.
- Fixed a bug in the Billing page where users couldn’t proceed in the Edit Plan popup when opened directly.
- Updated "Account" menu links to redirect to the workspace and language settings.

### 4/24/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added "Email Report" tab for enterprise users.  
- Fixed an issue where some meetings on 04/21 midnight did not generate summaries.  
- Fixed an error tooltip when the "Start Recording" button was used after exceeding the base quota in paid plans.  
- Improved clarity of the "Connect Google Calendar" reminder popup.  
- Updated the feedback survey shown during subscription cancellation.


### 4/17/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Adjusted the "Request Access" email — clicking the button will now redirect users to the "Share Meeting" popup on the meeting page.  
- Fixed layout issues in the "Share Meeting" popup under certain conditions.  
- Fixed authorization prompt display when accessing a shared meeting page in Incognito mode.  
- Fixed an issue where applying a summary template during an ongoing meeting could prematurely trigger meeting completion and stop summary updates.  
- Optimized the Google Calendar binding flow during registration and for existing users.  
- Fixed an issue where setting speaker diarization to "1 speaker" caused errors in audio file uploads.  
- Improved server resources for audio uploads to accelerate processing speed.
- Fixed cases where hallucinated prompts appeared in "Meeting Summary" or "Action Items." 
- Fixed paragraph segmentation issues in long transcripts.


### 4/10/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Enhanced "Share Meeting": when selecting "All participants in calendar event" attendees can access the meeting page after logging in.  
- Users without invitations can request access via shared meeting links. The meeting inviter will receive an email notification for each access request.  
- Workspace members can approve or reject access requests on the meeting page. Approved users will be notified via email.  
- Updated "Auto-share Meeting Notes" emails to distinguish between workspace members and external users.  
- Improved member count display on the "Members" page.  
- Updated tooltip for "Integrations" when edit Google Drive is not available.  
- Updated error messages format when the browser extension fails to connect.  
- Updated description for the "Upload Audio", including messaging for speaker diarization.  
- Urgent fix: Resolved issue where speaker identification failed due to recent Google Meet UI changes.

### 3/27/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Updated the "Auto-share Meeting Notes" email and Google Meet in-call message link. Recipients can request access to the specific shared meeting only.  
- Updated browser extension favicon to display the language currently being transcribed.  
- Refined pricing explanation in the "Edit Plan" section.  
- Added product chatbot to the landing page.

### 3/20/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Introduced meeting sharing functionality, allowing links to be shared with non-workspace users and granting access to either "Anyone with the link" or "Invited users only."
- Fixed an issue where meeting summaries generated using the "Standard Template" now align with the newly recorded transcription language.
- Prevented errors from being triggered when the bot was not allow to join a meeting and no audio recording is available.
- Corrected the fee calculation explanation for the "Edit Plan" popup.
- Fixed an issue where the language prompt was incorrect when inviting the bot to join Google Meet.
- Removed the "Upgrade" button for "Custom Plans."
- Adjusted the bot's meeting entry behavior for "Recorded Meetings."

### 3/13/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added localization support for additional languages, including Cantonese (Traditional Chinese – Hong Kong, Simplified Chinese) and Spanish (Latin America).
- Fixed an issue preventing the bot from joining meetings when invited via the extension in newly supported languages.
- Resolved an issue where summary templates could not be applied in the Individual or Team plan.

### 3/04/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added support for meeting transcription in the following languages: Spanish, French, German, Danish, Polish, Thai, Hindi, Vietnamese, Japanese, and Korean.
- Fixed timestamp errors caused by daylight saving time adjustments.
- Corrected Chinese Wikipedia links.
- Fixed an issue where replacing a speaker caused misalignment in speaker layout.
- Adjusted the sorting order for the summary template list.

### 2/20/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Introduced Summary Templates, allowing users to apply different templates for meeting summaries.
- Adjusted text layout for the Try It Now invitation button on the landing page.
- Modified the timestamp display for meetings occurring within an hour.
- Fixed an issue where English users who had not used the service for several days after registration were receiving notifications in Chinese instead of English.

### 2/13/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Added a "Try It Out" section on the product landing page.  
- Adjusted timestamps on the meeting list to display in minutes for meetings ending within an hour or starting soon.  
- Fixed an issue where logging in with an unregistered Google account on the extension would get stuck on the loading screen.  
- Fixed the calculation method for speaker ID queue.  

### 2/6/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Improved audio file upload experience, including progress bar display, restriction on submission before file upload, and guidance for incorrect file formats.  
- Corrected the FAQ section explanation regarding "In-Person Meetings" on the landing page.  


### 1/22/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Updated Google Docs meeting titles to include dates for distinguishing recurring meetings.  
- Modified the user flow after clicking the extension. 


### 1/16/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Enhanced audio upload experience with improved failure notifications, file analysis loading previews, and clearer error messages.  
- Fixed an issue where refreshing under a filtered view would not clear the filters.  
- Resolved a bug where switching workspaces did not exit the original meeting page.


### 1/9/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Improved the interface of the meeting list filter feature.  


### 1/2/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Enhanced stability of audio file uploads.  
- Added a "Retry" option for failed audio uploads.  
- Improved user experience for audio uploads by displaying queue status.  
- Supported meetings that require login, such as those initiated by educational accounts.  
- Fixed auto-join failures for HubSpot scheduled meetings.  
- Resolved an issue where the copilot wouldn't leave after 15 minutes of meeting inactivity.  
- Fixed the extension's infinite loading issue preventing meeting joins.  


### 12/19/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Fixed issues related to multi-track audio file uploads.


### 12/5/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Updated the "Upload Audio" to additionally support .m4a, .opus, .ogg, and multi-track formats, as well as file names containing spaces.
- Removed whitespace checks for "Upload Audio."
- Fixed an issue caused by Google Meet updates affecting speaker name detection.
- Updated the new account onboarding process, allowing users to choose whether to enable "Auto Join Meetings" and "Auto Share Meeting Notes."

### 12/2/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Added "Upload Audio", supporting formats like .mp3, .wav, .flac, and .aac.
- Improved automatic support for meetings initiated by educational accounts.
- Updated the FAQ section on the landing page.
- When inviting the bot to a Google Meet with a meeting name via the extension, the meeting name will now be automatically captured as the meeting title.


### 11/21/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Updated the SeaMeet landing page version
- Improved notifications for successful and failed Google Meet invitations
- Adjusted meeting status color indicators in the meeting list

##### **<font color="#d66a60">Bugfix</font>**
- Resolved an issue where users who joined a meeting early could not pre-invite the bot via the extension
- Fixed an issue where users who joined late, after the bot had exited, could not reinvite the bot

### 11/14/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Improved the retry mechanism for bot rejoining meetings
- Resolved issues with the extension's status checks
- Enhanced the stability of bot meeting recording termination

### 11/7/2024
##### **<font color="#d66a60">Bugfix</font>**
- Fixed issues with data masking for users with canceled paid plans during error masking scenarios
- Adjusted the extension's method for retrieving meeting IDs


### 10/31/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Added a light theme option.
- Adjusted meetings to fully transcribe the entire meeting (with partial data masking depending on the user's SeaMeet plan).
- Refined in-call messages to include language, inviter information, and plan details.

##### **<font color="#d66a60">Bugfix</font>**
- Improved reconnection mechanisms to handle unexpected service interruptions.

### 10/24/2024
##### **<font color="#739963">New Features and Improvements</font>**
- Introduced an audio retention mechanism to ensure full audio recording in case of brief meeting interruptions.

##### **<font color="#d66a60">Bugfix</font>**
- Resolved issues preventing SeaMeet functionality in meetings initiated by educational accounts due to recent Google updates.
- Added automated audio reconstruction attempts when errors are detected.

### 10/03/2024
##### **<font color="#d66a60">Bugfix</font>**
- Fixed incorrect or incomplete bot names when joining meetings due to Google Meet page loading issues.
- Fixed issue where canceling a plan prevented users from initiating new meetings from the meeting list.
- Updated wording for pricing plans.

### 09/26/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Automatically switch to "Final Summary" when the meeting ends.
- Adjusted the meeting list to display the summary title instead of summary content.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed the error caused by Google Calendar event IDs starting with "_".

### 09/19/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Saved both "Final Summary" and "Real-time Summary" within meetings to retain all necessary information.
- Added date grouping in the meeting list for easier differentiation of meeting dates.
- Adjusted the structure and presentation of action items.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed the issue where the extension failed to correctly capture the meeting title.

### 09/12/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Introduced Beta features for "Speaker ID" and "Re-run Summary" to split in-person meetings by speaker and regenerate summaries, available for paid users only.
- Removed automatically added meetings from the meeting list when "Auto-Join" is disabled.
- Added a safeguard to prevent duplicate subscriptions during plan selection.
- Added a "Use Case" section to the product landing page.
- Updated button styles on the product landing page.
- Optimized word segmentation in meeting transcripts.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed the issue where external users did not receive "Auto-shared Meeting Notes" emails.

### 09/05/2024
##### **<font color="#d66a60">Bugfix</font>**
- Updated the format of new meeting summaries in Google Docs.
- Standardized the template for "Auto-shared Meeting Notes."
- When replacing a speaker with "Speaker ID," the identified speaker will be automatically replaced in the participants list.

### 08/29/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Updated the presentation format for meeting summaries.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed the issue where speakers couldn't be identified due to a Google Meet update.

### 08/22/2024
##### **<font color="#739963">New Features and Performance Optimization</font>**
- Unified the structure of the extension websocket to improve SeaMeet's stability.
- Updated the tab styles within the product.

##### **<font color="#d66a60">Bugfix</font>**
- Fixed the broken product Wikipedia link.
- Resolved the issue with abnormal event IDs caused by a Google Calendar update.


### 08/15/2024
##### **<font color="#739963">New Features and Performance Optimization</font>** 
- Adjusted the email template for auto share.
##### **<font color="#d66a60">Bugfix</font>**
- Fixed the incorrect timing for plan limit prompts.
- Resolved errors caused by the Google Meet update.
- Optimized performance when syncing a large number of participants.

### 08/08/2024
##### **<font color="#d66a60">Bugfix</font>**
- Resolved the error caused by changes in Google Calendar login authentication.

### 08/01/2024
##### **<font color="#739963">New Features and Performance Optimization</font>** 
- Improved system infrastructure stability and performance.
- Optimized the user flow on the plan selection page.


### 07/17/2024
##### **<font color="#739963">New Features and Performance Optimization</font>** 
- Optimize onboarding process
- Add signup page and OTP login
- Display plan names in Chinese
- Improve copilot performance and efficiency

##### **<font color="#d66a60">Bugfix</font>**
- Correct plan name display error in plan limit messages
- Fix sorting issue for single meeting in the new meeting list
- Resolve slow transcript updates
- Fix issue where meetings didn't end properly after the bot exited in SeaMeet



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
