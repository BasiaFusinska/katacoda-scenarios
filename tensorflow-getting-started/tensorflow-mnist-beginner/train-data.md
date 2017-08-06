Our task is to build a classifying neural network with TensorFlow. First, we need set up the architecture, train the network (using training set) and then evaluate the result on the test set.

The following image shows the classification process and the layers of the neural network:

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-mnist-beginner/assets/network.png" alt="Neural network">

To feed the network with the training data, we need to flatten the digit images. Depending on the phase (training or testing), different examples will be pushed through the classifier. The training process will be based on the labels while comparing them to the current predictions. This is why we need to define these two placeholders.

<pre class="file" data-filename="app.py" data-target="append">
# Define placeholders
training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
labels = tf.placeholder(tf.float32, [None, labels_size])
</pre>
