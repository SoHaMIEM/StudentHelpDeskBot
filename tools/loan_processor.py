# tools/loan_processor.py

MAX_LOAN_AMOUNT = 100000  # INR
MIN_PARENT_INCOME = 300000  # INR per year

def evaluate_loan_request(application: dict) -> dict:
    """Evaluate the student loan application."""
    requested_amount = application.get("requested_amount", 0)
    parent_income = application.get("parent_income", 0)

    if requested_amount > MAX_LOAN_AMOUNT:
        status = "Rejected: Requested amount exceeds maximum limit."
    elif parent_income < MIN_PARENT_INCOME:
        status = "Rejected: Parent income below minimum threshold."
    else:
        status = "Approved"

    return {
        "student_id": application.get("student_id"),
        "status": status,
        "approved_amount": requested_amount if status == "Approved" else 0
    }
