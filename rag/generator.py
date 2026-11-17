import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5-coder:3b"


class LegalGenerator:

    def __init__(self):

        print("Connecting to Ollama...")

        try:
            response = requests.get(
                "http://localhost:11434/api/tags",
                timeout=5
            )

            response.raise_for_status()

        except requests.RequestException as e:

            raise RuntimeError(
                "Ollama is not running. "
                "Start Ollama and try again."
            ) from e

        print(
            f"Ollama connected. Model: {MODEL_NAME}"
        )


    def build_prompt(self, question, documents):

        context_parts = []

        for i, document in enumerate(
            documents,
            start=1
        ):

            page = document.metadata.get(
                "page",
                "Unknown page"
            )

            content = document.page_content.strip()

            context_parts.append(
                f"""
--- EVIDENCE {i} ---
PAGE: {page}

{content}
--- END EVIDENCE {i} ---
"""
            )

        context = "\n".join(context_parts)

        prompt = f"""
You are an AI legal research assistant.

Your task is to answer the user's question based ONLY
on the legal evidence provided below.

IMPORTANT RULES:

1. Read all the evidence carefully.
2. Find information that directly relates to the question.
3. If the evidence contains relevant information, USE IT
   to answer the question.
4. Summarize the relevant evidence in your own words.
5. You may combine information from multiple evidence sections.
6. Do not use information that is not present in the evidence.
7. Do not rely on your general or pretrained legal knowledge.
8. Do not invent facts, cases, Articles, Sections, or punishments.
9. Only say that information is insufficient when the evidence
   genuinely does not contain an answer.
10. Keep the answer concise and clear.

IMPORTANT EXAMPLE:

If the evidence says that Section 497 was criticized because
it affected fundamental rights under Articles 14, 15 and 21,
and the user asks:

"Why was Section 497 challenged?"

then explain that the challenge was based on those constitutional
rights.

Do NOT say that the information is insufficient if the evidence
contains the answer.

LEGAL EVIDENCE:

{context}

USER QUESTION:

{question}

ANSWER:
"""

        return prompt


    def generate(self, question, documents):

        prompt = self.build_prompt(
            question,
            documents
        )

        print("\n========== PROMPT ==========\n")
        print(prompt)
        print("\n============================\n")

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.0,
                "num_predict": 250
            }
        }

        print("Generating answer with Ollama...")

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=180
        )

        response.raise_for_status()

        result = response.json()

        answer = result.get(
            "response",
            ""
        ).strip()

        if not answer:

            return (
                "I could not generate an answer from "
                "the provided legal documents."
            )

        return answer