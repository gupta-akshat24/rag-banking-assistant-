import os
from pypdf import PdfReader

DATA_DIR = "data/"

def process_pdfs(uploaded_files):
    """
    Save uploaded PDFs to data directory
    for LlamaIndex to process
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    for uploaded_file in uploaded_files:
        file_path = os.path.join(DATA_DIR, uploaded_file.name)

        # Save PDF to data folder
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    return True


def extract_text_from_pdf(file_path):
    """
    Extract raw text from a PDF file
    """
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text
