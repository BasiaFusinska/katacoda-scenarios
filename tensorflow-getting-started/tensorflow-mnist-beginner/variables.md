Placeholders will be filled with the values passed when evaluating the computation graph. But the actual goal of the training is to adjust the values of the weights and biases. This is why we need the structure that will allow changing the values along the process.

TensorFlow provides variables for this exact purpose. The initial values for the weights will follow the normal distribution while biases will get the value 1.0. Once we have them defined, the creation of the output layer is just one line.

<pre class="file" data-filename="app.py" data-target="append">
# Variables to be tuned
W = tf.Variable(tf.truncated_normal([image_size*image_size, labels_size], stddev=0.1))
b = tf.Variable(tf.constant(0.1, shape=[labels_size]))

# Build the network (only output layer)
output = tf.matmul(training_data, W) + b
</pre>
