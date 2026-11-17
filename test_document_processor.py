from rag.document_processor import (
    create_document,
    split_document
)

PDF_PATH = "data/text/sample.pdf"

print("Loading PDF...")

document = create_document(PDF_PATH)

print("\n========== DOCUMENT ==========")

print("File:", document.metadata["file_name"])
print("Source:", document.metadata["source"])
print("Characters:", len(document.page_content))

print("\nFirst 1000 characters:")
print(document.page_content[:1000])

print("\n========== CHUNKING ==========")

chunks = split_document(document)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- Chunk {i + 1} ---")
    print("Characters:", len(chunk.page_content))
    print(chunk.page_content[:500])