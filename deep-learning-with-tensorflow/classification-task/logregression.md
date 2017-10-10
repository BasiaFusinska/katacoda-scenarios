We can use several algorithms can in the binary classification task. Most popular are [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier), [Decision Trees](https://en.wikipedia.org/wiki/Decision_tree_learning), [Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression), [k-Nearest Neighbours](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm), but the list is in no way exhausted. We will apply Logistic Regression in this scenario.

You can go into the details for this particular method, but the basic idea is based on the fact that our data are _linearly separable_ regarding labels. This means that you can draw the line between the dots of the different colours.

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/classification-task/assets/logistic_regression.png" alt="Logistic regression">

We're in the lucky position that this line can be drawn in many ways, and still be separating the dots. The algorithm adjusts the coefficients during the training phase so that the distances from the dots to the line are minimised.

The data is stored in the classification_data.csv file. The first thing we're going to do is to read and visualise the data. Some helper functions have already been written for you. They can be found in the helpers.py file.

You're going to write the code in the `classification.py`{{open}} file. It already contains needed packages imports. All you need to do is to use the helper `read_data` function to load the data from the file.

<pre class="file" data-filename="classification.py" data-target="append">
# Read the data
data = h.read_data()
print data
</pre>

You can always run the code written so far using the following command:
`python classification.py`{{execute}}
