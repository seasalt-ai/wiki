---
title: "Auto-Labeling"
description: "Learn how to set up and use the Auto-Labeling feature to automate and streamline conversation labeling processes."
lead: ""
date: 2024-12-29T00:00:00-07:00
lastmod: 2024-12-29T00:00:00-07:00
weight: 90
draft: false
images: []
toc: true
url: /en/seachat/manual/create-agent/advanced-settings/auto-labeling/
---

### Auto-Labeling 

---

**Overview**  
Auto-labeling is an integral part of the integrations in Seasalt.ai's suite of tools. This feature intelligently and automatically applies labels to conversations, streamlining processes for use cases such as customer service and healthcare. 

In this tutorial, we will guide you through setting up and using the Auto-Labeling feature on SeaChat. You are welcome to check out our video tutorial to replicate the example use case below.

**What Is Auto-Labeling?**  
Auto-labeling is a system that automates the application of labels to conversations or other data points based on predefined rules and AI-driven analysis. Instead of manually tagging, users can set conditions under which labels are applied or removed dynamically.

---

**Key Features**  

<br/>

<center>
<a href="/images/seachat/en/gpt-tools/image5.png">
<img height="100%" width="100%" src="/images/seachat/en/gpt-tools/image5.png"  alt="Example of New Custom Tool">
</a>

<br/>

*Example: we have a GET endpoint that retrieves dog pictures.*

</center>

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

**How to Set Up Auto-Labeling**  

1. **Navigate to Integrations**  
   - Open the ```Integrations``` section and select ```Auto Labeling.```  

2. **Create Rules**  
   - Define triggers for adding or removing labels.  
   - Example: For healthcare hotlines:
     - ```Extreme pain``` triggers the ```Escalated``` label.  
     - ```Minor aches``` triggers the ```Low Priority``` label.  

3. **Test Your Rules**  
   - Simulate conversations to see if labels apply correctly.  
   - Example: Input "I feel so much pain, I need a doctor’s attention" to trigger ```Escalated.```  

4. **Adjust and Save**  
   - Modify rules to refine accuracy and save the configuration.  

---

**Advanced Use Cases**  

1. **Medical Triage System**  
   - Labels like ```Green```, ```Yellow```, and ```Red``` can classify conditions based on severity.  
     - Red: Severe issues like difficulty breathing or severe bleeding.  
     - Yellow: Moderate pain or fever.  
     - Green: Minor aches or colds.  

2. **Label Automation**  
   - Link actions to specific labels:
     - Trigger an email or SMS when ```Escalated``` is applied.  
     - Automate follow-ups for ```Low Priority``` cases.  

---

**Benefits of Auto-Labeling**  

- **Efficiency**: Reduces manual labeling efforts.  
- **Scalability**: Handles high volumes of data.  
- **Accuracy**: Ensures consistent application of rules.  
- **Customization**: Adapts to various industries and use cases.  

---

**Conclusion**  
Auto-labeling transforms how businesses manage conversations and data. From dynamic triaging in healthcare to streamlining customer support, this tool simplifies and accelerates processes while ensuring accuracy. Future tutorials will delve into removing labels and leveraging label automation for more advanced workflows. Stay tuned!

