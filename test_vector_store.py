from rag.document_processor import (
    create_document,
    split_document
)

from rag.vector_store import create_vector_store


PDF_PATH = "data/text/sample.pdf"


print("========== STEP 1: LOAD PDF ==========")

documents = create_document(PDF_PATH)

print("Document loaded.")
print("Pages loaded:", len(documents))


print("\n========== STEP 2: CREATE CHUNKS ==========")

chunks = split_document(documents)

print("Total chunks:", len(chunks))


print("\n========== SAMPLE CHUNK ==========")

print("Metadata:")
print(chunks[0].metadata)

print("\nContent:")
print(chunks[0].page_content[:500])


print("\n========== STEP 3: CREATE FAISS VECTOR STORE ==========")
from rag.document_processor import (
    create_document,
    split_document
)

from rag.vector_store import (
    create_vector_store,
    save_vector_store
)


PDF_PATH = "data/text/sample.pdf"


print("========== STEP 1: LOAD PDF ==========")

documents = create_document(PDF_PATH)

print("Document loaded.")
print("Pages loaded:", len(documents))


print("\n========== STEP 2: CREATE CHUNKS ==========")

chunks = split_document(documents)

print("Total chunks:", len(chunks))


print("\n========== SAMPLE CHUNK ==========")

print("Metadata:")
print(chunks[0].metadata)

print("\nContent:")
print(chunks[0].page_content[:500])


print("\n========== STEP 3: CREATE FAISS VECTOR STORE ==========")

vector_store = create_vector_store(chunks)

print("\nVector store created successfully!")


print("\n========== STEP 4: SAVE FAISS VECTOR STORE ==========")

save_vector_store(vector_store)

print("\nFAISS vector store saved successfully!")
vector_store = create_vector_store(chunks)

print("\nVector store created successfully!")


print("\n========== STEP 4: SAVE FAISS VECTOR STORE ==========")

from rag.vector_store import save_vector_store

save_vector_store(vector_store)

print("\nFAISS vector store saved successfully!")