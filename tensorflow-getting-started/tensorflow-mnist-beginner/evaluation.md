After the training is finished we would like to check the network performance on the data it hasn't previously seen - in the test set. We can reuse `accuracy` and feed it with the training data instead of the training batch.

<pre class="file" data-filename="app.py" data-target="append">
# Evaluate on the test set
test_accuracy = accuracy.eval(feed_dict={training_data: mnist.test.images, labels: mnist.test.labels})
print("Test accuracy: %g %%"%(test_accuracy*100))
</pre>

The file is ready now, and we can run it using the following command:

`python app.py`{{execute}}

Try to change some values like `learning_rate` or `steps_number` to see if you can influence the accuracy.
