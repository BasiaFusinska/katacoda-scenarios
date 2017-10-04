So far we defined how the optimisation process should look like. In TensorFlow this means establishing the computation graph. Now it's time for running it inside of the session.

We'll create the session and initialise the variables.

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

The process will run iteratively.

for i in range(20):
   sess.run(train_step)

After it's done, let's print the result and close the session.

y_v, x_v = sess.run(y), sess.run(x)
print 'Minimised value is: %d for the x: %d' % y_v, x_v
sess.close()
