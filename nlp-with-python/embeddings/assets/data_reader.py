import numpy as np

def load_embeddings(file="vectors.vec"):
    embeddings = {}
    words = []
    with open(file) as f:
        for line in f:
            tokens = line.split()
            word = tokens[0].lower()
            if not word in embeddings.keys():
                words.append(word)
                embedding = np.array([float(token) for token in tokens[1:]])
                embeddings[word] = embedding
    return embeddings, words
