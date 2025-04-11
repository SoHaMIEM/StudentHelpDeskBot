# crew/crew_setup.py

from crewai import Crew

# Import Agents
from agents.admission_officer import admission_officer
from agents.document_checker import document_checker
from agents.shortlister import shortlister
from agents.student_counselor import student_counselor
from agents.loan_agent import loan_agent

# Import Tasks
from tasks.document_tasks import document_validation_task
from tasks.shortlist_tasks import shortlisting_task
from tasks.counselor_tasks import counseling_task
from tasks.loan_tasks import loan_processing_task
from tasks.officer_tasks import officer_decision_task

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
        document_validation_task,
        shortlisting_task,
        counseling_task,
        loan_processing_task,
        officer_decision_task
    ],
    verbose=True,
    description="Crew responsible for automating student admission using an agentic workflow."
)

def run_admission_crew():
    result = admission_crew.kickoff()
    return result
