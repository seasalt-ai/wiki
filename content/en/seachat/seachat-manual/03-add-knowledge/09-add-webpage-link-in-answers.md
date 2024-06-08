---
title: "Adding buttons to KB responses"
description: "Learn how to add reference URLs to SeaChat AI assistant answers to provide more detailed information  to users. This guide will walk you through adding URLs in the 'Existing Knowledge' page, enriching AI assistant interactions. Included YouTube video tutorials will demonstrate this process in detail, ensuring easy comprehension and implementation of these enhancements. By adding URLs, your AI assistant will be able to offer more comprehensive customer support, enhancing user experience."
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-05-29T08:48:57+00:00
draft: false
images: []
aliases:
  - /en/seachat/seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers/
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
    <p style="margin-top: 20px; font-size: 15px">Additional Setting in Manual Entry</p>
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

Let's first upload some information to the agent's knowledge base. Please refer to [here](/en/seachat/seachat-manual/03-add-knowledge/) to find a way to upload information to the agent's knowledge base.

Once there is information in the knowledge base, the agent will start using this information to respond to user queries. I will provide more than one URL in the agent's answer to show you how it works. You can add as many URLs as you want to the agent's answer. 

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/url-to-answer.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/url-to-answer.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">URLs added to Agent's Answer</p>
</div>


There are a more advanced features in SeaChat agents' knowledge base that you can leverage to optimize your agent's responses. Check out our tutorials on [Advanced Features](/en/seachat/seachat-manual/03-add-knowledge/09-advanced-features/) to learn more about these functionalities.