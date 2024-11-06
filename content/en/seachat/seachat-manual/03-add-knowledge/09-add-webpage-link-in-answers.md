---
title: "Adding URL buttons to KB responses"
description: "Enhance your SeaChat AI agent's responses by adding URL buttons for more information in responses."
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-05-29T08:48:57+00:00
draft: false
images: []
aliases:
  - /en/seachat/seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers/
url: /en/seachat/manual/add-knowledge/webpage-link/  
weight: 150
toc: true
---

[//]: # ()
[//]: # (# :movie_camera: Video Tutorial)

[//]: # ()
[//]: # (<iframe width="100%" height="400" src="https://www.youtube.com/embed/?listType=playlist&list=PL8K7_LTqly449uOg_uBWOPfFyL1fJRjkE&index=12" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>)

[//]: # ()
[//]: # (---)
# Overview

You can include relevant reference URLs in the AI assistant's responses, allowing users to access more detailed content to users. In the **Existing Knowledge** page, you can find relevant knowledge and add reference URLs the AI agent's responses. This feature enhances the user experience by providing additional information and resources to users when they are looking for some specific information. 

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/new-kb-ui.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/new-kb-ui.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Knowledge Setting</p>
</div>

## [Additional Settings in Knowledge Base](#additional-setting-ui)

Find **Knowledge Base** under **Agent Configuration** and click to open the uploaded knowledge. Then, locate the **Edit** button and add a URL button to that knowledge entry.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/choose-knowledge.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/choose-knowledge.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Choose the Knowledge to add URL Buttons to</p>
</div>

Make sure to provide a clear **Document Title** for the agent to retrieve the knowledge easily. Additionally, carefully describe the information to your agent in the **Document Text**. Your description will help the agent to form a response based on the information you provide.

Now the AI agent will remember to attach the URL button in its response every time it retrieves this piece of information from the knowledge base.

## [Buttons](#additional-setting-ui)

SeaChat Provides different ways to add additional information to the agent's response. Choose the **Buttons** option to add a URL button to the agent's response.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/choose-button.png" target="_blank">
    <img width="70%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/choose-button.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Choose <strong>Button</strong></p>
</div>

The URL you provide here will be displayed as a button in the chat window. When the user clicks on the button, they will be redirected to the URL you have provided. Put the label that you wish to show your user in the **Title** and provide the URL in the **Content** field. You can add as many buttons as you want to the answer by simply clicking on the Plus(Add) sign.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/add-more-url.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/add-more-url.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Add URL Button by Pressing <strong>Plus</strong> Button</p>
</div>

## Add URL Buttons to Knowledge Base Responses

Knowledge Base is where our agent will look for information to respond to user queries. A very powerful use case will be a FAQ agent, where the agent can provide answers to frequently asked questions. In this case, you can add URLs to the agent's answers to provide more detailed information to users.

Now, let's test out the URL button in the chat window. When the AI agent retrieves certain information from knowledge base as contextual information, it will display the answer with the URL button if the button feature is enabled for this piece of information. The user can click on the button to access the URL and get more detailed information. As simple as that!

Let's first upload some information to the agent's knowledge base. Please refer to [here](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/intro/) to find a way to upload information to the agent's knowledge base.

Once there is information in the knowledge base, the agent will start using this information to respond to user queries. I will provide more than one URL in the agent's answer to show you how it works. You can add as many URLs as you want to the agent's answer. 

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/url-to-answer.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/url-to-answer.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">URLs added to Agent's Answer</p>
</div>


### KB IDs

A KB ID is a unique identifier for each piece of knowledge in the knowledge base. You can copy the ID of any knowledge item to your clipboard by clicking on the **Copy KB ID** button located under the **More** button for that knowledge.

You can then paste this KB ID to the content field of a button. The AI agent will then retrieve the information and return it to the user when the button is clicked.

This is particularly useful when the content of a button becomes too lengthy. For users that are using external channels like [LINE](http://wiki.seasalt.ai/seachat/seachat-manual/04-channels/05-install-to-line/#limits-of-line-button-messages), there is a set of limits related to the button messages. 

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/kb-id-problem.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/kb-id-problem.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Message Cutoff due to Message Limitation</p>
</div>
<br/>

The KB ID feature provides a solution for these users to provide detailed information without worrying about exceeding the character limit.

The AI agent will reference the knowledge base to retrieve the information and respond, bypassing the character limit imposed.

Not only does this feature free users from the character limit of the button content, but it also enables agent editors to better manage information in the knowledge base. Instead of overloading the button content with information, you can create a separate knowledge item accessible to the AI agent, which the button can link to.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/kb-id.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/kb-id.png" alt="">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Complete Message Using KB ID</p>
</div>

<br/>

> 🚨Attention 🚨
>
> For security reasons, AI agents cannot access KB IDs from another AI agent's knowledge base. KB IDs are unique to the knowledge in the knowledge base of a given AI agent, regardless of whether the agents are in the same workspace.


## URL Buttons from Spreadsheets

You can also add URL buttons to your agent's responses using a spreadsheet. When you are adding knowledge using a spreadsheet to upload a large amount of information, it can be difficult to add reference buttons to each knowledge manually. Don't worry. SeaChat has a solution for you. 

By adding columns called **seachat_ref** in your spreadsheet, your agent will automatically extract information to add URL buttons to the agent's responses. You can put as many column as you want to add multiple URL buttons to the answer.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/spreadsheet-example.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/spreadsheet-example.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Spreadsheet Example</p>
</div>

Since the agent will look into this particular column, we need to make sure that we use the correct variables to help the agent understand the information.

**Please make sure to follow the format below to ensure the agent can extract the information correctly:**

In each row of the **seachat_ref** column, your AI agent will look for two pieces of information: <code>button text</code> (line 1) and <code>button value</code> (line 2). The following is what your seachat_ref column should look like:

```
"User Manual Wiki" --- line 1
"https://user-manual-wiki.com" --- line 2
```


> 🚨Attention🚨
> 
> If the button value is not a URL, e.g. some text, 2 paragraphs, or 3 URLs in 3 lines, the button will show the entire content of button value when clicked.

All the information that you put inside `seachat_ref` will be extracted as buttons. If the content of the button value is a URL, the button will redirect the user to that URL when clicked. If the button value is not a URL, the button will return the button value in a response.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/non-url-buttons.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/non-url-buttons.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Buttons in Agent Response</p>
</div>


<br/>

That's it. Now you no longer have to worry about manually adding URL buttons to your agent's responses when you are uploading a spreadsheet with a large amount of information.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/spreadsheet-url-buttons.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/spreadsheet-url-buttons.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Multiple URL Buttons in Agent Response</p>
</div>


<br/>

There are more advanced features in SeaChat agents' knowledge base that you can leverage to optimize your agent's responses. Check out our tutorials on [Advanced Features](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/additional-features-in-kb/) to learn more about these functionalities.