Wow, this is a lot of words. Do you think all of them are needed for our model? Probably not. How about we limit them to the 500 most common ones?

Fortunately we don't have to do it by hand as *CountVectorizer* has *max_features* parameter in the constructor. We'll limit the vocabulary to 500. Feel free to change this.

`vectorizer = CountVectorizer(max_features=500)
one_hot = fit_transform_vectorizer(vectorizer)`{{execute}}

This is a clearer list, isn't it? But what strikes me immediately is all the numbers appearing at the beginning of the list. I would like to get rid of them as I don't think their values would bring anything to the classification task. Actually I would like to match the words to be only letters and having at least 2 letters.

This can be achieved by using regular expressions and again *CountVectorizer* has the parameter (*token_pattern*) that can handle it.

`vectorizer = CountVectorizer(max_features=500, token_pattern='[a-zA-Z]{2,}')
one_hot = fit_transform_vectorizer(vectorizer)`{{execute}}

Much tidier now, but there are still some problems I can see. One is that vocabulary uses a lot of [stop words](https://en.wikipedia.org/wiki/Stop_words) which are commonly appearing words that don't bring much meaning of context. These are words like:

*a, an, and, both, do, have, how, is, it, I, more, much, my, on, one, so, the, this, to, too, very, what, who, where, you*

... and many more. Every language have their on list and different algorithms and teams use slightly changed lists. Sometimes you may need to decide the list of your stop words.

*CountVectorizer* has a handler for english language. For other languages the parameter *stop_words* has to be set to be a list.

`vectorizer = CountVectorizer(max_features=500, token_pattern='[a-zA-Z]{2,}', stop_words='english')
one_hot = fit_transform_vectorizer(vectorizer)`{{execute}}

Now the words seem to bring more meaning. The last issue is [stemming](https://en.wikipedia.org/wiki/Stemming). In a nutshell it is bringing the word to it's root value. You may have notices that we have for example sets like: *acquire - acquired, firm - firms* or *product - production* being set as separate features. We may want to merge to the base values.

There are several stemmers out there so you don't have to write your own (it's actually quite a complex although interesting task). We will use *PorterStemmer* imported from *nltk* library. This time our vectorizer construction has to change a little bit. We will first build the analyzer and then use it to initialize the final one.

```
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
analyzer = CountVectorizer(stop_words='english', token_pattern='[a-zA-Z]{2,}').build_analyzer()

vectorizer = CountVectorizer(max_features=500, analyzer=(lambda text: (stemmer.stem(word) for word in analyzer(text))))
one_hot = fit_transform_vectorizer(vectorizer)
```{{execute}}

Now we can see how this representation looks like and then how well it can be used to predict the category of text. First let's have a peek on the result of transformation and display one example. Feel free to change the index and check others.

`print(one_hot.toarray())
example_idx = 73 # Feel free to change the index
print(one_hot.toarray()[example_idx])`{{execute}}

Do you see now what I meant about sparcity? Most of the words don't appear in the sentence and we also limite3d our vocabulary so rare and stop words won't be represented as features.
