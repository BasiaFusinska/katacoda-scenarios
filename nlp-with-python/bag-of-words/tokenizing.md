Our goal is to build the vocabulary, so the first step is to get all the words from the corpus.

# Task: Get All the words from the corpus

Run the code to get the required imports:

```
from nltk import word_tokenize

words = []
```{{execute}}

Iterate through all the documents, use `word_tokenize` in every one of them and append tokens to `words`. Remember to bring the words to the lowercase value (use `lower()` function).

Once you have all the words use [FreqDist](http://www.nltk.org/api/nltk.html#nltk.probability.FreqDist) class to get the frequencies. We've written a function for you to get the top words from the vocabulary you will be building.

```
from nltk.probability import FreqDist

def get_vocabulary(words, top=500):
    word_counts = FreqDist(words)
    vocabulary = word_counts.most_common(top)
    return vocabulary

get_vocabulary(words)
```{{execute}}
