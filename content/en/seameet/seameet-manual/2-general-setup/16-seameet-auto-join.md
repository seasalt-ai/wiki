---
title: "Auto Join Meetings"
description: ""
date: 2024-04-18T08:48:57+00:00
lastmod: 2024-08-01T08:48:57+00:00
draft: false
images: []
aliases:
  - /en/seameet/16-seameet-auto-join/
weight: 22
toc: true
---

Let SeaMeet automatically join your meetings without the need to manually enter the meeting ID and start a new meeting record. You can enable the auto-join feature in SeaMeet settings, and it will automatically join at the start of the meeting.

## Sync with Google Calendar
1. Go to the SeaMeet settings page, click **Integration**, and connect SeaMeet to the Google account you want.

<br/>

<center>

<a name="seameet-third-party-integration" href="/images/seameet-en/16-seameet-auto-join/seameet-third-party-integration.png" target="_blank">

<img style="width: 80%" src="/images/seameet-en/16-seameet-auto-join/seameet-third-party-integration.png" alt="Seameet Third-Party Integration"/>

</a>


*1. SeaMeet Interface – Integration*

</center>

2. Go to the **Meeting Preference** page, click **Auto-join Meetings**, enable auto join meetings, and select **All Meetings in My Calendar**.

<br/>

<center>

<a name="seameet-select-all-meetings-in-my-calendar" href="/images/seameet-en/16-seameet-auto-join/seameet-select-all-meetings-in-my-calendar.png" target="_blank">

<img style="width: 80%" src="/images/seameet-en/16-seameet-auto-join/seameet-select-all-meetings-in-my-calendar.png" alt="Seameet Select All Meetings in My Calendar"/>

</a>


*2. SeaMeet Interface – Select All Meetings in My Calendar*

</center>

## Google Calendar Settings

When scheduling a new meeting in Google Calendar, make sure to click add a video meeting, so that there is a video meeting link, and SeaMeet can correctly add the meeting to the list. Meetings without video meeting links will not be automatically joined by SeaMeet.

After completing the above steps, your Google Calendar will automatically be added to the SeaMeet meeting list, and it will automatically join at the start of the meeting.

[//]: # (<br/>)

[//]: # (<center>)

[//]: # (<a name="seameet-select-all-meetings-in-my-calendar" href="/images/seameet-en/16-seameet-auto-join/google-calendar-settings.png" target="_blank">)

[//]: # (<img src="/images/seameet-en/16-seameet-auto-join/google-calendar-settings.png" alt="Google Calendar Settings"/>)

[//]: # (</a>)

[//]: # ()
[//]: # (*Add Video Meeting*)

[//]: # (</center>)

## View Scheduled Meetings List

After enabling the auto-join meetings feature, you can find the added meetings in the meetings list. When the meeting starts, SeaMeet will automatically join and start recording.

<br/>

<center>

<a name="seameet-select-all-meetings-in-my-calendar" href="/images/seameet-en/16-seameet-auto-join/seameet-auto-join-new-meeting.png" target="_blank">

<img src="/images/seameet-en/16-seameet-auto-join/seameet-auto-join-new-meeting.png" alt="Seameet Auto Join New Meeting"/>

</a>


*View All Scheduled Meetings in the Meetings List*

</center>

## Disable Auto-join

First, please disconnect your Google Calendar in order to stop SeaMeet Copilot from synchronizing with your Google Calendar. Go to **Account** -> **Integration** to disconnect Google Calendar.

After disconnecting, if SeaMeet Copilot still joins the meeting automatically, it is because the meeting was scheduled before the disconnection. In this case, you can manually remove the meeting from your meeting list. Go to Meeting List and find the future meetings with the turquoise background. Simply click on the trash can icon to delete the meeting.


## Need Help?

Need help? Feel free to contact us at [seameet@seasalt.ai](mailto:seameet@seasalt.ai).
