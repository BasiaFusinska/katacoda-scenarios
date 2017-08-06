Training process works by optimising (either maximising or minimising) the loss function. In our case, we would like to minimise the difference between the network predictions and actual labels' values. In deep learning, we often use a technique called [Cross entropy](https://en.wikipedia.org/wiki/Cross_entropy) to define the loss.

TensorFlow provides the function called `tf.nn.softmax_cross_entropy_with_logits` that internally applies the softmax on the model's unnormalized prediction and sums across all classes. The `tf.reduce_mean` function takes the average over these sums. This way we get the function that can be further optimised. In our example, we use [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) method from the `tf.train` API.

<pre class="file" data-filename="app.py" data-target="append">
# Define the loss function
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=output))

# Training step
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
</pre>

Gradient descent optimiser will work in several steps adjusting the values of the W and b variables. We would also like to have a way of evaluating the performance.

First, we want to compare which labels were predicted correctly by using `tf.argmax` function. `tf.equal` returns the list of booleans so by casting the values to float and then calculating the average we finally get the accuracy of the model.

<pre class="file" data-filename="app.py" data-target="append">
# Accuracy calculation
correct_prediction = tf.equal(tf.argmax(output, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
</pre>
