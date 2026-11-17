from rag.retriever import retrieve_documents


query = input("\nEnter your legal question: ")

print("\nSearching legal document...\n")

results = retrieve_documents(
    query,
    k=4
)

print(f"Retrieved {len(results)} chunks.\n")


for i, (document, score) in enumerate(results, start=1):

    print("=" * 70)
    print(f"RESULT {i}")
    print("=" * 70)

    print("\nSimilarity score:", score)

    print(
        "\nSource:",
        document.metadata.get("source")
    )
    print("Page:", document.metadata.get("page"))
    

    print("\nContent:")

    print(document.page_content[:1000])