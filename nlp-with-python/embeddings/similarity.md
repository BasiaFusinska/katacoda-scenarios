To have some play with the embeddings we need a function that would indicate how similar two words (and consequently two embeddings vectors) are. For word embedding this measure of similarity is [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity).

<img src="/basiafusinska/courses/nlp-with-python/embeddings/assets/cosine.png" alt="Cosine similarity">

Run the following code to define a function making proper calculations:

```
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (len(v1) * len(v2))
```{{execute}}

Once the function is defined calculate some similarities:

```
import numpy as np

idx1 = 25
idx2 = 134

v1 = embeddings[words[idx1]]
v2 = embeddings[words[idx2]]

cosine_similarity(v1, v2)
```{{execute}}

Feel free to change indexes and experiment.
