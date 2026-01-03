import math

from embeddings import embed_texts
from vectorize import build_index, normalize

index = build_index()
query_embedding = embed_texts(["this is a test query containing words about the berlin wall"])[0]
vectors_list = [row[3] for row in index]
query_embedding = normalize(query_embedding)

def search():
    results = []

    for source, chunk_id, chunk_text, vec in index:
        score = 0.0
        for i, value in enumerate(vec):
            score += value * query_embedding[i]

        results.append((source, chunk_id, chunk_text, score))

    results.sort(key=lambda x: x[3], reverse=True)
    return results[:3]

print(search())