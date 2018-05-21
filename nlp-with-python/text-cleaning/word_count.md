For many text tasks counting the occurrences of words is very useful. To do this we will build the dictionary that will count words in the document.

```
from collections import defaultdict
word_counts = defaultdict(int)

for word in document.split():
   word_counts[word] += 1

word_counts
```{{execute}}

To find out the most common words let us use [Counter](https://docs.python.org/2/library/collections.html#collections.Counter).

```
from collections import Counter

words_counter = Counter(word_counts)
words_counter.most_common(50)
```{{execute}}

Punctuation characters are very common, right?
