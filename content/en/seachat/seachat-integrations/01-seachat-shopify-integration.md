---
title: "Shopify"
description: "Bring SeaChat to your Shopify storefront"
date: 2022-11-22T08:48:57+00:00
lastmod: 2022-11-22T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
   - /en/seachat/seachat-integrations/shopify/
   - /seachat/seachat-integrations/shopify/
weight: 10
toc: true
---

<p>
This manual details the process for embedding the SeaChat AI agent into your Shopify storefront. Access the required code snippet by navigating to Agent Configuration/Channels within your workspace at the SeaChat website, specifically under the Shopify channel.
</p>


<p>
1. Go to your Shopify dashboard and click on Online Store from the menu. 
</p>

<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step1.png" alt="Go to your Shopify dashboard and click on Online Store from the menu.">


<p>
2. Start editing by clicking the ellipsis icon next to your current theme and choosing Edit code.
</p>

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step2.png" alt="Start editing by clicking the ellipsis icon next to your current theme and choosing Edit code.">


<p>
3. Click on “theme.liquid” on the left side panel.
</p>

<img width="40%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step3.png" alt="Click on “theme.liquid” on the left side panel.">


<p>
4. Paste the SeaChat code snippet from the Shopify integration setup on Seachat into the &lt;head&gt; section. You can paste it anywhere between the opening &lt;head&gt; tag and the closing &lt;/head&gt; tag.
</p>

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step4.png" alt="Paste the SeaChat code snippet in the head; section. You can paste it anywhere between the opening head tag and the closing /head tag">


<p>
5. Click “Save” button on top right. Click “Preview Store” to test the AI agent. Remember to launch the store again when you are ready!

Important Note: if you want to configure the style of your widget, please go to “Channels” -> “WebChat Widget” -> “Basic Setting”. Your AI Agent will share the same style across your webchat widget channels.
</p>


<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step5.png" alt="Click “Save” button on top right. Click “Preview Store” to test the AI agent. Remember to launch the store again when you are ready!">


<p>
6. (Optional) Please disconnect any other chatbot services, like Shopify Inbox, to prevent confusion. For Shopify app users, disable the "Apps embeds" toggle on your website customization page. If your previous chatbot service is embedded in code, remove it carefully. 
</p>

Need assistance? Contact us at seachat@seaslt.ai.

 
 