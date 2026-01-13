from pathlib import Path

import asyncio
from app.rag import search
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

TRACING_ENABLED = (
    os.getenv("LANGSMITH_TRACING") == "true"
    or os.getenv("LANGCHAIN_TRACING_V2") == "true"
)

if TRACING_ENABLED:
    langsmith_key = os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY")
    if not langsmith_key:
        raise RuntimeError(
            "Tracing enabled but missing LangSmith key. "
            "Set LANGSMITH_API_KEY or LANGCHAIN_API_KEY, or disable tracing."
        )

    from agents import set_trace_processors
    from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor

    set_trace_processors([OpenAIAgentsTracingProcessor()])

async def main():
    question = input("Ask questions about a private document collection and get grounded, cited answers.\n")
    result = search(question)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())