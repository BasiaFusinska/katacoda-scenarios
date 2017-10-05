Training process works by optimising the loss function. We'll use [Cross entropy](https://en.wikipedia.org/wiki/Cross_entropy). TensorFlow provides the function called `tf.nn.sigmoid_cross_entropy_with_logits` that internally applies the sigmoid on the model's unnormalized prediction and sums across all classes. The `tf.reduce_mean` function takes the average over these sums. Then we'll define Gradient Descent optimiser, that will work in several steps adjusting the values of the W and b variables.

<pre class="file" data-filename="neural_network.py" data-target="append">
# Define the loss function
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=labels, logits=output))

# Training step
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
</pre>

To evaluate the algorithm performance, we will calculate the accuracy by establishing the predicted classes and comparing with the train data labels.

<pre class="file" data-filename="neural_network.py" data-target="append">
# Accuracy calculation
predictions = tf.greater(tf.sigmoid(output),0.5)
correct_prediction = tf.equal(predictions, tf.equal(labels,1.0))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
</pre>
