---
title: "Agent Duplication"
description: "Learn how to efficiently duplicate AI agents in SeaChat, allowing you to create new agents with similar settings for streamlined testing and optimization."
lead: "Discover the power of SeaChat's agent duplication feature for creating new agents based on existing settings, perfect for prototyping and optimizing your AI agents."
date: 2024-07-10T08:48:45+00:00
lastmod: 2024-07-10T08:48:45+00:00
weight: 20
draft: false
images: []
toc: true
aliases:
  - /en/seachat/seachat-manual/02-create-agent/03-agent-duplication
---

## Agent Duplication

Agent duplication is a feature that allows you to create a new agent based on an existing agent. This feature is useful when you want to create a new agent with similar settings as an existing agent.

To duplicate an agent, click on the **Agent Duplicate** button located next to the agent you want to duplicate in **Agents** under **Workspace**. This will create a new agent called **{Agent Name} (COPY)** with the same settings as the original agent. You can then modify the settings by clicking on **Edit** or simply go to **Agent Information**.

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/create-a-new-agent/agent-duplication-btn.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
      <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/create-a-new-agent/agent-duplication-btn.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Duplicate Agent Button</p>
  </div>
</div>

<br/>

This feature is very powerful for agent editors in prototyping new agent settings and separating development and production agents for testing and optimization.

This process might take some time based on the complexity of the agent. Once you see the success message, you can start training your agent. Everything is set up, including the available knowledge base and agent information.

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/create-a-new-agent/duplication-confirmation.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
      <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/create-a-new-agent/duplication-confirmation.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Duplication Confirmation</p>
  </div>
</div>

<br/>

For users with integrations or channels connected to the original agent, you will need to update the integration to include the new agent copy since the agent copy is still a new agent.
