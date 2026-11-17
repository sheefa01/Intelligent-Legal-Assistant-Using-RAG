# ⚖️ AI Legal Research Assistant Using RAG

An **AI-powered Legal Research Assistant** that uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from legal documents and generate evidence-based answers using a locally running Large Language Model.

The system combines **document processing, semantic embeddings, FAISS vector search, and Ollama** to provide answers grounded in the uploaded legal documents rather than relying solely on the language model's pretrained knowledge.

---

## 🚀 Features

* 📄 Process legal PDF documents
* ✂️ Split documents into searchable text chunks
* 🧠 Generate semantic embeddings using Sentence Transformers
* 🔎 Retrieve relevant legal passages using FAISS
* 🤖 Generate answers using Ollama and Qwen2.5-Coder 3B
* 📚 Display source documents and page numbers
* 📊 Display similarity scores for retrieved chunks
* 🛡️ Evidence-based prompting to reduce hallucinations
* ❌ Return an insufficient-information response when relevant evidence cannot be found
* 🖥️ Interactive Streamlit web interface
* 🧪 Includes test scripts for major RAG components

---

## 🏗️ System Architecture

```text
                 ┌──────────────────────┐
                 │      Legal PDF       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Document Processing  │
                 │  Text Extraction     │
                 │  Chunking            │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Sentence Transformer│
                 │    Embeddings        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    FAISS Vector      │
                 │       Store          │
                 └──────────┬───────────┘
                            │
                  User Question
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Similarity Search  │
                 │      Retriever       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      Ollama          │
                 │ Qwen2.5-Coder 3B     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Evidence-Based       │
                 │ Legal Answer         │
                 └──────────────────────┘
```

---

## 🔄 RAG Workflow

### 1. Document Processing

Legal PDF documents are processed and their text is extracted.

The extracted text is divided into smaller chunks so that relevant portions can be efficiently retrieved during question answering.

### 2. Embedding Generation

Each document chunk is converted into a numerical vector using a **Sentence Transformer embedding model**.

These embeddings represent the semantic meaning of the text.

### 3. FAISS Vector Store

The generated embeddings are stored in a **FAISS vector index**.

FAISS performs similarity search to identify the document chunks most relevant to a user's question.

### 4. Retrieval

When a user asks a question:

```text
User Question
      ↓
Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Document Chunks
```

The system retrieves the most relevant chunks and filters them using a similarity-distance threshold.

### 5. Generation

The retrieved evidence is passed to **Qwen2.5-Coder 3B through Ollama**.

The prompt instructs the model to:

* Use only the retrieved evidence
* Avoid outside knowledge
* Avoid inventing facts
* Explain the evidence in its own words
* Indicate when sufficient information is unavailable

### 6. Source Display

The application displays:

* Document name
* Page number
* Similarity score
* Retrieved document content

This allows the user to verify the source of the generated answer.

---

## 🛠️ Technologies Used

| Technology                | Purpose                               |
| ------------------------- | ------------------------------------- |
| **Python**                | Core programming language             |
| **Streamlit**             | Web application interface             |
| **LangChain**             | Document and vector-store integration |
| **Sentence Transformers** | Semantic text embeddings              |
| **FAISS**                 | Vector similarity search              |
| **Ollama**                | Local LLM inference                   |
| **Qwen2.5-Coder 3B**      | Answer generation                     |
| **PyTorch**               | Machine learning framework            |
| **Requests**              | Communication with Ollama API         |
| **PDF Processing**        | Legal document text extraction        |

---

## 📁 Project Structure

```text
Intelligent-Legal-Assistant-Using-RAG/
│
├── app.py
│
├── rag/
│   ├── __init__.py
│   ├── document_processor.py
│   ├── embeddings.py
│   ├── generator.py
│   ├── retriever.py
│   └── vector_store.py
│
├── data/
│   └── text/
│       ├── indian_law.pdf
│       └── sample.pdf
│
├── requirements.txt
│
├── test_document_processor.py
├── test_embeddings.py
├── test_generator.py
├── test_metadata.py
├── test_prompt.py
├── test_retrieval.py
├── test_summary.py
└── test_vector_store.py
```

---

## 💻 Requirements

Before running the project, make sure you have:

* Python 3.11
* Ollama
* Qwen2.5-Coder 3B model
* Required Python packages from `requirements.txt`

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sheefa01/Intelligent-Legal-Assistant-Using-RAG.git
```

### 2. Navigate to the project

```bash
cd Intelligent-Legal-Assistant-Using-RAG
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Ollama Setup

Install and start Ollama on your system.

Then download the model:

```bash
ollama pull qwen2.5-coder:3b
```

Verify that the model is available:

```bash
ollama list
```

You should see:

```text
qwen2.5-coder:3b
```

Ollama runs locally and the application communicates with it through:

```text
http://localhost:11434
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## 🧪 Example Question

After starting the application, you can ask questions based on the available legal documents.

Example:

```text
Why was Section 497 challenged?
```

The system retrieves relevant passages from the legal document and generates an evidence-based answer.

The application also displays the supporting:

* Source document
* Page number
* Similarity score
* Retrieved evidence

---

## 🔍 Example RAG Result

```text
Question:
Why was Section 497 challenged?

Retrieved Documents:
Page 46
Page 10
Page 71
Page 53

Generated Answer:
Section 497 was challenged because it was argued to violate
fundamental rights under Articles 14, 15 and 21. The evidence
also discusses concerns regarding unequal treatment and the
subordination of women.
```

The exact generated response may vary depending on the retrieved context and model output.

---

## 🛡️ Hallucination Control

A major objective of the system is to keep generated answers grounded in retrieved evidence.

The generator prompt explicitly instructs the model to:

```text
Use ONLY the provided legal evidence.
Do NOT use outside knowledge.
Do NOT invent facts.
Do NOT make assumptions.
```

If the retrieved evidence does not contain sufficient information, the system can respond that sufficient information was not found in the provided legal documents.

---

## 📊 Why RAG?

A conventional LLM may answer a legal question using information from its pretrained knowledge, which can lead to outdated or unsupported responses.

This project uses **Retrieval-Augmented Generation**:

```text
Legal Documents
      ↓
Knowledge Retrieval
      ↓
Relevant Evidence
      ↓
LLM
      ↓
Grounded Answer
```

This allows the generated answer to be connected to the actual documents being searched.

---

## 🧪 Testing

The project contains separate test scripts for different components:

```text
test_document_processor.py
test_embeddings.py
test_generator.py
test_metadata.py
test_prompt.py
test_retrieval.py
test_summary.py
test_vector_store.py
```

These scripts can be executed individually using:

```bash
python test_generator.py
```

or:

```bash
python test_retrieval.py
```

---

## ⚠️ Limitations

* The current system depends on the quality of the provided legal documents.
* The quality of the generated answer depends on the retrieved context and the local language model.
* The current implementation is intended for **legal research assistance**, not as a replacement for professional legal advice.
* The current local model is a relatively small 3B parameter model and may produce less detailed responses than larger models.
* Internet access is not required for Ollama inference after the required model is downloaded.

---

## 🔮 Future Enhancements

Possible future improvements include:

* 📄 Support for multiple legal documents
* 🔎 Improved retrieval and reranking
* ⚖️ Legal-document validation
* 💬 Conversation history
* 🗂️ Document management
* 📌 Improved citation and evidence highlighting
* 🌐 Deployment to a cloud platform
* 🤖 Evaluation of multiple LLMs
* 📈 Retrieval and answer-quality evaluation
* 🎨 Improved Streamlit interface

---

## 🎯 Project Objective

The objective of this project is to build a practical **Retrieval-Augmented Generation system for legal research** that allows users to ask questions about legal documents and receive concise answers grounded in retrieved evidence, along with source and page information for verification.




