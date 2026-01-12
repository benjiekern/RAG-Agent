from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
from pathlib import Path

client = OpenAI()
DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "docs"

def load_texts():
    docs = []

    # Load .txt
    txt_loader = DirectoryLoader(
        str(DOCS_DIR),
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True,
        use_multithreading=True,
    )
    docs.extend(txt_loader.load())

    # Load .pdf
    pdf_loader = DirectoryLoader(
        str(DOCS_DIR),
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
        use_multithreading=True,
    )
    docs.extend(pdf_loader.load())

    return docs


def chunk_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)


_embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


def embed_documents(documents):
    texts = [doc.page_content for doc in documents]
    return _embeddings.embed_documents(texts)


def embed_text(text):
    return _embeddings.embed_query(text)