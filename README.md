# 🚀 Bedrock AI Services Playground

A modular and production-oriented project for experimenting with Amazon Bedrock capabilities, including text generation, image generation, embeddings, and Retrieval-Augmented Generation (RAG).

This repository is designed as a hands-on environment for building real-world AI services using AWS infrastructure and modern LLM workflows.

---

## 🧠 Features

* ✍️ Text Generation (LLM-based APIs)
* 🖼️ Image Generation (Titan Image Generator)
* 🔎 Embeddings & Semantic Search
* 📚 RAG (Retrieval-Augmented Generation)
* ⚙️ Service-based architecture (Lambda-ready structure)
* ☁️ AWS integration (Bedrock, S3, Agents)

---

## 📁 Project Structure

```bash
src/
├── 0_intro/        # Basic concepts & experiments
├── 1_text/         # Text generation examples
├── 2_image/        # Image generation pipelines
├── 3_embedding/    # Embedding & vector-related logic
├── 4_langchain/    # LangChain experiments
├── 5_services/     # Production-style services
│   ├── image/      # Image generation API
│   ├── rag/        # RAG (Bedrock Agent Runtime)
│   └── text/       # Text summarization API
```

---

## ⚙️ Tech Stack

* Python 3.13
* AWS Bedrock (LLMs, Agents, Knowledge Base)
* AWS Lambda (serverless execution)
* Amazon S3 (storage)
* boto3 (AWS SDK)
* LangChain (experimental workflows)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/bedrock-ai-services.git
cd bedrock-ai-services
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure AWS

Make sure AWS CLI is configured:

```bash
aws configure
```

Or use SSO/profile if required.

---

## 🔌 Example Services

### 🔹 Text Summarization

* Input: raw text
* Output: structured summary using LLaMA

---

### 🔹 Image Generation

* Input: prompt
* Output: generated image stored in S3 + signed URL

---

### 🔹 RAG (Knowledge Base)

* Input: user question
* Output: context-aware answer using Bedrock Agent Runtime

---

## 🧩 Infrastructure

This project is designed to be extended with:

* AWS CDK (recommended)
* Terraform (optional)
* API Gateway + Lambda deployment

---

## ⚠️ Notes

* Ensure correct AWS region alignment (Bedrock + S3)
* Signed URLs require proper S3 configuration
* Bedrock models are region-specific
* IAM permissions must be properly configured

---

## 🎯 Roadmap

* [ ] Add full CDK deployment
* [ ] Improve RAG pipeline with custom prompts
* [ ] Add streaming responses
* [ ] Production-ready API layer
* [ ] Add monitoring & logging

---

## 🤝 Contributing

This is a personal playground project, but feel free to explore, fork, and experiment.

---

## 📌 Final Thought

> LLM alone is just a toy.
> LLM + Retrieval + Infrastructure = real system.

---

## 👤 Author

Built with frustration, curiosity, and too many AWS errors 😄
