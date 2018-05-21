To start working with Python use the following command:

`python`{{execute}}

In this scenario we will be working with the [NLTK](https://www.nltk.org/) library. In some way we will repeat some work from the previous scenario using the library instead of vanilla Python.

Let's read movie reviews again.

`import data_reader
documents = data_reader.read_reviews()`{{execute}}

Then we can look as an example document (feel free to change the index and load different document).

`example_idx = 123
document = documents[example_idx]
document`{{execute}}
