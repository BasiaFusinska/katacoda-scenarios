Word frequency couldn't be any easier in the NLTK world.

```
from nltk.probability import FreqDist
words_counts = FreqDist(words)

words_counts.items()
words_counts.most_common(20)
```{{execute}}

All you need to do is to use `FreqDist` class.
