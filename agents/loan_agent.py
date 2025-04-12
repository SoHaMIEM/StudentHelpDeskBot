from crewai import Agent
from llm_config import llm
# agents/loan_agent.py
loan_agent = Agent(
    role="Student Loan Agent",
    goal="Process student loan queries and requests",
    backstory="You help students with loan-related information and approve loans within the set policy limits.",
    allow_delegation=False,
    llm=llm
)