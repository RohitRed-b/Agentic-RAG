# ⚖️ Agentic RAG on AWS for Legal & Compliance Document Automation

> Automating legal document analysis with LangChain Agents, Hugging Face LLMs, FAISS, and AWS serverless stack.

---

## 🚀 Overview

This project implements an **Agentic Retrieval-Augmented Generation (RAG)** system using **LangChain Agents** and a **serverless AWS architecture**. The system processes and analyzes legal and compliance documents (CUAD dataset), enabling intelligent querying, summarization, and clause extraction through **LLM-driven agents**.

> ⚡ Outperforms traditional RAG by enabling autonomous reasoning, tool usage, and multi-step decision making.

---

## 🧠 Key Features

- 🧾 **CUAD-based legal document understanding**
- 🤖 **LangChain Agents** for intelligent control flow and reasoning
- 🧠 **Falcon-7B-Instruct LLM** via Hugging Face Hub
- 📚 **FAISS** for fast vector retrieval
- 🛠️ Serverless compute with **AWS Lambda + API Gateway**
- ☁️ **S3 integration** to load documents on-demand
- 🧩 Designed to be extensible with **Bedrock** and **SageMaker**

---

## 🔧 Technologies Used

| Layer              | Tool/Service                               |
|-------------------|--------------------------------------------|
| Embeddings         | `sentence-transformers/all-mpnet-base-v2` |
| LLM Inference      | `Falcon-7B-Instruct` via Hugging Face Hub |
| Document Store     | FAISS (local vector DB)                   |
| Orchestration      | LangChain Agents                          |
| Cloud Compute      | AWS Lambda                                |
| API Layer          | API Gateway                               |
| File Storage       | AWS S3                                     |
| Optional Extension | Amazon Bedrock, SageMaker                 |

---

Install dependencies 
pip install -r requirements.txt

Download Dataset:
https://github.com/TheAtticusProject/cuad
Credits: TheAtticusProject 

☁️ Serverless Deployment (AWS Lambda)

Zip the Lambda function

mkdir deployment && cd deployment
cp -r ../app . && cp ../lambda/handler.py . && cp ../lambda/requirements.txt .
pip install -r requirements.txt -t .
zip -r lambda.zip .

Deploy to AWS Lambda
Upload lambda.zip

Set runtime to Python 3.9 or 3.11
Set handler to handler.lambda_handler

Connect API Gateway
Create a REST API trigger to invoke Lambda

IAM Permissions
Ensure Lambda has S3 read access if using S3 integration


🧪 Sample API Request
{
  "query": "List GDPR compliance clauses",
  "doc_key": "contracts/nda_sample.txt"
}


🧠 Extend It With

🔁 SageMaker: Serve custom or fine-tuned LLMs
💬 Bedrock: Use Claude or Amazon Titan for enterprise-grade inference
🖼️ Streamlit UI: Add a front-end for interactive demos
🧾 PDF Parsing: Extend to process scanned contracts or structured PDFs







