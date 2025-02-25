---
title: "Evaluation: Enhancing AI Agent Response Accuracy with Test Sets"
description: "Enhancing AI Agent Response Accuracy with Test Sets"
date: 2025-02-25T00:22:19-07:00
lastmod: 2025-02-25T00:22:19-07:00
draft: false
weight: 802
aliases:
  - /en/seachat/seacaht-manual/07-test-and-improve-ai-agent/evaluation
---

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
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/2add-a-new-set.png"  alt="Add a new set">
</a>

_Click + Add new set to add a new set_

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
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
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/4add-sample.png"  alt="Add a new test sample">
</a>

_Example: Add a user test query and an agent gold response to customerQ&A test set_

</center>

### **Step 4: Run the Test Set**

1. Click the **Run** icon next to the test set and click confirm button in the popup
2. Navigate to the **Test Runs** tab to review the results.

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/5run-set.png"  alt="Click Run button to run">
</a>

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/6confirm-run.png"  alt="Click Run button to run">
</a>

</center>

### **Step 5: Review Test Run Results**

1. Review all test runs in the **Test Runs** tab

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
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
<a href="/images/seachat/en/evaluation/add-members.png">
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
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/11needs-review-page.png"  alt="Click Add to Test Set button to add to a test set">
</a>

_Example: In the Needs Review page, click the + Add to Test Set button to add the agent response to a test set._

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/12add needs review message to a test set.png"  alt="Modify sample to be added to the test set">
</a>

_Example: Add user message and modify the agent gold response, then add this sample to the customerQ&A test set._

</center>

</center>

<br/>

<center>
<a href="/images/seachat/en/evaluation/add-members.png">
<img height="100%" width="100%" src="/images/seachat/en/evaluation/13new sample in test set.png"  alt="View the newly added test sample">
</a>

_Example: Navigate to the Evaluation page, the NLP related query has been added to the customerQ&A test set._

</center>

## **3\. Pricing**

Test runs consume agent responses and will be billed accordingly. Each test case in a test set costs **$0.01**.

If you need further assistance, feel free to reach out to [seachat@seasalt.ai](mailto:seachat@seasalt.ai)! 🚀
