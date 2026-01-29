---
title: "SeaX Mobile Release Notes"
description: "Stay informed about the latest SeaX Mobile capabilities, performance optimizations, and fixes."
date: 2026-01-08T08:48:57+00:00
lastmod: 2026-01-08T08:48:57+00:00
draft: false
images: []
menu:
  seax:
    parent: "seax-product-updates"
aliases:
  - /en/seax-mobile-release-notes/
  - /en/seax/mobile-release-notes/
# NOTE: All product update pages should follow the URL format: https://wiki.seasalt.ai/${language}/${product}/product-updates/
url: /en/seax-mobile/product-updates/
weight: 2
toc: true
---

Stay on top of SeaX Mobile enhancements. For a unified omnichannel log, visit the [SeaX Release History](/en/seax/product-updates/).

### 0.0.2

##### **<font color="#739963">New Features & Improvements</font>**

- Redesigned MessageBubble with direction labels, live timestamps, unsynced-media placeholders, and recording cards, using localized "Inbound / Outbound" and WhatsApp sync warnings.
- ConversationDetail and ConversationList hooks are now network-aware, add Twilio-specific ordering fields, and capture retry plus WebSocket lifecycle logs to cut offline errors.
- Conversation screens merge route parameters with store fallbacks for workspace/phone selection and adopt KeyboardAvoidingViewCompat, handlingStatus, ChannelIcon, and ContactAvatar for better headers and input handling.
- DialerScreen was overhauled with an MD3 dial pad, PhoneSelectField, lazy-loaded workspace phones, full-screen search and contact suggestions, microphone permission prompts, DEV diagnostics, and prefilled numbers from other screens.
- ActiveCallScreen derives display names from Twilio call parameters and workspace contacts while CallLog / IncomingCall / PhoneSelection reuse PhoneSelectField and loadWorkspacePhones for consistent phone metadata.
- Android adds EarlyInitProvider plus ReactNativeInitializer, and core bootstraps (AppProviders, StatusBarBackground, useOptionalNetInfo) along with package/babel/metro/jest/i18n updates to stabilize startup.

##### **<font color="#d66a60">Bug Fixes</font>**

- Conversation sockets now retry based on connectivity and Twilio ordering, preventing duplicate or out-of-order messages after a reconnect.
- CallLog, PhoneSelection, and ActiveCallScreen log failures and show fallback descriptions when workspace phone metadata cannot be fetched, avoiding blank views.
- Android boot now preloads React Native and Twilio Voice, fixing intermittent background-notification connection failures.
- KeyboardAvoidingViewCompat offset tuning keeps the conversation composer visible instead of being covered by the OS keyboard.

### 0.0.1

##### **<font color="#739963">New Features & Improvements</font>**

- Established the Seasalt rebrand baseline by resetting marketing/build numbers to 0.0.1, unifying bundle identifiers, and updating scripts, environment files, and docs.
- Delivered the initial React Native experience: login, workspace selection, conversation list/detail, Twilio Voice calling, push notifications, and caller ID setup.

##### **<font color="#d66a60">Bug Fixes</font>**

- Unified MARKETING_VERSION/versionName and build-number baselines to remove iOS vs. Android version conflicts.

