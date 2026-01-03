from openai import OpenAI

client = OpenAI()

def embed_texts(texts):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )

    return [item.embedding for item in response.data]