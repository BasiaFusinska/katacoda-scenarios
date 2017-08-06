import tensorflow as tf

def get_layers(image_size, labels_size):
    # Define placeholders
    training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
    labels = tf.placeholder(tf.float32, [None, labels_size])

    # Variables to be tuned
    W = tf.Variable(tf.zeros([image_size*image_size, labels_size]))
    b = tf.Variable(tf.zeros([labels_size]))

    # Build the network (only output layer)
    output = tf.matmul(training_data, W) + b

    return training_data, labels, output
