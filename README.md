# rag-banking-assistant-
RAG-powered banking assistant for instant document Q&amp;A

# 🏦 RAG-Powered Banking Assistant

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-0.10-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Overview
An intelligent banking assistant that centralizes open-source 
bank documents into a RAG pipeline, enabling instant process 
lookups and WhatsApp delivery of required documents.

## ✨ Features
- 📄 Upload and index multiple bank PDF documents
- 💬 Natural language Q&A on banking processes
- 🔍 Semantic search across all documents
- 📱 WhatsApp integration for document delivery
- 🔒 Secure API key management

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| LlamaIndex | RAG pipeline and document indexing |
| OpenAI GPT-3.5-turbo | Answer generation |
| text-embedding-ada-002 | Vector embeddings |
| Streamlit | Chat interface |
| pypdf | PDF text extraction |
| Twilio | WhatsApp integration |
| python-dotenv | API key management |

## ⚙️ Setup

### 1. Clone the repository
git clone https://github.com/yourusername/rag-banking-assistant.git
cd rag-banking-assistant

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure environment variables
cp .env.example .env
# Add your API keys to .env

### 4. Run the app
streamlit run app.py

## 📱 WhatsApp Setup
1. Create a Twilio account at twilio.com
2. Enable WhatsApp sandbox
3. Add Twilio credentials to .env

## 🔒 Security
- Never commit your .env file
- All API keys stored as environment variables
- PDFs stored locally, never pushed to GitHub

## 📜 License
MIT License — free to use and modify
