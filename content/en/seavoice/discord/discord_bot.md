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

   <iframe width="100%" height="10%" src="https://www.youtube.com/embed/00DoeiS3l1Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

SeaVoice is a voice intelligence bot that uses advanced AI technology to improve the Discord voice channel experience. One of the great things about Discord’s text channels is that they maintain a permanent log of the server’s conversations. But what about the voice channels? Once something is said verbally in the channel, *it’s gone* - you can’t catch up on part of the conversation you missed or search the conversation later. 

Invite SeaVoice to the voice channel, and you can get real time speech transcriptions delivered to a chat channel as the conversation is happening. You'll also receive a final version of your transcript and voice recording in a DM after the session ends. SeaVoice is set apart from bots offering similar services because it’s backed by state-of-the-art deep learning models crafted by Seasalt.ai.

We feel that providing highly accurate transcriptions for voice channels is a huge accessibility improvement for Discord. Additionally, because transcriptions are automatically posted to a text channel, that means they are permanent, searchable, and shareable. Similarly, speech synthesis also boosts participation in voice channels by making them more accessible to people who can’t or don’t want to speak personally.

## Capabilities

### ✍️ Speech-to-Text
##### Transcribe Audio from Voice Channels

###### /recognize

`/recognize` -> Bot joins the voice channel you're currently in, and continues to listen and output transcription in real time to the chat channel. The bot will record and transcribe everyone in the voice channel. Transcriptions are output to the text channel where the initial slash command was entered. When the session ends, the bot will DM each participant a final transcription file and a link to a full audio download.

<p style="color:#19b6c0">Pro Tip:</p>

Use the `/recognize` command from the voice channel chat window to see your transcriptions side-by-side with the participants or live stream!

<center>
<img src="/images/discord/voice-chat-side-by-side.png"/>
</center>

To open the voice channel chat panel, click the chat icon next to the voice channel name:

<center>
<img width="60%" src="/images/discord/voice-chat-channel.png">
</center>

###### /stop

`/stop` -> Bot stops listening and leaves the voice channel.

### 🗣 Text-to-Speech
#### Synthesize Speech from Chat to Voice Channel 

Seasalt.ai also excels at speech synthesis. We offer a text-to-speech command, which allow users to type in a chat channel and have audio synthesized and played in a particular voice channel for them.

###### /speak [voice] [text]
To use this command, you should already be in a voice channel. In any text channel, type the `/speak` slash command and then specify which `voice` you would like to use, and enter the `text` that you would like synthesized. You can see the available voices below:
| Name      | Sex | Language          |
| --------- | --- | ----------------- |
| Orca      | M   | American English  |
| Narwhal   | M   | British English   |
| Angelfish | F   | American English  |

### 🎙️ Record & Download
#### Export Audio from Voice Channels
Users are able to download their transcriptions and full audio recordings to a file.

If someone uses the `/stop` command while an STT session was in progress, the bot will DM each participant a final transcription file and a link to a full audio download. To download the audio, follow the link and then right click in the web browser and select "Save as...".

<center>
<img width="60%" src="/images/discord/post-stt-direct-message.png">
</center>

In the future we may offer downloads for different file types. Particularly, we plan to offer transcriptions in close-caption format so that they can be aligned with audio or video and used as subtitles.

## Language Support
Currently our text-to-speech and speech-to-text models support English. However, we're always working on creating new language models and improving our existing ones. We have excellent models for Chinese that may be added to the bot soon. We're also working on new models for Vietnamese, Spanish, French, and more! We'd love to hear which languages you're most eager to use.

## Why SeaVoice?

#### 🎯 Cutting-edge Accuracy
Speech techonology is our specialty. We create our own models in-house using state of the art deep learning neural network algorithms.

#### ⏱️ Real-time Transcription and Synthesis
Real-time speed is essential when you're dealing with live conversation. We guarantee you'll never fall behind in a conversation because of slow transcription speeds.

## Add SeaVoice to Your Server

Adding the SeaVoice bot to your server is easy! Simply click the invite link, verify your credentials with Discord, and then choose which server to add the bot to.

<div class="row justify-content-center">
    <div class="col-lg-9 col-xl-8 text-center">
        <p class="lead"></p>
        <a class="btn btn-primary btn-lg px-4 mb-2" href="https://discord.com/api/oauth2/authorize?client_id=1001955060210749492&permissions=2184436736&scope=bot%20applications.commands" role="button">Invite SeaVoice</a>
    </div>
</div>

## Support

Join our official Discord server! We'd love to chat and find out how we can improve our bot. Our bot is in *active development* - please let us know if you find any bugs, have ideas for new features, or want to provide any feedback!

<div class="row justify-content-center">
    <iframe src="https://discordapp.com/widget?id=919037515514654721&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
</div>  

#### Also see our page on Top.gg!

<div class="row justify-content-center">
    <a href="https://top.gg/bot/1001955060210749492">
        <img src="https://top.gg/api/widget/1001955060210749492.svg">
    </a>
</div>