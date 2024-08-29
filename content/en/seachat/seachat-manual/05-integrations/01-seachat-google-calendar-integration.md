---
title: "Google Calendar"
description: "Book appointments seamlessly with SeaChat and sync them to your Google Calendar for effortless scheduling. Learn how to integrate SeaChat's AI chat and voice agent with Google Calendar for efficient appointment management."
date: 2024-03-19T08:48:57+00:00
lastmod: 2024-08-28T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
   - /en/seachat/seachat-integrations/google-calendar/
weight: 10
toc: true
---

## Overview
> After logging into SeaChat, navigate to **Agent Configuration** -> **Integrations** -> **Google Calendar** to add the integration.

## Google Calendar Integration

<br/>
<center>
  <a href="/images/seachat-integrations/google-calendar/en/google-calendar-ui.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/google-calendar/en/google-calendar-ui.png" alt="">
</a>

*Google Calendar Integration Interface*
</center>

With the Google Calendar integration, your SeaChat agent can book appointments for you through chat or voice interactions. The process is simple and involves just two steps. Follow the on-screen instructions to integrate SeaChat with your Google Calendar.

First, authorize SeaChat to connect to your Google Calendar. Next, set up your working hours so the SeaChat agent knows when to schedule appointments.

## Meeting Invitation

Once the integration is complete, your SeaChat agent will be able to book appointments on your behalf. The agent will send a meeting invitation to the user and automatically add the event to your Google Calendar. The customer will receive the meeting invitation directly from the agent.

However, the format of the meeting invitation varies depending on the type of agent used:

- **For Voice Agent**: An SMS containing the calendar link will be sent to the customer's phone number. Please note that since the invitation is not sent via email, the customer may forget about the meeting. It’s advisable to follow up with a call to remind them.

- **For Chat Agent**: Ensure that email collection is enabled in SeaChat by navigating to **Channels** → **Webchat Widget** → **Custom Forms**. Either add a new form or edit the existing one, making sure the **Email** field is both **Required** and **Enabled**. If a meeting is booked, a calendar invitation will be sent to the collected email address.

### Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 
 