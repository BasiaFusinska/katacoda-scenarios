import tensorflow as tf

def get_layers(image_size, labels_size):
    # Define placeholders
    training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
    labels = tf.placeholder(tf.float32, [None, labels_size])

    # Variables to be tuned
    W = tf.Variable(tf.truncated_normal([image_size*image_size, labels_size], stddev=0.1))
    b = tf.Variable(tf.constant(0.1, shape=[labels_size]))

    # Build the network (only output layer)
    output = tf.matmul(training_data, W) + b

    return training_data, labels, output
