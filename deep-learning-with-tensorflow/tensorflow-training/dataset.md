In this scenario, we will use [TensorFlow](https://www.tensorflow.org/) for the task of building and training a simple neural network. As the dataset, we will be using the linearly separable one that you had a chance to work previously.

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/tensorflow-training/assets/dataset.png" alt="Dataset">

To start working on the task, open the `neural_network.py`{{open}} file. Include some necessary imports and read the data.

<pre class="file" data-filename="neural_network.py" data-target="replace">
import tensorflow as tf
import helper as h

# Read data
data = h.read_data()
</pre>

We are also defining some of the values that will be use further in the code:

<pre class="file" data-filename="neural_network.py" data-target="append">
learning_rate = 0.05
steps_number = 1000
</pre>
