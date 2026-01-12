from pathlib import Path

from agents import set_trace_processors
import asyncio
from app.rag import search
from langsmith.wrappers import OpenAIAgentsTracingProcessor
from dotenv import load_dotenv
import os

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "Missing OPENAI_API_KEY. Copy .env.example to .env and set your key, "
        "or set it as an environment variable."
    )
elif not os.getenv("LANGSMITH_API_KEY"):
    raise RuntimeError(
        "Missing LANGSMITH_API_KEY. Copy .env.example to .env and set your key, "
        "or set it as an environment variable."
    )

async def main():
    question = input("Ask questions about a private document collection and get grounded, cited answers.\n")
    result = search(question)
    print(result)

if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())