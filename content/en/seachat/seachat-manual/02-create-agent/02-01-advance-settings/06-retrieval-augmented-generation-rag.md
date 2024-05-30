---
title: "Retrieval Augmented Generation (RAG)"
description: "Discover SeaChat's advanced settings, including Agent Memory and Retrieval Augmented Generation (RAG). Learn how to optimize your AI agent's performance and real-time user engagement."
lead: ""
date: 2024-04-26T08:48:45+00:00
lastmod: 2024-05-26T08:48:45+00:00
weight: 50
draft: false
images: []
toc: true
aliases:
  - /en/seachat/seachaat-manual/02-create-agent/06-retrieval-augmented-generation-rag
---

## Overview
Retrieval Augmented Generation (RAG) is a pivotal feature within SeaChat, enhancing data retrieval and augmenting the accuracy of interactions with the AI agent. By providing you with the ability to tailor query patterns, select search methods, and define knowledge base retrieval counts.

---

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-rag-ui" href="/images/seachat/en/agent-advanced-settings/rag-dashboard.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-advanced-settings/rag-dashboard.png" alt="image of the Retrieval Augmented Generation (RAG) feature in SeaChat">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">RAG Settings in SeaChat</p></p>
</div>

## [1. Query Pattern](#seachat-rag-ui)
Whether you require comprehensive context, focused engagement, or quick, precise responses, SeaChat's flexible query patterns for querying the knowledge base ensure an optimized chat experience tailored to your preferences.

Example conversation between a customer and a parking lot FAQ AI agent with information of more than hundreds of parking lots in the knowledge base:

---

👨 (Query 1): Is there a parking lot near the Seattle Space Needle?

🤖️ (Response): Yes, you can park at the ABC Parking Lot on 123rd Ave NE. It has 50 parking spots. The parking fee starts at $10 per hour, with a daily maximum of $60.

👨 (Query 2): I will be working near there. Can I rent a parking spot monthly?

---

#### Query Pattern Options

### Previous Query &#8594; Bot Response &#8594; Current Query
Offers comprehensive context by incorporating the last three turns of the conversation. In this case, the complete conversation (Query 1 + Bot Response + Query 2) is used to query the knowledge base and to generate the AI agent's next response for Query 2 .

### Previous Query &#8594; Current Query
Focuses more heavily on the user’s requests and is not influenced by the AI agent’s response. It includes the last two user inputs (Query 1 and Query 2) to query the knowledge base and to generate the AI agent's next response.

### Current Query
Provides a succinct approach, considering only the user's latest input, i.e.Query 2, for the AI agent's next response. This is ideal for one-turn dialogues or cases where users frequently switch topics. However, it may miss important context when discussing the same topic over multiple turns.

## [2. Search Method](#seachat-rag-ui)

You can optimize knowledge base search by choosing from distinct knowledge base search methods:

### Keyword Search
Matches user’s provided keywords against the knowledge base to deliver relevant results. This works well when you have unique tokens such as product names, locations, IDs, etc. but may miss cases where the user doesn’t say the exact keyword (ex/ they use a synonym or a different language than the KB document).

### Vector Search
Utilizes the capabilities of text embedding to enhance the retrieval of relevant information. Vector search can work well across languages and retrieve similar documents even if they don’t have matching keywords. However, it may struggle with rare tokens such as product names, locations, or IDs.

### Hybrid Search
Integrates both Keyword and Vector Search methods to optimize information retrieval. 


## [3. Knowledge Base Retrieval Count](#seachat-rag-ui)

This field allows you to specify the number of KB chunks to retrieve, ensuring efficient information retrieval. The ideal count is flexible and depends on the token limits and document types.

Considerations for Setting the Count:
- **Too Few Chunks**

You may miss essential information, leading to incomplete or inaccurate responses from GPT.

- **Too Many Chunks**

Important information may get buried under irrelevant details, making it harder for GPT to provide accurate responses.

- **Context Limit**

There is a limit to the amount of context that can be provided with each request. If the retrieved documents exceed this limit, SeaChat will use as many documents as can fit within the limit.

By adjusting the KB retrieval count, you can optimize the balance between depth of information and resource usage, ensuring accurate and efficient responses.
