---
title: "Zendesk Ticket Search Tool"
description: ""
date: 2025-02-04-T00:22:19-07:00
date: 2025-02-04-T00:22:19-07:00
draft: false

weight: 70
url: /seachat/seachat-manual/automation/zendesk-ticket-search
---

SeaChat now offers a new custom GPT tool designed specifically for Zendesk ticket search. By connecting your Zendesk account, you enable SeaChat to respond to user queries based on relevant ticket information, improving support efficiency.

## SeaChat Zendesk Ticket Search Tool

The SeaChat Zendesk Ticket Search Tool is an innovative feature from Seasalt.ai that streamlines support workflows by transforming complex Zendesk ticket data into direct, context-aware answers for user queries. Instead of forcing users to sift through numerous search results and manually open individual tickets, SeaChat extracts key insights from entire ticket conversations and returns precise answers—all in a single interaction.

---

## How It Works

The tool leverages Zendesk’s robust API capabilities through the following steps:

&nbsp;&nbsp;&nbsp;&nbsp; **1. Keyword Extraction:**

When a user submits a query, SeaChat automatically parses the input to extract one or more keywords. These keywords are then used to form a search query to the Zendesk Search API.

&nbsp;&nbsp;&nbsp;&nbsp; **2. Ticket Search via Zendesk Search API:**

SeaChat submits the extracted keyword(s) to the Zendesk Search API (/api/v2/search.json?query=xxx). This API returns a list of relevant tickets based on the search criteria. Notably, the initial API response includes only the first comment (often the ticket’s description) for each ticket thread, which serves as a preview of the ticket content.

&nbsp;&nbsp;&nbsp;&nbsp; **3. Retrieving Full Ticket Threads:**

For each ticket returned in the search results, SeaChat then makes additional requests to the Zendesk Ticket Comments API (/api/v2/tickets/{id}/comments). This step ensures that all comments—including follow-ups, agent responses, and internal notes—are retrieved, providing a complete picture of the ticket’s history.

&nbsp;&nbsp;&nbsp;&nbsp; **4. Answer Synthesis:**
Finally, using advanced natural language processing, SeaChat analyzes the full ticket conversations to determine the most relevant answer to the user's query. This process aggregates insights from multiple tickets if needed, allowing SeaChat to deliver a direct and actionable response without requiring manual navigation through the Zendesk UI.

---

## Use Cases

The SeaChat Zendesk Ticket Search Tool is versatile and can be applied in various support and operational scenarios:

&nbsp;&nbsp;&nbsp;&nbsp; -- **Streamlined Support Response:**
Agents can quickly retrieve complete answers to customer questions by tapping into historical ticket data, reducing the time spent manually searching through tickets.

&nbsp;&nbsp;&nbsp;&nbsp; -- **Automated Knowledge Base Augmentation:**
By consolidating frequent queries and their corresponding resolutions, the tool can help automatically update FAQs and knowledge base articles, ensuring that self-service options are always current and accurate.

&nbsp;&nbsp;&nbsp;&nbsp; -- **Root Cause Analysis:**
Support managers can utilize the tool to analyze patterns in ticket conversations—such as recurring issues or common troubleshooting steps—to improve product reliability and customer satisfaction.

&nbsp;&nbsp;&nbsp;&nbsp; -- **Efficient Data Integration:**
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
