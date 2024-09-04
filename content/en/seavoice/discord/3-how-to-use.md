---
title : "How to Use"
description: "SeaVoice cutting edge artificial intelligence text to speech and speech to text Discord bot documentation."
lead: ""
date: 2024-02-14T23:19:57+00:00
lastmod: 2023-02-3T23:19:57+00:00
weight: 20
draft: false
images: []
menu:
    seax:
        parent: "discord"
toc: true
---

## ✍️ Speech-to-Text
#### Transcribe Audio from Discord Voice Channels

##### /recognize [language]

`/recognize [language]` -> Bot joins the voice channel you're currently in, and continues to listen and output transcription in real time to the chat channel. The bot will record and transcribe everyone in the voice channel. Transcriptions are output to the text channel where the initial slash command was entered. When the session ends, the bot will DM the session creator a final transcription file, an SRT-formatted transcript file (used for subtitles), and a link to a full audio download. The session will automatically wrap up if all the users leave the voice channel, or if the bot shuts down or restarts for any reason (such as when a new version gets released).


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

#### Stop Transcription
##### /stop

`/stop` -> Bot stops listening and leaves the voice channel. Upon running the stop command, the session creator will receive a DM with the full transcription and audio files.

## 🗣 Text-to-Speech
#### Synthesize Speech from Chat to Voice Channel 

Seasalt.ai also excels at speech synthesis. We offer a text-to-speech command, which allows users to type in a chat channel and have audio synthesized and played in a particular voice channel for them.

##### /speak [voice] [text]
To use this command, you should already be in a voice channel. In any text channel, type the `/speak` slash command and then optionally specify which `voice` you would like to use, and enter the `text` that you would like synthesized. When the TTS is done speaking, a 🏁 reaction will be applied to the command message. The default voice if not specified is `Orca`, you can also set your own default voice using the `/user_config` command. You can see the available voices below:

| Name      | Sex | Language          |
| --------- | --- | ----------------- |
| Orca      | M   | American English  |
| Narwhal   | M   | British English   |
| Angelfish | F   | American English  |
| Starfish  | F   | Mandarin (Taiwan) |
| Dolphin   | F   | Mandarin (Taiwan) |

## 🎙️ Record & Download
#### Export Audio & Transcriptions from Voice Channels
Users are able to download their transcriptions and full audio recordings to a file.

When the STT session ends the bot will a final transcription file, an SRT-formatted transcript file (used for subtitles), and a link to a full audio download. To download the audio, follow the link and then right click in the web browser and select "Save as...". Download links will expire after 24 hours - so if you want to a permanent copy of your file, download it to your computer.

<center>
<img src="/images/discord/seavoice-discord-bot-stt-download-message.png" alt="SeaVoice STT Discord bot sends users a message with audio and transcription download links.">
</center>

