import streamlit as st

from rag.retriever import retrieve_documents
from rag.generator import LegalGenerator


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Legal Research Assistant",
    page_icon="⚖️",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #AAAAAA;
        margin-bottom: 30px;
    }

    .answer-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #444444;
        background-color: #171922;
        font-size: 18px;
        line-height: 1.7;
    }

    .info-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #171922;
        border: 1px solid #333333;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# GENERATOR
# ============================================================

@st.cache_resource
def load_generator():

    return LegalGenerator()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ System")

    try:

        generator = load_generator()

        st.success("🟢 Ollama Connected")

    except Exception as e:

        st.error("🔴 Ollama Not Connected")

        st.stop()


    st.markdown("### LLM Model")

    st.info(
        "qwen2.5-coder:3b"
    )


    st.markdown("### Vector Store")

    st.info(
        "FAISS"
    )


    st.markdown("### Embedding")

    st.info(
        "Sentence Transformers"
    )


    st.markdown("### Architecture")

    st.write(
        """
        PDF
        ↓
        Text Extraction
        ↓
        Chunks
        ↓
        Embeddings
        ↓
        FAISS
        ↓
        Retriever
        ↓
        Ollama
        ↓
        Answer
        """
    )


    st.divider()

    st.warning(
        """
        ⚠️ Disclaimer

        This application is an AI-based legal
        research assistant.

        It provides information from the uploaded
        legal documents and should not be treated
        as professional legal advice.
        """
    )


# ============================================================
# MAIN TITLE
# ============================================================

st.markdown(
    '<div class="main-title">'
    '⚖️ AI Legal Research Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Upload a legal document and ask questions '
    'to retrieve evidence-based answers.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DOCUMENT UPLOAD
# ============================================================

st.header("📄 Legal Document")

uploaded_file = st.file_uploader(
    "Upload a legal PDF",
    type=["pdf"]
)


# ============================================================
# DOCUMENT PROCESSING
# ============================================================

if uploaded_file:

    st.success(
        f"Document selected: {uploaded_file.name}"
    )

    st.session_state["current_document"] = (
        uploaded_file.name
    )

    st.divider()

    # --------------------------------------------------------
    # DOCUMENT INFORMATION
    # --------------------------------------------------------

    st.header("📊 Document Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Document",
            uploaded_file.name
        )

    with col2:

        st.metric(
            "Top Results",
            "6"
        )

    with col3:

        st.metric(
            "Vector Store",
            "FAISS"
        )


# ============================================================
# QUESTION SECTION
# ============================================================

st.header("🔎 Ask a Legal Question")


question = st.text_area(
    "Enter your legal question:",
    placeholder=(
        "Example: Why was Section 497 challenged?"
    ),
    height=100
)


# ============================================================
# ASK QUESTION
# ============================================================

if st.button(
    "🔍 Ask Question",
    type="primary",
    use_container_width=False
):

    if not question.strip():

        st.warning(
            "Please enter a legal question."
        )

        st.stop()


    # ========================================================
    # RETRIEVAL
    # ========================================================

    with st.spinner(
        "🔎 Searching legal documents..."
    ):

        try:

            results = retrieve_documents(
                question,
                k=6,
                score_threshold=1.2
            )

        except Exception as e:

            st.error(
                f"Retrieval failed: {e}"
            )

            st.stop()


    # ========================================================
    # NO RESULTS
    # ========================================================

    if not results:

        st.warning(
            """
            I could not find sufficiently relevant
            information in the uploaded legal document.
            """
        )

        st.stop()


    # ========================================================
    # DOCUMENTS FOR LLM
    # ========================================================

    documents = [
        document
        for document, score in results
    ]


    # ========================================================
    # GENERATION
    # ========================================================

    with st.spinner(
        "🤖 Generating evidence-based answer..."
    ):

        try:

            answer = generator.generate(
                question,
                documents
            )

        except Exception as e:

            st.error(
                f"Generation failed: {e}"
            )

            st.stop()


    # ========================================================
    # ANSWER
    # ========================================================

    st.header("💡 Answer")

    st.markdown(
        f"""
        <div class="answer-box">

        {answer}

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # EVIDENCE
    # ========================================================

    st.header("📚 Evidence & Sources")


    for i, (document, score) in enumerate(
        results,
        start=1
    ):

        source = document.metadata.get(
            "source",
            "Unknown source"
        )

        page = document.metadata.get(
            "page",
            "Unknown page"
        )


        with st.expander(
            f"📄 Source {i} | Page {page}"
        ):

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Document:** `{source}`"
                )

            with col2:

                st.write(
                    f"**Similarity:** `{score:.4f}`"
                )


            st.divider()


            st.write(
                document.page_content
            )