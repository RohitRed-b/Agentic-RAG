# File: app/embedder.py
# Purpose: Embed chunked documents and store them in FAISS

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def embed_documents(chunks, model_name="sentence-transformers/all-mpnet-base-v2"):
    """
    Generate embeddings using HuggingFace and store in FAISS.
    """
    embedder = HuggingFaceEmbeddings(model_name=model_name)
    vectorstore = FAISS.from_documents(chunks, embedder)
    vectorstore.save_local("./vectorstore")
    return vectorstore
