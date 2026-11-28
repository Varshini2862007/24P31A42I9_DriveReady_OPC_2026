# Day 4 – AI Agents with Tools and Google Sheets Integration

## Overview
Today I learned how to build AI agents that can use tools to perform specific tasks instead of only generating text responses. I explored tool calling using LangChain and integrated Google Sheets to store user queries.

## Concepts Learned
- Creating custom tools using the `@tool` decorator.
- Understanding how AI agents select and use tools.
- Integrating multiple tools into a single AI agent.
- Using Google Sheets as a simple data storage mechanism.
- Connecting Google Colab with Google Sheets using `gspread`.
- Maintaining conversation history in an AI agent.
- Using `create_agent()` to initialize a tool-enabled agent.
- Handling errors during agent execution.

## Tools Implemented
- **get_feature_info:** Retrieves information about CampusBridge features.
- **get_profile_checklist:** Provides a checklist for preparing a placement profile.
- **log_query:** Saves student queries into a Google Sheet when requested.

## Mini Project
### CampusBridge AI Assistant
Customized an AI assistant for CampusBridge, a college-mediated placement portal. The agent can answer questions about platform features, provide profile-preparation guidance and save student queries to Google Sheets when explicitly requested.

## Technologies Used
- Python
- LangChain
- LangChain-Groq
- Groq API
- GPT-OSS-20B
- Google Colab
- Google Sheets
- gspread

## Outcome
Built a tool-enabled AI agent with conversational memory and Google Sheets integration, allowing it to retrieve predefined platform information, provide profile guidance and save user queries.
