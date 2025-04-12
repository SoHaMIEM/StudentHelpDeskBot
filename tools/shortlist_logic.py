from typing import List, Dict
from crewai.tools import BaseTool

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

def shortlist_students(all_students: List[dict]) -> List[dict]:
    """Shortlist students based on eligibility and university capacity."""
    eligible = [s for s in all_students if check_eligibility(s)]
    return eligible[:UNIVERSITY_CAPACITY]

# Tool class for checking eligibility
class EligibilityCheckerTool(BaseTool):
    name: str = "EligibilityChecker"
    description: str = "Checks if a student meets the eligibility criteria for admission."

    def _run(self, student: dict) -> bool:
        return check_eligibility(student)

# Tool class for shortlisting students
class StudentShortlisterTool(BaseTool):
    name: str = "StudentShortlister"
    description: str = "Shortlists eligible students based on criteria and university capacity."

    def _run(self, all_students: List[dict]) -> List[dict]:
        return shortlist_students(all_students)

# Instances to be used in tasks
check_eligibility_tool = EligibilityCheckerTool()
shortlist_students_tool = StudentShortlisterTool()
