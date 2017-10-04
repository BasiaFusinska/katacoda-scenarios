Your task now is to use the same process to optimise the variables from the example in the TensorFlow Core scenario. Below you can see the problem reminder.

The first thing you should do is to create the placeholders for the x and y and variables for the linear model.

`x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

a = tf.Variable([1], dtype=tf.float32)
b = tf.Variable([-2], dtype=tf.float32)`{{execute}}

Then we should set up the model itself.

`linear_model = a*x + b`{{execute}}

The loss function is the sum of the squares of the differences between the points and the line.

`squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)`{{execute}}

Use this and the previous steps to optimise the loss function. Remember to pass the values in the feed_dict when you're evaluating the objects in the session: `{x:[0,1,2,3,4,5], y:[-1,-0.5,0,0.5,1,1.5]}` .
