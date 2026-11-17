from pathlib import Path

from langchain_community.vectorstores import FAISS

from rag.embeddings import get_embedding_model


VECTOR_STORE_PATH = "data/faiss_index"


def create_vector_store(chunks):
    """
    Create a FAISS vector store from document chunks.
    """

    embedding_model = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store


def save_vector_store(vector_store):
    """
    Save the FAISS index locally.
    """

    Path(VECTOR_STORE_PATH).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    vector_store.save_local(VECTOR_STORE_PATH)

    print(f"FAISS index saved to: {VECTOR_STORE_PATH}")


def load_vector_store():
    """
    Load an existing FAISS index.
    """

    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store