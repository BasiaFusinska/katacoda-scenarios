To adjust the values of the variables we need to specify the expected results for our linear model. Working only with one dimension we could visualise the model:

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-core/assets/lin-model.png" alt="Linear model">

The data points have coordinates as values provided in the `x` and `y` placeholders and the lines' `a` and `b` parameters provide the slope and intercept. This means that adjusting the variables will give us the proper match of the line to the actual data points.

Let's say we want to fix the line for the data point from the image. This means we need to provide the values `0, 1, 2, 3, 4, 5` for the `x` and `-1, -0.5, 0, 0.5, 1, 1.5` for the `y` placeholders. As you can see, the initial values of `a` and `b` variables (the green line) don't really fit the data. To calculate the error, you can use the following code:

`squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)`{{execute}}

Let's run the calculations with the placeholders values:

`feed_dict = {
  x:[0,1,2,3,4,5],
  y:[-1,-.5,0,.5,1,1.5] }
print(sess.run(loss, feed_dict))`{{execute}}

As you can see the number is high, so let's try to fit the line a little better (brown line):

`assignA = tf.assign(a, [.25])
assignB = tf.assign(b, [0])
sess.run([assignA, assignB])`{{execute}}

Then the loss function with the same values for the placeholders would give the following result.

`print(sess.run(loss, feed_dict))`{{execute}}

The value is better, but still not perfect. With the given data we can actually find the perfect match, as the data points are forming the line.

`assignA = tf.assign(a, [.5])
assignB = tf.assign(b, [-1])
sess.run([assignA, assignB])
print(sess.run(loss, feed_dict))`{{execute}}

In the real world scenarios, the point wouldn't make the perfect line. The optimisation task would be to find the parameters that fit data the best (but not ideally) and the process itself wouldn't be manual. In the next tutorial, we will introduce automated way of adjusting the variables that machine learning algorithms are using.
