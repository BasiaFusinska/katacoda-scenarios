import pandas as pd
import numpy as np
import tensorflow as tf

# Read data
data = pd.read_csv('dataset.csv')
X = data.as_matrix(['x1', 'x2'])
Y = data.as_matrix(['label'])

learning_rate = 0.5
steps_number = 10000
hidden_size = 5

# Task 1: Define placeholders
x = # TODO: Placeholder shape [None, 2]
labels = # TODO: Placeholder shape [None, 1]

# Task 2: Define hidden layer
Wh = # TODO: Variable shape [2, hidden_shape]
bh = # TODO: Variable shape [1, hidden_shape]
hidden = # TODO: multiply x, W; add b; use tf.nn.tanh as activation function

# Task 3: Build the output layer
Wo = # TODO: Variable shape [hidden_shape, 1]
bo = # TODO: Variable shape [1, 1]
output = # TODO: multiply hidden, W; add b;

# Define the loss function
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=labels, logits=output))

# Training step
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

# Accuracy calculation
predictions = tf.greater(tf.sigmoid(output), 0.5)
correct_prediction = tf.equal(predictions, tf.equal(labels,1.0))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Run the training
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

for i in range(steps_number):
  # Task 4: Set up the dictionary
  feed_dict = # TODO: use X and Y

  # Run the training step
  train_step.run(feed_dict=feed_dict)

  # Print the accuracy progress on the batch every 1000 steps
  if i%1000 == 0:
    train_accuracy = accuracy.eval(feed_dict=feed_dict)
    print("Step %d, training accuracy %g %%"%(i, train_accuracy*100))
