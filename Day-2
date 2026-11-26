from google.colab import userdata
from openai import OpenAI

client = OpenAI(
    api_key=userdata.get("groqAPI"),
    base_url="https://api.groq.com/openai/v1"
)
import functools
from openai import OpenAI, RateLimitError, APIConnectionError
from google.colab import userdata

client = OpenAI(
    api_key=userdata.get("groqAPI"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-20b"

FEATURES = {
    "profile": "Students can create profiles with skills, academics and projects.",
    "jobs": "Students can browse placement opportunities posted by companies.",
    "applications": "Students can track their application progress.",
    "college": "Colleges verify student profiles and mediate placements.",
    "companies": "Companies can post jobs and define eligibility criteria."
}

SYSTEM = f"""ROLE: You are the friendly AI assistant for CampusBridge, a college-mediated placement portal.

FACTS: CampusBridge features: {FEATURES}

RULES: Help students with profiles, jobs, applications and placement preparation.
       Never invent job openings, eligibility requirements or application statuses.
       If information isn't available, say "Please check with your college placement cell."
       Remember the student's name and details during the chat.
       Do not claim to access actual databases.

FORMAT: Under 50 words, friendly, simple, English or Telugu matching the user."""

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"   [log] {func.__name__}{args} -> {result!r}")
        return result
    return wrapper

@log_call
def get_feature_info(feature: str) -> str:
    """Return information about a CampusBridge feature."""
    return FEATURES.get(feature.lower().strip(), "Feature information not available.")

history = [{"role": "system", "content": SYSTEM}]
MAX_TURNS = 3

def chat(user_text: str) -> str:
    history.append({"role": "user", "content": user_text})

    recent = [history[0]] + history[1:][-MAX_TURNS:]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=recent,
            temperature=0.3
        )
        reply = response.choices[0].message.content

    except RateLimitError:
        reply = "We're a little busy. Please try again in a minute."

    except APIConnectionError:
        reply = "I can't reach the server right now. Please try again shortly."

    history.append({"role": "assistant", "content": reply})
    return reply

print("Profile information:", get_feature_info("profile"))

while True:
    text = input("You: ")

    if text.lower().strip() in ("bye", "exit", "quit"):
        print("Bot: Thank you for using CampusBridge!")
        break

    print("Bot:", chat(text))
