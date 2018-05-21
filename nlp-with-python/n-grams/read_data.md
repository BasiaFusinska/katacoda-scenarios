To use n-grams in the sentiment analysis task we need to read the documents with the corresponding labels.

`import data_reader
documents, labels = data_reader.read_reviews()`{{execute}}

You can look at the sentiment distribution.

```
set(labels)
len(documents)
positive = [documents[i] for i in range(0, len(documents)) if labels[i] == 'pos']
len(positive)
negative = [documents[i] for i in range(0, len(documents)) if labels[i] == 'neg']
len(negative)
```{{execute}}
