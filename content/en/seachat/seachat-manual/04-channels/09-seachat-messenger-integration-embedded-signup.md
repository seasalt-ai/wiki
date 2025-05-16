---
title: "Facebook Messenger Using Embedded Signup"
description: "Set up a ChatGPT-powered bot on Facebook Messenger. Follow our guide to create a Meta app, configure webhooks, and launch your bot for seamless communication."
date: 2024-04-08T08:48:57+00:00
lastmod: 2024-04-08T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /en/seachat/seachat-manual/04-channels/09-seachat-messenger-integration-embedded-signup/
  - /seachat/seachat-manual/04-channels/09-seachat-messenger-integration-embedded-signup/
url: /en/seachat/manual/channels/facebook-messenger-embedded-signup/
weight: 502
toc: true
---


This guide will walk you through how to connect your Facebook Page to SeaChat using Facebook Embedded Signup.

###  ✨ Why Use Embedded Signup?
Compared to the old method, SeaChat’s Messenger integration with embedded signup is simpler, faster, and more powerful. Here’s why:

✅ Seamless Setup Experience
You no longer need to leave the SeaChat interface or switch tabs. Everything happens within SeaChat — login, permission approval, and Page connection.

✅ No Meta Developer Account Required
With embedded signup, you don’t need to create your own Meta App or go through Meta’s App Review process. We’ve done that for you.

✅ Pass the 24-Hour Rule for Live Agent Support
If your customers need to talk to a real person, SeaChat’s Meta-approved app allows live agent handoff even after the 24-hour window. That’s something most user-created apps can’t do without Meta approval.


### Connect Your Facebook Page with JUST TWO STEPS
Go to the `Messenger With Embedded Signup` card in your SeaChat Channels page.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-1.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

**Step 1: Signin to Facebook and Select Facebook Page**

- Click the Connect button and a Facebook login popup will appear.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

- Login with your Facebook account that manages the Page.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2-1.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

- Select the Page you want to connect and grant all requested permissions. Note that we only support one Page per AI agent. If you want to connect multiple Pages, you need to create a new SeaChat AI agent for each Page.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2-2.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

**Step 2: Choose Channel Specific Language**
Define the language of voice messages so SeaChat can transcribe them to text, and reply in the same language. This also works on system messages (e.g., after user clicks 🧹New Topic)

🚀 You’re All Set!
Once completed, SeaChat will start handling messages via your SeaChat AI agent. You can test it right away by sending a message to your connected Page.

### Already Connected Messenger the Old Way?
If you previously integrated Messenger through our old method, here’s how to switch:
Go to your Messenger Integration page in SeaChat.

- Find the "Messenger Integration(Deprecated)" card.
- Click "Remove" on the upper right norner to remove the old integration.
- Then, go to the new `Messenger With Embedded Signup` card and follow the updated steps to reconnect.

🙋 Need help with the migration? <br/>
📧 Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai). <br/>
🌍 We offer multilingual customer service and are happy to assist!


### Engage with a real human agent
Did you notice in the above picture that I used /live_agent to request a human agent? If an agent happened to be online by setting their online status:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 40%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" alt="SeaChat | Messenger | Live Agent Status">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent status
</p>
</div>
</div>

<br/> 

They can directly talk with the user!

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" alt="SeaChat | Messenger | Live Agent interaction Example">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent interaction
</p>
</div>
</div>

<br/> 

If an agent is not online, they can turn on Email notification to receive real-time emails when a user initiates a chat, or request a live agent:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" alt="SeaChat | Messenger | Live Agent Preference">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent preference
</p>
</div>
</div>

<br/> 



## Respond to Voice Clips
Do you know that SeaChat supports audio messages too? If a user sends a voice clip, SeaChat can transcribe it to text, and respond via text!

Currently, it supports English speech to transcription, but let us know if you want more languages supported.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" alt="SeaChat | Messenger | Messenger Voice Clip">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Facebook Messenger voice clip transcription and response by SeaChat</strong></p>
</div>
</div>

<br/> 

### Button limits on Messenger

After following the above steps, you can now use the button feature on SeaChat integrated with Messenger. However, since we are still using the API provided by Messenger, there are some limitations to keep in mind when creating your buttons to avoid any issues.

The following are the limitations:

- The button template allows up to **3 postback buttons** per message template.
- Each button can have a **payload of up to 1000 characters**, which is sent back to your webhook when clicked.
- The **button title** is limited to **20 characters**.
- These limits apply to each individual button, so you can have 3 buttons per message, each with its own 1000-character payload and 20-character title.
- [Developer Documentation](https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback)

A good solution to reduce the effect of these limitations is to use SeaChat's **[KB ID](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/webpage-link/#kb-ids)** feature. Please check out the link for more information.


## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).
