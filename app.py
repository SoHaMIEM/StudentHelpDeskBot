# app.py

import streamlit as st
from workflow.manager import AdmissionWorkflowManager
from rag.rag_chain import get_rag_chain
from data.load_data import save_sample_data
import json
import os

st.set_page_config(page_title="Student Admission Helpdesk", layout="wide")

# Initialize workflow manager in session state
if 'workflow_manager' not in st.session_state:
    st.session_state.workflow_manager = AdmissionWorkflowManager()

if 'report' not in st.session_state:
    st.session_state.report = None

def main():
    st.title("Student Admission Helpdesk")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Query Status", "Run Admission Process", "Student Records", "Reports"])
    
    if page == "Dashboard":
        show_dashboard()
    elif page == "Query Status":
        show_query_interface()
    elif page == "Run Admission Process":
        run_process_interface()
    elif page == "Student Records":
        show_student_records()
    else:
        show_reports()

def show_dashboard():
    st.header("Admission Process Dashboard")
    
    # Check if report exists
    if st.session_state.report:
        report = st.session_state.report
        
        # Display statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Total Applications", value=report["total_applications"])
        with col2:
            st.metric(label="Documents Verified", value=report["documents_validated"])
        with col3:
            st.metric(label="Shortlisted", value=report["shortlisted"])
            
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Loan Applications", value=report["loan_applications"])
        with col2:
            st.metric(label="Loans Approved", value=report["loans_approved"])
        with col3:
            st.metric(label="Total Loan Amount", value=f"₹{report['total_loan_amount']:,}")
    else:
        st.info("No admission report available. Please run the admission process first.")
    
    # Display timeline
    st.subheader("Admission Timeline")
    timeline_data = {
        "Application Start": "January 15, 2025",
        "Application End": "March 15, 2025",
        "Document Verification": "March 20, 2025",
        "Shortlisting": "March 25, 2025",
        "Loan Processing": "March 30, 2025",
        "Final Admission": "April 10, 2025"
    }
    
    for stage, date in timeline_data.items():
        st.write(f"**{stage}:** {date}")

def show_query_interface():
    st.header("Query Admission Status")
    
    query = st.text_area("Ask about admission process, status, or statistics:", height=100)
    
    if st.button("Submit Query"):
        if query:
            with st.spinner("Processing your query..."):
                # Use RAG chain to answer query
                try:
                    rag_chain = get_rag_chain()
                    response = rag_chain({"query": query})
                    
                    st.success("Query processed successfully!")
                    st.subheader("Response:")
                    st.write(response["result"])
                    
                    # Show source documents if available
                    if "source_documents" in response and response["source_documents"]:
                        with st.expander("Source Documents"):
                            for i, doc in enumerate(response["source_documents"]):
                                st.write(f"**Source {i+1}:**")
                                st.write(doc.page_content)
                                st.write("---")
                except Exception as e:
                    st.error(f"Error processing query: {str(e)}")
        else:
            st.warning("Please enter a query first.")

def run_process_interface():
    st.header("Run Admission Process")
    
    st.write("""This will execute the complete admission workflow:
    1. Document validation
    2. Shortlisting candidates
    3. Processing loan requests
    4. Sending communications
    5. Generating final reports
    """)
    
    # Option to generate sample data
    if st.button("Generate Sample Data"):
        with st.spinner("Generating sample student data..."):
            save_sample_data()
            st.success("Sample student data generated successfully!")
    
    if st.button("Start Admission Process"):
        with st.spinner("Running admission process..."):
            try:
                # Run the workflow
                result = st.session_state.workflow_manager.run_full_workflow()
                st.session_state.report = result
                
                st.success("Admission process completed successfully!")
                st.subheader("Process Summary:")
                st.json(result)
                
                # Display a progress bar for visual effect
                progress_bar = st.progress(0)
                for i in range(100):
                    import time
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
            except Exception as e:
                st.error(f"Error running admission process: {str(e)}")

def show_student_records():
    st.header("Student Records")
    
    # Load student data
    workflow_manager = st.session_state.workflow_manager
    if not workflow_manager.students:
        workflow_manager.load_data()
    
    if not workflow_manager.students:
        st.info("No student records found. Please generate sample data first.")
        return
    
    # Display student records
    st.subheader(f"Total Students: {len(workflow_manager.students)}")
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["All Students", "Shortlisted", "Loan Decisions"])
    
    with tab1:
        for student in workflow_manager.students:
            with st.expander(f"{student['name']} ({student['student_id']})"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Percentage:** {student['percentage']}%")
                    st.write(f"**Stream:** {student['stream']}")
                    st.write(f"**Age:** {student['age']}")
                with col2:
                    docs = student.get('documents', {})
                    st.write("**Documents:**")
                    for doc_name, doc_file in docs.items():
                        st.write(f"- {doc_name}: {doc_file}")
    
    with tab2:
        if not workflow_manager.shortlisted_students:
            st.info("No shortlisted students yet. Run the admission process first.")
        else:
            for student in workflow_manager.shortlisted_students:
                with st.expander(f"{student['name']} ({student['student_id']})"):
                    st.write(f"**Percentage:** {student['percentage']}%")
                    st.write(f"**Stream:** {student['stream']}")
    
    with tab3:
        if not workflow_manager.loan_decisions:
            st.info("No loan decisions yet. Run the admission process first.")
        else:
            for decision in workflow_manager.loan_decisions:
                status_color = "green" if decision["loan_status"] == "Approved" else "red"
                with st.expander(f"{decision['name']} ({decision['student_id']})"):
                    st.write(f"**Status:** :{status_color}[{decision['loan_status']}]")
                    if decision["approved_amount"] > 0:
                        st.write(f"**Approved Amount:** ₹{decision['approved_amount']:,}")

def show_reports():
    st.header("Admission Reports")
    
    if os.path.exists("reports/admission_report.json"):
        with open("reports/admission_report.json", "r") as f:
            report = json.load(f)
        
        st.subheader("Latest Admission Report")
        st.json(report)
        
        # Visualize report data
        st.subheader("Application Statistics")
        
        import matplotlib.pyplot as plt
        import numpy as np
        
        # Create a simple chart
        fig, ax = plt.subplots(figsize=(10, 6))
        
        labels = ['Total Applications', 'Valid Documents', 'Invalid Documents', 'Shortlisted']
        values = [
            report["total_applications"], 
            report["documents_valid"], 
            report["documents_invalid"], 
            report["shortlisted"]
        ]
        
        x = np.arange(len(labels))
        width = 0.6
        
        rects = ax.bar(x, values, width)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_title('Admission Process Statistics')
        
        # Add labels on bars
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., height + 0.5,
                    f'{int(height)}', ha='center', va='bottom')
        
        st.pyplot(fig)
        
        # Loan statistics
        st.subheader("Loan Statistics")
        
        fig2, ax2 = plt.subplots(figsize=(8, 8))
        
        loan_labels = ['Approved', 'Rejected']
        loan_values = [
            report["loans_approved"],
            report["loan_applications"] - report["loans_approved"]
        ]
        
        ax2.pie(loan_values, labels=loan_labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        ax2.set_title('Loan Approval Status')
        
        st.pyplot(fig2)
    else:
        st.info("No admission reports available. Please run the admission process first.")

if __name__ == "__main__":
    main()