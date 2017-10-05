In this step, you will add the hidden layer to the architecture. This layer connects the input data with the output. As a fully connected it stores weights and biases and performs the activation function after the matrix multiplication.

## Task 2

To define the hidden layer, you need to think of the complete steps:

* Define weights and biases as TensorFlow [variables](https://www.tensorflow.org/api_docs/python/tf/Variable).
* Multiply the input data with the weights, add bias
* Apply [tanh](https://www.tensorflow.org/api_docs/python/tf/tanh) as the activation function
