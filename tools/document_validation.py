# tools/document_validation.py

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
