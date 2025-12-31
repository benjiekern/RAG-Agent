import tiktoken

def chunk_text(text, max_tokens=300, overlap=60, model='gpt-4o-mini'):
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)

    chunks = []
    start = 0

    while start < len(tokens):
        end = start + max_tokens
        chunk_tokens = tokens[start:end]
        c_text = encoding.decode(chunk_tokens)

        chunks.append(c_text)

        start = end - overlap  # overlap for context
        if start < 0:
            start = 0

    return chunks