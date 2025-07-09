# File: lambda/handler.py
# Loads document from S3, processes with RAG agent, returns answer

import boto3
import os
from app.rag_chain import load_vectorstore, build_retrieval_chain
from app.agent_executor import build_agent, run_agent

s3 = boto3.client("s3")
BUCKET_NAME = "rag-legal-docs"

# Load once during cold start
vectorstore = load_vectorstore("./vectorstore")
qa_chain = build_retrieval_chain(vectorstore)
agent = build_agent(qa_chain)

def load_document_from_s3(key):
    response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    text = response["Body"].read().decode("utf-8")
    return text

def lambda_handler(event, context):
    try:
        query = event.get("query", "")
        doc_key = event.get("doc_key", "")

        if not query or not doc_key:
            return {
                "statusCode": 400,
                "body": "Missing 'query' or 'doc_key' in request."
            }

        document_text = load_document_from_s3(doc_key)
        

        response = run_agent(agent, query)
        return {
            "statusCode": 200,
            "body": response
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
