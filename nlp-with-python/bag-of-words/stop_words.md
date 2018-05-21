The vocabulary looks better now, but there are still some issues. Here we will deal with [stop words](https://en.wikipedia.org/wiki/Stop_words) which are commonly appearing words that don't bring much meaning of context. These are words like:

*a, an, and, both, do, have, how, is, it, I, more, much, my, on, one, so, the, this, to, too, very, what, who, where, you*

... and many more. Every language have their on list and different algorithms and teams use slightly changed lists. Sometimes you may need to decide the list of your stop words. We will use `nltk.corpus.stopwords` for english language.

```
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
```{{execute}}

# Task

Filter stop words from the `words` variable.

Once done this line should return the vocabulary without stop words.

`get_vocabulary(words)`{{execute}}
