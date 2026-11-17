from rag.vector_store import load_vector_store


def retrieve_documents(
    query: str,
    k: int = 6,
    score_threshold: float = 1.0
):
    """
    Retrieve relevant documents from FAISS.

    FAISS distance:
    Lower score = more similar.

    Process:
    1. Retrieve top-k candidate chunks.
    2. Filter chunks using similarity distance.
    3. Return documents with their scores.
    """

    vector_store = load_vector_store()

    # Retrieve top-k candidates
    results = vector_store.similarity_search_with_score(
        query,
        k=k
    )

    # Filter weak results
    filtered_results = []

    for document, score in results:

        score = float(score)

        if score <= score_threshold:

            filtered_results.append(
                (document, score)
            )

    # Keep best matches first
    filtered_results.sort(
        key=lambda x: x[1]
    )

    return filtered_results