# SeaChat Documentation (Merged Summary)

*Merged and condensed from all language versions — combined_wiki_md_files/seachat_en.md, seachat_zh.md, seachat_zh-TW.md. The English source is the most complete (Chinese versions are translations of the same or a smaller/older subset); see the originals for full detail/screenshots.*

## What is SeaChat?

SeaChat is Seasalt.ai's ChatGPT-powered omni-channel AI agent platform with a free-for-life web chat widget for human replies. Set up AI + human agent workflows across channels in under 10 minutes. Sign up: https://chat.seasalt.ai/

**Truly Free plan**: choose "Human Agent Only" mode at signup — unlimited chats/history/contacts/exports, 1 agent, 1 workspace, no card required. You only need a paid plan once you want AI-automated replies, custom knowledge base, 24/7 support, or phone calls; AI can be toggled on/off anytime without redoing channel setup.

**Quick start**: create workspace → create agent (name + response language + optional live-agent toggle) → add knowledge → upload files → test agent → fine-tune.

## Creating & Configuring an Agent

- **Create New Agent**: from scratch (full custom prompt) or from a predefined **Use Case** (SeaChat-authored base prompt + your Description appended) — combined into the full system prompt.
- **Agent Information / Basic Settings**: Name (internal only — display name is set per-channel), Use Case, Description, Response Language ("respond in user's language" vs "always respond in selected language" — mixed-language messages default to the most prominent language), Live Agent toggle, Agent URL for standalone testing, API Key for embedding.
- **Chat Design Style**: customizable widget colors/style with live preview; Chat Settings for greeting/start/end messages.
- **Agent Version Control**: **Duplicate** an agent (copies basic info, advanced settings, KB, widget — NOT channels) to prototype safely; **Replace** swaps a production agent with a tested copy while keeping original settings/channels intact — typical flow: duplicate A→B, develop B, replace A with B.

## Advanced Settings

- **RAG (Retrieval Augmented Generation)**: Query Pattern — "Prev Query→Bot→Current" (full context, last 3 turns), "Prev→Current" (user-focused, ignores bot reply), or "Current Query only" (best for single-turn/topic-switching). Search Method — Keyword (best for exact IDs/names), Vector (cross-language/semantic), or Hybrid. KB Retrieval Count — tune chunk count vs. context-window limits. **KB Search Refinement**: optional secondary LLM pass with custom instructions (e.g. "extract branch/product name from query, exclude unrelated branches") — great for multi-location or large product-catalog KBs.
- **Long-Term Memory** (premium): agent retains persistent per-user facts/preferences across sessions indefinitely (default history is 20 turns without it). Supervisors manage/view/erase memory per-conversation in Conversations (3-dot menu → Erase All, irreversible). To fully disable context, also set Conversation History Turn Count to 0.
- **Time Awareness & Context**, **Context Extraction** (define structured fields — non-survey and survey use cases — to extract from conversations, monitored per-conversation), **KB References** (source citation config), **AI Agent Response Schedule** (Advanced Settings → set business-hours/24-7/seasonal automation windows — e.g. AI only outside business hours).

## Knowledge Base

Upload methods: **Spreadsheet/Table** (.csv/.xlsx, optionally one KB doc per row), **Audio/Video** (English/Traditional Chinese), **Template Upload** (predefined spreadsheet templates), **Document Upload** (Document Title + Text, additional attribute key/value pairs, optional settings), **Import URLs**, **Import Sitemaps**, **Manual Entry**, and **KB ID** buttons (attach clickable URL buttons to KB-sourced responses — also fixes LINE's message-truncation limit). File Size Rule and token usage vary by plan (see Pricing). **Card Message** / **Button Message** / **Document Weight** are additional KB-response formatting options.

## Live Agent & Hybrid Mode

Enable via Agent Information checkbox. Human agents monitor/take over in **Conversations**; click **Complete** to hand back to AI, or **Reactivate** to resume. WebChat shows a "Talk to Live Agent" button; non-widget channels (Messenger, WhatsApp) require the customer to ask verbally (togglable separately). LINE shows a Live Agent button. Markdown/links render in WebChat only. **Hybrid Mode** options: disable proactive live-agent requests, show conversation summary to all parties, and auto-timeout idle live-agent sessions back to AI.

## Conversations & Analytics

Conversations dashboard: full history, audio download, exportable agent conversation history. Analytics dashboard covers: Conversations, Activity Trend, Label Usage Overview/by Period, Label Relationship Analysis, CSAT, Yearly Overview, with configurable time zone.

## Channels

- **WhatsApp** (via Business Platform/Cloud API — create Meta app, connect business, set up permanent system-user token, decorate WA Business profile; button-count limits apply)
- **LINE Official Account** — auto-reply integration; button messages have a character limit (use KB IDs to avoid truncation)
- **Facebook Messenger** — current method via **Embedded Signup** (2-step connect) or legacy/deprecated manual Meta-app + webhook setup; button limits apply
- **Calls (Voice Agent)** — purchase a toll-free number in-app, configure inbound/outbound voice agent (SeaVoice or experimental SeaVoice-2 model), enable live-agent handoff, test with real calls
- **Instagram** — current OAuth-based 2-step connect (requires Instagram Business/Creator account) or legacy manual Meta-app setup
- **Webpage** widget — Basic/Chat Settings, Card Settings, appearance/name/language settings, Custom Forms (pre-chat info collection, CSAT survey form)

## Other Platform Integrations

Google Calendar (appointment booking via chat/voice), Shopify, Squarespace, Wix, MailerLite (auto-add form emails to lists via API token), WordPress — each has an embed/connect guide.

## SeaX Integrations

- **SMS & Call**: assign/configure a number, sync AI agents, configure inbound handling, test, set up outbound campaigns, manage inbound callbacks
- **Bulk Outbound/Inbound Phone Calls with AI Agents**
- **WhatsApp bulk messaging** with SeaChat auto-reply
- **Programmatic contact-form pre-fill**: pass query-string params in the webchat URL to pre-fill the WebChat form so customers don't retype info

## Operations & Team Features

- **Workspace Management**: members, custom fields, membership assignment, notification settings (add members, enable email notifications, consider enabling the web-widget form)
- **Test and Improve AI Agent** (tutorial + tips), **SOP for After-Launch Operations** — defines what human agents vs. AI-agent editors/admins should routinely do
- **Evaluation (Test Sets)**: create a test set, add test samples (incl. pulling from real conversations), run the set, review results, import/export as JSON — use cases: QA on responses, performance monitoring, multilingual support testing, industry-specific knowledge training
- **Custom GPT Tools / API Tool integration**: configure external API calls as agent tools (select tool type, required fields, result display, test, save) — includes an image-input variant with card-description settings
- **Zendesk Ticket Search Tool**: configure account info + search parameters so the agent can look up Zendesk tickets
- **Auto Labeling** and **Label Automation**: auto-tag conversations and trigger actions based on applied labels
- **Inline.app Assistant**: restaurant order/reservation management integration
- Agent understands **uploaded image and audio messages** from users (e.g. a webinar invite screenshot) without the user retyping content
- **Build Email Lists with MailerLite** and **Book Appointments Instantly with Google Forms & Voice Agent**: dedicated tutorials for form-to-email-list and form-to-instant-call automations

## Pricing (see source for current details)

- **Free**: lifetime 100 AI text replies, 1 agent, KB up to 10 docs/200KB/200K tokens, 1 owner + 1 workspace, GPT-3.5-turbo
- **Standard**: 2 agents, KB up to 100 docs/1MB/1M tokens, 1 owner + 1 member + 1 workspace, $0.01/AI response, GPT-3.5-turbo
- **Premium**: 10 agents, KB up to 500 docs/10MB/5M tokens, 1 owner + 3 members + 2 workspaces, AI response from $0.006, choice of model (GPT-4o/4o-mini/4-turbo/3.5-turbo/Mistral etc.), voice agent from $0.15/min, plus Context Extraction, API access, branding removal
- **Launch Support Plan** available for complex/voice deployments (LLM+RAG expertise, FCC/telecom compliance help)
- Billing dashboard: plan editing, next-bill cost breakdown, billing recipient, usage (text+voice), invoice history (PDF)

## Reference Material

- **Prompt Examples**, **SeaChat API** (RESTful, for workflow automation), **Call-forwarding setup guides** for major US/TW/SG carriers (AT&T, T-Mobile, Verizon, Comcast/Xfinity, RingCentral, Vonage, Google Voice, Chunghwa Telecom, Taiwan Mobile, Singtel) to route inbound calls to a SeaChat voice agent
- **FAQ highlights**: login is passwordless (email login-code only, no password reset); LINE button truncation is fixed via KB IDs; to attract more chat engagement, use a GIF widget icon and a delayed popup bubble (Channels→Webchat→Bubble)

## Release Notes Highlights (recent; full changelog in source files)

- 2025/12/10: idle-wait auto-hangup for Twilio calls; voicemail-detection examples for the voice agent
- 2025/08: emoji reactions on Meta-channel messages; Analytics CSAT block added; new Japanese/Indonesian voices
- Ongoing: steady channel, CRM (Zoho/Zendesk), analytics, and voice-agent updates — full weekly changelog (2024–2025) in the source files.
