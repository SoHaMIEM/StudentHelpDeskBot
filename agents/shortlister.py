
from crewai import Agent
from llm_config import llm
# agents/shortlister.py
shortlister = Agent(
    role="Shortlisting Agent",
    goal="Shortlist candidates based on eligibility criteria and university capacity",
    backstory="You apply the university's eligibility rules to identify students who qualify for admission.",
    allow_delegation=False,
    llm=llm
)