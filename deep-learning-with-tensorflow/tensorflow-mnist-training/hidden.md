The next thing is to build the input and hidden layer. Later we will be connecting it to the output.

## Task 2

Define the [placeholders](https://www.tensorflow.org/api_docs/python/tf/placeholder) for the input data and the labels. The dimensions are given in the code or you can just try to figure them out on your own.

## Task 3

To set up the hidden layer you have to create the [variables](https://www.tensorflow.org/api_docs/python/tf/Variable). Use the [random values](https://www.tensorflow.org/api_docs/python/tf/truncated_normal) for the weights and [constants](https://www.tensorflow.org/api_docs/python/tf/constant) for the biases.

The hidden layer is the result of the multiplying the input and weights, adding biases and wrapping up with the [reLU](https://www.tensorflow.org/api_docs/python/tf/nn/relu) function.
