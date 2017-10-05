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
  feed_dict = {training_data: X, labels: Y}

  # Run the training step
  train_step.run(feed_dict=feed_dict)
</pre>

We'll use the `accuracy` defined previously to monitor the performance during the training process. The code will print it every 100 steps.

<pre class="file" data-filename="neural_network.py" data-target="append">
  # Print the accuracy progress on the batch every 100 steps
  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict=feed_dict)
    print("Step %d, training accuracy %g %%"%(i, train_accuracy*100))
</pre>
