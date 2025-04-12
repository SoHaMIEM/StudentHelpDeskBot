from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document

CHROMA_PATH = "chroma_db"

def get_vectorstore(persist_directory=CHROMA_PATH):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding,
    )
    return vectordb

def save_documents_to_vectorstore(docs, persist_directory=CHROMA_PATH):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        persist_directory=persist_directory,
    )
    vectordb.persist()
    return vectordb
