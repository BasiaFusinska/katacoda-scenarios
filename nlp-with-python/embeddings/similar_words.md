The whole point of similarity measure is to use it to for instance find words similar to some vector.

The following code is returning nearest neighbors to the specified vector:

```
def get_nearest(vector, embeddings, top=10):
    distances = [(w, cosine_similarity(embeddings[w], vector)) for w in embeddings.keys()]
    distances = sorted(distances, key=lambda x: x[1], reverse=True)
    return distances[:top]
```{{execute}}

## Task: Get similar words

Build the function that will return k nearest words to the specified one. It should take word(string) and embeddings as parameters.

`def get_similar_words(word, embeddings, top = 10):`{{execute}}

Once defined you should be able to find the nearest neighbors:

```
get_similar_words("britain", embeddings)
get_similar_words("british", embeddings)
get_similar_words("china", embeddings)
get_similar_words("chinese", embeddings)
```{{execute}}

Feel free to check other words. Make sure they are in the vocabulary.
