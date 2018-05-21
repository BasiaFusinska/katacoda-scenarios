Fortunately, this time we don't have to do it by hand. As in the *Text Classification* scenario, we can use *CountVectorizer*. To take ngrams into account one need to fill in *ngram_range* parameter. For bigrams we need the following code:

```
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features=500, stop_words='english', token_pattern='[a-zA-Z]{2,}', ngram_range=(2, 2))
analyze = vectorizer.build_analyzer()
```{{execute}}

Let's have a look at the bigrams for one of the documents:

`idx = 73
document = documents[idx]
analyze(document)`{{execute}}

Now you can transform the `document` using the `vectorizer`:

`vectors = vectorizer.fit_transform(documents).toarray()
vectors[idx]`{{execute}}

And to see the bigrams for the corpus:

`vectorizer.get_feature_names()`{{execute}}

You can do the same using `TfidfVectorizer` too.
