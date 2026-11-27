!pip install -q openai
!pip install -q langchain langchain-groq
from google.colab import userdata
from openai import OpenAI

client = OpenAI(
    api_key=userdata.get("groqAPI"),
    base_url="https://api.groq.com/openai/v1"
)
import os
from google.colab import userdata

os.environ["GROQ_API_KEY"] = userdata.get("groqAPI")
 from google.colab import files

uploaded = files.upload()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2)

SYSTEM = """ROLE: You are the friendly AI assistant for CampusBridge,
a college-mediated placement portal.

FACTS: Students can create profiles with skills, academic details and projects.
       Students can browse placement opportunities and track applications.
       Colleges verify student profiles and mediate placements.
       Companies can post jobs and define eligibility criteria.

RULES: Help students with profiles, jobs, applications and placement preparation.
       Never invent job openings, eligibility criteria or application statuses.
       If information is unavailable, say
       "Please check with your college placement cell."

FORMAT: Friendly, simple, concise English."""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()
import csv

def run_tests(path="test.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    passed = 0
    for row in rows:
        answer = chain.invoke({"history": [], "question": row["question"]})
        ok = row["must_include"].lower() in answer.lower()
        passed += ok
        print("PASS" if ok else "FAIL", "|", row["question"], "→", answer[:70])

    print(f"\n{passed}/{len(rows)} passed ({passed / len(rows):.0%})")

run_tests()
from langchain.agents import create_agent

agent = create_agent(model=llm, tools=[], system_prompt=SYSTEM)   # tools come tomorrow
result = agent.invoke({"messages": [{"role": "user", "content": "Do you make eggless cakes?"}]})
print(result["messages"][-1].content)
