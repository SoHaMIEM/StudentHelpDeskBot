# tasks/document_tasks.py
from crewai import Task
from tools.document_validation import validate_documents
from agents.document_checker import document_checker

document_check_task = Task(
    description="Validate submitted student documents and ensure all required files are present.",
    expected_output="A validation report containing document status and missing items (if any).",
    tools=[validate_documents],
    agent=document_checker,
    async_execution=False
)
