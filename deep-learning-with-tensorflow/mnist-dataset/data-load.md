To start working with MNIST let us include some necessary imports:

`import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data`{{execute}}

Then we can use the helper function to load the data. The code uses built-in capabilities of TensorFlow to download the dataset locally and load it into the python variable. As a result, the data will be downloaded into the provided folder.

`mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)`{{execute}}

Notice that if you use the parameter `one_hot` with the value `False` it will set up actual numbers as the labels. Sometimes this representation may be helpful.
