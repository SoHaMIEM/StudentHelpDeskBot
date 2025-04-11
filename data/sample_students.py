# data/sample_students.py

sample_students = [
    {
        "student_id": "STU2025001",
        "name": "Rahul Sharma",
        "percentage": 82.5,
        "stream": "Science",
        "age": 18,
        "documents": {
            "identity_proof": "aadhar_card.pdf",
            "marksheet_12th": "marksheet.pdf",
            "passport_photo": "photo.jpg",
            "address_proof": "electricity_bill.pdf"
        },
        "loan_application": {
            "student_id": "STU2025001",
            "requested_amount": 75000,
            "parent_income": 450000
        }
    },
    {
        "student_id": "STU2025002",
        "name": "Priya Patel",
        "percentage": 91.2,
        "stream": "Science",
        "age": 19,
        "documents": {
            "identity_proof": "passport.pdf",
            "marksheet_12th": "marksheet.pdf",
            "passport_photo": "photo.jpg"
            # Missing address_proof
        },
        "loan_application": {
            "student_id": "STU2025002",
            "requested_amount": 50000,
            "parent_income": 600000
        }
    },
    {
        "student_id": "STU2025003",
        "name": "Amit Kumar",
        "percentage": 72.8,  # Below minimum percentage
        "stream": "Commerce",
        "age": 18,
        "documents": {
            "identity_proof": "aadhar_card.pdf",
            "marksheet_12th": "marksheet.pdf",
            "passport_photo": "photo.jpg",
            "address_proof": "utility_bill.pdf"
        },
        "loan_application": {
            "student_id": "STU2025003",
            "requested_amount": 90000,
            "parent_income": 350000
        }
    },
    {
        "student_id": "STU2025004",
        "name": "Meera Singh",
        "percentage": 85.3,
        "stream": "Arts",
        "age": 19,
        "documents": {
            "identity_proof": "aadhar_card.pdf",
            "marksheet_12th": "marksheet.pdf",
            "passport_photo": "photo.jpg",
            "address_proof": "rental_agreement.pdf"
        },
        "loan_application": {
            "student_id": "STU2025004",
            "requested_amount": 120000,  # Exceeds maximum loan amount
            "parent_income": 550000
        }
    },
    {
        "student_id": "STU2025005",
        "name": "Arjun Reddy",
        "percentage": 79.4,
        "stream": "Science",
        "age": 20,
        "documents": {
            "identity_proof": "aadhar_card.pdf",
            "marksheet_12th": "marksheet.pdf",
            "passport_photo": "photo.jpg",
            "address_proof": "bank_statement.pdf"
        },
        "loan_application": {
            "student_id": "STU2025005",
            "requested_amount": 80000,
            "parent_income": 250000  # Below minimum parent income
        }
    }
]