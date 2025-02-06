---
title: "Conversations"
description: "Manage customer interactions with Conversations board. Access details, history, and download audio files."
date: 2024-07-30T08:48:57+00:00
lastmod: 2024-07-30T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /en/seachat/seachat-manual/seachat-agent-conversation/
url:  /en/seachat/manual/conversation/
weight: 104
toc: true
---

## Conversation Dashboard
The conversation dashboard is where you can view and manage all the conversations that your agents are handling. You can view the details of each conversation, check the conversation history, and manually answer users' questions.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/seachat-conversation/conversation-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/seachat-conversation/conversation-dashboard.png" alt="Conversation Dashboard | Agent Conversation">
</a>

**Agent Conversations View**
</center>



Users can switch between all conversations and live agent conversations. In live agent conversations, users can view conversations that have been handled by live agents.

In each conversation row, there will be an icon indicating the conversation channel e.g. WhatsApp, phone calls etc. You can easily identify the communication channel of conversation through these icons.

## Download Audio Conversation

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/seachat-conversation/download-audio.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/seachat-conversation/download-audio.png" alt="Download Audio | Agent Conversation">
</a>

**Download Audio Conversations**
</center>

For conversations with phone icons, you can download the audio conversation by clicking on the download icon inside the conversation. The audio conversation will be downloaded in `mp3` format. This is a useful tool for quality assurance and training purposes, as you can listen to the conversation between the agent and the user and provide critical feedback to fine-tune the agent's responses.

## Download Agent Conversation History

If you wish to download the conversation history of certain agent conversations, you can do so by navigating to **Workspace*  - `-> **Agents**. 

Click on **Download Conversations*  - `and Choose the year of the conversation history you wish to download. 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/seachat-conversation/download-conversation-history.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/seachat-conversation/download-conversation-history.png" alt="Download Conversation History | Agent Conversation">
</a>

**Download Conversation History**
</center>

This process might take a while depending on the size of the conversation history. Once the download is ready, you will receive a system notification says `AI agent conversation history export successful. Please click link or copy the link to browser to download. The link will expire in 24 hours.`

Click on the link to download the conversation history in a zip file format. 

You will see the conversation history in a CSV file format. The CSV file contains the following columns:

| Sender type | Channel type | Sender name | Time in GMT | Message | Data |
|-------------|--------------|-------------|-------------|---------|------|

- **Sender type**: The type of sender. You can identify whether the sender is the agent, system notification, user, etc.
- **Channel type**: The communication channel of the conversation. The following is the list of channel types:
   - `System (this means system message)`
   - `WebChat`
   - `SeaAuth (this is usually for verification purpose)`
   - `Line`
   - `WhatsApp`
   - `Messenger`
   - `Instagram`
   - `Voice (this means phone calls)`
   - `ThirdPartyClient`
   - `AgentPhone (this means phone calls from SeaChat voice agent, usually for token verification purposes)`
   - `SeaX_Call (this means phone calls through SeaX)`
   - `SeaX_SMS (this means SMS through SeaX)`
- **Sender name**: The name of the sender. You will find the senders' ID or Email in this column if the sender is an actual user. Otherwise, it will be an identifier from the system.
- **Time in GMT**: The timestamp of the message in GMT format.
- **Message**: The message content of the conversation. Most of the time, this field contains plain text messages. However, it can also include specific command types, such as:
   - `/live_agent:  User requests conversation transfer to a live agent.`
   - `/submit_form: User submits a form. If an entity is involved, the command will appear as /submit_form{"entity_name":"entity_value"}.`
   - `/clear_history: User requests the bot to forget the conversation history and start fresh.`
   - `/ai_agent: User requests conversation transfer to an AI agent.`
- **Data**: The data content of the conversation in JSON format. This column will be empty if there is no data content in the conversation. When data is present, it can include, but is not limited to, the following types:
   - `Image URL that gets sent in the message.`
   - `Recording file URL of the voice call.`
   - `A form that the user completes during the chat.`
