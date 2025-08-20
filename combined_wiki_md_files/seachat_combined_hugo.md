# Seachat Documentation

*Combined documentation from content/en/seachat (Hugo weight-ordered)*

---


### Introduction to SeaChat

<!-- Source: getting-started/01-seachat-intro.md -->

<!-- Weight: 1 -->

*ChatGPT-powered Omni-channel Chatbot with a Life-time Free Widget for Human Replies*


We offer a versatile chat solution that lets you start for free with human agents and seamlessly upgrade to AI-powered automation when you're ready. Build and launch an AI agent that elevates your workflow in under 10 minutes, or begin with manual responses - the choice is yours.

---

## Ready to explore AI capabilities?
This tutorial will guide you through creating your first AI-powered SeaChat agent. From agent creation and knowledge base setup to testing and fine-tuning, we'll cover everything you need to know to leverage our advanced AI features when you're ready to upgrade.

<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/HsrMcNV8KJQ?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="Build Your Own ChatGPT Bot with Live Agent Transfer in 10 min | SeaChat | AI Bot with Agent Transfer" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

With SeaChat, you can enable or disable AI support anytime without changing your existing setup on all channels. Enjoy the flexibility of on-demand AI support while starting completely free.

---
## What makes SeaChat special?
Tired of chatbots that restrict channels, require large upfront costs, or lack pricing transparency?
SeaChat has a truly free plan for live agents, and it’s also an omni-channel solution, supporting web chat, WhatsApp, Facebook Messenger, and LINE simultaneously.

Our service grows with your business—start for free, and pay only when you need AI automation, when you need support 24/7, or when you need an extra hand from an AI agent.

- A truly free plan for manual responses by a human agent: unlike most competitors, the human agent can use the free plan to connect to multiple channels including webchat, WhatsApp, Messenger, and Line.
- 90% of our customers come to use the free 🆓 website chat widget!
- Chatbot has omni-channel support: web chat, WhatsApp, Facebook Messenger, LINE, SMS, and phone calls
- Supports over 30 document types (PDF, Excel, CSV, Word documents, images, websites, etc.) for knowledge base management 
- Integration with CRM, MailerLite, website builders like WordPress, Shopify, Wix, and Squarespace, Google Calendar, Twilio, ZenDesk, and more
- Multilingual support for global reach
- No code required


---


### Build Your First Agent

<!-- Source: getting-started/02-quick-start.md -->

<!-- Weight: 2 -->

*Set up AI agents with SeaChat. Integrate AI and human agents and manage workflows in under 10 minutes.*

---
* In just under 10 minutes, you'll have your own customized AI agent set up and ready to assist your customers.
* For more detailed guidance, please consult the [SeaChat User Manual](https://wiki.seasalt.ai/zh/seachat/manual/create-new-agent/). Should you encounter any issues or have questions, our [support team](#support) is on standby to assist you. Don't hesitate to reach out.
---

In this tutorial, we will create a SeaChat agent from scratch. This AI agent will help answer FAQs about a parking lot business. We will walk you through the process of creating the AI agent, adding knowledge to its knowledge base, testing and fine-tuning the agent to ensure it's ready to answer all incoming questions from customers!

## Step 1: Create a Workspace 
If this is your first time logging into SeaChat, you'll need to create a workspace to start the process. Click on **Create** to create your first workspace. I named my new workspace as **My Work Space**. You can give your workspace a different name! If you have existing workspace available, you can simply click on **Access** to visit the workspace.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240426-tutorial-intro-step1.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240426-tutorial-intro-step1.png" alt="An image illustrate the dashboard of workspace creation.">
</a>

*Create First Workspace*
</center>

> **What Is a Workspace ?**
>
>  A workspace serves as an information hub containing your organization's data, offering an overview of your agents, members, and API keys. You have the option to either create a new workspace for yourself or join an existing one by requesting an invitation from the admin.

## Step  2: Your First SeaChat Agent
Click on **Add New Agent** to configure your new agent. If you already have a workspace and an agent, you can create a new one by clicking on the dropdown menu located in the top-right corner next to your profile avatar.

> :books: **AI Agent and Live Agent**
>
>You will see the term, **Agent**, used throughout this tutorial. An **AI agent** is essentially an AI assistance with a custom knowledge base, we use the term to emphasize its capability to assist your customers like a real human agent. Whereas a **Live Agent** refers to an actual human agent who interacts with customers in real-time.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step2-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step2-rs.jpg" alt="An image that shows how to navigate to the dashboard of agent creation.">
</a>

*Add New Agent*
</center>

<br/>

Next, let's choose **Start From Scratch** to create a new agent. You can also choose to start from a **Use Case** if you prefer.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240426-tutorial-intro-step2-3.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240426-tutorial-intro-step2-3.png" alt="An image that shows how to navigate to the dashboard of agent creation.">
</a>

*Choose **Start From Scratch***
</center>

<br/>

In **New Agent**, we need to give our agent some context of its role and functions before you choose its use case and response language. After picking a creative name **My Parking Agent** for this tutorial, I will choose **FAQ** as my use case, since this agent will be used to answer frequently asked questions, and **US English** for the response language.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step2-2-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step2-2-rs.jpg" alt="An image the shows the interface of agent configuration.">
</a>

*Agent Configuration*
</center>

<br/>

<br/>

> :bulb: **Note** 
>
>  The live agent feature will require a human agent in case the customer wishes to be transferred to one. If you choose this option, the customer will then have the option to request a human agent during the chat, and you should arrange a human agent to respond to ongoing conversations.
> 

## Step 3:  Add Knowledge
To fully leverage the capabilities of your SeaChat agent, we need to add knowledge to its knowledge base. SeaChat offers a range of options for uploading content to your agent's knowledge base. Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. 

Feel free to try out the different ways to upload data to your knowledge base. For the purposes of this tutorial, we'll focus on utilizing the **Upload Spreadsheet** method. However, if you're interested in exploring additional data uploading techniques, we invite you to take a look at the [Add Knowledge](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/intro/) section within our user manual for comprehensive instructions and tips.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step3-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem;cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step3-rs.jpg" alt="An image that suggests the user to choose the upload spreadsheet method for uploading to agent's knowledge base.">
</a>

*Choose an Upload Method*
</center>

<br/>

## Step  4:  Upload Files to Knowledge Base
Uploading a spreadsheet is as simple as clicking on the upload icon and choosing the desired spreadsheet. Once you see your uploaded files in the preview section below the drag-and-drop section, click on the **Next** button to confirm. 
Now, my CSV file, ncc_Car_Parks (1) is uploaded, and we can see each header and its corresponding data in the preview section. My Parking Agent is now ready for the next step. 

Download the sample .csv file [here](/sample-files/ncc_Car_Parks.csv), and try it out yourself.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step4-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step4-rs.jpg" alt="An image that illustrate the dashboard of file upload">
</a>

*Review Uploaded File and Submit*
</center>

<br/>


To see the uploaded data of parking lots, we simply navigate to the **Existing** section in the top-right corner of the dashboard once your files have been successfully uploaded.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step4-2-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step4-2-rs.jpg" alt="An image that shows the success message when the file is uploaded">
</a>

*Uploaded Successfully*
</center>

<br/>

That’s it. Now, My Parking Agent has processed the uploaded data, and let’s set it up for a test to see if it needs further fine-tuning. Click on the **Test AI Agent** button located in the bottom-right corner. Let's try chatting with My Parking Agent to see if we can optimize its performance!

`<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step4-3-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem;cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step4-3-rs.jpg" alt="An image that indicates the location of the button, Test AI Agent">
</a>

*Click on **Test AI Agent***
</center>

<br/>`

## Step 5: Test Your SeaChat Agent

Before putting the AI agent we've just created into action, it’s crucial to train it through testing and fine-tuning. Imagine yourself as the customer interacting with the AI agent. You can now start asking any questions to see how your SeaChat agent responds.

With its updated knowledge base, My Parking Agent is now ready to be tested. You can start by asking questions to see how your agent responds after you click on the **Test AI Agent** button.

Here is what my agent has to say.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step5-1-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step5-1-rs.jpg" alt="An image that showcase the conversation with the AI agent.">
</a>

*Conversation with AI Agent*
</center>

<br/>

To review a message, hover over it and provide positive feedback to your agent with a thumbs up. If the message needs further review, give it a thumbs down.

Oops, it looks like My Parking Agent needs some fine-tuning. I will give a thumbs down here to provide a feedback.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step5-2-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step5-2-rs.jpg" alt="An image that shows how to review the agent's answers.">
</a>

*Review Agent's Response*
</center>

<br/>

## Step 6:  SeaChat Agent Fine-Tuning

SeaChat provides a set of sophisticated tools for you to fine-tune your agent to perfection. You can find these amazing features in the **Needs Review** section, accessible via the sidebar menu on the left. Here, you can review the responses that have received your feedback.


<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step6-1-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step6-1-rs.jpg" alt="An image indicates the button to modify agent's knowledge data.">
</a>

*Review Agent's Response*
</center>

<br/>

It looks like the information about Unicorn Road Car Park is missing in the knowledge base of My Parking Agent. I need to click on the CSV file that the missing information belongs to and add it.


<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step6-2-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step6-2-rs.jpg" alt="An image illustrate how to fine-tune your AI agent's responses.">
</a>

*Modify Relevant Documents*
</center>

<br/>

Now, click save once you are sure of the uploaded information. Don't forget to click on **Move to Reviewed** to consolidate your changes.
You can switch to **Reviewed** section to see the changes you've made. All done! Now, let's test the agent again to see if it has improved.

<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step6-3-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step6-3-rs.jpg" alt="An image that reminds the user to mark the reviewed message as reviewed.">
</a>

*Mark Conversation as Reviewed*
</center>

<br/>

Ta-da! My Parking Agent now is giving me the right information. It is that easy! You can now try it out yourself and see how your agent performs.


<br/>
<center>
<a href="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step6-4-rs.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/tutorial-intro/20240311-tutorial-intro-step6-4-rs.jpg" alt="An image illustrates the optimized performance of the AI agent.">
</a>

*Optimal Performance with Fine-tuned Responses*
</center>

<br/>

Fine-tuning your AI agent is a crucial and continuous process. We kindly advise you to check out the **Advanced** section in our user manual for a more comprehensive explanation and to understand the different parameters and features involved in the fine-tuning process.


##  Custom AI Agent at Your Service

Sit back and watch how SeaChat AI agents can elevate your operations. From customer service and marketing to serving as a collaboration coordinator, SeaChat empowers you to automate your workflows for optimal efficiency with ease.
In this tutorial, we've walked you through the steps necessary to set up your first AI agent. However, to fully unleash the power of SeaChat AI agent, there are a few more aspects for you to grasp. We kindly invite you to explore our detailed [user manual](https://wiki.seasalt.ai/seachat/getting-started/01-seachat-intro/) to understand the true potential of SeaChat, or you can directly contact our [support team](#support) for further information and assistance. 

## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

---


### Truly Free Plan as in Free 🍺 & 🎙️

<!-- Source: getting-started/01-seachat-free-agent-mode.md -->

<!-- Weight: 3 -->

*Truly free plan for web chat widget with unlimited chat and history.*

---


Introducing SeaChat's Human Agent Only Mode: Your Ticket to Unmatched Communication Freedom!

We’re thrilled to present the **SeaChat Human Agent Mode**, offering you **1 human agent free for life**—yes, you heard that right, for life!

### Why Choose SeaChat? Because It's **Truly Free!**

- **Unlimited Chat:** Engage in as many conversations as you need, with no caps.
- **Unlimited Chat History:** Never lose a conversation—access your chat history anytime.
- **Unlimited Contacts:** Build your network without any restrictions.
- **Freedom to Export:** Your data, your rules—export all your chat history effortlessly.


<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/tYLpWa3LeCM?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


**The Power of Freedom**

We believe in **absolute freedom**—both in terms of cost and control. With SeaChat, you’re not locked into any platform. Imagine enjoying the benefits of "**free beer**" 🍺 and "**free speech**" 🎙️ simultaneously!

**No Limitations, No Worries**

Unlike other options on the market that come with hidden catches—like restricted chat counts, limited history, or unexportable data—SeaChat offers you **true freedom** with no strings attached.

**Try SeaChat’s live agent mode now and embrace a world of endless possibilities!**

## How to Start using SeaChat for free?

### Step 1
Open an account at [SeaChat](https://chat.seasalt.ai/?utm_source=wiki). No credit card required. Our onboarding process will guide you through creating your first SeaChat agent. There’s only one thing you need to do to **use SeaChat without incurring extra costs — choose Human Agent Only under the Conversation Handling Mode option**.  

<br/>
<center>
<a href="/images/seachat/en/getting-started/free-human-agent-mode.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/getting-started/free-human-agent-mode.png" alt="An image illustrate the Conversation Handling Mode option. (Human Agent Only)" alt="Switch to Human Agent Mode">
</a>

*Choose Human Agent Only Mode*
</center>

**You will start with the free plan. You will only need to upgrade to a paid plan if you need to use AI-powered responses.**

The Human Agent Mode includes:
- Incoming message support across multiple channels (Web Chat – widget for your website, Facebook Messenger, WhatsApp, LINE)
- Manual response capability through a unified conversation panel (You will personally respond to all messages)
- Quota: 1 Agent (1 user account) and 1 workspace
- No hidden costs or usage limits -- unlimited chats and chat history

### Step 2
Install your new SeaChat agent to your [website](https://wiki.seasalt.ai/en/seachat/manual/channels/webpage/), [Facebook Messenger](https://wiki.seasalt.ai/en/seachat/manual/channels/facebook-messenger/), [WhatsApp](https://wiki.seasalt.ai/en/seachat/integrations/whatsapp/), and/or [LINE](https://wiki.seasalt.ai/en/seachat/manual/channels/install-to-line/).

### Step 3
Scale your business without spending money on customer service chatbots – until you need to.

---
## When do I need to pay?

We’ll support you in responding to customers manually across channels for free, as long as you need to scale your business.

Our customers often choose to upgrade to a paid SeaChat plan when they need to:

- Respond to many customer queries
- Provide prompt, intelligent, automated responses
- Answer based on a custom knowledge base
- Have 24/7 customer support
- Take customer phone calls
- Focus on more important tasks rather than handling repetitive requests

With SeaChat, you can enable or disable AI support anytime without changing your existing setup on all the channels. Enjoy the flexibility of on-demand AI support.


---


#### Create New Agent

<!-- Source: seachat-manual/02-create-agent/01-create-new-agent.md -->

<!-- Weight: 100 -->

*Create an AI agent with SeaChat using our guide to set up agents from scratch or predefined use cases.*


## How to Create a New Agent

If this is your first time using SeaChat, you will need to create a new agent. After creating your workspace or being invited to one, SeaChat will take you to the agent creation page. There are a lot of things to consider when creating an agent, and we suggest you to read more on [Agent Information](https://wiki.seasalt.ai/en/seachat/manual/create-agent/agent-information/) to understand the basic settings of your AI agent.

You may want to create a new agent for different use cases, languages, or different agent description. SeaChat allows users to create an agent from scratch or to utilize predefined use cases. Now, let's see how we can create a new agent using the two different methods.

First, let's start by using the **Add New Agent** button located next to your avatar.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/create-a-new-agent/create-new-agent-shortcut.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/create-a-new-agent/create-new-agent-shortcut.png" alt="Create Agent Shortcut | SeaChat Agent">
</a>
    <p style="margin-top: 20px; font-size: 15px">Create a New Agent Shortcut</p>
</div>
</div>

<br/> 

## Agent Creation Setup

Before we can start with the agent configuration, we have to first choose the method of creating the agent. You can either create an agent from scratch or pick a use case that suits your agent's purpose. 

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/create-a-new-agent/choose-creation-method.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/create-a-new-agent/choose-creation-method.png" alt="Create Methods| SeaChat Agent">
</a>
    <p style="margin-top: 20px; font-size: 15px">Choose Agent Creation Method</p>
</div>
</div>

<br/> 

### Name and Response Language

Pick a name for your agent. You can pick a name that describes the task that the agent will be responsible for. For example, I have an agent with a very straightforward name, Customer Service Agent. Note that this name is for internal use. If you want to change the agent name on Webchat Widget, please go to [Webchat Widget setting](https://wiki.seasalt.ai/en/seachat/manual/channels/webpage/).

In **Preferred Response Language**, pick a language that the agent will use to answer to your customer. I pick US English for the purpose of this tutorial. If you want your agent to be multilingual, you can choose "Always match user input language".

### Live Agent
Finally, you can enable [live agent](https://wiki.seasalt.ai/en/seachat/live-agent-transfer/) by checking the **Users can request a live agent during chat**.

### Use Case and Description

Depending on your choice of method to create an agent, your setup for the agent will be slightly different.

Generally, your choice of use case will come with a suitable prompt designed by the SeaChat team for that specific scenario. Our predefined prompt will help train the AI agent to understand its primary task in a conversation. Additionally, the description field is used to provide supplemental information. In this field, you will describe your business and give more details about the agent. Together, the base prompt provided with the use case and the information in the description field will form the complete prompt for the AI agent.

We will look into the difference in these two methods below:

## Custom AI Agent: Start from Scratch

If you want to configure your agent with an existing prompt description or create a brand-new definition, you may choose to start from scratch, as this gives you full control to customize your prompt. For users who already have instructions, this is the best approach.

First, choose a use case for your agent, and then input the description that defines your agent's behavior. Once you have completed the setup, click on **Create** to finish the process.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/create-a-new-agent/start-from-scratch.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/create-a-new-agent/start-from-scratch.png" alt="Create from Scratch | SeaChat Agent">
</a>
    <p style="margin-top: 20px; font-size: 15px">Create an AI Agent from Scratch</p>
</div>
</div>

<br/> 

## Click to Start: Pick a Use Case

A use case can help you quickly set up your agent and start your conversation. Choose a use case that suits your agent's purpose, and then define your agent's description.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/create-a-new-agent/pick-a-use-case.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/create-a-new-agent/pick-a-use-case.png" alt="Create from Use Case | SeaChat Agent">
</a>
    <p style="margin-top: 20px; font-size: 15px">Pick a Use Case</p>
</div>
</div>

<br/> 

Unlike starting from scratch, a use case comes with predefined instructions prepared by SeaChat. You can enter your own description, which will be appended to these instructions. This way, you can provide context to your agent along with the predefined instructions.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/create-a-new-agent/choose-a-use-case.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/create-a-new-agent/choose-a-use-case.png" alt="Creation Use Cases | SeaChat Agent">
</a>
    <p style="margin-top: 20px; font-size: 15px">Define Agent Description</p>
</div>
</div>

<br/>




---


#### Agent Information

<!-- Source: seachat-manual/02-create-agent/01-agent-information.md -->

<!-- Weight: 101 -->

*Explore SeaChat's AI agent information section to set up your AI agent. Use case and other agent details*


# Overview

Agent information is the core of your AI agent. It contains all the necessary information about your agent, including its name, description, and other advanced settings like context extraction. In this tutorial, we will walk you through each of the attribute that you will find in **Agent Information** under **Agent Configuration**.

---

## Basic Setting in Agent Information

SeaChat allows you to configure your AI agent's information such as names, use case, and description. Inside **Basic Setting**, users can set the following fields:

### Name
The name of your AI agent. This name will be displayed in the conversation window.

> :page_facing_up: **NOTE**
> 
> This will be the name of your agent for the purpose of agent management. If you wish to change the displayed name in your agent integration. Please refer to [Webpage Integration](https://wiki.seasalt.ai/en/seachat/manual/channels/webpage/).


### Use Case
The use case of your AI agent. This will help you to categorize your AI agent. SeaChat provides a list of use cases to choose from. Depending on your needs, you can choose a use case that best fits your AI agent. Different use cases might require different description settings, but you can simply follow the instructions in the description section when incorporating a use case.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/use-case-examples.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/use-case-examples.png" alt="image that display the use case options available in SeaChat">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Choose a use case for your AI agent</p>
</div>

### Description
A brief description of your AI agent that details your agent's behavior and its reference. Whatever you put inside the description field will show up in agent instructions on the right-hand side of the page. This description will then be used to prompt a language model to generate responses.

The use case comes with a basic prompt. Description is where you can customize the bot even more by appending/inserting a description about your agent into the prompt. To view full prompt, you can check the right-hand side of the page.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/description-preview.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/description-preview.png" alt="image showcasing how to write an agent description">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent Description</p>
</div>

### Response Language
By choosing a response language, you can help frame the conversation and ensure that the AI agent responds in the correct language. This is especially useful when you have a multilingual audience. 

Take English language as an example, standard US English and UK English nuance in many ways. By setting the response language to US English, the AI agent will optimize the response to match the US English.

This is how it works:
- If a user has a preferred response language, they should select **Respond in the user's language**.
- If a user does not specify a preferred response language but wants the AI agent to reply in the language of the user’s message, they should select **Always respond in the selected language** box. 

If the user's message contains multiple languages, the AI agent will respond in the language that appears most frequently or is the most prominent within the message.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/response-language.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/response-language.png" alt="image showcases the options of response language">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent's Response Language</p>
</div>

### Live Agent
The live agent feature allows a human agent to intervene in the conversation when needed. If you enable this feature, your customer will have the option to request a live agent or leave a message during the chat conversation. This requires you to provide a real-human agent that will monitor and respond to the user. 

You can disable this feature by unchecking the box such that your user cannot request a human agent during the conversation. However, SeaChat admins and agents can intervene in the conversation from the SeaChat Conversation section.

> :page_facing_up: **NOTE**
> 
> If no agent is online, the customer can leave a message. The human agent can review the conversation summary and respond during work hour.

### Test your AI Agent
You can immediately test the AI agent that you have just built. In **Agent URL**, you can click the URL to interact with your AI agent in a standalone window. 

Or if you wish to integrate your AI agent into your website, you can also access your API key in the **API Key** section. Please check out the [Webpage Integration](https://wiki.seasalt.ai/en/seachat/manual/channels/webpage/) for more information on how to programmatically integrate your AI agent into your website.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/additional-options.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/additional-options.png" alt="image that displays the additional options in Basic Settings">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Additional Options in Basic Settings</p>
</div>


## Chat Design Style

### Style Settings

SeaChat allows you to design your own web chat widget. You can customize the chat widget to match your brand's color scheme and style. You can choose from a variety of colors and styles to create a chat widget that fits your brand's aesthetic. Everytime you make a change, you can preview the chat widget in real-time to see how it will look on your website by clicking on the **Preview** button.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/style-setting.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/style-setting.png" alt="image that displays the additional options in Style Settings">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Customizable WebChat</p>
</div>

### Chat Settings

In addition to the style settings, you can also customize the chat settings. This feature can reduce the amount of time that your AI agent editor spends on basic conversational trainings. You can set the chat settings to automatically set-up the conversation flow, such as greeting messages, conversation start messages, and conversation end messages.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/agent-information/chat-setting.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/chat-setting.png" alt="image that displays the additional options in Chat Settings">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px"> Personalized Chat Settings </p>
</div>

## Advanced Settings

We suggest you to refer to the [Advanced Settings](https://wiki.seasalt.ai/en/seachat/manual/create-agent/advanced-settings/rag/) tutorial to learn more about the advanced features available in SeaChat. For feature such as context extraction and Retrieval Augmented Generation (RAG), you can find them in the **Advanced Settings** section under **Agent Information**.



---


#### Agent Version Control

<!-- Source: seachat-manual/02-create-agent/03-agent-duplicaiton.md -->

<!-- Weight: 102 -->

*Efficiently duplicate and manage AI agents in SeaChat. Create, test, and handle agent versions smoothly.*



## Agent Duplication

> 📍What is duplicated?
> 
> When an agent is duplicated or replaced, the agent's basic info, advanced settings, knowledge base, and widget are concerned. Channels cannot be duplicated or replaced.

Agent duplication is a feature that allows you to create a new agent based on an existing one. This is useful when you want to create a new agent with similar settings as an existing one.

To duplicate an agent, click on the Agent Duplicate button located next to the agent you want to duplicate in Agents under Workspace. This will create a new agent called {Agent Name} (COPY) with the same settings as the original agent. You can then modify the settings by clicking on Edit or by going to Agent Information.

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/create-a-new-agent/agent-duplication-btn.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
      <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/create-a-new-agent/agent-duplication-btn.png" alt="Duplicate Button | SeaChat Agent Duplicate">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Duplicate Agent Button</p>
  </div>
</div>

<br/>

This feature is very powerful for agent editors when prototyping new agent settings and separating development and production agents for testing and optimization.

This process might take some time depending on the complexity of the agent. Once you see the success message, you can start training your agent. Everything is set up, including the available knowledge base and agent information.

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/create-a-new-agent/duplication-confirmation.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
      <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/create-a-new-agent/duplication-confirmation.png" alt="Confirm Duplication | SeaChat Agent Duplicate">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Duplication Confirmation</p>
  </div>
</div>

<br/>

For users with integrations or channels connected to the original agent, you will need to update the integration to include the new agent copy since the agent copy is still a new agent.

## Agent Replacement

> 📍What is replaced?
> 
> When an agent is duplicated or replaced, the agent's basic info, advanced settings, knowledge base, and widget are concerned. Channels cannot be duplicated or replaced.

The agent replacement feature provides an efficient way to manage different versions of your agent.

This is particularly useful when you want to develop an existing agent without affecting the original version. By using this feature, agent editors can make changes to a copy of the original agent rather than modifying the original agent directly.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/create-a-new-agent/replace-button.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/create-a-new-agent/replace-button.png" alt="Agent Replacement | SeaChat Agent Duplicate">
</a>

**Agent Replacement**
</center>

A common use case might look like this:

1. Duplicate the original Agent A and name the copy Agent B (Agent A Copy).
2. Add new features to Agent B and test them.
3. Once development is complete, replace Agent A with Agent B.
4. Now, the new agent is running in production with the original settings from Agent A and the new features implemented in Agent B.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/create-a-new-agent/replacement-workflow.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/create-a-new-agent/replacement-workflow.jpg" alt="">
</a>

**Agent Replacement Workflow**
</center>

By following this process, you can keep the original agent running in production while developing and testing a new version of the agent.

---


#### Live Agent

<!-- Source: seachat-manual/02-create-agent/02-live-agent-transfer.md -->

<!-- Weight: 103 -->

*Set up live agent transfers in SeaChat for customer support. Manage live conversations across channels.*

A live agent is a human agent who can take over the conversation from the AI agent when needed. Not only can live agents take over the conversation, but they can also provide the virtual agent with new knowledge, and help train the virtual agent by testing and fine-tuning the response of the AI agent.

Depending on your SeaChat channel, it might take different configurations to enable the live agent feature. SeaChat offers many integration configurations and channels. We recommend you refer to [Integration](https://wiki.seasalt.ai/seachat/integrations/seax-seachat/) or [Channels](https://wiki.seasalt.ai/en/seachat/manual/channels/webpage/) to learn how to set up your agent properly.

In this tutorial, we will show you how to transfer to a live agent during chat conversations and how to set it up, using the different methods that SeaChat provides.

## Setting it up

Before you integrate your custom AI agent into your production, we need to make sure that the live agent feature is enabled in your SeaChat account. Go to **Agent Information** under **Agent Configuration**. You can see all the basic settings for your AI agent. If you want to reconfigure your agent or simply to have an overview of your agent, you can do them all here.

At the bottom of the screen, you can see the checkbox that says ***Users can request a live agent during chat***. Make sure to check this box to enable the live agent feature.

> :exclamation: **IMPORTANT** :exclamation:
>
> If you choose to enable the feature of the live agent, your customer will now have the option to request a live agent during the chat conversation. This requires you to provide a real-human agent that will monitor and respond to the user.

<br/>
<a href="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-1.png" alt="Set up Step | SeaChat Live Agent Transfer">
</a>
<br/>

## Talk to Customer as a Live Agent
Find the **Conversations** section from the sidebar menu on the left. Here you can see all the conversations that your AI agent has had with your customers. You can see the conversation history and the status of the conversation and this is the control center of your live agent's conversation.

If a customer requests a live agent during the chat conversation, the human agent will see a notification pop-up that indicates the request. If the list of conversations gets too long, simply click on the **Live Agent** button to see the list of conversations that live agents need to complete.

<br/>
<a href="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-2.png" alt=""Conversation | SeaChat Live Agent Transfer>
</a>
<br/>
<br/>

That's it. You have now set up a Live Agent Transfer function for your SeaChat AI Agent. You can have a live agent take over the conversation to further assist your customer. Once the live agent has completed the request that the customer has, the live agent must click on the **Complete** button to give the conversation back to the AI agent.

<center>
<a href="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-3.png" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-3.png" alt="Complete Conversation | SeaChat Live Agent Transfer">
</a>
</center>
<br/>

Once the live agent has completed the conversation, the conversation will be marked as completed and the customer will be notified that the conversation has been completed. Live agents can also reactivate the conversation when needed. Simply click on the **Reactivate** button to restart the conversation.


### Markdown Support

SeaChat conversations support url and Markdown formats in its web channel. Both your live agents and your users can insert links and Markdown text in the chat conversation.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/live-agent-transfer/markdown-support-in-response.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/markdown-support-in-response.png" alt=" Markdown Support | SeaChat Live Agent Transfer">
</a>
    <p style="margin-top: 20px; font-size: 15px">Markdown Support in Agent Response</p>
</div>
</div>

<br/> 

The conversation will be displayed in the same format as it was inputted. This feature is especially useful when information needs to maintain its original format for readability. You can easily copy and paste the information to the conversation without losing the format. Currently, the markdown support only applies to the web chat integration.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/live-agent-transfer/markdown-response-in-web-ui.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/markdown-response-in-web-ui.png" alt="Markdown Support in Response | SeaChat Live Agent Transfer">
</a>
    <p style="margin-top: 20px; font-size: 15px">Markdown Support in WebChat UI</p>
</div>
</div>

<br/> 


## How to Request Live Agent on WebChat

> :open_book: **Note** :open_book:
>
> The WebChat widget will be the same for **Shopify** and **Squarespace**. The only difference is the way you integrate the widget into your website.
>
> Check [Integration](https://wiki.seasalt.ai/seachat/integrations/seax-seachat/) for more information on how to do it.


The WebChat Channel is a channel that allows you to embed the SeaChat widget on your website. This channel is the most common channel used by businesses to provide customer support.

The chat conversation will let your customer know how many live agents are currently available, and they can request a live agent during the chat conversation by clicking the ***Talk to Live Agent*** button.

<br/>
<a href="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-web-widget-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-web-widget-1.png" alt="Request Live Agent | SeaChat Live Agent Transfer">
</a>
<br/>

If your AI agent is deployed to a non-webchat channel, such as Messenger and WhatsApp, then they cannot display the button. Instead, users can ask for a live agent transfer verbally like the following:

<br/>
<a href="/images/seachat/en/live-agent-transfer/ask-to-chat-with-live-agent.jpeg" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/ask-to-chat-with-live-agent.jpeg" alt="Request Live Agent | SeaChat Live Agent Transfer">
</a>
<br/>


You can enable this feature separately via the following setting:


<br/>
<a href="/images/seachat/en/live-agent-transfer/settings-ask-to-chat-with-live-agent.jpeg" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/settings-ask-to-chat-with-live-agent.jpeg" alt="Request Live Agent | SeaChat Live Agent Transfer">
</a>
<br/>





## How to Request Live Agent on LINE

Once you have integrated the LINE channel, your customer will see the **Live Agent** button at the bottom of the LINE chat. The customer can click on the **Live Agent** button to request a live agent during the chat conversation.

<center>
<a href="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-line-channel.png" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/20240325-live-agent-transfer-line-channel.png" alt="Live Agent on Line | SeaChat Live Agent Transfer">
</a>
</center>
<br/>

## Hybrid Mode (AI Agent + Human Agent)


Besides the human-only and AI-only modes, SeaChat also offers a hybrid mode where both human agents and AI agents can work together to provide customer support. 

The hybrid (AI Agent + Human Agent) combines the strengths of both human agents and AI agents. This creates much more flexibility in providing customer support. 

As the result of such flexibility, here are feature options that users can only find in the hybrid mode:

### 1.  Do not let customers request a live agent proactively

If selected, **Show Summary** and **Automatic Switch to AI Agent** features  should hide or grey out, and the users should not be able to request a live agent during the chat conversation.

<center>

<a href="/images/seachat/en/live-agent-transfer/do-not-request.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/do-not-request.png" alt="Live Mode Timeout | SeaChat Live Agent Transfer">
</a>
</center>
<br/>

### 2. Show Summary
If selected, everyone in the chat can see the summary of the conversation. 

<center>
<a href="/images/seachat/en/live-agent-transfer/remove-live-agent.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/remove-live-agent.png" alt="Remove Live Agent | SeaChat Live Agent Transfer">
</a>
</center>
<br/>

### 3. Automatic Switch to AI Agent

Sometimes, a human live agent might have to deal with a lot of the conversation at once, and they can forget to click on the **Complete** button to give the conversation back to the AI agent. 

To prevent this from happening, you can set up an automatic timeout for the live agent feature. This will automatically complete the conversation if there is no activity from the chat for a certain amount of time.

<center>
<a href="/images/seachat/en/live-agent-transfer/auto-timeout.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/live-agent-transfer/auto-timeout.png" alt="Auto Transfer Back to AI Agent">
</a>
</center>
<br/>

## :dart: Troubleshooting

### Remove Live Agent Feature
If you wish to deactivate the live agent feature, simply uncheck the box that says ***Do not let customers request a live agent proactively*** in the **Basic Settings** in your **Agent Information**. 

This will disable the live agent feature and your customers will no longer be able to request a live agent during the chat conversation, nor will they see the **Live Agent** button.

> :pushpin: Note
>
> Live agent, if available, will still be able to monitor and take over conversations in **Conversations**. Unchecking the box only removes the option for customers to request a live agent.
> 



---


#### Conversations

<!-- Source: seachat-manual/02-create-agent/04-seachat-conversations.md -->

<!-- Weight: 104 -->

*Manage customer interactions with Conversations board. Access details, history, and download audio files.*


## Conversation Dashboard
The conversation dashboard is where you can view and manage all the conversations that your agents are handling. You can view the details of each conversation, check the conversation history, and manually answer users' questions.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/seachat-conversation/conversation-dashboard.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/seachat-conversation/conversation-dashboard.png" alt="Conversation Dashboard | Agent Conversation">
</a>

**Agent Conversations View**
</center>



Users can switch between all conversations and live agent conversations. In live agent conversations, users can view conversations that have been handled by live agents.

In each conversation row, there will be an icon indicating the conversation channel e.g. WhatsApp, phone calls etc. You can easily identify the communication channel of conversation through these icons.

## Download Audio Conversation

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/seachat-conversation/download-audio.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/seachat-conversation/download-audio.png" alt="Download Audio | Agent Conversation">
</a>

**Download Audio Conversations**
</center>

For conversations with phone icons, you can download the audio conversation by clicking on the download icon inside the conversation. The audio conversation will be downloaded in `mp3` format. This is a useful tool for quality assurance and training purposes, as you can listen to the conversation between the agent and the user and provide critical feedback to fine-tune the agent's responses.

## Download Agent Conversation History

If you wish to download the conversation history of certain agent conversations, you can do so by navigating to **Workspace*  - `-> **Agents**. 

Click on **Download Conversations*  - `and Choose the year of the conversation history you wish to download. 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/seachat-conversation/download-conversation-history.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/seachat-conversation/download-conversation-history.png" alt="Download Conversation History | Agent Conversation">
</a>

**Download Conversation History**
</center>

This process might take a while depending on the size of the conversation history. Once the download is ready, you will receive a system notification says `AI agent conversation history export successful. Please click link or copy the link to browser to download. The link will expire in 24 hours.`

Click on the link to download the conversation history in a zip file format. 

You will see the conversation history in a CSV file format. The CSV file contains the following columns:

| Sender type | Channel type | Sender name | Time in GMT | Message | Data |
|-------------|--------------|-------------|-------------|---------|------|

- **Sender type**: The type of sender. You can identify whether the sender is the agent, system notification, user, etc.
- **Channel type**: The communication channel of the conversation. The following is the list of channel types:
   - `System (this means system message)`
   - `WebChat`
   - `SeaAuth (this is usually for verification purpose)`
   - `Line`
   - `WhatsApp`
   - `Messenger`
   - `Instagram`
   - `Voice (this means phone calls)`
   - `ThirdPartyClient`
   - `AgentPhone (this means phone calls from SeaChat voice agent, usually for token verification purposes)`
   - `SeaX_Call (this means phone calls through SeaX)`
   - `SeaX_SMS (this means SMS through SeaX)`
- **Sender name**: The name of the sender. You will find the senders' ID or Email in this column if the sender is an actual user. Otherwise, it will be an identifier from the system.
- **Time in GMT**: The timestamp of the message in GMT format.
- **Message**: The message content of the conversation. Most of the time, this field contains plain text messages. However, it can also include specific command types, such as:
   - `/live_agent:  User requests conversation transfer to a live agent.`
   - `/submit_form: User submits a form. If an entity is involved, the command will appear as /submit_form{"entity_name":"entity_value"}.`
   - `/clear_history: User requests the bot to forget the conversation history and start fresh.`
   - `/ai_agent: User requests conversation transfer to an AI agent.`
- **Data**: The data content of the conversation in JSON format. This column will be empty if there is no data content in the conversation. When data is present, it can include, but is not limited to, the following types:
   - `Image URL that gets sent in the message.`
   - `Recording file URL of the voice call.`
   - `A form that the user completes during the chat.`


---


#### Analytics

<!-- Source: seachat-manual/02-create-agent/06-analytics.md -->

<!-- Weight: 105 -->

*Monitor statistics about conversation and messages with your bot over time.*


## SeaChat Analytics
### Overview
The SeaChat Analytics feature provides valuable insights into user interactions with your AI chatbot. This dashboard enables you to track key performance metrics over time, helping measure engagement, optimize chatbot performance, and make data-driven decisions. Navigate to the `Analytics` tab below `Agent Configuration` to view the analytics page for a specific bot.

📊 Track Chatbot Performance
Monitor the number of conversations, unique visitors, and message activity to understand how users are engaging with your chatbot.

📈 Measure Growth and Trends
Compare data across different time ranges (Last 7 Days, Last 30 Days, etc.) to identify trends in chatbot usage and user behavior.

🤖 Optimize Chatbot Responses
Analyze bot message statistics to see how effectively the chatbot is handling conversations and refine responses for better user satisfaction.

👥 Improve Customer Engagement
By tracking live agent requests and user interactions, businesses can identify opportunities to enhance customer support and automation strategies.

🔄 Data-Driven Decision Making
Use real-time analytics to refine chatbot workflows, improve response accuracy, and optimize user experience based on actual usage patterns.

### Settings

At the top of the page, there are a couple settings you can configure. First, select the timezone you would like the data to be presented in. Second, check the box for whether or not you would like to include conversations that have *no messages from the user*. For example, if a user opens the webchat and reads the welcome message, but does NOT send a message, the conversation will still be created and show up in the conversation statistics. If you check the setting box, conversations like this with no user messages will be *excluded* from the statistics.

By default, the dashboard data will update every hour. If you would like to refresh the data on demand, click the "Refresh Data" button.

### Basic Metrics

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/01-seachat-analytics-settings-metrics.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/01-seachat-analytics-settings-metrics.png" alt="SeaChat Analytics Basic Metrics">
</a>

**SeaChat Analytics Basic Metrics**
</center>

The Metrics section in SeaChat Analytics provides a detailed breakdown of your chatbot's performance over a selected time range. You can customize the date range by choosing from:

- Last Day
- Last 7 Days
- Last 30 Days
- Last 90 Days
- Last 180 Days

Once a time range is selected, SeaChat will compare the chatbot's performance during that period to the same length of time immediately before it. For example:

> If you select Last 7 Days, the displayed metrics will compare the last 7 days to the previous 7-day period.

> If you select Last 30 Days, it will compare the last 30 days to the 30 days before that.

#### Understanding the Metrics
The key performance indicators (KPIs) displayed include:

- Conversations – The total number of chatbot interactions initiated during the selected time period.
- Unique Visitors – The number of distinct users who interacted with the chatbot.
- Messages Received – The number of messages sent by users to the chatbot.
- Bot Messages Sent – The number of responses generated by the chatbot.
- Live Agent Requests – The number of times users requested a human agent.
- Agent Messages Sent – The number of messages sent by live agents in conversations.

Each metric includes a percentage change indicator, showing how it has increased or decreased compared to the previous equivalent time period. Green arrows indicate positive growth, while red arrows (if applicable) indicate a decline.

This comparison helps businesses track chatbot performance trends over time, evaluate improvements, and identify areas for optimization.

### Conversation Yearly Overview

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/02-seachat-analytics-conversations-by-year.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/02-seachat-analytics-conversations-by-year.png" alt="SeaChat Analytics Conversation Yearly Overview">
</a>

**Conversation Yearly Overview**
</center>

The Conversation Overview section in SeaChat Analytics provides a high-level summary of chatbot interactions for a selected year. Users can choose a specific year from the dropdown menu to view key statistics on chatbot engagement during that period.

- Total Number of Conversations – Displays the total count of chatbot conversations for the selected year.
Average Number of Messages Per Conversation – Shows the average number of messages exchanged per conversation, helping assess user engagement levels.
- Total Messages by Month

Below the key metrics, a line graph visualizes the total number of messages exchanged with the chatbot each month. This allows users to:

- Identify trends in chatbot activity over time.
- Spot seasonal fluctuations or spikes in engagement.
- Assess the impact of business campaigns or chatbot improvements on conversation volume.

### Conversation & Messages Breakdown

The Conversations Breakdown by Day, Time & Channel section allows users to analyze chatbot interactions across various channels and time periods within a custom date range. By selecting a specific start and end date, businesses can gain detailed insights into when and where most of their interactions are occurring.

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/03-seachat-analytics-conversation-breakdown-by-channel.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/03-seachat-analytics-conversation-breakdown-by-channel.png" alt="SeaChat Analytics Channel Breakdown">
</a>

**Channel Breakdown**
</center>

The channel breakdown table displays the following data for each channel:

- Channel – The different communication channels through which users are interacting with the chatbot (e.g., Webchat, LINE, WhatsApp, Voice, Messenger, etc.). All channels offered by SeaChat will automatically appear in the table once they have traffic.
- Unique Visitors – The number of distinct users who engaged with the chatbot via each specific channel within the selected time frame.
- Inbound Messages Received – The total number of messages sent by users across each channel during the selected date range.

#### Setting Up Sub-Channel Tracking
The SeaChat WebChat widget allows you to install a chat window directly in your own website.
Some clients add the webchat widget to multiple sites and want to be able to track the amount of traffic from the widget on each site separately.
By default, the channel breakdown will lump all the webchat traffic together into a single channel type called `WEBCHAT`.
However, with a simple customization to the WebChat widget code, you can provide a specific "subchannel" name to each instance of the widget and track the traffic separately.
Once you customize the webchat widget with subchannel information, all subsequent traffic will appear as `WEBCHAT - {subchannel}` in the table.

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/06-seachat-widget-subchannel-setup.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/06-seachat-widget-subchannel-setup.png" alt="SeaChat Analytics WebChat Subchannel Setup">
</a>

**WebChat Subchannel Setup**
</center>

Navigate to `Channels` -> `WebChat` -> `Install Widget` to find the WebChat widget code.
Within this code block, there are four instances of your chatbot's webchat URL - it looks like this: `https://chat.seasalt.ai/chat/{chat_config_id}`.
To distinguish different subchannels, simply append to following to the end of the URL: `?channel={subchannel_name}`. 
For example, say you want to add the WebChat widget to your homepage as well as your wiki site.
You could update the URL `https://chat.seasalt.ai/chat/aaaabbbbccccdddd` to `https://chat.seasalt.ai/chat/aaaabbbbccccdddd?channel=homepage` and add the widget code to your homepage.
Then you could update the URL again to `https://chat.seasalt.ai/chat/aaaabbbbccccdddd?channel=wiki` and add the code to your wiki site.
In the channel breakdown, you would see traffic from two separate channels: `WEBCHAT - homepage` and `WEBCHAT - wiki`.

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/04-seachat-analytics-messages-by-day-of-week.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/04-seachat-analytics-messages-by-day-of-week.png" alt="SeaChat Analytics Day of the Week Breakdown">
</a>

**Day of the Week Breakdown**
</center>

The 'Day of the Week' breakdown allows you to see how many user messages are sent to your bot on each day of the week. This allows you to identify trends of when users are engaging with your bot.

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/analytics/05-seachat-analytics-messages-by-hour-of-day.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/analytics/05-seachat-analytics-messages-by-hour-of-day.png" alt="SeaChat Analytics Hour of the Day Breakdown">
</a>

**Hour of the Day Breakdown**
</center>

The 'Hour of the Day' breakdown allows you to see what time of day users are sending messages to your bot. This allows you to identify trends of when users are engaging with your bot, and may help with making decisions such as what times to have live agents online.

---


##### Retrieval Augmented Generation (RAG)

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/02-retrieval-augmented-generation-rag.md -->

<!-- Weight: 105 -->

*Enhance SeaChat AI with Retrieval Augmented Generation (RAG). Design query patterns to boost performance.*


## Overview

Retrieval Augmented Generation (RAG) is a pivotal feature within SeaChat, enhancing data retrieval and augmenting the accuracy of interactions with the AI agent. It provides you with the ability to change settings for Query Pattern, Search Method, and Knowledge Base Retrieval Count. By experimenting with these settings, you can customize how your AI agent interacts with the knowledge base efficiently.

---

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-rag-ui" href="/images/seachat/en/agent-advanced-settings/rag-dashboard.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-advanced-settings/rag-dashboard.png" alt="image of the Retrieval Augmented Generation (RAG) feature in SeaChat">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">RAG Settings in SeaChat</p></p>
</div>

## [Query Pattern](#seachat-rag-ui)

Whether you require comprehensive context, focused engagement, or quick, precise responses, SeaChat's flexible query patterns for querying the knowledge base ensure an optimized chat experience tailored to your preferences.

The following is an example conversation between a customer and a parking lot FAQ AI agent with information of more than hundreds of parking lots in the knowledge base:

---

👨 (Previous Query): Is there a parking lot near the Seattle Space Needle?

🤖️ (Bot Response): Yes, you can park at the ABC Parking Lot on 123rd Ave NE. It has 50 parking spots. The parking fee starts at $10 per hour, with a daily maximum of $60.

👨 (Current Query): I will be working near there. Can I rent a parking spot monthly?

---

### Previous Query &#8594; Bot Response &#8594; Current Query

Offers comprehensive context by incorporating the last three turns of the conversation. In this case, the complete conversation (Previous Query + Bot Response + Current Query) is used to query the knowledge base and to generate the AI agent's next response for Current Query.

### Previous Query &#8594; Current Query

Focuses more heavily on the user’s requests and is not influenced by the AI agent’s response. It includes the last two user inputs (Previous User Query and Current User Query) to query the knowledge base and to generate the AI agent's next response.

### Current Query

Provides a succinct approach, considering only the user's latest input, i.e. Current User Query, for the AI agent's next response. This is ideal for one-turn dialogues or cases where users frequently switch topics. However, it may miss important context when discussing the same topic over multiple turns.

## [Search Method](#seachat-rag-ui)

You can optimize knowledge base search by choosing from distinct knowledge base search methods:

### Keyword Search

Matches user’s provided keywords against the knowledge base to deliver relevant results. This works well when you have unique tokens such as product names, locations, IDs, etc. but may miss cases where the user doesn’t say the exact keyword (for example, they use a synonym or a different language than the KB document).

### Vector Search

Utilizes the capabilities of text embedding to enhance the retrieval of relevant information. Vector search can work well across languages and retrieve similar documents even if they don’t have matching keywords. However, it may struggle with rare tokens such as product names, locations, or IDs.

### Hybrid Search

Integrates both Keyword and Vector Search methods to optimize information retrieval.

## [Knowledge Base Retrieval Count](#seachat-rag-ui)

Changing Knowledge Base Retrieval Count allows you to specify the number of KB documents(chunks) to retrieve, ensuring efficient information retrieval. These retrieved documents will serve as important contexts for AI agent responses at each turn. The ideal count is flexible and depends on the token limits and document types.

### Considerations for setting the count

- **Too Few Documents/Chunks**

You may miss essential information, leading to incomplete or inaccurate responses from GPT.

- **Too Many Documents/Chunks**

Important information may get buried under irrelevant details, making it harder for GPT to provide accurate responses.

- **Context Limit**

There is a limit to the amount of context that can be provided with each request. If the retrieved documents exceed this limit, SeaChat will use as many documents as can fit within the limit.

By adjusting the KB retrieval count, you can optimize the balance between depth of information and resource usage, ensuring accurate and efficient responses.

## Knowledge Base Search Refinement

SeaChat now offers an advanced feature called Knowledge Base Search Refinement that allows you to further enhance the quality of retrieved information. This feature enables the AI to perform a secondary refinement on preliminary search results before generating responses.

### Configuring KB Search Refinement

You can enable this feature in the Agent Information's Advanced Settings page:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement" href="/images/seachat/en/agent-advanced-settings/kb-refinement.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-advanced-settings/kb-refinement.png" alt="image of the Knowledge Base Search Refinement feature in SeaChat">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">KB Search Refinement Settings in SeaChat</p></p>
</div>

### Optional KB Refinement Instructions

Simply enabling this feature without any additional instructions is sufficient for most use cases. The system will automatically refine search results using default optimization strategies. Custom instructions are optional but can significantly enhance performance for specific scenarios.

For more precise control over how the LLM refines search results, you can provide custom instructions in the text field. These instructions guide the AI on:

- How to evaluate document relevance
- Which types of information to prioritize
- How to handle ambiguous queries
- Special considerations for your specific knowledge domain

#### Example Instructions

Here are some examples of effective refinement instructions:

- "Prioritize documents containing specific product codes when the user asks about product specifications."
- "For parking-related queries, focus on documents with location information that matches the user's mentioned area."
- "When handling technical support questions, prioritize the most recent documentation over older versions."
- "For multi-part questions, ensure that documents addressing all parts of the query are included."
- "When summarizing the conversation history, include the branch name if it can be inferred from the discussion, ensuring that it reflects the branch the user intended in the last query, even if not explicitly mentioned."
- "When identifying relevant articles, exclude those related to branches different from the one mentioned in the summary, provided the summary specifies a branch name."

### Benefits of KB Search Refinement

Enabling this feature can significantly improve your AI agent's performance by:

- Providing more accurate and relevant responses
- Reducing information overload in complex knowledge bases
- Handling ambiguous queries more effectively
- Improving the contextual understanding of user questions
- Delivering more concise and focused answers

By fine-tuning your KB Search Refinement settings, you can create a more intelligent and responsive AI agent that better understands and addresses your users' specific needs.

### 📌 Example 1: Handling Multi-Branch Knowledge with KB Search Refinement

Imagine you run a restaurant with five different branches. In your knowledge base, you’ve collected menus, service details, hours, and promotions for each branch in a spreadsheet. When users ask about a specific branch, you want your AI agent to answer with accurate, branch-specific information.

To enhance your AI agent’s performance, there are two powerful ways to improve how it processes user queries:

**1. Include Branch Names in Your Knowledge Base Entries**

For every cell or row in your Excel sheet, add the branch name to the content it refers to.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement" href="/images/seachat/en/agent-advanced-settings/kb-refinement-example.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-advanced-settings/kb-refinement-example.png" alt="An example spreadsheet contains five restaurant branches">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Example Spreadsheet: Multi-Branch Knowledge Base with Branch-Specific Tags</p></p>
</div>

This ensures that when AI agent's reads the knowledge base content, it understands which branch the information belongs to, improving its relevance when forming a response.

**2. Upload Spreadsheet**

Upload this spreadsheet to your knowledge base through the **Upload Spreadsheets** card.  And choose this option to upload each row in the table as an individual KB document.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement" href="/images/seachat/en/agent-advanced-settings/kb-refinement-upload2.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-advanced-settings/kb-refinement-upload2.png" alt="Upload each row as an individual kb article">
    </a>
</div>
</div>
<br/>


**3. Use KB Search Refinement to Filter Irrelevant Results**

Enable Knowledge Base Search Refinement feature and add refinement instructions:
```
Extract the branch name from user’s query.
Exclude articles or rows that refer to branches other than the one mentioned.
```

With these instructions, even if your initial KB search returns a mix of results from all branches, the AI agent will automatically filter out unrelated content and keep only what’s relevant to the user’s intended branch—leading to more accurate, focused, and helpful answers.

This approach is especially effective for:

- Large knowledge bases with overlapping content
- Businesses with multiple locations
- Scenarios where branch-specific accuracy is critical

By combining good KB structure (with branch names) and refinement logic, you can make your AI agent feel smarter, more precise, and more human-like.


### 📌 Example 2: Managing Product Information with KB Search Refinement

Imagine you manage an e-commerce platform with thousands of products. Your knowledge base contains detailed product logs including specifications, pricing, inventory status, and customer feedback across multiple spreadsheets. When customers inquire about specific products, you want your AI agent to provide accurate, product-specific information.

**1. Include Product Names in Your Knowledge Base Entries**

For each cell in your spreadsheet, include the product name to clearly identify the information:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement-product" href="/images/seachat/en/agent-advanced-settings/kb-refinement-product.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-advanced-settings/kb-refinement-product.png" alt="An example spreadsheet containing product information">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Example Spreadsheet: Product Knowledge Base with Product-Specific Tags</p></p>
</div>

This structured spreadsheet ensures that when the AI agent processes the knowledge base, it can accurately associate information with specific products.

**2. Upload Spreadsheet**

Upload this spreadsheet to your knowledge base through the **Upload Spreadsheets** card.  And choose this option to upload each row in the table as an individual KB document.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a id="seachat-kb-refinement" href="/images/seachat/en/agent-advanced-settings/kb-refinement-upload2.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-advanced-settings/kb-refinement-upload2.png" alt="Upload each row as an individual kb article">
    </a>
</div>
</div>
<br/>


**3. Configure KB Search Refinement Instructions**

Enable Knowledge Base Search Refinement and add specific instructions:

```
Extract product names from the user's query.
Prioritize exact matches first, then consider product variants or related models. 
Exclude information about different products unless specifically comparing features.
```

With these instructions, your AI agent can:
- Identify the specific product being discussed
- Focus on relevant product details
- Include related product information only when appropriate
- Maintain context across multiple queries about the same product

This approach is particularly effective for:
- Large product catalogs with similar items
- Technical support scenarios requiring precise product information
- Product comparison and recommendation queries
- Handling customer inquiries about product specifications and availability

By implementing this structure, your AI agent can efficiently navigate through extensive product information and provide accurate, contextual responses to customer queries.

---


##### Long-Term Memory

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/long-term-memory.md -->

<!-- Weight: 106 -->

*Learn how to enable and configure Long-Term Memory in SeaChat for persistent user context and personalized conversations.*


## Overview

Long-Term Memory in SeaChat allows agents to retain persistent user context across conversations, enabling more human-like, personalized, and context-aware responses. This premium feature is essential for use cases like marketing, sales, and customer service, where remembering user preferences and past interactions is crucial.

For example, a user might ask, "What do you know about me?" With Long-Term Memory enabled, the AI agent can recall and respond with detailed information from previous conversations, like hobbies, preferences, or travel plans.

THe following guide explains how to enable and use Long-Term Memory in SeaChat for and example use case and management tips.

## Video Tutorial:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/JsSXUt009ZU?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## Getting Started

Here’s a guide to enabling and using Long-Term Memory in SeaChat:

### Long-Term Memory

<br/>

<center>
<a href="/images/seachat/en/user-memory/activate-user-memory.png">
<img height="100%" width="100%" src="/images/seachat/en/user-memory/activate-user-memory.png"  alt="Activate Long-Term Memory Feature">
</a>

</center>

<br/>

To enable Long-Term Memory:

- Navigate to **Agent Configuration** ➔ **Advanced Settings**.

- Enable the Long-Term Memory feature.

- Save your changes.

## How It Works

When Long-Term Memory is active, SeaChat will automatically save key facts about users during conversations, like their preferences, past questions, and relevant interests. 

When a user returns, even after a long time, SeaChat can recall this information, creating a more seamless and tailored interaction.

## Example Use Case

***Initial Conversation***

<br/>

<center>
<a href="/images/seachat/en/user-memory/conversation-1.png">
<img height="100%" width="80%" src="/images/seachat/en/user-memory/conversation-1.png"  alt="Long-Term Memory Example | Conversation 1">
</a>

</center>

<br/>

***Follow-Up Conversation***

<br/>

<center>
<a href="/images/seachat/en/user-memory/conversation-2.png">
<img height="100%" width="80%" src="/images/seachat/en/user-memory/conversation-2.png"  alt="Long-Term Memory Example | Conversation 2">
</a>

</center>

<br/>

***Updated Preferences***

<br/>

<center>
<a href="/images/seachat/en/user-memory/conversation-3.png">
<img height="100%" width="80%" src="/images/seachat/en/user-memory/conversation-3.png"  alt="Long-Term Memory Example | Conversation 3">
</a>

</center>

<br/>

With each interaction, the agent dynamically updates the user profile, retaining both past and new preferences.

## Managing Long-Term Memory

<br/>

<center>
<a href="/images/seachat/en/user-memory/option-btn.png">
<img height="100%" width="100%" src="/images/seachat/en/user-memory/option-btn.png"  alt="Long-Term Memory Option Button">
</a>

</center>

<br/>


Supervisors can manage Long-Term Memory in the Conversations section:

- Select the desired user conversation.

- Click the **Long-Term Memory** option (three dots).

- View, update, or erase the user’s memory.

> Tip: Use this feature to segment users, deliver targeted marketing messages, or provide tailored support.

### Resetting Memory

<br/>

<center>
<a href="/images/seachat/en/user-memory/delete-memory.png">
<img height="100%" width="100%" src="/images/seachat/en/user-memory/delete-memory.png"  alt="Delete Long-Term Memory Permanently">
</a>

</center>

<br/>

For testing or privacy purposes, you can reset Long-Term Memory:

- Select the desired user conversation.

- Click the **Long-Term Memory** option (three dots).

- Select **Erase All** for the user.

> Warning: Resetting memory is irreversible and will remove all stored context.


### Conversation History Turn

SeaChat retains up to 20 conversation turns by default. Long-Term Memory extends this limit indefinitely, allowing agents to remember user context over extended periods.

However, this means if the users wishes to disable the Long-Term Memory feature, it will only prevent the AI agent from remembering any user context. To completely remove the effect of context, users should also set the **Conversation History Turn Count** to 0 to prevent the AI agent from remembering any conversation history.

Here are the steps to modify the **Conversation History Turn Count**:

<br/>

<center>
<a href="/images/seachat/en/user-memory/conversation-turn.png">
<img height="100%" width="100%" src="/images/seachat/en/user-memory/conversation-turn.png"  alt="Context | Conversation History Turn Count">
</a>

</center>

<br/>

- Navigate to **Agent Configuration** ➔ **Advanced Settings**.

- Click on **Context**.

- Set the **Conversation History Turn Count** to 0.


## Additional Notes

- Default Context Limit: SeaChat retains up to 20 conversation history turns by default. Long-Term Memory extends this limit indefinitely.

- Privacy Compliance: Long-Term memory is securely stored and can be erased at any time to ensure data privacy compliance.

- Applications: Ideal for customer profiling, personalized marketing, and enhancing user experiences.


## Conclusion

Long-Term Memory transforms SeaChat into a smarter, more personalized AI assistant by retaining user context over extended periods. Whether for sales, customer support, or small talk, this feature ensures your AI agent remembers what matters most to your users.


---


##### Time Awareness and Context

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/04-time-awareness-context.md -->

<!-- Weight: 107 -->

*Learn how SeaChat AI's Time Awareness and Context features enhance agent control for time-sensitive responses.*


--- 

## Overview

In addition to the [Retrieval Augmented Generation (RAG)](https://wiki.seasalt.ai/en/seachat/manual/create-agent/advanced-settings/rag/) feature and [Context Extraction](https://wiki.seasalt.ai/en/seachat/manual/create-agent/advanced-settings/context-extraction/), SeaChat AI offers various options in advanced settings that allow users to further control their agent’s behavior.

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

---


##### Context Extraction

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/03-context-extraction.md -->

<!-- Weight: 108 -->

*SeaChat Context Extraction tracks customer profiles to ensure relevant conversations and assist in expected outcomes.*



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


  <iframe width="100%" height="400" src="https://www.youtube.com/embed/Msgg3U3lW4M?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


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
<a href="/images/seachat/en/context-extraction/general-setup.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/general-setup.png" alt="Navigate to Advanced Settings">
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

[//]: # (<a href="/images/seachat/en/context-extraction/add-and-remove.png" target="_blank">)

[//]: # (<img width="20%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/add-and-remove.png" alt="">)

[//]: # (</a>)

[//]: # ()
[//]: # (<br/>)

[//]: # ()
[//]: # (*Plus &#40;Add&#41; and Minus &#40;Remove&#41;*)

[//]: # (</center>)

4. Finally, save your extraction settings by clicking the save button at the bottom.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/7220ada1-b2e3-4353-9052-c49d45225bd8)

[//]: # (<center>)

[//]: # (<a href="/images/seachat/en/context-extraction/save-setting.png" target="_blank">)

[//]: # (<img width="40%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/save-setting.png" alt="">)

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
> DO NOT modify the **//QUESTIONS START** and **//QUESTIONS END** tokens. These are crucial to properly populate the extraction field for this use case

2. After setting up the description and question section, press the save button at the bottom.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/9b59ff3a-04aa-44c7-83a8-2cd02fe13f78)

<center>
<a href="/images/seachat/en/context-extraction/question-start.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/question-start.png" alt="Start Question Section">
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
<a href="/images/seachat/en/context-extraction/advanced-settings.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/advanced-settings.png" alt="Advanced Settings | Context Extraction">
</a>

<br/>

*Advanced Settings*
</center>

## Extraction in Conversations 

The extraction for each conversation will update in real time and we can check the values from the Conversation page

1. Head to the Conversations page from the left hand side

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/00c4d418-879d-49a5-9ffc-a49972668ed7)

<center>
<a href="/images/seachat/en/context-extraction/conversation-page.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/conversation-page.png" alt=""Conversaiton Page | Context Extraction>
</a>

<br/>

*Conversations*
</center>

2. Find the desired conversation from the list and press the triple dot icon in the bottom right corner for that conversation.

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/9be38868-cdbf-4223-a445-636695b8c922)

<center>
<a href="/images/seachat/en/context-extraction/extraction-btn.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/extraction-btn.png" alt="Extraction Button | Context Extraction">
</a>

<br/>

*Click on **Extraction***
</center>

3. Pressing **Extraction** will bring up the latest extracted values for that conversation

[comment]: ![image](https://github.com/seasalt-ai/ngChat/assets/72329316/5872958e-9b35-4ad7-93c2-50ac2a50f81f)

<center>
<a href="/images/seachat/en/context-extraction/extracted-value.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/extracted-value.png" alt="Extraction Value | Context Extraction">
</a>

<br/>

*Latest Extracted Values*
</center>

## 🤖 Example Use Case

Imagine we have an AI agent tailored to enhance customer experience management. The agent's effectiveness hinges on its ability to track user preferences accurately, necessitating the establishment of specific extraction fields for such data.

### Initial Setup

Before delving into extraction field configurations, it's crucial to have your AI agent operational. If you haven't set up your agent yet, please consult our [Create New Agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/) guide for detailed instructions.

### Define Extraction

Proceed by navigating to the **Advanced Settings** tab where you can define the extraction fields:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/context-extraction/example-advanced-setting.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/example-advanced-setting.png" alt="Extraction Definition | Context Extraction">
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
    <a href="/images/seachat/en/context-extraction/example-conversation.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/example-conversation.png" alt="Example Conversation | Context Extraction">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Monitor Conversation Extraction</p>
</div>

The extracted values from conversations are accessible within the system. Simply Move to the **Conversations** page, select the desired conversation, and click on the **Extraction** button to view the extracted values. Read again [here](#initial-setup) to learn to see your result like the image below.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/context-extraction/example-result.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/context-extraction/example-result.png" alt="Result Example | Context Extraction">
    </a>
</div>
 <p style="margin-top: 20px; font-size: 15px">Value Extracted</p>
</div>

# Retrieve Conversation Extraction

Each conversation's Extraction value can be retrieved via [the API](https://wiki.seasalt.ai/seasaltapi/seasalt-api/01-seachat-api-intro/) for further processing.



---


##### Enabling References in Chat

<!-- Source: seachat-manual/02-create-agent/03-advanced-settings/05-kb-references.md -->

<!-- Weight: 109 -->

*The Knowledge Base References feature in SeaChat by Seasalt.ai provides a convenient way to link back to documents used to generate chat responses. When enabled, each chat response will include a References section that lists the source documents, allowing users to see exactly what information contributed to the response.*


#### Overview

The Knowledge Base References feature in SeaChat by Seasalt.ai provides a convenient way to link back to documents used to generate chat responses. When enabled, each chat response will include a References section that lists the source documents, allowing users to see exactly what information contributed to the response.

#### How to Enable Knowledge Base References

To enable this feature, follow these steps:

1. **Go to the Agent Information \-\> Advanced Settings** tab
2. **Toggle Knowledge Base References**
   - Find the Knowledge Base References setting and switch it on to activate the feature.

<center>
<a href="/images/seachat/en/kb-references/image01.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image01.png"  alt="KB References Section in the Advanced Settings Page">
</a>
<br/>

</center>

Once enabled, the References section appears under the AI Agent’s responses, displaying the names of the Knowledge Base documents that SeaChat used to generate the answer. If the source is a clickable URL, it will be displayed as a link for easy access. This allows users to verify the sources and gain a better understanding of how responses are formed.

#### What Kind of Knowledge Base Entries Show as References?

The types of Knowledge Base entries that can appear as references include:

#### **1\. URL-Based Entries**

Web pages or publicly accessible articles added to the KB. When the chatbot retrieves information from a URL, the reference appears as a clickable link.

<center>
<a href="/images/seachat/en/kb-references/image02.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image02.png"  alt="AI agent response displays two clickable urls">
</a>
<br/>

_Example: AI agent response displays two clickable urls._

</center>

#### **2\. Manual Knowledge Base Entries**

Custom text-based knowledge entries manually added. These are typically short documents or FAQs written in SeaChat’s _Write a New KB Document_ page. The reference will display the title of the manual KB entry.

<center>
<a href="/images/seachat/en/kb-references/image03.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image03.png"  alt="A Manual KB entry">
</a>
<br/>
</center>
<br/>
<center>
<a href="/images/seachat/en/kb-references/image04.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image04.png"  alt="AI agent response displays a citation from the Manual KB entry">
</a>
<br/>

_Example: AI agent response displays a citation from the Manual KB entry: The Basics of Renewable Energy._

</center>

#### **3\. Uploaded Files**

Various document types that users upload to the Knowledge Base. When an uploaded document contributes to a response, the filename will appear in the References section. Supported file formats include:

- Excel Files (.csv, .xls, .xlsx, .xlsm, .xlsb, .odf, .ods and .odt)

- Documents (.doc, .docx, .eml, .epub, .gif, .jpg, .json, .html, .msg, .odt, .ogg, .pdf, .png, .pptx, .ps, .rtf, .tiff, .txt, .zip)

<center>
<a href="/images/seachat/en/kb-references/image05.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image05.png"  alt="A document">
</a>
<br/>
</center>
<br/>
<center>
<a href="/images/seachat/en/kb-references/image06.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image06.png"  alt="AI agent response displays a citation from the document">
</a>
<br/>

_Example: AI agent response displays a citation from the document: artificial_intelligence-docx._

</center>

<center>
<a href="/images/seachat/en/kb-references/image07.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image07.png"  alt="An Excel file">
</a>
<br/>
</center>
<br/>
<center>
<a href="/images/seachat/en/kb-references/image08.png">
<img height="100%" width="100%" src="/images/seachat/en/kb-references/image08.png"  alt="AI agent response displays a citation from a worksheet: renewable_energy-xlsx">
</a>
<br/>

_Example: AI agent response displays a citation from a worksheet: renewable_energy-xlsx._

</center>

#### Use Cases

Here are some scenarios where **Knowledge Base References** can be particularly valuable:

- **Customer Support & Helpdesk**
  - Human agents can quickly verify that chatbot responses align with official documentation.
  - Customers can see where information is sourced, ensuring transparency and trust.
- **Internal Knowledge Sharing**
  - Employees using SeaChat to find company policies or technical guidelines can check references for accuracy.
  - Training new team members becomes easier as they can trace back responses to internal knowledge base articles.
- **Education & Research**
  - Students and researchers can use SeaChat for academic inquiries while verifying the credibility of the sources used.
  - Teachers can guide students by pointing them to specific referenced materials.

By enabling Knowledge Base References, users gain better transparency, increased trust in AI responses, and more control over chatbot-generated content. 🚀


---


#### How to Add Knowledge

<!-- Source: seachat-manual/03-add-knowledge/01-add-knowledge-intro.md -->

<!-- Weight: 401 -->

*Learn to optimize your SeaChat agent's performance with advanced features by adding knowledge seamlessly.*

## Overview
This tutorial takes a deep dive into the different features to add information to your knowledge-based agent. We will guide you through every single step of the feature, and we will also highlight some key takeaways along the way.

## Prerequisites
By now, you should already have a SeaChat agent ready to receive new knowledge. If you have not created an agent, we kindly advise you to refer to our comprehensive tutorial on [how to create an agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/).

<br/>

<iframe width="100%" height="400" src="https://www.youtube.com/embed/5gKBId9hjC4?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>


---


#### Spreadsheet and Table

<!-- Source: seachat-manual/03-add-knowledge/02-spreadsheet-upload.md -->

<!-- Weight: 402 -->

*Integrate spreadsheets into SeaChat AI agent's knowledge base. Upload .csv or .xlsx files with ease*


> 🧭 **File Size Rule**
>
> Your file size limit for each uploaded document varies depending on your subscription plan. If you exceed the file upload limitation, you will receive an error message. Please reduce the size of your file before uploading again. Please refer to the [File Size Rule](https://wiki.seasalt.ai/en/seachat/file-size-rule/) for more information.

## Overview
SeaChat provides many methods to upload files to your agent. We will focus on the **Upload Spreadsheet** method in this tutorial and by the end of the tutorial your SeaChat agent will have a customized knowledge base at your service.


## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based AI agent in [Create an Agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/).


## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. By choosing **Upload Spreadsheet**, you can upload a .csv or .xlsx file to your agent.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step2.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step2.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a CSV or JSON file to an agent by selecting Upload from Template File.">
</a>

*Knowledge Base Dashboard*
</center>

## Upload File
By clicking on the upload button, you can submit to your agent choosing from various file formats[^1]. The file will be processed and the knowledge base will be updated accordingly once submitted.
[^1]: SeaChat supports .csv, .xls, .xlsx, .xlsm, .xlsb, .odf, .ods and .odt files.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step3.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step3.png" alt="Screenshot illustrating the navigation through the dashboard of knowledge base for SeaChat's AI agents. It illustrates the user interface">
</a>

*Click on Drag-and-Drop Zone to Upload*
</center>


> :rotating_light: **Note** :rotating_light:
> 
> Before uploading the file, check if the files meet the two following requirements:
> - Your spreadsheet table must use the first row as the header. If your header is the first column, please [transpose your table](https://support.microsoft.com/en-us/office/transpose-rotate-data-from-rows-to-columns-or-vice-versa-3419f2e3-beab-4318-aae5-d0f862209744) first.
> - The content in any row may not exceed 2000 tokens. If your row exceeds this limit, please contact us!
> 
> Check **Upload Guidelines** for more information.

## Choose Upload Mode

We now support two modes for uploading spreadsheets or tables to the knowledge base.

- **Upload each row in the table as a separate KB document**: This is especially helpful when you have a table where each row contains a self-contained piece of information. For instance, if each row is about a product, we recommend choosing this option to store each product description separately in the knowledge base.

- **Upload the table as a single KB document**: Use this option when the information in the entire table is interconnected. For example, if you have a table containing a full-day event schedule, we recommend uploading the entire table as a single KB document to ensure the AI agent learns about the entire schedule together during retrieval.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240507-spreadsheet-kb-mode.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240507-spreadsheet-kb-mode.png" alt="Screenshot illustrating the mode options for spreadsheet uploads">
</a>

*Choose the suitable upload mode for your spreadsheets*
</center>



## Before Submission
SeaChat allows users to upload in bulk. You can see the status of each uploading file in the section below the drag-and-drop zone.
You can upload as many spreadsheet files as you wish and each file can have more than just one worksheet.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step4.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step4.png" alt="Interface of SeaChat showing the bulk upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded and a preview section for the spreadsheet data, reminding users to verify file format and content before submission.">
</a>

*Uploading status*
</center>


Scroll further down for the dedicated preview window that will list the first 10 rows of your spreadsheet. Once you have included all the files to be uploaded, you can upload them by clicking on the **Next** button.

> :construction: **Embedded Image in Excel**
> 
> Currently, SeaChat does not support uploading images embedded in Excel files. If you wish to include image data, please upload the images separately to the specific knowledge that requires them.
> 
> For example, if you want to include an image to a card to a certain knowledge, you can still upload the Excel file first and then upload the image separately to the card knowledge.

###### Preview Example:
<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step4-table-example.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step4-table-example.png" alt="An example of table preview">
</a>

</center>

## Submit to Existing Knowledge Base
Voilà! You have successfully customized your SeaChat agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the **Files** section.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step5.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step5.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Next' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Look for Files in **Existing***
</center>

## Review your Knowledge Base
Click on the file you just uploaded to review the content. That's it! You have successfully uploaded a spreadsheet to your SeaChat agent. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the **Advance** section of the tutorial.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step6.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/spreadsheet/20240306-spreadsheet-tutorial-step6.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Next' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Review Uploaded File*
</center>

## :brain: Under the Hood

Why does SeaChat single out spreadsheet/table uploads? Because we believe spreadsheet/table are the most common way that any users organize their knowledge base. Yet special attention needs to be paid to optimize a Large Language Model's (e.g. ChatGPT) ability to understand tables:

1. We sacrifice space in exchange for understanding accuracy. In each data row, the actual values are prefixed with their header fields. So when a table becomes too big, the LLM/ChatGPT does not lose context.
2. Because of the limited context length of LLMs, we limit each row to be more than 2,000 tokens.



## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 

---


#### Audio/Video File

<!-- Source: seachat-manual/03-add-knowledge/03-multimedia-upload.md -->

<!-- Weight: 403 -->

*Enhance your AI agent’s knowledge base by uploading audio/video files in English or Traditional Chinese.*

> 🧭 **File Size Rule**
>
> Your file size limit for each uploaded document varies depending on your subscription plan. If you exceed the file upload limitation, you will receive an error message. Please reduce the size of your file before uploading again. Please refer to the [File Size Rule](https://wiki.seasalt.ai/en/seachat/file-size-rule/) for more information.

## Overview
Audio and video files can be used as knowledge base for your SeaChat agent too! Usually one would first transcribe these files to text, then upload the text documents to AI agent's knowledge base. SeaChat takes care of the transcription step for you by directly accepting audio/video files!

SeaChat provides many methods to upload files to your agent. We will focus on the **Transcribe Audio/Video** method in this tutorial.


## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based agent in [Create an Agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/).


## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. By choosing **Transcribe Audio/Video**, you can upload a video or audio file to your agent.

<br/>
<center>
<a href="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step2.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step2.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a video or audio file to an agent by selecting Transcribe Audio/Video.">
</a>

*Knowledge Base Dashboard*
</center>

## Upload File
By clicking on the upload button, you can submit to your agent choosing from various file formats[^1]. The file will be processed, transcribed into text format, and fed into knowledge base once submitted.
[^1]: SeaChat supports .wav, .flac, .aac, .opus, .mp3, .mp4, .ogg, .m4a files.

<br/>
<center>
<a href="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step3.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step3.png" alt="Screenshot illustrating the variety of file types that SeaChat accepts">
</a>

*Choose the Language of the Uploading File*
</center>

> :rotating_light: **Note** :rotating_light:
>
> Before uploading the file, check if the files meet the following requirements:
> - The media content must be in English or Chinese.
> - The file's duration should not exceed 15 minutes.
> - (Optional) After the audio/video files are uploaded, SeaChat will turn them into transcriptions in text format. Currently, SeaChat does not have speaker identification for video/audio transcription. If you need speaker identification in your transcription, please transcribe the file else where and upload the transcription to knowledge base as text document.

## Check the language
Make sure to choose the correct media language for the audio or video file. For now SeaChat supports English and Traditional Chinese. Once you have included all the files to be uploaded, you can upload them by clicking on the **Submit** button.

Note that the English/Chinese support only means that your uploaded audio/video files are transcribed into
corresponding language. 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step4.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step4.png" alt="Interface of SeaChat showing the bulk upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded and a preview section for the spreadsheet data, reminding users to verify file format and content before submission.">
</a>

*Uploading Status*
</center>


## Submit to Existing Knowledge Base
Voilà! You have successfully customized your AI agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the **Files** section.

<br/>
<center>
<a href="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step5.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step5.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Look for Files in **Existing***
</center>

## Review your Knowledge Base
Click on the file you just uploaded to review the content. That's it! Your SeaChat agent now has transcribed the content of the uploaded media into text. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the **Advance** section of the tutorial.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step6.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step6.png" alt="Review the uploaded information in a dropdown view">
</a>

*Review Uploaded File*
</center>

## :brain: Under the Hood

There are a few things to note to use this function properly:

1. For video files, SeaChat does not do anything with the video content. All it does is to extract the audio tracks from the video, and transcribe the audio to text, which can be used in the KB.
2. For each transcribed audio and video, you can check the transcription quality in Existing Knowledge Base.
3. If you have multimedia files in another language, feel free to transcribe them to text, and then upload to Seachat as text documents -- it achieves the same goal. 
4. For the audio/video file, SeaChat assumes there's only one speaker in the file. That is, SeaChat does not perform diarization or speaker identification. If you have an audio file that contains a conversation (such as a two-person podcast), you can first transcribe it and start each line with the speaker name if applicable. Then, you can upload the transcript as a text document on knowledge base.

 ## Why Do You Need Audio/Video Upload?

Many of our customers build up their knowledge base with past customer service conversations. Many of them use audio files from WhatsApp and Facebook Messenger conversations, which are often audio message containing one speaker and is less than 1 minute. The multimedia upload feature is a natural extension of this. 

If you do have past customer conversations in audio or video file formats, give it a try and upload to knowledge base. Your AI agent can definitely learn from past customer service coversations to generate quality responses.


## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).




---


#### Template Upload

<!-- Source: seachat-manual/03-add-knowledge/04-template-file-upload.md -->

<!-- Weight: 404 -->

*Easily upload and manage your SeaChat agent's knowledge base with our predefined spreadsheet templates.*

> 🧭 **File Size Rule**
>
> Your file size limit for each uploaded document varies depending on your subscription plan. If you exceed the file upload limitation, you will receive an error message. Please reduce the size of your file before uploading again. Please refer to the [File Size Rule](https://wiki.seasalt.ai/en/seachat/file-size-rule/) for more information.


## Overview
SeaChat provides several methods to upload files to your agent. We will focus on the **Upload Spreadsheet** method in this tutorial and by the end of the tutorial your SeaChat agent will have a customized knowledge base at your service.


## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based AI in [Create an Agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/).


## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. Click on **Upload from Template File**. SeaChat provides template files that can you can directly input.

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/knowledge-base.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a CSV or JSON file to an agent by selecting Upload from Template File.">

*Knowledge Base Dashboard*
</center>

## Template Files
SeaChat offers CSV and JSON template files that you can download and fill in with your data. Once you have filled in the template files, you can upload it to your agent by clicking on the drag-and-drop section.

###### Preview Example:
```CSV```

<div style="overflow-x: auto;">
<table>
<tr>
  <th>id</th>
  <th>title</th>
  <th>text</th>
  <th>references</th>
  <th>reminder</th>
  <th>capture</th>
  <th>live_agent_transfer</th>
  <th>sample_key</th>
</tr>
<tr>
  <td>kb-1</td>
  <td>Sample KB Doc</td>
  <td>This is an example of a KB document.</td>
  <td>[{"title":"Seasalt.ai","url":"https://seasalt.ai"}]</td>
  <td>This is some reminder text!</td>
  <td>Email,Phone Number</td>
  <td>False</td>
  <td>sample value</td>
</tr>
</table>
</div>


```JSON```
```json
[{
  "id": "kb-1",
  "title": "Sample KB Doc",
  "text": "This is an example of a KB document.",
  "custom": {"sample_key": "sample value"},
  "actions": {
    "references": [
      {"title": "Seasalt.ai", "url": "https://seasalt.ai"},
      {"title": "SeaChat", "url": "https://chat.seasalt.ai/"}
    ],
    "reminder": "This is some reminder text!",
    "capture": ["Email", "Phone Number"],
    "live_agent_transfer": false
  }
}]
```

1. **id**: Unique identifier for the document.
2. **title**: Title of the document.
3. **text**: Content of the document that the AI agent will interpret.
4. **custom**: Additional information that the AI agent can refer to. For example, when you need to refine a knowledge base response, you can add a custom key-value pair to the document for the AI agent to refer to.
4. **references**: Additional information or links that the AI agent can provide. Where **title** is the name of the reference that will render in the UI and **url** is the link.
5. **reminder**: Additional information that the AI agent will provide in the formatted reminder banner.
6. **capture**: Information that the AI agent will capture from the user. For example, when this specific knowledge is used. Agent will ask users for the inputs in capture field.
7. **live_agent_transfer**: Boolean value to enable or disable live agent transfer.

## Before Submission
You will see the status of each uploading file in the section below the drag-and-drop zone. Once you are sure with the uploaded files, you can upload them by clicking on the **Submit** button.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/template-upload/before-submission.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/before-submission.png" alt="Interface of SeaChat showing the upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded, reminding users to verify file format and content before submission.">
</a>

*Check the Uploaded Files*
</center>


## Submit to Existing Knowledge Base
Submit it and it's done. You have successfully customized your AI agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the "Files" section.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/template-upload/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/existing-files.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Look for Files in **Existing***
</center>

## Review your Knowledge Base
Click on the file you just uploaded to review the content. That's it! You have successfully uploaded a spreadsheet to your SeaChat agent. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the next part of the tutorial.

<div style="display: flex; justify-content: space-between; align-items: center;">
  <div style="display: flex; flex-direction: column; text-align: center;">
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/template-upload/csv-uploaded.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/csv-uploaded.png" alt="Example of a successfully uploaded csv.">
</a>
    <em>CSV File</em>
  </div>

  <div style="display: flex; flex-direction: column; text-align: center;">
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/template-upload/json-uploaded.png" target="_blank">
    <img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/template-upload/json-uploaded.png" alt="Example of a successfully uploaded json.">
</a>
    <em>JSON File</em>
  </div>
</div>



## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 

---


#### Upload Documents

<!-- Source: seachat-manual/03-add-knowledge/05-document-upload.md -->

<!-- Weight: 406 -->

*Build your SeaChat agent's knowledge base by uploading diverse document types for better service.*

> 🧭 **File Size Rule**
>
> Your file size limit for each uploaded document varies depending on your subscription plan. If you exceed the file upload limitation, you will receive an error message. Please reduce the size of your file before uploading again. Please refer to the [File Size Rule](https://wiki.seasalt.ai/en/seachat/file-size-rule/) for more information.


## Overview
SeaChat provides several methods to upload files to your agent. We will focus on the **Upload Documents** method in this tutorial and by the end of the tutorial your SeaChat agent will have a customized knowledge base at your service.


## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based AI agent in [Create an Agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/).


## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. Choose **Upload Documents** and have the more than 20 types of documents ready to be uploaded to your agent.

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/document-upload/choose-document-upload.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a CSV or JSON file to an agent by selecting Upload from Template File.">

*Knowledge Base Dashboard*
</center>

## Types of Documents
SeaChat supports more than 20 types[^1] of documents that you can upload to your agent. In this Tutorial, we will show you how to upload a DOCX file to your agent. 


> :rotating_light: **Note** :rotating_light:
>
> For picture files e.g. png, we only support English documents. For best result on audio files, we suggest you use [audio/video upload](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/multimedia-upload/) instead.


[^1]: SeaChat supports .doc, .docx, .eml, .epub, .gif, .jpg, .json, .html, .mp3, .msg, .odt, .ogg, .pdf, .png, .pptx, .ps, .rtf, .tiff, .txt, .wav, .zip files.

## Before Submission
You will see the status of each uploading file in the section below the drag-and-drop zone. Once you are sure with the uploaded files, you can upload them by clicking on the **Submit** button. 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/document-upload/file-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/document-upload/file-upload.png" alt="Interface of SeaChat showing the upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded, reminding users to verify file format and content before submission. A success message indicates the uploaded has been successful">
</a>

*File Uploaded Successfully*
</center>


## Submit to Existing Knowledge Base
You will see a success message once the files are uploaded successfully. You have customized your AI agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the "Files" section.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/document-upload/existing-files.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/document-upload/existing-files.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Look for Files in  **Existing***
</center>

## Review your Knowledge Base
Click on the file you just uploaded to review the content. That's all. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the next part of the tutorial.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/document-upload/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/document-upload/review-upload.png" alt="Review the uploaded information in a dropdown view">
</a>

*Review Uploaded DOCX File*
</center>


## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 

---


#### Import URLs

<!-- Source: seachat-manual/03-add-knowledge/06-import-urls.md -->

<!-- Weight: 407 -->

*Easily expand your SeaChat agent's knowledge base by importing URLs. Follow our step-by-step guide to integrate web content into your AI agent for enhanced performance.*

> 🧭 **File Size Rule**
>
> Your file size limit for each uploaded document varies depending on your subscription plan. If you exceed the file upload limitation, you will receive an error message. Please reduce the size of your file before uploading again. Please refer to the [File Size Rule](https://wiki.seasalt.ai/en/seachat/file-size-rule/) for more information.


## Overview
SeaChat provides several methods to upload files to your agent. We will focus on the **Import URLs** method in this tutorial. Let's use a blog post as an example to show you how to import URLs to your agent.

## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based AI agent in [Create an Agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/). 

## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. Choose **Import URLs** and have the URLs ready to be uploaded to your agent.

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/import-urls/choose-import-urls.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload by importing urls.">

*Knowledge Base Dashboard*
</center>

## Enter the URLs
SeaChat supports importing URLs to your agent. Copy and paste the URLs into the corresponding inputs. Once you are certain with the urls included, Click **Add** to confirm.

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/import-urls/enter-urls.png" alt="Image of the Knowledge Base interface where we lead the user to insert the url of the webpage that they wish to import">

*Insert the URL of the page to import text from the page*
</center>

By now, you should notice the additional option on the right-hand of the user interface that allows you to import text from **pages linked on this page**. Provide the links on the page to import the text from the linked pages. 

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/import-urls/enter-urls-2.png" alt="Image of the Knowledge Base interface where we lead the user to insert the url of the webpage that they wish to import">

*Insert the URL of the page to import text from the pages linked on this page*
</center>


Once you have added the URLs, you can click on the **Submit** button to upload the content to your agent's knowledge base. SeaChat will start importing the text from the URLs you provided. 


## Submit to Existing Knowledge Base
You will see a success message once the files are uploaded successfully. You have customized your AI agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the **URLs** section.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/import-urls/urls-in-existing.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/import-urls/urls-in-existing.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Look for **URLs** in **Existing***
</center>

## Review your Knowledge Base
Click on the file you just uploaded to review the content. The texts on your URLs are now in your knowledge base. That's all. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the next part of the tutorial.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/import-urls/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/import-urls/review-upload.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Review the uploaded content*
</center>




## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).


---


#### Import Sitemaps

<!-- Source: seachat-manual/03-add-knowledge/07-import-sitemap.md -->

<!-- Weight: 408 -->

*Enhance your AI agent’s knowledge base by importing sitemaps. Integrate website URLs into your AI agent.*

> 🧭 **File Size Rule**
>
> Your file size limit for each uploaded document varies depending on your subscription plan. If you exceed the file upload limitation, you will receive an error message. Please reduce the size of your file before uploading again. Please refer to the [File Size Rule](https://wiki.seasalt.ai/en/seachat/file-size-rule/) for more information.


## Overview
SeaChat provides several methods to upload files to your agent. We will focus on the **Import Sitemaps** method in this tutorial. Let's use a sitemap example to show you how to import URLs to your agent.

## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based AI agent in [Create an Agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/).

## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. Choose **Import Sitemaps** and have the XML files ready to be uploaded to your agent.

<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge//import-sitemaps/choose-/import-sitemaps.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload by importing urls.">

*Knowledge Base Dashboard*
</center>

## Enter the Sitemaps
By importing sitemaps, you can skip the process of adding URLs one by one. Your sitemap, usually XML files, will contain all the links in the website you wish to import. In the examples below, I simply put the keyword, **sitemap**, next to my page's url. As you can see, now we have the link to the sitemap of the page.

Copy and paste the URLs into the corresponding inputs. Once you are certain with the urls included, Click **Add** to confirm.

> :rotating_light: **Note** :rotating_light:
>
> Note that not all websites have sitemaps. One of the most common (and simple) ways to locate the XML sitemap of a website is to
manually check. you need to do is enter your website URL in the browser and then add `sitemap.xml` at the end of the URL, e.g. www.YourWebsiteUrl.com/sitemap.xml. If a sitemap (looks a like a XML file) shows up, then the website has a sitemap. There are more methods to locate your sitemap, please refer to [this article](https://seocrawl.com/en/how-to-find-a-sitemap/) to learn more.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/import-sitemaps/enter-url.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge//import-sitemaps/enter-url.png" alt="Insert Sitemap URL ">
</a>

*Insert the URL of the sitemap*
</center>

## Before Submission
Once you have added the sitemap, SeaChat will automatically parse the XML file and extract the URLs. You can review the URLs before submitting them to your agent's knowledge base.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge//import-sitemaps/before-submission.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge//import-sitemaps/before-submission.png" alt="Interface of SeaChat showing the upload section below for monitoring the status of each file being uploaded, reminding users to verify file format and content before submission.">
</a>

*Check the Uploaded Files*
</center>

## Submit to Existing Knowledge Base
You will see a success message once the files are uploaded successfully. You have customized your AI agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the **Sitemaps** section.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge//import-sitemaps/sitemap-in-existing.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge//import-sitemaps/sitemap-in-existing.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Look for **Sitemaps** in  **Existing***
</center>

## Review your Knowledge Base
Click on the file you just uploaded to review the content. The texts on your websites are now in your knowledge base. That's all. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the next part of the tutorial.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/import-urls/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/import-urls/review-upload.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Review the uploaded content*
</center>




## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).


---


#### Manual Entry

<!-- Source: seachat-manual/03-add-knowledge/08-manual-upload.md -->

<!-- Weight: 409 -->

*Manually input data into your SeaChat AI agent's knowledge base using our comprehensive tutorial.*

> 🧭 **File Size Rule**
>
> Your file size limit for each uploaded document varies depending on your subscription plan. If you exceed the file upload limitation, you will receive an error message. Please reduce the size of your file before uploading again. Please refer to the [File Size Rule](https://wiki.seasalt.ai/en/seachat/file-size-rule/) for more information.


## Overview
SeaChat provides several methods to upload files to your agent. We will focus on the **Manual Entry** method in this tutorial. Let's use a blog post as an example to show you how to manually enter data to your agent.

## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based AI agent in [Create an Agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/).

## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. Choose **Write a new KB Document** under **Manual Entry** and start entering data to be uploaded to your agent.


<br/>
<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/manual-entry/choose-manual-entry.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload by importing urls.">

*Knowledge Base Dashboard*
</center>

## When should I use Manual Entry?
You should choose Manual Entry when you have a piece of important information that you'd like to include in knowledge base. This can be a short product description, or a frequently asked questions. Manual Entries are also a great way to quickly troubleshoot and teach your AI agent some quick gotchas. 

## Enter the Data
There are a lot of fields to fill in. We will not go through all of them in detail, but if you are interested in learning more about them, you can check out our Advanced Section of the manual. For now, let's try to fill in the fields one by one, and add the data to our agent.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/manual-entry/empty-manual-entry.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/manual-entry/empty-manual-entry.png" alt="Visual guide highlighting the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">
</a>

*Fill in the empty fields in **Manual Entry**
</center>

### Document Title and Document Text
Choose a title for your document and write the texts of the document in the text area. Be descriptive on the text description, as it will show up on your knowledge library as the title of the knowledge entry. You can enter the detailed contents in the Document Text field. Both document title and texts will be available for AI agent during knowledge extraction.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/manual-entry/title-text.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/manual-entry/title-text.png" alt="Example of the Document Text and Document Title">
</a>

*Document title and text*
</center>

### Additional Attribute Value Pairs
If you have anything that is in the form of key-value pairs, you can add them here. For example, if you have a document that is related to a specific product and its price, you can add the product name(key) and the price(value) as key-value pairs. 


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/manual-entry/atr-value-pair.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/manual-entry/atr-value-pair.png" alt="Example of the Name and Value fields">
</a>

*Enter **Name**(Attribute) and **Value***
</center>

### (Optional) Additional Settings
You can also set the document to be a reminder, and provide users with urls.

- **URL Buttons**: You can add buttons that will redirect the user to a specific URL. Input the reference title and the URL in the respective fields.
- **Additional Message after Agent Response**: In **Reminder**, input additional information that you want to show to the end user whenever the agent uses this document to respond.
- **Document Weight**: Use Document Weight to control how important the document is. The higher the weight, the more important the document is, and therefore, the more likely the agent will use this document to respond to the user.

Once you are done, click on the **Submit** button to upload the content to your agent's knowledge base. SeaChat will start importing the information you provided.


## Submit to Existing Knowledge Base
You will see a success message once the files are uploaded successfully. You have customized your AI agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the **Manual KB** section.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/manual-entry/manual-kb-in-existing.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/manual-entry/manual-kb-in-existing.png" alt="Manual KB UI">
</a>

*Look for **Manual KB** in **Existing***
</center>

## Review your Knowledge Base
Click on the file you just uploaded to review the content. That's all. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the next part of the tutorial.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-add-knowledge/manual-entry/review-upload.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-add-knowledge/manual-entry/review-upload.png" alt="Review uploaded data">
</a>

*Review the uploaded content*
</center>




## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).




---


#### Adding URL buttons to KB responses

<!-- Source: seachat-manual/03-add-knowledge/09-add-webpage-link-in-answers.md -->

<!-- Weight: 410 -->

*Enhance your SeaChat AI agent's responses by adding URL buttons for more information in responses.*


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
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/choose-knowledge.png" alt="Navigate to Knowledge Base">
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
    <img width="70%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/choose-button.png" alt="Explaining the button feature">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Choose <strong>Button</strong></p>
</div>

The URL you provide here will be displayed as a button in the chat window. When the user clicks on the button, they will be redirected to the URL you have provided. Put the label that you wish to show your user in the **Title** and provide the URL in the **Content** field. You can add as many buttons as you want to the answer by simply clicking on the Plus(Add) sign.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/add-more-url.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/add-more-url.png" alt="Add URL button UI explanation">
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
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/url-to-answer.png" alt="Showcase of the inputted url in agent answer">
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
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/kb-id-problem.png" alt="Message Cutoff Explanation">
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
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/kb-id.png" alt="KB_ID feature">
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
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/spreadsheet-example.png" alt="Url Button for spreadsheets">
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
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/non-url-buttons.png" alt="Button in agent response">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Buttons in Agent Response</p>
</div>


<br/>

That's it. Now you no longer have to worry about manually adding URL buttons to your agent's responses when you are uploading a spreadsheet with a large amount of information.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/knowledge-advanced-features/url-button/spreadsheet-url-buttons.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/knowledge-advanced-features/url-button/spreadsheet-url-buttons.png" alt="Multiple Buttons in agent response">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Multiple URL Buttons in Agent Response</p>
</div>


<br/>

There are more advanced features in SeaChat agents' knowledge base that you can leverage to optimize your agent's responses. Check out our tutorials on [Advanced Features](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/additional-features-in-kb/) to learn more about these functionalities.

---


#### File Size Rule

<!-- Source: seachat-manual/03-add-knowledge/file-size-rule.md -->

<!-- Weight: 411 -->

*Learn SeaChat's file size limits like document size rules and checking token usage, based on your plan.*


According to your subscription plan, you can upload files up to a certain size. If you exceed the file size limit, you will receive an error message.

To understand the specific features in different plans, please refer to the [Pricing and Plans](https://wiki.seasalt.ai/seachat/seachat-payments/pricing-plans/).

The file size rule for each plan are as follows:

- **Free** - Knowledge base includes up to 10 documents (200KB max) and 200k tokens
- **Standard** - Knowledge base includes up to 100 documents (1 MB max) and 1 million tokens
- **Premium** - Knowledge base includes up to 500 documents (10 MB max) and 5 million tokens

### How to check your tokens

Once a document is uploaded to the knowledge base, the document is tokenized and the tokens are deducted from your account. You can check the number of tokens used by navigating to the **Knowledge Base** dashboard in the sidebar menu. Each document uploaded to the knowledge base will show the number of tokens used.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/pricing-plans/check-tokens.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/pricing-plans/check-tokens.png" alt="Check Tokens | SeaChat File Size Rule">
</a>

**How to Check Tokens**
</center>

> Here is a general rule of thumb to estimate the number of tokens of spreadsheets:
> 
> For 4o models, each spreadsheet row is 8K tokens, and each row is 2K tokens for 3.5 models.



---


##### Additional Features in Knowledge

<!-- Source: seachat-manual/03-add-knowledge/10-addtional-feature/01-additional-features-in-kb.md -->

<!-- Weight: 413 -->

*Enhance AI responses with buttons and images. Learn to edit entries, prioritize info, and sync content.*


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


---


#### WhatsApp

<!-- Source: seachat-manual/04-channels/04-seachat-whatsapp-integration.md -->

<!-- Weight: 500 -->

*Automate WhatsApp with SeaChat. Enhance customer support with AI agents for seamless communication.*


## 🎥 Video Tutorial
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/qpNlWtGP9jw?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

## Overview
In this section, we will dive deeper into the process of setting up a ChatGPT-powered chatbot or chat agent on WhatsApp. By the end of this section, you will have a clear understanding of how to:
1. **Automate responses to user messages**: 
  - Connect your WhatsApp business account to the SeaChat agent platform.
  - Train the AI Agent using ChatGPT's advanced language model to generate natural language responses to a wide range of user queries.
  - Configure the chat agent to automatically respond to incoming messages based on your knowledge base.
2. **Access all conversations with users through SeaChat**:
  - Use SeaChat, a user-friendly interface, to access and monitor all conversations between users and your AI agent.
  - Review chat transcripts, analyze user behavior, and identify areas for improvement in the chat agent's responses.
  - Manage and organize conversations efficiently to ensure seamless communication with users.
3. **Enable users to request live agent assistance**:
  - Implement a special command that allows users to request assistance from a real human agent if they have complex queries or require personalized support.
  - Seamlessly transfer conversations from the AI chat agent to live human agents, ensuring a smooth and efficient transition.
  - Empower users to choose the level of support they need, enhancing the overall customer experience.

Before embarking on the setup process, it's essential to keep in mind a few key points:

**WhatsApp Business App limitations**:
  - Once you integrate SeaChat with WhatsApp, you will no longer be able to use the regular WhatsApp Business App.
  - The SeaChat AI agent is designed to respond to incoming messages only and cannot initiate conversations on its own.
  - However, you as the agent creator will still be able to talk with the users once a live human agent is requested.

**Who benefits from this integration**:
  - Businesses and organizations with a high volume of incoming WhatsApp messages that require automation.
  - Companies looking to provide personalized and engaging customer support experiences.
  - Customer service departments seeking to reduce the burden on human agents by automating routine inquiries.
---

## WhatsApp Setup
Setting up WhatsApp can be a straightforward process with the right guidance. Here's a short version of the steps involved. You can also click on the titles to see a more detailed explanation of each step:

1. **[Create a WhatsApp App](#create-a-whatsapp-app)**:
- Go to the Meta Developer Site.
- Click on **My Apps** in the top-right corner.
- Select **Create App** from the dropdown menu.

2. **[Choose App Type](#choose-app-type)**:
- Choose **Other** under **App Type**.
- Enter a unique app name, avoiding the use of **WhatsApp** in the name.

3. **[Add WhatsApp Product](#add-whatsapp-product)**:
- Scroll down to the bottom of the app list.
- Find **WhatsApp** and select it to add the product to your app.

4. **[Connect to Business](#connect-to-business)**:
- Associate the WhatsApp app with your business.
- This step is necessary to utilize the **WhatsApp Business Platform API**.

5. **[Configure WhatsApp Application](#configure-whatsapp-application)**:
- Carefully review the information on the configuration page.
- Follow the instructions to provide necessary details, such as business name, address, and contact information.
- Ensure that all required fields are filled out correctly.

6. **[Generate Access Token](#lets-set-up-a-permanent-token)**:
- Once the configuration is complete, generate a permanent access token.
- This token is essential for using the WhatsApp Business API.

7. **[Test and Launch](#test-your-seachat-agent-via-whatsapp)**:
- Test your WhatsApp app to ensure it works as intended.
- Make any necessary adjustments based on the test results.
- Once satisfied with the performance, launch your app for public use.

8. **[Remove Your Messenger Integration](#remove-your-whatsapp-integration)**:
- Properly remove the page access from your Meta app
- Click the Remove button inside SeaChat

> :books: **Recommended Reading**:
> 
> Remember to adhere to the [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp/) policies and guidelines to maintain compliance and avoid any potential issues.


The following is an elaborated explanation that walks you through the process step-by-step:

### Create a WhatsApp app

You’ll first need to go to [Meta Developer Site](https://developers.facebook.com/) and create a new WhatsApp app by clicking **My Apps** in the top right corner, and then selecting **Create App** from the dropdown menu.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/whatsapp/create-new-whatsapp-app.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/create-new-whatsapp-app.png" alt="Create New WhatsApp Integration">
    </a>
    <p style="margin-top: 20px; font-size: 15px">Create a New WhatsApp</p>
</div>
</div>

### Choose App Type
Create an **Other** app because we’ll just use this App for accessing your WhatsApp account. On the **Select app type page**, select **Business** for the type, then click **Next**.

<br/>
<div style="display: flex; flex-direction: column; align-items: center;">
    <div style="width: 100%; height:100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/choose-app-type-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/choose-app-type-1.png" alt="Create Other App">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Create an <strong>Other</strong> app</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/choose-app-type-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/choose-app-type-2.png" alt="Fill up App Details">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Fill Up App Details</p>
    </div>
</div>

<br/>

Here we created an app called **Seasalt.ai WA**, note that Meta doesn’t allow the app to have **WhatsApp** in the name.


### Add WhatsApp Product

After creating the App, let’s add the WhatsApp product. Find the WhatsApp box under the **Add products to your app** section, and click **Set up** to create your app.

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/whatsapp/whatsApp-integration.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/whatsApp-integration.svg" alt="WhatsApp Integration">
    </a>
    <p style=" font-size: 15px">Add WhatsApp to Your App</p>
</div>
</div>


### Connect to Business
The WhatsApp app needs to be associated with your own business as it needs to utilize the [WhatsApp Business Platform API](https://developers.facebook.com/docs/whatsapp/). Select a business portfolio and click continue. Now back to your app dashboard, you should see the WhatsApp product added to your app. Click on **Start using the API** to start configuring.

<br/>
<div style="display: flex; flex-direction: column; align-items: flex-start;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/connect-to-business-1.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/connect-to-business-1.png" alt="Select Business Portfolio">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Select a Business Portfolio</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/connect-to-business-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/connect-to-business-2.png" alt="Start using API">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Click <strong>Start Using the API</strong></p>
    </div>
</div>

## How to Configure WhatsApp Application
> :rotating_light: **Warning** :rotating_light:
>
> Here is where things get a bit more complicated.  If you are not careful enough and miss a step, you might not be able to successfully configure your WhatsApp application. So, let's carefully go through the following instruction together.

If you click on **Start using the API** from above, it’ll bring you to **API Setup** like below. However, we do not need to pay too much attention to the information here. What really matters here is **Step 3: Configure webhooks**.

<br/>
<div style="display: flex; flex-direction: column; align-items: center; justify-content: space-between">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/configure-whatsApp-application-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/configure-whatsApp-application-1.png" alt="API Setup">
        </a>
        <p style="margin-top: 20px; font-size: 15px">API Setup</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/configure-whatsApp-application-2.svg" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/configure-whatsApp-application-2.svg" alt="Webhook Configuration">
        </a>
        <p style="font-size: 15px"><strong>Configure Webhooks</strong></p>
    </div>
</div>

It will bring you to **Configuration** under **WhatsApp** on the left. From here we’ll first need to configure the Webhook and tokens provided by SeaChat.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/en/channels/whatsapp/configure-whatsApp-application-3.svg" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/configure-whatsApp-application-3.svg" alt="Configuration Dashboard">
    </a>
    <p style=" font-size: 15px">Configuration Dashboard</p>
</div>
</div>

<br/>

For the configuration of the webhook, we will look at **Step 1** in the picture above. Here is all you have to do. Go to SeaChat, navigate to **Agent Configuration → Channels → WhatsApp** to get the **Callback URL** and **Verify token**. 

Copy SeaChat’s Step 1 and paste it to corresponding parts on WhatsApp dashboard like the picture below 


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/whatsapp/configure-whatsApp-application-4.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/configure-whatsApp-application-4.svg" alt=" Copy Seachat Data to Configuration">
</a>
    <p style="margin-top: 20px; font-size: 15px">Copy SeaChat info to configure</p>
</div>
</div>

<br/>

> :point_down: **Don’t forget to use set Webhook fields!** :point_down:
>
> We’ll need to give messages permission to the API, so that the SeaChat agent will be able to receive any incoming messages from WhatsApp.
>
> 
> <div style="display: flex; flex-direction: column; align-items: center;">
> <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
>   <a href="/images/seachat/en/channels/whatsapp/dont-forget-to-use-set-Webhook-fields.svg" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank"><img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/dont-forget-to-use-set-Webhook-fields.svg" alt="Webhook fields"></a>
>     <p style="margin-top: 10px; font-size: 15px">Webhook Fields</p>
> </div>
> </div>
> 


### Let’s set up a permanent token

[Step 2](#perma-token-webhook) is to obtain a **WhatsApp Access Token** to pass it back to SeaChat.

You might have seen the temporary access token before from API Setup:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
 <a href="/images/seachat/en/channels/whatsapp/permanent-token-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/permanent-token-1.png" alt="Temporary Access token">
</a>
    <p style="margin-top: 20px; font-size: 15px">Temporary Access Token</p>
</div>
</div>

<br/> 

<p>:point_up: As stated by Meta, this token is only valid for 24 hours. So let’s not use it.</p>

<br/> 



### 1. Creating System Users

you should get a permanent token by generating a [System User Access Token](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens). 

Here are the steps to create a system user:

1. Sign in to the [Meta Business Suite](https://business.facebook.com/).
2. Locate your business account in the top-left dropdown menu and click its **Settings** (gear) icon.
3. Click **Business settings**.
4. Navigate to **Users** → **System users**
5. Click the **Add** button and create either an admin or employee system user.


### 2. Generating System User Access Tokens

To generate a System User access token after creating a system user:
1. Sign in to the [Meta Business Suite](https://business.facebook.com/).
2. Locate your business account in the top-left dropdown menu and click its **Settings** (gear) icon.
3. Click **Business settings**.
4. Navigate to **User** → **System** users.
5. Select the appropriate system user from the list of system users.
6. ~~Click the Generate new token button~~. → **Do Not Do this Yet**. See [Assign Assets](#assign-assets) below. 
7. Select the app that will use the token.
8. Select any permissions the app needs to function properly and generate the token.

##### Assign Assets
We stop you at Step 6 above, because you’ll need to assign your WhatsApp app as the **Asset** first to get the proper scopes for the token. Please follow the steps below to assign your WhatsApp app as the Asset:

1. In System Users, click on [**Assign Asset**](#assign-assets-step-1).
2. Then go to **Apps** and select the app you created, and give it [**Full control**](#assign-assets-step-2).
3. Click **Generate new token** and select ***whatsapp_business_messaging*** and ***whatsapp_business_management*** in **Permissions**. It should look like [this](#assign-assets-step-3).
4. Once the token is generated, a [pop-up](#assign-assets-step-4) will show up to show you the information of the generated token. Copy the token.
5. Now click on the token, it’ll open the [**Access Token Debugger**](#assign-assets-step-5) and show you the correct Scope. Here you need to make sure you have ***whatsapp_business_messaging*** and ***whatsapp_business_management***.
6. Copy and paste the token to [SeaChat](#assign-assets-step-6).
7. Turn on your [**App Mode**](#assign-assets-step-7) to be **Live**.
8. Add your business phone number to your WhatsApp app by going back to [**WhatsApp** →  **Configuration**](#assign-assets-step-8) and add your WhatsApp number there. It should show at least 1 production number.

<div style="display: flex; flex-direction: column; width:100%  ; align-items: center;">
    <div id="assign-assets-step-1" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/assign-asset-1.svg" target="_blank" style=" width: 100%; height: 10%; display: flex; justify-content: center; align-items: center; overflow: hidden; padding: 0">
            <img style="max-width: 100%; max-height: 50%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/assign-asset-1.svg" alt="Assign Access on Asset">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 1: Click on <strong>Assign Asset</strong></p>
    </div>
    <div id="assign-assets-step-2" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/assign-asset-2.svg" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/assign-asset-2.svg" alt="Give Full Control to App">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 2: Give App <strong>Full control</strong></p>
    </div>
</div>
<div id="assign-assets-step-3" style="display: flex; flex-direction: column; width:100%; align-items: center;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/assign-asset-3.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/assign-asset-3.png" alt="Generate token and assign asset">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 3: <strong>Generate token</strong> and set up <strong>Permission</strong></p>
    </div>
    <div id="assign-assets-step-4" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/assign-asset-4.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/assign-asset-4.png" alt="Copy Token">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 4: Copy token</p>
    </div>
</div>
<div style="display: flex; flex-direction: column; width:100% ; align-items: center;">
    <div id="assign-assets-step-5" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/assign-asset-5.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/assign-asset-5.png" alt="Access Token Debugger">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 5: Open the <strong>Access Token Debugger</strong></p>
    </div>
    <div id="assign-assets-step-6" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/assign-asset-6.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/assign-asset-6.png" alt="Paste Access Token to SeaChat">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 6: Paste token to SeaChat</p>
    </div>
</div>
<div style="display: flex; flex-direction: column; width:100% ; align-items: center;">
    <div id="assign-assets-step-7" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/assign-asset-7.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/assign-asset-7.png" alt="Set App Mode to Live">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 7: Set <strong>App Mode</strong> to <strong>Live</strong></p>
    </div>
    <div id="assign-assets-step-8" style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/whatsapp/assign-asset-8.png" target="_blank" style="height: 200px; width: 100%;height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="max-width: 100%; max-height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/assign-asset-8.png" alt="Add Business Number">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Step 8: Add business number</p>
    </div>
</div>

## Test your SeaChat agent via WhatsApp

Finally, we are all set up! Once your agent is set up, try to send a few messages and expect a reply from SeaChat:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/en/channels/whatsapp/test-whatsapp-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/test-whatsapp-1.png" alt="WhatsApp Conversation">
</a>
    <p style="margin-top: 20px; font-size: 15px">WhatsApp Conversation</p>
</div>
</div>

<br/> 

From the **Conversations** view in SeaChat, you can see the same conversation with the user/sender’s name.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/en/channels/whatsapp/test-whatsapp-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/test-whatsapp-2.png" alt="SeaChat Conversation">
</a>
    <p style="margin-top: 20px; font-size: 15px">SeaChat Conversation</p>
</div>
</div>

### Properly Decorating your WhatsApp Business Account


The above screenshot shows a pretty rudimentary WhatsApp account, which does not even have a profile picture. In the competitive digital landscape, having a strong online presence is crucial for businesses of all sizes. WhatsApp, with its massive user base and widespread popularity, offers a powerful platform for businesses to connect with their customers. However, setting up and managing a WhatsApp Business account effectively can be a daunting task.

One of the essential aspects of managing a WhatsApp Business account is setting up the profile properly. A well-optimized profile creates a professional image, instills trust, and enhances visibility. Unfortunately, many businesses overlook the importance of profile setup or struggle to find the right settings.

Let's properly set up WhatsApp account profile by going to [Meta WhatsApp Business Manager](https://business.facebook.com/wa/manage) to do this. Or if you are still in the Meta for Developers website, navigate to **WhatsApp → Quickstart → WhatsApp Business** and click **Account information**:


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/en/channels/whatsapp/deploy-1.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/deploy-1.png" alt="Account Information UI">
</a>
    <p style="margin-top: 20px; font-size: 15px">Account information</p>
</div>
</div>

<br/> 

This will bring you to the correct account under **WhatsApp Business Manager**. Here, you can make necessary changes, upload a profile picture, and save the updates. It may take a few minutes for the changes to take effect. Once they do, you'll notice the updated profile information when you access your WhatsApp business account's info page on your mobile device.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/en/channels/whatsapp/deploy-2.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/deploy-2.png" alt="Edit Account">
</a>
    <p style="margin-top: 20px; font-size: 15px">Make Changes to Account</p>
</div>
</div>



<br/> 

After a few minutes, if you click your WhatsApp business account’s info page on your WhatsApp app on your phone, it’ll reflect the change:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
<a href="/images/seachat/en/channels/whatsapp/deploy-3.png" target="_blank">
<img width="50%" height="auto" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/deploy-3.png" alt="WhatsApp Business Account Info.">
</a>
    <p style="margin-top: 20px; font-size: 15px">WhatsApp Business Account Info</p>
</div>
</div>

<br/> 

Optimizing your WhatsApp Business profile goes beyond just adding a profile picture. Here are some additional tips to enhance your profile:

2. **Use a Clear and Professional Profile Picture**:
Choose a high-quality image that represents your brand or business. Avoid blurry or low-resolution images, as they can create a negative impression.

3. **Add Relevant Contact Information**:
Ensure that your phone number, email address, and website (if applicable) are prominently displayed in your profile. This makes it easy for customers to reach you through their preferred channels.

4. **Use Labels and Tags**:
Organize your contacts and conversations using labels and tags. This helps you categorize and manage customer interactions effectively, making it easier to track and respond to specific inquiries or requests.

By following these tips, you can properly democratize your WhatsApp Business account, create a professional profile, and enhance your overall customer engagement.

# Engage with a real human agent
Did you notice in the above picture that I used /live_agent to request a human agent? If an agent happened to be online by setting their online status:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/whatsapp/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/live-agent-status.png" alt=""Live Agent Status>
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent status
</p>
</div>
</div>

<br/> 

They can directly talk with the user!

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/whatsapp/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/live-agent-interaction.png" alt="Live agent interaction with customers">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent interaction
</p>
</div>
</div>

<br/> 

If an agent is not online, they can turn on Email notification to receive real-time emails when a user initiates a chat, or request a live agent:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/whatsapp/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/ai-agent-preference.png" alt="SeaChat | Live Agent Preference">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent preference
</p>
</div>
</div>

<br/> 

## Remove your WhatsApp Integration

If you want to remove the WhatsApp integration, you need to do it in two places:

1. Properly remove the webhook from your Meta app
2. Click the Remove button inside SeaChat

For Step 1, please go to your [Meta Business app](https://developers.facebook.com/) → WhatsApp → Configuration → Callback URL → Edit → Remove webhook

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/whatsapp/remove-app-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/whatsapp/remove-app-1.png" alt="SeaChat | Remove Integration">
</a>
    <p style="margin-top: 20px; font-size: 15px">Remove integration</p>
</div>
</div>

<br/> 

## Messages Postback on WhatsApp

Once you have set up your Messenger integration, you will be able to interact with your customers using the [button feature](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/webpage-link/) of SeaChat. This allows you to add urls or additional information to your answers in the form of buttons. 

Now the customers can click on the buttons to get more information or to navigate to a webpage.

Every time a button is clicked, a postback message triggers the SeaChat API in conjunction with the WhatsApp API.

### Button limits on WhatsApp

WhatsApp has certain limitations on the postback messages. Make sure to  keep the following in mind when creating your buttons to avoid any issues.

The following are the limitations:

- WhatsApp’s message API supports up to **3 interactive buttons per message**.
- Each button’s text (title) is limited to **20 characters**.
- The payload or postback data sent when a button is clicked is limited to **200 characters**.
- These limits apply individually to each button, not collectively across all buttons.
- [Developer Documentation](https://developers.facebook.com/docs/whatsapp/guides/interactive-messages/)

[//]: # (A good solution to reduce the effect of these limitations is to use SeaChat's **[KB ID]&#40;https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/webpage-link/#kb-ids&#41;** feature. Please check out the link for more information.)

## :dart: Troubleshooting

If you have not received responses from SeaChat Agent on WhatsApp, you should verify the following settings that users tend to overlook:
- Are you utilizing a **temporary access token** that is valid for only 24 hours? A System User's [**Permanent Access Token**](#1-creating-system-users) should be used instead. 
- Has your WhatsApp application been set to [**Live mode**](#assign-assets)? Be sure that it is not operating in Development mode.
- Did you configure the [**webhook fields**](#perma-token-webhook) to allow the **message permission**? If this permission is not properly granted, SeaChat will be unable to receive messages from WhatsApp.
- Did your SeaChat agent receive a message, but you cannot see the reply from your WhatsApp? It might be that when you generated the permanent token, you did not [**Assign Assets**](#assign-assets) first.




## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 


---


#### LINE Official Account

<!-- Source: seachat-manual/04-channels/05-install-to-line.md -->

<!-- Weight: 501 -->

*Enhance your LINE Official Account by integrating auto-response in LINE with SeaChat AI agents.*



## :movie_camera: Integrate SeaChat with Your LINE Official Account

Follow the video tutorial to install SeaChat on your LINE Official Account and start responding to customer messages!

<iframe  width="100%" height="400" src="https://www.youtube.com/embed/5YCiO8GEAu0?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>


## Utilize SeaChat and LINE's Auto-Response Messaging Functionality Together

You can use SeaChat as an AI assistant providing useful information, capable of understanding various questions and answering based on the knowledge base, while the LINE keyword auto-response function is mainly used to trigger actions and send media messages such as coupons, card messages, and videos. By combining the functionalities of SeaChat and LINE auto-response, you can effectively enhance user experience and strengthen interaction with customers.

|                                  | Line Automatic Response                                                                                  | SeaChat AI Assistant                                                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Natural Language Understanding**            | None                                                                                                     | Yes                                                                                                                                                                              |
| **Data Setup/Training**          | One-time keyword setup                                                                                   | Supports multiple file formats                                                                                                                                                   |
| **Message Types**                | Images, Text, Videos, etc.                                                                               | AI Text Messages                                                                                                                                                                 |
| **Keyword Setup**                | Yes                                                                                                      | Yes                                                                                                                                                                              |
| **Summary of Customer Conversations** | No                                                                                                       | Yes                                                                                                                                                                              |
| **Switch to Human Customer Service**  | No                                                                                                       | Yes                                                                                                                                                                              |
| **Suitable Scenarios**           | Fixed responses for brand/product related keyword-triggered basic responses                              | Highly contextual answers based on knowledge base, flexible and personalized responses, can be used for product recommendations, customer service, and collecting customer information, etc. |

<br/>
<center>

*LINE Automatic Response v.s. SeaChat AI Assistant*
</center>
<br/>

### Configuration Steps

1. Choose "Manual chat + auto-response" for LINE responses setting.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/choose-manual-chat-plus-auto-response-for-line-responses-setting.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/choose-manual-chat-plus-auto-response-for-line-responses-setting.png" alt="Choose manual chat plus auto-response for LINE responses setting">
</a>

*Choose manual chat plus auto-response for LINE response setting*
</center>
<br/>

2. To avoid duplicate responses, change LINE's auto-response to keyword response by going to [LINE Business](https://manager.line.biz/) > Auto-Response Messages > Click on Keyword Response.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/change-lines-auto-response-to-keyword-response.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/change-lines-auto-response-to-keyword-response.png" alt="Change LINE's auto-response to keyword response">
</a>

*Change LINE's auto-response to keyword response*
</center>
<br/>

3. Add the desired keywords to the keyword response and set up the messages, for example - the keyword for business hours could be: store hours, business hours, etc. And in the message setting, input: "We are open Monday to Friday, 9am to 6pm."

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/add-keywords-to-keyword-response.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/add-keywords-to-keyword-response.png" alt="Add keywords to keyword response">
</a>

*Add keywords to keyword response*
</center>
<br/>

4. Open SeaChat and add a knowledge base document.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/seachat-knowledge-base.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/seachat-knowledge-base.png" alt="Add knowledge to SeaChat knowledge base">
</a>

*Add knowledge to SeaChat knowledge base*
</center>
<br/>

5. Enter these keywords into the document title of SeaChat and provide additional explanations in the document text: You can write additional messages, such as appointment links, transferring to customer service, etc., and adjust the weight to 75.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/enter-keyword-response-into-seachat-knowledge-base.png" target="_blank">
<img height="60%" width="100%" src="/images/seachat/en/channels/line/enter-keyword-response-into-seachat-knowledge-base.png" alt="Enter keyword response into SeaChat knowledge base">
</a>

*Enter keyword response into SeaChat knowledge base*
</center>
<br/>

6. SeaChat AI Assistant will not repeat responses on LINE, and can help expand knowledge for your customers to improve their experience. LINE messages can be set as images, videos, and for more contexual responses, you can rely on SeaChat.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/LINE-text-messages-you-can-rely-on-seachat.png" target="_blank">
<img height="100%" width="50%" src="/images/seachat/en/channels/line/LINE-text-messages-you-can-rely-on-seachat.png" alt="LINE text messages you can rely on SeaChat">
</a>

*Respond to Customers using SeaChat and LINE auto-responses*
</center>
<br/>

## Managing LINE and SeaChat Integration

### Option 1: Completely Disable LINE Live Chat

**Step 1:** Disable the LINE live chat feature.

**After Disabling:**

* You can then use SeaChat's features to replace LINE's auto-reply and live chat functions, with all conversation records being saved in SeaChat.

### Option 2: Using Both Platforms Simultaneously

In this setup, both LINE and SeaChat can respond to incoming messages. However, special attention is needed when managing replies from each platform. Users can switch between the LINE backend or the SeaChat backend for live chat.

#### Auto-Reply:

* SeaChat can automatically respond to messages. These replies will appear in both the LINE backend and the SeaChat backend.

#### Live Reply from LINE Backend:

**Advantages:**

* Live replies will be fully displayed in the LINE backend.

**Disadvantages:**

* Live replies will not be shown in the SeaChat backend.
* SeaChat won't be aware that a live reply has been sent from LINE, so it will continue to send its own reply. This may result in the user receiving two responses: the SeaChat reply (usually the first) and the live reply from the LINE backend.
* Using SeaChat to reply incurs a cost of approximately NT$0.3 per message (GPT-3.5) or NT$0.18 per message (GPT-4o-mini).

#### Live Reply from SeaChat:

**Advantages:**

* Live replies will be fully displayed in the SeaChat backend.

**Disadvantages:**

* Live replies will not be shown in the LINE backend.
* These replies will count against LINE's monthly message limit (200 messages per month for free users). If the monthly limit is reached, you won't be able to send additional messages without upgrading your plan.

## LINE's Pricing Strategy

* Live replies sent through the LINE Official Account Manager do not count toward the free message quota.
* For detailed pricing, refer to the official pricing information: [LINE Official Account Manager Pricing](https://tw.linebiz.com/column/LINEOA-2023-Price-Plan/)

### Which Types of Messages Are Charged?

* Only "Broadcast Messages," "Push API Messages from the Advanced Features of the Messaging API," and "Progressive Messages" are counted toward the message limit. The following types of messages are considered "free":
    * Welcome messages for new friends.
    * One-on-one live chat messages.
    * Auto-reply messages.
    * AI auto-reply messages.
    * Messaging API's Reply API.

<br/>


## Limits of LINE Button Messages

When users are using the LINE channel with SeaChat, they may encounter issues where the button message is cut off when the message button is clicked. This is due to the character limit for the LINE button message.

Here is a summary of the current limits for our button templates and postback buttons:

- **Message character limit**: 200 characters

- **Postback button content character limit**: 300 characters across all buttons

- **Postback button number limit**: Up to 4 buttons

For detailed reference, please visit the following sections on LINE's developer documentation:

Button template message character limit and number of buttons limit under the [Buttons Template](https://developers.line.biz/en/reference/messaging-api/#template-messages) section.

Postback Button’s content character limit under the [Postback Action](https://developers.line.biz/en/reference/messaging-api/#action-objects) section.

SeaChat has a solution for this issue. Utilize the feature of KB ID to avoid the message being cut off. Please check out our wiki about [KB ID](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/webpage-link/#kb-ids) for more information on how to avoid the message being cut off.


## LINE's AI Auto-Reply Function Will Be Discontinued Soon

[LINE's AI auto-response function](https://tw.linebiz.com/manual/line-official-account/oa-manager-smartchat/) will be discontinued in May 2024.

If you are still using the AI auto-response function, make sure to arrange alternative solutions soon.

## 🔖 FAQ

### How do the customers know that the Live Agent has left the chat?

When the Live Agent finishes a conversation, he/she can click on the **Complete** button. The customer will see a message saying that **the Live Agent has left the conversation.**

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/line/faq-1.png" target="_blank">
<img height="50%" width="100%" src="/images/seachat/en/channels/line/faq-1.png" alt="LINE text messages you can rely on SeaChat">
</a>

</center>
<br/>

### Can I set an activation time for my AI Agent to start the conversation automatically? 

Currently, we do not support setting an activation time for the AI Agent to start the conversation automatically. However, you can easily turn on the AI Agent by clicking on **Complete** button in a conversation once you have finished your conversation. Refer to our [tutorial](/en/seachat/seachat-manual/02-create-agent/02-live-agent-transfer) for more information.

### Can I see the response of the AI Agent in the LINE chat?

Yes, you can see both the agent's and live agent's responses. You will have a complete overview of the chat. However, we recommend using SeaChat's conversation platform to have a better overview and control of all the conversations.

### Why does my button says "Live Agent" in my LINE Channel? How can I change it to Chinese?

To change the language of your button from English to Chinese in the UI of your LINE channel, you should go to the **Webchat Widget** channel.

In **Channels**, find the **Webchat Widget** channel. Modify the language to Chinese in the **Basic Settings**. This will then change the language of the buttons in the UI of your LINE chat. Now it should say **真人客服** instead of **Live Agent**.

<div style="display: flex; flex-direction: column; align-items: center;">
  <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/agent-information/webchat-settings-for-thrid-parties.png" target="_blank">
      <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/agent-information/webchat-settings-for-thrid-parties.png" alt="image that displays the additional options in Chat Settings">
    </a>
  </div>
  <p style="margin-top: 20px; font-size: 15px">Webchat Chat Settings and Basic Settings</p>
</div>


---


#### Facebook Messenger Using Embedded Signup

<!-- Source: seachat-manual/04-channels/09-seachat-messenger-integration-embedded-signup.md -->

<!-- Weight: 502 -->

*Set up a ChatGPT-powered bot on Facebook Messenger. Follow our guide to create a Meta app, configure webhooks, and launch your bot for seamless communication.*



This guide will walk you through how to connect your Facebook Page to SeaChat using Facebook Embedded Signup.

###  ✨ Why Use Embedded Signup?
Compared to the old method, SeaChat’s Messenger integration with embedded signup is simpler, faster, and more powerful. Here’s why:

✅ Seamless Setup Experience
You no longer need to leave the SeaChat interface or switch tabs. Everything happens within SeaChat — login, permission approval, and Page connection.

✅ No Meta Developer Account Required
With embedded signup, you don’t need to create your own Meta App or go through Meta’s App Review process. We’ve done that for you.

<!-- ✅ Pass <a href="https://developers.facebook.com/docs/messenger-platform/send-messages/?locale=en_US" target="_blank">Meta's 24-Hour Rule</a>for Live Agent Support. With SeaChat’s Messenger integration, users can message your Page at any time — and SeaChat will receive it instantly. Thanks to our Meta-approved app with Human Agent permission , your support team can reply even after the 24-hour window , without needing message templates or extra approvals. No need to create your own Meta app or go through App Review — SeaChat handles it all so you can focus on helping your customers. -->


### Connect Your Facebook Page with JUST TWO STEPS
Go to the `Messenger With Embedded Signup` card in your SeaChat Channels page.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-1.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

**Step 1: Signin to Facebook and Select Facebook Page**

- Click the Connect button and a Facebook login popup will appear.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

- Login with your Facebook account that manages the Page.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2-1.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

- Select the Page you want to connect and grant all requested permissions. Note that we only support one Page per AI agent. If you want to connect multiple Pages, you need to create a new SeaChat AI agent for each Page.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-2-2.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

**Step 2: Choose Channel Specific Language**
Define the language of voice messages so SeaChat can transcribe them to text, and reply in the same language. This also works on system messages (e.g., after user clicks 🧹New Topic)

🚀 You’re All Set!
Once completed, SeaChat will start handling messages via your SeaChat AI agent. You can test it right away by sending a message to your connected Page.

### Already Connected Messenger the Old Way?
If you previously integrated Messenger through our old method, here’s how to switch:
Go to your Messenger Integration page in SeaChat.

- Find the Messenger Integration(Deprecated) card.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-integration-embedded-signup-3.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

- Click Remove button on the upper right norner to remove the old integration.
- Then, go to the new `Messenger With Embedded Signup` card and follow the updated steps to reconnect.

🙋 Need help with the migration? <br/>
📧 Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai). <br/>
🌍 We offer multilingual customer service and are happy to assist!


### Engage with a real human agent
Did you notice in the above picture that I used /live_agent to request a human agent? If an agent happened to be online by setting their online status:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 40%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" alt="SeaChat | Messenger | Live Agent Status">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent status
</p>
</div>
</div>

<br/> 

They can directly talk with the user!

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" alt="SeaChat | Messenger | Live Agent interaction Example">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent interaction
</p>
</div>
</div>

<br/> 

If an agent is not online, they can turn on Email notification to receive real-time emails when a user initiates a chat, or request a live agent:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" alt="SeaChat | Messenger | Live Agent Preference">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent preference
</p>
</div>
</div>

<br/> 



## Respond to Voice Clips
Do you know that SeaChat supports audio messages too? If a user sends a voice clip, SeaChat can transcribe it to text, and respond via text!

Currently, it supports English speech to transcription, but let us know if you want more languages supported.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" alt="SeaChat | Messenger | Messenger Voice Clip">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Facebook Messenger voice clip transcription and response by SeaChat</strong></p>
</div>
</div>

<br/> 

### Button limits on Messenger

After following the above steps, you can now use the button feature on SeaChat integrated with Messenger. However, since we are still using the API provided by Messenger, there are some limitations to keep in mind when creating your buttons to avoid any issues.

The following are the limitations:

- The button template allows up to **3 postback buttons** per message template.
- Each button can have a **payload of up to 1000 characters**, which is sent back to your webhook when clicked.
- The **button title** is limited to **20 characters**.
- These limits apply to each individual button, so you can have 3 buttons per message, each with its own 1000-character payload and 20-character title.
- [Developer Documentation](https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback)

A good solution to reduce the effect of these limitations is to use SeaChat's **[KB ID](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/webpage-link/#kb-ids)** feature. Please check out the link for more information.


## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).


---


#### Facebook Messenger(Deprecated)

<!-- Source: seachat-manual/04-channels/06-seachat-messenger-integration.md -->

<!-- Weight: 503 -->

*Set up a ChatGPT-powered bot on Facebook Messenger. Follow our guide to create a Meta app, configure webhooks, and launch your bot for seamless communication.*


Note: This Messenger Integration is deprecated. Please use [Messenger Integration With Embedded Signup](/en/seachat/seachat-manual/04-channels/09-seachat-messenger-integration/) instead.

## 🎥 Video Tutorial
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/aFruY5bwG00?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


## Overview
In this section, we will dive deeper into the process of setting up a ChatGPT-powered chatbot or chat agent on Facebook Messenger. By the end of this section, you will have a clear understanding of how to:
1. **Automate responses to user messages**: 
  - Connect your Messenger business account to the SeaChat chatbot and agent platform.
  - Train the chatbot using ChatGPT's advanced language model to generate natural language responses to a wide range of user queries.
  - Configure the chat agent to automatically respond to incoming messages based on your knowledge base.
2. **Access all conversations with users through SeaChat**:
  - Use SeaChat, a user-friendly interface, to access and monitor all conversations between users and your chatbot.
  - Review chat transcripts, analyze user behavior, and identify areas for improvement in the chat agent's responses.
  - Manage and organize conversations efficiently to ensure seamless communication with users.
3. **Enable users to request live agent assistance**:
  - Implement a special command that allows users to request assistance from a real human agent if they have complex queries or require personalized support.
  - Seamlessly transfer conversations from the AI chat agent to live human agents, ensuring a smooth and efficient transition.
  - Empower users to choose the level of support they need, enhancing the overall customer experience.

By the end of this tutorial, you’ll have a SeaChat agent powered Facebook Messenger bot and also a SeaChat console to view all messages, as shown below:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/facebook-messenger-integration.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/facebook-messenger-integration.png" alt="SeaChat | Facebook Messenger Integration">
</a>
    <p style="margin-top: 20px; font-size: 15px">ChatGPT-powered chatbot integration with Facebook Messenger using SeaChat</p>
</div>
</div>

<br/> 

Before embarking on the setup process, it's essential to keep in mind a few key points:

**Messenger limitations**:
  - The SeaChat AI agent is designed to respond to incoming messages only and cannot initiate conversations on its own.
  - However, you as the agent creator will still be able to talk with the users once a live human agent is requested.

**Who benefits from this integration**:
  - Businesses and organizations with a high volume of incoming Messenger messages that require automation.
  - Companies looking to provide personalized and engaging customer support experiences.
  - Customer service departments seeking to reduce the burden on human agents by automating routine inquiries.

---

## Facebook Messenger Setup
Setting up Facebook Messenger can be a straightforward process with the right guidance. Here's a short version of the steps involved. You can also click on the titles to see a more detailed explanation of each step:

1. **[Create a Messenger App](#create-a-facebook-messenger-app)**:
- Go to the Meta Developer Site.
- Click on **My Apps** in the top-right corner.
- Select **Create App** from the dropdown menu.

2. **[Choose App Type](#choose-app-type)**:
- Choose **Other** under **App Type**.
- Enter a unique app name, avoiding the use of **Messenger App** or **Facebook** in the name.

3. **[Add Messenger Product](#add-messenger-product)**:
- Scroll down to the bottom of the app list.
- Find **Messenger** and select it to add the product to your app.

5. **[Configure Messenger Application](#step-1-configure-webhooks)**:
- Carefully review the information on the configuration page.
- Follow the instructions to provide necessary details, such as business name, address, and contact information.
- Ensure that all required fields are filled out correctly.

6. **[Generate Access Token](#step-2-generate-access-token)**:
- Once the configuration is complete, generate a permanent access token.
- This token is essential for using the Messenger API.

7. **[Remove Your Messenger Integration](#remove-your-messenger-integration)**:
- Properly remove the page access from your Meta app
- Click the Remove button inside SeaChat

> :books: **Recommended Reading**:
> 
> Remember to adhere to the [Messenger API](https://developers.facebook.com/docs/messenger/) policies and guidelines to maintain compliance and avoid any potential issues.


The following is an elaborated explanation that walks you through the process step-by-step:

### Create a Facebook Messenger App

You’ll first need to go to [Meta Developer Site](https://developers.facebook.com/) and create a new Facebook Messenger app by clicking **My Apps** in the top right corner, and then selecting **Create App** from the dropdown menu.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/facebook-messenger/create-new-messenger-app.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/create-new-messenger-app.png" alt="SeaChat | Messenger | Create New Messenger">
    </a>
<br/>
    <p style="margin-top: 20px; font-size: 15px">Create a New Messenger</p>
</div>
</div>

### Choose App Type
Create an **Other** app because we’ll just use this App for accessing your Messenger account. On the **Select app type page**, select **Business** for the type, then click **Next**.

<br/>
<div style="display: flex; flex-direction: column; align-items: center;">
    <div style="width: 100%; height:100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-1.png" target="_blank" style="height: 200px; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-1.png" alt="SeaChat | Messenger | Create Other App">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Create an <strong>Other</strong> app</p>
    </div>
<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-2.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-2.png" alt="SeaChat | Messenger | Choose Business">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Choose <strong>Business</strong></p>
    </div>
</div>

<br/>

Here we created an app called **Seasalt.ai App**, note that Meta doesn’t allow the app to have **Facebook** or **Messenger** in the name. Carefully read through warning messages when choosing the app name.

<br/>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/channels/facebook-messenger/choose-app-type-3.png" target="_blank" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/choose-app-type-3.png" alt="SeaChat | Messenger | Choose App Type">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Create App</p>
    </div>
<br/>

### Add Messenger Product

After creating the App, let’s add the [Messenger product](https://developers.facebook.com/docs/messenger/). Find the Messenger box under the **Add products to your app** section, and click **Set up** to create your app.

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/facebook-messenger/add-messenger-product.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; height: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/add-messenger-product.png" alt="SeaChat | Messenger | Add Messenger Products">
    </a>
<br/>
    <p style=" font-size: 15px">Add Messenger to Your App</p>
</div>
</div>

## How to Configure Messenger Application
> :rotating_light: **Warning** :rotating_light:
>
> Here is where things get a bit more complicated.  If you are not careful enough and miss a step, you might not be able to successfully configure your Messenger application. So, let's carefully go through the following instruction together.

### Step 1: Configure webhooks

Find **Messenger API** under **Messenger** on the left. From here we’ll first need to configure the Webhook and tokens provided by SeaChat.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-1.png" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-1.png" alt="SeaChat | Messenger | Configuration Step 1">
    </a>
<br/>
    <p style=" font-size: 15px">Verify Token</p>
</div>
</div>


Here is all you have to do. Go to SeaChat, navigate to **Agent Configuration → Channels → Messenger** to get the **Callback URL** and **Verify token**. 

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
   <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-2.png" target="_blank"
style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;">
    <img id="perma-token-webhook" width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-2.png" alt="SeaChat | Messenger | Configuration Step 2">
    </a>
<br/>
    <p style=" font-size: 15px">Navigate to <strong>Messenger</strong> on SeaChat</p>
</div>
</div>


Copy SeaChat’s Step 1 and paste it to corresponding parts on Messenger dashboard.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-3.png" alt="SeaChat | Messenger | Configuration Step 3">
</a>
    <p style="margin-top: 20px; font-size: 15px">Copy SeaChat info to configure</p>
</div>
</div>

<br/>

Paste the **Callback URL** and **Verify token** to the corresponding fields on the Messenger dashboard:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-4.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-4.png" alt="SeaChat | Messenger | Configuration Step 4">
</a>
    <p style="margin-top: 20px; font-size: 15px">Paste the URL and token</p>
</div>
</div>

<br/>

After this, we’ll need to properly configure **Webhook Fields** to give the right permission to the webhook callback URL:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-5.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-5.png" alt="SeaChat | Messenger | Configuration Step 5">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Webhook Fields</strong> configuration</p>
</div>
</div>

<br/>

Select **messages** and click **Subscribe**:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-6.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-6.png" alt="SeaChat | Messenger | Configuration Step 6">
</a>
    <p style="margin-top: 20px; font-size: 15px">Subscribe selected messages</p>
</div>
</div>

<br/>

So your final configuration of webhook would look like this:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/how-to-config-7.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/how-to-config-7.png" alt="SeaChat | Messenger | Configuration Step 7">
</a>
    <p style="margin-top: 20px; font-size: 15px">Webhook configuration</p>
</div>
</div>

<br/>

### Step 2: Generate Access Token

The Meta app needs to access a certain Facebook Page to be able to receive messages sent from that Page. So in Step 2, you’ll first need to authorize it to access your public Facebook Page.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-1.png" alt="SeaChat | Messenger | Access Token Step 1">
</a>
    <p style="margin-top: 20px; font-size: 15px">Generate Access Token</p>
</div>
</div>

<br/>

After authorizing with a Facebook Page, you can further **Add Subscriptions**:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-2.png" alt="SeaChat | Messenger | Access Token Step 2">
</a>
    <p style="margin-top: 20px; font-size: 15px">Click on <strong>Add Subscription</strong></p>
</div>
</div>

<br/>

Again, we want to subscribe to **messages**:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-3.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-3.png" alt="SeaChat | Messenger | Access Token Step 3">
</a>
    <p style="margin-top: 20px; font-size: 15px">Choose <strong>messages</strong></p>
</div>
</div>

<br/>

Finally, let’s generate the access token:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-4.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-4.png" alt="SeaChat | Messenger | Access Token Step 4">
</a>
    <p style="margin-top: 20px; font-size: 15px">Token generation</p>
</div>
</div>

<br/>

Once the token is generated, we need to copy the token:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-5.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-5.png" alt="SeaChat | Messenger | Access Token Step 5">
</a>
    <p style="margin-top: 20px; font-size: 15px">Token details</p>
</div>
</div>

<br/>

Paste it to Step 2 of SeaChat Messenger setup:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/access-token-6.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-6.png" alt="SeaChat | Messenger | Access Token Step 6">
</a>
    <p style="margin-top: 20px; font-size: 15px">Paste Token to SeaChat</p>
</div>
</div>

<br/>

Now turn on your App Mode to be **Live** and you can chat with the bot:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a id="live-mode" href="/images/seachat/en/channels/facebook-messenger/access-token-7.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/access-token-7.png" alt="SeaChat | Messenger | Access Token Step 7">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live mode</p>
</div>
</div>

<br/>

### Step 3: Alternative to  Complete App Review

So far your messenger bot will respond **only to you**, the app creator. If you pass it to others, they will not get a response at all. It might be tempting to do “Step 3. Complete App Review” per Facebook’s instructions:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/app-review-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/app-review-1.png" alt="SeaChat | Messenger | App Review Step 1">
</a>
    <p style="margin-top: 20px; font-size: 15px">App review</p>
</div>
</div>

<br/> 

However, It might take up to 5 days to complete the App Review and the process is very cumbersome. For instance, it requires you to take a video walkthrough of the Meta app.

An alternative way is to assign the page to the business you have with Meta. To do so, go to [Meta Business Suite](https://business.facebook.com/), select the business your Meta app was created under, and then go to **Accounts** → **Pages**, and make sure that the Facebook Page your chatbot is connected to is there:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/facebook-pages.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/facebook-pages.png" alt="SeaChat | Messenger | Facebook Pages">
</a>
    <p style="margin-top: 20px; font-size: 15px">Make sure the Facebook Page shows up under your business 
</p>
</div>
</div>

<br/> 

You should now be all set!

# Engage with a real human agent
Did you notice in the above picture that I used /live_agent to request a human agent? If an agent happened to be online by setting their online status:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 40%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-status.png" alt="SeaChat | Messenger | Live Agent Status">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent status
</p>
</div>
</div>

<br/> 

They can directly talk with the user!

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/live-agent-interaction.png" alt="SeaChat | Messenger | Live Agent interaction Example">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent interaction
</p>
</div>
</div>

<br/> 

If an agent is not online, they can turn on Email notification to receive real-time emails when a user initiates a chat, or request a live agent:

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/ai-agent-preference.png" alt="SeaChat | Messenger | Live Agent Preference">
</a>
    <p style="margin-top: 20px; font-size: 15px">Live agent preference
</p>
</div>
</div>

<br/> 

## Remove your Messenger Integration

If you want to remove the Messenger integration, you need to do it in two places:
1. Properly remove the page access from your Meta app
2. Click the Remove button inside SeaChat

For Step 1, please go to your **[Meta Business app](https://developers.facebook.com/)** → **Messenger** → **Messenger API Settings** → **Generate access tokens** → remove

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/remove-app-1.png" alt="SeaChat | Messenger | Remove App">
</a>
    <p style="margin-top: 20px; font-size: 15px">Remove integration</p>
</div>
</div>

<br/> 

## Respond to Voice Clips
Do you know that SeaChat supports audio messages too? If a user sends a voice clip, SeaChat can transcribe it to text, and respond via text!

Currently, it supports English speech to transcription, but let us know if you want more languages supported.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/messenger-voice-clip.png" alt="SeaChat | Messenger | Messenger Voice Clip">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Facebook Messenger voice clip transcription and response by SeaChat</strong></p>
</div>
</div>

<br/> 

## Messages Postback on Messenger

Once you have set up your Messenger integration, you will be able to interact with your customers using the [button feature](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/webpage-link/) of SeaChat. This allows you to add urls or additional information to your answers in the form of buttons.

To activate, simply go on the page of **Edit Page Subscription** on Messenger. 

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/facebook-messenger/edit-page-subs-postback.png" alt="SeaChat | Messenger | Edit Page Postback Feature">
</a>
    <p style="margin-top: 20px; font-size: 15px"><strong>Enable Postback on Edit Page Subscription</strong></p>
</div>
</div>

<br/> 

### Button limits on Messenger

After following the above steps, you can now use the button feature on SeaChat integrated with Messenger. However, since we are still using the API provided by Messenger, there are some limitations to keep in mind when creating your buttons to avoid any issues.

The following are the limitations:

- The button template allows up to **3 postback buttons** per message template.
- Each button can have a **payload of up to 1000 characters**, which is sent back to your webhook when clicked.
- The **button title** is limited to **20 characters**.
- These limits apply to each individual button, so you can have 3 buttons per message, each with its own 1000-character payload and 20-character title.
- [Developer Documentation](https://developers.facebook.com/docs/messenger-platform/reference/buttons/postback)

A good solution to reduce the effect of these limitations is to use SeaChat's **[KB ID](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/webpage-link/#kb-ids)** feature. Please check out the link for more information.

## :dart: Troubleshooting

If you have not received responses from SeaChat Agent on Messenger, you should verify the following easily missed settings:
- Has your Messenger application been set to [**Live mode**](#live-mode)? Be sure that it is not operating in Development mode.
- Did you configure the [**webhook fields**](#perma-token-webhook) to allow the **message permission**? If this permission is not properly granted, SeaChat will be unable to receive messages from messenger.


## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).


---


#### Calls

<!-- Source: seachat-manual/04-channels/07-seachat-voicebot.md -->

<!-- Weight: 504 -->

*Handle inbound/outbound calls, get a toll-free number, and enable live transfers with  with SeaChat's voice agent.*


Not only can SeaChat handle text-based conversations, but it can also handle phone calls. The SeaChat allows you to create a voice-based conversational agent to pick up all the inbound calls or to call out to customers. This voice agent can handle inbound calls, answer customer queries, and provide customer support. The SeaChat voice agent can also transfer calls to live agents when needed, providing a seamless experience for your customers. 

In the following sections, we will show you how easy it is to set up the SeaChat voice agent and how you can test your agent with actual calls.

---

## Setting up the SeaChat Voice Agent

First, we need a new agent that can handle voice calls. To create a new voice agent, click on the agent dropdown menu next to your avatar. You can see the list of agents that you have created. Click on the **Add New Agent** button to create a new agent. 

In my agent description, I made sure to include that this agent is for voice calls. This way, I can easily identify which agent is for voice calls and which agent is for text-based conversations.

<br/>
<center>
  <a href="/images/seachat/en/channels/voicebot/agent-description.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/voicebot/agent-description.png" alt="SeaChat | VoiceBot | Agent Description">
</a>

*Add Agent Description*
</center>

Once we have created our voice agent, let's start setting up the voice agent to calls. Find *Calls* in **Channel** under **Agent Configuration**. 

<br/>
<center>
  <a href="/images/seachat/en/channels/voicebot/choose-calls.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/voicebot/choose-calls.png" alt="SeaChat | Messenger | Choose Callee Agent">
</a>

*Setting up **Calls** Channel*
</center>

### Toll-Free Number

In the **Calls** channel, we need to first purchase a toll-free phone number. Choose the country where you want to purchase the toll-free number and phone number. Once you have chosen the desirable configuration,  click on the **Confirm Purchase** button.

<br/>
<center>
  <a href="/images/seachat/en/channels/voicebot/buy-a-number.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/voicebot/buy-a-number.png" alt="SeaChat | Messenger | Buy a Number">
</a>

*Purchase a toll-free number*
</center>

Once purchased, you can see the toll-free number of your choice. You can always release the number and purchase a new one if you are not satisfied with the number.

<br/>
<center>
  <a href="/images/seachat/en/channels/voicebot/toll-free-number.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/voicebot/toll-free-number.png" alt="SeaChat | Messenger | Toll Free Number">
</a>

*Toll-free number details*
</center>

### Agent Configuration

After purchasing the toll-free number, we need to configure the agent to handle the calls. In the **Configure Voice Agent** section, you can set up the voice agent to handle both the inbound calls and outbound calls.

You are welcome to enable the live agent feature for your voice agent just like any other SeaChat agent. Please make sure you have a real-human agent that will monitor and respond to the user when the live agent feature is enabled.

<br/>
<center>
  <a href="/images/seachat/en/channels/voicebot/configure-agent.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/voicebot/configure-agent.png" alt="SeaChat | Messenger | Agent Configuration">
</a>

*Voice agent configuration*
</center>

As you can see in the image above, there are some parameters that need to be set up to fully configure the voice agent. If you are not sure about the configuration, you can start from choosing the language and SeaChat will automatically set up the rest of the configuration for you.

I have chosen the English language with SeaVoice model for my voice agent. Now click on **Save Configuration** to consolidate your settings.

> :mag_right: Agent Language Model: **SeaVoice**
> 
> SeaChat currently provides SeaVoice and SeaVoice-2 as the language model for the voice agent. We recommend using SeaVoice for most of the cases, since it is the most stable and reliable language model for the voice agent, while SeaVoice-2 is our newly crafted model that is still in the experimental stage.

## Testing the Voice Agent

Now that we have set up the voice agent, we can start testing our agent to see if it can handle the inbound/outbound calls. 

<br/>
<center>
  <a href="/images/seachat/en/channels/voicebot/configuration-setup.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/voicebot/configuration-setup.png" alt="SeaChat | Messenger | Configuration Steps">
</a>

*Configuration set up*
</center>

### Inbound and Outbound Calls

There are two ways to test the voice agent. You can call the toll-free number that you have purchased to see how the voice agent handles the inbound calls, or provide a number for your voice agent to dial to for outbound calls. Since the two methods might require different configuration in agent setting, choose the method that suits you the best. 

<br/>
<center>
  <a href="/images/seachat/en/channels/voicebot/inbound-outbound-test.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/voicebot/inbound-outbound-test.png" alt="SeaChat | Messenger | Inbound/ Outbound Tests">
</a>

*Test you agent*
</center>

That's it. Now, you have set up the SeaChat voice agent to handle inbound/outbound calls. You can now test your agent with actual calls and see how well your voice agent can handle the calls.

## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

---


#### Instagram with OAuth Login

<!-- Source: seachat-manual/04-channels/10-instagram-oauth.md -->

<!-- Weight: 505 -->

*Follow these steps to integrate Instagram with your app and build a messaging AI agent.*


---

## Prerequisites

- **Instagram Professional Account**: You need either a Business or Creator account to set up Instagram Messaging. If your current account is not of this type, you can [switch it to a Professional account](https://www.facebook.com/business/help/502981923235522) in Instagram settings.

### Connect Your Instagram Account with JUST TWO STEPS

Go to the `Instagram` card in your SeaChat Channels page.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/instagram/instagram-card.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/instagram-card.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

**Step 1: Signin to your Instagram Account**

Click the Connect button and a Instagram login popup will appear. Grant all the permissions and click `Allow`.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/instagram/instagram-step-1.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/instagram-step-1.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 


**Step 2: Choose Channel Specific Language**

Define the language of voice messages so SeaChat can transcribe them to text, and reply in the same language. This also works on system messages (e.g., after user clicks 🧹New Topic)

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/instagram/instagram-step-2.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/instagram-step-2.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

🚀 You’re All Set!
Once completed, SeaChat will start handling messages via your SeaChat AI agent. You can test it right away by sending a message to your instagram account.

### Already Connected Instagram the Old Way?
If you previously integrated Instagram through our old method, you need to do it in two places:


#### Step 1: Remove from SeaChat

- Go to your Instagram Integration page in SeaChat. Find the Instagram Integration card under the `Deprecated` section.
<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat/en/channels/instagram/instagram-card-deprecated.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/instagram-card-deprecated.png" alt="SeaChat | Facebook Messenger Integration">
</a>
</div>
</div>

<br/> 

<br/> 

- Click Remove button on the upper right norner to remove the old integration.
- Then, go to the new `Instagram` card and follow the updated steps to reconnect.


#### Step 2: Remove from your Meta app

- Properly remove the page access from your Meta app
  - Go to your **Meta Business app** → **Instagram** → **API setup with Instagram login** → **Generate access tokens** → **trash can icon** → **Remove Account**


🙋 Need help with the migration? <br/>
📧 Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai). <br/>
🌍 We offer multilingual customer service and are happy to assist!

---


#### Instagram (Deprecated)

<!-- Source: seachat-manual/04-channels/08-instagram.md -->

<!-- Weight: 506 -->

*Follow these steps to integrate Instagram with your app and build a messaging AI agent.*


Note: This Instagram Integration is deprecated. Please use [Instagram Integration With OAuth Login](/en/seachat/manual/channels/instagram/) instead.

## Video Tutorial

<iframe width="100%" height="400" src="https://www.youtube.com/embed/50oKG8p-LzI?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  allowfullscreen></iframe>

---

## Prerequisites

- **Instagram Professional Account**: You need either a Business or Creator account to set up Instagram Messaging. If your current account is not of this type, you can [switch it to a Professional account](https://www.facebook.com/business/help/502981923235522) in Instagram settings.

## Instructions

### Step 1: Create an Instagram App

1. Visit the [Meta Developer Site](https://developers.facebook.com/) and click on **My Apps** in the top-right corner.
2. From the dropdown menu, select **Create App** to begin.

- Enter your app details, such as App Name and Contact Email, then click **Next**.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-name.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-name.png" alt="App Creation">
    </a>
</div>
</div>

<br/>

- Select a Use Case, choose **Other**, and click **Next**.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/use-cases.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/use-cases.png" alt="App Use Case Selection">
    </a>
</div>
</div>

<br/>

- Set the App Type to Business and click **Next**.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-type.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-type.png" alt="App Type Selection">
    </a>
</div>
</div>

<br/>

- Review your app details and click **Create App**.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/business-details.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/business-details.png" alt="App Review and Creation">
    </a>
</div>
</div>

<br/>


### Step 2: Add the Instagram Product to Your App

- Under the **Add Products to Your App** section, select Instagram.
- Click the **Set Up** button to add it to your app.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/add-instagram.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/add-instagram.png" alt="Add Instagram Product">
    </a>
</div>
</div>

<br/>

### Step 3: Connect Instagram Account

- Navigate to the API Setup with Instagram business login page.
- Click **Add Account** in Step 1 to connect to your Instagram account.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/instagram-connect.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/instagram-connect.png" alt="Connect Instagram Account">
    </a>
</div>
</div>

<br/>

### Step 4: Configure Webhook

1. Navigate to SeaChat to get the webhook URL.
   - Go to **Agent Configuration** → **Channels** → **Instagram** to find the Callback URL and Verify Token.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/seachat-channel.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/seachat-channel.png" alt="SeaChat Webhook Details">
    </a>
</div>
</div>

<br/>

2. Click **Set Up Verify Token** in Step 1. Once completed, a popup will confirm the token has been saved successfully.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/verify-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/verify-token.png" alt="Verify Token Confirmation">
    </a>
</div>
</div>

<br/>

3. Return to the Instagram app dashboard, paste the Webhook URL and Verify Token into the respective fields, and click **Save**.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/callback-url.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/callback-url.png" alt="Webhook URL and Tokens">
    </a>
</div>
</div>

<br/>

- Enable all necessary webhook events by clicking the **Manage** button to configure webhook fields.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/manage-webhook.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/manage-webhook.png" alt="Webhook Configuration">
    </a>
</div>
</div>

<br/>

### Step 5: Generate Access Token

- Click the **Generate Token** button in the Generate Access Token section.
- Check the **I Understand** checkbox in the popup to copy the access token.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/generated-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/generated-token.png" alt="Generate Access Token">
    </a>
</div>
</div>

<br/>

- Paste the copied token into Step 2 of the SeaChat Instagram setup interface and click **Save**.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/save-token.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/save-token.png" alt="Access Token Setup">
    </a>
</div>
</div>

<br/>

Now you’ve finished all steps to set up Instagram integration in SeaChat!


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/seachat-setup.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/seachat-setup.png" alt="Integration Complete">
    </a>
</div>
</div>

<br/>

### Step 6: Add Privacy Policy URL, Icon, and Category

1. Go to **App Settings** → **Basic**.
2. Add a Privacy Policy URL, Icon, and Category, then click **Save Changes**.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/app-setting.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/app-setting.png" alt="App Settings Update">
    </a>
</div>
</div>

<br/>

### Step 7: Set App to Live

- Toggle the **App Status** to Live.

Congratulations! You’ve successfully set up an Instagram Messaging AI agent. 🎉

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/set-app-to-live.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/set-app-to-live.png" alt="App Live Status">
    </a>
</div>
</div>

<br/>

### Step 9: Remove your Instagram Integration

If you want to remove the Instagram integration, you need to do it in two places:

- Properly remove the page access from your Meta app
  - Go to your **Meta Business app** → **Instagram** → **API setup with Instagram login** → **Generate access tokens** → **trash can icon** → **Remove Account**
- Click the **Remove** button inside SeaChat


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/channels/instagram/remove-on-seachat.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/channels/instagram/remove-on-seachat.png" alt="Remove Instagram channel on SeaChat">
    </a>
</div>
</div>

<br/>

---


#### Webpage

<!-- Source: seachat-manual/04-channels/08-install-to-webpage.md -->

<!-- Weight: 507 -->

*Integrate SeaChat into your webpage so your customers can chat with your AI agent anytime. Enhance your online presence and streamline communication.*


## :movie_camera: Integrate SeaChat Widget on Webpage

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/5YCiO8GEAu0?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## Customize Your Own Company Webpage Widget

Webpage widget is a powerful tool that allows you to integrate SeaChat into your website. This feature enables you to provide real-time customer support and engage with your website visitors. The widget can be customized to match your brand identity and website design. You can also create forms to collect visitor information and feedback.

## SeaChat Widget Configuration

SeaChat widgets come with a range of customization options to help you create a seamless customer experience. You can adjust the widget's appearance, behavior to suit your needs.

### Basic Settings and Chat Setting

Here, you can define the widget's name, description, and choose the widget UI language in **Basic Setting**. Scroll down to see the **Chat Setting**. Here you can define the agent's behavior during the chat.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/basic-settings.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/en/channels/webpage-widget/basic-settings.png" alt="Basic setting on SeaChat">
</a>

_Basic Setting for Style_

</center>
<br/>

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/chat-settings.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/en/channels/webpage-widget/chat-settings.png" alt="Chat setting on SeaChat">
</a>

_Chat Setting for Agent's Answers_

</center>
<br/>

Everytime you make a change you can see the change in the preview window by clicking on **Preview**. Once you are satisfied with the changes, click on **Save**.

> :warning: Attention
>
> Please note that the changes will not be saved until you click on the **Save** button. We recommend you to click on the **Preview** button to see the changes, and only after saving the changes can you click on **Test AI Agent**.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/preview-widget-chat.png" target="_blank">
<img height="100%" width="70%" style="border-radius: 5px" src="/images/seachat/en/channels/webpage-widget/preview-widget-chat.png" alt="Basic setting on SeaChat">
</a>

_Preview Window_

</center>
<br/>

### Card Settings

In addition to the fully customizable widget, you can also create cards to display information to your customers. Cards can be used to provide information to user when they first land on your website. You can also attach links to the cards to direct users to specific pages. To add more cards, click on the **Plus** button.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/card-setting.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/en/channels/webpage-widget/card-setting.png" alt="Chat setting on SeaChat">
</a>

_Design your Card_

</center>
<br/>

### Custom Forms: Pre-chat user information collection form

Sometimes you may want to collect information from your customers. You can create a custom form to collect information such as name, email, and phone number. This information can be used to provide personalized support to your customers. Depending on your use case, we can define new forms and reuse old ones.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/custom-forms.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/en/channels/webpage-widget/custom-forms.png" alt="Custom form setting on SeaChat">
</a>

_Choose or Create Customer Forms_

</center>
<br/>

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/custom-forms2.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/en/channels/webpage-widget/custom-forms2.png" alt="Custom form setting on SeaChat">
</a>

_Choose Before Chats Start_

</center>
<br/>

To edit a form, click on the **Edit** button after click on the **&#8942;**. You can also delete a form by clicking on the **Delete** button.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/access-edit-forms.png" target="_blank">
<img height="100%" width="60%" src="/images/seachat/en/channels/webpage-widget/access-edit-forms.png" alt="Custom form setting on SeaChat">
</a>

_Choose or Create Customer Forms_

</center>
<br/>

### Custom Forms: CSAT Survey Form

You can now collect customer feedback effortlessly with CSAT Survey Form — just like how you set up a User Information Collection Form! When a visitor tries to close the WebChat Widget, the form will automatically pop up, allowing the visitor to leave a star rating and optionally write a comment.

To set up:

1. Click the Add New Form button and choose the Customer Satisfaction Survey card.
   <br/>

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/custom-forms2.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/en/channels/webpage-widget/custom-forms2.png" alt="Custom form setting on SeaChat">
</a>

_Choose Customer Satisfaction Survey_

</center>
<br/>

2. Configure the Survey

- Turn on the Enable switch.
- Customize fields based on your needs including: form name, survey title, survey description, and choose to enable or disable comment box (for written feedback). If enabled, you can also customize the placeholder Text in the comment box. Click Save when you're done.

3. Follow the following [Installation](/en/seachat/manual/channels/webpage/#installation) step to install the updated widget code your website.

4. View the Survey Results

   Now, when visitors chat with your AI Agent and click the bottom-right icon to close the widget, the CSAT Survey Form will pop up. If the visitor submits feedback, you can go to SeaChat's Conversations page and view the star rating and comments by clicking the avatar of the conversation.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/csat-demo.gif" target="_blank">
<img height="100%" width="100%" src="/images/seachat/en/channels/webpage-widget/csat-demo.gif" alt="Custom form setting on SeaChat">
</a>

_Demonstration of how your website visitor can leave a feedback_

</center>
<br/>

<br/>

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/csat-form-result.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/en/channels/webpage-widget/csat-form-result.png" alt="Custom form setting on SeaChat">
</a>

_View Customer Satisfaction Survey Result_

</center>

<br/>

## Installation

Now that you have customized your widget, you can install it on your website. Simply copy the provided code snippet from **Install Widget** and paste it into your website's HTML code. That is, the end of your current `<body>{...}</body>` tag.

The widget will be displayed on your website, allowing you to provide real-time support to your customers.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/channels/webpage-widget/installation-code.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/en/channels/webpage-widget/installation-code.png" alt="SeaChat interface that guides the user to install the webpage widget">
</a>

*Follow the Installation Procedure*
</center>
<br/>

## Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).


---


#### Google Calendar

<!-- Source: seachat-manual/05-integrations/01-seachat-google-calendar-integration.md -->

<!-- Weight: 600 -->

*Integrate SeaChat AI agents with Google Calendar for appointment booking. Manage your meetings via chat or voice.*


## Overview
> After logging into SeaChat, navigate to **Agent Configuration** -> **Integrations** -> **Google Calendar** to add the integration.

## Google Calendar Integration

<br/>
<center>
  <a href="/images/seachat-integrations/google-calendar/en/google-calendar-ui.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/google-calendar/en/google-calendar-ui.png" alt="SeaChat | Google Calendar | Google Calendar UI">
</a>

*Google Calendar Integration Interface*
</center>

With the Google Calendar integration, your SeaChat agent can book appointments for you through chat or voice interactions. The process is simple and involves just two steps. Follow the on-screen instructions to integrate SeaChat with your Google Calendar.

First, authorize SeaChat to connect to your Google Calendar. Next, set up your working hours so the SeaChat agent knows when to schedule appointments.

## Meeting Invitation

Once the integration is complete, your SeaChat agent will be able to book appointments on your behalf. The agent will send a meeting invitation to the user and automatically add the event to your Google Calendar. The customer will receive the meeting invitation directly from the agent.

However, the format of the meeting invitation varies depending on the type of agent used:

- **For Voice Agent**: An SMS containing the calendar link will be sent to the customer's phone number. Please note that since the invitation is not sent via email, the customer may forget about the meeting. It’s advisable to follow up with a call to remind them.

- **For Chat Agent**: Ensure that email collection is enabled in SeaChat by navigating to **Channels** → **Webchat Widget** → **Custom Forms**. Either add a new form or edit the existing one, making sure the **Email** field is both **Required** and **Enabled**. If a meeting is booked, a calendar invitation will be sent to the collected email address.

### Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 
 

---


#### Shopify

<!-- Source: seachat-manual/05-integrations/02-seachat-shopify-integration.md -->

<!-- Weight: 601 -->

*Integrate SeaChat AI into your Shopify store to boost customer engagement with personalized AI-driven interactions.*



This page details the process for embedding the SeaChat AI agent into your Shopify storefront.

## Step 1: Create a SeaChat account
If you do not have a SeaChat account, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! Then you can build your AI agent and bring it to your Shopify websites.

## Step 2: Open Shopify
Go to your Shopify dashboard and click on Online Store from the menu. 

<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step1.png" alt="Go to your Shopify dashboard and click on Online Store from the menu.">


## Step 3: Edit code on Shopify
Start editing by clicking the ellipsis icon next to your current theme and choosing Edit code.


<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step2.png" alt="Start editing by clicking the ellipsis icon next to your current theme and choosing Edit code.">

## Step 4: Click on theme.liquid
Click on “theme.liquid” on the left side panel.


<img width="40%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step3.png" alt="Click on “theme.liquid” on the left side panel.">


## Step 5: Copy SeaChat Code
You will have to be logged in on SeaChat to view this code snippet. Sign up for free at [SeaChat](https://chat.seasalt.ai/). Access the required code snippet by navigating to Agent Configuration -> Channels within your workspace at the SeaChat dashboard, specifically under the Shopify channel.

Paste the SeaChat code snippet from the Shopify integration setup on Seachat into the &lt;head&gt; section. You can paste it anywhere between the opening &lt;head&gt; tag and the closing &lt;/head&gt; tag.


<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step4.png" alt="Paste the SeaChat code snippet in the head; section. You can paste it anywhere between the opening head tag and the closing /head tag">


## Step 6: Save and preview
Click “Save” button on top right. Click “Preview Store” to test the AI agent. Remember to launch the store again when you are ready!

**Important Note**: if you want to configure the style of your widget, please go to “Channels” -> “WebChat Widget” -> “Basic Setting”. Your AI Agent will share the same style across your webchat widget channels.

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/shopify/20240228-shopify_integration_step5.png" alt="Click “Save” button on top right. Click “Preview Store” to test the AI agent. Remember to launch the store again when you are ready!">


## Step 7: (Optional) Disconnect other chatbot
Please disconnect any other chatbot services, like Shopify Inbox, to prevent confusion. For Shopify app users, disable the "Apps embeds" toggle on your website customization page. If your previous chatbot service is embedded in code, remove it carefully. 


### Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 
 

---


#### Squarespace

<!-- Source: seachat-manual/05-integrations/03-seachat-squarespace-integration.md -->

<!-- Weight: 602 -->

*Embed SeaChat AI on your Squarespace site. Sign up, configure your agent, and enhance user experience.*


This page details the process for embedding the SeaChat AI agent into your Squarespace website.

## Step 1: Create a SeaChat account
If you do not have a SeaChat account, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! Then you can build your AI agent and bring it to your Squarespace websites.


## Step 2: Open Squarespace
Go to your Squarespace dashboard for the website of interest. Select the “Website” on the sidebar menu. 


<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step1.png" alt="Go to your Squarespace dashboard and click on Website from the menu.">


## Step 3: Open Website Tools
Next, select “Website Tools” in the sidebar menu.


<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step2.png" alt="Click on Website Tools on Squarespace">


## Step 4: Open Code Injection
Select “Code Injection” in the sidebar menu.


<img width="30%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step3.png" alt="Select Code Injection in the sidebar menu.">


## Step 5: Copy SeaChat Code
You will have to be logged in on SeaChat to view this code snippet. Sign up for free at [SeaChat](https://chat.seasalt.ai/). Access the required code snippet by navigating to Agent Configuration -> Channels within your workspace at the SeaChat dashboard, specifically under the Squarespace channel.

Paste the SeaChat code snippet from the Squarespace integration setup on Seachat into the HEADER text box. Remember to click “SAVE”.

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step4.png" alt="Paste the SeaChat code snippet in the HEADER text box. Remember to click SAVE.">

## Step 6: Save and preview
Use “Preview” function on Squarespace to test the AI agent. Remember to launch the website again when you are ready!

**Important Note**: if you want to configure the style of your widget, please go to “Channels” -> “WebChat Widget” -> “Basic Setting”. Your AI Agent will share the same style across your webchat widget channels.

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/squarespace/20240228-squarespace-integration-step5.png" alt="Preview SeaChat agent on website">


## Step 7: (Optional) Disconnect other chatbot
Please disconnect any other chatbot services to prevent confusion. If your previous chatbot service is embedded in code, remove it carefully from the “Code Injection” section. 

### Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 

---


#### Wix

<!-- Source: seachat-manual/05-integrations/04-seachat-wix-integration.md -->

<!-- Weight: 603 -->

*Integrate SeaChat AI into your Wix site with our simple guide. Customize the chat widget to boost engagement.*


This page details the process for embedding the SeaChat AI agent into your Wix website.

## Step 1: Create a SeaChat account
If you do not have a SeaChat account, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! Then you can build your AI agent and bring it to your Wix websites.


## Step 2: Open Wix and "Design Site"
Go to your Wix dashboard for the website of interest. Select the Design Site on the top right menu. 


<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step1.png" alt="Go to your Wix dashboard and click on Design Site from top right menu.">


## Step 3: Open "Add Elements"
Next, select “Add Elements" in the sidebar menu.


<img width="50%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step2.png" alt="Click on Add Elements on Wix">


## Step 4: Open "Embed Code" -> "Embed HTML"
Select “Embed Code” -> "Embed HTML" in the menu.


<img width="50%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step3.png" alt="Select Embed Code and then Embed HTML.">


## Step 5: Copy SeaChat Code
You will have to be logged in on SeaChat to view this code snippet. Sign up for free at [SeaChat](https://chat.seasalt.ai/). Access the required code snippet by navigating to Agent Configuration -> Channels within your workspace at the SeaChat dashboard, specifically under the Wix channel.

Paste the SeaChat code snippet from the Wix integration setup on Seachat into the code box. Remember to click “Update”.

<img width="90%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step4.png" alt="Paste the SeaChat code snippet in the HEADER text box. Remember to click SAVE.">

## Step 6: Adjust Chat Widget Box Size
Use the sizing tool to adjust the chat widget to big enough size. In the example, I adjusted the size to be `W: 700, H:600`. After you adjust the widget size, drag the widget to the desired location, usually in the lower right hand corner.

<img width="80%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step5.png" alt="Adjust chat widget size">

## Step 7: Anchor SeaChat Widget Position

Ensure the SeaChat widget is anchored in place (lower right hand corder) to avoid movement during page scrolling. 

Select the widget. Right-click. Select "Pin to Screen". Then this widget component will be anchored on the corner and floating. 

<img width="60%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-pin-to-screen.png" alt="Adjust chat widget size">

You can adjust the margin/offset. We recommend 20 for both vertial and horizontal settings.

<img width="60%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-offset-margin.png" alt="Adjust chat widget size">


## Step 8: Save and preview
Use “Preview” function on Wix to test the AI agent. Remember to launch the website again when you are ready!

**Important Note**: if you want to configure the style of your widget, please go to “Channels” -> “WebChat Widget” -> “Basic Setting”. Your AI Agent will share the same style across your webchat widget channels.

<img width="60%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wix/wix-seachat-integration-step6.png" alt="Preview SeaChat agent on website">


## Step 9: (Optional) Disconnect other chatbot
Please disconnect any other chatbot services to prevent confusion. If your previous chatbot service is embedded in code, remove it carefully from the “Code Injection” section. 

### Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 

---


#### MailerLite

<!-- Source: seachat-manual/05-integrations/05-seachat-mailerlite-integration.md -->

<!-- Weight: 604 -->

*Integrate SeaChat with MailerLite to automatically add customer emails from forms to your lists. Learn how to generate an API token for email marketing.*


This page details the process for setting up MailerLite integration with SeaChat. After setting up this integration, you can use SeaChat forms to collect customer emails and information, and add them to your email lists on [MailerLite](https://www.mailerlite.com/) automatically.

For a visual guide on how to integrate SeaChat with MailerLite, you can watch the tutorial video below:
<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/xTnJ9L1sVC4?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## Step 1: Create a SeaChat account
If you do not have a SeaChat account, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! Then you can build your AI agent and integrate with MailerLite.


## Step 2: Open "Integrations"
Go to your MailerLite dashboard and click on "Integrations" from left panel.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 50%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/add-mailerlite-integrations.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/add-mailerlite-integrations.png" alt="Go to your Mailerlite dashboard and click on Design Site from top right menu.">
</a>
</div>
</div>


## Step 3: Select "API"
Select "API" by clicking on "Use".


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/select-mailerlite-api.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/select-mailerlite-api.png" alt="Select API on MailerLite">
</a>
    <p style="margin-top: 20px; font-size: 15px">Generate new token on MailerLite
</div>
</div>



## Step 4: Generate new token
Click on "Generate new token". Give this API key a self-explanatory name and accept the API token requirements. Click on "Create token".

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/generate-new-token-mailerlite.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/generate-new-token-mailerlite.png" alt="Generate new token on MailerLite">
</a>
    <p style="margin-top: 20px; font-size: 15px">Generate new token on MailerLite
</div>
</div>

<br>

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 60%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/give-api-token-name-mailerlite.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/give-api-token-name-mailerlite.png" alt="Give the new token a name on MailerLite">
</a>
    <p style="margin-top: 20px; font-size: 15px">Give the new token a name on MailerLite
</div>
</div>

## Step 5: Copy API key
Save a copy of your API key. Then, go back to SeaChat integration page for MailerLite to finish integration.


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/copy-and-save-mailerlite-api-key.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/copy-and-save-mailerlite-api-key.png" alt="Copy and save MailerLite API key">
</a>
    <p style="margin-top: 20px; font-size: 15px">Copy and save MailerLite API key
</div>
</div>



## Step 6: (Optional) Find your Group IDs
If you want to add contacts to specific MailerLite Group. You can find all the Group IDs under your account at the bottom of “Developer API” page. Hint: you can add a contact to multiple groups.

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
  <a href="/images/seachat-integrations/mailerlite/get-mailerlite-group-id.png" style="height: 200px; width: 100%; height: 100%;display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
<img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/mailerlite/get-mailerlite-group-id.png" alt="Get MailerLite group ID">
</a>
    <p style="margin-top: 20px; font-size: 15px">Get MailerLite group ID
</div>
</div>


### Support
Need assistance? Contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).

 

---


#### Wordpress

<!-- Source: seachat-manual/05-integrations/06-seachat-wordpress-integration.md -->

<!-- Weight: 605 -->

*Embed SeaChat AI agents into Wordpress website. Follow our guide to start chatting with your website visitors.*


This page details the process for embedding the SeaChat AI agent into your Wordpress website.

## Step 1: Create a SeaChat account

If you do not have a SeaChat account, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! Then you can build your AI agent and bring it to your Wordpress websites.

## Step 2: Open Wordpress and "Appearance"

Go to your Wordpress dashboard for the website of interest. Click on Appearance on the left-hand side menu.

<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wordpress/wordpress-seachat-en-dashboard.png" alt="Go to your Wordpress dashboard and click on Appearance from left menu.">

## Step 3: Copy SeaChat Code

You will have to be logged in on SeaChat to view this code snippet. Access the required code snippet by navigating to Agent Configuration -> Channels within your workspace at the SeaChat dashboard, specifically under the Wordpress channel. Copy the code snippet.

## Step 4: Open "Theme File Editor" and Add SeaChat Code Snippet

Select "Theme File Editor" on the left-hand side menu -> "Theme Footer" on the right-hand side menu. Then, paste the SeaChat code snippet in between `<body>` and `</body>`. Finally, click on `Update File` to save your change.

<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wordpress/wordpress-seachat-add-widget-code.png" alt="Select Theme File Editor to install SeaChat widget.">

## Step 5: Save and preview

Review your website now! If you go to your website now, you can see the SeaChat widget in the lower right corner.

**Important Note**: if you want to configure the style of your widget, please go to “Channels” -> “WebChat Widget” -> “Basic Setting”. Your AI Agent will share the same style across your webchat widget channels.

## Debug Tip: SeaChat Widget Not Loading?

If you are using WordPress optimization plugins that eliminate render-blocking CSS, please be aware that this may cause the SeaChat webchat widget to not load properly on your website.

#### **🔍 Why Does This Happen?**

Some optimization plugins attempt to defer or remove critical CSS, which may interfere with how the SeaChat widget is rendered. This can result in:

- The widget is not appearing on your site.
- Unexpected UI issues affecting the chat widget.

#### **🛠️ How to Fix It?**

If you have a performance plugin enabled, follow these steps:

1. Check your plugin settings for “Eliminate Render-Blocking CSS” or “Optimize CSS Delivery.”
2. Disable this specific optimization to prevent it from affecting the chat widget.
3. Clear your cache and reload your site to ensure the chat widget works correctly.

#### **Example: WP Rocket**

We take _WP Rocket_, a widely used web performance plugin as an example. In the **FILE Optimization** tab, we should not check the **Optimize CSS delivery** box to ensure smooth loading of SeaChat webchat.

<center>
<a href="/images/seachat-integrations/wordpress/wordpress-seachat-wp_rocket.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/wordpress/wordpress-seachat-wp_rocket.png" alt="WP Rocket Settings">
</a>
</center>

<br/>

If you need further assistance, feel free to reach out to [seachat@seasalt.ai](mailto:seachat@seasalt.ai)! 🚀


---


#### SeaX Integration with SMS & Call

<!-- Source: seachat-manual/05-integrations/07-seax-integration-sms-calll-in-seachat.md -->

<!-- Weight: 606 -->

*Integrate SeaX with SeaChat for bulk messaging and automated call handling. Automate customer communications with AI.*


## Overview

In this tutorial, we will guide you through setting up Seasalt's bulk-messaging platform, SeaX, in SeaChat. SeaX is a powerful omni-channel platform that enables you to manage all your business channels from a single interface.

For more information, check out our [SeaX Documentation](https://wiki.seasalt.ai/seax/seax-messaging/bulk-messaging-features/).

With SeaX integrated into SeaChat, you can not only manually manage customer conversations but also automate responses with your SeaChat AI agent. SeaX consolidates all your business channels, such as WhatsApp, phone calls, and SMS, allowing these channels to be directed to SeaChat for AI-driven responses.

## SeaX Bulk Call/Send

SeaX provides a channel for your AI agents to communicate with customers. Once SeaX is integrated with SeaChat, you can start sending bulk messages to your customers via SeaX.

SeaChat and SeaX work seamlessly with each other to perform the bulk messaging. SeaX will start calling each customer on the given list about 1 second per call. Once the call is answered, the AI agent will take over the conversation, and all you have to do now is go to the **Conversations** dashboard to view the conversation.

SeaChat does not know the list of the customers you are calling, and neither is it capable of making calls. SeaChat only handles the conversation once conversation is initiated. On the other hand, SeaX is responsible for initiating the calls and sending the messages.

You can create **Campaigns** to send SMS messages or voice drops to your customers. These campaigns will be delivered through SeaX, and then handled by your personalized AI agent on SeaChat.

## Outbound Call Campaign

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/call-integration.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/call-integration.png" alt="Outbound/ Inbound Calls Integration">
    </a>
<br/>
    <p style="font-size: 15px">Outbound/Inbound Calls Integration</p>
</div>
</div>

Outbound calls is an effective way to reach out to your customers. With SeaX, you can automate these calls.

1. **Languages**: Choose the language and the model it is available in. We recommend using SeaVoice for its stability and reliability in production.

2. **Text-to-Speech Voice**: Select a preferred voice and click the play button next to the dropdown to hear it.

3. **Outbound Starting Messages**: This message will be played when the call is answered, with the AI agent handling the rest of the conversation. You can view the conversation in the **Conversations** dashboard.

## Inbound Calls Integration

Inbound calls offer a reliable solution for customer service. AI agents can answer calls and act as voice receptionists.

Follow the same steps as the [Outbound Calls Integration](#outbound-calls-integration) to set up language, voice, and greeting messages.

## SMS Integration

SMS is an effective tool for text marketing. Starting or receiving an SMS conversation is simple. Just set up the starting messages and let the AI agent take care of the rest.

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/sms.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/sms.png" alt="SMS Setup">
    </a>
<br/>
    <p style="font-size: 15px">SMS Setup</p>
</div>
</div>

## Test It Out

With SeaX set up in SeaChat, you can test the integration by sending a message to your SeaChat AI agent. Before sending bulk messages to your customers via SeaX, we recommend testing locally by using the designated buttons on each page.

Once you have completed the testing, you can begin sending bulk messages to your customers through SeaX and let your SeaChat agent continue the conversation.

<div style="display: flex; flex-direction: column; align-items: center; width:100%">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat-integrations/seax/find-seax.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/find-seax.png" alt="SeaX Messages in SeaChat">
    </a>
<br/>
    <p style="font-size: 15px">SeaX Messages in SeaChat</p>
</div>
</div>

## :dart: Troubleshooting

1. **No phone available for inbound calls and inbound SMS. How can I configure my phone correctly?**

<div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <a href="/images/seachat-integrations/seax/no-phone-available.png" style="height: 200px; width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" target="_blank">
        <img style="width: 100%; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat-integrations/seax/no-phone-available.png" alt="No Phone Available Warning">
    </a>
<br/>
    <p style="font-size: 15px;">No Phone Available Warning</p>
</div>
</div>

When the system displays the above warning, it means you need to provide a phone number to the AI agent so that the agent can use it as the channel to manage incoming calls and SMS messages. If someone calls this number or sends an SMS, the AI agent will handle the conversation.

To provide this number, you need to configure SeaX and send an outbound call or SMS to the SeaChat agent first. Please follow the [SeaX Documentation](https://wiki.seasalt.ai/seax/seax-messaging/bulk-messaging-features/) for instructions on how to send an SMS or make a call to the agent.

Specifically:

1. SeaX -> Outbound calls to agent -> Configure agent inbound call number
2. SeaX -> Outbound SMS to agent -> Configure agent inbound SMS number

If you are unsure whether the agent has received the call or SMS, you can check the conversation in the **Conversations** dashboard.


---


#### Bulk Outbound and Automatic Inbound Phone Calls with AI Agents

<!-- Source: seachat-manual/05-integrations/08-seax-integration-bulk-phone-calls.md -->

<!-- Weight: 607 -->

*Integrate SeaX with SeaChat for bulk phone calls, inbound and outbound. Automate customer communications with AI.*




## Overview

[SeaX](https://seax.seasalt.ai) empowers organizations to conduct large-scale outbound and inbound phone call campaigns using AI-powered agents. When integrated with SeaChat, SeaX enables both automated outbound calls—such as surveys or customer outreach—and seamless handling of inbound calls with 24/7 AI agent support. This integration is ideal for businesses seeking to automate voice interactions, improve customer engagement, and ensure that no call goes unanswered.

## 🎥 Video Tutorial

A comprehensive video tutorial demonstrates step-by-step how to set up and use SeaX with phone calls, including both outbound campaigns and inbound call handling by AI agents.

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/An4n8JhhdvA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

## Key Features

**Bulk Outbound Calling:**  
Initiate large-scale outbound phone call campaigns to hundreds or thousands of recipients directly from SeaX. Use AI agents to automate surveys, interviews, or notifications.

**AI-Powered Inbound Call Handling:**  
Configure AI agents to answer incoming phone calls, providing instant, consistent responses to customer inquiries at any time, day or night.

**Unified Management:**  
Manage outbound and inbound call campaigns, phone numbers, and AI agents from a single SeaX interface. Synchronize AI agents across SeaX and SeaChat for streamlined configuration.

**Real-Time Transcription and Summaries:**  
Automatically transcribe calls and generate summaries, making it easy to review interactions and extract key information.


## Prerequisites

- SeaX and SeaChat accounts.
- At least one phone number provisioned in SeaX (toll-free or local).
- Administrator privileges to configure integrations and AI agents.

## Step-by-Step Setup

### 1. Assign and Configure a Phone Number

- Log in to SeaX and navigate to **Workspace → Numbers**.
- Select or provision a phone number for outbound and/or inbound calls.
- Click **Edit** on the chosen number.
- Enable the option **AI Agent to answer the phone**.
- Assign an AI agent from your SeaChat workspace to handle inbound calls.

### 2. Synchronize AI Agents

- Ensure your SeaX and SeaChat workspaces are synchronized.
- All AI agents created in SeaChat will be available for assignment in SeaX, allowing for consistent agent behavior across channels.

### 3. Configure Inbound Call Handling

- In SeaChat, go to **Integrations** and select the phone call integration.
- Link the phone number to your chosen AI agent.
- Set preferences such as language, voice (e.g., "Jessica" for text-to-speech), and the greeting message for inbound calls.
- Save your configuration.

### 4. Test Inbound Calls

- Place a test call to your configured number.
- The AI agent should answer with your preset greeting and respond to queries according to its configuration.
- All call transcripts and summaries will be available in both SeaX and SeaChat for review.

### 5. Set Up Outbound Calling Campaigns

- In SeaX, navigate to **Bulk Send/Call** or **Campaigns**.
- Select your phone-enabled number.
- Import or select your contact list (ensure no duplicate contacts).
- Configure your AI agent’s outbound script or survey (e.g., interview questions for a recruitment campaign).
- Schedule or launch the outbound campaign. The AI agent will call each contact and conduct the conversation as configured.
- Monitor campaign progress and review call summaries and extracted responses in real time.

### 6. Manage Inbound Callbacks

- If recipients return missed calls, the same AI agent (or a different one, if configured) will answer and continue the conversation.
- All inbound and outbound call data, including transcripts and summaries, are accessible from both SeaX and SeaChat.

## Managing Multiple Phone Numbers

SeaX supports multiple phone numbers for different campaigns or departments. Assign different AI agents to each number as needed and manage all activity from the unified interface.

## Best Practices

**Avoid Duplicate Contacts:**  
Ensure each phone number appears only once in your contact lists to prevent multiple calls to the same recipient.

**Personalize Campaigns:**  
Tailor outbound call scripts to the campaign’s purpose (e.g., surveys, appointment reminders, customer notifications).

**Monitor and Review:**  
Use SeaX’s reporting tools to track call delivery, response rates, and campaign effectiveness. Review call transcripts and summaries for quality assurance.

**Maintain Compliance:**  
Adhere to telecommunication regulations regarding automated calls and ensure recipients have consented to receive calls where required.

## Troubleshooting

- If inbound calls are not answered by the AI, verify that the phone number is correctly linked to an AI agent in both SeaX and SeaChat.
- For outbound issues, check contact list formatting and ensure no duplicate entries.
- Confirm that your phone numbers are provisioned and active within SeaX.

## Support

For further assistance, contact Seasalt AI support at seachat@seasalt.ai.


---


#### SeaX Integration with WhatsApp

<!-- Source: seachat-manual/05-integrations/09-seax-integration-whatsapp-in-seachat.md -->

<!-- Weight: 608 -->

*Integrate SeaX with SeaChat for bulk WhatsApp messaging. Automate customer communications with AI.*


## Overview

[SeaX](https://seax.seasalt.ai) enables businesses to send bulk WhatsApp messages and manage large-scale customer engagement campaigns efficiently. When integrated with SeaChat, SeaX not only allows for outbound messaging at scale but also automates replies to incoming customer responses using AI. This integration streamlines both outbound campaigns and inbound support, making it ideal for organizations handling high message volumes or seeking to automate customer interactions.

## 🎥 Video Tutorial
  <iframe width="100%" height="400" src="https://www.youtube.com/embed/WUwn2QoeBGA?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## Key Features

- **Bulk WhatsApp Messaging:** Send broadcast messages to large lists of WhatsApp contacts directly from SeaX.
- **AI-Powered Auto-Reply:** Seamlessly hand over inbound replies to SeaChat, which can automatically respond using advanced language models.
- **Human Agent Takeover:** Switch between AI and human agents at any time for personalized support.
- **Unified Management:** Oversee multiple WhatsApp business accounts and campaigns from a single SeaX interface.
- **Compliance:** Ensure all recipients have opted in to receive WhatsApp messages, in accordance with WhatsApp policies.

---

## Prerequisites

- A WhatsApp Business account with API access.
- SeaX and SeaChat accounts.
- Administrator privileges on Meta Business Suite for WhatsApp integration.

---

## Step-by-Step Setup

### 1. Connect WhatsApp to SeaX

1. Navigate to **Channels** under **Workspace** in SeaX.
2. Select **WhatsApp Business Platform** and follow the on-screen instructions to connect your WhatsApp Business account using Meta Business Suite credentials.
3. Once connected, your WhatsApp account will appear in the SeaX workspace channels.

### 2. Configure Bulk Messaging

1. Go to the **Conversations** or **Bulk Send/Call** section in SeaX.
2. Select your WhatsApp-enabled number and compose your bulk message.
3. Import or select your contact list. Ensure all recipients have opted in to receive messages.
4. Send or schedule your broadcast. SeaX will deliver messages to all selected contacts.

### 3. Integrate SeaChat for Auto-Reply

1. In SeaChat, navigate to **Agent Configuration → Integrations**.
2. Enable the WhatsApp integration and link it to your SeaX account.
3. Assign the WhatsApp number used for bulk messaging to the SeaChat AI agent.
4. In SeaX, edit the WhatsApp number settings and enable "AI Agent to answer WhatsApp".
5. Save your settings.

### 4. Test the Integration

- Send a test WhatsApp message to your business number.
- Verify that incoming replies are automatically handled by SeaChat’s AI agent.
- Human agents can take over any conversation at any time by joining the chat or using the "takeover" button.

---

## Managing Multiple WhatsApp Accounts

SeaX supports the management of multiple WhatsApp business accounts. Add new accounts via **Channels → Add Account** and manage all numbers and agents centrally. Assign different agents to different accounts as needed, and monitor all activity from the unified interface.

---

## Human Agent Takeover

If a customer’s query requires human intervention, agents can take over from the AI at any time. This can be triggered manually or by customer request (e.g., using a command like `/live_agent`). The transition is seamless, and customers cannot distinguish whether they are chatting with an AI or a human unless informed.

---

## Best Practices

- **Obtain Consent:** Only send bulk messages to users who have opted in to receive WhatsApp communications from your business.
- **Personalize Messages:** Use variables and templates to tailor bulk messages for higher engagement.
- **Monitor Campaigns:** Use SeaX’s reporting tools to track delivery, response rates, and campaign effectiveness.
- **Maintain Compliance:** Adhere to WhatsApp’s business messaging policies to avoid account restrictions.

---

## Troubleshooting

- Ensure you are using a permanent access token for WhatsApp API integration.
- Verify that your WhatsApp application is set to Live mode.
- Confirm webhook permissions are correctly configured for message delivery and reception.
- If auto-replies are not functioning, check that the WhatsApp number is correctly linked to both SeaX and SeaChat.

---

## Support

For further assistance, contact Seasalt AI support at seachat@seasalt.ai.

---


#### Programmatically Pre-Fill Contact Forms in WebChat

<!-- Source: seachat-manual/05-integrations/10-seachat-prefill-contact-forms.md -->

<!-- Weight: 609 -->

*SeaChat supports pre-filling user information in the webchat form by detecting query strings in the webchat URL. This allows seamless integration between your website and the chat widget, so your customers don’t need to enter their details manually. *


SeaChat supports pre-filling user information in the webchat form by detecting query strings in the webchat URL. This allows seamless integration between your website and the chat widget, so your customers don’t need to enter their details manually.

<center>
<a href="/images/seachat-integrations/widget/demo1.gif">
<img height="800px" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/demo1.gif" alt="Demo GIF of prefilling">
</a>
</center>

<br/>

Why is this important? This is mostly used in scenarios where your end users have already logged into your system, then you can use their login info to auto fill in the contact form. In this case:

1. Users save time by not manually filling the contact form once again.
2. You prevent users from inputting wrong or fake information in the contact form.

### **Use Cases**

The ability to pre-fill user details in the webchat form is particularly useful in the following scenarios:

1. Customer Support & Helpdesk  
   When users initiate a chat from a customer support portal, their details (name, email, phone) can be auto-filled to save time.
2. Logged-In Users on Websites & Apps  
   If users are already logged in, their details can be automatically injected into the webchat form.

3. E-Commerce & Sales Inquiry Forms  
   If a customer is browsing a product and needs support, their account details can be passed into the chat.

4. Booking & Reservation Systems  
   In online booking or appointment scheduling, AI agents can pre-fill customer information to confirm their details faster.

5. Lead Capture & Marketing Campaigns  
   When running email campaigns or ads, a pre-filled chat form ensures that potential leads don't have to re-enter information when engaging with the AI agent.

---

### How It Works

#### Step 1: Add a contact form to display in WebChat

1. Login to SeaChat and go to **Channels** tab.
2. Click the **Webchat Widget** card
3. On top right, go to the **Custom Forms** tab
4. Click **\+ Add New Form**
5. Enable the form by turning of the switch on top of the page
6. If you allow users to skip the form, **Allow users to skip the form** too
7. Edit the form if you would like customize
8. When finish editing, click **Save**

<center>
<a href="/images/seachat-integrations/widget/webchat form configuration.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/webchat form configuration.png" alt="webchat form configuration">
</a>
</center>

<br/>

#### Step 2: Retrieve Your Webchat Widget Code

1. Log in to **SeaChat** and navigate to the **Channels** tab.
2. Click the **Make your webchat widget support omni-channel** button.
3. Copy the **widget code** and integrate it to your website.

<center>
<a href="/images/seachat-integrations/widget/widget code page.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/widget code page.png" alt="widget code page">
</a>
</center>

<br/>

#### Step 3: Append Query Parameters to Webchat URL

You will find your webchat URL in this format in your widget code:

`https://chat.seasalt.ai/chat/uuid`

To pre-fill user details such as name, email, and phone number, you should append query parameters to all webchat URLs in your widget code.

<center>
<a href="/images/seachat-integrations/widget/widge code highlight url.png">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/widge code highlight url.png" alt="widge code highlight url">
</a>
</center>

<br/>

##### Field Format:

| User Information | Query Parameter |
| :--------------- | :-------------- |
| **Email**        | `_EMAIL`        |
| **Name**         | `_NAME`         |
| **Phone**        | `_PHONE`        |

##### Example: Pre-fill webchat form with user’s name, email and phone number

Your original webchat URL is:

```
https://chat.seasalt.ai/chat/uuid
```

You should modify your webchat URL as the follows:

```
https://chat.seasalt.ai/chat/uuid?_NAME=JohnDoe&_EMAIL=johndoe@example.com&_PHONE=123456
```

When the webchat loads with the modified URL, the form will be automatically populated with the provided user details:

- **Name:** John Doe
- **Email:** [johndoe@example.com](mailto:johndoe@example.com)
- **Phone:** 123456
<center>
<a href="/images/seachat-integrations/widget/demo1.gif">
<img height="800px" style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/demo1.gif" alt="Demo GIF of prefilling">
</a>
</center>

<br/>

### Adding Custom Fields

SeaChat also supports pre-filling custom fields in the webchat form.

#### How to Add Custom Fields to webchat form:

1. Log in to **SeaChat** and navigate to the **Channels** tab.
2. Go to the **Webchat Widget** card.
3. Navigate to the **Custom Forms** tab and edit your form.
4. Click **\+Add** to add a new custom field.
   - When you add the first custom field, it will use `VAR_0001`.
   - If you add more fields, they will use `VAR_0002`, `VAR_0003`, and so on.

##### Custom Field Format:

| User Information        | Query Parameter |
| :---------------------- | :-------------- |
| **Custom Field Name 1** | `VAR_0001`      |
| **Custom Field Name 2** | `VAR_0002`      |

##### Example: Pre-fill webchat form with user’s name and account ID

If you want to pre-fill an **Account ID** (identified using `VAR_0001`) field in your webchat form, your updated webchat URL will look like this:

```
https://chat.seasalt.ai/chat/uuid?_NAME=JohnDoe&_EMAIL=johndoe@example.com&_PHONE=123456&VAR_0001=9876
```

When the webchat loads, the form will be auto-filled with:

- **Name:** John Doe
- **Email:** [johndoe@example.com](mailto:johndoe@example.com)
- **Phone:** 123456
- **Account ID:** 9876

<center>
<a href="/images/seachat-integrations/widget/demo2.gif">
<img height="800px"style="border-radius: 0.4rem" src="/images/seachat-integrations/widget/demo2.gif" alt="Demo GIF of prefilling">
</a>
</center>

<br/>

## **Summary**

- Retrieve and integrate the **webchat widget code** from SeaChat.
- Modify the **webchat URL** with `_NAME`, `_EMAIL`, and `_PHONE` parameters.
- Add **custom fields** using `VAR_0001`, `VAR_0002`, etc.
- When users open the webchat, the form is **pre-filled automatically**.

🚀 **That’s it\! Your webchat is now set up to accept user details programmatically.**


---


#### Workspace Management

<!-- Source: seachat-manual/06-workspace/01-workspace-management.md -->

<!-- Weight: 700 -->

*Manage SeaChat workspace, agents, and members. Optimize your workspace for efficient operations.*


Workspace is the control center of all your agents and members. Let's first navigate to the section under **Workspace** to find all the features that we will cover in this article. 

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div height="10%" style="width: 50%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/workspace-sidebar.png" target="_blank">
    <img height="10%" width="50%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/workspace-sidebar.png" alt="SeaChat | Workspace | Sidebar Navigation">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Workspace in Sidebar Menu</p>
</div>

## Agents

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/agents.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/agents.png" alt="SeaChat | Workspace | Agents">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Agent Management</p>
</div>

This is where you can manage all your AI agents. Each row represents an agent and its name, email, and status. You can also see the number of unread messages. Find the URL to the agent conversation, launch the conversation directly, or add new agents here.

## Members

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/members.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/members.png" alt="SeaChat | Workspace | Members">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Members Management</p>
</div>

There are different types of members. Depending on the type of membership, members will have different access and permissions. If you are the owner of a workspace, you can add new members to your workspace and assign different roles to them. Here are some of the roles you can assign to a member:

1. **Admin**: Admins have full access to the workspace and can manage all the settings. They can edit the AI agents' settings, manage the knowledge base, access the agent conversation, and take over conversations as human agents.
2. **AI Agent Editor**: AI Agent Editors can edit the AI agents' settings, manage the knowledge base, and access the agent conversation and testing.
3. **Human Agent**: Human Agents can access the agent conversation and take over conversations as human agents.

### Membership Assignment

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/add-member.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/add-member.png" alt="SeaChat | Workspace | Add Member">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Member Settings</p>
</div>

You can assign different agents to different members. For instance, a good practice is assigning the testing agents to your AI agent editors and agents in production to your human agents. Admins can access both types of agents for monitoring and control.

> **🤖 Agents vs. 👨 Members**
> 
> We use the word “agent” and “bot” interchangeably in this document. As you can see, most URL parameters use “bot” while the writeup most of the time uses “agent”. 
> 
> Seasalt.ai is adding more reasoning and execution functionalities to the normal “chatbot”, thus why we prefer to use the word “agent” rather than “bot”, meaning that an agent can execute things than a bot.
> 
> However, “agent” can be confused with a human in the context of “live agent” or “human agent”. In these situations we’ll use “AI agent” to refer to autonomous agents and “live agent” to refer to a live human.
> 
> On the other hand, members can only mean real human members.


[//]: # (## Workspace Preferences)

[//]: # ()
[//]: # (<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">)

[//]: # (<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">)

[//]: # (    <a href="/images/s``eachat/en/workspace/01-workspace-management/preference.png" target="_blank">)

[//]: # (    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/preference.png" alt="">)

[//]: # (    </a>)

[//]: # (</div>)

[//]: # (    <p style="margin-top: 20px; font-size: 15px">Preference Settings</p>)

[//]: # (</div>)

[//]: # ()
[//]: # (Here is where you can manage the notification settings of your workspace. SeaChat can automatically send you emails to notify you about new conversations and new live agent requests. After enabling the types of notifications you want to receive, you can also set the language of the notifications.)

### Notification Settings

SeaChat provides notifications in different languages. You can choose the language you want to receive the notifications in. Although you can set the language to default (same as the appearance language), we recommend setting it to the language you use in conversations. This helps optimize the performance of the agent and speeds up operations.

## Workspace API Keys

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/workspace-api.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/workspace-api.png" alt="SeaChat | Workspace | API">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">SeaChat Workspace API</p>
</div>

If you wish to access your workspaces or agents programmatically, you can use the API key found under your **Workspace**. You can generate new API keys, view the existing ones, and delete them here. Please make sure to set up the following two prerequisites before using the API key:

1. **Workspace Creation**: If you haven't already, create a workspace in SeaChat and note down the workspace ID from the URL, which follows the format: `https://chat.seasalt.ai/gpt/workspace/{workspace-id}/bot/{bot-id}/`.
2. **Access Credentials**: Obtain your Client ID and Access Token by reaching out to seachat@seasalt.ai. These credentials are essential for authenticating your API requests. This is where you can apply the access token in the **API Keys** section of your workspace settings.

SeaChat API uses Bearer Authentication methods. Therefore, you must apply your bearer token in the header of your API requests. For example, if you are using curl, you can use the following code snippet to authenticate your API requests:

```curl
curl -X 'POST' \
  'https://chat.seasalt.ai/api/v1/public/bots' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer [access token]' \
  -H 'Content-Type: application/json' \
  -d '{
    "workspace_id": "XXXXX-XXX-XXXXXXXXX",
    "name": "SeaChat",
    "description": "string",
    "use_case": "Customer Service",
    "live_agent_transfer": false,
    "default_response_language": "default",
    "is_enabled": true
  }'
```

SeaChat API is an in-depth tool that allows you to access your workspace and agents programmatically. You can use the API to create new AI agents, manage existing agents, and access the conversation history. For more information on the SeaChat API, please refer to the [API documentation](https://chat.seasalt.ai/redoc). Or contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai)


##  Multiple Workspaces

The concept of workspace is meant to represent a team of AI agents and members. Under a workspace, you can have multiple AI agents and members. If you are part of multiple workspaces, you can switch between them by clicking on the workspace name in the top left corner of the screen or simply go to **Workspace Dashboard** to manage them.

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/access-workspace-dashboard.png" target="_blank">
    <img width="60%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/access-workspace-dashboard.png" alt="SeaChat | Workspace | Dashboard">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Navigate to Workspace</p>
</div>

Once you are in the workspace dashboard, you can access all your workspaces. If you wish to create a new workspace, you can do so by clicking on the **Create** button. 

<div id="additional-setting-ui" style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center">
    <a href="/images/seachat/en/workspace/01-workspace-management/create-workspace.png" target="_blank">
    <img width="100%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/workspace/01-workspace-management/create-workspace.png" alt="SeaChat | Workspace | Create Workspace">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">Creating a New Workspace</p>
</div>


You can build multiple AI agents in a workspace, each with different use cases, languages, and agent descriptions. These AI agents can then serve different clients in different channels or integrations under a single workspaces. A practical example to utilize the multiple workspace feature is in testing and development of new agents. You might want to create a separate workspace for testing and development, and another for production. This way, you can test new agents without affecting the production environment.

## Workspace Limits

Different plans have different limits on the number of workspaces you can create. If you have reached the limit, you can upgrade your plan to create more workspaces. If you have any questions about the pricing, please refer to [Pricing and Plans](https://wiki.seasalt.ai/seachat/seachat-payments/pricing-plans/).

Here are the numbers of workspaces you can create based on the plan you are subscribed to:

- **Free** - 1 workspace
- **Standard** -  1 workspace
- **Premium** -  2 workspaces
- **Enterprise** -  multiple workspaces


---


#### Test and Improve AI Agent

<!-- Source: seachat-manual/07-test-and-improve-ai-agent/improve-agent.md -->

<!-- Weight: 800 -->

*Learn to test and enhance your AI agent on SeaChat with video tutorial and practical tips for customer interactions.*


  <iframe width="100%" height="400" src="https://www.youtube.com/embed/kKN9t4F3j_8?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

---


#### SOP for After Launch Operations

<!-- Source: seachat-manual/07-test-and-improve-ai-agent/post-launch-sop.md -->

<!-- Weight: 801 -->

*After launching SeaChat, follow this SOP guide to optimize daily operations and improve team workflows for productivity.*


Congratulations on successfully launching SeaChat to your selected channels – website, WhatsApp, or others. We are only half way there. This guide walks you through the remaining steps to ensure a successful operation on a daily basis.

## Setup

### 1. Add More Members to your Workspace

<br/>

<center>
<a href="/images/seachat/en/post-launch-sop/add-members.png">
<img height="100%" width="40%" src="/images/seachat/en/post-launch-sop/add-members.png"  alt="Add more members through workspace and member management section on SeaChat.">
</a>

*Workspace → Members*

</center>

If you haven’t done so already, you can go to *Workspace* → *Members* to add your team there.

Note that there are [three roles](https://wiki.seasalt.ai/en/seachat/workspace/workspace-management/#members): Admin, AI Agent Editor, and Human Agents.

Human Agents won’t be able to see how you’ve configured your AI agent, they are just there to reply to incoming messages.

Your AI Agent Editor can modify your AI Agent. So be very careful with assigning such roles.

If you have **multiple AI Agents**, you can assign different human agents to different AI agents.

### 2. Enable Email Notification

You should ask each of your agents to enable email notifications at *Workspace* → *Preference*.

<center>
<a href="/images/seachat/en/post-launch-sop/enable-email-notification.png">
<img height="100%" width="80%" src="/images/seachat/en/post-launch-sop/enable-email-notification.png"  alt="Enable email notification on SeaChat platform to keep track with chat conversation.">
</a>

*Enable Email Notification on SeaChat*

</center>

In this way you’ll be notified as soon as someone starts chatting with your AI agent. Then you can choose whether to chime in.

### 3. Consider Enabling Form on Web Widget

If you use a webchat widget, visitors might not leave their phone number, name, or email. You won’t know whom you are chatting with. In this case, you can go to *Channels* → *Webchat Widget* → *Custom Forms* to force visitors to fill in their contact details before chatting:

<div style="display: flex; flex-direction: row; align-items: center; justify-content: space-between; gap: 20px;">
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/post-launch-sop/web-widget.png" target="_blank" style="width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: auto; height: 200px; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/post-launch-sop/web-widget.png" alt="SeaChat | Custom Form in Widget">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Custom Form in WebChat Widget</p>
    </div>
    <div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center;">
        <a href="/images/seachat/en/post-launch-sop/web-widget-form.png" target="_blank" style="width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;">
            <img style="width: auto; height: 200px; border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/post-launch-sop/web-widget-form.png" alt="SeaChat | Create Web Widget">
        </a>
        <p style="margin-top: 20px; font-size: 15px">Create WebChat Widget</p>
    </div>
</div>

## Daily Routine

### What Human Agents Should Do

Every day, your agent should do two things:

- Go to Conversations and reply to incoming inquiries
- Mark anything that’s answered not well by the AI Agent using 👎
- Mark anything that’s answered well by Human Agents using 👍

### What AI Agent Editor and Admin Should Do

Every day, your AI Agent Editor or Admin should do three things:

- Go to Conversations and watch how the AI Agents and Human Agents replied to your customers
- Mark anything that’s answered not well by the Human Agent using 👎
- Mark anything that’s answered well by Human Agents using 👍

Once the AI Agent Editor or Admin identified areas that need improvement, they can go to the *Needs Review* session and start adding or modifying the Knowledge Base:

<center>
<a href="/images/seachat/en/post-launch-sop/need-review.png">
<img height="100%" width="80%" src="/images/seachat/en/post-launch-sop/need-review.png"  alt="AI Agent Editor and Admin should review daily conversations in 'Need Reviews' section on SeaChat to improvement chat quality">
</a>

*Conversations that need reviews*

</center>

## Weekly Routine

Every week for about 30 minutes to 1 hour, the Admin should work with the AI Agent Editor in the following areas:

*Improve the knowledge base*
- Review the *Needs Review* session and revise the knowledge base
- KB revision includes not only addition, but also removing old stale articles.

*Use Knowledge Base to improve your website*
- Discuss what’s being added to the knowledge base
- If there are commonly asked questions, consider adding them to your website.

*Use your website to improve your Knowledge Base*
- If you recently have written more documents, and you want the AI Agents to know, you can go to the Knowledge Base to import them.
- If your website changed, you can re-import them by clicking on the *Sync Now* button.

<center>
<a href="/images/seachat/en/post-launch-sop/knowledge-base.png">
<img height="100%" width="80%" src="/images/seachat/en/post-launch-sop/knowledge-base.png"  alt="Update your agent's Knowledge Base on a weekly bases to improve the performance of your agents' response.">
</a>

*Update Knowledge Base for improvement*

</center>

## Keep Iterating

The AI Agents know about two things:
- what they are trained to know about your business
- world knowledge about some common sense and facts

It is your responsibility to improve them on a daily and weekly basis to make it better, so that your human agents will do less and less work!


---


#### Evaluation: Enhancing AI Agent Response Accuracy with Test Sets

<!-- Source: seachat-manual/07-test-and-improve-ai-agent/evaluation.md -->

<!-- Weight: 802 -->

*Enhancing AI Agent Response Accuracy with Test Sets*


## **1\. Overview**

The **Evaluation** feature in SeaChat allows users to systematically test their AI agent's performance by comparing actual responses to predefined gold responses. It uses large language model to evaluate test sets and assigns correctness scores to determine response quality. It helps businesses **monitor, test, and improve** their AI agent’s performance.

- It ensures high-quality responses by comparing real-time agent answers with gold standards.
- Users can refine their AI models by testing responses regularly and adjusting knowledge base content.
- Seamless integration with real customer conversations allows users to improve AI dynamically.

## **2\. Use Case**

### **📌 Use Case 1: Quality Assurance for AI Agent Responses**

A customer support team at an **e-commerce company** wants to ensure that their AI agent gives **accurate return policy information**.

- They create a **Test Set** with **common return-related questions**.
- They input **gold responses based on company policy**.
- After a test run, they find that **30% of responses are incorrect**.
- They update the **knowledge base** and re-run the test, improving the AI’s accuracy.

✅ **Outcome:** The AI agent now provides **correct return policy answers**, reducing **customer escalations**.

---

### **📌 Use Case 2: AI Agent Performance Monitoring**

A SaaS company using SeaChat wants to track AI performance across **product troubleshooting queries**.

- Every month, they run **a test set with 100+ common customer issues**.
- They compare correctness scores over time to **track improvements**.
- When scores drop, they analyze **incorrect responses and knowledge base gaps**.

✅ **Outcome:** Proactive monitoring prevents **customer frustration** and **increases support efficiency**.

---

### **📌 Use Case 3: Improving AI Agent for Multilingual Support**

A **global airline** wants to test how well its AI agent handles **customer queries in different languages**.

- They create test sets for **English, Spanish, and French** queries.
- They use **gold responses verified by human translators**.
- Test runs reveal that the AI struggles with **French flight rescheduling queries**.
- They improve **French language knowledge base** and re-test.

✅ **Outcome:** The AI agent provides **accurate, multilingual support**, reducing **miscommunication**.

---

### **📌 Use Case 4: Training AI Agent for Industry-Specific Knowledge**

A **healthcare provider** uses SeaChat to **automate patient FAQs**.

- They create a **test set with medical insurance questions**.
- They add **gold responses written by medical professionals**.
- Test results show **inconsistent answers about coverage limits**.
- They refine **AI agent description and knowledge base and re-run tests** to ensure correctness.

✅ **Outcome:** The AI agent now provides **trusted medical guidance**, ensuring **compliance and accuracy**.

## **3\. How to Set Up**

### **Step 1: Navigate to the Evaluation Tab**

1. Log in to **SeaChat**.
2. Click on the **Evaluation** tab in the left sidebar.

### **Step 2: Create a New Test Set**

1. Click the **three-dot menu** (⋮) in the Evaluation tab.
2. Select **"Add New Test Set"**.
3. Enter a **Test Set Name**.
4. Set the **Individual Test Sample Success Threshold** and **Test Set Success Threshold** (values between **0 and 1**). These thresholds determine whether a response is correct.
5. Click **Confirm** to create the test set.

<br/>

<center>
<a href="/images/seachat/en/evaluation/2add-a-new-set.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/2add-a-new-set.png"  alt="Add a new set">
</a>

_Click + Add new set to add a new set_

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/3new-set-input.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/3new-set-input.png"  alt="Add new test configurations">
</a>

_Configure a set name and thresholds to be considered correct_

</center>

### **Step 3: Add Test Samples**

1. Click the **"Add New Sample"** button inside your test set.
2. **Configure the test sample:**
   - **Conversation History:** Add relevant context with past **user/agent messages**.
   - **User Test Query:** The exact user message that will be tested.
   - **Agent Gold Response:** The ideal AI-generated response for comparison.
3. Click **Save** to add the test sample.

<br/>

<center>
<a href="/images/seachat/en/evaluation/4add-sample.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/4add-sample.png"  alt="Add a new test sample">
</a>

_Example: Add a user test query and an agent gold response to customerQ&A test set_

</center>

### **Step 4: Run the Test Set**

1. Click the **Run** icon next to the test set and click confirm button in the popup
2. Navigate to the **Test Runs** tab to review the results.

<center>
<a href="/images/seachat/en/evaluation/5run-set.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/5run-set.png"  alt="Click Run button to run">
</a>

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/6confirm-run.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/6confirm-run.png"  alt="Click Run button to run">
</a>

</center>

### **Step 5: Review Test Run Results**

1. Review all test runs in the **Test Runs** tab

<center>
<a href="/images/seachat/en/evaluation/7test-run-page.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/7test-run-page.png"  alt="Navigate to Test Runs tab to view results">
</a>

</center>

<br/>

2. Click on a completed test run to view:
   - **Overall Correctness Score** for the test set.
   - **Correctness Scores for each test sample**.
   - **Actual AI agent responses vs. Gold responses**.
   - **Knowledge Base articles** the AI agent referenced.
3. If needed, **edit knowledge base articles** to improve AI responses.

<br/>

<center>
<a href="/images/seachat/en/evaluation/8test-run-result.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/8test-run-result.png"  alt="Click one item to view the results in detail">
</a>

_Example: The first query has a correctness score of 19.55% and the second one has a score of 65.47%, resulting in an overall correctness of 43.51%._

</center>

### **Step 6: Adding Test Samples from Real Conversations**

1. During live conversations, if the AI agent provides an to-be-improved or exceptional response, click the **Thumb Down/UP** button.
2. The response will appear under the **"Needs Review"** tab.
3. Click the response, then select **"+ Add to Test Set"**.
4. Choose a **Test Set Name** and configure:
   - **Conversation History**
   - **User Test Query**
   - **Agent Gold Response**
5. Click **Save**. The test sample is now added to the test set for future evaluations.
6. Repeat **Step 4 and Step 5** to re-run tests and refine AI responses.

<br/>

<center>
<a href="/images/seachat/en/evaluation/11needs-review-page.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/11needs-review-page.png"  alt="Click Add to Test Set button to add to a test set">
</a>

_Example: In the Needs Review page, click the + Add to Test Set button to add the agent response to a test set._

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/12needs-review.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/12needs-review.png"  alt="Modify sample to be added to the test set">
</a>

_Example: Add user message and modify the agent gold response, then add this sample to the customerQ&A test set._

</center>

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/13new-sample-test-set.png.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/13new-sample-test-set.png"  alt="View the newly added test sample">
</a>

_Example: Navigate to the Evaluation page, the NLP related query has been added to the customerQ&A test set._

</center>

## **3\. Pricing**

Test runs consume agent responses and will be billed accordingly. Each test case in a test set costs **$0.01**.

## **4\. Importing and Exporting Evaluation Test Sets**

Managing evaluation test sets efficiently is essential for optimizing AI model performance. The system allows users to **export** test sets for backup, editing, or sharing, and **import** them for bulk updates. Follow the instructions below to **export** or **import** a test set.

### **Use Case**

Importing and exporting evaluation test sets can be beneficial in multiple scenarios, such as:

1. **Data Backup and Recovery**
   - Export test sets regularly to create backups, ensuring that no critical test data is lost.
   - If an evaluation test set is accidentally deleted or modified, users can easily restore it by importing a previously saved JSON file.
2. **Collaboration and Sharing**
   - Teams working on AI model evaluation can share test sets by exporting them to a JSON file and sharing them across different environments.
   - This is particularly useful when different teams need to validate or benchmark AI models with the same test cases.
3. **Bulk Management and Editing**
   - Instead of manually adding test samples one by one, users can **export** a test set, edit the JSON file in bulk, and **import** it back into the system.
   - This speeds up test set updates and modifications, ensuring consistency and reducing manual work.
4. **Migrating Test Sets Across Environments**
   - Users can move test sets between **staging, development, and production environments** by exporting them from one environment and importing them into another.
   - This ensures that AI models are tested consistently across different environments.
5. **AI Model Benchmarking**
   - Users can create standardized test sets for benchmarking AI model improvements over time.
   - Exporting and importing test sets allows for reusing the same evaluation set to track progress effectively.

## **How to Export an Evaluation Test Set**

1. Navigate to the **Evaluation** tab.
2. Click the **three-dot menu** (⋮) next to the evaluation test set you want to export.
3. Select **"Export this set"** from the dropdown menu.

<center>
<a href="/images/seachat/en/evaluation/export-import-menu.png">
<img height="100%" width="40%" src="/images/seachat/en/evaluation/export-import-menu.png"  alt="Option menu">
</a>

</center>

4. A notification window will appear with a link to the JSON file.
5. Click the link—it will open the JSON file in a new tab.
6. Right-click on the new tab and select **"Save As"** to download the JSON file.

<center>
<a href="/images/seachat/en/evaluation/export-success.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/export-success.png"  alt="Export success message">
</a>

</center>

### **Example of an Exported JSON File:**

```{
  "id": "baded98d44024b63964a866c5c1670d3",
  "name": "customerQ&A",
  "set_success_threshold": 0.8,
  "sample_success_threshold": 0.8,
  "samples": [
    {
      "id": "8be53adf616a451d8282a6455f3f346d",
      "user_test_query": "What products do you offer?",
      "agent_gold_response": "We offer SeaX Messaging, SeaMeet, SeaChat, SeaVoice (including Discord bot), and SeaX Enterprise contact center solution.",
      "conversation_history": { "messages": [] }
    },
    {
      "id": "a6455f3f346d8be53adf616a451d8282",
      "user_test_query": "I need to use it with LINE, do you support it?",
      "agent_gold_response": "Yes, SeaChat can be integrated with LINE to respond to customer messages effectively.",
      "conversation_history": {
        "messages": [
          { "role": "user", "content": "Tell me all about SeaChat" },
          {
            "role": "assistant",
            "content": "SeaChat is an AI-powered intelligent chatbot that automates responses to customer queries and transitions to human support when needed."
          }
        ]
      }
    }
  ]
}
```

## **How to Import from a File**

1. Navigate to the **Evaluation** tab.
2. Click the **three-dot menu** (⋮) and select **"Import from file"**.
3. Click to select a JSON file or drag and drop it into the upload window.
4. Once uploaded, click **"Done"** to finalize the process.
<center>
<a href="/images/seachat/en/evaluation/import-success.png">
<img height="100%" width="50%" src="/images/seachat/en/evaluation/import-success.png"  alt="Export success message">
</a>

</center>

### **Example JSON File for Import:**

```{
  "name": "customerQ&A",
  "set_success_threshold": 0.8,
  "sample_success_threshold": 0.8,
  "samples": [
    {
      "user_test_query": "What products do you offer?",
      "agent_gold_response": "We offer SeaX Messaging, SeaMeet, SeaChat, SeaVoice (including Discord bot), and SeaX Enterprise contact center solution.",
      "conversation_history": { "messages": [] }
    },
    {
      "user_test_query": "I need to use it with LINE, do you support it?",
      "agent_gold_response": "Yes, SeaChat can be integrated with LINE to respond to customer messages effectively.",
      "conversation_history": {
        "messages": [
          { "role": "user", "content": "Tell me all about SeaChat" },
          {
            "role": "assistant",
            "content": "SeaChat is an AI-powered intelligent chatbot that automates responses to customer queries and transitions to human support when needed."
          }
        ]
      }
    }
  ]
}
```

If you need further assistance, feel free to reach out to [seachat@seasalt.ai](mailto:seachat@seasalt.ai)! 🚀


---


#### Custom GPT Tools

<!-- Source: seachat-manual/09-automation/gpt-tools.md -->

<!-- Weight: 900 -->


## Overview

Custom GPT Tools in SeaChat allow users to enhance the agent's responses by integrating custom actions directly into conversations. This feature enables users to define specific conditions under which the agent can execute these actions, providing tailored responses and intelligent assistance based on real-time information. For example, you might want the agent to perform a search or fetch data from your company’s API, enabling SeaChat to provide enriched answers that draw on external resources.

## Video Tutorials

Here’s a quick simple tutorial to call two APIs to display single picture. We demonstrate how to configure the API endpoint, and display cute dog pictures in the chat:


<iframe width="100%" height="400" src="https://www.youtube.com/embed/olWQTiPLHOc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

In the 2nd tutorial, we call the weather API by configuring the API parameters, and dynamically converting location names to GPS coordinates to get accurate weather information:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/7v7zBr5j-So?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

In this 3rd tutorial, we demonstrate how to get a carousel of cards with multiple dog pictures. We showed you how to utilize the **PATH** parameter to display multiple pictures of a specified dog breed in the chat:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/wBGJyfB9hcY?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

In this 4th tutorial, we demonstrate how to set up email alerts using Custom GPT Tools in SeaChat, detecting concerning content in chat conversations and automatically sending email notifications.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/KhjHDbRTIJc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

In this 5th tutorial, we demonstrate how to configure SMS notifications in SeaChat for monitoring user conversations. As an example, we demonstrated how to set up SMS alerts when detecting signs of depression in user interactions in this video.

<iframe width="100%" height="400" src="https://www.youtube.com/embed/Z7Zj6BWEXTc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

In this 6th tutorial, we demonstrate how to automatically send information to callers via SMS. 

<iframe width="100%" height="400" src="https://www.youtube.com/embed/LNezPT4qzCs?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>


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


---


#### Auto Labeling

<!-- Source: seachat-manual/09-automation/auto-labeling.md -->

<!-- Weight: 901 -->

*Learn how to set up and use the Auto Labeling feature to automate and streamline conversation labeling processes.*


---

## Video Tutorial

<iframe width="100%" height="400" src="https://www.youtube.com/embed/2lZcfofYQj4?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  allowfullscreen style="border-radius: 30px;"></iframe>

---

**Overview**  
Auto Labeling is an integral part of the integrations in Seasalt.ai's suite of tools. This feature intelligently and automatically applies labels to conversations, streamlining processes for use cases such as customer service and healthcare. 

We welcome you to check out our feature of [Label Automation](https://wiki.seasalt.ai/seachat/manual/labeling/label-automation/) for more advanced workflows as labe-automation builds upon the auto Labeling feature.

**What Is Auto Labeling?**  
Auto Labeling is a system that automates the application of labels to conversations or other data points based on predefined rules and AI-driven analysis. Instead of manually tagging, users can set conditions under which labels are applied or removed dynamically.

---

## Key Features


<center>
<a href="/images/seachat/en/labeling/auto-labeling/auto-labeling-feat-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/auto-labeling-feat-ui.png"  alt="Overview of the Auto Labeling UI">
</a>

</center>

<br/>

1. **Automated Label Application**  
   - Adds labels like ```Escalated``` or ```Low Priority``` based on conversation content.  
   - Handles multiple labels simultaneously.

2. **Dynamic Rule-Based System**  
   - Users can define triggers for labels, such as specific keywords or phrases.  
   - Includes functionality to both add and remove labels automatically.

3. **Custom Use Cases**  
   - Examples include healthcare hotlines, where ```Escalated``` might apply to severe pain, or ```Low Priority``` to minor aches.

4. **Visual Feedback**  
   - Labels appear in conversation histories, providing instant insight into their classification.

---

## How to Set Up Auto Labeling

1. **Navigate to Integrations**
   - Open the ```Integrations``` section and select ```Auto Labeling.```  


<center>
<a href="/images/seachat/en/labeling/auto-labeling/navigation-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/navigation-ui.png"  alt="Navigation to Auto Labeling">
</a>

</center>

<br/>

2. **Create Rules**  
   - Define triggers for adding or removing labels.  
   - Example: For healthcare hotlines:
     - ```Extreme pain``` triggers the ```Escalated``` label.  
     - ```Minor aches``` triggers the ```Low Priority``` label.  

<br/>

<center>
<a href="/images/seachat/en/labeling/auto-labeling/define-rules.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/define-rules.png"  alt="Define Labeling Rules">
</a>

<br/>

</center>

3. **Test Your Rules**  
   - Simulate conversations to see if labels apply correctly.  
   - Example: Input "I feel so much pain, I need a doctor’s attention" to trigger ```Escalated.```  

<center>
<a href="/images/seachat/en/labeling/auto-labeling/test-rules.png">
<img height="100%" width="80%" src="/images/seachat/en/labeling/auto-labeling/test-rules.png"  alt="Test Labeling Rules in Conversation">
</a>


</center>

<br/>

4. **Adjust and Save**  
   - Modify rules to refine accuracy and save the configuration.  


<center>
<a href="/images/seachat/en/labeling/auto-labeling/save-rules.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/save-rules.png"  alt="Define Labeling Rules">
</a>

</center>

<br/>

---

**Advanced Use Cases**  

1. **Medical Triage System**  
   - Labels like ```Green```, ```Yellow```, and ```Red``` can classify conditions based on severity.  
     - Red: Severe issues like difficulty breathing or severe bleeding.  
     - Yellow: Moderate pain or fever.  
     - Green: Minor aches or colds.  


<center>
<a href="/images/seachat/en/labeling/auto-labeling/advanced-rules.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/auto-labeling/advanced-rules.png"  alt="Define Labeling Rules">
</a>

</center>

<br/>

2. **Label Automation**  
   - Link actions to specific labels:
        - Trigger an email or SMS when ```Escalated``` is applied.  
        - Automate follow-ups for ```Low Priority``` cases.
   - Check out our tutorial on [Label Automation](https://wiki.seasalt.ai/seachat/manual/labeling/label-automation/) for more details.


---

**Benefits of Auto Labeling**  

- **Efficiency**: Reduces manual labeling efforts.  
- **Scalability**: Handles high volumes of data.  
- **Accuracy**: Ensures consistent application of rules.  
- **Customization**: Adapts to various industries and use cases.  

---

**Conclusion**  
Auto Labeling transforms how businesses manage conversations and data. From dynamic triaging in healthcare to streamlining customer support, this tool simplifies and accelerates processes while ensuring accuracy. Future tutorials will delve into removing labels and leveraging label automation for more advanced workflows. Stay tuned!



---


#### Label Automation

<!-- Source: seachat-manual/09-automation/label-automation.md -->

<!-- Weight: 902 -->

*Learn how to set up and use Label Automation in SeaChat to trigger actions based on applied labels.*


---

## Video Tutorial

<iframe width="100%" height="400" src="https://www.youtube.com/embed/2SYYU1lQqrc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px";></iframe>

---

**Overview**  

Label Automation is a feature in SeaChat that allows users to define actions triggered when labels are applied or removed from conversations. 

It builds upon the [Auto Labeling](https://wiki.seasalt.ai/seachat/manual/labeling/auto-labeling/) feature by introducing workflows to notify or escalate important events automatically.

This tutorial walks you through setting up Label Automation, providing practical examples to enhance your workflow.

---

## Key Features

<center>
<a href="/images/seachat/en/labeling/label-automation/feature-overview.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/feature-overview.png"  alt="Feature Overview">
</a>

</center>

<br/>

1. **Trigger Actions Automatically**  
   - Set up actions such as sending emails, SMS, or API requests.  
   - Actions are triggered as soon as a specific label is applied or removed.

2. **Customizable Workflows**  
   - Define workflows for individual labels like **Code Red** or **Code Yellow.**  
   - Tailor actions to your use case, such as healthcare triage or customer service alerts.

3. **Built-in Automation**  
   - Avoid reliance on external tools like Zapier by using SeaChat's integrated features.  

4. **Manual and Automatic Integration**  
   - Labels can be applied either automatically using Auto Labeling or manually during conversations.

---

## How to Set Up Label Automation

1. **Navigate to Integrations**  
   - Open the **Integrations** section and select **Label Automation**.


<center>
<a href="/images/seachat/en/labeling/label-automation/navigation-ui.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/navigation-ui.png"  alt="Navigate to Label Automation">
</a>

</center>

<br/>

2. **Choose a Label**  
   - Select a label such as **Code Red** or **Code Yellow.**  
   - Example: Use **Code Red** for severe conditions.

<center>
<a href="/images/seachat/en/labeling/label-automation/choose-a-label.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/choose-a-label.png"  alt="Choose Label to Automate">
</a>

</center>

<br/>

3. **Define Actions**  
   - Add actions for the selected label:
     - **Email**: Specify recipients and message content.
     - **SMS**: Provide a phone number and message text.
     - **API Requests**: Configure custom endpoints (for advanced users).  



<center>
<a href="/images/seachat/en/labeling/label-automation/define-action.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/define-action.png"  alt="Define Automation Action">
</a>

</center>

<br/>

4. **Save and Test**  
   - Save the configuration and test it by manually or automatically applying the label.  

<center>
<a href="/images/seachat/en/labeling/label-automation/save-and-test.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/save-and-test.png"  alt="Save and Test Actions">
</a>

</center>

<br/>

---

## Example Use Case: Healthcare Triage

To see the full version of the use case example, please check out our video tutorial on Label Automation.

1. **Code Red - Severe Conditions**  
   - **Trigger**: Apply **Code Red** to conversations involving severe conditions like difficulty breathing or severe bleeding.  
   - **Action**: Send an email and SMS to the relevant healthcare team.

2. **Code Yellow - Moderate Conditions**  
   - **Trigger**: Apply **Code Yellow** for cases such as moderate pain or fever.  
   - **Action**: Notify relevant staff via email.

3. **Removing Labels**  
   - **Trigger**: When **Code Red** is removed, send an email to notify **Alert Disarmed.**  

---

## Workflow Example

1. **Defining a Workflow for **Code Red****  
   - Set up an email to notify staff about a severe condition.  
   - Configure an SMS alert to a Google Voice number for redundancy.

<center>
<a href="/images/seachat/en/labeling/label-automation/define-email-action.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/define-email-action.png"  alt="Define Email Actions">
</a>

</center>

<br/>

2. **Manual Trigger Test**  
   - Apply **Code Red** manually during a conversation and verify actions.  
   - Check email and SMS notifications to confirm they were triggered correctly.

<center>
<a href="/images/seachat/en/labeling/label-automation/conversation-example.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/conversation-example.png"  alt="Conversation Example">
</a>

</center>

<br/>

3. **Automated Trigger with Auto Labeling**  
   - Combine with the Auto Labeling feature to trigger **Code Red** based on predefined conversation rules.  

<center>
<a href="/images/seachat/en/labeling/label-automation/action-on-labeling.png">
<img height="100%" width="100%" src="/images/seachat/en/labeling/label-automation/action-on-labeling.png"  alt="Auto Labeling Integration">
</a>

</center>

<br/>

---

**Benefits of Label Automation**

- **Efficiency**: Streamline workflows by automating actions triggered by labels.  
- **Flexibility**: Support both manual and automatic labeling.  
- **Integration**: Built directly into SeaChat, eliminating the need for third-party tools.  
- **Customization**: Configure workflows to suit various industries and use cases.  

---
 
**Advanced Features**

- **API Integration**: For advanced users, trigger custom workflows using API requests.  
- **Combined Automation**: Integrate Label Automation with Auto Labeling for a seamless workflow.  

---

**Conclusion**  
Label Automation enhances SeaChat's capabilities by turning applied labels into actionable events. Whether you're managing a healthcare hotline or streamlining customer service, this feature provides the tools to automate and optimize your processes. Try combining Label Automation with Auto Labeling to create powerful, efficient workflows tailored to your needs.



---


#### Zendesk Ticket Search Tool

<!-- Source: seachat-manual/09-automation/zendesk-ticket-search.md -->

<!-- Weight: 903 -->


The SeaChat Zendesk Ticket Search Tool is an innovative feature from Seasalt.ai that streamlines support workflows by transforming complex Zendesk ticket data into direct, context-aware answers for user queries. Instead of forcing users to sift through numerous search results and manually open individual tickets, SeaChat extracts key insights from entire ticket conversations and returns precise answers—all in a single interaction.

---

<iframe width="100%" height="400" src="https://www.youtube.com/embed/PJYiC-jKDnU?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px";></iframe>

## How It Works

The tool leverages Zendesk’s robust API capabilities through the following steps:

**1. Keyword Extraction:**

When a user submits a query, SeaChat automatically parses the input to extract one or more keywords. These keywords are then used to form a search query to the Zendesk Search API.

**2. Ticket Search via Zendesk Search API:**

SeaChat submits the extracted keyword(s) to the Zendesk Search API `/api/v2/search.json?query=xxx`. This API returns a list of relevant tickets based on the search criteria. Notably, the initial API response includes only the first comment (often the ticket’s description) for each ticket thread, which serves as a preview of the ticket content.

**3. Retrieving Full Ticket Threads:**

For each ticket returned in the search results, SeaChat then makes additional requests to the Zendesk Ticket Comments API `/api/v2/tickets/{id}/comments`. This step ensures that all comments—including follow-ups, agent responses, and internal notes—are retrieved, providing a complete picture of the ticket’s history.

**4. Answer Synthesis:**
Finally, using advanced natural language processing, SeaChat analyzes the full ticket conversations to determine the most relevant answer to the user's query. This process aggregates insights from multiple tickets if needed, allowing SeaChat to deliver a direct and actionable response without requiring manual navigation through the Zendesk UI.

---

## Use Cases

The SeaChat Zendesk Ticket Search Tool is versatile and can be applied in various support and operational scenarios:

-- **Streamlined Support Response:**
Agents can quickly retrieve complete answers to customer questions by tapping into historical ticket data, reducing the time spent manually searching through tickets.

-- **Automated Knowledge Base Augmentation:**
By consolidating frequent queries and their corresponding resolutions, the tool can help automatically update FAQs and knowledge base articles, ensuring that self-service options are always current and accurate.

-- **Root Cause Analysis:**
Support managers can utilize the tool to analyze patterns in ticket conversations—such as recurring issues or common troubleshooting steps—to improve product reliability and customer satisfaction.

-- **Efficient Data Integration:**
When integrating Zendesk with other systems (e.g., CRM platforms or analytics dashboards), the tool’s ability to extract comprehensive ticket information enables more effective cross-platform data analysis and reporting.

---

By combining the powerful search capabilities of Zendesk’s Search API with the detailed insights provided by the Ticket Comments API, SeaChat offers a seamless and efficient alternative to the traditional Zendesk search UI. This innovative approach not only accelerates the resolution process but also improves the overall quality of support responses.

## **Steps to Configure a Zendesk Ticket Search Tool:**

To set up this feature, after logging into SeaChat, navigate to Agent Configuration \-\> Integrations \-\> Custom GPT Tools.

### **Step 1: Select Tool Type**

Click **"Add a New Custom GPT Tool"**, then select **Zendesk Ticket Search** as the tool type.

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image1.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image1.png"  alt="Example of New Custom Tool">
</a>
<br/>
</center>

### **Step 2: Add Zendesk Account Information**

To configure a Zendesk ticket search tool, you’ll need to provide several key pieces of information:

- Enable the Tool: Turn on the Enable switch. This will activate the tool, allowing SeaChat to start using it automatically in relevant conversations.
- Tool Name: Enter a name for your tool. This should contain only letters (A-Z, a-z), numbers (0-9), underscores (\_), or hyphens (-) without any spaces.
- Description: Provide a detailed description of what kind of data SeaChat can expect to find in Zendesk and under what conditions it should activate this custom tool.

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image2.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image2.png"  alt="Example of New Custom Tool">
</a>
<br/>

_Example: We set up a Zendesk ticket search tool to retrieve tickets, product names, and prices._

</center>

You should also provide the following Zendesk account information to allow SeaChat to securely access and search tickets.

- **Subdomain**: Your Zendesk subdomain is the first part of your Zendesk URL. For example, my Zendesk URL is: *https://seasaltai9494.zendesk.com*,then, my subdomain is _seasaltai9494_.
- **Email**: Enter the email address associated with your Zendesk account. This is the same email you use to log in.
- **API Token**: It authenticates SeaChat’s access to your Zendesk account, To generate an API token, follow these steps:

1. Log in to your Zendesk Admin Center.
2. In the left sidebar, go to Apps and Integrations → Zendesk API.
3. Under the Settings tab, find the Token Access section.
4. Toggle Enable API Token Access (if not already enabled).
5. Click Add API Token.
6. Optionally, add a description for the API token.
7. Copy the generated API token and store it securely (it will not be displayed again).
8. Click Save.

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image3.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image3.png"  alt="Example of New Custom Tool">
</a>
<br/>

_Example: We entered Zendesk account credentials to authenticate SeaChat for API access._

</center>

### **Step 3: Define Search Parameters**

You can customize the search parameters to control how Zendesk tickets are retrieved and displayed.

- **per_page:** It determines the number of tickets to retrieve in a single request. It is recommended to set this between 1 and 20, with a default value of 5\. For each retrieved ticket, SeaChat will call the Zendesk API to fetch its details and comments using the following endpoint: `GET https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_no}/comments`  
  Since SeaChat retrieves all comments for each ticket, increasing the number of tickets per request may slow down the response time.
- **sort_by**: It defines the sorting criteria for the retrieved tickets. You can choose to sort by the ticket’s last updated time (updated_at), creation time (created_at), priority (priority), status (status), or type (ticket_type). By default, the sorting is based on relevance.
- **sort_order**: It specifies whether the tickets should be sorted in ascending (asc) or descending (desc) order. The default sorting order is descending.

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image4.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image4.png"  alt="Example of New Custom Tool">
</a>
<br/>

_Example: We fetch 10 tickets and their comments at a time, sorting them by the latest update in descending order (newest to oldest)._

</center>

### **Step 4(Optional): Test Your Zendesk Ticket Search setting**

Before finalizing, you can test the tool by entering a query such as a **product name, order number, or relevant query**. Click **Submit** to send a test request. If successful, you will see real-time Zendesk search results displayed on the right-hand side.

<center>
<a href="/images/seachat/en/zendesk-ticket-search/image5.png">
<img height="100%" width="100%" src="/images/seachat/en/zendesk-ticket-search/image5.png"  alt="Example of New Custom Tool">
</a>
<br/>

_We tested using the product 452-ABC and successfully retrieved ticket comments related to this product._

</center>

### **Step 5: Save your tool**

Click Save, and your Zendesk Ticket Search tool is ready to use. Your SeaChat AI agent can now retrieve Zendesk ticket data to enhance customer support.


---


#### User Sends an Image Message

<!-- Source: seachat-manual/08-incoming-queries/01-user-sends-an-image-message.md -->

<!-- Weight: 1000 -->

*Learn how SeaChat understands and responds to user uploaded image messages.*


# Overview

Up to this point, you've likely only seen SeaChat respond to text-based user chat messages. However, SeaChat has the capability to handle multimedia messages, such as audio and image, as well! This makes interactions more flexible and convenient for users, enabling them to share content in various formats for richer communication. 

---

## Image Understanding

When a user uploads an image, SeaChat analyzes it to generate a detailed textual description. This description serves as the foundation for SeaChat's response, ensuring that the AI’s reply is tailored to the visual content. The process is designed to make it easier for users to share visual information without needing to describe or re-type it themselves.

> :bulb: **Note** 
> This feature is only available to premium subscribers. For non-premium accounts, SeaChat will only know that the user uploaded an image, but will not have any insight on the content.

### Example

In the following example, a user chats with the Seasalt.ai bot via WebChat and uploads a screenshot of a webinar invite in their message to the agent. By analyzing the contents of the image, SeaChat is able to understand and respond to the user's message effectively (without the user having to re-type all the contents of the image).

<br/>
<center>
<a href="/images/seachat/en/incoming-queries/SeaChat_Responds_to_Image_Message_Webchat.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/incoming-queries/SeaChat_Responds_to_Image_Message_Webchat.png" alt="SeaChat is able to understand and respond to a user-uploaded image message in WebChat.">
</a>

*Sending an Image Message to SeaChat*
</center>

<br/>

---


### Pricing

<!-- Source: seachat-payments/pricing-plans.md -->

<!-- Weight: 1100 -->

*SeaChat's flexible pricing plans for various business needs. Learn about plan features, model options, and support packages.*


SeaChat offers a range of pricing plans to suit your business needs. Choose from our flexible plans to get started with SeaChat today. 

Each plan includes a set of features that cater to different business requirements. You can upgrade or downgrade your plan at any time to suit your business needs.

Here we will take a look into the different pricing plans available for SeaChat.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/pricing-plans/pricing-plans.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/pricing-plans/pricing-plans.png" alt="SeaChat | Pricing & Plans">
</a>

**Pricing Information**
</center>


## Free

- Lifetime 100 free AI text replies
- 1 AI Agent
- Knowledge base includes up to 10 documents (200KB max) and 200k tokens
- 1 owner account and 1 workspace
- Model: ChatGPT-3.5-turbo

## Standard

- 2 AI Agents
- Knowledge base includes up to 100 documents (1 MB max) and 1 million tokens
- 1 owner account, 1 member account, and 1 workspace
- Every AI agent response costs $0.01USD
- Model: ChatGPT-3.5-turbo

## Premium

- 10 AI Agents
- Knowledge base includes up to 500 documents (10 MB max) and 5 million tokens
- 1 owner account, 3 member account, and 2 workspace
- AI agent response starting price $0.006USD
- Choose your favorite model. Options include GPT-4o mini, GPT-4o, GPT-4-turbo, ChatGPT-3.5-turbo, Mistral etc. 
- Voice AI agent over phone calls (starting from $0.15 per minute)
- Advanced features : Context Extraction / API Access / SeaChat branding Removal / Voice Agent

## Model Pricing

Premium and Enterprise users can choose from a range of models for their AI agents. Each model has a different pricing structure. Please refer to SeaChat official website for pricing details, or take a look at the pricing information down below.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/pricing-plans/pricing-model.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/pricing-plans/pricing-model.png" alt="SeaChat | Model Pricing">
</a>

**Model Pricing**
</center>


## Support Plan

For customers with complex usage scenarios, we recommend subscribing to our **Launch Support Plan**. Deploying an LLM-powered AI agent requires extensive in-domain knowledge, technical support, and careful design decisions. The SeaChat team has observed many failed deployments due to a lack of understanding of how LLMs and RAG function. Additionally, voice applications are subject to strict regulations from telecom authorities and the FCC.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/pricing-plans/pricing-support.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/pricing-plans/pricing-support.png" alt="SeaChat | Pricing Support">
</a>

**Support Plans**
</center>



---


### Billing and Subscription

<!-- Source: seachat-payments/subscription-and-billing.md -->

<!-- Weight: 1101 -->

*Manage your SeaChat billing and subscription. View and edit your plan, update billing info, and download invoices directly from the SeaChat dashboard.*


You can find all the information about billing and subscription in the billing section of the SeaChat dashboard. Find **Billing** in the left sidebar of the dashboard.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/billing-and-subscription/billing-and-subscription.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/billing-and-subscription/billing-and-subscription.png" alt="SeaChat | Billing & Subscription">
</a>

**Billing and Subscription**
</center>

## Subscription Plan

In the **Plan** section, you can see the details of your current subscription plan. Edit your plan by clicking the **Edit Plan** button. 

### Billing Details

Click on **Cost Breakdown** under **Next Billing Period** to see the details of your next billing details according to your subscription and usage.

### Billing Recipient

In the **Billing Recipients** section, you can see the details of the billing recipients. Click on **Change Recipient** to modify the billing recipient. If you have an organization name, you can add it here.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/billing-and-subscription/billing-recipients.png" target="_blank">
<img width="60%" style="border-radius: 0.4rem" src="/images/seachat/en/billing-and-subscription/billing-recipients.png" alt="SeaChat | Bill Recipient">
</a>

**Change Billing Recipient**
</center>


## Usage Details

In the **Usage** section, you can see the details of your usage. Your monthly usage is calculated based on total usage of your text and voice agent(s) in the current billing cycle.

## Billing History - Invoices

In the **Billing History** section, you can see the details of your past billing history. Click on the download icon to download the invoice in PDF format.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/billing-and-subscription/invoices.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/billing-and-subscription/invoices.png" alt="SeaChat | Invoices">
</a>

**Download Invoice**
</center>

---


### Build Email Lists with MailerLite

<!-- Source: full-tutorials/01-mailerlite.md -->

<!-- Weight: 1200 -->

*Integrate MailerLite with SeaChat Forms for email list building and campaign management with easy setup.*


---

* **MailerLite Integration**: Use MailerLite to gather emails and automate mailing lists for promotions and updates. SeaChat allows seamless integration with MailerLite to enhance your AI Webchat Agent.
* **Automatic Data Collection**: Configure SeaChat Agents to prompt users for their email and other details during interactions, ensuring no lead is missed.
* **Lead Retention and Engagement**: Keep all users informed and engaged by automatically adding them to your mailing lists after interaction with your agents.
---

For a visual guide on how to integrate SeaChat with MailerLite, you can watch the tutorial video below:
<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/xTnJ9L1sVC4?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


---
In this tutorial, we will walk you through every step you need to connect your MailerLite with SeaChat Forms.

## Step 1: Navigate to MailerLite setup

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-integrations/mailerlite/navigate-to-mailerlite-setup.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/navigate-to-mailerlite-setup.png" alt="Screenshot illustrating how to access MailerLite integration on SeaChat">
</a>

*Navigate to MailerLite integration on SeaChat*
</center>


With your workspace and agent selected, navigate to the "Agent Configuration" drop down on the left action bar and select "Plugins". From the Plugins page you can select the MailerLite card to access the setup page.

## Step 2: Collect emails using SeaChat Form and sync to MailerLite

On the Mailerlite setup page you will see two sections. The first section contains configuration settings for the form that will be sent to the user when starting a webchat conversation. The second section contains configuration settings for your specific MailerLite integration.

### SeaChat Form

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-integrations/mailerlite/mailerlite-form-setup.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/mailerlite-form-setup.png" alt="Screenshot illustrating how to configure form for MailerLite integration on SeaChat">
</a>

*Set up SeaChat Form for MailerLite integration*
</center>

The form configuration section has your settings on the left, as well as a preview of your current form on the right. Lets go over each of the settings and how they affect the form:

- **Enable This Form:** This switch enables and disables the form. When it is enabled, the form you configure will appear at the beginning of a new conversation with your SeaChat Agent. Keep in mind that you can only have one form attached to an agent at a time, so when you enable this, all other forms will disabled for the current agent. If you would like to use another form, this form must be disabled. 

- **Allow users to skip form:** When enabled this switch will allow users to skip your form by means of an **X** button that will appear in the top right of the form. When disabled, the **X** will not appear.

- **Form Name:** This is the name that the form will be saved under.

- **Form Title:** This is the Title that will appear at the top of the form when it appears to the user.

- **Form Design Fields:** These fields will appear on your form and will be what users fill out to submit information. The Email Field is required to add users to your MailerLite mailing list and cannot be configured, but the other fields can be configured individually. Each of these field's name can be changed by clicking on the field itself. To the right of each of these fields are two checkboxes for additional configuration. If "Required" is checked the
field must be filled before the user can submit the form; this will be indicated by an asterisk(*) next to the name of the field. The "Enabled" checkbox determines whether or not the field will appear on the form at all. If "Enabled" is unchecked, the field will not appear to user when they recieve the form. All fields except for Email are enabled and not required by default.

### MailerLite Setup

Next, there are two fields in the MailerLite integration settings card. 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-integrations/mailerlite/mailerlite-integration-setup.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/mailerlite-integration-setup.png" alt="Screenshot illustrating how to set up API key and group ID for MailerLite integration on SeaChat">
</a>

*Set up MailerLite on SeaChat*
</center>

The first is your API Key, which is what connects your form submissions to your MailerLite account. If you are unsure of how to find your MailerLite API Key you can follow this link for instructions: [How to get MailerLite API Key](/seachat/seachat-manual/05-integrations/05-seachat-mailerlite-integration/). There is also a link at the bottom of this card. 

**NOTE:** The API key field is required to save the integration

The second field, "Group ID" is optional. If you want users to be added to specific groups in your mailing list you can add their ids here (separated by comma if multiple). 

Once you have completed configuring your forms, you can save your configurations by pressing the save button at the bottom of the page. 

If you wish to remove your configurations, you can use the remove button at the top right of the page. This will clear out your settings for the MailerLite form in your workspace, filling the page again with the default values. 

## Step 3: Test your Form with MailerLite integration 

Once you have configured and saved your MailerLite form settings, you probably want to test that everything is working. To do this, make sure your form is enabled and navigate to the "Agent Information" page from the Agent Configuration drop down on the left action bar.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-integrations/mailerlite/test-ai-agent-button.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/test-ai-agent-button.png" alt="Screenshot illustrating how to test SeaChat AI agent for MailerLite integration">
</a>

*Test SeaChat form with MailerLite integration*
</center>

On this page you will see a large green button that says "Test AI Agent" on the bottom right. If you click this button it will open a chat conversation with your currently selected AI Agent. 


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-integrations/mailerlite/mailerlite-form-submission.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/mailerlite-form-submission.png" alt="Screenshot illustrating how to submit a form on SeaChat for MailerLite integration">
</a>

*How to submit the form on SeaChat, with MailerLite integration*
</center>


If it is a new conversation, within a few seconds your MailerLite form that you configured in the last step will appear at the bottom of the chat window. From here you can fill out requested information and hit submit at the bottom of the form. (Note: If this is not your first time testing your AI Agent it is possible that it will open a previous conversation. You can open this page in a new incognito window to ensure you start a new conversation)  



<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-integrations/mailerlite/mailerlite-find-email.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/mailerlite-find-email.png" alt="Screenshot illustrating how to check an email submission successfully lands on MailerLite">
</a>

*How to check for new email submissions on MailerLite*
</center>

Once the form has been submitted you can head over to MailerLite. Once you log in you can go to the Subscribers page from the left action bar. Here, you should be able to see the email from the user that you have just submitted at the top of your subscriber list. If you dont see it right away, you can also search for it up with the grey search button at the top right of the page.



<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat-integrations/mailerlite/mailerlite-view-email.png" target="_blank">
<img width="100%" style="border-radius: 0.4rem" src="/images/seachat-integrations/mailerlite/mailerlite-view-email.png" alt="Screenshot illustrating how to check details of an email on MailerLite">
</a>

*How to check details for an email on MailerLite*
</center>

You can click on the email to view details about the newly added subscriber such as any other information that might have been submitted with the form, as well as any groups that you included on the setup page.

## Conclusion
Configuring your SeaChat web agent with a MailerLite integration is an efficient method to enhance your lead acquisition process. Every interaction with your AI agent presents a potential subscription to your MailerLite mailing list, guaranteeing a steady influx of new subscribers. By following the provided guidelines, you can quickly establish this integration and begin expanding your user base effectively.


---


### Book Appointments Instantly with Google Forms & Voice Agent

<!-- Source: full-tutorials/02-google-forms.md -->

<!-- Weight: 1201 -->

*Streamline appointment booking with instant calls after form submission, leveraging the integration of Google Forms with SeaChat Voice Agent.*


---

At the end of this tutorial, you will be able to:
* 👍 Be compliant with the latest TCPA/FCC one-to-one rule using Google Forms
* 📋 Collect information from your customers using a **Google Forms**
* 📞 **Immediately call inbound leads** after they submit the form
* 📅 On the call, SeaChat voice agent will **prequalify leads and book appointments into your calendar**
* 📊 Track all calls made by the voice agent in a **Google Sheet**
* 🚀 **Book 10x more appointments**, serve customers 24/7 without needing to work more or hire more people


---
Calling right after form submission is crucial to lock down a meeting while the lead is still engaged and interested, increasing the chances of successful appointment scheduling.

In this tutorial, we will walk you through every step you need to connect your Google Form with SeaChat Voice Agent. 

> **Note:** If you use other types of forms such as web forms, Jotform, or any other form, please contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai). We will help you set up the same appointment booking integration.

## Video Tutorial

<iframe width="100%" height="400" src="https://www.youtube.com/embed/tMywzLCnwNI?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px";></iframe>


## Step 1: Create an Agent and Set Up the Appointment Scheduling Use Case

First, you need to create a SeaChat voice agent. This agent will be responsible for making calls, prequalifying leads, and booking appointments. For details on how to set up your voice agent, please refer to our [Create a New Agent](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/) guide. For this Google Forms integration, you will want to use the "Appointment Scheduling" use case, which we have a step by step guide on how to set up [in this video](https://www.youtube.com/embed/Hh04t_Qg8-I?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0).


## Step 2: Buy a Phone Number

Next, purchase a phone number through SeaChat. This number will be used by your voice agent to make calls to the customers who submit the Google Form.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/buy-phone-number-on-seachat.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/buy-phone-number-on-seachat.png" alt="Screenshot illustrating how to buy a phone number on SeaChat">
</a>

*You can buy a phone number directly on SeaChat*
</center>

The phone number is $3 per month and you can buy it directly on SeaChat and pay with your SeaChat monthly bill.

If you already have a phone number, you can contact us and we can discuss the cost to bring your own number to SeaChat or set up forwarding to your existing number.


## Step 3: Connect Google Calendar

Integrate your Google Calendar with SeaChat to ensure that voice agent has the latest information about your availability. This will allow the voice agent to check availability and schedule appointments directly into your calendar.

To learn how to connect your Google Calendar with SeaChat, please refer to our [Connect Google Calendar](https://wiki.seasalt.ai/en/seachat/integrations/google-calendar/) guide.

## Step 4: Copy the Google Form Template

> **🔗 [Download Template Google Form](https://docs.google.com/forms/d/1sPkZ-ZLlRToEFxuGvr1lZFkqKWVX6715iGAa0rWdsUA/edit).**

Copy our [template Google Form](https://docs.google.com/forms/d/1sPkZ-ZLlRToEFxuGvr1lZFkqKWVX6715iGAa0rWdsUA/edit) that includes all the essential fields to gather information from your customers as well as the required Google Apps Script to automate the call and booking process. Ensure that you have a field called "Phone Number" as this is essential for the voice agent to make calls. 

Collecting customer information using a different form? [Contact us](mailto:seachat@seasalt.ai) to set up the same integration and start booking appointments immediately.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/copy-google-form-template.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/copy-google-form-template.png" alt="Screenshot illustrating how to copy the Google Form template">
</a>

*Copy the Google Form template*
</center>


## Step 5: Connect a Google Form to your Voice Agent

First, let's find your SeaChat Agent ID and get a unique access token. These are the two keys you need to connect your Google Form to your SeaChat Voice Agent.

### Find your SeaChat Agent ID

Sign in to your SeaChat account and click on the "Agent Information" tab. You can find the SeaChat Agent ID in the URL, e.g. `https://chat.seasalt.ai/gpt/workspace/{WORKSPACE-ID}/bot/{AGENT-ID}/detail/botInfo` (the string between `bot/` and `/detail` is your Agent ID).

### Get a unique access token

Go to the "API Key" section at the bottom of the "Agent Information" section. Click on "API Key" hyperlink. This will open the API key management page. 

First, turn on the toggle of "Enable API Access". Then, copy the Access Token. Note that the Access Token is a very long string and you need to copy it all. 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/generate-seachat-access-token.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/generate-seachat-access-token.png" alt="Screenshot illustrating how to generate a new SeaChat access token">
</a>

*Generate a new access token*
</center>


### Add your Agent to your Google Form script 

Open the Google Form you just copied and click on the three dots in the top right corner. Select "Script Editor", which will open up a pre-filled script! 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/open-script-editor.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/open-script-editor.png" alt="Screenshot illustrating how to open the script editor">
</a>

*Open the script editor*
</center>


Next, replace the `YOUR_AGENT_ID` and `YOUR_ACCESS_TOKEN` with the ones you just got. Note that you need to replace the entire string, including the curly braces `{}` around the values.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/connect-seachat-agent-to-form-before.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/connect-seachat-agent-to-form-before.png" alt="Screenshot illustrating how to find the agent ID and access token">
</a>

*Where to find the agent ID and access token in Apps Script*
</center>

For example, if your agent ID is `1234567890` and your access token is `abcdefghijk`, the script should look like this:

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/connect-seachat-agent-to-form-after.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/connect-seachat-agent-to-form-after.png" alt="Screenshot illustrating how to replace the agent ID and access token">
</a>

*Replace the agent ID and access token*
</center>

Finally, click on "Save" to save the changes. The save button is the flappy disk icon at the top menu.

### Add a Trigger to the Google Form

Go to the "Triggers" section at the left-hand side menu. Click on "Add Trigger" button (in bottom right corner). 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/add-a-trigger.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/add-a-trigger.png" alt="Screenshot illustrating how to replace the agent ID and access token">
</a>

*Add a trigger for the Google Form Apps Script*
</center>

After clicking on "Save", Google Forms will ask you to authorize the script to access your Google Form. Follow the steps to authorize the script. If you encounter any anthorization issues, please just go back to the script editor and click on "Save" again to restart authorization.

## Step 6: Test the Phone Call by a Submission

Submit a test entry through your Google Form to ensure that the voice agent is working correctly. You should receive a call from the SeaChat agent shortly after submitting the form. 

The SeaChat agent should call the number provided, prequalify the lead, and book an appointment if applicable. You are welcome to test a lot and improve the agent performance. There are plenty of resources on this wiki website to help you improve the agent performance.

> **Note:** If you are not receiving a call, please check the [Troubleshooting](#troubleshooting) section below.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/test-voice-bot.png" target="_blank">
<img width="70%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/test-voice-bot.png" alt="Screenshot illustrating how to test the voice agent">
</a>

*Test the voice agent via a Google Form submission*
</center>


### Troubleshooting

If the voice agent is not working, please check the following:
* The phone number you provided is correct and reachable (We support e.164 format, e.g. +1234567890)
* You have an active SeaChat account, an active phone number connected to your account, and an active Premium plan
* The SeaChat agent is connected to the Google Form (Double check Step 5. Ensure you replaced the agent ID and access token correctly)

If you have any questions, please contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).


## Step 7: (Optional) Document All Call Activities on a Google Sheet

Congratulations! You have now set up a Google Form that automatically calls your customers and books appointments into your calendar, as soon as the customer submits the form. This is a great start, but you might want to keep track of all calls made by the voice agent. To do this, you can create a new tab in your Google Sheet called "Call Logs". 

To do this, you can connect your Google Form to a Google Sheet, and then add an Apps Script to your Google Sheet to automate the logging of calls.

### Connect Google Form to Google Sheet

First, you need to connect your Google Form to a Google Sheet. To do this, you can click "Responses" tab on your Google Form (You can find it at the top of the form management page), select "Link to Sheets" to create a new sheet. All the responses from your Google Form will be automatically logged into this new sheet.

Please open the Google Sheet after creating.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/create-google-sheet.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/create-google-sheet.png" alt="Screenshot illustrating how to connect your Google Form to a Google Sheet">
</a>

*Connect your Google Form to a Google Sheet*
</center>


### Add and Deploy an Apps Script

Add an Apps Script to your Google Sheet to automate the logging of calls. Go to "Extensions" -> "Apps Script" on the top menu.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/create-app-script-on-google-sheet.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/create-app-script-on-google-sheet.png" alt="Screenshot illustrating how to create an Apps Script on a Google Sheet">
</a>

*Create an Apps Script on a Google Sheet*
</center>

Copy the following script and paste it into the Apps Script editor. Remember to replace `{YOUR_SHEET_ID}` with the ID of your Google Sheet. 

> How to find the sheet ID? 
You can your Google Sheet ID from the URL of your Google Sheet, e.g. `https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit`. For example, if your Google Sheet URL is `https://docs.google.com/spreadsheets/d/abcdefg/edit`, your sheet ID is `abcdefg`.

```
function jsonEscape(str)  {
    return str.replace(/\n/g, "\\\\n").replace(/\r/g, "\\\\r").replace(/\t/g, "\\\\t");
}

function doPost(e) {
  try {
    // Open the target Google Sheet by its ID
    const spreadsheet = SpreadsheetApp.openById("1clTaM5mSR5rsrNKL_5PrL3im5mTFYS_LSvqeVaFjDPQ");

    // Get or create the sheet named "test"
    let parsedData = JSON.parse(JSON.parse(jsonEscape(e.postData.contents)));
    let sheet = spreadsheet.getSheetByName("Call Logs");
    if (!sheet) {
      sheet = spreadsheet.insertSheet("Call Logs");
    }

    // Log the target sheet information
    console.log("Writing to Sheet: " + sheet.getName());

    // Append the relevant data to the sheet
    sheet.appendRow([
      new Date(), // Timestamp of the script execution
      parsedData["agent_number"], // From
      parsedData["customer_number"], // To
      parsedData["call_status"], // Call status
      parsedData["summary"], // Call summary
      JSON.stringify(parsedData["labels"]) // Labels
    ]);
    console.log("Data written successfully!");

    // Return success response
    return ContentService.createTextOutput("Data processed successfully!");
  } catch (error) {
    // Log any errors encountered during execution
    console.log("Error: " + error.message);
    console.log("Stack Trace: " + error.stack);

    // Return error response
    return ContentService.createTextOutput("Error processing data: " + error.message).setMimeType(ContentService.MimeType.TEXT);
  }
}
```

After pasting the script, check whether Line 16 has the correct sheet ID. Then,click on "Save" to save the changes.

### Deploy the Apps Script

Click on "Deploy" button on the top menu. 

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/deploy-app-script.png" target="_blank">
<img width="100%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/deploy-app-script.png" alt="Screenshot illustrating how to deploy the Apps Script">
</a>

*Deploy the Apps Script*
</center>

Select "New Deployment" and then choose "Web app" as the deployment type. 

Please copy the setting in the screenshot. After you have copied the settings, click on "Deploy" button.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/web-app-config.png" target="_blank">
<img width="80%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem" src="/images/seachat/en/tutorial-google-form/web-app-config.png" alt="Screenshot illustrating how to deploy a web app">
</a>

*Configure the web app*
</center>

You will need to authorize the web app to access your account. Click on "Authorize" button and then select your Google account.

### Copy the Web App URL back to the Google Form Script

> Note: In this final step, you need go back to the Google Form script and replace the `{YOUR_CALLBACK_URL}` with the web app URL you just copied. The script in Step 5 is the Google Form script.

Copy the web app URL. You will need this URL to start receiving data from SeaChat Voice Agent and log it into your Google Sheet. This is the URL you will need to replace the `{YOUR_CALLBACK_URL}` in the Google Form script.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/tutorial-google-form/copy-webapp-url.png" target="_blank">
<img width="80%" style="border-radius: 0.3rem; border: thin solid black; style="border-radius: 0.4rem; border: thin solid black;" src="/images/seachat/en/tutorial-google-form/copy-webapp-url.png" alt="Screenshot illustrating how to copy the web app URL">
</a>

*Copy the web app URL*
</center>

Finally, replace the entire `payload` section with the following code snippet and then click on "Save" to save the changes:

```
    payload: JSON.stringify({
      "to_number": responsesObj['Phone Number'],
      "callback_url": "{YOUR_CALLBACK_URL}"
    })
```

`"callback_url": "{YOUR_CALLBACK_URL}"` will look like something like this: `"callback_url": "https://script.google.com/macros/s/abcdefggregqfkelwfww/exec"`



## Step 8: (Optional) Check the Call Logs

Make a call again and check the "Call Logs" tab in your Google Sheet after the call is finished. You should see the call logs there. By default, each new row in the "Call Logs" tab is a new call log containing the following information:

- Timestamp of the call
- Caller number, or AI agent phone number
- Customer number, or the phone number the customer submitted in the Google Form
- Call status, e.g. "Completed", "Voicemail", "No Answer", etc.
- Call summary
- Labels generated from the conversation


## Congratulations

Congratulations! You have now set up a Google Form that automatically calls your customers and books appointments into your calendar, as soon as the customer submits the form. For high achievers, you have also set up a Google Sheet to log all call activities.

You can now book 10x more appointments, serve customers 24/7 without needing to work more or hire more people. 

If you need help with integrating SeaChat with other types of forms, please contact us at [seachat@seasalt.ai](mailto:seachat@seasalt.ai).




---


### Forward Inbound Calls to Voice Agents - Video Tutorial

<!-- Source: inbound-voice-agent/tutorial.md -->

<!-- Weight: 1300 -->

*SeaChat Call Forwarding Tutorial*


---

The following is a video tutorial of the above walkthrough to deploy an AI voice agent in 18 minutes with no coding skills required:

<br/>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/Hh04t_Qg8-I?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube Video Player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>

---

## Introduction to Call Forwarding and How It Works

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/inbound-voice-agent/call-forwarding/call-forwarding-diagram.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; background-color: #ffffff" src="/images/seachat/en/inbound-voice-agent/call-forwarding/call-forwarding-diagram.png" alt="Call Forwarding Diagram">
</a>

**Call Forwarding**
</center>

Call forwarding is a telecommunication feature that allows users to redirect incoming calls from one number to another. This ensures that important calls are not missed, even when you're unable to answer your primary phone. There are two main types of call forwarding: Unconditional Call Forwarding, which redirects all incoming calls, and Conditional Call Forwarding, which only forwards calls under specific conditions, such as when the line is busy or when there’s no answer.

In most cases, businesses and individuals prefer Conditional Call Forwarding to ensure that calls are forwarded only when necessary, rather than every time a call comes in. Setting up this feature is usually straightforward, and different telecom providers and VoIP services offer simple ways to configure call forwarding through settings or dialing specific codes on your phone.

---


## Redirect Calls to AI Agent
Once you've configured your call forwarding with your telecom provider, you can streamline your answering services by directing calls to your SeaChat Voice Agent. Your SeaChat agent can help manage appointments and generate call summaries during busy times or when you're unavailable.

The following tutorial will walk you through all the necessary steps to set up your phone number for call forwarding to your SeaChat agents. Once you have successfully set up a call forwarding pipeline, you can visit our [wiki](https://wiki.seasalt.ai/) or check out our tutorial videos on Seasalt.ai’s YouTube channel to further implement different features of SeaChat into your production.

## Preparation Step
Before moving onto the calling forwarding setup, let’s make sure the AI agent is ready for taking the calls.


- **Step 1** – **Create a SeaChat Agent**: 
  - If this is your first time logging into SeaChat, you will need to set a new agent first to continue the following steps. You are welcome to visit our [wiki](https://wiki.seasalt.ai/en/seachat/manual/create-new-agent/) for a more detailed instruction on how to do so.
- **Step 2** – **Deploy the Voice AI agent**: 
  - We need to assign a phone to the voice AI agent, so we can deploy it into production for call answering. Follow the instructions below to complete the step or you can check out our [wiki](https://wiki.seasalt.ai/en/seachat/manual/channels/voicebot/) for a more comprehensive guide – Calls Channel Configuration.
      - ***Step 2.1*** – ***Navigate to the configuration page of Calls***.
        - Go to Channel -> Calls under the Agent Configuration section in the sidebar on the left.
      - ***Step 2.2*** – ***Buy a toll-free number and deploy the AI agent to the number***.
        - Follow the steps on SeaChat UI to purchase a toll-free number that the Ai agent will be deployed to.
        - Configure the AI agent and set up the correct behavior that you want the agent to have.
      - ***Step 2.3*** – ***Test your AI Agent***.
        - You should always test your AI agent before you deploy it to production. Fine-tune and adjust agent’s configuration to achieve the optimal performance that you need.

  


---


#### Android / iPhone

<!-- Source: inbound-voice-agent/call-forwarding-setup/android-and-iphone.md -->

<!-- Weight: 1302 -->

*SeaChat Feature Tutorial | Call Forwarding Setup (Android/iPhone)*


## Check if the preparation step is done

To proceed with the configuration of the call forwarding, we need to make sure that we have deployed a phone number that will be answered by SeaChat AI agents. If you haven't done this, Please check out our [tutorial](https://wiki.seasalt.ai/seachat/inbound-voice-agent/tutorial/) on how to do so.


## Forward your personals calls to SeaChat (Android)
To forward your personal calls to Seasalt.ai, we need to configure both your personal phone and the destined SeaChat AI agent. You can follow the steps below to achieve this:


- **Step 1** – **Configure Call forwarding feature for your phone**:
  - Now we need to configure your number on your device to enable the call forwarding feature. Note that the IOS system has a different configuration in comparison to the Android one. This section will focus on the configuration related to Android devices.
    - ***Step 1.1*** – ***Open the Phone App***.
      - Locate the Phone App on your device. This is usually the app with the phone icon.
    - ***Step 1.2*** – ***Access Call Settings***.
      - Find the Settings option in the Phone App. You can usually find it by clicking on the  Menu icon. Then go to "General" -> "Calling accounts"
      -> select your carrier (such as T-Mobile) -> Call forwarding.
    - ***Step 1.3*** – ***Find and Enable Call Forwarding***.
      - Or you can search for Call Forwarding in Settings. Find keywords, Call Forwarding or Forwarding, in the section. There may be under the names of Calls or Advanced Settings
    - ***Step 1.4*** – ***Enter the number of the AI agent***.
      - Now you should see the following image that allows you to route calls to your AI agent’s number. Input the number in the fields that you wish for the AI agent to take over. For Conditional Forwarding, we will focus on the fields of When busy, When unanswered and When unreachable.
    - ***Step 1.5*** – ***Enter AI numbers in the target fields***.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/en/inbound-voice-agent/call-forwarding/enter-number-android.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seachat/en/inbound-voice-agent/call-forwarding/enter-number-android.png" alt="Android UI for Entering Phone numbers">
</a>

**Enter the Phone Numbers to Forward to**
</center>

- **Step 2** – **Save the Settings**:
  - Once you've entered the SeaChat agent phone number, tap the Save or OK button to save the call forwarding settings. The calls to your Android device will now be redirected to your SeaChat agent.
- **Step 3** – **Test the Call Forwarding**:
  - You should now have a fully functioning call forwarding feature setup to your SeaChat agent. Test it to see if the feature works. If not, review each of the above again to see if something is missing.

## Forward your personal calls to SeaChat (iPhone)
To forward your personal calls to Seasalt.ai, we need to configure both your iPhone and the destined SeaChat AI agent. You can follow the steps below to achieve this:

- **Step 1** – **Configure Call Forwarding on iOS Devices**:  
  This section will guide you through setting up call forwarding specifically on iOS devices, which differs slightly from the Android process.
  - ***Step 1.1*** – ***Open the Settings App***.
    - Locate and open the Settings app on your iPhone. This is where you'll find all your phone's settings, including call forwarding options.
  - ***Step 1.2*** – ***Access Phone Settings***.
    - Scroll down in the Settings app and tap on Phone. This will open the settings related to your device’s calling features.
  - ***Step 1.3*** – ***Find and Enable Call Forwarding***.
    - In the Phone settings, tap on Call Forwarding. Toggle the switch to turn on the feature. Once activated, a field labeled **Forward To** will appear, allowing you to enter the number to which calls should be forwarded.
  - ***Step 1.4*** – ***Enter the AI Agent's Number***.
    - In the **Forward To** field, input the phone number provided by your AI answering service. This will redirect your calls to the AI agent when you are unavailable. If necessary, ensure to include the appropriate country code.
  - ***Step 1.5*** – ***Save the Settings***.
    - After entering the AI agent's number, tap **Back** or **Done** to save your changes. This will confirm that your calls are now being forwarded.

- **Step 2** – **Test the Call Forwarding**:  
  To ensure the call forwarding is set up correctly, test the feature by asking someone to call your phone. If the call is redirected to your AI agent, the process was successful. If not, review the steps to check if any part of the setup is missing or needs adjustment.

The call forwarding feature now redirects your inbound calls to your SeaChat agent when conditional forwarding is set up. Activating this feature may require extra steps, depending on your telecom provider’s policies. We recommend checking with your telecom provider first to find out if there are any additional requirements, such as in-person registration.


---


#### Businesses - US, VoIP, Taiwan, Singapore

<!-- Source: inbound-voice-agent/call-forwarding-setup/business.md -->

<!-- Weight: 1303 -->

*SeaChat Feature Tutorial | Call Forwarding Setup (Businesses - US, VoIP, Taiwan, Singapore)*


## Check if the preparation step is done

To proceed with the configuration of the call forwarding, we need to make sure that we have deployed a phone number that will be answered by SeaChat AI agents. If you haven't done this, Please check out our [tutorial](https://wiki.seasalt.ai/seachat/inbound-voice-agent/tutorial/) on how to do so. 

## Forward your Business calls to SeaChat

Forwarding business calls can be more complex than forwarding personal calls. For specific instructions and proper setup, it's recommended to consult the official documentation or contact customer support for assistance. Please carefully proceed with the instructions below to avoid potential issues.

## US Carriers

### AT&T
- **Unconditional Call Forwarding:**  
  Lift the phone receiver and dial ```*72 ``` (or  ```72# ```), then enter the number you want to forward calls to. For long-distance calls, include 1 + the 10-digit number.  
  For local calls, use just the area code and 7-digit number, or simply the 7-digit number for calls that don't require an area code.  
  Call forwarding is activated when you hear the confirmation tone.
- **No Answer Call Forwarding:**  
  Dial  ```*92 ```, then enter the 10-digit forwarding number and press #. Wait for the confirmation tone.
- **Busy Call Forwarding:**  
  Dial  ```*90 ```, then enter the 10-digit forwarding number and press #. The confirmation tone indicates the activation of call forwarding.
- **Selective Call Forwarding:**  
  Dial  ```*63 ``` and follow prompts to forward specific pre-selected numbers.
- **Turning Off Call Forwarding:**  
  For unconditional forwarding, dial  ```*73# ```.  
  For no-answer forwarding, dial  ```*93# ```.  
  For busy forwarding, dial  ```*91# ```.

### Frontier
- **Unconditional Call Forwarding:**  
  Dial  ```*72 ``` and enter the 10-digit forwarding number. Wait for the phone to be answered and for the confirmation tone.  
  Exceptions: In certain areas (e.g., Indiana, Illinois, Pennsylvania), dial ```72#```. For Connecticut Frontier Voice customers, dial ```72``` followed by the number.
- **No Answer Call Forwarding:**  
  Dial  ```*92 ``` and set the number of rings before forwarding. Then, enter the 10-digit forwarding number.  
  Exceptions: In Seneca Gorham, dial ```52```; in Rochester, dial ```44```. You can also change the ring duration by dialing ```40``` and setting the number of seconds before forwarding.
- **Busy Call Forwarding:**  
  Dial  ```*90 ```, enter the 10-digit number, and press #.  
  Exceptions: In Seneca Gorham, dial ```50```; in Rochester, dial ```48```.
- **Selective Call Forwarding:**  
  Dial  ```*63 ``` and follow the voice instructions to manage your forwarding list.
- **Turning Off Call Forwarding:**  
  Unconditional: Dial  ```*73 ``` and press **Talk**.  
  No Answer: Dial  ```*93 ``` and press **Talk**.  
  Busy: Dial  ```*91 ``` and press **Talk**.

### US Mobile
- **Unconditional Call Forwarding:**  
  On your phone's dial pad, enter ```*72```. Then, input the 10-digit number (including the area code) where you want to forward your calls (e.g., ```*72-908-123-4567```). Tap the Call button and wait for the confirmation tone or message. End your call to activate call forwarding.
- **No Answer Call Forwarding:**  
  On your phone's dial pad, enter ```*71```. Enter the 10-digit forwarding number, including the area code (e.g., ```*71-908-123-4567```). Tap the Call button and wait for the confirmation tone or message. Call forwarding will be activated after confirmation.
- **Busy Call Forwarding:**  
  Similar to No Answer Call Forwarding, on your phone's dial pad, enter ```*71```, followed by the 10-digit number where you want calls forwarded. Tap Call and wait for the confirmation tone. End the call once forwarding is confirmed.
- **Turning Off Call Forwarding:**  
  To cancel any type of call forwarding, dial ```*73``` on your phone. Tap Call, and once you hear the confirmation tone, end the call to deactivate call forwarding.

### T-Mobile
- **Unconditional Call Forwarding:**  
  Dial ```*21``` followed by the 10-digit forwarding number and press the call button. Wait for the activation tone to confirm the setup.
- **No Answer Call Forwarding:**  
  Dial ```*61``` followed by the 10-digit forwarding number and press the call button. The forwarding will activate upon hearing the confirmation tone.
- **Busy Call Forwarding:**  
  Dial ```*67``` followed by the 10-digit forwarding number and press the call button. The call forwarding is activated once you hear the activation tone.
- **Not Reachable Call Forwarding:**  
  Dial ```*62``` followed by the 10-digit forwarding number and press the call button. The call forwarding will be activated once you hear the activation tone.
- **Turning Off Call Forwarding:**  
  Unconditional Call Forwarding: Dial ```##21#```, press the call button, and wait for the confirmation tone to turn off.  
  No Answer Call Forwarding: Dial ```##61#``` and press the call button.  
  Busy Call Forwarding: Dial ```##67#``` and press the call button.  
  Not Reachable Call Forwarding: Dial ```##62#``` and press the call button.  
  All Conditional Call Forwarding: Dial ```##004#``` to disable all conditional call forwarding.

### Comcast (Business)
- **Unconditional Call Forwarding:**  
  Before picking up the receiver or pressing **Talk**, dial ```*72```. Then, dial the 10-digit number you wish to forward calls to. Press **Talk** to activate call forwarding, which will be confirmed by a tone and message.
- **No Answer Call Forwarding:**  
  Before picking up the receiver or pressing **Talk**, dial ```*71```. Then, enter the 10-digit forwarding number and press **Talk.** Call forwarding will activate after the confirmation tone.
- **Busy Call Forwarding:**  
  Dial ```*90``` before picking up the receiver or pressing **Talk**, then enter the 10-digit forwarding number. Press **Talk,** and wait for the confirmation tone.
- **Selective Call Forwarding:**  
  Lift the receiver and dial ```*63```. Follow the voice prompts to select which numbers to forward, and activate after the confirmation code.
- **Turning Off Call Forwarding:**  
  Unconditional Call Forwarding: Dial ```*73```, wait for the confirmation tone, then hang up.  
  No Answer Call Forwarding: Dial ```*93```, wait for the tone, and hang up.  
  Busy Call Forwarding: Dial ```*91```, wait for the confirmation tone, and hang up.  
  Selective Call Forwarding: Dial ```*83```, enter rule details, and save to deactivate.

### Xfinity Mobile (Comcast consumers)
- **Unconditional Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and press ```*72```. Enter the 10-digit forwarding number provided by your answering service. Call forwarding will activate once you hear the confirmation tone.
- **No Answer Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and press ```*92```. Enter the 10-digit forwarding number. The call forwarding will activate after you hear the confirmation code.
- **Busy Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and press ```*90```. Enter the 10-digit number. Call forwarding is activated once the confirmation tone is heard.
- **Selective Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and press ```*63```. Enter the 10-digit number you want to forward. The service will activate once you hear the confirmation tone.
- **Turning Off Call Forwarding:**  
  Unconditional Call Forwarding: Dial ```*73``` to turn off the service. Wait for the confirmation tone.  
  No Answer Call Forwarding: Dial ```*93``` to deactivate. Wait for the confirmation tone.  
  Busy Call Forwarding: Dial ```*91``` to disable. Wait for the confirmation tone.  
  Selective Call Forwarding: Dial ```*83``` and press ```3``` to turn off selective forwarding. Wait for the confirmation tone.

### Verizon
- **Unconditional Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and dial ```*72``` followed by the 10-digit forwarding number (e.g., ```*72-999-555-4567```). Wait for a series of beeps, then the call will automatically end, confirming that call forwarding is active.
- **No Answer Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and dial ```*71``` followed by the 10-digit forwarding number (e.g., ```*71-999-555-4567```). The call will be forwarded if not answered after 3 to 6 rings. Once you hear the beeps, the call will automatically end, confirming activation.
- **Busy Call Forwarding:**  
  Dial ```*71``` and enter the 10-digit number where you want calls to be forwarded if the line is busy. After hearing the beeps, the call will end, activating the feature.
- **Turning Off Call Forwarding:**  
  To turn off call forwarding, dial ```*73```. Wait for the confirmation tone, and the service will be deactivated.

### RingCentral
- **Call Forward for Unreachable Phones:**  
  When your phone is offline, incoming calls are forwarded to another user’s extension or an external number. This can be configured under different call handling rules:
    - User/Business hours
    - After hours
    - Custom answering rules  
      Once the phone service is restored, calls will automatically resume ringing on the original phone.

- **Requirements:**
    - The extension must have at least one desk phone with a DigitalLine assigned.
    - Desktop & Mobile Apps must be disabled in the ring list.
    - PSTN numbers should also be turned off in the ring list.
- **Conditions**:
    - All desk phones tied to the extension must be unreachable for this feature to activate.
    - If forwarding calls to other phones, all forwarding devices must be unreachable for this feature to trigger.
    - Turning on PSTN numbers or Desktop & Mobile Apps in the ring list will prevent this feature from working.
- **Enabling Call Forwarding for Unreachable Phones:**  
  Sign in to your RingCentral online account.
    - ***Non-admin users***:  
      Click Settings in the top menu. Open the Call Handling section and select your call rule (Work-hours, After-hours, or Custom).
    - ***Admin users***:  
      Click Users in the top menu. Select a user from the Users with Extensions list. Open the Call Handling section and select the desired call rule.  
      In the Work Hours tab, click Edit under Call Forward for Unreachable Phone. Toggle on the Call Redirection feature.  
      Choose where you want the calls to be forwarded:
        - Extension
        - Other number
- **Click Save to activate the forwarding rule.**

### Vonage
- **Unconditional Call Forwarding:**
    - Lift the receiver, dial ```*72```, and enter the 10-digit number you wish to forward calls to. Press 1 to confirm, and wait for the confirmation tone.
    - Online Setup: You can also set up call forwarding via your Online Account or the Vonage Enterprise Portal by navigating to the **Summary tab** > **My Numbers** > **Calling Features** > **Call Forwarding** and following the prompts to enter the forwarding number and desired ring duration before forwarding.
- **No Answer Call Forwarding:**
    - Sign in to your Online Account or Vonage Enterprise Portal. Navigate to Calling Features, select Call Forwarding, and set the number of seconds before forwarding. Enter the forwarding number and save the settings.
- **Busy Call Forwarding:**
    - For residential users, sign in to your Online Account, go to Calling Features, and enter the forwarding number. Save the settings.
    - For enterprise users, go to **Voice Settings** > **General** in the Vonage Enterprise Portal to enable busy call forwarding.
- **Selective Call Forwarding:**
    - In the Online Account or Enterprise Portal, navigate to Calling Features, set the conditions for selective forwarding, and enter the forwarding number. Save the settings.

### Google Voice
#### Android:
- **Unconditional Call Forwarding:**  
  Open the Google Voice app on your mobile device. **Tap Menu** > **Settings**, and under Custom Call Forwarding, select Manage rules. Choose the contact whose calls you want to forward, and enter the number where you want calls forwarded. The rule will be applied once saved.
- **No Answer Call Forwarding:**  
  In the Google Voice app, **go to Menu** > **Settings** > **Manage** rules. Set a rule for a specific contact or group, and select the option to forward calls when unanswered. Specify the forwarding number.
- **Busy Call Forwarding:**  
  Access Manage rules in the Google Voice settings. Choose the contact you wish to forward, and create a rule to forward calls when your line is busy. Enter the forwarding number and save the rule.
- **Selective Call Forwarding:**  
  In the Google Voice settings, under Custom Call Forwarding, tap Manage rules. Select a specific contact or contact group to forward their calls to a different number. The rule will activate after saving.
- **Turning Off Call Forwarding:**  
  To turn off custom call forwarding for a specific contact, go to Manage rules in the Google Voice settings. Find the contact or rule you want to disable, and delete or edit the rule accordingly.

#### iPhone/iOS:
- **Unconditional Call Forwarding:**  
  Open the Google Voice app on your mobile device. Tap Menu > Settings, then navigate to Custom Call Forwarding and select Manage rules. Choose a contact or contact group and enter the number you want to forward calls to. The rule will activate once saved.
- **No Answer Call Forwarding:**  
  In the Google Voice app, go to Menu > Settings > Manage rules. Create a rule to forward calls when unanswered and enter the forwarding number. The call forwarding will activate after saving the rule.
- **Busy Call Forwarding:**  
  Access the Google Voice settings under Manage rules. Set a rule for calls to be forwarded when the line is busy. Enter the forwarding number and save the changes.
- **Selective Call Forwarding:**  
  In Google Voice, go to Manage rules under Custom Call Forwarding. Set a rule to forward calls from specific contacts or groups and specify the forwarding number. The service will activate after saving.
- **Turning Off Call Forwarding:**  
  To turn off custom call forwarding for a specific contact or group, go to Manage rules in Google Voice, find the rule you want to disable, and delete or edit the rule.

## Taiwan Carriers
### Chunghwa Telecom
- **Immediate Call Forwarding:**  
  To activate, dial ```*77``` followed by the forwarding number, then hang up.  
  To deactivate, dial ```#77```.
- **Busy Line Call Forwarding:**  
  To activate, dial ```*76``` followed by the forwarding number, then hang up.  
  To deactivate, dial #76.
- **No Answer Call Forwarding:**  
  To activate, dial ```*75``` followed by the forwarding number, then hang up.  
  To deactivate, dial #75.

### Taiwan Mobile
- **Unconditional Call Forwarding:**  
  Forward to a Landline: Dial ```*21``` followed by the area code and phone number, then ```*11#```, and press Send.  
  Forward to a Mobile Phone: Dial ```*21``` followed by the mobile number, then ```*11#```, and press Send.  
  Video Calls Forward to Mobile: Dial ```*21``` followed by the mobile number, then ```*24#```, and press Send.
- **No Answer Call Forwarding:**  
  Forward to a Landline: Dial ```*61``` followed by the area code and phone number, then ```*11#```, and press Send.  
  Forward to a Mobile Phone: Dial ```*61``` followed by the mobile number, then ```*11#```, and press Send.  
  Video Calls Forward to Mobile: Dial ```*61``` followed by the mobile number, then ```*24#```, and press Send.
- **Unavailable Call Forwarding:**  
  Forward to a Landline: Dial ```*62``` followed by the area code and phone number, then ```*11#```, and press Send.  
  Forward to a Mobile Phone: Dial ```*62``` followed by the mobile number, then ```*11#```, and press Send.  
  Video Calls Forward to Mobile: Dial ```*62*``` followed by the mobile number, then ```*24#```, and press Send.
- **Busy Line Call Forwarding:**  
  Forward to a Landline: Dial ```*67*``` followed by the area code and phone number, then ```*11#```, and press Send.  
  Forward to a Mobile Phone: Dial ```*67``` followed by the mobile number, then ```*11#```, and press Send.  
  Video Calls Forward to Mobile: Dial ```*67``` followed by the mobile number, then ```*24#```, and press Send.
- **Cancel Call Forwarding:**  
  To cancel individual forwarding settings, dial ## followed by the specific service code (21/61/62/67) and #, then press Send.  
  To cancel all call forwarding, dial ##002# and press Send.

## Singapore Carriers
### Singtel
- **Unconditional Call Transfer:**  
  Lift the handset, wait for the dial tone, and dial ```#210YYYYYYYY#```, where ```YYYYYYYY``` is the number you want calls to be forwarded to. Wait for the repeated tone and hang up. Your call transfer is now activated.
- **Cancel Unconditional Call Transfer:**  
  Lift the handset, wait for the dial tone, and dial ```#211#```. Wait for the repeated tone and hang up.
- **Call Transfer When No Reply:**  
  Lift the handset, wait for the dial tone, and dial ```#220YYYYYYYY#``` where ```YYYYYYYY``` is the number to forward calls when there’s no reply. Wait for the repeated tone and hang up.
- **Cancel Call Transfer When No Reply:**  
  Lift the handset, wait for the dial tone, and dial ```#221#```. Wait for the repeated tone and hang up.
- **Call Transfer When Busy:**  
  Lift the handset, wait for the dial tone, and dial ```#230YYYYYYYY#``` where ```YYYYYYYY``` is the number to forward calls when your line is busy. Wait for the repeated tone and hang up.
- **Cancel Call Transfer When Busy:**  
  Lift the handset, wait for the dial tone, and dial ```#231#```. Wait for the repeated tone and hang up.




---


### Prompt Examples

<!-- Source: seachat-resources/prompt-examples.md -->

<!-- Weight: 1500 -->

*Explore prompt examples to train SeaChat AI agents, optimizing responses with our practical examples.*


## Overview

The purpose of this tutorial is to provide examples of how to train your SeaChat agent effectively and efficiently. Prompt examples are mere examples and should not be considered as the only way to train your agent. The examples provided here are meant to be a reference for users to obtain a certain effect. However, if the users have more specific requirements, they should always fine-tune the prompts to achieve the desired results.

## Limiting Bot Answers within Defined Scenarios

You can provide defined scenarios to limit the AI agent's answers. A good way to do so is to list the scenarios and elaborate on them.


Prompt examples:
```markdown

You are an assistant at {company_name}’s customer service. 

Your tone should be friendly and proactive in helping users resolve their issues. 

Use casual language and avoid repeating the same sentences. Instead, use diverse and lively expressions. 

For user queries, follow this process:

Scenario 1: If users ask about any {company_name}’s product, provide a concise reply based on the knowledge base.

Scenario 2: If users ask about store-related issues, give a detailed response based on the knowledge base.

Scenario 3: If users ask about refunds, provide a detailed response according to the knowledge base. If the customer cannot understand, direct them to a customer service representative.

Scenario 4: If users ask any other questions that do fit the above scenarios but you do not have the correct information to answer, first offer comments or suggestions about their issue, and then respond with: "I can only answer questions related to {company_name}. If you have other issues, please contact the company at {company_number}."

```

---


### SeaChat API

<!-- Source: seachat-resources/seachat-api.md -->

<!-- Weight: 1501 -->

*Integrate and automate AI agent workflows with SeaChat's RESTful API, detailed in our API documentation.*


SeaChat RESTful API allows users to integrate and automate AI agent workflows, providing the flexibility to manage AI agents programmatically. You are welcome to check out the [API documentation](https://wiki.seasalt.ai/seasaltapi/seasalt-api/01-seachat-api-intro/) for detailed information and guidance for seamless integration.

---


### SeaChat FAQ

<!-- Source: seachat-resources/seachat-faq.md -->

<!-- Weight: 1502 -->

*Frequently asked questions about SeaChat. Find answers to common queries about SeaChat's features, channels, and more.*


## 1. **How do I change the password for my Seasalt products?**

All Seasalt products use the same password management mechanism. We only support logging in by sending a login code via email each time you log in, and we do not have a password change feature.

This approach helps prevent you from forgetting your password or inadvertently sharing it. To log in to any Seasalt product, simply enter your login email, and you will receive a login code. Use this code to log in.

## 2. **The LINE button cuts the messages short. How do I display the full message?**

When users are using the LINE channel with SeaChat, they may encounter issues where the message is cut off after clicking the message button for more information. This is due to the character limit for LINE button messages.

SeaChat provides a solution for this issue. Utilize the KB ID feature to avoid the message being cut off. Learn more about how the [KB ID](https://wiki.seasalt.ai/en/seachat/manual/add-knowledge/webpage-link/#kb-ids) feature works to prevent messages from being truncated.

Please check out our wiki about the [LINE Channel](http://wiki.seasalt.ai/seachat/seachat-manual/04-channels/05-install-to-line/#limits-of-line-button-messages) for more information on the message limits imposed by LINE.

## 3. **How do I attract more chats once SeaChat is deployed?**

To attract more users, you can do 2 things:
1. make the widget icon a GIF
2. add a bubble to popup after 2 seconds or some other time if user hasn't clicked


<div style="display: flex; flex-direction: column; align-items: center;">
<div style="width: 100%; text-align: center; display: flex; flex-direction: column; align-items: center; justify-item: center">
    <a href="/images/seachat/en/seachat-resources/seachat-bubble-with-gif.gif" target="_blank">
    <img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/seachat-resources/seachat-bubble-with-gif.gif" alt="SeaChat uses bubble and gif to attract more users">
    </a>
</div>
    <p style="margin-top: 20px; font-size: 15px">SeaChat uses bubble and gif to attract more users</p>
</div>

Bubble config can be found in Channels --> Webchat --> Bubble (first tab)



---


### SeaChat Release History

<!-- Source: seachat-product-updates/seachat-product-updates.md -->

<!-- Weight: 1600 -->

*Stay up-to-date with SeaChat's latest release on new AI features, improvements, and bug fixes.*

### 08/07/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Users of Meta apps (Messenger, Instagram, WhatsApp) can now add reactions to messages from live agents and bots, and our UI will display these reactions.
- When starting a conversation in Webchat or the Widget, the first user message will have an opacity effect to enhance the user experience and indicate that the conversation is loading.
- A new CSAT section has been added to the SeaChat Analytics page, allowing you to view ratings within the selected time range and download all customer feedback from that period.
- New Japanese and Indonesian voice options are now available for Twilio integration and SeaX phone integration

### 7/24/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Adjusted AI assistant response behavior on Instagram and Messenger: When users react to your Instagram Story, it no longer triggers AI assistant replies.
- Optimized the backend customer service online status switching functionality in SeaChat, making it more real-time and responsive.
- Added live agent transfer functionality to SeaX phone integration: When a SeaX phone number is set up and the SeaChat AI assistant is enabled, users can now transfer to live agents during SeaX phone calls.

### 7/17/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Fixed an issue where images sent by Messenger users could not be displayed properly.
- Fixed an issue where empty summary titles were still displayed on Messenger and Instagram when the transfer summary feature was not enabled.

### 7/10/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Workspaces page now mobile responsive: You can now access your workspace on your mobile devices and manage conversations.
- Adjusted AI agent behavior for Instagram and Messenger: When a user reacts to an AI agent's message on Instagram or Messenger, it no longer triggers AI agent reply. It’s the first step, with more optimizations and feature improvements coming soon.

### 7/3/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Image upload limit introduced: To ensure the AI agent can accurately interpret images and provide a better conversation experience, users can now upload up to 20 images per message.
- LINE integration update: When your LINE message quota is used up, an automated email notification will be sent to the workspace owner as a reminder.
- Multi-image message handling fixed: Messages from Messenger and Instagram that contain multiple images are now consolidated into a single message, ensuring all images are correctly identified and understood by the AI agent.

### 6/26/2025
##### **<font color="#739963">New Features and Improvements</font>**
- “Deploy” Button for Easier Channel Integration: A new Deploy button has been added to the header, providing quick access to all supported platforms, channels, and website integrations. User can navigate to relevant setup pages and deploy their AI agent across desired communication platforms
- New Multi-Image Message Interface: All images within a single message will now be presented in this new design. This update improves both the visual clarity of the conversation context and the performance of sending multiple images efficiently.
- Improved Stability for Knowledge Base Article Upload: Resolved several issues affecting the stability of knowledge base article uploads.

### 6/19/2025
##### **<font color="#739963">New Features and Improvements</font>**
- Improved CSAT Result Display: Users can now view CSAT (Customer Satisfaction) ratings and comments directly within the conversation window.
- Sign-in Email Validation Fixed: Resolved an issue where SeaChat sign-in incorrectly flagged valid email formats as invalid.
- Billing Page Error Resolved: Fixed error code 10002 where newly registered users saw a "paid user not found" account error on the billing page.
- Twilio Phone Number Purchase Bug Fixed: Addressed an issue preventing users from purchasing phone numbers through Twilio.

### 6/12/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Custom CSAT Form for Widget Installations: You can now attach a CSAT (Customer Satisfaction) form to your SeaChat widget. When users interact via the widget, the form can automatically pop up, and you’ll be able to view feedback linked to each conversation directly from your dashboard. See tutorial [here](/en/seachat/manual/channels/webpage/#custom-forms-csat-survey-form).
- Multiple Image Support in WebChat: SeaChat now supports sending multiple images in a single message when your customers chat with your AI agent. SeaChat AI agent will now comprehensively understand all images together—enabling more contextual and accurate responses, instead of processing them one by one.
- Improved Time Awareness Accuracy: Fixed an issue where the AI agent, when time awareness was enabled, failed to provide the correct localized time.
- LINE Formatting Fix: Resolved a bug where messages sent by the AI agent to LINE always had an unnecessary leading whitespace before each sentence.

### 6/5/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Instagram Login with OAuth: Streamlined authentication process allowing you to easily sign in and connect your Instagram account with your SeaChat AI agent. See tutorial [here](/en/seachat/manual/channels/instagram/).
- Enhanced Image Upload Capacity: Maximum image upload size increased to 20MB for human agent conversations, enabling more flexibility in sharing visual content with customers.

### 6/1/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Auto-Labeling Refined: Fixed behavior where auto-labeling incorrectly replaced labels instead of patching them. With this update, labels are now correctly patched—allowing multiple labels to coexist without overwriting each other.
- GA4 Customization Support: You can now add your GA4 Measurement ID directly in the Agent Information tab → Design Style page → Chat Settings section. Once set, SeaChat will begin sending widget interaction data (like message sends, button clicks, and agent handovers) to your GA4 property—allowing for detailed user behavior insights and performance monitoring.
- Live Agent Transfer Options: We updates the options for live agent transfer so users can customize how live agent handovers are triggered. Users can now choose between user requests via button clicks, intent expressed during conversations with the AI agent, or both.
- Conversation Image Upload Size Limit Increased: We’ve raised the maximum image upload size to 20 MB. You can now upload images up to this size in your conversations, making it easier to share clearer, higher-quality visuals.

### 5/22/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Live Agent Transfer Enhancement: Added seamless live agent transfer functionality in chat. When enabled, customer messages to the AI agent will be smoothly transferred to a human agent.
- Webchat Card Improvements: Added support for inbound message cards in Webchat. When users click these cards, the system sends a predefined question to your AI agent, initiating a conversation automatically.
- LINE Message Template Enhancement: Improved LINE template message handling by sending quick action buttons as a separate text message, ensuring button visibility throughout the conversation.

### 5/15/2025

##### **<font color="#739963">New Features and Improvements</font>**
- Better document knowledge base upload handling: Fixed the bug that caused server timeout when uploading large documents. Now users can upload large documents and the system will process the upload as a background process, while users can work on something else.
- Messenger integration with FB embedded signup: We support FB embedded signup, and users can sign up with their FB account directly and choose which FB page to connect with their SeaChat AI agent. See tutorial [here](/en/seachat/manual/channels/facebook-messenger-embedded-signup/).

### 5/8/2025

##### **<font color="#739963">New Features and Improvements</font>**
- Added multilanguage support in Billing page cost breakdown for the next bill.

### 5/1/2025

##### **<font color="#739963">New Features and Improvements</font>**
- Messenger Conversation Title Enhancement: Fixed an issue where sender names were not being captured in Messenger conversation titles. Now, conversation titles from Messenger are automatically updated to include the sender's name, making conversations more identifiable and easier to manage.
- Expanded AI agent Description Limit: Increased the character limit for AI agent descriptions based on different language models. Users can now provide more comprehensive descriptions of AI agent functionalities.
- Voice Conversation Recording Download Fix: Resolved the issue with downloading voice conversation recordings, ensuring users can successfully access their voice conversation records.

### 4/24/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Extraction Enhancement: We have optimized the `Extraction` feature, enabling AI agents to more accurately identify and extract key information from user conversations.
- Google Calendar Timezone Fix: Fixed the default timezone setting issue in Google Calendar integration. The system now correctly identifies and uses the user's browser timezone, preventing AI agent from stop responding issues previously caused by incorrect timezone codes.

### 4/16/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Human Agent-Only Mode Enhancement: The automatic switch to AI agents is now disabled in human agent-only mode, ensuring that human agents have sufficient time to address customer inquiries without interruption.
- Mobile Widget Display Optimization: Improved the display logic for mobile widgets, ensuring that only one widget icon is visible on mobile devices when a single widget is configured.

### 4/9/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Enhanced References feature: When users enable the References feature in the Advanced Settings page and have configured the Zendesk ticket search tool, if the AI agent's response includes content from Zendesk tickets, the system will display the relevant ticket numbers and titles in the references area, making it easier to track information sources.

### 4/1/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Knowledge Base Refinement: Users can now configure whether to refine knowledge base search results and customize instructions for the LLM in the Agent Information's Advanced Settings page on how to optimize these results, enhancing AI agent performance when answering user queries. See [tutorial](/en/seachat/manual/create-agent/advanced-settings/rag/#knowledge-base-search-refinement).

### 3/20/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Webchat Widget Bubble Feature: Users can now add an attention-grabbing bubble near the webchat widget to make it more visually prominent and appealing. This feature can be configured in the webchat widget settings page.

### 3/13/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Email Format Validation: An email format validation is added in webchat forms to ensure customers provide correct email addresses.
- Enhanced Call End Feature: When a voice conversation is in progress, the button in the upper right corner of the conversation detail window will function as an end call button, allowing users to terminate ongoing calls with a single click.

### 3/5/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Improved Mobile Experience: Fixed conversation page styles on mobile to ensure users can conveniently view conversations and reply to customers.
- Google Calendar Integration Update: Setting up Google Calendar integration now automatically enables Time Awareness in the AI agent’s Advanced Settings, using the selected timezone.

### 2/26/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Evaluation Test Set Import & Export: Users can now export evaluation test sets to a JSON file, allowing for easier backup and editing. Additionally, users can import test set data by uploading a JSON file, enabling bulk management of test sets more efficiently. See [tutorial](/seachat/seachat-manual/07-test-and-improve-ai-agent/evaluation/#4-importing-and-exporting-evaluation-test-sets)
- Email Notifications for Assigned Conversations: When a conversation is assigned to a human agent, the system will now automatically send an email notification to that agent to promptly inform the agent.
- Configurable Auto-Hangup for Voice Calls: Users can now configure whether they want to enable automatic hangups for voice calls when a caller says phrases like "goodbye" or expresses an intent to leave.

### 2/19/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Evaluation Testing: Users can now assess AI agent responses by providing test sets, each containing a user query, a gold response, and optional conversation history. The AI agent’s response is compared against the gold response, with results displaying overall correctness and individual sample accuracy. Users can refine their AI agent and run evaluations to continuously improve performance.
- Conversation Label Editing: Users can now create, edit, and delete chat labels directly from the Labels page.
- Knowledge Base (KB) Export: Users can now export all KB entries by going to Knowledge Based → Existing → View All and choose Export to CSV or JSON via the corresponding option. Files can be updated and re-uploaded through "Upload from Template File".

### 2/13/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Pre-Fill Contact Forms: SeaChat now auto-fills webchat forms using query strings in the URL, eliminating manual entry. See [tutorial](/en/seachat/seachat-integrations/seachat-prefill-contact-forms/)
- Fix for Empty Instagram Conversations: Prevents false alerts from thumbs-up reactions and story mentions.
- Improved WebChat UI: When open, the widget now shows a close icon instead of the logo for better clarity.

### 2/6/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Items Per Page Selector in Pagination for Bulk Actions: A dropdown has been added to pagination, allowing you to choose how many items to display per page.
- Knowledge Base Sort By Title: You can now search KB articles by title. Additionally, click the sort icon to organize articles in ascending order.
- Quick Customer Calling: A new **Call Customer** button is available in the upper right corner of the conversation detail window. If a customer called in via the voice channel, you can now quickly call them back.
- Updated Conversation History File Name Formats: Downloaded conversation history files now follow a structured format:`Conversation Title – Conversation Start Datetime – Channel.csv`.

### 1/16/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Channel-Specific Language Support: SeaChat now supports defining the language for voice messages on a per-channel basis. This enables the platform to transcribe voice messages into text and reply in the same language. This setting allows users to tailor communication to meet the needs of different language-speaking audiences across various platforms, including LINE, WhatsApp, Messenger, and Instagram. The setting also applies to system messages, such as the one sent to users when they click 🧹 "New Topic."
- Voice Call Widget Added: A voice call widget has been added to the chat widget. Users can either embed HTML code or a URL to a form to receive customers’ calls. When customers click the call icon, an iframe containing your embedded HTML will pop up, or they will be redirected to your specified form if a URL is provided.

### 1/9/2025

##### **<font color="#739963">New Features and Improvements</font>**

- Transcribe Voice Messages from WhatsApp and LINE: SeaChat AI Agent now supports transcription of audio messages sent via WhatsApp and LINE. When your customers send a voice message, SeaChat will transcribe it, enabling your AI Agent to understand and respond accurately to their inquiries.
- New Custom GPT Tool: Zendesk Ticket Search: We’ve added a new Zendesk Ticket Search tool to the Custom GPT Tool library. You can provide your Zendesk account information to enable SeaChat to fetch ticket details and comments, allowing SeaChat to answer user queries based on relevant tickets.
- Input Box Detect Input Language: SeaChat now supports automatic language detection in the agent's typing input box and the webchat input box for customers. Whether it's a Right-to-Left (RTL) or Left-to-Right (LTR) language, the input is handled automatically.

### 12/26/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Instagram Widget: Users can now add an Instagram widget to their website by simply entering the Instagram link and copying the automatically generated HTML code snippet in Channels to embed it seamlessly.
- Customizable Webchat Menu: Users can now choose to remove the "Get SeaChat" link from the menu dropdown in the webchat's upper-right corner. This option is available in the Design Style section of the Agent Information tab.
- Real-Time Auto-Labeling Updates: We’ve fixed an issue where the UI did not update in real time when labels were automatically applied or removed from conversations using the auto-labeling feature. Now, label changes are reflected immediately in the UI.

### 12/19/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Auto-labeling: SeaChat can now automatically add or remove labels from conversations based on the content of the discussion. Users can define trigger conditions, provide detailed descriptions for accuracy, and select the labels to be managed.
- Label Automations: Users can configure actions that will automatically triggered by label changes within conversations. Users can define which labels should activate these actions and configure one or more automations to streamline workflows and improve efficiency. SeaChat will execute the predefined actions automatically whenever a label is applied or removed.
- Instagram integration: SeaChat now supports Instagram integration, allowing users to connect their Instagram accounts and manage messages directly within the platform.

### 12/11/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Custom GPT Tool Limit: Users can now create more than five custom GPT tools. However, only up to five tools can be enabled at any given time. If users attempt to create a new tool after reaching this limit, the tool will be successfully created but automatically disabled. To enable it, user will need to delete or disable one of the currently enabled tools.
- View and Manage Long-Term Memory: Users can now view user long-term memory by right-clicking on any conversation and selecting the 'User Memory' option. To make this option available, the 'User Memory' feature must first be enabled in Advanced Settings.
- Agent Email Visibility Update: Live agents' emails will no longer be displayed in webchat. Instead, only the agent's name will be shown. Live agents can customize the name displayed to customer via their profile settings in SeaChat.

##### **<font color="#d66a60">Bugfix</font>**

- Conversation History Download: We have resolved an issue with generating conversation history download links. Users can now successfully download their conversation history.

### 11/27/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Expanded Language Support: We now support more languages in the webchat widget, including English, Spanish, French, Japanese, Korean, Russian, Portuguese, Polish, Simplified Chinese, and Traditional Chinese. Configurable messages in the widget are automatically translated based on the selected language. Users can still customize these messages if needed.
- Enhanced Automated Actions with Custom GPT Tools: Two new custom GPT tools have been added - Send Email and Send SMS. These tools enable SeaChat to intelligently decide when to send emails or SMS messages based on your instructions.
- Long-Term User Memory: SeaChat now offers long-term memory for AI agents, enabling them to retain key information about customers, such as preferences, past questions, and interests. When users return, even after a long time, AI agents can recall this information.
- Improved Conversation Keyword Search: The conversation keyword search now includes conversation titles, allowing users to search by title for more comprehensive and accurate results.

### 11/21/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Preferred and Enforced Response Languages: Users can now specify the language SeaChat should use in responses. With the preferred response language setting, SeaChat detects the user's language and responds accordingly, defaulting to the selected language if it cannot determine the user's language. With the enforced response language setting, SeaChat consistently responds in the selected language regardless of the user's input.
- Hybrid Conversation Handling Mode: In Hybrid mode, users can now configure whether to allow customers to proactively request a live agent. If enabled, customers will see a "Talk to Human Agent" button in webchat or a quick action button in WhatsApp, Messenger, and LINE.
- Complete Form Message Configuration: Users can now configure the message sent after a user completes a form, such as "I agree to the Privacy Policy I just submitted." in Webchat Widget Custom Form page.
- Voice Bot Filler Word Configuration: Users can now enable filler words in the voice bot for faster responses and adjust the probability of including filler words in its replies in Calls integration page and SeaX Calls integration page.

### 11/14/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Button Display Limits on Messenger and WhatsApp: We've resolved an issue where exceeding the platform button limits on Messenger and WhatsApp caused display issues. Now, if the button count exceeds the limit, we will display only the maximum allowable number of buttons.
- Free Welcome Message and User Form: The welcome message and user form completion no longer count toward the monthly message quota. They are free.
- Enhanced Conversation Handling Mode Compatibility: Conversation Handling Mode now functions seamlessly across LINE, Messenger, and WhatsApp, besides Webchat. When you switch from any mode to Human Agent Only mode, all customer messages will be sent directly to your live agent. When switching to AI Agent Only mode, customer messages will be handled exclusively by your AI bot. Switching to Hybrid mode keeps the current conversation status unchanged, but your customers can change interaction modes by requesting to return to the AI agent or transfer to a human agent.

### 11/07/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Custom GPT Tools Result Display Options: Users can now select how results from custom GPT tools appear in webchat — either displayed in cards or as plain text in the Edit Custom GPT Tools page.
- New SeaChat Conversation Handling Mode: Users can choose how chats with customers are managed, the three modes are:
  - Hybrid Mode: The AI agent handles interactions initially, but users can request a live agent transfer when needed.
  - AI Agent Only: The AI agent independently manages all chats.
  - Human Agent Only: Human agents handle all conversations exclusively, and this mode is LIFE-TIME FREE.
- Updated Webchat Menu Card Behavior for Text Messages: When users click on a menu card, the card name will be sent as a message from the user, and the bot will respond with the complete canned message stored within the card. The behavior for cards with URLs remains unchanged.

### 10/31/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Automate Actions with Custom GPT Tools: This new feature enables the SeaChat AI agent to query a user’s API endpoint and perform custom actions based on defined conditions. GPT will trigger these actions automatically at the right time.
- "Memory" Renamed to "Extraction": The "Memory" feature in the AI agent's Advanced Settings page is now called "Extraction," with no changes to its functionality.
- Enhanced Workspace List for Better Quota Management: Users will now see their workspace dashboard showing two lists of workspaces. One is Active Workspaces, which shows the number of workspaces created by the user (first number) and the workspace limit allowed under the user's plan (second number). The other is Joined Workspaces, which displays workspaces owned by other users that the current user has joined.

### 10/17/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Display Unread Conversation Count: Users will now see two distinct notifications in the conversation tab and they can hover over each conversation count to understand its purpose. The left number shows the total unread messages. The right number displays unread messages assigned specifically to the user, ensuring agents can easily identify their responsibilities at a glance.
- Enhanced AI Understanding with Postback Button Content: Your AI agent will now have access to the content of buttons clicked by your customers. This ensures that the AI agent can accurately respond to follow-up queries.
- Improved Customization Options for Webchat Forms and Menu Cards: Users can now customize the text display in the submit button in custom forms. Users also have options to enable menu cards to be always-on. Additionally, menu cards support sending a text to AI agent on click besides redirecting to an URL, and there’s now an option to remove pictures for menu cards.

### 10/15/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Enhanced Upload Progress Indicator: We’ve improved the UI by adding upload progress indicators, allowing users to see exactly which URL or sitemap is being processed in real-time.
- SeaChat Widget and Mobile Layout Enhancements: When users click the webchat widget icon, the AI agent's webchat will now open in full screen within the current tab. Additionally, layout issues on mobile screens have been resolved, ensuring the webchat is fully displayed in full screen on users’ phones.

### 10/03/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Human-Agent Assignment: This feature introduces a streamlined interface that allows users to easily assign human agents to respond to customers. Additionally, a new filter has been added to help users quickly locate conversations that have been assigned to them.
- Billing Usage Page Enhancements: The Billing -> Usage page has been upgraded. Users can now see the model and usage information for text and voice messages.
- Conversation Title Consistency: The conversation title now consistently aligns with the user’s full name, ensuring greater accuracy in how conversations are displayed.
- Messenger Interaction Flow: It has been improved to ensure that a quick reply is sent after every message, resulting in smoother and more efficient communication.

### 09/27/2024

##### **<font color="#739963">New Features and Improvements</font>**

- AI Agent Time Awareness: For every message, the AI agent will now be aware of the current time, such as: "The current time is 9:41 AM, September 11, 2024, Wednesday, PST timezone." This allows the AI agent to respond more accurately to user queries about business hours and other time-related questions.
- SeaX Integration Page Redesign: The SeaX integration page has been redesigned to enhance the user experience.

##### **<font color="#d66a60">Bugfix</font>**

- Webchat Icon Clickability: Fixed an issue where the webchat widget installation code caused the webchat icon to be unclickable.

### 09/20/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Language Support: Added additional language support, including French, expanding the localization capabilities of SeaChat. This update enhances user experience for multi-language environments.
- Annual Payment Plan: Users can subscribe to a newly introduced annual payment plan, providing more flexible billing choices and the ability to save on long-term commitments.
- Export Conversation History: Users can now export their conversation history data for their own analytics or admin management purposes, offering more control over their communication data and insights.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed Messenger Live Agent Transfer Issue: Resolved an issue with the Facebook Messenger live agent transfer quick reply button functionality, ensuring smooth transitions between AI and human agent responses.

### 09/11/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Messenger Cards Support : You can now enhance user interactions on Messenger with buttons featuring canned messages and cards with images and buttons, offering a richer, more dynamic experience for your audience.
- Image Support Across Platforms: SeaChat Webchat, WhatsApp, and LINE integrations now support sending and receiving images, enabling more visual and engaging communication across all platforms.
- Analytics Page: Our new Analytics page is now available to all users. Easily track your AI agent’s activities and gain deeper insights into performance and interactions.
- Email Preferences for Human Agents: Human agents can now configure their email preferences to receive email notifications, ensuring a more customized and efficient workflow.

### 09/04/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Enhanced Knowledge Base Search: The search functionality for existing knowledge base articles now uses the same strategy as RAG search method, improving search accuracy and efficiency.
- Support for WebP Format: You can now upload WebP format images to use as icons, allowing for more flexible image options.
- Google Calendar Integration: Users can now select which Google Calendar to book appointments, providing more control over scheduling.
- Customizable Webchat Widget Icon: You can now personalize your webchat widget by uploading any image as the widget icon, giving you more customization options.
- Simplified Webchat Widget Installation: The webchat widget installation code block has been updated in all integrations page. You can now easily copy and paste one code block to install multiple widgets to your integration channels.

### 08/28/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Message Quota Management: Users can now set specific quotas in the Advanced Settings page for the number of chat and voice messages an AI agent can send.
- Enhanced SeaX Calls Integration Page: Features improved control over call speed and voicemail settings.
- Updated UI with New Tabs Style: Streamlined navigation with a fresh tabs design, enhancing user interface interaction.
- LINE Live Agent Message Cap Notification: Notifications are now sent in SeaChat when the message sent by live agent through SeaChat to LINE approaches LINE’s limit.
- Increased Character Limit for Agent Descriptions: Agent descriptions can now include up to 3000 characters, allowing for more detailed explanations.
- Simplified Onboarding Process: New users can build their first knowledgeable AI agent by uploading just a small file or a website URL.

### 08/21/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Easily Copy KB ID: Now you can quickly copy the Knowledge Base ID from file’s right menu and use it as button content.
- Enforced Memory Fields Character Limit: Memory fields now have a strict character limit of 1024.
- Knowledge Base Quota Page: Introducing Quota page for knowledge base that helps you track and optimize your document and token usage efficiently.
- Updated Tab Styles: Enjoy a refreshed look with brand-new tab styles for a more intuitive and modern interface.

##### **<font color="#d66a60">Bugfix</font>**

- Correct Chat Participant Names in Emails: Fixed an issue where a random value was shown instead of the correct chat participant’s name in the "New message received" email.

### 08/15/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Easy Agent Replacement: The new one-click feature in the agent management page simplifies version control and agent duplication, making the process more convenient.
- Improved Test AI Agent Access: The 'Test AI Agent' button has been relocated to the header for easier and more convenient access.
- Expanded Context Window: Open a 128K context window for advanced large language models such as GPT-4o, GPT-4o mini, and Mistral Large.
- Enhanced Button Content Management: Use the `$KB_ID_` header and KB document IDs as button content for streamlined access to knowledge base articles directly through button interactions.

### 08/08/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Introduced a Card-Style Agent Listing Page: Experience our newly designed layout for a more visual and organized way to browse agents.
- Added Model Switching Capability: Users can now switch between different large language models, including GPT-4o mini, GPT-4o, and Mistral Large, directly from the interface.
- Customizable Automatic Transfer Back to AI Agent: Automate the transfer back to the AI agent after a customizable minutes of inactivity from a live agent.
- Customizable "Live Agent Has Left the Conversation" Message: User can design the message that appears when a live agent exits the chat.
- Enabled Customization of Live Agent Transfer Phrases: Allow users to set specific phrases that trigger the seamless transfer of a conversation from the AI agent to a live agent.

### 08/01/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Enhanced Widget Installation: Easily install multiple widgets for SeaChat AI Agent web chat, LINE, WhatsApp, and Messenger on your website by simply copying and pasting one code snippet.
- Improved Popup Window: Experience a more user-friendly popup window that helps you easily track when hit Knowledge Base quota limit.
- Enhanced Browser Notifications: New notifications on the browser tab make unread messages more noticeable.
- Advanced Twilio Call Settings: Configure speed adjustments for both inbound and outbound calls, with options for outbound voicemail to either send a customizable voicemail message or automatically hang up.

### 07/25/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Knowledge base limitations: Upload limits are now tailored to specific plans, including restrictions on file size, file count, and token count.
- Improved Plan Downgrade Process: Users receive notifications advising them to remove excess agents, files, and workspace members. This allows for necessary cleanup before the downgrade takes effect.

### 07/19/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Added support for playing and downloading audio recordings
- Premium Plan Feature: Option to enable Memory is only available for Premium Plan
- Premium Features Tips: New tips for managing multiple premium features, including adding additional members, AI agents, workspaces, memory, and setting up voice agents
- Plain text URLs are now clickable in webchat

### 07/11/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Create workspace automatically when onboarding new users
- Allow Premium plan to hide Seasalt.ai SeaChat branding message in Agent design styles

### 07/04/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Agent list page: To make the screen consistent, only display the first row of prompts.
- SeaChat landing page now supports Portuguese, Korean, Russian, Spanish, and Vietnamese.
- Added a new TTS voice for Chinese: Tongtong voice.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed AI Agent design style cannot be saved bug.

### 06/26/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Now users can create workspace in one click
- Label conversations with channel icon
- Improve the UI of Table upload options
- The number of free messages in the free plan has been revised to 100 messages life-time usage

### 06/13/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Supports LINE card messages and button messages, enriching your conversations.
- Enhanced User Experience: Improved behavior of adding buttons to lists.
- Message Response Support: Supports URL and Markdown formats.

### 06/06/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Interface Adjustment: Added design styles to AI Agent information, allowing you to better design the dialogue interface.
- New WordPress Integration: You can now deploy your AI Agent on WordPress.
- New MailerLite Integration: You can now sync contact information to MailerLite integration.
- New Integration Pages and Channel Design: Offers new integration options and improved channel designs.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed Several Knowledge Base Errors: Including issues with deleting knowledge bases and document error messages.

### 05/30/2024

##### **<font color="#739963">New Features and Improvements</font>**

- Knowledge Base Files: Now you can directly overwrite files with duplicate names, making it easier to update documents.
- New Refresh Button for Chat Window: You can click the button to refresh the chat window when WebSocket is disconnected.

##### **<font color="#d66a60">Bugfix</font>**

- Bug Fixes in Workspace Creation: Errors encountered during workspace creation have been resolved.

### 05/24/2024

##### **<font color="#739963">New Features and Performance Improvements</font>**

- Database Update: Improved file naming in the database for better visibility of documents.
- Automatic Overwrite: When uploading files with duplicate names, you have the option to overwrite the existing files for updates.
- Optimized Database Switching: Enhanced the fluidity of switching databases.
- Customer Service Access: We have added a customer service portal on the left side of our service interface. If you have any questions, you can contact us anytime. Providing the best experience is our greatest motivation.
- Email Template Modification: For SeaChat emails, we've modified the email templates to simplify how you view your emails.

### 05/18/2024

##### **<font color="#739963">New Features</font>**

- Added mail language settings to make email notifications more readable (now you can receive chat email notifications from `seachat@seasalt.ai`).
- Introduced RAG (Retrieval-Augmented Generation) with new query modes, retrieval methods, and retrieval counts to enhance data retrieval and AI assistant response accuracy.
- Added automatic clearing of Memory information when a user clears a conversation.

##### **<font color="#739963">New Features</font>**

- Fixed issues with uploading CSV and Excel files, addressing upload failures and blank screen problems.
- Repaired missing Knowledge Base data and related answers.
- Fixed issues with reply messages containing broken links.
- Corrected strings and updated the use-case library.

### 05/02/2024

##### **<font color="#739963">New Features</font>**

- Upload Table Optimization: On the upload table page, users can now choose whether to upload each row in a table file as an individual Knowledge Base document or as a single file.
- Added Wix Channel: You can now deploy your Agent on Wix.
- Database Enhancement: Restructured Knowledge Base data for optimized data retrieval and interpretation.
- Interface Optimization for Shopify and Squarespace Channels: Enhanced user interface for more streamlined operations for these integrations.
- Automatically fill out bot description for the Survey use case.
- Fixed Live Agent Transfer Behavior in the Survey use case.

### 04/19/2024

##### **<font color="#739963">New Features</font>**

- Added Use Case Library Page: Makes it easier for you to create AI Agents efficiently.
- Access to customer email information: You can now quickly copy customer emails directly from the conversation history list.
- Updated WhatsApp/Messenger Setup Token Process: Improve the channel binding experience.
- Introduced "Memory": Records key information from historical conversations. Paired with the Survey Use Case, it helps you research user needs and characteristics through dialogue.

### 04/09/2024

##### **<font color="#739963">New Features</font>**

- Added `remove` button for WhatsApp and Meta Facebook Messenger channels, allowing users to unlink accounts easily.
- Display the end user's email upon completing the form, enhancing user tracking and engagement.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed an error in the process of creating agents, streamlining agent creation.
- Resolved bugs related to editing agents, ensuring smoother modifications and updates.

### 04/02/2024

##### **<font color="#739963">New Features</font>**

- New portal for creating agents, simplifying the bot creation process.

##### **<font color="#d66a60">Bugfix</font>**

- Improved WhatsApp responses to reduce cases of incorrect or garbled replies.
- Enhanced AI Agent responsiveness, addressing issues of stalling or failure to respond.

### 03/28/2024

##### **<font color="#739963">New Features</font>**

- New Social Media Channels Supported: Added Meta Facebook Messenger and WhatsApp channels, expanding communication platforms for Agents.
- New Website Integration Support: You can use SeaChat on [Shopify](https://wiki.seasalt.ai/seachat/seachat-manual/05-integrations/02-seachat-shopify-integration/) and [Squarespace](https://wiki.seasalt.ai/seachat/seachat-manual/05-integrations/03-seachat-squarespace-integration/).
- New Use Cases: Introduced 5 new use cases, making Agent creation more convenient and focused.
- Login Process Optimization: Simplified registration with Google accounts.

##### **<font color="#d66a60">Bugfix</font>**

- Support for LINE stickers, enhancing the response experience for customers.
- Added `/live_agent` transfer feature in WhatsApp and Meta Facebook Messenger.
- Fixed incorrect Live agent status display.
- Corrected the issue where Live Agent sends incorrect messages.

### 03/14/2024

##### **<font color="#739963">New Features</font>**

Language Model Optimization:

- Upgraded SeaChat Agent model
- Enhanced appointment scheduling prompt improvements.

##### **<font color="#d66a60">Bugfix</font>**

- Fixed random language summaries.

### 03/07/2024

##### **<font color="#739963">New Features</font>**

- Knowledge Base: Now supports Video, Audio, and Spreadsheet files, enabling more comprehensive content sharing and collaboration.

##### **<font color="#d66a60">Bugfix</font>**

- Extended support for longer video and audio files, with a maximum duration of 15 minutes.
- Fixed bug in uploading spreadsheets.
- In members setting, payment no longer prompts when adjusting AI Agent assignments.

### 03/04/2024

##### **<font color="#739963">New Features</font>**

- KnowledgeBase - Spreadsheet Upload: Now you can upload spreadsheets directly to the knowledge base
- KnowledgeBase - Video and Audio Uploads: Enhance your knowledge base with multimedia by uploading video and audio clips.
- You can now download invoice from billing history

### 02/23/2024

##### **<font color="#739963">New Features</font>**

- Email notifications for live agent requests and new conversations
- Users can switch between AI Agent and live human agent

##### **<font color="#d66a60">Bugfix</font>**

- Reduce new workspace creation time significantly

### 01/24/2024

##### **<font color="#739963">New Feature</font>**

- Preferred Response Language: Now you can set the default response language in the "Agent Information" menu. SeaChat will ensure the quality of your assistant's responses

<center>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/20240124-preferred-response-lang.png" alt="Set up a separate text channel just for live transcriptions from SeaVoice STT.">
</center>

##### **<font color="#d66a60">Bugfix</font>**

- Webchat Widget Preview: fix color mismatch bug in webchat widget preview


---


#### User Sends an Audio Message

<!-- Source: seachat-manual/08-incoming-queries/02-user-sends-an-audio-message.md -->

<!-- Weight: 10001 -->

*Learn how SeaChat understands and responds to user uploaded audio messages.*


# Overview

Up to this point, you've likely only seen SeaChat respond to text-based user chat messages. However, SeaChat has the capability to handle multimedia messages, such as audio and image, as well! This makes interactions more flexible and convenient for users, enabling them to share content in various formats for richer communication. 

---

## Audio Understanding

Some channels, such as Messenger, WhatsApp, and Line, allow users to send audio messages. SeaChat uses speech-to-text technology to convert the audio message into text, which is then processed as the user’s input. This feature ensures that even spoken messages can receive accurate and relevant responses from SeaChat. For users, this adds a layer of convenience, enabling hands-free communication in situations where typing might be difficult or less efficient.

### Example

In the following example, a user chats with the Seasalt.ai bot on WhatsApp and uses the "Voice Note" feature to send an audio message to the agent. By transcribing the audio first with speech-to-text, SeaChat is able to understand and respond to the audio message.

<br/>
<center>
<a href="/images/seachat/en/incoming-queries/SeaChat_Responds_to_Voice_Message_WhatsApp.jpg" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in;" src="/images/seachat/en/incoming-queries/SeaChat_Responds_to_Voice_Message_WhatsApp.jpg" alt="Using speech-to-text SeaChat is able to understand and respond to a user-uploaded audio message in WhatsApp.">
</a>

*Sending an Audio Message to SeaChat*
</center>

<br/>

---
