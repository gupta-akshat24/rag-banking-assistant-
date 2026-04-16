import streamlit as st
from dotenv import load_dotenv
from utils.pdf_processor import process_pdfs
from utils.rag_engine import initialize_engine, query_engine
from whatsapp import send_whatsapp_message
import os

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="🏦 Banking Assistant",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 RAG-Powered Banking Assistant")
st.caption("Ask me anything about banking processes and documents")

# Sidebar for PDF upload
with st.sidebar:
    st.header("📄 Upload Bank Documents")
    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type="pdf",
        accept_multiple_files=True
    )

    if uploaded_files:
        with st.spinner("Processing documents..."):
            process_pdfs(uploaded_files)
            st.success(f"✅ {len(uploaded_files)} document(s) loaded!")

    st.divider()

    # WhatsApp Section
    st.header("📱 Send via WhatsApp")
    phone_number = st.text_input(
        "Enter WhatsApp number",
        placeholder="+1234567890"
    )

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "index" not in st.session_state:
    st.session_state.index = None

# Load index if PDFs processed
if uploaded_files and st.session_state.index is None:
    st.session_state.index = initialize_engine()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about any banking process..."):
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        if st.session_state.index:
            with st.spinner("Searching documents..."):
                response = query_engine(
                    st.session_state.index,
                    prompt
                )
                st.markdown(response)

                # WhatsApp send button
                if phone_number:
                    if st.button("📱 Send via WhatsApp"):
                        send_whatsapp_message(phone_number, response)
                        st.success("✅ Sent on WhatsApp!")
        else:
            response = "⚠️ Please upload bank documents first!"
            st.warning(response)

    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
