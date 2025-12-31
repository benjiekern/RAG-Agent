from chunking import chunk_text
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "docs"

def build_index():
    index = []
    for file in DOCS_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")
        for chunk in chunk_text(text):
            index.append((chunk, embed(chunk)))

    return index

def embed_query(query: str):
    return embed(query)

def embed(text):
    vector = [0] * 26
    for letter in text.lower():
        char = ord(letter)
        if 97 <= char <= 122:
            vector[char - 97] += 1

    return vector