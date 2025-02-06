---
title: "Additional Features in Knowledge"
description: "Enhance AI responses with buttons and images. Learn to edit entries, prioritize info, and sync content."
lead: ""
date: 2024-03-04 10:43:51.069 +0100
lastmod: 2024-06-17 10:43:51.069 +0100
weight: 413
draft: false
images: []
aliases:
  - /en/seachat/seachat-manual/03-add-knowledge/10-additional-feature/01-additional-features-in-kb
url: /en/seachat/manual/add-knowledge/additional-features-in-kb/
---

## Overview

In addition to your prompt response, SeaChat provides more advanced features to enhance your AI agent's responses. These features include adding buttons, images, and videos to your responses. This guide will walk you through how to add these features to your AI agent's responses, ensuring that your users receive the most comprehensive support possible. All the following parameters are available for every piece of knowledge that you have uploaded to your knowledge base.

## Additional Features in Knowledge Base

Let's first navigate to the knowledge base dashboard and pick an existing knowledge to add the additional features to. Find **Knowledge Base** under **Agent Configuration** in the sidebar on the left-hand side, and then click on **Existing** to view all the knowledge that has been uploaded to your AI agent.

Open the knowledge that you wish to add the additional features to, and then click on the **Edit** button.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/kb-dashboard.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/kb-dashboard.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Go to <strong>Existing</strong></p>
</div>

## Edit Knowledge in Additional Features

When your AI agent needs to answer a question, it will search the knowledge base for the most relevant information. The AI agent will look into the **Document Text** to look for relevancy. SeaChat leverages this behavior and allows you to add additional features to individual knowledge, so every time the agent retrieves this information from this particular knowledge, it will remember to include these additional features in its response. This allows SeaChat users to provide more detailed information to their customers.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/additional-settings.png   " target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/additional-settings.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Additional Settings</p>
</div>

### Card Message

When providing information to customers, it is useful to provide the source of the given information or supplementary readings to paint a better picture for them. SeaChat allows you to add both cards and buttons to your responses to provide a more comprehensive response to your users.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/card-info.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/card-info.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Knowledge Setting</p>
</div>

Card message provides a strong visual representation of the information you are providing. You can add a title, subtitle, and image to your card message. This feature is particularly useful when you want to provide a preview of the information you are providing.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/card-msg.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/card-msg.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Upload Image to Card Message</p>
</div>

### Button Message

In comparison to cards, buttons are more straightforward. You can add a title and a URL to your button message. This feature is particularly useful when you want to provide a link to the source of the information you are providing, and you can add as many buttons to a response as you want. This feature offers simpler navigation for your users in contrast to the card messages.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/btn-msg.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/btn-msg.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Knowledge Setting</p>
</div>

### Document Weight

The document weight is a parameter that allows you to prioritize a particular piece of knowledge. The higher the weight, the more likely the knowledge will be retrieved by the AI agent when it is searching for relevant information. This feature is particularly useful when you have multiple knowledge that is relevant to the same question, and you want to prioritize the most important knowledge to be retrieved first.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/doc-weight.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/doc-weight.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Knowledge Setting</p>
</div>

## Synchronize URL Knowledge

If the knowledge is imported through a URL or sitemap, you can synchronize the knowledge with the source URL. This feature is particularly useful when the knowledge is updated frequently, and you want to ensure that the knowledge in your knowledge base is always up-to-date. 

This feature allows the users to have a better experience of knowledge management. As long as the URL is still accessible, users do not need to re-upload the knowledge to the knowledge base.  

All you have to do now just click on the **Sync** button of the knowledge that you want to synchronize with the source URL, and Seachat will automatically update the knowledge with the latest information from the source URL.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/sync-button.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/knowledge-additional-features/sync-button.png" alt="knowledge synchronization button">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Sync Knowledge</p>
</div>
