What about the lengths of the documents? You can check how they differ by first creating the new list storing the lengths.

`doc_lengths = [len(document) for document in documents]`{{execute}}

Once you have the lengths you can look at some statistics (like the minimum, maximum or average value). [Series](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html) of [Pandas](https://pandas.pydata.org/) package offer a *describe* function that can give you summary information. The following code will use it to print first few lengths and retwrieve statistics.

```
import pandas as pd

doc_lengths = pd.Series(doc_lengths)
doc_lengths[:10]
doc_lengths.describe()
```{{execute}}

You can see the statistics now. The histogram would look like this:

<img src="/basiafusinska/courses/nlp-with-python/text-cleaning/assets/doc_lengths.png" alt="Document lengths distribution">

As you can see the dataset is a little skewed.
