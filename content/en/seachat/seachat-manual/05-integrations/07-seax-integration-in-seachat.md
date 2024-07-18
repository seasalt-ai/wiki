---
title: "SeaX Messaging Integration"
description: ""
date: 2024-07-16T08:48:57+00:00
lastmod: 2024-07-16T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /en/seachat/seachat-integrations/seax-integration-in-seachat/
  - /seachat/seachat-integrations/seax-integration-in-seachat/
  - /seachat/seachat-integrations/07-seax-integration-in-seachat/
weight: 60
toc: true
---

## Overview

In this tutorial, we will guide you through setting up SeaSalt's bulk-messaging platform, SeaX, in SeaChat. SeaX is a powerful omni-channel platform that enables you to manage all your business channels from a single interface.

For more information, check out our [SeaX Messaging Documentation](https://wiki.seasalt.ai/seax/seax_messaging/bulk-messaging-features/).

With SeaX integrated into SeaChat, you can not only manually manage customer conversations but also automate responses with your SeaChat AI agent. SeaX consolidates all your business channels, such as WhatsApp, phone calls, and SMS, allowing these channels to be directed to SeaChat for AI-driven responses.

## SeaX Bulk Messaging

SeaX Messaging provides a channel for your AI agents to communicate with customers. Once SeaX is integrated with SeaChat, you can start sending bulk messages to your customers via SeaX Messaging.

You can create **Campaigns** to send SMS messages or voice drops to your customers. These campaigns will be delivered through SeaX Messaging, and then handled by your personalized AI agent on SeaChat.

## Outbound Calls Integration

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/call-integration.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/call-integration.png" alt="Outbound/ Inbound Calls Integration">
    </a>
<br/>
    <p style="font-size: 15px">Outbound/Inbound Calls Integration</p>
</div>
</div>

Outbound calls is an effective way to reach out to your customers. With SeaX, you can automate these calls.

1. **Languages**: Choose the language and the model it is available in. We recommend using SeaVoice for its stability and reliability in production.

2. **Text-to-Speech Voice**: Select a preferred voice and click the play button next to the dropdown to hear it.

3. **Outbound Starting Messages**: This message will be played when the call is answered, with the AI agent handling the rest of the conversation. You can view the conversation in the **Conversations** dashboard.

## Inbound Calls Integration

Inbound calls offer a reliable solution for customer service. AI agents can answer calls and act as voice receptionists.

Follow the same steps as the [Outbound Calls Integration](#outbound-calls-integration) to set up language, voice, and greeting messages.

## SMS Integration

SMS is an effective tool for text marketing. Starting or receiving an SMS conversation is simple. Just set up the starting messages and let the AI agent take care of the rest.

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/sms.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/sms.png" alt="SMS Setup">
    </a>
<br/>
    <p style="font-size: 15px">SMS Setup</p>
</div>
</div>

## Test It Out

With SeaX set up in SeaChat, you can test the integration by sending a message to your SeaChat AI agent. Before sending bulk messages to your customers via SeaX Messaging, we recommend testing locally by using the designated buttons on each page.

Once you have completed the testing, you can begin sending bulk messages to your customers through SeaX Messaging and let your SeaChat agent continue the conversation.

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/find-seax.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/find-seax.png" alt="SeaX Messages in SeaChat">
    </a>
<br/>
    <p style="font-size: 15px">SeaX Messages in SeaChat</p>
</div>
</div>
