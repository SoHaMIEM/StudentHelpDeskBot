# tasks/loan_tasks.py
from crewai import Task
from tools.loan_processor import evaluate_loan_request
from agents.loan_agent import loan_agent

loan_evaluation_task = Task(
    description="Evaluate student loan applications and determine approval status.",
    expected_output="Loan decision report with approval status and sanctioned amount.",
    tools=[evaluate_loan_request],
    agent=loan_agent,
    async_execution=False
)
