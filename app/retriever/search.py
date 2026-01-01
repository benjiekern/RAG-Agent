import math

from vectorize import build_index, embed_query

index = build_index()
embed = embed_query("this is a test query containing words about the berlin wall")
def search():
    dot_products = []
    for vector in index:
        row_total = 0
        for i, each in enumerate(vector[1]):
            row_total += each * embed[i]
        dot_products.append(row_total)
    a_magnitude = []

    for vector in index:
        row_total = 0
        for i, each in enumerate(vector[1]):
            row_total += each ** 2
        a_magnitude.append(math.sqrt(row_total))
    row_total = 0
    for each in embed:
        row_total += each ** 2
    b_magnitude = math.sqrt(row_total)

    results = []
    for i, each in enumerate(dot_products):
        if a_magnitude[i] == 0 or b_magnitude == 0:
            results.append((index[i][0], 0.0))
            continue
        results.append((index[i][0], each / (a_magnitude[i] * b_magnitude)))
    results.sort(key=lambda x: x[1], reverse=True)
    return results
search()