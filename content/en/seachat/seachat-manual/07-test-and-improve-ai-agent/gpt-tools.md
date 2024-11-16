---
title: "Custom GPT Tools"
description: ""
date: 2024-11-13T00:22:19-07:00
lastmod: 2024-11-13T00:22:19-07:00
draft: false
weight: 2
---

## Overview

Custom GPT Tools in SeaChat allow users to enhance the agent's responses by integrating custom actions directly into conversations. This feature enables users to define specific conditions under which the agent can execute these actions, providing tailored responses and intelligent assistance based on real-time information. For example, you might want the agent to perform a search or fetch data from your company’s API, enabling SeaChat to provide enriched answers that draw on external resources.

Here’s a quick simple tutorial to call two APIs to display single picture. We demonstrate how to configure the API endpoint, and display cute dog pictures in the chat:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/TMBN0qOUDpQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>
https://www.youtube.com/watch?v=TMBN0qOUDpQ&list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0&index=18
In the next tutorial, we call the weather API by configuring the API parameters, and dynamically converting location names to GPS coordinates to get accurate weather information:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/2C2IOabHHFc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

Finally, we demonstrate how to get a carousel of cards with multiple dog pictures. We showed you how to utilize the **PATH** parameter to display multiple pictures of a specified dog breed in the chat:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/Cj0tYlhEMfM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


## Getting Started

To set up this feature, after logging into SeaChat, navigate to **Agent Configuration** \-\> **Integrations** \-\> **Custom GPT Tools**. 

### Step 1: Select Tool Type

SeaChat currently supports one main type of tools:

* **Search and Display Tools**: These tools allow SeaChat to perform an external search using your API and fetch additional information based on the conversation context. The search results will be displayed in webchat as plaintext or as a carousel of cards.

We plan to support more tool types in the future.

### Step 2: Add Required Fields

To configure a Custom GPT Tool, you’ll need to provide several key pieces of information:

* **Enable the Tool**: Turn on the **Enable** switch. This will activate the tool, allowing SeaChat to start using it automatically in relevant conversations.  
* **Tool Name**: Enter a name for your tool. This should contain only letters (A-Z, a-z), numbers (0-9), underscores (\_), or hyphens (-) without any spaces.  
* **HTTP Method**: Choose from the available HTTP methods (`POST`, `PUT`, `GET`, `PATCH`, `DELETE`) depending on the operation required for your API.  
* **Endpoint URL**: Input the URL of your API endpoint where SeaChat will send the requests.  
* **Description**: Provide a brief description of the tool and the API endpoint so GPT understands the tool’s function and purpose.


<br/>

<center>
<a href="/images/seachat/en/gpt-tools/image5.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/image5.png"  alt="Example of New Custom Tool">
</a>

<br/>

*Example: we have a GET endpoint that retrieves dog pictures.*

</center>



You should also configure parameters to be sent with the API request:

* **Fixed Value Parameters**: These are prefilled parameters defined by you that will be sent exactly as entered with each API request.  
* **Dynamic Variable Parameters:** These are parameters that SeaChat extracts dynamically from the conversation. For each of these, provide a description of the information that should be extracted, and SeaChat will use conversation context to generate values before making the API request.


<br/>

<center>
<a href="/images/seachat/en/gpt-tools/image7.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/image7.png"  alt="Example of API Endpoints">
</a>

<br/>

*Example: this dog picture search API endpoint has a fixed parameter, ‘count,’ set to a value of 1 and a dynamic parameter, ‘breed’, defines the specific dog breed the user is searching for.*

</center>



### Step 3: Configure Result Display

Once the API is configured, you can decide how to display its results in the chat. API results will be displayed as plain text by default. In cases where the API response lacks a valid URL or button, you can set up a fallback card to display by filling in a default image URL and a default button title. To enable the fallback card, simply check the relevant checkbox. 


<br/>

<center>
<a href="/images/seachat/en/gpt-tools/image2.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/image2.png"  alt="Optional Settings">
</a>

<br/>

*Example: we leave the ‘Enabled’ checkbox unselected, so the result will be displayed as plain text, as shown below.*

</center>



<br/>

<center>
<a href="/images/seachat/en/gpt-tools/image3.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/image3.png"  alt="Chat Demo">
</a>

<br/>

*Example: The result is shown as plain text, with the URL displayed as a clickable link that leads to a dog picture.*

</center>

<br/>

<center>
<a href="/images/seachat/en/gpt-tools/image1.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/image1.png"  alt="Enable Cards">
</a>

<br/>

*Example usage: In this case, if we check the *Enabled* checkbox, the result will be displayed in a card format, as shown below.*

</center>

<br/>

<center>
<a href="/images/seachat/en/gpt-tools/image6.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/image6.png"  alt="Card Response Example">
</a>

<br/>

*Example: The result is displayed as a card, with the image showing the retrieved picture, and the button title and URL set to the default button title and button URL.*

</center>


### Step 4: Test Your API Configuration

After filling out the required fields, a testing query will be automatically generated based on the parameters you specified. You can use this testing area to verify that your API configuration is functioning correctly and see the API response on the right side.


<br/>

<center>
<a href="/images/seachat/en/gpt-tools/image4.png">
<img height="100%" width="90%" src="/images/seachat/en/gpt-tools/image4.png"  alt="API Configuration Test">
</a>

<br/>

*Example: we click *Submit* to execute the API, resulting in a 200 success status code.*

</center>


### Step 5: Save and Done

Once you've confirmed that your Custom GPT Tool settings are working as expected, you can proceed to save the configuration by clicking the Save button to save your Custom GPT Tool settings permanently.

## Limits

To ensure optimal performance, certain limits apply to Custom GPT Tool settings:

* **Character Limits**: The combined character count of the tool name, description, all Fixed Value Parameters (keys and values), and all Dynamic Variable Parameters (keys and descriptions) must not exceed 1024 characters.  
* **Tool Execution Limit**: SeaChat will activate at most one enabled GPT tool per incoming user message. This includes any integrations with calendars or live agent transfers, ensuring that only the most relevant tool is selected for each conversation.

