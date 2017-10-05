We've built our computation graph, so it's time to run the actual training. To do this TensorFlow requires opening the session.

<pre class="file" data-filename="neural_network.py" data-target="append">
# Run the training
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
</pre>

We are going to run the training in steps. In our case, we run the `train_step` inside the loop feeding it with the input data and corresponding labels. This is the moment where we fill in the placeholders by using `feed_dict` parameters of the function `run`.

<pre class="file" data-filename="neural_network.py" data-target="append">
for i in range(steps_number):
  # Set up the dictionary
  feed_dict = {x: X, labels: Y}

  # Run the training step
  train_step.run(feed_dict=feed_dict)
</pre>
