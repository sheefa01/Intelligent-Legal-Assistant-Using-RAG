import re

from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def clean_text(text):
    """
    Clean common PDF header, footer and extraction noise.
    """

    # Remove Indian Kanoon header
    text = re.sub(
        r"Joseph Shine vs Union Of India on 27 September, 2018",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Remove Indian Kanoon footer and page number
    text = re.sub(
        r"Indian Kanoon\s*-\s*\d+",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Remove standalone page numbers
    text = re.sub(
        r"(?m)^\s*\d+\s*$",
        "",
        text
    )

    # Normalize spaces
    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    # Normalize excessive blank lines
    text = re.sub(
        r"\n\s*\n+",
        "\n\n",
        text
    )

    # Remove common extracted special characters
    text = text.replace("‚", "'")
    text = text.replace("ƒ", "'")
    text = text.replace("€", "'")
    text = text.replace("‹", "'")
    text = text.replace("›", "'")

    return text.strip()


def create_document(pdf_path):

    reader = PdfReader(pdf_path)

    documents = []

    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        text = page.extract_text()

        if not text:
            continue

        text = clean_text(text)

        if not text:
            continue

        document = Document(
            page_content=text,
            metadata={
                "source": str(pdf_path),
                "page": page_number
            }
        )

        documents.append(document)

    return documents


def split_document(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(
        documents
    )

    return chunks