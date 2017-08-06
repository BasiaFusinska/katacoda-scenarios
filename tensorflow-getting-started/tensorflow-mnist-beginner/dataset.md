This scenario is an introduction to how to use [TensorFlow](https://www.tensorflow.org/) when building a simple neural network architecture, training the model and evaluate the results. We will be working on the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). We will be solving the classification task and try to recognise the actual digit from its handwritten representation.

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-mnist-beginner/assets/MNIST-classification.png" alt="MNIST Classification">

TensorFlow has the dataset already built in, so there is no need to manually download it.

To start working with MNIST let us include some necessary imports:

<pre class="file" data-filename="app.py" data-target="replace">
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Read data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
</pre>

The code uses built-in capabilities of TensorFlow to download the dataset locally and load it into the python variable. As a result (if not specified otherwise), the data will be downloaded into the `MNIST_data/` folder.

We are also defining some of the values that will be use further in the code:
<pre class="file" data-filename="app.py" data-target="append">
image_size = 28
labels_size = 10
learning_rate = 0.05
steps_number = 1000
batch_size = 100
</pre>
