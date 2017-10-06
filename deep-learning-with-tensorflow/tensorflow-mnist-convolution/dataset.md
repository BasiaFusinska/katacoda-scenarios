In this scenario, you will be adding two convolutional layers to the neural network, you've built previously. To start the lab, open the `neural_network.py`{{open}} file and follow the instructions. We will be classifying the MNIST dataset, so the first thing we need to get is the dataset itself.

`mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)`

Then the placeholders are defined.

`training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
labels = tf.placeholder(tf.float32, [None, labels_size])`

The network architecture will look like in the image below. You will implement the convolutional and max-pooling layers. The dense ones and the training process is already there.

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/tensorflow-mnist-convolution/assets/convolution.png" alt="Convolutional Neural Network">

## Task 1

The images read from the dataset are flattened. For the first convolution layer to work properly they should be reshaped into 2D. For this task you can use the [tf.reshape](https://www.tensorflow.org/api_docs/python/tf/reshape) function and apply it to the `training_data`.
