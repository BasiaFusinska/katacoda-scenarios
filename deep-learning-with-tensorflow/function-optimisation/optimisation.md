So far we defined how the optimisation process should look like. In TensorFlow this means establishing the computation graph. Now it's time for running it inside of the session.

We'll create the session and initialise the variables.

`sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())`{{execute}}

The process will run iteratively.

`for i in range(20):
   sess.run(optimiser)

`{{execute}}

After it's done, let's print the result and close the session.

`print('Minimised value is: {} for the x: {}'.format(sess.run(y), sess.run(x)))
sess.close()`{{execute}}
