The default architecture consists of only one output layer. This influences both performance and accuracy. In this step, we will add another dense layer to the network.

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-mnist-expert/assets/hidden.png" alt="Hidden layer">

We will start with defining the function and placeholders.

<pre class="file" data-filename="app.py" data-target="replace">
import tensorflow as tf

def get_layers(image_size, labels_size):
    # Define placeholders
    training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
    labels = tf.placeholder(tf.float32, [None, labels_size])
</pre>

Then we define the hidden layer as the dense one. We chose to use 1024 neurons and [reLU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) as the activation function. Notice that we used the `tf.nn.relu` after performing the matrices multiplication.

<pre class="file" data-filename="app.py" data-target="append">
    # Variables for the hidden layer
    hidden_size = 1024

    W_h = tf.Variable(tf.truncated_normal([image_size*image_size, hidden_size], stddev=0.1))
    b_h = tf.Variable(tf.constant(0.1, shape=[hidden_size]))

    # Build the network (only output layer)
    hidden = tf.nn.relu(tf.matmul(training_data, W_h) + b_h)
</pre>

As a finishing touch, we connect hidden layer with the output one and return required objects. Notice that we changed the dimension for the weights variable to fit the hidden layer instead of the input one.

<pre class="file" data-filename="app.py" data-target="append">
    # Variables to be tuned
    W = tf.Variable(tf.truncated_normal([hidden_size, labels_size], stddev=0.1))
    b = tf.Variable(tf.constant(0.1, shape=[labels_size]))

    # Build the network (only output layer)
    output = tf.matmul(hidden, W) + b

    return training_data, labels, output
</pre>

Once the code is in the `nnlayers.py` you can run the whole thing using the following command:

`python training.py`{{execute}}
