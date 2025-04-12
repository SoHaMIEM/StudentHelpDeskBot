# tasks/counselor_tasks.py
from crewai import Task
from tools.communication import create_welcome_message_tool, create_rejection_message_tool, create_loan_status_message_tool
from agents.student_counselor import student_counselor

counselor_task = Task(
    description="Generate appropriate communication emails based on admission and loan decisions.",
    expected_output="Student-facing email content.",
    tools=[create_welcome_message_tool, create_rejection_message_tool, create_loan_status_message_tool],
    agent=student_counselor,
    async_execution=False
)