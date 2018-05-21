Most of the work when working with the text require some tokenization. You can use Python function `split()` to get words from the document.

`words = document.split()`{{execute}}

Notice that this method is not perfect. It just use space to figure out the words. If the punctuation happens to be attached to the word it will stay there.

Try to use *split* to get the sentences from the document. (Hint: Try simple solution where sentences are separated by the ".").

## Task

Get the series of data for the word counts in all the documents. Get the basic statistics and find out about the distribution.

You should get the visualization like this:

<img src="/basiafusinska/courses/nlp-with-python/text-cleaning/assets/doc_words.png" alt="Document words counts distribution">
