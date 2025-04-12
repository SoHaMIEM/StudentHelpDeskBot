# llm_config.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
