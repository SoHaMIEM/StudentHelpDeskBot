# tools/document_validation.py

from crewai_tools import FunctionTool

REQUIRED_DOCUMENTS = [
    "identity_proof",
    "marksheet_12th",
    "passport_photo",
    "address_proof"
]

def validate_documents(documents: dict) -> dict:
    """Validates if all required documents are submitted."""
    missing_docs = [doc for doc in REQUIRED_DOCUMENTS if doc not in documents]
    is_valid = len(missing_docs) == 0
    return {
        "valid": is_valid,
        "missing": missing_docs
    }

document_validation_tool = FunctionTool.from_defaults(
    name="DocumentValidator",
    description="Validates student documents and checks for required files.",
    func=validate_documents
)













# # *2. Create: helpers/document_verifier.py
# # 📌 This handles PDF reading + matching with CSV + validation messages.*
# # # _define-ocg_
# import fitz  # PyMuPDF
# import pandas as pd

# def extract_text_from_pdf(uploaded_file):
#     doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     return text.lower()

# def verify_document(uploaded_file):
#     static_db = pd.read_csv("static_db.csv")
#     extracted_text = extract_text_from_pdf(uploaded_file)

#     for _, row in static_db.iterrows():
#         # Extract values for comparison
#         name = row['StudentName'].lower()
#         father = row['FatherName'].lower()
#         mother = row['MotherName'].lower()
#         dob = str(row['DOB']).lower()
#         passing_year = str(row['PassingYear']).lower()
#         photo_id = row['PhotoID'].lower()
#         phy = str(row['Physics']).lower()
#         chem = str(row['Chemistry']).lower()
#         maths = str(row['Maths']).lower()

#         checks = {
#             "Student Name": name in extracted_text,
#             "Father's Name": father in extracted_text,
#             "Mother's Name": mother in extracted_text,
#             "Photo ID": photo_id in extracted_text,
#             "Date of Birth": dob in extracted_text,
#             "Passing Year": passing_year in extracted_text,
#             "Physics Marks": phy in extracted_text,
#             "Chemistry Marks": chem in extracted_text,
#             "Maths Marks": maths in extracted_text
#         }

#         if all(checks.values()):
#             return f"""
# ✅ Document Verified Successfully!

# *Student Name:* {row['StudentName']}
# *Father's Name:* {row['FatherName']}
# *Mother's Name:* {row['MotherName']}
# *Photo ID:* {row['PhotoID']}
# *DOB:* {row['DOB']}
# *Passing Year:* {row['PassingYear']}
# *Physics:* {row['Physics']}
# *Chemistry:* {row['Chemistry']}
# *Maths:* {row['Maths']}

# 🎯 This student is eligible for the shortlisting phase.
# """
#         else:
#             error_fields = [field for field, ok in checks.items() if not ok]
#             return f"❌ Verification failed. Issues found in: {', '.join(error_fields)}."

#     return "❌ No matching record found in the database."