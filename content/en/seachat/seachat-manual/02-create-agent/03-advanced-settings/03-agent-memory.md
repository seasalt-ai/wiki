---
title: "Extraction"
description: "SeaChat Extraction tracks customer profiles to ensure relevant conversations and assist in expected outcomes."
lead: ""
date: 2024-04-26T08:48:45+00:00
lastmod: 2024-05-21T08:48:45+00:00
weight: 80
draft: false
images: []
toc: true
aliases:
   - /en/seachat/seachat-manual/02-create-agent/03-advanced-settings/03-agent-memory
url: /en/seachat/manual/create-agent/advanced-settings/agent-memory/
---


<div style="display: flex; align-self: flex-end; align-items: baseline">

`This feature is only available on `
   <div style="border-radius: 30%; 
    background: linear-gradient(90deg, #135f5c, #3a947b); 
    width: 5rem; 
    color: #ffffff; 
    padding: calc(min(100vw, 1366px)* 0.00439) calc(min(100vw, 1366px)* 0.00878);
    border-radius: calc(min(100vw, 1366px)* 0.01464);
    display: block;
    unicode-bidi: isolate;
    box-sizing: border-box;
   font-size: .8rem;
    align-content: center;
   ">
   <div>Enterprise</div>
</div>
<div style="border-radius: 30%; 
    background: linear-gradient(90deg,#824a14,#886f40);
    width: 5rem; 
    color: #ffffff; 
    padding: calc(min(100vw, 1366px)* 0.00439) calc(min(100vw, 1366px)* 0.00878);
    border-radius: calc(min(100vw, 1366px)* 0.01464);
    display: block;
    unicode-bidi: isolate;
    box-sizing: border-box;
   font-size: .8rem;
   margin-left: .5rem;
        align-content: center;
   ">
   <div>Premium</div>
</div>

`plans `

</div>

# Overview


  <iframe width="100%" height="400" src="https://www.youtube.com/embed/?v=Msgg3U3lW4M&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=11" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


Extraction allows users to intuitively define the most important aspect of the conversation to keep dialogue relevant and to aid in objectively determining the conversation outcome. 

The use cases of Extraction include:
* Build a user persona, so next time the same user comes back, the AI agent still remembers key points from last conversation. For instance: `{married: yes, family: 2 kids, hobby: golf}`.
* Store a survey results, then later retrieve these results from the API to analyze them. For instance: `{score: 2, feedback: wifi charging issue}`.
* Qualify a potential buyer, then trigger some actions based on that. For instance: `{intent: buying an iPhone, lease or cash: cash, when: ASAP}`.


In this document we'll cover:

- Designing extraction fields and descriptions for agents to extract for each conversation.
- Extract extraction for each conversation.

--- 

# Set up Extraction in Advanced Settings

In this section we'll go through how to effectively set up Extraction fields for your agent.
We separate the use cases into two categories:

1. Non-survey use cases: the agent editor needs to manually define Extraction of interest.
2. Survey use cases: the Extraction is automatically extracted from a list of survey questions and cannot be modified.

## Extraction Setup for non-Survey Use Cases

For most agents, to set up Extraction we'll use the provided UI in the **Advanced settings** section.

1. In the **Agent Information**, head to the **Advanced Settings** section at the top right.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/d4261fc5-2b20-4f65-a264-ade4d9266d3a)


<center>
<a href="/images/seachat/en/memory/general-setup.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/general-setup.png" alt="">
</a>

<br/>

*Agent Information → Advanced Settings*
</center>

<br/>

2. Create desired fields in the sections provided:
    - **Field**: The name of the extraction "variable" we want to extract
        - Make this name intuitive. Ideally you should know what this field is monitoring for based on the name.
    - **Content**: The default value for this extraction field
        - This is the starting value for the extraction field. This will usually be empty.
    - **Description**: The definition of the field
        - In natural language, describe what this field is and what type of value to extract.
        - Be descriptive yet concise here. This can greatly affect extracted values.
      
<br/>

3. Add or remove fields as necessary using the plus (add) and minus (remove) icons on the right side of the page

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/621eaa33-78a9-45d4-8597-07deda70b141)

[//]: # ()
[//]: # (<center>)

[//]: # (<a href="/images/seachat/en/memory/add-and-remove.png" target="_blank">)

[//]: # (<img width="20%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/add-and-remove.png" alt="">)

[//]: # (</a>)

[//]: # ()
[//]: # (<br/>)

[//]: # ()
[//]: # (*Plus &#40;Add&#41; and Minus &#40;Remove&#41;*)

[//]: # (</center>)

4. Finally, save your extraction settings by clicking the save button at the bottom.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/7220ada1-b2e3-4353-9052-c49d45225bd8)

[//]: # (<center>)

[//]: # (<a href="/images/seachat/en/memory/save-setting.png" target="_blank">)

[//]: # (<img width="40%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/save-setting.png" alt="">)

[//]: # (</a>)

[//]: # ()
[//]: # (<br/>)

[//]: # ()
[//]: # (*Save Your Extraction Settings*)

[//]: # (</center>)


## Extraction Setup for Survey Use Cases

For the survey use cases (CSAT, Brand Perception, Market Research, etc.), the extraction pane in Advanced Settings will be dynamically set from the description section.

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
<a href="/images/seachat/en/memory/question-start.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/question-start.png" alt="">
</a>

<br/>

*Question Section*
</center>

3. Head over to the Advanced Settings tab to make sure the fields are properly set.

> :rotating_light: NOTE :rotating_light:
>
> DO NOT change any section in the extraction pane when using Survey use cases. If you need to make a change to the questions use the description page.


[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/aa6a0fda-3e34-4271-9010-28305d9cd296)

<center>
<a href="/images/seachat/en/memory/advanced-settings.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/advanced-settings.png" alt="">
</a>

<br/>

*Advanced Settings*
</center>

## Extraction in Conversations 

The extraction for each conversation will update in real time and we can check the values from the Conversation page

1. Head to the Conversations page from the left hand side

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/00c4d418-879d-49a5-9ffc-a49972668ed7)

<center>
<a href="/images/seachat/en/memory/conversation-page.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/conversation-page.png" alt="">
</a>

<br/>

*Conversations*
</center>

2. Find the desired conversation from the list and press the triple dot icon in the bottom right corner for that conversation.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/9be38868-cdbf-4223-a445-636695b8c922)

<center>
<a href="/images/seachat/en/memory/memory-btn.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/memory-btn.png" alt="">
</a>

<br/>

*Click on **Extraction***
</center>

3. Pressing **Extraction** will bring up the latest extracted values for that conversation

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/5872958e-9b35-4ad7-93c2-50ac2a50f81f)

<center>
<a href="/images/seachat/en/memory/extracted-value.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/extracted-value.png" alt="">
</a>

<br/>

*Latest Extracted Values*
</center>

## 🤖 Example Use Case

Imagine we have an AI agent tailored to enhance customer experience management. The agent's effectiveness hinges on its ability to track user preferences accurately, necessitating the establishment of specific extraction fields for such data.

### Initial Setup

Before delving into extraction field configurations, it's crucial to have your AI agent operational. If you haven't set up your agent yet, please consult our [Create New Agent](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/) guide for detailed instructions.


### Define Extraction

Proceed by navigating to the **Advanced Settings** tab where you can define the extraction fields:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/memory/example-advanced-setting.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/example-advanced-setting.png" alt="">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Define Extraction</p>
</div>
</div>


1. **Field**: For instance, setting 'product_name' as a field indicates the agent will focus on extracting information about the product names mentioned during interactions.

2. **Description**: Here, you'll specify what information the field should capture. For 'product_name', the description would guide the AI to recognize and remember product names from the conversation. I also gave examples of the type of information to extract.

3. **Save**: Ensure to save these configurations to apply them.

### Monitoring Conversation Extraction

The AI agent will monitor conversations in real time, updating extraction fields as soon as relevant information is detected. This dynamic updating enables the agent to adapt its responses based on the extracted data.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/memory/example-conversation.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/example-conversation.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Monitor Conversation Extraction</p>
</div>

The extracted values from conversations are accessible within the system. Simply Move to the **Conversations** page, select the desired conversation, and click on the **Extraction** button to view the extracted values. Read again [here](#monitor-conversation-memory) to learn to see your result like the image below.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/memory/example-result.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/memory/example-result.png" alt="">
    </a>
</div>
 <p style="margin-top: 20px; font-size: 15px">Value Extracted</p>
</div>

# Retrieve Conversation Extraction

Each conversation's Extraction value can be retrieved via [the API](https://wiki.seasalt.ai/seasaltapi/seasalt-api/01-seachat-api-intro/) for further processing.

