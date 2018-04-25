To start working with Python use the following command:

`python`{{execute}}

The first step in every text processing task is to read in the data. We'll be working with the [Reuters dataset](http://www.daviddlewis.com/resources/testcollections/reuters21578/) that is fortunately already imported and processed in the Python [nltk](https://www.nltk.org/) library.

We've written the *read_train_test* function in the *data_reader* module to help you get started and focus on language processing rather than on specifics of the dataset and data reading techniques. As we will be dealing with the classification task, the result of the function is returning train and test datasets and corresponding labels. At the moment you will use documents, transforming them to the form that can be used to be fed into the machine learning algorithm. At the end you will also use labels.

`import data_reader
train_documents, train_labels, test_documents, test_labels = data_reader.read_train_test()`{{execute}}

Once the documents and labels are read you can have a look at the data. The code here is displaying the number of examples in both training and test datasets. Then we use *set* to get unique values from labels, which will constitute to the available categories.

```
print("Number of documents in the training set: ", len(train_documents))
print("Number of documents in the test set: ", len(test_documents))

categories = set(train_labels)
print("Categories (", len(categories), "): ", categories)
```{{execute}}

In the next command you can have a look at the content of the documents. Change the index by replacing the *example_idx* value and print the document and corresponding category.

You may see that documents still require some formatting, or that they have html elements till in their content.

`example_idx = 75
print("Example document (category: ", train_labels[example_idx], "):")
print(train_documents[example_idx])`{{execute}}
