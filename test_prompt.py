from rag.retriever import retrieve_documents
from rag.generator import build_rag_prompt


question = input(
    "\nEnter your legal question: "
)

print("\nRetrieving relevant documents...\n")

documents = retrieve_documents(
    question,
    k=4
)

print(
    f"Retrieved {len(documents)} relevant chunks."
)

print("\nBuilding RAG prompt...\n")

prompt = build_rag_prompt(
    question,
    documents
)

print("=" * 80)
print("GENERATED RAG PROMPT")
print("=" * 80)

print(prompt)