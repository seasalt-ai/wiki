---
title : "Settings"
description: "SeaVoice cutting edge artificial intelligence text to speech and speech to text Discord bot documentation."
lead: ""
date: 2024-02-14T23:19:57+00:00
lastmod: 2023-02-3T23:19:57+00:00
weight: 30
draft: false
images: []
menu:
    seax:
        parent: "discord"
toc: true
---


SeaVoice offers customizable settings for both servers and individual users.

Note: If you update any settings, you must stop and re-start any active `/recognize` sessions before the new configurations are applied.

## 👥 Setting for Everyone in Server

> /server_config [live_transcript] [transcript_recipients] [transcript_style] [ignore_bots] [censor]

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

## 👤 Setting for Just Yourself

> /user_config [exclude_stt] [default_tts_voice]

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

## ⚙️ Server / User Status

### Check Server Status
> /server_status

Run the `/server_status` command to get a break down of your current server configurations.

<center>
<img width="60%" src="/images/discord/seavoice-discord-server-status.png" alt="SeaVoice Discord bot sends user a summary of the server configurations.">
</center>

### Check User Status
> /user_status

Run the `/user_status` command to get a break down of your current user configurations.

<center>
<img width="60%" src="/images/discord/seavoice-discord-user-status.png" alt="SeaVoice Discord bot sends user a summary of the user configurations.">
</center>

