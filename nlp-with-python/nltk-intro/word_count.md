Word frequency couldn't be any easier in the NLTK world. All you need to do is to use `FreqDist` class.

```
from nltk.probability import FreqDist
words_counts = FreqDist(words)

words_counts.items()
```{{execute}}

It doesn't look sorted, but there is a simple way to get the most common words:

`words_counts.most_common(20)`{{execute}}
