---
title: "Custom GPT Tools"
description: ""
date: 2024-11-13T00:22:19-07:00
lastmod: 2024-11-13T00:22:19-07:00
draft: false
weight: 70
url: /seachat/seachat-manual/custom-gpt-tool/gpt-tools
---

## Overview

Custom GPT Tools in SeaChat allow users to enhance the agent's responses by integrating custom actions directly into conversations. This feature enables users to define specific conditions under which the agent can execute these actions, providing tailored responses and intelligent assistance based on real-time information. For example, you might want the agent to perform a search or fetch data from your company’s API, enabling SeaChat to provide enriched answers that draw on external resources.

## Video Tutorials

Here’s a quick simple tutorial to call two APIs to display single picture. We demonstrate how to configure the API endpoint, and display cute dog pictures in the chat:


<iframe width="100%" height="400" src="https://www.youtube.com/embed/TMBN0qOUDpQ?si=LrXqfjo0jjO8DyF6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In the 2nd tutorial, we call the weather API by configuring the API parameters, and dynamically converting location names to GPS coordinates to get accurate weather information:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/2C2IOabHHFc?si=954wmcmmhQeneWmN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In this 3rd tutorial, we demonstrate how to get a carousel of cards with multiple dog pictures. We showed you how to utilize the **PATH** parameter to display multiple pictures of a specified dog breed in the chat:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/Cj0tYlhEMfM?si=YHvnd22-M6IyPdNB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In this 4th tutorial, we demonstrate how to set up email alerts using Custom GPT Tools in SeaChat, detecting concerning content in chat conversations and automatically sending email notifications.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/KhjHDbRTIJc?si=D2e5WzI4HBk-QRts" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In this 5th tutorial, we demonstrate how to configure SMS notifications in SeaChat for monitoring user conversations. As an example, we demonstrated how to set up SMS alerts when detecting signs of depression in user interactions in this video.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/Z7Zj6BWEXTc?si=GHiKnsI_M4AwCyx0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In this 6th tutorial, we demonstrate how to automatically send information to callers via SMS. 

<iframe width="100%" height="400" src="https://www.youtube.com/embed/LNezPT4qzCs?si=wvvho3rr77RpDxj_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Getting Started

To set up this feature, after logging into SeaChat, navigate to **Agent Configuration** \-\> **Integrations** \-\> **Custom GPT Tools**. 

>
> SeaChat currently supports three types of tools:
> 
> - **Search and Display Tools**: These tools allow SeaChat to perform an external search using your API and fetch additional information based on the conversation context. The search results will be displayed in webchat as plaintext or as a carousel of cards.
> - **Send Email**: Automate email sending based on your instructions. Ensure you specify the purpose, recipients, and conditions. To send emails to users, collect their email addresses via a webchat form.
> - **Send SMS**: Automate SMS sending based on your instructions. Define the purpose, recipients, and conditions. To send SMS to users, ensure access to their phone numbers through the channel or a webchat form.
> 
> <br/>
> <center>
> <a href="/images/seachat/en/gpt-tools/seachat-tool-options.png">
> <img height="100%" width="100%" src="/images/seachat/en/gpt-tools/seachat-tool-options.png"  alt="SeaChat Supported Tool Type">
> </a>
> <br/>
> </center>

## Steps to Configure a Search and Display Tool:

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

## Steps to Configure Email-Sending or SMS-Sending Tools

### Step 1: Add Required Fields

You need to provide several key pieces of information:

- **Enable the Tool**: Turn on the Enable switch. This will activate the tool, allowing SeaChat to start using it automatically in relevant conversations.
- **Tool Name**: Enter a name for your tool. This should contain only letters (A-Z, a-z), numbers (0-9), underscores (_), or hyphens (-) without any spaces.
- **Description**: Add a brief description to help GPT understand the conditions for triggering the email or SMS.

<br/>

<center>
<a href="/images/seachat/en/gpt-tools/image9.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/image9.png"  alt="Request via Emails Example">
</a>

<br/>

*Example A: This tool is set up to send an email when user request information via email*

</center>

<br/>

<center>
<a href="/images/seachat/en/gpt-tools/sms-setup.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/sms-setup.png"  alt="SMS Alerts Example">
</a>

<br/>

*Example B: This tool is set up to send an SMS message when a user exhibits excessively rude behavior or uses inappropriate language.*

</center>

### Step 2: Configure Email/SMS Content and Recipients
You need to define the following fields to set up the actual message content to be sent via email or SMS.

- **Title**: For the Send Email tool, provide a title for the email.
- **Content**: Write the content you want to send.
- **Options**: Check the option to include the AI agent's response at the end of the email/SMS, if desired.
- **Recipients**: Enter a comma-separated list of recipients. Use placeholders like `{{user_phone}}` for SMS or `{{user_email}}` for email if SeaChat collects these values from webchat forms.

> 📝 Note:
> 
> For emails, the sender address is defaulted to `no-reply@seasalt.ai`.
> For SMS, the sender number is configured in the Calls channel. Learn how to set up a phone number [here](https://wiki.seasalt.ai/en/seachat/manual/channels/voicebot/#toll-free-number).


<br/>

<center>
<a href="/images/seachat/en/gpt-tools/email-settings.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/email-settings.png"  alt="Email setup">
</a>

<br/>

*Example A: Email titled "Your Requested Info" with content containing a placeholder. The checkbox is selected to include the AI agent's response in the email.*

</center>

<br/>

<center>
<a href="/images/seachat/en/gpt-tools/flag-msg-setting.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/flag-msg-setting.png"  alt="Flagged Message Setting">
</a>

<br/>

*Example B: SMS with the content "The user has been flagged for inappropriate conduct."*

</center>

### Step 3: Save and Test
Once you've completed configuring your Custom GPT Tool email or SMS settings, click the Save button to save your changes. You can then test your tools by interacting with your AI agent.


<br/>

<center>
<a href="/images/seachat/en/gpt-tools/chat-example.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/chat-example.png"  alt="Chat Example for Flagged Message">
</a>

<a href="/images/seachat/en/gpt-tools/seachat-req.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/seachat-req.png"  alt="SeaChat Request Email">
</a>

<br/>

*Example A: When a user asks the AI agent for a menu, the email tool is triggered, sending an email with the AI agent’s response included after "Here’s what you requested:".*

</center>

<br/>

<center>
<a href="/images/seachat/en/gpt-tools/flag-msg.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/flag-msg.png"  alt="Flagged Message">
</a>

<br/>

*Example B: SMS with the content "The user has been flagged for inappropriate conduct."*

</center>

## Limits

To ensure optimal performance, certain limits apply to Custom GPT Tool settings:

* **Character Limits**: The combined character count of the tool name, description, all Fixed Value Parameters (keys and values), and all Dynamic Variable Parameters (keys and descriptions) must not exceed 1024 characters.
* **Tool Execution Limit**: SeaChat will activate at most one enabled GPT tool per incoming user message. This includes any integrations with calendars or live agent transfers, ensuring that only the most relevant tool is selected for each conversation.
