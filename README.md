⚖️ Agentic RAG on AWS for Legal & Compliance Document Automation
Automating legal document analysis with LangChain Agents, Hugging Face LLMs, FAISS, and AWS serverless stack.
🚀 Overview
This project implements an Agentic Retrieval-Augmented Generation (RAG) system using LangChain Agents and a serverless AWS architecture. The system processes and analyzes legal and compliance documents (CUAD dataset), enabling intelligent querying, summarization, and clause extraction through LLM-driven agents.
⚡ Outperforms traditional RAG by enabling autonomous reasoning, tool usage, and multi-step decision making.
🧠 Key Features
🧾 CUAD-based legal document understanding
🤖 LangChain Agents for intelligent control flow and reasoning
🧠 Google FLAN-T5 Small via Hugging Face Hub (lightweight & cost-efficient)
📚 FAISS for fast vector retrieval
🛠️ Serverless compute with AWS Lambda + API Gateway
☁️ S3 integration to load documents on-demand
🧩 Designed to be extensible with Bedrock and SageMaker
🔧 Technologies Used
Layer	Tool/Service
Embeddings	sentence-transformers/all-mpnet-base-v2
LLM Inference	FLAN-T5 Small via Hugging Face Hub
Document Store	FAISS (local vector DB)
Orchestration	LangChain Agents
Cloud Compute	AWS Lambda
API Layer	API Gateway
File Storage	AWS S3
Optional Extension	Amazon Bedrock, SageMaker
Why FLAN-T5 Small?
🪶 Lightweight & serverless-friendly – ideal for Lambda deployment
🚀 Fast inference for prototyping and demos
🔄 Easily swappable with larger models (Falcon, Claude, Bedrock models) when scaling
