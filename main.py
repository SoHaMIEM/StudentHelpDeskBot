# main.py

import os
from dotenv import load_dotenv
from crew.crew_setup import run_admission_crew
from langchain.chat_models import ChatGoogleGenerativeAI

# RAG: Document preprocessing & vector store setup
from rag.document_loader import load_documents, split_documents
from rag.vector_store import save_documents_to_vectorstore

def populate_chromadb():
    """Loads and embeds static documents into ChromaDB."""
    print("\n📚 Initializing ChromaDB with static documents...")
    docs = load_documents()
    chunks = split_documents(docs)
    save_documents_to_vectorstore(chunks)
    print("✅ ChromaDB initialized and documents embedded.\n")

def main():
    # Load environment variables from .env
    load_dotenv()

    # Step 1: Initialize ChromaDB
    populate_chromadb()

    # Step 2: Load Gemini (Langchain wrapper)
    print("🤖 Loading Gemini model for CrewAI...")
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.3,
        verbose=True
    )

    # Step 3: Run CrewAI with agents and tasks
    print("\n🎓 Running the Student Admission Helpdesk system...\n")
    result = run_admission_crew()
    print(f"Result: {result}")

if __name__ == "__main__":
    main()