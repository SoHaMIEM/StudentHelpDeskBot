from typing import Dict
from crewai.tools import BaseTool

def generate_email(to: str, subject: str, body: str) -> dict:
    """Generate a formatted email dictionary."""
    return {
        "to": to,
        "subject": subject,
        "body": body
    }

def create_welcome_message(student: dict) -> str:
    return f"""
    Dear {student.get('name')},

    Congratulations! You have been shortlisted for admission. Please proceed with the next steps as outlined in your admission letter.

    Regards,
    Student Admission Office
    """

def create_rejection_message(student: dict) -> str:
    return f"""
    Dear {student.get('name')},

    We regret to inform you that your application has not met the eligibility criteria for admission.

    Regards,
    Student Admission Office
    """

def create_loan_status_message(student: dict, status: str, amount: int) -> str:
    if status.startswith("Approved"):
        return f"""
        Dear {student.get('name')},

        Your student loan of INR {amount} has been approved. The amount will be disbursed as per university timelines.

        Regards,
        Student Financial Services
        """
    else:
        return f"""
        Dear {student.get('name')},

        Your loan application has been reviewed and was unfortunately not approved.

        Reason: {status}

        Regards,
        Student Financial Services
        """

# Tool for welcome message
class WelcomeMessageCreatorTool(BaseTool):
    name: str = "WelcomeMessageCreator"
    description: str = "Creates a welcome message for admitted students."

    def _run(self, student: Dict) -> str:
        return create_welcome_message(student)

# Tool for rejection message
class RejectionMessageCreatorTool(BaseTool):
    name: str = "RejectionMessageCreator"
    description: str = "Creates a rejection message for students who didn't meet criteria."

    def _run(self, student: Dict) -> str:
        return create_rejection_message(student)

# Tool for loan status message
class LoanStatusMessageCreatorTool(BaseTool):
    name: str = "LoanStatusMessageCreator"
    description: str = "Creates a loan status message based on approval status."

    def _run(self, input_data: Dict) -> str:
        student = input_data.get("student", {})
        status = input_data.get("status", "")
        amount = input_data.get("amount", 0)
        return create_loan_status_message(student, status, amount)

# Instances to use
create_welcome_message_tool = WelcomeMessageCreatorTool()
create_rejection_message_tool = RejectionMessageCreatorTool()
create_loan_status_message_tool = LoanStatusMessageCreatorTool()
