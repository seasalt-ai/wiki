---
title: "Agent Memory"
description: "Memory tutorial"
lead: ""
date: 2024-04-26T08:48:45+00:00
lastmod: 2024-04-26T08:48:45+00:00
weight: 80
draft: false
images: []
toc: true
---

# Overview

Memory allows users to intuitively define the most important aspect of the conversation to keep dialogue relevant and to aid in objectively determining the conversation outcome. In this document we'll conver:

- Designing memory fields and descriptions for Bots to extract for each conversation.
- Monitor extracted values for each conversation.
- Modify Bot memory fields and Conversation memory through the api.


# Set up Memory in Bot Advanced Settings

In this section we'll go through how to effectively set up Memory fields for your bot.

## General Setup (For non-Survey use cases)

For most bots, to set up memory we'll use the provided UI in the **Advanced settings** section.

1. In the **Agent Information**, head to the **Advanced Settings** section at the top right.

   [comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/d4261fc5-2b20-4f65-a264-ade4d9266d3a)


<center>
<a href="/images/product-updates/seachat/en/memory/general-setup.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/general-setup.png" alt="">
</a>

<br/>

*Agent Information → Advanced Settings*
</center>

<br/>

2. Create desired fields in the sections provided:
    - **Field**: The name of the memory "variable" we want to extract
        - Make this name intuitive. Ideally you should know what this field is monitoring for based on the name.
    - **Content**: The default value for this memory field
        - This is the starting value for the memory field. This will usually be empty.
    - **Description**: The definition of the field
        - In natural language, describe what this field is and what type of value to extract.
        - Be descriptive yet concise here. This can greatly affect extracted values.
      
<br/>

3. Add or remove fields as necessary using the plus (add) and minus (remove) icons on the right side of the page

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/621eaa33-78a9-45d4-8597-07deda70b141)

<center>
<a href="/images/product-updates/seachat/en/memory/add-and-remove.png" target="_blank">
<img width="20%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/add-and-remove.png" alt="">
</a>

<br/>

*Plus (Add) and Minus (Remove)*
</center>

4. Finally, save your memory settings by clicking the save button at the bottom.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/7220ada1-b2e3-4353-9052-c49d45225bd8)

<center>
<a href="/images/product-updates/seachat/en/memory/save-setting.png" target="_blank">
<img width="40%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/save-setting.png" alt="">
</a>

<br/>

*Save Your Memory Settings*
</center>


## Memory setup for Survey Use Cases

For the survey use cases (CSAT, Brand Perception, Market Research, etc.), the memory pane in Advanced Settings will be dynamically set from the description section

1. By selecting one of these use cases, the description section will contain a blank question section (for base survey use case) or a pre-filled question section (templated surveys such as CSAT).
    - This section is denoted by **//QUESTIONS START** at the top and **//QUESTIONS END** at the bottom.
    - The format is ONE question per line with ALL question in between **//QUESTIONS START** and **//QUESTIONS END**.
    - Feel free to add, remove, or alter the questions.

> :rotating_light: NOTE :rotating_light:
> 
> DO NOT modify the **//QUESTIONS START** and **//QUESTIONS END** tokens. These are crucial to properly populate the memory field for this use case

2. After setting up the description and question section, press the save button at the bottom.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/9b59ff3a-04aa-44c7-83a8-2cd02fe13f78)

<center>
<a href="/images/product-updates/seachat/en/memory/question-start.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/question-start.png" alt="">
</a>

<br/>

*Question Section*
</center>

3. Head over to the Advanced Settings tab to make sure the fields are properly set.
    - NOTE: Do NOT change any section in the memory pane when using Survey use cases. If you need to make a change to the questions use the description page.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/aa6a0fda-3e34-4271-9010-28305d9cd296)

<center>
<a href="/images/product-updates/seachat/en/memory/advanced-settings.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/advanced-settings.png" alt="">
</a>

<br/>

*Advanced Settings*
</center>

# Monitor Conversation Memory

The memory for each conversation will update in real time and we can check the values from the Conversation page

1. Head to the Conversations page from the left hand side

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/00c4d418-879d-49a5-9ffc-a49972668ed7)

<center>
<a href="/images/product-updates/seachat/en/memory/conversation-page.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/conversation-page.png" alt="">
</a>

<br/>

*Conversations*
</center>

2. Find the desired conversation from the list and press the triple dot icon in the bottom right corner for that conversation.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/9be38868-cdbf-4223-a445-636695b8c922)

<center>
<a href="/images/product-updates/seachat/en/memory/memory-btn.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/memory-btn.png" alt="">
</a>

<br/>

*Click on **Memory***
</center>

3. Pressing "Memory" will bring up the latest extracted values for that conversation

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/5872958e-9b35-4ad7-93c2-50ac2a50f81f)

<center>
<a href="/images/product-updates/seachat/en/memory/extracted-value.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/extracted-value.png" alt="">
</a>

<br/>

*Latest Extracted Values*
</center>

## Advanced Memory Use

In this section we will go over using the API to get and update the memory for bots and conversations.
Warning: This is intended for advanced users only. Improper usage may break the memory extraction for future conversations.

# Getting Bot Memory

`GET /api/v1/workspaces/{workspace_id}/gptbots/{bot_id}`

Querying this endpoint will allow you to get the memory settings for the bot. That is the desired fields and default values that will be extracted for future conversations. Here is an example response:

``` JSON
{
  "name": "Test bot",
  "description": "You are a test bot",
  "use_case": "Customer Service",
  "live_agent_transfer": false,
  "default_response_language": "default",
  "memory": "{\"product\": {\"content\": \"null\", \"description\": \"The product the user is interested in.\"}, \"max_cost\": {\"content\": \"null\", \"description\": \"The maximum amount the user is willing to spend\"}",
  "kb_index_number": 2,
  "is_enabled": true,
  "appointment_scheduling": {
    "enabled": false,
    "type": "None",
    "calendar_args": {},
    "refresh_token": null
  },
  "id": "1c0b0d6d-5e9f-4cf5-a22c-143c264cbb23",
  "workspace_id": "ffffffff-abcd-4000-0000-000000000000",
  "is_deleted": false,
  "kb_index": "seachat-gpt-bot-1c0b0d6d-5e9f-4cf5-a22c-143c264cbb23-kb",
  "coach_enabled": false,
  "coach_task": null,
  "conversation_config_id": "97f8c61578c242358c8c7bd733d48b2f",
  "conversation_config_name": "Cody Test_default_config",
  "chat_window_url": "https://chat-dev.seasalt.ai/chat/97f8c61578c242358c8c7bd733d48b2f",
  "unread_number": 1
}
```

# Setting Bot Memory

`PATCH /api/v1/workspaces/{workspace_id}/gptbots/{bot_id}`

With this endpoint you can modify the bot memory. Changing this will update the fields to extract for future conversations

To only update the memory, an example request body will look like this, where memory is a JSON formatted string
``` JSON
{
  "memory": "{\"product\": {\"content\": \"null\", \"description\": \"the product of interest\"}, \"max_cost\": {\"content\": \"null\", \"description\": \"the maximum amount the customer is willing to spend\"}}",
}
```

The general format of the string is `{"FIELD 1": {"content": "null", "description": "DESCRIPTION OF FIELD 1"}, "FIELD 2": {"content": "null", "description": "DESCRIPTION OF FIELD 1"}}`, adding fields as needed. You will need to escape the double quotes in the request.

For example, this JSON string `{\"product\": {\"content\": \"null\", \"description\": \"the product of interest\"}, \"max_cost\": {\"content\": \"null\", \"description\": \"the maximum amount the customer is willing to spend\"}}` correlates to this memory setting


[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/d4261fc5-2b20-4f65-a264-ade4d9266d3a)

<center>
<a href="/images/product-updates/seachat/en/memory/json-advanced-settings.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/json-advanced-settings.png" alt="">
</a>

<br/>

*Memory Example*
</center>

# Getting Conversation Memory

`GET /api/v1/conversations/async/{conversation_id}`

Querying this endpoint will allow you to get the extracted memory for a particular conversation. Here is an example response where
we can see the memory field at the bottom.

``` JSON
{
  "user_id": "f5dcc11658f143b0bf6cf6114062dd73",
  "bot_url": "http://seasalt-ai-ngchat-seachat-gpt-master-bot-core/webhooks/rest/webhook",
  "agent_icon_url": null,
  "config_id": "f88446df0c16496d944278ad98ace580",
  "agent_id": null,
  "agent_listened": false,
  "bot_listened": true,
  "last_read_sequence": 3,
  "agent_last_read_sequence": 3,
  "status": "BOT_HANDLED",
  "is_unread": false,
  "id": "e6fd2003361d4257a943364d80063a69",
  "labels": [],
  "remark": null,
  "created_at": "2024-04-23T17:43:29.315241",
  "updated_at": "2024-04-24T17:21:08.292048",
  "ended_at": null,
  "user": {
    "id": "f5dcc11658f143b0bf6cf6114062dd73",
    "name": "Mature Ball 36c59624fa",
    "first_name": "Mature Ball",
    "last_name": "36c59624fa",
    "phone": null,
    "email": null,
    "channel_type": "WebChat"
  },
  "latest_message_time": "2024-04-23T17:43:38.778985",
  "workspace_id": "ffffffff-abcd-4000-0000-000000000000",
  "gptbot_id": "669d5f43-d1ae-4aef-aeda-cfce8204ea98",
  "channel_type": "WEBCHAT",
  "title": "Mature Ball 36c59624fa",
  "is_coach": false,
  "memory": "{\"product\": {\"content\": \"SeaX Enterprise\", \"description\": \"The product the user is interested in.\"}, \"max_cost\": {\"content\": \"\", \"description\": \"The maximum amount the user is willing to spend\"}, \"sequence\": -1}"
}
```

# Setting Conversation Memory
`PATCH /api/v1/conversations/async/{conversation_id}`

With this endpoint you can set the memory for a specic conversation. Changing this will change the memory extracted for that particular conversation.

NOTE: This endpoint should only be used to update the content of the memory. Do NOT change the fields or descriptions as these will be overwritten with the next interaction with the bot. It is highly recommended that you query the GET conversation endpoint above first to get the current memory fields.

For example, if you query the GET conversation endpoint and get the memory as

``` JSON
{
  "memory": "{\"product\": {\"content\": \"null\", \"description\": \"the product of interest\"}, \"max_cost\": {\"content\": \"null\", \"description\": \"the maximum amount the customer is willing to spend\"}}"
}
```
This result corresponds to a blank conversation memory:

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/2dd89961-88bc-4b26-82e6-6e5616d41194)

<center>
<a href="/images/product-updates/seachat/en/memory/empty-memory.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/empty-memory.png" alt="">
</a>

<br/>

*Empty Memory*
</center>


Here is an example request body to modify just the memory for a conversation
``` JSON
{
  "memory": "{\"product\": {\"content\": \"SeaX Enterprise\", \"description\": \"the product of interest\"}, \"max_cost\": {\"content\": \"null\", \"description\": \"the maximum amount the customer is willing to spend\"}}"
}
```

In the example above, this will set the conversation memory to:

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/5872958e-9b35-4ad7-93c2-50ac2a50f81f)

<center>
<a href="/images/product-updates/seachat/en/memory/setting-conversation-memory.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/product-updates/seachat/en/memory/setting-conversation-memory.png" alt="">
</a>

<br/>

*Conversation Memory*
</center>