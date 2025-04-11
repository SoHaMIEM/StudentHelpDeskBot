# tools/communication.py

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
