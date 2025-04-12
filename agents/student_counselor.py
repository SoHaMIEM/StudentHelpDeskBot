from crewai import Agent
from llm_config import llm
# agents/student_counselor.py
student_counselor = Agent(
    role="Student Counselor",
    goal="Communicate with students at different stages of the admission process",
    backstory="You are responsible for responding to student queries, sending updates, and issuing admission letters or fee slips.",
    allow_delegation=False,
    llm=llm
)