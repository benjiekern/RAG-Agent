from openai import OpenAI
from app.prompts import build_prompt
from app.retriever.search import search_chunks

def get_client():
    return OpenAI()


def call_llm(prompt: str) -> str:
    client = get_client()
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a careful, grounded assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )

    return response.choices[0].message.content


def search(query):
    results = search_chunks(query)
    prompt = build_prompt(query, results)
    answer = call_llm(prompt)
    return answer