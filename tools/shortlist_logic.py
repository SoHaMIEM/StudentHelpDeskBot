# tools/shortlist_logic.py

ELIGIBILITY_CRITERIA = {
    "min_percentage": 75,
    "accepted_streams": ["Science", "Commerce", "Arts"]
}

UNIVERSITY_CAPACITY = 100  # Example: Only 100 seats available

def check_eligibility(student: dict) -> bool:
    """Check if student meets the eligibility criteria."""
    percentage = student.get("percentage", 0)
    stream = student.get("stream", "")

    return (
        percentage >= ELIGIBILITY_CRITERIA["min_percentage"] and
        stream in ELIGIBILITY_CRITERIA["accepted_streams"]
    )

def shortlist_students(all_students: list) -> list:
    """Shortlist students based on eligibility and university capacity."""
    eligible = [s for s in all_students if check_eligibility(s)]
    return eligible[:UNIVERSITY_CAPACITY]
