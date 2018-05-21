import numpy as np

def load_embeddings(file="vectors.vec"):
    embeddings = {}
    words = []
    with open(file) as f:
        for line in f:
            tokens = line.split()
            word = tokens[0].lower()
            words.append(word)
            embedding = np.array([float(token) for token in tokens[1:]])
    return embeddings, words
