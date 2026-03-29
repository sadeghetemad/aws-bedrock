import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("One of the vectors is zero, cannot compute cosine similarity.")

    return dot_product / (norm_a * norm_b)



