from rag.retriever import retrieve_documents
from rag.generator import LegalGenerator


question = input(
    "\nEnter your legal question: "
)


print("\nRetrieving relevant documents...\n")

results = retrieve_documents(
    question,
    k=4,
    score_threshold=1.0
)


if not results:

    print("\nNo sufficiently relevant information "
          "was found in the legal documents.")

    exit()


documents = [
    document
    for document, score in results
]

print(
    f"Retrieved {len(documents)} documents."
)


print("\nLoading generator...\n")

generator = LegalGenerator()


print("\nGenerating answer...\n")

answer = generator.generate(
    question,
    documents
)


print("=" * 80)
print("FINAL ANSWER")
print("=" * 80)

print(answer)
print("\n" + "=" * 80)
print("SOURCES")
print("=" * 80)

seen_sources = set()

for document, score in results:

    source = document.metadata.get(
        "source",
        "Unknown source"
    )

    page = document.metadata.get(
        "page",
        "Unknown page"
    )

    source_key = (source, page)

    if source_key not in seen_sources:

        print(
            f"📄 {source} — Page {page}"
        )

        seen_sources.add(source_key)
