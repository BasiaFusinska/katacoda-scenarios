import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Task 1: Load MNIST dataset
mnist =

image_size = 28
labels_size = 10
hidden_size = 1024

# Task 2: Define placeholders
training_data = # TODO: Placeholder shape: [None, image_size*image_size]
labels = # TODO: Placeholder shape: [None, labels_size]

# Task 3: Define hidden layer with reLU activation function
Wh = # TODO: Variable shape: [image_size*image_size, hidden_size]
bh = # TODO: Variable shape: [hidden_size]

hidden = # TODO: training_data x Wh + bh; use tf.nn.relu

# Define output layer
Wo = # TODO: Variable shape: [hidden_size, labels_size]
bo = # TODO: Variable shape: [labels_size]

output = # TODO: hidden x Wo + bo

learning_rate = 1e-4
steps_number = 1000
batch_size = 100

# Define the loss function
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=output))

# Task 4: Define Adam Optimiser to minimise the loss
train_step =

# Accuracy calculation
correct_prediction = tf.equal(tf.argmax(output, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Start the session
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

# Task 5: Define training
for i in range(steps_number):
    input_batch, labels_batch = # TODO: Get the next batch from the training data, use batch_size

    # Print the accuracy progress on the batch every 100 steps
    if i%100 == 0:
        feed_batch = # TODO: Use batch data
        train_accuracy = accuracy.eval(feed_dict=feed_batch)
        print("Step %d, training batch accuracy %g %%"%(i, train_accuracy*100))

        # Run the training step
        feed_data = # TODO: Use training data
        train_step.run(feed_dict=feed_data)

    print("The end of training!")

# Task 6: Evaluate on the test set
feed_test = # TODO: Use test data
test_accuracy = accuracy.eval(feed_dict=feed_test)
print("Test accuracy: %g %%"%(test_accuracy*100))

sess.close()
