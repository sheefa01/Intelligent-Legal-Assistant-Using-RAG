from rag.document_processor import (
    create_document,
    split_document
)

from rag.embeddings import get_embedding_model


PDF_PATH = "data/text/sample.pdf"


print("Loading document...")

document = create_document(PDF_PATH)

chunks = split_document(document)

print("Total chunks:", len(chunks))


print("\nLoading embedding model...")

embedding_model = get_embedding_model()

print("Embedding model loaded successfully!")


print("\nGenerating embedding for first chunk...")

vector = embedding_model.embed_query(
    chunks[0].page_content
)

print("Embedding generated!")

print("Vector dimensions:", len(vector))

print("\nFirst 10 values:")

print(vector[:10])