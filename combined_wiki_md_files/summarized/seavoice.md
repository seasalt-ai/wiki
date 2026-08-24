# Seavoice Documentation (Merged Summary)

*Merged and condensed from all language versions — combined_wiki_md_files/seavoice_en.md, seavoice_zh-TW.md. English is far more complete: Chinese only covers the STT decoder and TTS customization tutorials (both also present in English), and is missing the entire Discord bot section and the STT customization tutorial.*

## What is SeaVoice?

SeaVoice is Seasalt.ai's AI speech-to-text (STT) and text-to-speech (TTS) technology, offered publicly today as a **Discord bot**. It's built on Seasalt.ai's own deep-learning speech models (in-house English and Mandarin-Taiwan models; other languages use a tuned multilingual open-source base model).

- Homepage: https://suite.seasalt.ai/voice/discord
- Invite link: https://discord.com/api/oauth2/authorize?client_id=1001955060210749492&permissions=2184436736&scope=bot%20applications.commands
- Demo video: https://www.youtube.com/embed/drOVk_bexFY

## Why SeaVoice

Discord voice channels have no permanent log — SeaVoice fixes this by transcribing voice channels live to a text channel, and DMs the session creator a final transcript + audio recording afterward. Benefits: accessibility, searchability, shareability of voice conversations, and TTS lets non-speaking users participate.

Differentiators: in-house deep learning models (not third-party), real-time speed, downloadable transcripts (with timestamps, usable as subtitles).

## Commands

### Speech-to-Text
- `/recognize [language]` — bot joins your current voice channel, transcribes everyone live to the text channel where the command was run. On session end, DMs the creator a transcript file, an SRT subtitle file, and an audio download link (link expires after 24h). Session ends automatically if everyone leaves the channel or the bot restarts.
- `/stop` — bot stops listening, leaves the channel, and DMs the final transcript/audio.
- Tips: use the voice channel's own chat panel to see transcripts side-by-side with participants; make a dedicated low-notification channel for transcripts; right-click the bot → "Deafen Server" to pause listening without ending the session.

### Text-to-Speech
- `/speak [voice] [text]` — synthesizes text as audio into the voice channel you're in. Reacts with 🏁 when done. Default voice is `Orca` unless you set a personal default via `/user_config`.
- Available voices:

| Name | Sex | Language |
|---|---|---|
| Orca | M | American English |
| Narwhal | M | British English |
| Angelfish | F | American English |
| Starfish | F | Mandarin (Taiwan) |
| Dolphin | F | Mandarin (Taiwan) |

### Settings
- `/server_config` (admin only) — configure per-server behavior:
  - `live_transcript`: enabled (default) / disabled
  - `transcript_recipients`: session_creator (default) / participants / this channel / nobody
  - `transcript_style`: plaintext (default) / fancy (embed card)
  - `ignore_bots`: ignore (default) / include
  - `censor`: disabled (default) / enabled (asterisks out profanity/slurs; can't detect euphemisms)
- `/user_config` — personal settings, persist across servers:
  - `exclude_stt`: include (default) / exclude (opt out of being transcribed)
  - `default_tts_voice`: sets your default `/speak` voice (default `Orca`)
- `/server_status`, `/user_status` — show current server/user configuration.

## Language Support

12 languages supported. English and Mandarin (Taiwan) are Seasalt.ai's own from-scratch models (most accurate). All others run on a tuned multilingual open-source base model, which can occasionally "hallucinate" (insert unsaid words, mis-detect language, or translate instead of transcribe):

English, Mandarin (Taiwan), Spanish, Italian, Portuguese, German, Japanese, Korean, Russian, Hindi, Vietnamese, French.

## Community & Support

- Official Discord server (widget id 919037515514654721)
- Vote/review on Top.gg: https://top.gg/bot/1001955060210749492
- Patreon support: https://www.patreon.com/bePatron?u=88101525 — bot core functionality stays free; premium tiers planned.

## Other Resources (see full doc for details)

- **TTS Customization Panel tutorial** (EN + ZH-TW) — web UI for fine-grained control of pronunciation, formatting, pacing, and emphasis, with walkthrough demo videos.
- **STT Decoder** (EN + ZH-TW) — GPU-accelerated decoder benchmarked against Microsoft Azure STT on Real Time Factor (RTFx) and Word Error Rate (WER), showing better speed and accuracy.
- **STT Customization Panel tutorial** (EN only) — web UI to tune the STT engine for domain-specific jargon and ambiguous pronunciations.
