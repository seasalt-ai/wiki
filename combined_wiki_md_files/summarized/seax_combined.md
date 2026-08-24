# Seax Documentation (Summary)

*Condensed from combined_wiki_md_files/seax_combined.md — the most up-to-date SeaX doc (release notes through 1/8/2026). See that file for full detail.*

## What is SeaX?

**SeaX** is Seasalt.ai's omni-channel communication platform for **bulk outreach**, **two-way messaging**, and **AI-agent automated responses** (via SeaChat) across **SMS**, **WhatsApp**, **Phone Calls**, and (via Enterprise) Facebook/Instagram/LINE/Google Business Messages. Homepage: https://seax.seasalt.ai/

Three pillars per channel: bulk messaging/calling at scale, two-way conversation threads, and AI-agent handoff with optional human escalation. A unified **"All Conversations"** view and per-channel sidebar tabs let agents browse messages across all connected channels/channel groups.

## Channels & Dialpad

- **SMS**, **WhatsApp** (Business API), **Phone Calls** (automated TTS/recorded campaigns + human dialer)
- Built-in browser **dialpad**: statuses Available/Away/Do Not Disturb/Offline/On a Call; round-robin routing (10s ring per agent, least-busy first, AI fallback if no human online); manual or AI-assisted dialing (pick a SeaChat voice agent + number)

## WhatsApp Integration (3 connection modes)

1. **WhatsApp Business Platform (Meta Cloud API)** — connect via Workspace→Channels, requires Meta-approved templates (synced into SeaX), E.164 contacts, CSV bulk import; messaging rules: 24h free reply window after customer contact, or business-initiated via approved template (requires payment method on file); no contact limits
2. **WhatsApp Coexistence (Beta, new)** — keeps the native WhatsApp Business App on your phone while adding Cloud API scale. Setup: Workspace→Channels→Add New Channel→WhatsApp Coexistence→login with Meta→choose "Connect a WhatsApp Business App"→enter existing number→scan QR from the WhatsApp app (Settings→Linked Devices)→confirm up to 6 months of 1-on-1 chat history sync (group chats excluded). "Tri-sync" across native app, SeaX web, and SeaX mobile app; unlimited agents (breaks the native app's 4-device cap); requires opening the phone app at least once every 14 days to keep the connection alive
3. **WhatsApp Business App (Deprecated)** — QR-linked, up to unlimited accounts connected to SeaX despite the app's own 4-device limit

## SeaX Bulk Send with SeaChat (AI agents)

Same-workspace SeaX number + SeaChat AI agent required. Flow: recipient labels → contacts → compose campaign (name, labels, "Chat/Voice Agent" execution, schedule + call cutoff time) → sender number → review (incl. inbound agent) → Send Now. Optional key-press capture (calls) and click tracking (SMS). Conversation sync: SeaChat-initiated outbound calls show on both platforms; SeaChat-received inbound calls don't sync to SeaX; SMS replies sync to SeaChat only if the number is an active AI-campaign recipient.

## Zapier Integration — "Agentic Send"

Collapses multi-step Zapier automations (trigger → formatter → path/condition → send, often 5+ steps) into **2 steps**: a trigger + one "Agentic Send" action. You write a plain-language system prompt (e.g. "extract phone numbers from the participant list and send an SMS reminder") and paste the trigger's raw JSON payload directly — an LLM agent extracts data, fixes phone format (e.g. adds missing E.164 country code), and sends via SMS/WhatsApp (select workspace/number/template). Works with any of Zapier's 8,000+ trigger apps (Google Sheets, Typeform, Mailchimp, Google Calendar, etc.). Zapier app page: https://zapier.com/apps/seasaltai/integrations

## Zoho CRM Integration

Workspace→Integrations→Zoho. Requires creating a Server-based Application client in Zoho's API Console (api-console.zoho.com) using SeaX-provided Homepage URL and Redirect URI, then pasting the resulting Client ID/Secret back into SeaX and authorizing. Once connected, sync contacts from any conversation via the Edit Contact → Sync Zoho button (push SeaX edits to Zoho, or pull existing Zoho contact details into SeaX). Zoho's free tier (3 users, 5,000 API calls/day) supports the integration.

## SeaX Widget (Webchat)

Embeddable chat button. Customize Bubble (icon, popup greeting), Popout (title, colors, opening message), optional Custom Forms (pre-chat fields, consent checkbox, submission message — active forms can't be deleted). Install by pasting a snippet before `</body>`; test via the dashboard's **Test Widget** button without installing.

## Customer Satisfaction (CSAT) Surveys

Available for **LINE, WhatsApp, Instagram, Messenger** (contact support for other channels). Configure under Workspace→Channels: enable CSAT, write a message instructing customers to reply with a single digit **1–5** (only digits 1-5 count as valid ratings).

- **Manual send**: CSAT icon in the conversation window, unlimited uses — but for Instagram/Messenger/WhatsApp (Meta channels), the icon is disabled unless the customer messaged within the last 24 hours (Meta policy)
- **Auto-send**: toggle + configurable delay (minutes) after the customer's last inbound message; countdown restarts on each new inbound message; retries until a valid rating is received; triggers once per conversation but keeps retrying
- **Reply parsing**: valid 1–5 reply → recorded as score, resends stop; invalid reply (e.g. "thanks", emoji) → treated as a normal message, auto-retry continues; no reply → countdown just restarts on next inbound message
- CSAT metrics appear on the analytics page

## SeaX Enterprise Contact Center (Twilio Flex)

Omni-channel agent interface (Facebook, SMS, Google Business Messages/Maps, WhatsApp, LINE). Basics: warm/cold transfer, supervisor monitor & barge-in, custom hours/holiday messages, voicemail with assignment. Advanced: SeaX Virtual Agent (FAQ bot with live-agent escalation), AI Knowledge Base, AI-Powered Agent Coach, Case Management, Auto Dialers (Message Drop / Progressive), SeaMeet Copilot analytics. CRM/other integrations: HubSpot, Salesforce (click-to-dial, auto case creation, CSAT), Discord.

## Release Notes Highlights (recent; full changelog in source file)

- 2026/01/08: unified "All Conversations" view + channel sidebar tabs; call records now include outcomes; auto-fill agent names on outbound logs
- 2025/12/29–12/18: Zoho integration polish, CSAT metrics on analytics page, CSAT scheduling, channel-group settings, mobile push-credential sync
- 2025/12/04: **Zapier integration launched**; SeaNotify push-notification framework; multi-note contacts
- 2025/11/21: read receipts for LINE/WhatsApp, multi-channel contact avatars
- 2025/08–10: WhatsApp Coexistence beta, various dialpad/CSAT/Zoho refinements

*Full weekly changelog (2024–2026) preserved in the original seax_combined.md.*
