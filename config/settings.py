import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# === GEMINI API SETTINGS ===
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-pro")
GEMINI_TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", 0.3))

# === CHROMADB SETTINGS ===
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "chroma_db")

# === VECTOR STORE COLLECTION NAME ===
VECTOR_COLLECTION_NAME = os.getenv("VECTOR_COLLECTION_NAME", "admission_docs")

# === STATIC DOCUMENT PATHS ===
STATIC_DOCS_PATH = os.path.join("data", "static_docs")

# === STUDENT SUBMISSIONS PATH ===
STUDENT_SUBMISSIONS_PATH = os.path.join("data", "student_submissions")

# === OTHER CONSTANTS ===
UNIVERSITY_NAME = "Your University Name"
DEFAULT_CAPACITY = int(os.getenv("DEFAULT_CAPACITY", 100))  # Max shortlisted students
LOAN_BUDGET = float(os.getenv("LOAN_BUDGET", 1000000))      # Total loan budget pool
