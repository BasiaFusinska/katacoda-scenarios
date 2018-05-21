NLTK provides function for text tokenizing. With sentences it's `sent_tokenize`:

```
from nltk import sent_tokenize

document
sentences = sent_tokenize(document)
sentences
```{{execute}}

And for words it's `word_tokenize`:

```
from nltk import word_tokenize

words = word_tokenize(document)
words
```{{execute}}
