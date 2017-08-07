import tensorflow as tf

image_size = 28
labels_size = 10
hidden_size = 1024

# Define placeholders
training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
labels = tf.placeholder(tf.float32, [None, labels_size])

# Variables for the hidden layer
W_h = tf.Variable(tf.truncated_normal([image_size*image_size, hidden_size], stddev=0.1))
b_h = tf.Variable(tf.constant(0.1, shape=[hidden_size]))

# Hidden layer with reLU activation function
hidden = tf.nn.relu(tf.matmul(training_data, W_h) + b_h)

# Variables for the output layer
W = tf.Variable(tf.truncated_normal([hidden_size, labels_size], stddev=0.1))
b = tf.Variable(tf.constant(0.1, shape=[labels_size]))

# Connect hidden to the output layer
output = tf.matmul(hidden, W) + b

# Train & test the network
import training
training.train_network(training_data, labels, output)
