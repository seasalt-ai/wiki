---
title: "Agent Duplication and Replacement"
description: "Learn how to efficiently duplicate and replace AI agents in SeaChat. This guide covers creating new agents based on existing ones for seamless testing and development, and managing different agent versions to streamline your production workflow."
lead: "Explore SeaChat's powerful agent duplication and replacement features, designed for creating and managing different versions of your AI agents. Perfect for prototyping, testing, and smoothly transitioning from development to production."
date: 2024-07-10T08:48:45+00:00
lastmod: 2024-07-10T08:48:45+00:00
weight: 31
draft: false
images: []
toc: true
aliases:
  - /en/seachat/seachat-manual/02-create-agent/03-agent-duplication-replacement
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

## Agent Replacement

The agent replacement feature provides an efficient way to manage different versions of your agent.

This is particularly useful when you want to develop an existing agent without affecting the original version. By using this feature, agent editors can make changes to a copy of the original agent rather than modifying the original agent directly.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/create-a-new-agent/replace-button.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/create-a-new-agent/replace-button.png" alt="">
</a>

**Agent Replacement**
</center>

A common use case might look like this:

1. Duplicate the original Agent A and name the copy Agent B (Agent A Copy).
2. Add new features to Agent B and test them.
3. Once development is complete, replace Agent A with Agent B.
4. Now, the new agent is running in production with the original settings from Agent A and the new features implemented in Agent B.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/create-a-new-agent/replacement-workflow.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/create-a-new-agent/replacement-workflow.jpg" alt="">
</a>

**Agent Replacement Workflow**
</center>

By following this process, you can keep the original agent running in production while developing and testing a new version of the agent.
