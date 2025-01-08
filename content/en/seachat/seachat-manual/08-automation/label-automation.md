---
title: "Label Automation"
description: "Learn how to set up and use Label Automation in SeaChat to trigger actions based on applied labels."
lead: ""
date: 2024-12-29T00:00:00-07:00
lastmod: 2024-12-29T00:00:00-07:00
weight: 90
draft: false
images: []
toc: true
url: /en/seachat/manual/labeling/label-automation/
---

---

## Video Tutorial

<iframe width="100%" height="400" src="https://www.youtube.com/embed/2SYYU1lQqrc?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

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

