!pip install -q langchain langchain-groq gspread

import os
from google.colab import userdata, auth

os.environ["GROQ_API_KEY"] = userdata.get("groqAPI")
from langchain.tools import tool

FEATURES = {
    "profile": "Students can create profiles with skills, academic details and projects.",
    "jobs": "Students can browse placement opportunities posted by companies.",
    "applications": "Students can track their application progress.",
    "college": "Colleges verify student profiles and mediate placements.",
    "companies": "Companies can post jobs and define eligibility criteria."
}

@tool
def get_feature_info(feature: str) -> str:
    """Get information about a CampusBridge feature.
    Feature can be profile, jobs, applications, college or companies."""
    info = FEATURES.get(feature.lower().strip())
    return info if info else "Information unavailable. Please check with your college placement cell."

@tool
def get_profile_checklist() -> str:
    """Get a checklist of information students should prepare for their placement profile."""
    return (
        "Prepare your academic details, technical skills, projects, "
        "certifications, resume and contact information for your placement profile."
    )

@tool
def log_query(name: str, category: str, question: str) -> str:
    """Save a student's general CampusBridge query to the Queries sheet.
    Use only when the student explicitly asks to save or log their query.
    Do not log passwords, sensitive personal information or confidential records."""
    if not question.strip():
        return "Query cannot be empty."

    ws.append_row([name, category, question])
    return f"Query saved successfully for {name if name else 'student'}."
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    max_retries=3
)
auth.authenticate_user()

import gspread
from google.auth import default

creds, _ = default()
gc = gspread.authorize(creds)

sh = gc.create("CampusBridge Student Queries")  # Run once
ws = sh.sheet1

ws.append_row(["name", "category", "question"])

print("Sheet ready:", sh.url)
from langchain.agents import create_agent

SYSTEM = """ROLE: You are the friendly AI assistant for CampusBridge,
a college-mediated placement portal.

FACTS: Students can create profiles, add skills, academic details and projects.
       Students can browse placement opportunities and track applications.
       Colleges verify student profiles and mediate placements.
       Companies can post jobs and define eligibility criteria.

RULES: Use get_feature_info for platform feature questions.
       Use get_profile_checklist when students ask about profile preparation.
       Use log_query only when the student explicitly asks to save or log a query.
       Never invent actual job openings, eligibility requirements or application statuses.
       If information is unavailable, say "Please check with your college placement cell."
       Do not claim to access actual student records or databases.

FORMAT: Under 60 words, friendly, English or Telugu matching the student."""

agent = create_agent(
    model=llm,
    tools=[get_feature_info, get_profile_checklist, log_query],
    system_prompt=SYSTEM
)
history = []

def chat(text: str) -> str:
    global history

    try:
        result = agent.invoke({
            "messages": history + [{"role": "user", "content": text}]
        })

        history = result["messages"]
        return history[-1].content

    except Exception as e:
        print("Agent error:", e)
        return "Sorry, I'm a little busy. Please try again."
print(chat("What can I add to my placement profile?"))
print(chat("Give me a profile checklist."))
print(chat("What does the college do in CampusBridge?"))
print(chat("Save my query. My name is Ravi and I want to know how to prepare for placements."))
for message in history:
    message.pretty_print()
