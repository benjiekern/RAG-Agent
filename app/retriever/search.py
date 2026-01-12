from app.retriever.embeddings import embed_text
from app.retriever.vectorize import build_index, normalize

def search_chunks(query):
    index = build_index()
    query_embedding = embed_text(query)
    query_embedding = normalize(query_embedding)
    results = []

    for source, chunk_id, chunk_text, vec in index:
        score = 0.0
        for i, value in enumerate(vec):
            score += value * query_embedding[i]

        results.append((source, chunk_id, chunk_text, score))

    results.sort(key=lambda x: x[3], reverse=True)
    return results[:3]