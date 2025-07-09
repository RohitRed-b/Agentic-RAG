# File: app/rag_chain.py
# Purpose: Load vectorstore and build RetrievalQA chain

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA

def load_vectorstore(path="./vectorstore"):
    """
    Load FAISS vectorstore from disk.
    """
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    return FAISS.load_local(path, embedding)

def build_retrieval_chain(vectorstore):
    """
    Create a RetrievalQA chain using a language model and retriever.
    """
    llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct", model_kwargs={"temperature": 0.1, "max_new_tokens": 512})
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
