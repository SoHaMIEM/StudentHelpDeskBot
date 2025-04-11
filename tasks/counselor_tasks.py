from crewai import Task
from tools.communication import create_welcome_message, create_rejection_message, create_loan_status_message
from agents.student_counselor import student_counselor

counselor_task = Task(
    description="Generate appropriate communication emails based on admission and loan decisions.",
    expected_output="Student-facing email content.",
    tools=[create_welcome_message, create_rejection_message, create_loan_status_message],
    agent=student_counselor,
    async_execution=False
)
