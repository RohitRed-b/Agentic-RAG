# File: app/loader.py
# Purpose: Load and preprocess CUAD legal dataset

import os
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_cuad_data(data_dir: str = "./cuad"):
    """
    Load CUAD JSON files, extract clauses as documents.
    """
    documents = []
    for file in os.listdir(data_dir):
        if file.endswith(".json"):
            with open(os.path.join(data_dir, file), 'r') as f:
                content = json.load(f)
                for section in content.get("annotations", []):
                    clause = section.get("text", "")
                    if clause:
                        documents.append(clause)
    return documents


def split_documents(docs):
    """
    Chunk documents into smaller pieces for vector DB.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.create_documents(docs)
