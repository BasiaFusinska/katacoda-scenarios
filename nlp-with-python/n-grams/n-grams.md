The general function using `zip` would look like the following and use `n` as an argument.

```
def ngrams(tokens, n):
    return zip(*[tokens[i:] for i in range(n)])
```{{execute}}

Then different n-grams can be retrieved as follows:

```
list(ngrams(sentence_tokens, 2))
list(ngrams(sentence_tokens, 3))
list(ngrams(sentence_tokens, 4))
```{{execute}}

NLTK offers few functions out of the box:

```
import nltk
list(nltk.bigrams(sentence_tokens))
list(nltk.trigrams(sentence_tokens))
```{{execute}}

The next step would be to build vectors based on ngrams.
