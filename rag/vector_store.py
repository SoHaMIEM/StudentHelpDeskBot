# rag/vector_store.py

import os
from langchain.vectorstores import Chroma
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.docstore.document import Document

CHROMA_PATH = "chroma_db"

def get_vectorstore(persist_directory=CHROMA_PATH):
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding,
    )
    return vectordb

def save_documents_to_vectorstore(docs, persist_directory=CHROMA_PATH):
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        persist_directory=persist_directory,
    )
    vectordb.persist()
    return vectordb

