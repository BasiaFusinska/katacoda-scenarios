import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

image_size = 28
labels_size = 10
hidden_size = 1024

# Load MNIST dataset
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Define placeholders
training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
labels = tf.placeholder(tf.float32, [None, labels_size])

# Task 1: reshape the input images
training_images = # TODO: Use tf.reshape with the shape [-1, image_size, image_size, 1]

# Task 2: Define 1st convolutional layer variables
W_conv1 = # TODO: Variable shape: [5, 5, 1, 32]
b_conv1 = # TODO: Variable shape: [32]

# Task 3: Define 1st convolution & max pooling
conv1 = # TODO: use tf.nn.conv2d with strides=[1, 1, 1, 1], padding='SAME'; wrap in tf.nn.relu
pool1 = # TODO: use tf.nn.max_pool with ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME'

# Task 4: 2nd convolutional layer variables
W_conv2 = # TODO: Variable shape: [5, 5, 32, 64]
b_conv2 = # TODO: Variable shape: [64]

# 2nd convolution & max pooling
conv2 = # TODO: use tf.nn.conv2d with strides=[1, 1, 1, 1], padding='SAME'; wrap in tf.nn.relu
pool2 = # TODO: use tf.nn.max_pool with ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME'

# Task 5: Flatten the 2nd convolution layer
pool2_flat = # TODO: Use tf.reshape with the shape [-1, 7 * 7 * 64]

#Variables for the hidden dense layer
W_h = tf.Variable(tf.truncated_normal([7 * 7 * 64, hidden_size], stddev=0.1))
b_h = tf.Variable(tf.constant(0.1, shape=[hidden_size]))

# Hidden layer with reLU activation function
hidden = tf.nn.relu(tf.matmul(pool2_flat, W_h) + b_h)

# Variables to be tuned
W = tf.Variable(tf.truncated_normal([hidden_size, labels_size], stddev=0.1))
b = tf.Variable(tf.constant(0.1, shape=[labels_size]))

# Connect hidden to the output layer
output = tf.matmul(hidden, W) + b

import helper as h
h.train_evaluate_network(training_data, labels, output, mnist)
