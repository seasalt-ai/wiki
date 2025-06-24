---
title: "SeaX Inbound/Outbound Call with a Dialpad"
description: "Use SeaX to place phone calls for your Twilio phone number"
date: 2025-06-24T08:48:57+00:00
lastmod: 2025-06-24T08:48:57+00:00
draft: false
images: []
menu:
  seax:
    parent: "seax-omni"
url: /en/seax/seax-omni/phone-call-dialpad/
weight: 40
toc: true
---

SeaX provides a comprehensive contact center solution that allows you to handle both inbound and outbound phone calls using an integrated dial pad interface. This feature complements SeaX's existing capabilities for large-scale outbound campaigns, WhatsApp messaging, and SMS communications.

## 🎥 Video Tutorial for Dialpad

A comprehensive video tutorial demonstrates step-by-step how to set up and use SeaX with phone calls, including both outbound and inbound calls handled by human agents.

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/1luD3EFnIu4?list=PL8K7_LTqly45pLJ1NAw3P3VlPseovylOC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius: 30px;"></iframe>


**Key Features Covered:**
- ✅ Dial pad setup and configuration
- ✅ Inbound call handling
- ✅ Outbound call management
- ✅ AI agent integration
- ✅ Multi-agent round robin system
- ✅ Contact management and call logs

### Prerequisites

Before using the dial pad feature, ensure you have:
- An active SeaX workspace
- Phone numbers configured for voice calls
- Proper audio devices (microphone and speakers) configured
- Agent status set to "Available"

### Setting Up Your Dial Pad

#### Agent Configuration

1. **Access the Dial Pad**: Navigate to your SeaX workspace and locate the dial pad interface
2. **Set Agent Status**: Change your status to "Available" to receive incoming calls
3. **Configure Audio Devices**: 
   - Select your preferred speaker (computer speaker or external device)
   - Choose your microphone input
   - Test audio settings before taking calls

#### Phone Number Setup

1. **Navigate to Numbers**: Go to **Workspace > Numbers** to view your available phone numbers
2. **Verify Voice Enablement**: Ensure your numbers are enabled for voice calls (you'll see options for SMS, MMS, and phone calls)
3. **Check Number Types**: SeaX supports various number types including:
   - WhatsApp-enabled numbers
   - SIP trunking for legacy PSTN lines
   - Standard phone numbers with SMS/MMS capabilities

### Handling Inbound Calls

#### Receiving Calls

When an inbound call arrives:
1. You'll hear an incoming call notification
2. Click to answer the call through your browser interface
3. Use the on-screen keypad during calls if needed for IVR navigation

#### Call Management Features

- **Call Logs**: Access detailed logs of all incoming and outbound calls
- **Contact Integration**: Numbers registered in your contacts will display associated names
- **Multi-Channel Integration**: The same number can be used for both voice calls and WhatsApp messaging

### Making Outbound Calls

#### Manual Dialing

1. **Open Dial Pad**: Access the dial pad interface
2. **Search Contacts**: Use the search function to find existing contacts
3. **Select Number**: Choose the appropriate number if multiple options are available
4. **Initiate Call**: Click to start the outbound call

#### AI-Assisted Dialing

SeaX offers AI agent integration for outbound calls:
1. **Select AI Agent**: Choose from available voice AI agents configured in SeaChat
2. **Enter Target Number**: Input the recipient's phone number
3. **Start AI Dial**: The AI agent will make the call on your behalf
4. **Use Cases**: Perfect for job interviews, appointment scheduling, or follow-up calls

### Advanced Configuration

#### Number Assignment

For each phone number, you can configure:
- **Multiple Agent Assignment**: Assign several agents to handle calls for a single number
- **Default Inbound Agents**: Set whether humans or AI agents handle incoming calls by default
- **Channel-Specific Settings**: Configure different agents for SMS vs. voice calls

#### Round Robin System

When multiple agents are assigned to a number:
- Calls are distributed to available agents in round-robin fashion
- Each agent receives a 10-second ring before the call moves to the next available agent
- System prioritizes agents with "least busy" status
- If no human agents are available, calls can automatically transfer to AI agents

### Integration with Other SeaX Features

The dial pad functionality integrates seamlessly with:
- **Large-scale outbound campaigns**
- **WhatsApp Business messaging**
- **SMS and MMS communications**
- **SeaChat AI agents for omnichannel support**

### Best Practices

1. **Agent Availability**: Keep your status updated to ensure proper call routing
2. **Audio Quality**: Use quality headsets for better call experience
3. **Contact Management**: Maintain updated contact lists for efficient outbound calling
4. **AI Backup**: Configure AI agents as backup for when human agents are unavailable
5. **Call Logging**: Regularly review call logs for performance insights

### Troubleshooting

**Common Issues:**
- **Audio Echo**: Adjust microphone and speaker settings to prevent feedback
- **Missed Calls**: Ensure agent status is set to "Available" and audio notifications are enabled
- **Number Configuration**: Verify phone numbers are properly enabled for voice calls in the Numbers section

This dial pad feature transforms SeaX into a complete human-AI native contact center solution, allowing seamless transitions between automated campaigns and personal customer interactions.

## 📷 Tutorial for Dialpad with Product Pictures

### Overview

SeaX integrates both internal and external phone communication into a single platform. On this platform, you can:

**Making and Receiving Calls**

* Search or type a number to start a call right from the platform  
* Pick up incoming calls without switching apps  
* Choose from different outbound numbers or let an AI agent handle the call for you.

**Call Management**

* All inbound, outbound, and missed calls are logged automatically  
* Saved contacts appear by name in your call history, not just as numbers.  
* Easily search call logs to follow up or check history

**Contact Management**

* Import and export contact lists  
* Assign multiple tags to each contact  
* Group contacts by tags for easier organization

### Dialpad Calling

SeaX provides a built-in dialpad, enabling users to make and receive calls directly through the platform—no external devices or apps required.

#### How to Make an Outbound Call

Click the dialpad icon at the top right to open the dialpad. Enter a number manually or search by name or number to quickly place a call.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/1-dialpad.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/1-dialpad.png" alt="SeaX | Dialpad">
</a>

*SeaX Dialpad*
</center>


#### How to Answer an Inbound Call

When there’s an inbound call, a notification card will appear in the top right corner. Click to answer or decline the call.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/2-dialpad-inbound-call.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/2-dialpad-inbound-call.png" alt="SeaX | Dialpad Inbound Call">
</a>

*SeaX Dialpad Inbound Call*
</center>


#### Calling with an AI Agent

Click the arrow next to the call button in the dialpad to select an AI agent. Then enter or search for the contact’s number to place the call.

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/3-dialpad-ai-agent.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/3-dialpad-ai-agent.png" alt="SeaX | Dialpad Calling with an AI Agent">
</a>

*SeaX Dialpad Calling with an AI Agent*
</center>


#### Call Log Overview

All inbound and outbound calls are logged in the call history panel on the left, where users can view or search by time, duration, contact, and more.


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/4-call-logs.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/4-call-logs.png" alt="SeaX | Dialpad Call Logs">
</a>

*SeaX Dialpad Call Logs*
</center>


### Agent Status Settings

SeaX provides a status switching feature so agents can control their availability. The system routes calls based on current status.

Status Types

* Available  
* Away  
* Do Not Disturb  
* Offline  
* On a Call

#### How to Change Your Status

1. Click your profile icon at the top right after logging in to SeaX


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/5-status-menu.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/5-status-menu.png" alt="SeaX | Dialpad Status Menu">
</a>

*SeaX Dialpad Status Menu*
</center>


2. Find the status panel showing your current availability


<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/6-status-menu-open.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/6-status-menu-open.png" alt="SeaX | Dialpad Status Menu Open">
</a>

*SeaX DialpadStatus Menu Open*
</center>


3. Click your current status to view all options (Available, Away, Do Not Disturb, Offline). Select your preferred status, and SeaX will update it immediately.

#### Status Effects:

Available: Green – able to receive calls  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/7-status-available.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/7-status-available.png" alt="SeaX | Dialpad Status Green">
</a>

*SeaX Dialpad Status: Available*
</center>


Away: Orange – no new calls will be routed  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/8-status-away.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/8-status-away.png" alt="SeaX | Dialpad Status Away">
</a>

*SeaX Dialpad Status: Away*
</center>


Do Not Disturb: Red – no new calls will be routed  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/9-status-do-not-disturb.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/9-status-do-not-disturb.png" alt="SeaX | Dialpad Status: DND">
</a>

*SeaX Dialpad Status: DND*
</center>

Offline: Gray – completely inactive  

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/10-status-offline.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/10-status-offline.png" alt="SeaX | Dialpad Status: Offline">
</a>

*SeaX Dialpad Status: Offline*
</center>


On a Call: Automatically activated during a call and reverts after ending

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seax/en/phone-call-dialpad/11-status-in-the-call.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem" src="/images/seax/en/phone-call-dialpad/11-status-in-the-call.png" alt="SeaX | Dialpad Status: On A Call">
</a>

*SeaX Dialpad Status: On A Call*
</center>



### Understanding Round Robin

When a phone number is set to route inbound calls to human agents, SeaX applies the following ring assignment rules based on agent status:

Ringing Logic

* Only agents with Available status will be called  
* Agents are sorted by activity time to determine the ringing order  
* Each agent is tried for 10 seconds before the system moves to the next  
* In each round, agents who were already rung but didn’t answer are skipped

Note: If only one agent is online and doesn’t answer, the system will play a busy message to the caller and end the call.