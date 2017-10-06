The fully connected layers' code has bee already written for you. The last thing to do is to pipe in together the convolutional with it.

## Task 5

As the next hidden layer requires one-dimensional vector to work, you need to flatten the output of the second convolutional layer before you feed it with the dense one. For this task, you can use `tf.reshape` function. Try to figure out the result size or use the hint in the code.
