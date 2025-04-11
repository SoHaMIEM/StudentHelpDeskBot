# tasks/officer_tasks.py
from crewai import Task
from agents.admission_officer import admission_officer

admission_officer_task = Task(
    description="Oversee the entire admission process, trigger agents and aggregate results for reporting.",
    expected_output="A complete report summarizing admission status, document validation, shortlisting, and loan approvals.",
    tools=[],  # Could include a reporting or logging tool if needed
    agent=admission_officer,
    async_execution=False
)
