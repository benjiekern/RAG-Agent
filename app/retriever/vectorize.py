from chunking import chunk_text
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "docs"

def build_index():
    chunks = []
    vectors = []
    for file in DOCS_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")
        for each in chunk_text(text):
            chunks.append(each)

    for chunk in chunks:
        vector = [0] * 26
        for letter in chunk:
            char = ord(letter.lower())
            if 97 <= char <= 122:
                vector[char - 97] += 1

        vectors.append(vector)

    index = list(zip(chunks, vectors))
    return index

def embed_query(query: str):
    vector = [0] * 26
    for letter in query:
        char = ord(letter.lower())
        if 97 <= char <= 122:
            vector[char - 97] += 1

    return vector