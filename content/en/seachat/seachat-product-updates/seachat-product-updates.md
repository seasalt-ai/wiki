---
title: "SeaChat Release History"
description: "Stay up-to-date with SeaChat's latest release on new AI features, improvements, and bug fixes."
date: 2023-11-22T08:48:57+00:00
lastmod: 2025-01-15-24T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-product-updates"
aliases:
  - /en/seachat-product-updates/
  - /en/seachat/seachat-product-updates/
url: /en/seachat/product-updates/
weight: 1600
toc: true
---

### 6/12/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Custom CSAT Form for Widget Installations: You can now attach a CSAT (Customer Satisfaction) form to your SeaChat widget. When users interact via the widget, the form can automatically pop up, and you’ll be able to view feedback linked to each conversation directly from your dashboard. See tutorial [here](/en/seachat/manual/channels/webpage/#custom-forms-csat-survey-form).
- Multiple Image Support in WebChat: SeaChat now supports sending multiple images in a single message when your customers chat with your AI agent. SeaChat AI agent will now comprehensively understand all images together—enabling more contextual and accurate responses, instead of processing them one by one.
- Improved Time Awareness Accuracy: Fixed an issue where the AI agent, when time awareness was enabled, failed to provide the correct localized time.
- LINE Formatting Fix: Resolved a bug where messages sent by the AI agent to LINE always had an unnecessary leading whitespace before each sentence.

### 6/5/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Instagram Login with OAuth: Streamlined authentication process allowing you to easily sign in and connect your Instagram account with your SeaChat AI agent. See tutorial [here](/en/seachat/manual/channels/instagram/).
- Enhanced Image Upload Capacity: Maximum image upload size increased to 20MB for human agent conversations, enabling more flexibility in sharing visual content with customers.

### 6/1/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Auto-Labeling Refined: Fixed behavior where auto-labeling incorrectly replaced labels instead of patching them. With this update, labels are now correctly patched—allowing multiple labels to coexist without overwriting each other.
- GA4 Customization Support: You can now add your GA4 Measurement ID directly in the Agent Information tab → Design Style page → Chat Settings section. Once set, SeaChat will begin sending widget interaction data (like message sends, button clicks, and agent handovers) to your GA4 property—allowing for detailed user behavior insights and performance monitoring.
- Live Agent Transfer Options: We updates the options for live agent transfer so users can customize how live agent handovers are triggered. Users can now choose between user requests via button clicks, intent expressed during conversations with the AI agent, or both.
- Conversation Image Upload Size Limit Increased: We’ve raised the maximum image upload size to 20 MB. You can now upload images up to this size in your conversations, making it easier to share clearer, higher-quality visuals.

### 5/22/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Live Agent Transfer Enhancement: Added seamless live agent transfer functionality in chat. When enabled, customer messages to the AI agent will be smoothly transferred to a human agent.
- Webchat Card Improvements: Added support for inbound message cards in Webchat. When users click these cards, the system sends a predefined question to your AI agent, initiating a conversation automatically.
- LINE Message Template Enhancement: Improved LINE template message handling by sending quick action buttons as a separate text message, ensuring button visibility throughout the conversation.

### 5/15/2025

##### **<font color="#739963">New Features and Improvements</font>**
- Better document knowledge base upload handling: Fixed the bug that caused server timeout when uploading large documents. Now users can upload large documents and the system will process the upload as a background process, while users can work on something else.
- Messenger integration with FB embedded signup: We support FB embedded signup, and users can sign up with their FB account directly and choose which FB page to connect with their SeaChat AI agent. See tutorial [here](/en/seachat/manual/channels/facebook-messenger-embedded-signup/).

### 5/8/2025

##### **<font color="#739963">New Features and Improvements</font>**
- Added multilanguage support in Billing page cost breakdown for the next bill.

### 5/1/2025

##### **<font color="#739963">New Features and Improvements</font>**
- Messenger Conversation Title Enhancement: Fixed an issue where sender names were not being captured in Messenger conversation titles. Now, conversation titles from Messenger are automatically updated to include the sender's name, making conversations more identifiable and easier to manage.
- Expanded AI agent Description Limit: Increased the character limit for AI agent descriptions based on different language models. Users can now provide more comprehensive descriptions of AI agent functionalities.
- Voice Conversation Recording Download Fix: Resolved the issue with downloading voice conversation recordings, ensuring users can successfully access their voice conversation records.

### 4/24/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Extraction Enhancement: We have optimized the `Extraction` feature, enabling AI agents to more accurately identify and extract key information from user conversations.
- Google Calendar Timezone Fix: Fixed the default timezone setting issue in Google Calendar integration. The system now correctly identifies and uses the user's browser timezone, preventing AI agent from stop responding issues previously caused by incorrect timezone codes.

### 4/16/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Human Agent-Only Mode Enhancement: The automatic switch to AI agents is now disabled in human agent-only mode, ensuring that human agents have sufficient time to address customer inquiries without interruption.
- Mobile Widget Display Optimization: Improved the display logic for mobile widgets, ensuring that only one widget icon is visible on mobile devices when a single widget is configured.

### 4/9/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Enhanced References feature: When users enable the References feature in the Advanced Settings page and have configured the Zendesk ticket search tool, if the AI agent's response includes content from Zendesk tickets, the system will display the relevant ticket numbers and titles in the references area, making it easier to track information sources.

### 4/1/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Knowledge Base Refinement: Users can now configure whether to refine knowledge base search results and customize instructions for the LLM in the Agent Information's Advanced Settings page on how to optimize these results, enhancing AI agent performance when answering user queries. See [tutorial](/en/seachat/manual/create-agent/advanced-settings/rag/#knowledge-base-search-refinement).

### 3/20/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Webchat Widget Bubble Feature: Users can now add an attention-grabbing bubble near the webchat widget to make it more visually prominent and appealing. This feature can be configured in the webchat widget settings page.

### 3/13/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Email Format Validation: An email format validation is added in webchat forms to ensure customers provide correct email addresses.
- Enhanced Call End Feature: When a voice conversation is in progress, the button in the upper right corner of the conversation detail window will function as an end call button, allowing users to terminate ongoing calls with a single click.

### 3/5/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Improved Mobile Experience: Fixed conversation page styles on mobile to ensure users can conveniently view conversations and reply to customers.
- Google Calendar Integration Update: Setting up Google Calendar integration now automatically enables Time Awareness in the AI agent’s Advanced Settings, using the selected timezone.

### 2/26/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Evaluation Test Set Import & Export: Users can now export evaluation test sets to a JSON file, allowing for easier backup and editing. Additionally, users can import test set data by uploading a JSON file, enabling bulk management of test sets more efficiently. See [tutorial](/seachat/seachat-manual/07-test-and-improve-ai-agent/evaluation/#4-importing-and-exporting-evaluation-test-sets)
- Email Notifications for Assigned Conversations: When a conversation is assigned to a human agent, the system will now automatically send an email notification to that agent to promptly inform the agent.
- Configurable Auto-Hangup for Voice Calls: Users can now configure whether they want to enable automatic hangups for voice calls when a caller says phrases like "goodbye" or expresses an intent to leave.

### 2/19/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Evaluation Testing: Users can now assess AI agent responses by providing test sets, each containing a user query, a gold response, and optional conversation history. The AI agent’s response is compared against the gold response, with results displaying overall correctness and individual sample accuracy. Users can refine their AI agent and run evaluations to continuously improve performance.
- Conversation Label Editing: Users can now create, edit, and delete chat labels directly from the Labels page.
- Knowledge Base (KB) Export: Users can now export all KB entries by going to Knowledge Based → Existing → View All and choose Export to CSV or JSON via the corresponding option. Files can be updated and re-uploaded through "Upload from Template File".

### 2/13/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Pre-Fill Contact Forms: SeaChat now auto-fills webchat forms using query strings in the URL, eliminating manual entry. See [tutorial](/en/seachat/seachat-integrations/seachat-prefill-contact-forms/)
- Fix for Empty Instagram Conversations: Prevents false alerts from thumbs-up reactions and story mentions.
- Improved WebChat UI: When open, the widget now shows a close icon instead of the logo for better clarity.

### 2/6/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Items Per Page Selector in Pagination for Bulk Actions: A dropdown has been added to pagination, allowing you to choose how many items to display per page.
- Knowledge Base Sort By Title: You can now search KB articles by title. Additionally, click the sort icon to organize articles in ascending order.
- Quick Customer Calling: A new **Call Customer** button is available in the upper right corner of the conversation detail window. If a customer called in via the voice channel, you can now quickly call them back.
- Updated Conversation History File Name Formats: Downloaded conversation history files now follow a structured format:`Conversation Title – Conversation Start Datetime – Channel.csv`.

### 1/16/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Channel-Specific Language Support: SeaChat now supports defining the language for voice messages on a per-channel basis. This enables the platform to transcribe voice messages into text and reply in the same language. This setting allows users to tailor communication to meet the needs of different language-speaking audiences across various platforms, including LINE, WhatsApp, Messenger, and Instagram. The setting also applies to system messages, such as the one sent to users when they click 🧹 "New Topic."
- Voice Call Widget Added: A voice call widget has been added to the chat widget. Users can either embed HTML code or a URL to a form to receive customers’ calls. When customers click the call icon, an iframe containing your embedded HTML will pop up, or they will be redirected to your specified form if a URL is provided.

### 1/9/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Transcribe Voice Messages from WhatsApp and LINE: SeaChat AI Agent now supports transcription of audio messages sent via WhatsApp and LINE. When your customers send a voice message, SeaChat will transcribe it, enabling your AI Agent to understand and respond accurately to their inquiries.
- New Custom GPT Tool: Zendesk Ticket Search: We’ve added a new Zendesk Ticket Search tool to the Custom GPT Tool library. You can provide your Zendesk account information to enable SeaChat to fetch ticket details and comments, allowing SeaChat to answer user queries based on relevant tickets.
- Input Box Detect Input Language: SeaChat now supports automatic language detection in the agent's typing input box and the webchat input box for customers. Whether it's a Right-to-Left (RTL) or Left-to-Right (LTR) language, the input is handled automatically.

### 12/26/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Instagram Widget: Users can now add an Instagram widget to their website by simply entering the Instagram link and copying the automatically generated HTML code snippet in Channels to embed it seamlessly.
- Customizable Webchat Menu: Users can now choose to remove the "Get SeaChat" link from the menu dropdown in the webchat's upper-right corner. This option is available in the Design Style section of the Agent Information tab.
- Real-Time Auto-Labeling Updates: We’ve fixed an issue where the UI did not update in real time when labels were automatically applied or removed from conversations using the auto-labeling feature. Now, label changes are reflected immediately in the UI.

### 12/19/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Auto-labeling: SeaChat can now automatically add or remove labels from conversations based on the content of the discussion. Users can define trigger conditions, provide detailed descriptions for accuracy, and select the labels to be managed.
- Label Automations: Users can configure actions that will automatically triggered by label changes within conversations. Users can define which labels should activate these actions and configure one or more automations to streamline workflows and improve efficiency. SeaChat will execute the predefined actions automatically whenever a label is applied or removed.
- Instagram integration: SeaChat now supports Instagram integration, allowing users to connect their Instagram accounts and manage messages directly within the platform.

### 12/11/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Custom GPT Tool Limit: Users can now create more than five custom GPT tools. However, only up to five tools can be enabled at any given time. If users attempt to create a new tool after reaching this limit, the tool will be successfully created but automatically disabled. To enable it, user will need to delete or disable one of the currently enabled tools.
- View and Manage Long-Term Memory: Users can now view user long-term memory by right-clicking on any conversation and selecting the 'User Memory' option. To make this option available, the 'User Memory' feature must first be enabled in Advanced Settings.
- Agent Email Visibility Update: Live agents' emails will no longer be displayed in webchat. Instead, only the agent's name will be shown. Live agents can customize the name displayed to customer via their profile settings in SeaChat.

##### **<font color="#d66a60">Bugfix</font>**

- Conversation History Download: We have resolved an issue with generating conversation history download links. Users can now successfully download their conversation history.

### 11/27/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Expanded Language Support: We now support more languages in the webchat widget, including English, Spanish, French, Japanese, Korean, Russian, Portuguese, Polish, Simplified Chinese, and Traditional Chinese. Configurable messages in the widget are automatically translated based on the selected language. Users can still customize these messages if needed.
- Enhanced Automated Actions with Custom GPT Tools: Two new custom GPT tools have been added - Send Email and Send SMS. These tools enable SeaChat to intelligently decide when to send emails or SMS messages based on your instructions.
- Long-Term User Memory: SeaChat now offers long-term memory for AI agents, enabling them to retain key information about customers, such as preferences, past questions, and interests. When users return, even after a long time, AI agents can recall this information.
- Improved Conversation Keyword Search: The conversation keyword search now includes conversation titles, allowing users to search by title for more comprehensive and accurate results.

### 11/21/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Preferred and Enforced Response Languages: Users can now specify the language SeaChat should use in responses. With the preferred response language setting, SeaChat detects the user's language and responds accordingly, defaulting to the selected language if it cannot determine the user's language. With the enforced response language setting, SeaChat consistently responds in the selected language regardless of the user's input.
- Hybrid Conversation Handling Mode: In Hybrid mode, users can now configure whether to allow customers to proactively request a live agent. If enabled, customers will see a "Talk to Human Agent" button in webchat or a quick action button in WhatsApp, Messenger, and LINE.
- Complete Form Message Configuration: Users can now configure the message sent after a user completes a form, such as "I agree to the Privacy Policy I just submitted." in Webchat Widget Custom Form page.
- Voice Bot Filler Word Configuration: Users can now enable filler words in the voice bot for faster responses and adjust the probability of including filler words in its replies in Calls integration page and SeaX Calls integration page.

### 11/14/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Button Display Limits on Messenger and WhatsApp: We've resolved an issue where exceeding the platform button limits on Messenger and WhatsApp caused display issues. Now, if the button count exceeds the limit, we will display only the maximum allowable number of buttons.
- Free Welcome Message and User Form: The welcome message and user form completion no longer count toward the monthly message quota. They are free.
- Enhanced Conversation Handling Mode Compatibility: Conversation Handling Mode now functions seamlessly across LINE, Messenger, and WhatsApp, besides Webchat. When you switch from any mode to Human Agent Only mode, all customer messages will be sent directly to your live agent. When switching to AI Agent Only mode, customer messages will be handled exclusively by your AI bot. Switching to Hybrid mode keeps the current conversation status unchanged, but your customers can change interaction modes by requesting to return to the AI agent or transfer to a human agent.

### 11/07/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Custom GPT Tools Result Display Options: Users can now select how results from custom GPT tools appear in webchat — either displayed in cards or as plain text in the Edit Custom GPT Tools page.
- New SeaChat Conversation Handling Mode: Users can choose how chats with customers are managed, the three modes are:
  - Hybrid Mode: The AI agent handles interactions initially, but users can request a live agent transfer when needed.
  - AI Agent Only: The AI agent independently manages all chats.
  - Human Agent Only: Human agents handle all conversations exclusively, and this mode is LIFE-TIME FREE.
- Updated Webchat Menu Card Behavior for Text Messages: When users click on a menu card, the card name will be sent as a message from the user, and the bot will respond with the complete canned message stored within the card. The behavior for cards with URLs remains unchanged.

### 10/31/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Automate Actions with Custom GPT Tools: This new feature enables the SeaChat AI agent to query a user’s API endpoint and perform custom actions based on defined conditions. GPT will trigger these actions automatically at the right time.
- "Memory" Renamed to "Extraction": The "Memory" feature in the AI agent's Advanced Settings page is now called "Extraction," with no changes to its functionality.
- Enhanced Workspace List for Better Quota Management: Users will now see their workspace dashboard showing two lists of workspaces. One is Active Workspaces, which shows the number of workspaces created by the user (first number) and the workspace limit allowed under the user's plan (second number). The other is Joined Workspaces, which displays workspaces owned by other users that the current user has joined.

### 10/17/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Display Unread Conversation Count: Users will now see two distinct notifications in the conversation tab and they can hover over each conversation count to understand its purpose. The left number shows the total unread messages. The right number displays unread messages assigned specifically to the user, ensuring agents can easily identify their responsibilities at a glance.
- Enhanced AI Understanding with Postback Button Content: Your AI agent will now have access to the content of buttons clicked by your customers. This ensures that the AI agent can accurately respond to follow-up queries.
- Improved Customization Options for Webchat Forms and Menu Cards: Users can now customize the text display in the submit button in custom forms. Users also have options to enable menu cards to be always-on. Additionally, menu cards support sending a text to AI agent on click besides redirecting to an URL, and there’s now an option to remove pictures for menu cards.

### 10/15/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Enhanced Upload Progress Indicator: We’ve improved the UI by adding upload progress indicators, allowing users to see exactly which URL or sitemap is being processed in real-time.
- SeaChat Widget and Mobile Layout Enhancements: When users click the webchat widget icon, the AI agent's webchat will now open in full screen within the current tab. Additionally, layout issues on mobile screens have been resolved, ensuring the webchat is fully displayed in full screen on users’ phones.

### 10/03/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Human-Agent Assignment: This feature introduces a streamlined interface that allows users to easily assign human agents to respond to customers. Additionally, a new filter has been added to help users quickly locate conversations that have been assigned to them.
- Billing Usage Page Enhancements: The Billing -> Usage page has been upgraded. Users can now see the model and usage information for text and voice messages.
- Conversation Title Consistency: The conversation title now consistently aligns with the user’s full name, ensuring greater accuracy in how conversations are displayed.
- Messenger Interaction Flow: It has been improved to ensure that a quick reply is sent after every message, resulting in smoother and more efficient communication.

### 09/27/2024

##### **<font color="#739963">New Features and Improvements</font>**

- AI Agent Time Awareness: For every message, the AI agent will now be aware of the current time, such as: "The current time is 9:41 AM, September 11, 2024, Wednesday, PST timezone." This allows the AI agent to respond more accurately to user queries about business hours and other time-related questions.
- SeaX Integration Page Redesign: The SeaX integration page has been redesigned to enhance the user experience.

##### **<font color="#d66a60">Bugfix</font>**

- Webchat Icon Clickability: Fixed an issue where the webchat widget installation code caused the webchat icon to be unclickable.

### 09/20/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Language Support: Added additional language support, including French, expanding the localization capabilities of SeaChat. This update enhances user experience for multi-language environments.
- Annual Payment Plan: Users can subscribe to a newly introduced annual payment plan, providing more flexible billing choices and the ability to save on long-term commitments.
- Export Conversation History: Users can now export their conversation history data for their own analytics or admin management purposes, offering more control over their communication data and insights.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed Messenger Live Agent Transfer Issue: Resolved an issue with the Facebook Messenger live agent transfer quick reply button functionality, ensuring smooth transitions between AI and human agent responses.

### 09/11/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Messenger Cards Support : You can now enhance user interactions on Messenger with buttons featuring canned messages and cards with images and buttons, offering a richer, more dynamic experience for your audience.
- Image Support Across Platforms: SeaChat Webchat, WhatsApp, and LINE integrations now support sending and receiving images, enabling more visual and engaging communication across all platforms.
- Analytics Page: Our new Analytics page is now available to all users. Easily track your AI agent’s activities and gain deeper insights into performance and interactions.
- Email Preferences for Human Agents: Human agents can now configure their email preferences to receive email notifications, ensuring a more customized and efficient workflow.

### 09/04/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Enhanced Knowledge Base Search: The search functionality for existing knowledge base articles now uses the same strategy as RAG search method, improving search accuracy and efficiency.
- Support for WebP Format: You can now upload WebP format images to use as icons, allowing for more flexible image options.
- Google Calendar Integration: Users can now select which Google Calendar to book appointments, providing more control over scheduling.
- Customizable Webchat Widget Icon: You can now personalize your webchat widget by uploading any image as the widget icon, giving you more customization options.
- Simplified Webchat Widget Installation: The webchat widget installation code block has been updated in all integrations page. You can now easily copy and paste one code block to install multiple widgets to your integration channels.

### 08/28/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Message Quota Management: Users can now set specific quotas in the Advanced Settings page for the number of chat and voice messages an AI agent can send.
- Enhanced SeaX Calls Integration Page: Features improved control over call speed and voicemail settings.
- Updated UI with New Tabs Style: Streamlined navigation with a fresh tabs design, enhancing user interface interaction.
- LINE Live Agent Message Cap Notification: Notifications are now sent in SeaChat when the message sent by live agent through SeaChat to LINE approaches LINE’s limit.
- Increased Character Limit for Agent Descriptions: Agent descriptions can now include up to 3000 characters, allowing for more detailed explanations.
- Simplified Onboarding Process: New users can build their first knowledgeable AI agent by uploading just a small file or a website URL.

### 08/21/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Easily Copy KB ID: Now you can quickly copy the Knowledge Base ID from file’s right menu and use it as button content.
- Enforced Memory Fields Character Limit: Memory fields now have a strict character limit of 1024.
- Knowledge Base Quota Page: Introducing Quota page for knowledge base that helps you track and optimize your document and token usage efficiently.
- Updated Tab Styles: Enjoy a refreshed look with brand-new tab styles for a more intuitive and modern interface.

##### **<font color="#d66a60">Bugfix</font>**

- Correct Chat Participant Names in Emails: Fixed an issue where a random value was shown instead of the correct chat participant’s name in the "New message received" email.

### 08/15/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Easy Agent Replacement: The new one-click feature in the agent management page simplifies version control and agent duplication, making the process more convenient.
- Improved Test AI Agent Access: The 'Test AI Agent' button has been relocated to the header for easier and more convenient access.
- Expanded Context Window: Open a 128K context window for advanced large language models such as GPT-4o, GPT-4o mini, and Mistral Large.
- Enhanced Button Content Management: Use the `$KB_ID_` header and KB document IDs as button content for streamlined access to knowledge base articles directly through button interactions.

### 08/08/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Introduced a Card-Style Agent Listing Page: Experience our newly designed layout for a more visual and organized way to browse agents.
- Added Model Switching Capability: Users can now switch between different large language models, including GPT-4o mini, GPT-4o, and Mistral Large, directly from the interface.
- Customizable Automatic Transfer Back to AI Agent: Automate the transfer back to the AI agent after a customizable minutes of inactivity from a live agent.
- Customizable "Live Agent Has Left the Conversation" Message: User can design the message that appears when a live agent exits the chat.
- Enabled Customization of Live Agent Transfer Phrases: Allow users to set specific phrases that trigger the seamless transfer of a conversation from the AI agent to a live agent.

### 08/01/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Enhanced Widget Installation: Easily install multiple widgets for SeaChat AI Agent web chat, LINE, WhatsApp, and Messenger on your website by simply copying and pasting one code snippet.
- Improved Popup Window: Experience a more user-friendly popup window that helps you easily track when hit Knowledge Base quota limit.
- Enhanced Browser Notifications: New notifications on the browser tab make unread messages more noticeable.
- Advanced Twilio Call Settings: Configure speed adjustments for both inbound and outbound calls, with options for outbound voicemail to either send a customizable voicemail message or automatically hang up.

### 07/25/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Knowledge base limitations: Upload limits are now tailored to specific plans, including restrictions on file size, file count, and token count.
- Improved Plan Downgrade Process: Users receive notifications advising them to remove excess agents, files, and workspace members. This allows for necessary cleanup before the downgrade takes effect.

### 07/19/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Added support for playing and downloading audio recordings
- Premium Plan Feature: Option to enable Memory is only available for Premium Plan
- Premium Features Tips: New tips for managing multiple premium features, including adding additional members, AI agents, workspaces, memory, and setting up voice agents
- Plain text URLs are now clickable in webchat

### 07/11/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Create workspace automatically when onboarding new users
- Allow Premium plan to hide Seasalt.ai SeaChat branding message in Agent design styles

### 07/04/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Agent list page: To make the screen consistent, only display the first row of prompts.
- SeaChat landing page now supports Portuguese, Korean, Russian, Spanish, and Vietnamese.
- Added a new TTS voice for Chinese: Tongtong voice.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed AI Agent design style cannot be saved bug.

### 06/26/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Now users can create workspace in one click
- Label conversations with channel icon
- Improve the UI of Table upload options
- The number of free messages in the free plan has been revised to 100 messages life-time usage

### 06/13/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Supports LINE card messages and button messages, enriching your conversations.
- Enhanced User Experience: Improved behavior of adding buttons to lists.
- Message Response Support: Supports URL and Markdown formats.

### 06/06/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Interface Adjustment: Added design styles to AI Agent information, allowing you to better design the dialogue interface.
- New WordPress Integration: You can now deploy your AI Agent on WordPress.
- New MailerLite Integration: You can now sync contact information to MailerLite integration.
- New Integration Pages and Channel Design: Offers new integration options and improved channel designs.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed Several Knowledge Base Errors: Including issues with deleting knowledge bases and document error messages.

### 05/30/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Knowledge Base Files: Now you can directly overwrite files with duplicate names, making it easier to update documents.
- New Refresh Button for Chat Window: You can click the button to refresh the chat window when WebSocket is disconnected.

##### **<font color="#d66a60">Bugfix</font>**

- Bug Fixes in Workspace Creation: Errors encountered during workspace creation have been resolved.

### 05/24/2024

##### **<font color="#739963">New Features and Performance Improvements</font>**

- Database Update: Improved file naming in the database for better visibility of documents.
- Automatic Overwrite: When uploading files with duplicate names, you have the option to overwrite the existing files for updates.
- Optimized Database Switching: Enhanced the fluidity of switching databases.
- Customer Service Access: We have added a customer service portal on the left side of our service interface. If you have any questions, you can contact us anytime. Providing the best experience is our greatest motivation.
- Email Template Modification: For SeaChat emails, we've modified the email templates to simplify how you view your emails.

### 05/18/2024

##### **<font color="#739963">New Features</font>**

- Added mail language settings to make email notifications more readable (now you can receive chat email notifications from `seachat@seasalt.ai`).
- Introduced RAG (Retrieval-Augmented Generation) with new query modes, retrieval methods, and retrieval counts to enhance data retrieval and AI assistant response accuracy.
- Added automatic clearing of Memory information when a user clears a conversation.

##### **<font color="#739963">New Features</font>**

- Fixed issues with uploading CSV and Excel files, addressing upload failures and blank screen problems.
- Repaired missing Knowledge Base data and related answers.
- Fixed issues with reply messages containing broken links.
- Corrected strings and updated the use-case library.

### 05/02/2024

##### **<font color="#739963">New Features</font>**

- Upload Table Optimization: On the upload table page, users can now choose whether to upload each row in a table file as an individual Knowledge Base document or as a single file.
- Added Wix Channel: You can now deploy your Agent on Wix.
- Database Enhancement: Restructured Knowledge Base data for optimized data retrieval and interpretation.
- Interface Optimization for Shopify and Squarespace Channels: Enhanced user interface for more streamlined operations for these integrations.
- Automatically fill out bot description for the Survey use case.
- Fixed Live Agent Transfer Behavior in the Survey use case.

### 04/19/2024

##### **<font color="#739963">New Features</font>**

- Added Use Case Library Page: Makes it easier for you to create AI Agents efficiently.
- Access to customer email information: You can now quickly copy customer emails directly from the conversation history list.
- Updated WhatsApp/Messenger Setup Token Process: Improve the channel binding experience.
- Introduced "Memory": Records key information from historical conversations. Paired with the Survey Use Case, it helps you research user needs and characteristics through dialogue.

### 04/09/2024

##### **<font color="#739963">New Features</font>**

- Added `remove` button for WhatsApp and Meta Facebook Messenger channels, allowing users to unlink accounts easily.
- Display the end user's email upon completing the form, enhancing user tracking and engagement.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed an error in the process of creating agents, streamlining agent creation.
- Resolved bugs related to editing agents, ensuring smoother modifications and updates.

### 04/02/2024

##### **<font color="#739963">New Features</font>**

- New portal for creating agents, simplifying the bot creation process.

##### **<font color="#d66a60">Bugfix</font>**

- Improved WhatsApp responses to reduce cases of incorrect or garbled replies.
- Enhanced AI Agent responsiveness, addressing issues of stalling or failure to respond.

### 03/28/2024

##### **<font color="#739963">New Features</font>**

- New Social Media Channels Supported: Added Meta Facebook Messenger and WhatsApp channels, expanding communication platforms for Agents.
- New Website Integration Support: You can use SeaChat on [Shopify](https://wiki.seasalt.ai/seachat/seachat-manual/05-integrations/02-seachat-shopify-integration/) and [Squarespace](https://wiki.seasalt.ai/seachat/seachat-manual/05-integrations/03-seachat-squarespace-integration/).
- New Use Cases: Introduced 5 new use cases, making Agent creation more convenient and focused.
- Login Process Optimization: Simplified registration with Google accounts.

##### **<font color="#d66a60">Bugfix</font>**

- Support for LINE stickers, enhancing the response experience for customers.
- Added `/live_agent` transfer feature in WhatsApp and Meta Facebook Messenger.
- Fixed incorrect Live agent status display.
- Corrected the issue where Live Agent sends incorrect messages.

### 03/14/2024

##### **<font color="#739963">New Features</font>**

Language Model Optimization:

- Upgraded SeaChat Agent model
- Enhanced appointment scheduling prompt improvements.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed random language summaries.

### 03/07/2024

##### **<font color="#739963">New Features</font>**

- Knowledge Base: Now supports Video, Audio, and Spreadsheet files, enabling more comprehensive content sharing and collaboration.

##### **<font color="#d66a60">Bugfix</font>**

- Extended support for longer video and audio files, with a maximum duration of 15 minutes.
- Fixed bug in uploading spreadsheets.
- In members setting, payment no longer prompts when adjusting AI Agent assignments.

### 03/04/2024

##### **<font color="#739963">New Features</font>**

- KnowledgeBase - Spreadsheet Upload: Now you can upload spreadsheets directly to the knowledge base
- KnowledgeBase - Video and Audio Uploads: Enhance your knowledge base with multimedia by uploading video and audio clips.
- You can now download invoice from billing history

### 02/23/2024

##### **<font color="#739963">New Features</font>**

- Email notifications for live agent requests and new conversations
- Users can switch between AI Agent and live human agent

##### **<font color="#d66a60">Bugfix</font>**

- Reduce new workspace creation time significantly

### 01/24/2024

##### **<font color="#739963">New Feature</font>**

- Preferred Response Language: Now you can set the default response language in the "Agent Information" menu. SeaChat will ensure the quality of your assistant's responses

<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/20240124-preferred-response-lang.png" alt="Set up a separate text channel just for live transcriptions from SeaVoice STT.">
</center>

##### **<font color="#d66a60">Bugfix</font>**

- Webchat Widget Preview: fix color mismatch bug in webchat widget preview
