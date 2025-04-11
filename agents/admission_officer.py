from crewai import Agent

admission_officer = Agent(
    role="Admission Officer",
    goal="Oversee and coordinate the entire student admission process",
    backstory="You are the lead officer of the university's admission department. You review the work of other agents and make final decisions.",
    allow_delegation=True
)