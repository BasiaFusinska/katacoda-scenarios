It's time to make our network more complex. It will repay us with higher accuracy.

## Task 2

The _filter_ of the _convolutional layer_ will go through the 2D image. To make it happen, we need to define the variables for _weights_ and the _biases_. The size of the filter is 5x5, and we will set up the 32 features. Use `tf.truncated_normal` for the weights and `tf.constant` for the biases.

## Task 3

Here you will set up the first convolutional layer with the max-pooling on top. To accomplish this you can use [tf.nn.conv2d](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d) function for the convolutional layer. Apply `'SAME'` padding and 1x1 strides. Once the filter is applied, you need to add bias and wrap everything with the [reLU](https://www.tensorflow.org/api_docs/python/tf/nn/relu) function.

For the max-pooling layer just use [tf.nn.max_pool](https://www.tensorflow.org/api_docs/python/tf/nn/max_pool) function with the window size 2x2 and `'SAME'` padding.
