# Seax Documentation (Summary)

*Condensed from combined_wiki_md_files/seax_en.md — see that file for full detail.*

## What is SeaX?

**SeaX** is Seasalt.ai's omni-channel communication platform for **bulk outreach**, **two-way messaging**, and **AI-agent automated responses** (via SeaChat) across **SMS**, **WhatsApp**, and **Phone Calls**. Homepage: https://seax.seasalt.ai/

Three pillars per channel: (1) Bulk messaging/calling at scale with delivery tracking, (2) Two-way conversation threads for lead qualification/support, (3) AI agent handoff via SeaChat integration with optional escalation to human agents.

## Channels

- **SMS** — global reach, notifications/reminders
- **WhatsApp** — via WhatsApp Business API, rich media/buttons, brand-verified
- **Phone Calls** — automated (TTS/recorded) campaigns + human agent dialer (outbound campaigns, inbound routing, click-to-call)
- Coming soon: Facebook Messenger, Instagram Messaging, LINE

## Dialpad (inbound/outbound calling)

Built-in browser dialpad complementing bulk campaigns. Agent statuses: Available (green) / Away (orange) / Do Not Disturb (red) / Offline (gray) / On a Call (auto). Round-robin routing: rings each Available agent 10s, prioritizes least-busy, skips no-answers, falls back to AI if no human available. Supports manual dialing (search contacts) and AI-assisted dialing (select a SeaChat voice agent, enter target number — good for interviews, appointments, follow-ups). Call logs, contact-name resolution, per-number/per-channel agent assignment configurable.

## WhatsApp Integration

**WhatsApp Business Platform (Meta Cloud API — current/recommended)**
- Connect via Workspace → Channels → WhatsApp Business Platform → Add Account (Meta Business Suite login)
- Templates must be pre-approved in Meta WhatsApp Manager (category, `{{variables}}`, media, buttons), then **Synchronize from WhatsApp** into SeaX
- Contacts: manual entry or CSV bulk import, E.164 phone format required
- Campaign flow: Bulk Send → select WhatsApp → recipient labels → sender number/campaign name → template → final review → Send Now (10s cancel window)
- Messaging rules: customer-initiated messages get a free 24h reply window; business-initiated messages require an approved template, which also opens a 24h window; template sending requires a valid payment method
- No contact limits; pricing is volume-independent
- Monitoring: Delivered/Failed/Read status per message; replies land in Conversations

**WhatsApp Business App (Deprecated)** — QR-code device linking, bypasses the official app's 4-device cap by connecting unlimited WhatsApp Business accounts to SeaX; per-account agent assignment via Numbers settings.

## SeaX Bulk Send with SeaChat (AI agents)

Requires a SeaX phone number and a SeaChat AI agent **in the same workspace**. Flow: pick recipient labels → confirm contacts → compose campaign (name, labels, execution method = "Chat/Voice Agent", schedule + cutoff time for calls) → choose sender number → review (incl. inbound agent) → Send Now. Optional: capture recipient key-presses (calls) and click tracking (SMS links).

Conversation sync caveats: SeaChat-agent-initiated outbound calls show in both platforms' Conversations; but inbound calls received on SeaChat don't sync to SeaX, and SMS replies only sync to SeaChat if the number is an active AI-campaign recipient.

## SeaX Widget (Webchat)

Embeddable chat button for websites/apps. Customize: Bubble (icon URL, popup greeting), Popout (title, colors, opening message), and optional Custom Forms (pre-chat text/email/phone fields, consent checkbox with privacy-policy link, submission message; active forms can't be deleted). Install by pasting a JS/HTML snippet before `</body>`. Test without installing via the dashboard's **Test Widget** button.

## SeaX Enterprise Contact Center (Twilio Flex)

Full collaborative contact center unifying omni-channel messaging (Facebook, SMS, Google Business Messages/Maps, WhatsApp, LINE) in one agent interface.

- **Basics**: warm/cold call transfer, supervisor monitor & barge-in, custom hours + holiday/offline auto-messages, voicemail with agent assignment and admin notifications
- **Advanced**: SeaX Virtual Agent (chat/voice AI answering location/hours/contact/amenities/menu, escalates to live agent for complex questions), AI Knowledge Base (real-time answer lookup for agents), AI-Powered Agent Coach (live conversation objective checklist), Case Management (customer info + open case tracking), Auto Dialers — **Message Drop Dialer** (auto-dial + play message) and **Progressive Dialer** (auto-dial, only connects agent once a human answers), SeaMeet Copilot (call/meeting analytics + AI agent performance metrics)
- **CRM/other integrations**: HubSpot (call sync, automated appointment scheduling), Salesforce (click-to-dial + auto case creation, call recording/logs, auto CSAT survey & reporting), Discord (automated support/case tracking with HubSpot)

## Release History Highlights (recent; full changelog in source file)

- 2025/08/07: call log agent visibility, workspace list cleanup, voice call activity logging
- 2025/07/17–07/31: WhatsApp HSM campaigns with media/titles, mobile calling, skills/IVR assignment, Argentina number format support
- 2025/07/10: WhatsApp campaign ↔ SeaChat AI agent sync, SeaX↔SeaChat message sync, Meta template-fetch API
- 2025/02/13: SeaChat integration with WhatsApp Business Platform; per-number AI agent assignment
- 2025/02/20: MegaSend feature with DNC checking
- 2024: WhatsApp channel launch (05/2024), user registration/self-serve workspaces (09/2024), phone number purchasing, dynamic WhatsApp message loading, Business Caller ID binding

*Full weekly changelog (2024–2025) preserved in the original seax_en.md.*
