Now it's time to start feature generation for the read documents. First we will use simple [Bag of Words](https://en.wikipedia.org/wiki/Bag-of-words_model) model, then moving to [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

**Bag of Words** is a model that requires building the vocabulary and the assigning a number of occurences for every word in the document to the proper index. For example if the vocabulary is:

[ also, and, both, football, games, john, like, likes, mary, movie, movies, titanic, to, too, watch ]

the sentence:

*"John likes to watch movies. Mary likes to watch movies too."*

will become the following vector:

*[ 0, 0, 0, 0, 0, 1, 0, 2, 1, 0, 1, 0, 2, 1, 2 ]*

Python [sklearn](http://scikit-learn.org) library offers [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer) class to do this task for you. It takes collection of texts, builds the vocabulary based on words that appear in it and transforms it to the count vectors. It makes the preprocessing easier as you don't have to split the text, count occurences and build your vocabulary. It also uses efficient data structures to represent the vectors as they will be sparsed.

The following function is a helper that takes the vectorizer object, fits to the provided collection and transforms it according to the built model. Additionally it prints the vocabulary (feature names). As a default it will extract every word defined as the alphanumeric one with the length of at least 2.

```
from sklearn.feature_extraction.text import CountVectorizer

def fit_transform_vectorizer(vectorizer, print_features=True):
    one_hot = vectorizer.fit_transform(train_documents)
    if print_features:
        print(vectorizer.get_feature_names())
    return one_hot

```{{execute}}

All we have to do now is to use the function and pass a vanilla CountVectorizer. Let's see what happens.

`vectorizer = CountVectorizer()
one_hot = fit_transform_vectorizer(vectorizer)`{{execute}}
