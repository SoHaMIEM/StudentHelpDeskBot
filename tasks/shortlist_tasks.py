# tasks/shortlist_tasks.py
from crewai import Task
from tools.shortlist_logic import check_eligibility_tool, shortlist_students_tool
from agents.shortlister import shortlister

shortlist_task = Task(
    description="Shortlist eligible candidates based on criteria and capacity.",
    expected_output="A list of shortlisted student IDs.",
    tools=[check_eligibility_tool, shortlist_students_tool],
    agent=shortlister,
    async_execution=False
)