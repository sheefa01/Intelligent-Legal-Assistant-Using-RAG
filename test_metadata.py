from rag.document_processor import (
    create_document,
    split_document
)


PDF_PATH = "data/text/sample.pdf"

documents = create_document(PDF_PATH)

chunks = split_document(documents)

print("Total chunks:", len(chunks))


for index in [0, 1, 50]:

    if index < len(chunks):

        print("\n" + "=" * 80)
        print(f"CHUNK {index}")
        print("=" * 80)

        print("\nMetadata:")
        print(chunks[index].metadata)

        print("\nContent:")
        print(chunks[index].page_content[:700])