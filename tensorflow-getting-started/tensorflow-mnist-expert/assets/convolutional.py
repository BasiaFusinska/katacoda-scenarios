import tensorflow as tf

image_size = 28
labels_size = 10
hidden_size = 1024

# Define placeholders
training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
training_images = tf.reshape(training_data, [-1, image_size, image_size, 1])

labels = tf.placeholder(tf.float32, [None, labels_size])

# 1st convolutional layer variables
W_conv1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1))
b_conv1 = tf.Variable(tf.constant(0.1, shape=[32]))

# 1st convolution & max pooling
conv1 = tf.nn.relu(tf.nn.conv2d(training_images, W_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)
pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# 2nd convolutional layer variables
W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
b_conv2 = tf.Variable(tf.constant(0.1, shape=[64]))

# 2nd convolution & max pooling
conv2 = tf.nn.relu(tf.nn.conv2d(pool1, W_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2)
pool2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# Flatten the 2nd convolution layer
pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])

#Variables for the hidden dense layer
W_h = tf.Variable(tf.truncated_normal([7 * 7 * 64, hidden_size], stddev=0.1))
b_h = tf.Variable(tf.constant(0.1, shape=[hidden_size]))

# Hidden layer with reLU activation function
hidden = tf.nn.relu(tf.matmul(pool2_flat, W_h) + b_h)

# Dropout
keep_prob = tf.placeholder(tf.float32)
hidden_drop = tf.nn.dropout(hidden, keep_prob)

# Variables to be tuned
W = tf.Variable(tf.truncated_normal([hidden_size, labels_size], stddev=0.1))
b = tf.Variable(tf.constant(0.1, shape=[labels_size]))

# Connect hidden to the output layer
output = tf.matmul(hidden_drop, W) + b

# Train & test the network
import training
training.train_network(training_data, labels, output, keep_prob)
