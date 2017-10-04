We know how our network is predicting. The next step is to set up the loss function. This will become the [function](https://en.wikipedia.org/wiki/Loss_functions_for_classification) we are going to optimise in the process. By finding the optimum, the algorithm will adjust the values of the weights and biases in the training process.

We will use the [cross-entropy loss](https://en.wikipedia.org/wiki/Cross_entropy) which equation can be set up as follows:
<img src="/basiafusinska/courses/deep-learning-with-tensorflow/neural-network-training/assets/loss.png" alt="Loss function">

You can find the implementation in the `helper.py` file as `cost` function.
