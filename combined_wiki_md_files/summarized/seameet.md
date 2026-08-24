# Seameet Documentation (Merged Summary)

*Merged and condensed from all language versions — combined_wiki_md_files/seameet_en.md, seameet_zh.md, seameet_zh-TW.md. English and Chinese (zh) cover the same feature set at the same recency; zh-TW is an older snapshot missing some newer features. English also contains ~680 lines of internal drip-campaign marketing material (not product docs), omitted here.*

## What is SeaMeet?

SeaMeet is Seasalt.ai's AI meeting assistant (Copilot) that joins online meetings to produce live transcripts, translation, summaries, action items, and discussion topics, plus post-meeting Email Copilot workflows. Site: https://meet.seasalt.ai/ (also https://seameet.ai/)

## Inviting the Bot to Record

**Google Meet** (3 ways):
1. Install the [SeaMeet Chrome extension](https://chrome.google.com/webstore/detail/seameet-ai-meeting-minute/gkkhkniggakfgioeeclbllpihmipkcmn) (Chrome/Edge/Arc/Brave) and click "Start Transcription" in Meet
2. In the SeaMeet meeting list, click "Start New Meeting Record" and enter the Google Meet code, or paste a meeting link
3. Invite `meet@seasalt.ai` to the meeting via Google Calendar

**Microsoft Teams**: paste a meeting link (supports teams.microsoft.com, launcher, and Google Calendar-copied link formats), or bind Outlook Calendar and enable "Auto Join" for Teams meetings; the bot posts a chat message identifying the inviter, recording language, and viewing link when it joins.

**Audio upload**: upload external recordings from the file list. Supports .mp3/.wav/.aac/.flac/.ogg/.opus/.m4a/.mp4/.webm/.wma/.wmv. Free plan: 5 uploads (first 3 min viewable only); Individual plan: 100/month; Team plan: 200/month.

**Auto-join**: link your Google or Outlook account under Third-Party Integrations, then enable "Auto Join" + "All meetings on my calendar" in Meeting Settings. New Google Calendar events must include a video-conference link to be picked up. To disable, unlink the calendar first (already-scheduled meetings must be deleted manually from the meeting list).

## Live Translation

Requires a Google account + Chromium-based browser. After installing the extension, click "Start Recording" in the Meet widget; the host must approve the bot. In the widget's "Transcription & Translation" tab:
- **Standard translation**: pick up to 2 formal languages for live parallel translation — English, Spanish (Spain/LatAm), French, German, Danish, Polish, Thai, Hindi, Vietnamese, Korean, Japanese, Malay, Filipino, Cantonese (Simplified/HK Traditional), Mandarin (Taiwan/Simplified), Arabic, Farsi
- **"Third track" fun translation**: an extra playful track — Klingon, Dothraki, Elvish, Minionese, Morse Code, Emoji-only, UwU speak, Doggo speak, Shakespearean English, Pirate Speak, Yoda Speak, Spanglish/Chinglish/Singlish, Shorthand/Texting, etc.
- After the meeting, view the full transcript, summary, action items, and all translation tracks in the workspace

## Email Copilot

After a meeting, Copilot emails a summary + action items with a "Reply" prompt. Instead of copy-pasting a transcript into a separate LLM tool, just reply in the email thread with natural-language requests — e.g. "draft a customer follow-up email", "create a formal SOW from the pricing discussion", "create a Markdown GitHub issue ticket". Copilot replies in the same thread with generated content, and you can keep replying to iterate (tone, format). Context persists in the email thread instead of being lost across tab switches. Requires the SeaMeet Chrome extension and a seameet.ai account.

## Workspaces & Plans

- Workspaces manage meetings, members, and plans. The workspace creator is the "primary admin"; their subscription applies to all workspaces they own
- Seat count = unique accounts across all of a primary admin's workspaces
- Roles: Admin (view/delete all meetings, invite/remove users, grant any role) vs Member (views all meetings by default, can be restricted to own meetings only; cannot delete meetings; can only invite as Member)
- Personal Settings lets you set a default recording language, default storage workspace, and UI language
- Subscribe: Sign in → Plans & Billing → Edit Plan → choose plan → Confirm Subscription → complete payment
- Billing page shows current plan, next billing breakdown, billing recipient, usage (by conversation count), and invoice history (PDF)
- **Decision Insights** (Team plan): aggregated analysis across a workspace's meetings, can be emailed to a specified recipient

## Language Support

English (US/Singapore), Spanish (Spain/LatAm), French, German, Polish, Danish, Mandarin (Taiwan Traditional/Simplified), Cantonese (HK Traditional/Simplified), Japanese, Korean, Vietnamese, Thai, Hindi, Malay, and more. Set a default in Personal Settings, or switch per-meeting or in the SeaMeet widget. For mixed English/Chinese meetings, choose Traditional Chinese (it recognizes English concurrently).

## Meeting Features

- **Live transcript & AI analysis**: shows speaker + timestamp (custom speaker names, multilingual display); AI periodically generates summary, action items, discussion topics (one-click copy summary); collaborative "Team Notes" also available
- **Recording playback**: full playback (±10s skip) or click any transcript segment to play that portion
- **Ending a meeting**: manual stop, or automatic after 30s once everyone leaves / after 15 min of silence with someone still present
- **Meeting labels**: add/select from workspace labels per meeting, or manage centrally under Workspace Settings → Label Management
- **In-person meeting speaker identification**: audio diarization — specify speaker count to "Identify Speakers", then "Change Speaker" by listening to each segment and assigning real names, then "Regenerate Summary"; best with 2–6 speakers
- **Custom summary templates**: apply only to the "Overall Summary" (not live summary). 1 default + 17 built-in templates (class notes, client meetings, standups, interviews, sales calls, product dev, etc.). Apply per-meeting, pin to a recurring meeting series, set a personal default, or create your own
- **Export to Google Docs**: requires linking Google Drive to the workspace
- **Auto-share meeting records**: choose self-only / all calendar attendees (incl. Teams) / same-domain attendees / no one; plus an additional-recipients list (CC/BCC + blocklist)

## FAQ Highlights

- Supported formats: Google Meet, Microsoft Teams live recording, audio upload
- Video recording is not supported, audio only
- Audio download: Individual/Team plans only
- Over-limit usage: $1/hour; Free plan lifetime cap 6 hours; per-meeting cap: 1h free / 5h paid
- Team plan supports multi-user collaboration and concurrent meetings; Individual plan handles one meeting at a time
- Education accounts need manual enablement via seameet@seasalt.ai
- Transcripts aren't directly editable in SeaMeet — edit via the exported Google Doc instead
- Individual plan is $9.99/month, prorated for mid-month signup; Team plan bills new seats the following month
- Can't self-remove a credit card while subscribed (usage/seat charges settle next cycle); annual wire payment is an alternative
- No self-serve account/workspace deletion (irreversible) — contact support
- Security: Azure/AWS WAF, FIPS encryption, CASA Level 2, Nessus scanning, HECVAT certified, US data residency
- Cannot issue Taiwan invoices (US-registered company); receipts can include your tax ID

## Other Integrations

- **Browser extension**: Chrome/Edge/Arc/Brave, integrates with Google Meet, Calendar, Docs, and Outlook Calendar
- Feedback: "Feedback" tab in the sidebar, email seameet@seasalt.ai, 24–48h response time

## Release Notes Highlights (recent; full changelog in source files)

- 2025/10/16: live transcript speaker indicators + multilingual display, custom speaker names
- 2025/10/09: auto-share email support for Microsoft Teams calendar meetings
- 2025/09/12: launched Team-plan "Decision Insights"; weekly meeting digest email became interactive/dynamic
- 2025/08/28: Microsoft account sign-in, Outlook Calendar binding, Teams auto-join
- 2025/07/17: "Enhanced Recognition Vocabulary" for domain-specific terms; Teams meeting recording via link
- 2025/02/20: launched Summary Templates
- 2024: audio upload, speaker replacement, auto-join, multi-browser support, paid plans launched

*Full weekly changelog (2024–2025) preserved in the source files.*
