# RAG Agent — Private Document Question Answering System

## Overview
A Retrieval-Augmented Generation (RAG) system that answers questions over private document collections with grounded, cited responses.
Supports both .txt and PDF files and provides an end-to-end pipeline from document processing to answer generation.

## Notable Features:

- PDF & .txt document ingestion

- Recursive chunking with overlap

- OpenAI embeddings + vector similarity search

- Grounded answers with explicit citations

- Modular architecture (retriever, generator, pipeline)

- Optional LangSmith tracing for observability

## Setup

### Windows
Clone the repository
```
git clone https://github.com/benjiekern/RAG-Agent.git
cd RAG-Agent
```

Create virtual environment
```
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies
```
pip install -r requirements.txt
```

Create `.env` from the example and add your API keys:
```
copy .env.example .env
```

```
export LANGSMITH_TRACING=true
export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
export LANGSMITH_API_KEY=YOUR_KEY_GOES_HERE
export LANGSMITH_PROJECT=pr-nautical-dime-88
export OPENAI_API_KEY=YOUR_KEY_GOES_HERE
```

Add your documents

Place any .txt and/or .pdf files in:

data/docs/

Run the system

```
python -m app.main
```


### MacOS/Linux
Clone the repository
```
git clone https://github.com/benjiekern/RAG-Agent.git
cd RAG-Agent
```

Create virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies
```
pip3 install -r requirements.txt
```

Create `.env` from the example and add your API keys:
```
cp .env.example .env
```

```
export LANGSMITH_TRACING=true
export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
export LANGSMITH_API_KEY=YOUR_KEY_GOES_HERE
export LANGSMITH_PROJECT=pr-nautical-dime-88
export OPENAI_API_KEY=YOUR_KEY_GOES_HERE
```

## Post Setup
Add your documents

Place any .txt and/or .pdf files in:

data/docs/

Run the system

```
python3 -m app.main
```

Ask a question:

```
Ask questions about a private document collection and get grounded, cited answers.
> How long is the Berlin Wall?
```

Example output:

```
The Berlin Wall was more than 140 kilometres long
(Source: berlin-wall.txt, Chunk: 89)
```

# Tech Stack

Python 3.10+

LangChain

OpenAI API

Vector similarity search

LangSmith (optional observability)
