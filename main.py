# File: main.py
# Purpose: End-to-end local pipeline for Agentic RAG on legal documents

from app.loader import load_cuad_data, split_documents
from app.embedder import embed_documents
from app.rag_chain import load_vectorstore, build_retrieval_chain
from app.agent_executor import build_agent, run_agent
import os

def build_vectorstore_if_needed():
    """
    Check if FAISS vectorstore exists locally, if not, build it from CUAD data.
    """
    vectorstore_path = "./vectorstore/index.faiss"
    if os.path.exists(vectorstore_path):
        print("Vectorstore already exists. Loading from disk...")
        return load_vectorstore("./vectorstore")
    else:
        print("Vectorstore not found. Building from CUAD dataset...")
        raw_docs = load_cuad_data("./cuad")
        chunks = split_documents(raw_docs)
        print(f"Loaded and split {len(chunks)} chunks from CUAD.")
        return embed_documents(chunks)

def run_local_agent_demo():
    """
    Load the agent and run a sample query.
    """
    vectorstore = build_vectorstore_if_needed()
    qa_chain = build_retrieval_chain(vectorstore)
    agent = build_agent(qa_chain)

    # Sample query for testing
    query = "List all clauses related to GDPR in this contract"
    print(f"\nRunning agent on query:\n{query}\n")
    response = run_agent(agent, query)
    print("Agent Response:\n", response)

if __name__ == "__main__":
    run_local_agent_demo()
