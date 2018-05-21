To start working with Python use the following command:

`python`{{execute}}

The first step in every text processing task is to read in the data. We'll be working with the Movie Reviews Corpus provided by the Python [nltk](https://www.nltk.org/) library. You don't have to worry about this now as we've prepared the code to read the data for you.

We've written the *read_reviews* function in the *data_reader* module to help you get started and focus on language processing rather than on specifics of the dataset and data reading techniques. The data will be read into *documents* variable.

`import data_reader
documents = data_reader.read_reviews()`{{execute}}

Once the documents and labels are read you can have a look at the data.
You can check the number of examples.

`len(documents)`{{execute}}

As you can see we have 2000 reviews in the dataset. Pick and index number and see what some of then are doing.

`example_idx = 75
document = documents[example_idx]
document`{{execute}}
