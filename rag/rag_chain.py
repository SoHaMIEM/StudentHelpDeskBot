# rag/rag_chain.py

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatGoogleGenerativeAI
from rag.vector_store import get_vectorstore
from llm_config import llm

def get_rag_chain():
    vectordb = get_vectorstore()
    retriever = vectordb.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
    )

    return qa_chain
