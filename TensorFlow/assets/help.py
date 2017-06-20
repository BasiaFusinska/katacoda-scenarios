import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

def read_mnist(folder_path="MNIST_data/"):
    return input_data.read_data_sets(folder_path, one_hot=True)

def build_training(y_labels, y_output, learning_rate=0.5):
    # Define loss function
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_labels, logits=y_output))
    #train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
    train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

    # Calculate accuracy
    correct_prediction = tf.equal(tf.argmax(y_output,1), tf.argmax(y_labels,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    return train_step, accuracy

def train_test_model(mnist, x_input, y_labels, accuracy, train_step, steps=1000, batch=100):
    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())
    for i in range(steps):
      input_batch, labels_batch = mnist.train.next_batch(batch)
      feed_dict = {x_input: input_batch, y_labels: labels_batch}

      if i%100 == 0:
        train_accuracy = accuracy.eval(feed_dict=feed_dict)
        print("Step %d, training batch accuracy %g"%(i, train_accuracy))

      train_step.run(feed_dict=feed_dict)

    print("The end of training!")

    print("Test accuracy: %g"%accuracy.eval(feed_dict={x_input: mnist.test.images, y_labels: mnist.test.labels}))
    print("Validation accuracy: %g"%accuracy.eval(feed_dict={x_input: mnist.validation.images, y_labels: mnist.validation.labels}))

def train_test_model_dropout(mnist, x_input, y_labels, accuracy, train_step, should_drop, steps=1000, batch=100):
    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())
    for i in range(steps):
      input_batch, labels_batch = mnist.train.next_batch(batch)
      feed_dict = {x_input: input_batch, y_labels: labels_batch, should_drop: True}
      feed_dict_test = {x_input: input_batch, y_labels: labels_batch, should_drop: False}

      if i%100 == 0:
        train_accuracy = accuracy.eval(feed_dict=feed_dict_test)
        print("Step %d, training batch accuracy %g"%(i, train_accuracy))

      train_step.run(feed_dict=feed_dict)

    print("The end of training!")

    print("Test accuracy: %g"%accuracy.eval(feed_dict={x_input: mnist.test.images, y_labels: mnist.test.labels, should_drop: False}))
    print("Validation accuracy: %g"%accuracy.eval(feed_dict={x_input: mnist.validation.images, y_labels: mnist.validation.labels, should_drop: False}))
