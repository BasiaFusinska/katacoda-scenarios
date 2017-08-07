The next two layers we're going to add are the integral parts of *convolutional networks*. They work differently than the dense ones and perform especially well with 2- and more dimensions input. The parameters of the [convolutional layer](https://en.wikipedia.org/wiki/Convolutional_neural_network) are the size of the convolution window and the strides. *Padding* set as `'SAME'` indicates that the resulting layer is of the same size. After this step, we apply *max pooling*. We will build two convolutional layers, connect it to the dense hidden layer. The resulting architecture can be visualised as follows:

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-mnist-expert/assets/convolution.png" alt="Convolutional network">

The code for the whole network can be found in the `convolutional.py`{{open}} and we will walk you through it now. In the previous example placeholders are representing flattened digits' images and the corresponding labels. Although, a convolutional layer can work with higher dimensional data, so we need to reshape the images.

`training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
training_images = tf.reshape(training_data, [-1, image_size, image_size, 1])
labels = tf.placeholder(tf.float32, [None, labels_size])`

Next step is to set up the variables for the first convolutional layer. Then we initiate the convolutional and max polling phases. As you can see we use the variety of tf.nn functions like `relu`, `conv2d` or `max_pool`. This layer reads the reshaped images directly from the input data.

`W_conv1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1))
b_conv1 = tf.Variable(tf.constant(0.1, shape=[32]))`

`conv1 = tf.nn.relu(tf.nn.conv2d(training_images, W_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)
pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')`

The second layer is analogical and has been defined below. Notice that as in input it takes the result of the max polling from the previous step.

`W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
b_conv2 = tf.Variable(tf.constant(0.1, shape=[64]))`

`conv2 = tf.nn.relu(tf.nn.conv2d(pool1, W_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2)
pool2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')`

The last thing left is to connect it to the next layer which is a dense hidden one. Dense layers don't work with the dimensions of the convolution, so we need to flatten the result from the convolution phase.

`pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])`

The next step will show how to connect it to the hidden dense layer.
