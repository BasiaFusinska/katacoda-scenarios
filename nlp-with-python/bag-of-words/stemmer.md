In some situations it's good to use [stemming](https://en.wikipedia.org/wiki/Stemming) with the vocabulary. In a nutshell it is bringing the word to it's root value. You may have notices that we have for example sets like: *acquire - acquired, firm - firms* or *product - production* being set as separate features. We may want to merge to the base values.

There are several stemmers out there so you don't have to write your own (it's actually quite a complex although interesting task). We will use *PorterStemmer* imported from *nltk* library. This time our vectorizer construction has to change a little bit. We will first build the analyzer and then use it to initialize the final one.


```
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
```{{execute}}

# Task

Replace every word with the stemmed value (using `stem` function on the stemmer).

Once done this line should return the vocabulary of stems.

`get_vocabulary(words)`{{execute}}
