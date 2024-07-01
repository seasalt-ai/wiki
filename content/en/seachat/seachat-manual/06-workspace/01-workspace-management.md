---
title: "Workspace Management"
description: "SeaChat Workspace Management"
lead: ""
date: 2020-10-06T08:48:45+00:00
lastmod: 2024-06-27T08:48:45+00:00
weight: 61
draft: false
images: []
aliases: 
  - /en/seachat/seachat-manual/workspace/01-workspace-management
  - /seachat/seachat-manual/workspace/01-workspace-management
---




## Agents

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/agents.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/agents.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent Management</p>
</div>

This is where you can manage all your AI agents. Each row represents an agent and its name, email, and status. You can also see the number of unread message. Find the URL to the agent conversation, launch the conversation directly, or add new agents here.

## Members

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/seachat-manual/workspace/01-workspace-management/members.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/members.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Members Management</p>
</div>


There are different types of members. According to the type of the membership, member will have accoess and permission. If you are the owener of a workspace, you can add new members to your workspace and assign different roles to them. Here are some of the roles you can assign to a member:

1. **Admin**: Admins have full access to the workspace and can manage all the settings. They can edit the AL agents' settings, manage the knowledge base, access the agent conversation and take over conversations as human agent.
2. **AI Agent Editor**: AI Agent Editors can edit the AI agents' settings, manage the knowledge base, and access the agent conversation and testing.
3. **Human Agent**: Human Agents can access the agent conversation and take over conversations as human agent.

### Agent Assignment

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/seachat-manual/workspace/01-workspace-management/add-member.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/add-member.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Member Settings</p>
</div>

You can assign different agents to different members. For instance, a good practice will be assigning the testing agents to your AI agent editors and agents in production to your human agents. Whereas the admin can have access to both types of the agents for monitoring and controls.


## Workspaces Preferences

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/preference.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/preference.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Preference Settings</p>
</div>

Here is where you can manage the notification settings of your workspace. SeaChat can automatically send you emails to notify you about new conversations and new live agent requests. After enabling the types of notifications you want to receive, you can also set the language of the notifications.


### Notification Settings


SeaChat provides different languages for the notifications. You can choose the language you want to receive the notifications in. Although you can set the language to default(Same with Apprearance Language), we recommend setting the language to a predetermined one that have been provided to you. Since this can help optimize the performance of the agent and speed up operation.

## Workspace API Keys

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/workspace-api.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/workspace-api.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">SeaChat Workspace API</p>
</div>


If you wish to access your workspaces or agents programmatically, you can use the API key found under your **Workspace**. You can generate new API keys, view the existing ones, and delete them here. Please make sure to set up the two following prerequisites before using the API key:

1. Workspace Creation: If you haven't already, create a workspace in SeaChat and note down the workspace ID from the URL, which follows the format: `https://chat.seasalt.ai/gpt/workspace/{workspace-id}/bot/{bot-id}/`.
2. Access Credentials: Obtain your Client ID and Access Token by reaching out to seachat@seasalt.ai. These credentials are essential for authenticating your API requests. This is where you can apply the access token in the **API Keys** section of your workspace settings. 

SeaChat API uses Bearer Authentication methods, Therefore, your must apply your bearer token in the header of your API requests. For example, if you are using curl, you can use the following code snippet to authenticate your API requests:

```curl
curl -X 'POST' \
  'https://chat.seasalt.ai/api/v1/public/bots' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer [access token]' \
  -H 'Content-Type: application/json' \
  -d '{
    "workspace_id": "XXXXX-XXX-XXXXXXXXX",
    "name": "SeaChat",
    "description": "string",
    "use_case": "Customer Service",
    "live_agent_transfer": false,
    "default_response_language": "default",
    "is_enabled": true
  }'
```

SeaChat API is an in-depth tool that allows you to access your workspace and agents programmatically. You can use the API to create new AI agents, manage existing agents, and access the conversation history. For more information on the SeaChat API, please refer to the [API documentation](https://chat.seasalt.ai/redoc). Or contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai)



