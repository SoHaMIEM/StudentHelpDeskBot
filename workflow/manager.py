# workflow/manager.py

from data.load_data import save_sample_data, load_student_data
from tools.document_validation import validate_documents
from tools.shortlist_logic import check_eligibility, shortlist_students
from tools.loan_processor import evaluate_loan_request
from tools.communication import create_welcome_message, create_rejection_message, create_loan_status_message
import json
import os

class AdmissionWorkflowManager:
    def __init__(self):
        self.students = []
        self.validated_students = []
        self.shortlisted_students = []
        self.loan_decisions = []
        self.communications = []
        
    def load_data(self):
        """Load sample student data."""
        self.students = load_student_data()
        return len(self.students)
        
    def validate_all_documents(self):
        """Run document validation for all students."""
        self.validated_students = []
        
        for student in self.students:
            result = validate_documents(student.get("documents", {}))
            student["validation_result"] = result
            self.validated_students.append({
                "student_id": student["student_id"],
                "name": student["name"],
                "is_valid": result["valid"],
                "missing_docs": result["missing"]
            })
            
        return self.validated_students
    
    def run_shortlisting(self):
        """Shortlist eligible students."""
        # Only consider students with valid documents
        valid_students = [s for s in self.students if s.get("validation_result", {}).get("valid", False)]
        self.shortlisted_students = shortlist_students(valid_students)
        
        return [{
            "student_id": s["student_id"],
            "name": s["name"],
            "percentage": s["percentage"],
            "stream": s["stream"]
        } for s in self.shortlisted_students]
    
    def process_loans(self):
        """Process loan applications for shortlisted students."""
        shortlisted_ids = [s["student_id"] for s in self.shortlisted_students]
        loan_applicants = [s for s in self.students if s["student_id"] in shortlisted_ids and "loan_application" in s]
        
        self.loan_decisions = []
        for student in loan_applicants:
            loan_result = evaluate_loan_request(student["loan_application"])
            self.loan_decisions.append({
                "student_id": student["student_id"],
                "name": student["name"],
                "loan_status": loan_result["status"],
                "approved_amount": loan_result["approved_amount"]
            })
        
        return self.loan_decisions
    
    def generate_communications(self):
        """Generate communication emails for all students."""
        self.communications = []
        
        # Get IDs of shortlisted students
        shortlisted_ids = [s["student_id"] for s in self.shortlisted_students]
        
        # Get loan decisions
        loan_decisions_dict = {ld["student_id"]: ld for ld in self.loan_decisions}
        
        for student in self.students:
            student_id = student["student_id"]
            
            # Generate communication based on status
            if student_id in shortlisted_ids:
                # Student is shortlisted
                welcome_email = create_welcome_message(student)
                self.communications.append({
                    "student_id": student_id,
                    "name": student["name"],
                    "type": "admission_acceptance",
                    "content": welcome_email
                })
                
                # Check if student has loan decision
                if student_id in loan_decisions_dict:
                    loan_decision = loan_decisions_dict[student_id]
                    loan_email = create_loan_status_message(
                        student, 
                        loan_decision["loan_status"], 
                        loan_decision["approved_amount"]
                    )
                    self.communications.append({
                        "student_id": student_id,
                        "name": student["name"],
                        "type": "loan_status",
                        "content": loan_email
                    })
            else:
                # Student is not shortlisted
                rejection_email = create_rejection_message(student)
                self.communications.append({
                    "student_id": student_id,
                    "name": student["name"],
                    "type": "admission_rejection",
                    "content": rejection_email
                })
        
        return self.communications
    
    def generate_final_report(self):
        """Generate a comprehensive final report of the admission process."""
        report = {
            "total_applications": len(self.students),
            "documents_validated": len(self.validated_students),
            "documents_valid": len([s for s in self.validated_students if s["is_valid"]]),
            "documents_invalid": len([s for s in self.validated_students if not s["is_valid"]]),
            "shortlisted": len(self.shortlisted_students),
            "loan_applications": len(self.loan_decisions),
            "loans_approved": len([ld for ld in self.loan_decisions if ld["loan_status"] == "Approved"]),
            "total_loan_amount": sum([ld["approved_amount"] for ld in self.loan_decisions]),
            "communications_sent": len(self.communications)
        }
        
        # Save report to file
        os.makedirs("reports", exist_ok=True)
        with open("reports/admission_report.json", "w") as f:
            json.dump(report, f, indent=4)
        
        return report
    
    def run_full_workflow(self):
        """Run the complete admission workflow."""
        # Step 1: Load data
        print(f"Loaded {self.load_data()} student applications")
        
        # Step 2: Validate documents
        print("Validating documents...")
        validated = self.validate_all_documents()
        print(f"Document validation complete. {len([v for v in validated if v['is_valid']])} valid, {len([v for v in validated if not v['is_valid']])} invalid")
        
        # Step 3: Shortlist students
        print("Shortlisting eligible students...")
        shortlisted = self.run_shortlisting()
        print(f"Shortlisting complete. {len(shortlisted)} students shortlisted")
        
        # Step 4: Process loans
        print("Processing loan applications...")
        loan_results = self.process_loans()
        print(f"Loan processing complete. {len([lr for lr in loan_results if lr['loan_status'] == 'Approved'])} approved, {len([lr for lr in loan_results if lr['loan_status'] != 'Approved'])} rejected")
        
        # Step 5: Generate communications
        print("Generating communications...")
        communications = self.generate_communications()
        print(f"Generated {len(communications)} communication emails")
        
        # Step 6: Generate final report
        print("Generating final report...")
        report = self.generate_final_report()
        
        return report