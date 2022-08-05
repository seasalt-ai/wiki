---
title : "SeaVoice Discord Bot"
description: "SeaVoice Discord Bot Documentation"
lead: ""
date: 2022-08-4T23:19:57+00:00
lastmod: 2022-08-4T23:19:57+00:00
weight: 100
draft: false
images: []
menu:
    seax:
        parent: "discord"
toc: true
---

## SeaVoice Bot Introduction

🐙 The SeaVoice Bot is a new Discord integration brought to you by Seasalt.ai, a startup run by some of the world’s leading experts in deep speech recognition, neural speech synthesis, and natural language processing. 🐙

SeaVoice is a voice intelligence bot that uses advanced AI technology to improve the Discord voice channel experience. One of the great things about Discord’s text channels is that they maintain a permanent log of the server’s conversations. But what about the voice channels? Once something is said verbally in the channel, *it’s gone* - you can’t catch up on part of the conversation you missed or search the conversation later. 

Invite SeaVoice to the voice channel, and you can get real time speech transcriptions delivered to a chat channel as the conversation is happening. SeaVoice is set apart from bots offering similar services, because it’s backed by state-of-the-art deep learning models crafted by Seasalt.ai.

We feel that providing highly accurate transcriptions for voice channels is a huge accessibility improvement for Discord. Additionally, because transcriptions are automatically posted to a text channel, that means they are permanent, searchable, and shareable. Similarly, speech synthesis also boosts participation in voice channels by making them more accessible to people who can’t or don’t want to speak personally.

## Capabilities

### ✍️ Speech-to-Text
##### Transcribe Audio from Voice Channels

###### /recognize

`/recognize live: True` -> Bot joins the voice channel you're currently in, and continues to listen and output transcription in real time to the chat channel

`/recognize live: False` -> Bot joins the voice channel you're currently in, listens until talking stops and then outputs one transcription per user

###### /leave

`/leave` -> Bot stops listening and leaves the voice channel

###### Explanation

The transcription service can be started by joining a voice channel and entering the `/recognize` slash command. Transcription has two modes: live and batch. If set to `live: True`, the bot will continuously listen and update transcriptions in the chat channel as conversation participants speak. If set to `live: False` the bot will listen until the channel is silent for 3 seconds, and then output a single transcription in bulk, and leave the channel. You can also use the `/leave` command to have the bot immediately leave the channel and stop listening.

### 🗣 Text-to-Speech
#### Synthesize Speech from Chat to Voice Channel 
<p style="color:red">⚠️ Work in Progress</p>

Seasalt.ai also excels at speech synthesis. We plan to offer text-to-speech commands, which will allow users to type in a chat channel and have audio synthesized and played in a particular voice channel for them. 

To get a sneak peak of some of our sythensized voices (including Tom Hanks, David Attenborough, and Reese Witherspoon), check out our [Text-to-Speech page](https://suite.seasalt.ai/tts).


### 🎙️ Record & Download
#### Export Audio from Voice Channels
<p style="color:red">⚠️ Work in Progress</p>

In the future, users will also be able to download their transcriptions to a file. Additionally we also plan to offer audio recording download so that users can save their full conversations.

## Add SeaVoice to Your Server

Adding the SeaVoice bot to your server is easy! Simply click the invite link, verify your credentials with Discord, and then choose which server to add the bot to.

<div class="row justify-content-center">
    <div class="col-lg-9 col-xl-8 text-center">
        <p class="lead"></p>
        <a class="btn btn-primary btn-lg px-4 mb-2" href="https://discord.com/api/oauth2/authorize?client_id=1001955060210749492&permissions=2184436736&scope=bot%20applications.commands" role="button">Invite SeaVoice</a>
    </div>
</div>

## Support

Join our official Discord server! We'd love to chat and find out how we can improve our bot. Please let us know if you find any bugs or have any ideas for new features!

<div class="row justify-content-center">
    <iframe src="https://discordapp.com/widget?id=919037515514654721&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
</div>