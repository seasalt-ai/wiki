---
title: "Agent Information"
description: ""
lead: ""
date: 2024-04-26T08:48:45+00:00
lastmod: 2024-05-19T08:48:45+00:00
weight: 90
draft: false
images: []
toc: true
aliases:
  - /en/seachat/seachaat-manual/02-create-agent/03-agent-memory
---

# Overview

Agent information is the core of your AI agent. It contains all the necessary information about your agent, including its name, description, and other advanced settings like memory fields. In this tutorial, we will walk you through each of the parameters that you will find in **Agent Information** under **Agent Configuration**.

---

## Basic Setting in Agent Information

SeaChat allows you to configure your AI agent's information such as names, use case, and description. Inside **Basic Setting**, users can set the following parameters:

### Name
The name of your AI agent. This name will be displayed in the conversation window.

> :page_facing_up: **NOTE**
> 
> This will be the name of your agent for the purpose og agent management. If you wish to change the displayed name in your agent integration. Please refer to [Webpage Integration](/seachat/seachat-manual/04-channels/08-install-to-webpage/).


### Use Case
The use case of your AI agent. This will help you to categorize your AI agent. SeaChat provides a list of use cases to choose from. Depending on your needs, you can choose a use case that best fits your AI agent. Different use cases might require different description settings, but you can simply follow the instructions in the description section when incorporating a use case.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/memory/example-conversation.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/example-conversation.png" alt="image that display the use case options available in SeaChat">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Choose a use case for your AI agent</p>
</div>

### Description
A brief description of your AI agent that details your agent's behavior and its reference. Whatever you put inside the description field will show up in agent instructions on the right-hand side of the page. This description will then be used to prompt a language model to generate responses.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/memory/example-conversation.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/example-conversation.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent Description</p>
</div>

### Response Language
The language the AI agent will use to respond to the user. If the language that the agent will use is not definitive, you can choose **Always match user input language**. 

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/response-language.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/response-language.png" alt="image showcases the options of response language">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent's Response Language</p>
</div>

### Live Agent
The live agent feature allows a human agent to intervene in the conversation when needed. If you enable this feature, your customer will have the option to request a live agent during the chat conversation. This requires you to provide a real-human agent that will monitor and respond to the user. 

You can disable this feature by unchecking the box such that your user will not be able to make a request for a live agent during the conversation, while the live agent can still take over the conversation from the **Conversations** dashboard. You can visit our [Live Agent Tutorial](/seachat/seachat-manual/02-create-agent/04-agent-information/) for more detailed explanation of the feature. 

### Interact with AI Agent
You can immediately interact with the AI agent that you have just built. In **Agent URL**, you can click the URL to interact with your AI agent in a standalone window. 

Or if you wish to integrate your AI agent into your website, you can also access your API key in the **API Key** section. Please check out the [Webpage Integration](/seachat/seachat-manual/04-channels/08-install-to-webpage/) for more information on how to programmatically integrate your AI agent into your website.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/additional-options.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/additional-options.png" alt="image that displays the additional options in Basic Settings">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Additional Options in Basic Settings</p>
</div>

## Advanced Settings

Different from the basic settings, advanced settings allow you to customize your AI agent with more advanced features that SeaChat has curated for you. Inside **Advanced Settings** under **Agent Information**, the following advanced features are available:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/advanced-settings-dashboard.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/advanced-settings-dashboard.png" alt="image that displays the additional options in Basic Settings">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Advanced Settings Dashboard</p>
</div>

### Agent Memory
Agent memory fields are used to extract information from a conversation and store it for future reference. Memory is a powerful yet complex feature. We recommend you refer to the [Agent Memory](/seachat/seachat-manual/02-create-agent/03-agent-memory/) tutorial to learn more about how to set up memory fields for your AI agent.

### Retrieval Augmented Generation (RAG)
Through Retrieval Augmented Generation (RAG), we can optimize the output of a Large Language Model (LLM) by integrating external data that is not present in the training data (Knowledge). This feature will drastically reduce the continuous training that you would otherwise need without RAG. Retrieval augmented generation is a sophisticated framework for improving the response of LLM models, and thus we invite you to consult our dedicated section on RAG for a better understanding of the feature.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/rag-input-fields.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/rag-input-fields.png" alt="image of the Retrieval Augmented Generation (RAG) feature in SeaChat">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Retrieval Augmented Generation (RAG)</p></p>
</div>