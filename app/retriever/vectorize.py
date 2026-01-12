from app.retriever.embeddings import chunk_text, load_texts, embed_documents
import math
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "docs"

def normalize(v):
    mag = math.sqrt(sum(x * x for x in v))
    return [x / mag for x in v] if mag != 0 else v

def build_index():
    texts = load_texts()
    chunks = chunk_text(texts)
    vectors = embed_documents(chunks)
    vectors = [normalize(v) for v in vectors]

    index = []
    for i, (doc, vec) in enumerate(zip(chunks, vectors), start=1):
        source = doc.metadata.get("source", "unknown")
        text = doc.page_content
        index.append((source, i, text, vec))

    return index