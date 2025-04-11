# data/load_data.py

import os
import json
from data.sample_students import sample_students

def save_sample_data():
    """Save sample student data to JSON files for processing."""
    data_dir = "data/student_submissions"
    
    # Create directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)
    
    for student in sample_students:
        student_id = student["student_id"]
        file_path = os.path.join(data_dir, f"{student_id}.json")
        
        with open(file_path, 'w') as f:
            json.dump(student, f, indent=4)
            
    print(f"Saved {len(sample_students)} student records to {data_dir}")

def load_student_data():
    """Load all student data from JSON files."""
    data_dir = "data/student_submissions"
    students = []
    
    if not os.path.exists(data_dir):
        print(f"Directory {data_dir} does not exist. No student data loaded.")
        return []
    
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(data_dir, filename)
            with open(file_path, 'r') as f:
                student = json.load(f)
                students.append(student)
    
    return students