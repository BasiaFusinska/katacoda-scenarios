In the last scenario, we've built a simple neural network, with just one output layer. As we know this is not sufficient when working with the non linearly separated data.

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/tensorflow-deep-training/assets/dataset.png" alt="Dataset">

The network will need the hidden layer, so the architecture will look as follows:

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/tensorflow-deep-training/assets/network.png" alt="Neural network">

You will be writing the code in the `neural_network.py`{{open}} file. Specific tasks have been marked. As you can see, we have loaded the data for you and set up some variables for the further process.

## Task 1

The first thing you need to do is to define the [placeholders](https://www.tensorflow.org/api_docs/python/tf/placeholder) for the input data and labels. Because the size of the input data doesn't have to be defined now, you can use `None`.
