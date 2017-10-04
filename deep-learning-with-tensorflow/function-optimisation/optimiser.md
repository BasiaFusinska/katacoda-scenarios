Once the loss function is defined, all you need to do is to choose the optimiser. In our task, we will apply [Gradient Descent](https://www.tensorflow.org/api_docs/python/tf/train/GradientDescentOptimizer) from TensorFlow.

`optimiser = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)`{{execute}}

This is it! No calculations of the gradient, no variables updating. All is taken care of inside of the GradientDescentOptimizer class. Have a look at other optimiser options.
