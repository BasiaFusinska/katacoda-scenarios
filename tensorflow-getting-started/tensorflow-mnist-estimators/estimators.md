TensorFlow `tf.contrib.learn` is a high level API for machine learning process. It offers variety of `Estimator`s that represent predefined models. Some of the examples are:
* [LinearClassifier](https://www.tensorflow.org/api_docs/python/tf/contrib/learn/LinearClassifier) - model for linear classification
* [KMeansClustering](https://www.tensorflow.org/api_docs/python/tf/contrib/learn/KMeansClustering) - an estimator for K-Means clustering.
* [DNNClassifier](https://www.tensorflow.org/api_docs/python/tf/contrib/learn/DNNClassifier) - a classifier for deep neural network models
* [DNNRegressor](https://www.tensorflow.org/api_docs/python/tf/contrib/learn/DNNRegressor) - deep neural network models.

You are also provided with the techniques to write your own estimators if the list of available ones is not sufficient.

In this tutorial we will use the `DNNClassifier` to train the model and predict the labels for the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). We will be solving the classification task and try to recognise the actual digit from its handwritten representation.

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-mnist-estimators/assets/MNIST-classification.png" alt="MNIST Classification">
