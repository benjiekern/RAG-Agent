def build_prompt(query, results):
    context_blocks = []
    for source, chunk_id, chunk, score in results:
        context_blocks.append(
            f"[Source: {source} | Chunk: {chunk_id} | Score: {score:.3f}]\n{chunk}"
        )

    context = "\n".join(context_blocks)

    return f"""You are a grounded assistant.

Rules:
- Use ONLY the CONTEXT below to answer.
- If the answer is not in the context, say: "I don't have enough information in the provided documents."
- Do NOT use outside knowledge.
- It is vital that every claim includes a citation like (Source: <file>, Chunk: <id>). Make sure that every bullet point/claim has a source attached.
- DO NOT add all the sources at the end, THEY MUST BE ATTACHED TO EACH CLAIM INLINE.

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""