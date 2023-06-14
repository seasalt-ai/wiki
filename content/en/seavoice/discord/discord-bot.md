---
title : "SeaVoice Speech to Text & Text to Speech Discord Bot"
description: "SeaVoice cutting edge artificial intelligence text to speech and speech to text Discord bot documentation"
lead: ""
date: 2022-08-4T23:19:57+00:00
lastmod: 2023-02-3T23:19:57+00:00
weight: 100
draft: false
images: []
menu:
    seax:
        parent: "discord"
toc: true
---

## SeaVoice Bot Introduction

🐙 The SeaVoice Bot is a new speech-to-text and text-to-speech Discord integration brought to you by Seasalt.ai, a startup run by some of the world’s leading experts in deep speech recognition, neural speech synthesis, and natural language processing. 🐙

   <iframe width="100%" height="400" src="https://www.youtube.com/embed/drOVk_bexFY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

SeaVoice is a voice intelligence bot that uses advanced AI technology to improve the Discord voice channel experience. One of the great things about Discord’s text channels is that they maintain a permanent log of the server’s conversations. But what about the voice channels? Once something is said verbally in the channel, *it’s gone* - you can’t catch up on part of the conversation you missed or search the conversation later. 

Invite SeaVoice to the voice channel, and you can get real time speech transcriptions delivered to a chat channel as the conversation is happening. You'll also receive a final version of your transcript and voice recording in a DM after the session ends. SeaVoice is set apart from bots offering similar services because it’s backed by state-of-the-art deep learning models crafted by Seasalt.ai.

We feel that providing highly accurate transcriptions for voice channels is a huge accessibility improvement for Discord. Additionally, because transcriptions are automatically posted to a text channel, that means they are permanent, searchable, and shareable. Similarly, speech synthesis also boosts participation in voice channels by making them more accessible to people who can’t or don’t want to speak personally.

## Capabilities

### ✍️ Speech-to-Text
##### Transcribe Audio from Discord Voice Channels

###### /recognize [language]

`/recognize [language]` -> Bot joins the voice channel you're currently in, and continues to listen and output transcription in real time to the chat channel. The bot will record and transcribe everyone in the voice channel. Transcriptions are output to the text channel where the initial slash command was entered. When the session ends, the bot will DM the session creator a final transcription file, an SRT-formatted transcript file (used for subtitles), and a link to a full audio download. The session will automatically wrap up if all the users leave the voice channel, or if the bot shuts down or restarts for any reason (such as when a new version gets released).

###### Language Support

SeaVoice currently supports 12 languages. The English and Taiwanese Mandarin models are our own in-house models trained from scratch; they are highly accurate and reliable. All other languages are supported using a multilingual open source model as the base. The performance wasn't great out of the box, so we integrated it into our own STT pipeline and tuned the model to improve the performance. One thing you may notice with the open source model is "hallucination". This can manifest in a couple different ways, such as: inserting words/phrases that weren't said, transcribing in the wrong language, and/or translating the spoken language to a different language.

| Language          |
| ----------------- |
| English           |
| Mandarin (Taiwan) |
| Spanish           |
| Italian           |
| Portuguese        |
| German            |
| Japanese          |
| Korean            |
| Russian           |
| Hindi             |
| Vietnamese        |
| French            |

<p style="color:#19b6c0">Pro Tip #1:</p>

Use the `/recognize [language]` command from the voice channel chat window to see your transcriptions side-by-side with the participants or live stream!

<center>
<img src="/images/discord/discord-voice-chat-stt-side-by-side.png" alt="Use SeaVoice Discord bot in a Discord voice chat channel to see live STT transcriptions side-by-side with participants."/>
</center>

To open the voice channel chat panel, click the chat icon next to the voice channel name:

<center>
<img width="60%" src="/images/discord/discord-voice-chat-channel.png" alt="How to open a Discord voice chat channel to start SeaVoice STT.">
</center>

<p style="color:#19b6c0">Pro Tip #2:</p>

To avoid excessive notifications from live transcriptions, create a separate channel just for transcriptions and set the notification settings lower.

<center>
<img width="100%" src="/images/discord/seavoice-discord-transcription-channel.png" alt="Set up a separate text channel just for live transcriptions from SeaVoice STT.">
</center>

<p style="color:#19b6c0">Pro Tip #3:</p>

If you want to temporarily stop the bot from listening to you (like pausing the session), you can right-click on the bot in the voice channel and check `Deafen Server`. This will prevent any audio data from being sent to the bot until it is un-checked. This way, you can pause the transcription and then pick your session back up when you're ready without having to stop and start a new one!

<center>
<img width="60%" src="/images/discord/deafen-seavoice-stt-discord-bot.JPG" alt="Deafen the SeaVoice STT Discord bot to pause the live transcription.">
</center>

###### /stop

`/stop` -> Bot stops listening and leaves the voice channel. Upon running the stop command, the session creator will receive a DM with the full transcription and audio files.

### 🗣 Text-to-Speech
#### Synthesize Speech from Chat to Voice Channel 

Seasalt.ai also excels at speech synthesis. We offer a text-to-speech command, which allows users to type in a chat channel and have audio synthesized and played in a particular voice channel for them.

###### /speak [voice] [text]
To use this command, you should already be in a voice channel. In any text channel, type the `/speak` slash command and then optionally specify which `voice` you would like to use, and enter the `text` that you would like synthesized. When the TTS is done speaking, a 🏁 reaction will be applied to the command message. The default voice if not specified is `Orca`, you can also set your own default voice using the `/user_config` command. You can see the available voices below:

| Name      | Sex | Language          |
| --------- | --- | ----------------- |
| Orca      | M   | American English  |
| Narwhal   | M   | British English   |
| Angelfish | F   | American English  |
| Starfish  | F   | Mandarin (Taiwan) |
| Dolphin   | F   | Mandarin (Taiwan) |

### 🎙️ Record & Download
#### Export Audio & Transcriptions from Voice Channels
Users are able to download their transcriptions and full audio recordings to a file.

When the STT session ends the bot will a final transcription file, an SRT-formatted transcript file (used for subtitles), and a link to a full audio download. To download the audio, follow the link and then right click in the web browser and select "Save as...". Download links will expire after 24 hours - so if you want to a permanent copy of your file, download it to your computer.

<center>
<img src="/images/discord/seavoice-discord-bot-stt-download-message.png" alt="SeaVoice STT Discord bot sends users a message with audio and transcription download links.">
</center>

## Configuration

SeaVoice offers customizable settings for both servers and individual users.

Note: If you update any settings, you must stop and re-start any active `/recognize` sessions before the new configurations are applied.

### 👥 Server Settings
#### Configure settings for everyone in the server

###### /server_config [live_transcript] [transcript_recipients] [transcript_style] [ignore_bots] [censor]

Use the `/server_config` command to configure the settings for the *current server* that you are in. *Only users with admin permissions in the server may use this command*.
Servers currently have the following settings:

<p style="color:#19b6c0">[live_transcript]</p>

One of SeaVoice's main features is the ability to produce real-time transcriptions in the text channel.
However, some users are only interested in the *final* transcription files.
By configuring `live_transcript` to `disabled`, you can turn off the live transcriptions and only receive the final transcript files. `live_transcript` is set to `enabled` by default.

| Value        | Description                                             |
| ------------ | ------------------------------------------------------- |
| `enabled`    | Send live transcriptions as messages to the text channel|
| `disabled`   | Do not send any live transcriptions                     |

<p style="color:#19b6c0">[transcript_recipients]</p>

In addition to live transcription, SeaVoice is able to send audio recording and final transcription files.
By default, when the `/recognize` session ends, SeaVoice will send a DM to the session creator (the user who sent the `/recognize` command) with the audio and transcription files.
You can instead configure the bot to send the DM to all participants in the session, a specific text channel, or no one at all.

| Value              | Description                                                        |
| ------------------ | ------------------------------------------------------------------ |
| `session_creator`  | Sends DM only to the user who sent the `/recognize` command        |
| `participants`     | Sends DM to all users who participated in the session              |
| `this channel`     | Sends to the channel where the `/server_config` command was run    |
| `nobody`           | Does not send final message                                        |

<p style="color:#19b6c0">[transcript_style]</p>

The live transcriptions sent by SeaVoice during the `/recognize` session can be styled in two ways. 
By default, they will be sent as regular text messages, which are more condensed on the page but look plain.
You can select the `fancy` setting to have each message sent as an embed/card.
This look nicer and is easier to read, but takes up more space on the page.

| Value       | Description                                        |
| ----------- | -------------------------------------------------- |
| `plaintext` | Sends transcript messages as plain text            |
| `fancy`     | Sends transcript messages as a stylized embed card |

<center>
<img width="60%" src="/images/discord/seavoice-discord-fancy-transcript.png" alt="'Fancy' live transcription style from SeaVoice Discord.">
<img width="60%" src="/images/discord/seavoice-discord-plain-transcript.png" alt="'Plaintext' live transcription style from SeaVoice Discord.">
</center>

<p style="color:#19b6c0">[ignore_bots]</p>

If there are other bots in the voice channel while a `/recognize` session is taking place, it is possible for SeaVoice to try and transcribe them. However, the most common type of bot that participates in the voice channel is a music bot - music in general is not transcribed well and just ends up cluttering the transcription. For this reason, by default the SeaVoice bot will *ignore* other bots. However, if you want SeaVoice to try and transcribe other bots (for example if you use a different text-to-speech bot and want it to show up in the transcript) you can enable SeaVoice to listen to other bots.

| Value       | Description                                        |
| ----------- | -------------------------------------------------- |
| `ignore`    | Do not transcribe other bots                       |
| `include`   | Transcribe other bots in the STT session           |

<p style="color:#19b6c0">[censor]</p>

Some servers may want to avoid nasty language appearing in their channels. The `censor` setting allows you to enable/disable a profanity censor on all transcripts. When `censor` is set to `enabled`, it will replace any swears, slurs, or sexual words with asterisks. By default, the censor is set to `disabled`. Keep in mind that the censor just hides inappropriate words, it can't infer the meaning behind the words - so inappropriate content relayed with normal words will not be censored.

| Value        | Description                                        |
| ------------ | -------------------------------------------------- |
| `enabled`    | Censor all live and final transcripts              |
| `disabled`   | Do not censor any transcriptions                   |

### 👤 User Settings
#### Configure settings for just yourself

###### /user_config [exclude_stt] [default_tts_voice]

Use the `/user_config` command to configure your personal settings for your Discord account. 
These settings will persist no matter which server you are in.
Users currently have the following settings:

<p style="color:#19b6c0">[exclude_stt]</p>

If for any reason you do not want to be included in the live transcription session, you may configure your account to be excluded from all `/recognize` sessions.

| Value       | Description                                                                      |
| ----------- | -------------------------------------------------------------------------------- |
| `include`   | Do not exclude me from STT sessions (I am OK with being recorded)                |
| `exclude`   | *Exclude* me from all STT sessions (I do not want to be transcribed or recorded) |

<p style="color:#19b6c0">[default_tts_voice]</p>

If there's one TTS voice you prefer to use more than the other, you can set it as your default. When you have a default set, you can leave the `voice` parameter of the `/speak` command empty and it will use your default. If you haven't set your own default TTS voice, it will be set to `Orca`.

| Value       | Sex | Language          |
| ----------- | --- | ----------------- |
| `Orca`      | M   | American English  |
| `Narwhal`   | M   | British English   |
| `Angelfish` | F   | American English  |
| `Starfish`  | F   | Mandarin (Taiwan) |
| `Dolphin`   | F   | Mandarin (Taiwan) |

### ⚙️ Server / User Status
#### Check your current server or user configurations

###### /server_status

Run the `/server_status` command to get a break down of your current server configurations.

<center>
<img width="60%" src="/images/discord/seavoice-discord-server-status.png" alt="SeaVoice Discord bot sends user a summary of the server configurations.">
</center>

###### /user_status

Run the `/user_status` command to get a break down of your current user configurations.

<center>
<img width="60%" src="/images/discord/seavoice-discord-user-status.png" alt="SeaVoice Discord bot sends user a summary of the user configurations.">
</center>

## Language Support
Currently our text-to-speech models support English and Mandarin, and our speech-to-text models support an additional 10 languages. However, we're always working on creating new language models and improving our existing ones. We'd love to hear which languages you're most eager to use!

## Why SeaVoice STT & TTS?

#### 🎯 Cutting-edge Accuracy
Speech technology is our specialty. We create our own models in-house using state of the art deep learning neural network algorithms.

#### ⏱️ Real-time Transcription & Synthesis
Real-time speed is essential when you're dealing with live conversation. We guarantee you'll never fall behind in a conversation because of slow transcription speeds.

#### 📂 Downloadable Transcription & Audio Files
Not only can you watch your transcriptions in real-time, but you can download them and save them for future use! Your voice-based conversations just became permanent, searchable, and shareable. Because all our transcriptions come with timestamps, you can even use them as subtitles.

## Add SeaVoice Discord Bot to Your Server

Adding the SeaVoice bot to your server is easy! Simply click the invite link, verify your credentials with Discord, and then choose which server to add the bot to.

<div class="row justify-content-center">
    <div class="col-lg-9 col-xl-8 text-center">
        <p class="lead"></p>
        <a class="btn btn-primary btn-lg px-4 mb-2" href="https://discord.com/api/oauth2/authorize?client_id=1001955060210749492&permissions=2184436736&scope=bot%20applications.commands" role="button">Invite SeaVoice</a>
    </div>
</div>

## Community

### Official Discord Server

Join our official Discord server! We'd love to chat and find out how we can improve our bot. Our bot is in *active development* - please let us know if you find any bugs, have ideas for new features, or want to provide any feedback!

<div class="row justify-content-center">
    <iframe src="https://discordapp.com/widget?id=919037515514654721&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
</div>  

### Also see our page on Top.gg!

Your comments and votes make SeaVoice easier to find for new users!

<a href="https://top.gg/bot/1001955060210749492">
    <img src="https://top.gg/api/widget/1001955060210749492.svg">
</a>

## Support SeaVoice

Love the SeaVoice Bot? Consider becoming a Patron! 
We will be adding Patreon tiers and a premium version of the bot soon - but don't worry, the core functionality of the bot will remain free for everyone!

<a href="https://www.patreon.com/bePatron?u=88101525" data-patreon-widget-type="become-patron-button">Become a Patron!</a>
<script async src="https://c6.patreon.com/becomePatronButton.bundle.js"></script>

