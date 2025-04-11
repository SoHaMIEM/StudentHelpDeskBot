# crew/crew_setup.py

from crewai import Crew

# Import Agents
from agents.admission_officer import admission_officer
from agents.document_checker import document_checker
from agents.shortlister import shortlister
from agents.student_counselor import student_counselor
from agents.loan_agent import loan_agent

# Import Tasks
from tasks.document_tasks import document_check_task
from tasks.shortlist_tasks import shortlist_task
from tasks.counselor_tasks import counselor_task
from tasks.loan_tasks import loan_evaluation_task
from tasks.officer_tasks import admission_officer_task

# Create the admission automation crew
admission_crew = Crew(
    agents=[
        document_checker,
        shortlister,
        student_counselor,
        loan_agent,
        admission_officer
    ],
    tasks=[
        document_check_task,
        shortlist_task,
        counselor_task,
        loan_evaluation_task,
        admission_officer_task
    ],
    verbose=True,
    description="Crew responsible for automating student admission using an agentic workflow."
)

def run_admission_crew():
    result = admission_crew.kickoff()
    return result