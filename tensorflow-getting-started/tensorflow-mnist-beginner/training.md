Now is the time when we have the computational graph built, and we can start the training process. To start, we need to initialise the session and variables defined earlier.

<pre class="file" data-filename="app.py" data-target="append">
# Run the training
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

</pre>

As mentioned before, optimiser works in steps. In our case, we run the `train_step` inside the loop feeding it with the batch data: images and corresponding labels. This is the moment where we fill in the placeholders by using `feed_dict` parameters of the function `run`.

<pre class="file" data-filename="app.py" data-target="append">
for i in range(steps_number):
  # Get the next batch
  input_batch, labels_batch = mnist.train.next_batch(batch_size)
  feed_dict = {training_data: input_batch, labels: labels_batch}

  # Run the training step
  train_step.run(feed_dict=feed_dict)
</pre>

We can make use of the `accuracy` defined previously to monitor the performance on the batches during the training process. By adding the following code, we will print out the value every 100 steps.

<pre class="file" data-filename="app.py" data-target="append">
  # Print the accuracy progress on the batch every 100 steps
  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict=feed_dict)
    print("Step %d, training batch accuracy %g %%"%(i, train_accuracy*100))
</pre>
