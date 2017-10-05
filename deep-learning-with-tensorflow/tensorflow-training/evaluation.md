We'll use the `accuracy` defined previously to monitor the performance during the training process. The code will print it every 100 steps.

<pre class="file" data-filename="neural_network.py" data-target="append">
  # Print the accuracy progress on the batch every 100 steps
  if i%10 == 0:
    train_accuracy = accuracy.eval(feed_dict=feed_dict)
    print("Step %d, training accuracy %g %%"%(i, train_accuracy*100))
</pre>

The file is ready now, and we can run it using the following command:

`python neural_network.py`{{execute}}

The last line is showing the accuracy we got for the trained model.
