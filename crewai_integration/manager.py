# crewai_integration/manager.py

from workflow.manager import AdmissionWorkflowManager
from crew.crew_setup import run_admission_crew
import json
import os

class CrewAIAdmissionManager:
    """
    This class bridges the workflow manager with the CrewAI agents.
    It prepares the data for CrewAI agents and processes their outputs.
    """
    
    def __init__(self):
        self.workflow_manager = AdmissionWorkflowManager()
        
    def prepare_data_for_agents(self):
        """Prepare student data in a format suitable for CrewAI agents."""
        # Load student data
        self.workflow_manager.load_data()
        
        # Create agent input directory if it doesn't exist
        os.makedirs("data/agent_inputs", exist_ok=True)
        
        # Prepare data for document checker
        document_checker_data = []
        for student in self.workflow_manager.students:
            document_checker_data.append({
                "student_id": student["student_id"],
                "name": student["name"],
                "documents": student.get("documents", {})
            })
        
        with open("data/agent_inputs/document_checker_input.json", "w") as f:
            json.dump(document_checker_data, f, indent=4)
        
        # Prepare data for shortlister
        shortlister_data = []
        for student in self.workflow_manager.students:
            shortlister_data.append({
                "student_id": student["student_id"],
                "name": student["name"],
                "percentage": student["percentage"],
                "stream": student["stream"],
                "age": student["age"]
            })
        
        with open("data/agent_inputs/shortlister_input.json", "w") as f:
            json.dump(shortlister_data, f, indent=4)
        
        # Prepare data for loan agent
        loan_agent_data = []
        for student in self.workflow_manager.students:
            if "loan_application" in student:
                loan_agent_data.append(student["loan_application"])
        
        with open("data/agent_inputs/loan_agent_input.json", "w") as f:
            json.dump(loan_agent_data, f, indent=4)
        
    def process_agent_outputs(self):
        """Process the outputs from CrewAI agents and update the workflow."""
        # Directory for agent outputs
        agent_output_dir = "data/agent_outputs"
        
        # Process document checker output
        if os.path.exists(f"{agent_output_dir}/document_validation_results.json"):
            with open(f"{agent_output_dir}/document_validation_results.json", "r") as f:
                doc_results = json.load(f)
                
            self.workflow_manager.validated_students = doc_results
        
        # Process shortlister output
        if os.path.exists(f"{agent_output_dir}/shortlisted_students.json"):
            with open(f"{agent_output_dir}/shortlisted_students.json", "r") as f:
                shortlisted = json.load(f)
                
            # Update the workflow manager with shortlisted students
            shortlisted_ids = [s["student_id"] for s in shortlisted]
            self.workflow_manager.shortlisted_students = [
                s for s in self.workflow_manager.students 
                if s["student_id"] in shortlisted_ids
            ]
        
        # Process loan agent output
        if os.path.exists(f"{agent_output_dir}/loan_decisions.json"):
            with open(f"{agent_output_dir}/loan_decisions.json", "r") as f:
                loan_decisions = json.load(f)
                
            self.workflow_manager.loan_decisions = loan_decisions
        
        # Generate communications
        self.workflow_manager.generate_communications()
        
        # Generate final report
        report = self.workflow_manager.generate_final_report()
        
        return report
        
    def run_crew_workflow(self):
        """Run the complete workflow using CrewAI agents."""
        # Step 1: Prepare data for agents
        self.prepare_data_for_agents()
        
        # Step 2: Run CrewAI
        try:
            crew_result = run_admission_crew()
            print("CrewAI execution completed:")
            print(crew_result)
        except Exception as e:
            print(f"Error running CrewAI: {str(e)}")
            # Fallback to direct workflow
            return self.workflow_manager.run_full_workflow()
        
        # Step 3: Process agent outputs
        report = self.process_agent_outputs()
        
        return report