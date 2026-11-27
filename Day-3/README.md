# Day 3 – Introduction to LangChain & AI Agent Testing

## Overview
Today I learned the basics of LangChain and how it simplifies connecting Large Language Models (LLMs) with prompts and application logic. I explored how a similar LangChain structure can be used with different supported model providers and APIs.

## Concepts Learned
- Introduction to LangChain.
- Connecting LLMs using LangChain integrations.
- Using Groq API with LangChain.
- Understanding prompt templates.
- Using `MessagesPlaceholder` for conversation history.
- Creating chains using the prompt, LLM and output parser.
- Initializing agents using `create_agent()`.
- Testing AI responses using CSV test cases.
- Basic response validation using expected keywords.

## Mini Project
### CampusBridge AI Assistant
Customized an AI assistant for CampusBridge, a college-mediated placement portal. The assistant helps students understand platform features, placement profiles, applications and placement preparation.

## Testing
Created a `test.csv` file containing placement-related questions and expected keywords to evaluate the assistant's responses.

## Technologies Used
- Python
- LangChain
- LangChain-Groq
- Groq API
- GPT-OSS-20B
- Google Colab
- CSV

## Outcome
Built a prompt-based CampusBridge assistant using LangChain and explored basic automated testing of LLM responses using CSV-based test cases.
## Test.csv contains
question,must_include
"What can students add to their profiles?","skills"
"Who verifies student profiles?","college"
"Can students browse placement opportunities?","jobs"
"What can companies specify when posting jobs?","eligibility"
"How can students track their applications?","applications"
"Where should I check for information about an unavailable feature?","placement cell"
