Our task is to build a classifying neural network with TensorFlow. First, we need set up the architecture:

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/tensorflow-training/assets/network.png" alt="Neural network">

TensorFlow works by creating the proper computational graph. To build the network we need to establish the input data. Usually, you should use tf.placeholders here. First one will be the training data inputs, second is representing the labels (colours of the dots). The actual values will be passed when the network is trained.

<pre class="file" data-filename="neural_network.py" data-target="append">
# Define placeholders
x = tf.placeholder(tf.float32, [None, 2])
labels = tf.placeholder(tf.float32, [None, 1])
</pre>
