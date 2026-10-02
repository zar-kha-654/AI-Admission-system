import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Add it to your .env file."
    )

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=GROQ_API_KEY,
    temperature=0.2
)
