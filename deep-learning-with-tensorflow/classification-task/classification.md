[Classification](https://en.wikipedia.org/wiki/Statistical_classification) is one of the classical problems in the [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning) field. As all the ML tasks, it is relying on the historical data. Assuming that the data contain the underlying pattern, the algorithm is _trained_ based on them. Once the learning is finished, the resulting model is supposed to be able to _generalise_ the embedded rules and predict the new examples.

The primary task of classification problem is to _find the correct labels_ for the presented examples. As mentioned, to properly train the model we have to have the past records, so that the algorithms can adjust its parameters. Classification is an example of supervised learning, which means that the historical data has to contain labels along the features.

In this scenario, we're going to classify the dots shown in the following picture. You can treat them as geometrical data. The _(x1,x2)_ coefficients are the examples features, while the colour indicates the labels (red and blue).

In this example, we have only two classes we expect the model to assign the records. This type is often called binary classification. The data have only two features, so they are easy to visualise. This is not the case with most of the real world problems, where we can expect even thousands of dimensions.
