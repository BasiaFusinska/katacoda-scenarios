To start working with Python use the following command:

`python`{{execute}}

In this scenario we will be building [Bag of Words](https://en.wikipedia.org/wiki/Bag-of-words_model) model based on the [Reuters dataset](http://www.daviddlewis.com/resources/testcollections/reuters21578/) that is fortunately already imported and processed in the Python [nltk](https://www.nltk.org/) library. We won't use the model further as there are libraries that provide better support. You will have the chance to work with them in the next scenario.

To read the corpus simply use the *read_documents* function from the *data_reader* module.

`import data_reader
documents = data_reader.read_documents()`{{execute}}

You can have a look at the data and see the number of documents.

`len(documents)`{{execute}}

It's good to have a look at some examples. Feel free to change the index and do your own exploration.

```
example_idx = 1024
document = documents[example_idx]
document
```{{execute}}

As you can see the documents has some raw leftovers.
