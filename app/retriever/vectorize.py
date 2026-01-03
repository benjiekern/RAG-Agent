import math

from chunking import chunk_text
from pathlib import Path
from embeddings import embed_texts

DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "docs"

def normalize(v):
    mag = math.sqrt(sum(x * x for x in v))
    return [x / mag for x in v] if mag != 0 else v

def build_index():
    raw_chunks = []
    sources = []

    for file in DOCS_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")
        for chunk in chunk_text(text):
            raw_chunks.append(chunk)
            sources.append(file.name)

    vectors = embed_texts(raw_chunks)
    vectors = [normalize(v) for v in vectors]

    index = [
        (sources[i], i+1, raw_chunks[i], vectors[i])
        for i in range(len(raw_chunks))
    ]

    return index