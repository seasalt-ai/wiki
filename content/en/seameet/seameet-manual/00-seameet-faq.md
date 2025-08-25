---
title: "FAQ"
description: "Frequently asked questions about SeaMeet. Find answers to common queries about SeaMeet's setup, transcription, and more."
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-08-01T08:48:57+00:00
draft: false
images: []
menu:
  seameet:
    parent: "seameet-manual"
aliases:
  - /en/seameet/00-seameet-faq/
weight: 200
toc: true
---

## 1. **What types of meeting recordings and platforms does SeaMeet support?**

SeaMeet supports three ways of recording different meeting formats, including:

1. Real-time recording for Google Meet
2. Real-time recording for Microsoft Teams
3. Audio file uploads

More online meeting platforms will be supported in the future.

## 2. **How do I start recording a Google Meet session with SeaMeet?**

You have several ways to invite the SeaMeet bot to join your Google Meet and record:

1. Method 1: Use the SeaMeet Chrome extension within Google Meet to invite.
2. Method 2: Enter the Google Meet ID in the SeaMeet meeting list to start a new recording.
3. Method 3: Send a Google Calendar invite to the SeaMeet bot ([meet@seasalt.ai](mailto:meet@seasalt.ai)) to join the meeting.
4. Method 4: Link your Google Calendar, and the bot will automatically join all scheduled meetings.

## 3. **How do I start recording a Microsoft Teams meeting?**

To record a Microsoft Teams meeting, please provide the meeting link.

The link format must begin with:
[https://teams.microsoft.com/l/meetup-join](https://teams.microsoft.com/l/meetup-join)...

*SeaMeet supports links starting with teams.microsoft.com generated from Microsoft 365 Business or Enterprise accounts. Currently, links starting with teams.live.com from free accounts (Free, Personal, or Family) are not supported.*

You can obtain the meeting link by:

* Clicking **Copy meeting link** in the Teams meeting.
* Or selecting **Copy join link** from the Teams calendar.

## 4. **How do I upload an audio file? What formats are supported?**

Go to the audio file list, click **Upload Audio**, and either select or drag-and-drop the file into the upload box.

* Free plan users can upload up to 5 audio files, but can only view the first 3 minutes of transcription.
* Individual plan users can upload up to 100 audio files per month.
* Team plan users can upload up to 200 audio files per month.

Supported formats: .aac, .flac, .m4a, .mp3, .mp4, .ogg, .opus, .wav, .webm, .wma, .wmv

## 5. **Does SeaMeet support in-person meetings?**

Yes, SeaMeet supports two methods for in-person meetings:

1. Record the meeting audio yourself and upload it to SeaMeet for processing.
2. In hybrid meetings, open Google Meet, and SeaMeet will help record the entire session.

In-person meetings often include multiple speakers. After the meeting, you can use **Speaker Identification** and **Speaker Reassignment** features to distinguish speakers.

## 6. **Can SeaMeet detect and differentiate speakers in a meeting?**

Yes, SeaMeet can label speakers as “Speaker 1,” “Speaker 2,” etc., and allows you to reassign them to actual participant names in bulk. The recognition works best when there are 2–6 participants.

## 7. **What languages does SeaMeet support for transcription?**

SeaMeet currently supports the following languages:

* English (U.S., Singapore)
* Spanish (Spain, Latin America)
* French
* German
* Polish
* Danish
* Mandarin (Traditional, Taiwan)
* Cantonese (Traditional, Hong Kong; Simplified)
* Japanese
* Korean
* Vietnamese
* Thai
* Hindi

More languages will be added in the future.

## 8. **Can I collaborate with my team members? What are the differences between Team and Personal plans? How many accounts does my team need?**

Yes. By upgrading to the Team plan, you can invite your team members to your workspace.
Team members can view all shared meetings in the workspace and co-edit meeting notes.

In addition, the Team plan provides:

* More transcription hours
* The ability to run up to 3 meetings simultaneously

We recommend subscribing to as many accounts as the number of members who need to record meetings.
For full team adoption of SeaMeet, please **contact us**.

## 9. **What is a workspace?**

A workspace is where you manage all your meetings, team members, and subscription plans.

### **9-1. How do I manage meetings in a workspace?**

All transcribed meeting notes are stored in the workspace. You can manage them whether they are upcoming, ongoing, or completed.

### **9-2. How do I collaborate in a workspace with my team?**

You can invite team members to join the workspace to view and edit meeting notes together. You can also set different permissions for better workspace management.

### **9-3. How do I choose a plan?**

If you need more transcription hours or advanced features, you can **upgrade your plan** or **contact our support team \<email: [seameet@seasalt.ai](mailto:seameet@seasalt.ai)>** for assistance.

## 10. **How do I log in to SeaMeet?**

You can log in using your Google or Microsoft account, or register with an email address.

## 11. **Do you support Google Education accounts?**

Yes, SeaMeet supports Google Education accounts.

However, due to Google’s restrictions, you cannot directly invite the SeaMeet bot to a meeting initiated by an Education account.
To enable this feature, please email [seameet@seasalt.ai](mailto:seameet@seasalt.ai), and we will help activate your account so the bot can join your future meetings.

## 12. **Can I edit transcripts that have already been recorded?**

You can export transcripts to Google Docs for editing. Editing directly within the SeaMeet meeting page is not yet supported.

## 13. **If I have multiple workspaces, can I store meetings separately? Can I switch languages?**

For meetings scheduled in Google Calendar, the storage location and language depend on your **Account → Meeting Preference** (default language and workspace).

If using the Chrome extension to invite the bot, you can specify which workspace to store the meeting in.

## 14. **Why does SeaMeet Copilot still join meetings even after I disable auto-join?**

First, disconnect your Google Calendar to stop synchronization.
Go to **Account Settings → Integrations** and remove the Google Calendar connection.

For meetings scheduled before the disconnection, manually delete them from the meeting list:
Go to **Meeting List**, find the future meeting with a light-blue background, and click the trash icon to delete.

## 15. **As a subscriber, can I re-invite Copilot if it leaves a meeting?**

Yes. You can re-invite Copilot by going to your meeting list and clicking **Start New Recording**.

## 16. **If I use a non-subscriber account to host a meeting, can subscribers still view the meeting notes?**

Yes. If a subscriber invites Copilot to the meeting, they can view the meeting notes.
Subscribers can also enable **Auto Sharing** to share notes with all invited participants:
Go to **General → Auto Share → All participants in calendar event (recommended)**.

For details, see our [guide](https://wiki.seasalt.ai/en/seameet/sharing/).

## 17. **If a subscriber attends a meeting hosted by another user, can they still receive the meeting notes?**

* If the subscriber invited Copilot → They will receive notes.
* If they did not invite Copilot → They will not receive notes, unless the host enabled Auto Sharing.

## 18. **Where can I see the emails set for auto-sharing?**

Go to **Workspace → General → Auto Sharing** to view the list of auto-share emails.

## 19. **Do I need to confirm invitation emails for Copilot to join meetings?**

No. As long as Copilot is invited and you have enough transcription minutes, it will automatically join.

## 20. **Do I have to use Google Calendar to invite Copilot?**

No. SeaMeet provides multiple ways to invite Copilot. See our [guide](https://wiki.seasalt.ai/seameet/seameet-manual/01-seameet-intro/) for more details.

## 21. **Can Copilot join multiple meetings simultaneously for subscribers?**

Only Team plan users can run multiple concurrent meetings. Individual plan users can only host one meeting at a time.

## 22. **How long are meetings stored in the meeting list? Can I see which one lasted the longest?**

Currently, meetings do not expire. You can view each meeting’s duration in the meeting list.

## 23. **What happens when I exceed my included meeting hours? Will I be notified?**

Once you exceed your plan’s hours, you’ll be charged \$1 per additional hour.
You can check your remaining and used minutes at the bottom of the sidebar anytime.

## 24. **Will Copilot stop recording when my included hours are used up?**

Only in two cases:

1. Free plan users exceed 6 total hours.
2. A single meeting exceeds time limits (1 hour for Free, 5 hours for paid plans).

## 25. **What if my meeting uses multiple languages, e.g., English and Chinese?**

We recommend setting the meeting language to the primary language.
If switching languages mid-meeting, adjust settings accordingly to ensure both are captured.

## 26. **Can I use SeaMeet to record meeting video?**

No. SeaMeet currently only supports transcription and audio recording, not video.

## 27. **Can I download recordings or export data from SeaMeet?**

* Only **Individual** and **Team** users can download audio. Free users can only listen on the platform.
* SeaMeet integrates with Google Drive, where all meeting records can be stored, owned, and shared by you.

## 28. **If the bot leaves a meeting, how do I re-invite it on mobile?**

Two scenarios:

1. **Meeting not previously recorded**: Invite `meet@seasalt.ai` via Google Calendar.
2. **Meeting already recorded**: Log in to SeaMeet → Meeting List → Start Meeting → Paste Google Meet ID.

⚠️ *Important*: Ensure the previous recording has fully ended before re-inviting.

## 29. **How do I ensure auto-join uses Team plan hours instead of Personal?**

SeaMeet determines billing based on the **workspace where the meeting is stored**.
To use Team hours, set the Team workspace as the default:
**Account → Meeting Preference → Default Workspace**

## 30. **What are the main differences between Team and Individual plans?**

1. Team plan allows multiple users to access transcripts, download audio, and export to Google Docs.
2. Team plan allows multiple concurrent Copilot sessions; Individual only allows one at a time.

## 31. **Why wasn’t my meeting fully recorded?**

Possible reasons:

* Bot was not admitted by the host
* Bot was removed during the meeting
* Recording or transcript processing failed

If the bot stayed throughout but data is missing, please email [seameet@seasalt.ai](mailto:seameet@seasalt.ai) with the meeting link.

## 32. **Why can’t the bot join and keeps spinning?**

Check if the host received the bot’s join request.
If not, verify in the SeaMeet meeting list whether the meeting was created successfully.

## 33. **Why does my meeting audio show “file not found”?**

Audio may still be processing within 5 minutes after the meeting ends.
If not available after 10 minutes, email [seameet@seasalt.ai](mailto:seameet@seasalt.ai) with the meeting link.

## 34. **How is recording time calculated?**

Time is only counted when the bot successfully joins the meeting.
Calendar-linked auto-join attempts do not consume minutes unless admitted.

Usage resets monthly for paid plans.

## 35. **Can non-hosts invite SeaMeet to record a meeting?**

Yes, but the host must admit the bot.
The bot will retry joining every 1–2 minutes until admitted.

If the host is also a SeaMeet user, they can invite using their account.

## 36. **What if I exceed the included plan hours?**

You can continue recording, but additional charges apply (see pricing chart).

## 37. **Why do meeting summary emails now link to SeaMeet instead of Google Docs?**

* Workspace users → redirected to SeaMeet meeting page
* Non-workspace users → redirected to a share-only page (view-only)
* Unauthorized users → blocked view (masked content)

This ensures both convenience and security.

## 38. **Where can I manage sharing permissions for meeting notes?**

Each meeting has its own **share list**.
Click the **Share** button on the meeting page to manage or approve viewer access.

If “Share with calendar attendees” is enabled, attendees are auto-added.

## 39. **How do I subscribe to an annual plan?**

Annual subscription is under development.
For now, contact [seameet@seasalt.ai](mailto:seameet@seasalt.ai) for manual setup.

## 40. **Why does my subscription cycle end this month? Why isn’t it \$9.99 flat?**

Subscriptions run from the 1st to the end of each month.
Mid-month signups are prorated. (e.g., signup on 4/20 → pay 1/3 of \$9.99).

## 41. **Does adding admins or members increase costs?**

Yes. Each additional Team user seat incurs extra charges, billed the following month.

## 42. **Why can’t I remove my credit card directly?**

To prevent unpaid balances (usage, added seats), card removal isn’t allowed while subscribed.
When unsubscribed, we can assist with card removal manually.

Annual plans are available with one-time payments (wire transfer possible).

## 43. **Can SeaMeet improve recognition of industry-specific terms?**

Yes. Please provide a glossary of commonly misrecognized terms for correction.

## 44. **How can I change my password?**

Currently, login is via Google, Microsoft, or OTP.
Password login is only for project clients and not user-editable.

## 45. **Can I delete my account or workspace?**

Direct deletion is not available.
You can unlink Google Calendar to stop auto-join.

If you need deletion, email [seameet@seasalt.ai](mailto:seameet@seasalt.ai). ⚠️ Once deleted, workspaces cannot be restored.

## 46. **Is SeaMeet secure?**

Yes. Security is our top priority.

* See our [Terms of Service](https://seasalt.ai/terms/) and [Privacy Policy](https://seasalt.ai/privacy).
* Web Application Firewall via Azure & AWS.
* FIPS-compliant encryption.
* CASA Level 2 security, Nessus scans, HECVAT certification, U.S. data residency.

## 47. **Can the bot auto-join meetings without host approval?**

No. Due to security concerns, host approval is always required.

See [documentation](https://wiki.seasalt.ai/en/seameet/audio-upload/).

## 48. **Can I change the bot’s nickname?**

Not at this time.

## 49. **Can I disable the bot from speaking in meetings?**

No. This is restricted by security policy.

## 50. **How do I disable the SeaMeet pop-up window in Google Meet?**

The pop-up is part of the Chrome extension.
Click the extension icon (top-right) → Manage Extensions.
