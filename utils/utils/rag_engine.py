import os
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings
)
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

DATA_DIR = "data/"

def initialize_engine():
    """
    Read all PDFs from data directory
    and build a VectorStoreIndex
    """
    # Configure LLM and embedding model
    Settings.llm = OpenAI(
        model="gpt-3.5-turbo",
        temperature=0.2
    )
    Settings.embed_model = OpenAIEmbedding(
        model="text-embedding-ada-002"
    )

    # Load documents from data directory
    documents = SimpleDirectoryReader(DATA_DIR).load_data()

    # Build index
    index = VectorStoreIndex.from_documents(
        documents,
        show_progress=True
    )

    return index


def query_engine(index, question):
    """
    Query the index with a user question
    and return a response
    """
    engine = index.as_query_engine(
        similarity_top_k=3,
        response_mode="compact"
    )

    response = engine.query(
        f"""You are a helpful banking assistant.
        Answer based strictly on the provided documents.
        If information is not in documents, say so clearly.
        
        Question: {question}
        """
    )

    return str(response)
