The default architecture consists of only one output layer. This influences both performance and accuracy. In this step, we will add another dense layer to the network. The whole code can bee seen in the `hidden.py`{{open}} file.

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-mnist-expert/assets/hidden.png" alt="Hidden layer">

As in the case of one output layer, the code should start with defining the placeholders, which are representing flattened digits' images and the corresponding labels.

`training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
labels = tf.placeholder(tf.float32, [None, labels_size])`

Then we define the hidden layer as the dense one. We chose to use 1024 neurons and [reLU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) as the activation function. Because it will be another dense layer, we need to define the weights and biases variables.

`W_h = tf.Variable(tf.truncated_normal([image_size*image_size, hidden_size], stddev=0.1))
b_h = tf.Variable(tf.constant(0.1, shape=[hidden_size]))`

TensorFlow provides the `tf.nn.relu` function that will be applied after performing the matrices multiplication.

`hidden = tf.nn.relu(tf.matmul(training_data, W_h) + b_h)`

As a finishing touch, we connect hidden layer with the output one and return required objects. Notice that we changed the dimension for the weights variable to fit the hidden layer instead of the input one.

`W = tf.Variable(tf.truncated_normal([hidden_size, labels_size], stddev=0.1))
b = tf.Variable(tf.constant(0.1, shape=[labels_size]))`

`output = tf.matmul(hidden, W) + b`

You can run the whole thing using the following command:

`python hidden.py`{{execute}}
