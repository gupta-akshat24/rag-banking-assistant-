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

## ⚙️ Personal Setup

### 1. Install dependencies
pip install -r requirements.txt

### 2. Add your API keys
Create a .env file in root folder and add:
OPENAI_API_KEY=your_openai_api_key_here
TWILIO_ACCOUNT_SID=your_twilio_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_WHATSAPP_NUMBER=+14155238886

### 3. Add bank documents
Drop your bank PDF files into:
data/

### 4. Run the app
streamlit run app.py

---

## 📁 Project Structure
rag-banking-assistant/
│
├── app.py                  → Main Streamlit application
├── whatsapp.py             → WhatsApp integration
├── requirements.txt        → All dependencies
├── .env                    → Your API keys (never share)
├── .env.example            → API key template
├── .gitignore              → Files hidden from GitHub
│
├── utils/
│   ├── pdf_processor.py    → PDF reading and saving
│   └── rag_engine.py       → RAG pipeline and querying
│
├── data/                   → Your bank PDFs go here
└── assets/                 → Screenshots and images

---

## 📱 How To Use
1. Run the app with streamlit run app.py
2. Upload bank PDF documents from sidebar
3. Ask any question about banking processes
4. Get instant answers from your documents
5. Send answers directly to WhatsApp if needed

---

## 🔒 Security Notes
- .env file is private and never pushed to GitHub
- All bank PDFs stored locally on your machine
- Repository is private — only accessible by you
- API keys secured via environment variables

---

## 📝 Personal Notes
# Add your own notes here
# e.g. which banks you have added
# e.g. what documents are indexed
# e.g. future improvements you want to make

---

*🏦 Built for personal banking document management*
