We can use several algorithms can in the binary classification task. Most popular are [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier), [Decision Trees](https://en.wikipedia.org/wiki/Decision_tree_learning), [Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression), [k-Nearest Neighbours](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm), but the list is in no way exhausted. We will apply Logistic Regression in this scenario.

You can go into the details for this particular method, but the basic idea is based on the fact that our data are _linearly separable_ regarding labels. This means that you can draw the line between the dots of the different colours.

We're in the lucky position that this line can be drawn in many ways, and still be separating the dots. The algorithm adjusts the coefficients during the training phase so that the distances from the dots to the line are minimised.
