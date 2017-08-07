In the last step, we created two convolutional layers and flattened the results. Now it's time to connect it to the dense hidden layer. This is analogical to what we've already seen in the second step of the tutorial with the difference that this time we use `pool2_flat` instead of the images as input.

`W_h = tf.Variable(tf.truncated_normal([7 * 7 * 64, hidden_size], stddev=0.1))
b_h = tf.Variable(tf.constant(0.1, shape=[hidden_size]))`

`hidden = tf.nn.relu(tf.matmul(pool2_flat, W_h) + b_h)`

We could now just connect the hidden dense layer to the output, but we would like to do one more thing - apply the dropout. *Dropout* is the technique that is used to avoid overfitting by not using some neurons when training the network.

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-mnist-expert/assets/dropout.png" alt="Dropout">

It's very important to dropout the neurons only in the training phase, but not when evaluating the model. This is why define an additional placeholder to keep the dropout probability. Then we use `tf.nn.dropout` function.

`keep_prob = tf.placeholder(tf.float32)
hidden_drop = tf.nn.dropout(hidden, keep_prob)`

The last step is to connect it to the output layer.

`W = tf.Variable(tf.truncated_normal([hidden_size, labels_size], stddev=0.1))
b = tf.Variable(tf.constant(0.1, shape=[labels_size]))`

`output = tf.matmul(hidden_drop, W) + b`

You can run the code with the command:

`python convolutional.py`{{execute}}

Notice that the complexity of the network is influencing the speed of training, but also improving the accuracy. Try to adjust the result by changing the training parameters.
