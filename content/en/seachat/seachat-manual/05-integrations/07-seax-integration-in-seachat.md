---
title: "SeaX Integration"
description: "Integrate SeaX with SeaChat for bulk messaging and automated call handling. Automate customer communications with AI."
date: 2024-07-16T08:48:57+00:00
lastmod: 2024-07-16T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-integrations"
aliases:
  - /seachat/seachat-manual/05-integrations/07-seax-integration-in-seachat/
  - /en/seachat/seachat-integrations/seax-integration-in-seachat/
  - /seachat/seachat-integrations/seax-integration-in-seachat/
  - /seachat/seachat-integrations/07-seax-integration-in-seachat/
weight: 60
toc: true
---

## Overview

In this tutorial, we will guide you through setting up Seasalt's bulk-messaging platform, SeaX, in SeaChat. SeaX is a powerful omni-channel platform that enables you to manage all your business channels from a single interface.

For more information, check out our [SeaX Documentation](https://wiki.seasalt.ai/seax/seax_messaging/bulk-messaging-features/).

With SeaX integrated into SeaChat, you can not only manually manage customer conversations but also automate responses with your SeaChat AI agent. SeaX consolidates all your business channels, such as WhatsApp, phone calls, and SMS, allowing these channels to be directed to SeaChat for AI-driven responses.

## SeaX Bulk Call/Send

SeaX provides a channel for your AI agents to communicate with customers. Once SeaX is integrated with SeaChat, you can start sending bulk messages to your customers via SeaX. 

SeaChat and SeaX work seamlessly with each other to perform the bulk messaging. SeaX will start calling each customer on the given list about 1 second per call. Once the call is answered, the AI agent will take over the conversation, and all you have to do now is go to the **Conversations** dashboard to view the conversation.

SeaChat does not know the list of the customers you are calling, and neither is it capable of making calls. SeaChat only handles the conversation once conversation is initiated. On the other hand, SeaX is responsible for initiating the calls and sending the messages. 

You can create **Campaigns** to send SMS messages or voice drops to your customers. These campaigns will be delivered through SeaX, and then handled by your personalized AI agent on SeaChat.

## Outbound Call Campaign

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

With SeaX set up in SeaChat, you can test the integration by sending a message to your SeaChat AI agent. Before sending bulk messages to your customers via SeaX, we recommend testing locally by using the designated buttons on each page.

Once you have completed the testing, you can begin sending bulk messages to your customers through SeaX and let your SeaChat agent continue the conversation.

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/find-seax.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/find-seax.png" alt="SeaX Messages in SeaChat">
    </a>
<br/>
    <p style="font-size: 15px">SeaX Messages in SeaChat</p>
</div>
</div>

## :dart: Troubleshooting

1. **No phone available for inbound calls and inbound SMS. How can I configure my phone correctly?**

<div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <a href="/images/seachat-integrations/seax/no-phone-available.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/no-phone-available.png" alt="No Phone Available Warning">
    </a>
<br/>
    <p style="font-size: 15px;">No Phone Available Warning</p>
</div>
</div>

When the system displays the above warning, it means you need to provide a phone number to the AI agent so that the agent can use it as the channel to manage incoming calls and SMS messages. If someone calls this number or sends an SMS, the AI agent will handle the conversation.

To provide this number, you need to configure SeaX and send an outbound call or SMS to the SeaChat agent first. Please follow the [SeaX Documentation](https://wiki.seasalt.ai/seax/seax_messaging/bulk-messaging-features/) for instructions on how to send an SMS or make a call to the agent.

Specifically:

1. SeaX -> Outbound calls to agent -> Configure agent inbound call number
2. SeaX -> Outbound SMS to agent -> Configure agent inbound SMS number

If you are unsure whether the agent has received the call or SMS, you can check the conversation in the **Conversations** dashboard.
