If you agree on the vocabulary to be ready, the last step is to use it to build a vector of features for the documents in the corpus. This would mean going through every document and comparing the words with the vocabulary while getting the words frequencies for specific document.

We've built a function for you to do it for specific document.

```
import numpy as np

def vectorize_doc(document, vocabulary):
    doc_words = word_tokenize(document.lower())
    doc_words = [stemmer.stem(word) for word in doc_words]
    doc_frequencies = FreqDist(doc_words)
    voc_size = len(vocabulary)
    doc_vector = np.zeros(voc_size)
    for idx in range(0, voc_size):
        token = vocabulary[idx]
        if token in doc_frequencies.keys():
            doc_vector[idx] = doc_frequencies[token]
    return doc_vector
```{{execute}}

Once you have this function see how the vector looks like for different documents.

```
vocabulary = [w for w, _ in get_vocabulary(words)]

idx = 1467
vectorize_doc(documents[idx], vocabulary)
```{{execute}}

Change the index and see other documents.
