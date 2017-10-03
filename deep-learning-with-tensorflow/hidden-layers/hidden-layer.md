_Hidden layers_ are the ones that are placed between the input and the output. They are usually not really hidden, which means you have full access to them. The name is more historical than anything.

Unlike the output layer, hidden ones are not usually activated using the sigmoid function. Instead, there are applied other like [tanh or reLU](https://en.wikipedia.org/wiki/Activation_function).

## Task 1

You are supposed to implement the `hidden_layer_fp`. The code should be similar to the one written for the output. The difference is the activation function. You can use the [np.tanh](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.tanh.html) for this.
