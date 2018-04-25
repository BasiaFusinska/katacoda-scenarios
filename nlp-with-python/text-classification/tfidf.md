Another way to get the feature vector is to use *tf-idf* model. It is based on calculating the frequency of words based on both appearing in the sentence and in the whole dataset. The method of calculation can represented as follows:

<img src="/basiafusinska/courses/nlp-with-python/text-classification/assets/tf-idf.png" alt="tf-idf equations">


*sklearn* again offering a class (*TfidfVectorizer*) to do the calculations for us. As we've learned from the previous experience we'll use the other techniques and just change the type of vectorizer assigning the transformation to the separate value.

```
from sklearn.feature_extraction.text import TfidfVectorizer

analyzer = TfidfVectorizer(stop_words='english', token_pattern='[a-zA-Z]{2,}').build_analyzer()

vectorizer_tfidf = TfidfVectorizer(max_features=500, analyzer=(lambda text: (stemmer.stem(word) for word in analyzer(text))))
tfidf = fit_transform_vectorizer(vectorizer_tfidf)
```{{execute}}

The vocabulary looks exactly the same but the representation differ. Instead of counts it should now contain real values representing tf-idf index. Let's have a look at the result of transformation.

`print(tfidf.toarray())
example_idx = 73 
print(tfidf.toarray()[example_idx])`{{execute}}
