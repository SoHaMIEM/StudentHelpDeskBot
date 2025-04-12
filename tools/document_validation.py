from typing import Any
from crewai.tools import BaseTool

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

class DocumentValidationTool(BaseTool):
    name: str = "DocumentValidator"
    description: str = "Validates student documents and checks for required files."

    def _run(self, documents: dict) -> dict:
        return validate_documents(documents)

document_validation_tool = DocumentValidationTool()
