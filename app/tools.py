from agents import function_tool
from dotenv import load_dotenv, find_dotenv
import os
from pathlib import Path
from app.retriever.chunking import chunk_text

load_dotenv(find_dotenv())
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

DOCS_DIR = Path(__file__).resolve().parent.parent / "data" / "docs"
os.environ["USER_AGENT"] = "MyRAGApp/1.0 (+https://mywebsite.com)"

@function_tool
def search_documents(query: str) -> str:
    results = []
    query_words = query.lower().split()

    for file in DOCS_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")
        chunks = chunk_text(text)

        for chunk in chunks:
            if any(word in chunk.lower() for word in query_words):
                results.append(f"Source: {file.name}\n{chunk}")

    return "\n\n".join(results[:3])