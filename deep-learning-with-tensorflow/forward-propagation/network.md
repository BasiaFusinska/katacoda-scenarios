Our goal is to build the simple neural network. It will only have _input and output layer_. The number of neurons in this case, is determined by the classification problem. The input layer has the same size as the feature dimensionality (two in our case). Because we're dealing with the binary classification, there is only one neuron in the output layer.

You can see how the architecture looks like in the image below.

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/forward-propagation/assets/network.png" alt="Network architecture">

The output layer holds the _weights_ and the _bias_. The whole point of the forward propagation is to use them when multiplying with the input data and aggregate by summation. In the end, we will use the activation function, but let us elaborate on this in the next steps.

You should recognise the inside of the equation as vectorised operations: matrix multiplication and add.
