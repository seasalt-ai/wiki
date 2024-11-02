---
title: "Time Awareness and Context"
description: "Learn how SeaChat AI's Time Awareness and Context features enhance agent control for time-sensitive responses."
lead: ""
date: 2024-10-01T08:48:45+00:00
lastmod: 2024-10-01T08:48:45+00:00
weight: 100
draft: false
images: []
toc: true
aliases:
   - /en/seachat/seachat-manual/02-create-agent/03-advanced-settings/04-time-awareness-context/
---

--- 

## Overview

In addition to the [Retrieval Augmented Generation (RAG)](https://wiki.seasalt.ai/seachat/seachat-manual/02-create-agent/03-advanced-settings/02-retrieval-augmented-generation-rag/) feature and [Context Extraction](https://wiki.seasalt.ai/seachat/manual/create-agent/advanced-settings/context-extraction/), SeaChat AI offers various options in advanced settings that allow users to further control their agent’s behavior.

While these features are less sophisticated than RAG and Context Extraction, they can still be valuable in certain situations. This article provides a general walkthrough of these features.

---

## Time Awareness

<br/>

<center>
<a href="/images/seachat/en/time-awareness-context/time-awareness-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/time-awareness-context/time-awareness-ui.png"  alt="UI of Time Awareness Feature">
</a>

</center>

<br/>

The time awareness feature enables the AI agent to understand the current time in a specified timezone. This is useful for delivering time-sensitive information to customers. 

<br/>

<center>
<a href="/images/seachat/en/time-awareness-context/time-awareness-kb.png">
<img height="100%" width="100%" src="/images/seachat/en/time-awareness-context/time-awareness-kb.png"  alt="Knowledge Example Used in Example Use Case">
</a>

</center>

<br/>

For instance, if a business user has two different numbers (number 559-894-3287 and 334-380-9257) for customer support during business hours and after hours, the time-aware AI agent can provide the appropriate number based on the current time. 

If a customer contact the AI agent during business hours, the AI agent can provide the first number (559-894-3287). If the customer contacts the AI agent after hours, the AI agent can provide the second number(334-380-9257).  This feature adds another layer of personalization to the AI agent's responses.


<br/>

<center>
<a href="/images/seachat/en/time-awareness-context/time-awareness-example.png">
<img height="100%" width="100%" src="/images/seachat/en/time-awareness-context/time-awareness-example.png"  alt="Example Use Case of Time Awareness">
</a>

</center>

<br/>



## Context

The context feature lets users define the maximum number of conversation turns the AI agent should consider when generating responses. This is helpful when you want to offer contextually aware responses without referencing the entire conversation history.

By limiting the number of conversational turns, users can reduce response latency and avoid overwhelming the AI agent with excessive information.