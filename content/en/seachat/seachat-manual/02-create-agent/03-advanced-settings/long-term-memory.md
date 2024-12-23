---
title: "Long-Term Memory"
description: "Learn how to enable and configure Long-Term Memory in SeaChat for persistent user context and personalized conversations."
lead: ""
date: 2024-12-16T00:00:00-07:00
lastmod: 2024-12-16T00:00:00-07:00
weight: 80
draft: false
images: []
toc: true
url: /en/seachat/manual/create-agent/advanced-settings/long-term-memory/
---

## Overview

Long-Term Memory in SeaChat allows agents to retain persistent user context across conversations, enabling more human-like, personalized, and context-aware responses. This premium feature is essential for use cases like marketing, sales, and customer service, where remembering user preferences and past interactions is crucial.

For example, a user might ask, "What do you know about me?" With Long-Term Memory enabled, the AI agent can recall and respond with detailed information from previous conversations, like hobbies, preferences, or travel plans.

THe following guide explains how to enable and use Long-Term Memory in SeaChat for and example use case and management tips.

## Video Tutorial:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/?listType=playlist&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=22" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

## Getting Started

Here’s a guide to enabling and using Long-Term Memory in SeaChat:

### Long-Term Memory

<br/>

<center>
<a href="/images/seachat/en/user-memory/activate-user-memory.png">
<img height="100%" width="100%" src="/images/seachat/en/user-memory/activate-user-memory.png"  alt="Activate Long-Term Memory Feature">
</a>

</center>

<br/>

To enable Long-Term Memory:

- Navigate to **Agent Configuration** ➔ **Advanced Settings**.

- Enable the Long-Term Memory feature.

- Save your changes.

## How It Works

When Long-Term Memory is active, SeaChat will automatically save key facts about users during conversations, like their preferences, past questions, and relevant interests. 

When a user returns, even after a long time, SeaChat can recall this information, creating a more seamless and tailored interaction.

## Example Use Case

***Initial Conversation***

<br/>

<center>
<a href="/images/seachat/en/user-memory/conversation-1.png">
<img height="100%" width="80%" src="/images/seachat/en/user-memory/conversation-1.png"  alt="Long-Term Memory Example | Conversation 1">
</a>

</center>

<br/>

***Follow-Up Conversation***

<br/>

<center>
<a href="/images/seachat/en/user-memory/conversation-2.png">
<img height="100%" width="80%" src="/images/seachat/en/user-memory/conversation-2.png"  alt="Long-Term Memory Example | Conversation 2">
</a>

</center>

<br/>

***Updated Preferences***

<br/>

<center>
<a href="/images/seachat/en/user-memory/conversation-3.png">
<img height="100%" width="80%" src="/images/seachat/en/user-memory/conversation-3.png"  alt="Long-Term Memory Example | Conversation 3">
</a>

</center>

<br/>

With each interaction, the agent dynamically updates the user profile, retaining both past and new preferences.

## Managing Long-Term Memory

<br/>

<center>
<a href="/images/seachat/en/user-memory/option-btn.png">
<img height="100%" width="100%" src="/images/seachat/en/user-memory/option-btn.png"  alt="Long-Term Memory Option Button">
</a>

</center>

<br/>


Supervisors can manage Long-Term Memory in the Conversations section:

- Select the desired user conversation.

- Click the **Long-Term Memory** option (three dots).

- View, update, or erase the user’s memory.

> Tip: Use this feature to segment users, deliver targeted marketing messages, or provide tailored support.

### Resetting Memory

<br/>

<center>
<a href="/images/seachat/en/user-memory/delete-memory.png">
<img height="100%" width="100%" src="/images/seachat/en/user-memory/delete-memory.png"  alt="Delete Long-Term Memory Permanently">
</a>

</center>

<br/>

For testing or privacy purposes, you can reset Long-Term Memory:

- Select the desired user conversation.

- Click the **Long-Term Memory** option (three dots).

- Select **Erase All** for the user.

> Warning: Resetting memory is irreversible and will remove all stored context.


### Conversation History Turn

SeaChat retains up to 20 conversation turns by default. Long-Term Memory extends this limit indefinitely, allowing agents to remember user context over extended periods.

However, this means if the users wishes to disable the Long-Term Memory feature, it will only prevent the AI agent from remembering any user context. To completely remove the effect of context, users should also set the **Conversation History Turn Count** to 0 to prevent the AI agent from remembering any conversation history.

Here are the steps to modify the **Conversation History Turn Count**:

<br/>

<center>
<a href="/images/seachat/en/user-memory/conversation-turn.png">
<img height="100%" width="100%" src="/images/seachat/en/user-memory/conversation-turn.png"  alt="Context | Conversation History Turn Count">
</a>

</center>

<br/>

- Navigate to **Agent Configuration** ➔ **Advanced Settings**.

- Click on **Context**.

- Set the **Conversation History Turn Count** to 0.


## Additional Notes

- Default Context Limit: SeaChat retains up to 20 conversation history turns by default. Long-Term Memory extends this limit indefinitely.

- Privacy Compliance: Long-Term memory is securely stored and can be erased at any time to ensure data privacy compliance.

- Applications: Ideal for customer profiling, personalized marketing, and enhancing user experiences.


## Conclusion

Long-Term Memory transforms SeaChat into a smarter, more personalized AI assistant by retaining user context over extended periods. Whether for sales, customer support, or small talk, this feature ensures your AI agent remembers what matters most to your users.
