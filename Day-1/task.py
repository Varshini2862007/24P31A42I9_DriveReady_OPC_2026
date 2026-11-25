!pip install -q openai
from openai import OpenAI
from google.colab import userdata

client = OpenAI(
    api_key=userdata.get("groqAPI"),
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM = """ROLE: You are the AI assistant for CampusBridge, a college-mediated placement portal.

FACTS: CampusBridge connects students, colleges and companies.
       Students can create profiles, add skills, projects and academic details,
       browse placement opportunities and track applications.
       Colleges verify student profiles and mediate placement processes.
       Companies post jobs and define eligibility criteria.

RULES: Help students understand placements, profiles, applications and platform features.
       Never invent job openings, eligibility criteria or application statuses.
       If information is unavailable, say "Please check with your college placement cell."
       Do not claim to access student records or databases.

FORMAT: Keep answers under 50 words, friendly, simple, English or Telugu matching the customer."""

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    messages=[
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": "How can I prepare my profile for placements?"}
    ],
)

print(response.choices[0].message.content)
print(response.usage)
