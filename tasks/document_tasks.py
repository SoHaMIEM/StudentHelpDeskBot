# tasks/document_tasks.py


from crewai import Task
from tools.document_validation import document_validation_tool
from agents.document_checker import document_checker


document_validation_task = Task(
    description="Validate submitted student documents and ensure all required files are present.",
    expected_output="A validation report containing document status and missing items (if any).",
    tools=[document_validation_tool],
    agent=document_checker,
    async_execution=False
)