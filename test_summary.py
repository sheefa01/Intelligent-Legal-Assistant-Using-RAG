from rag.retriever import retrieve_documents
from rag.generator import LegalGenerator


question = "Why was Section 497 challenged?"


print("Retrieving relevant documents...")

results = retrieve_documents(
    question,
    k=4,
    score_threshold=1.0
)

documents = [document for document, score in results]

print(f"Retrieved {len(documents)} documents.")


generator = LegalGenerator()


context = ""

for i, document in enumerate(documents, start=1):

    page = document.metadata.get(
        "page",
        "Unknown"
    )

    context += f"""
Evidence {i} (Page {page}):

{document.page_content[:700]}

"""


prompt = f"""
Summarize the following legal evidence
to answer the question.

Question:
{question}

Evidence:
{context}

Write 3 to 5 sentences explaining
the main reasons for the challenge.

Do not copy the evidence word-for-word.

Answer:
"""


inputs = generator.tokenizer(
    prompt,
    return_tensors="pt",
    truncation=True,
    max_length=512
)

inputs = {
    key: value.to(generator.device)
    for key, value in inputs.items()
}


outputs = generator.model.generate(
    **inputs,
    max_new_tokens=150,
    do_sample=False
)


answer = generator.tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)


print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(answer)