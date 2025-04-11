from crewai import Agent
# agents/document_checker.py
document_checker = Agent(
    role="Document Checker",
    goal="Validate submitted student application forms and documents",
    backstory="You are responsible for checking if all necessary documents are submitted and if they are valid.",
    allow_delegation=False
)
