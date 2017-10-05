As we've shown in the previous scenarios, the goal of the training process is to adjust the values of the weights and biases. This is why we need the structure that will allow changing the values along the process.

TensorFlow provides variables for this exact purpose. The input layer has the size 2, and the output is just one neuron. We'll initially put them all with the values 0.1. Once we have them defined, the creation of the output layer is just one line.

<pre class="file" data-filename="neural_network.py" data-target="append">
# Variables to be tuned
W = tf.Variable([[0.1], [0.1]], dtype=tf.float32)
b = tf.Variable([0.1], dtype=tf.float32)

# Build the network (only output layer)
output = tf.matmul(x, W) + b
</pre>
