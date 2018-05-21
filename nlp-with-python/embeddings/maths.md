Embeddings allow us to do interesting calculations. By vector representation we can find relations between words.

<img src="/basiafusinska/courses/nlp-with-python/embeddings/assets/word2vec.png" alt="Word2vec">

The following function is using the one you've built in the last step to build a sentence addressing these relations. It will return a sentence that is missing in the sentence:

*X is to Y as Z is to ...*

```
def x_is_to_y_as_z_is_to(x, y, z, embeddings):
    vx = embeddings[x.lower()]
    vy = embeddings[y.lower()]
    vz = embeddings[z.lower()]
    vector = vy - vx + vz
    word, _ = get_nearest(vector, embeddings)[0]
    print(x, "is to", y, "as", z, "is to", word)
    return word
```{{execute}}

Try it out with different combinations:

```
x_is_to_y_as_z_is_to("britain", "british", "china", embeddings)
x_is_to_y_as_z_is_to("england", "london", "france", embeddings)
x_is_to_y_as_z_is_to("england", "london", "china", embeddings)
x_is_to_y_as_z_is_to("king", "man", "queen", embeddings)
```{{execute}}
