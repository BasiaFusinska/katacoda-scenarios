After setting up al the computation graph elements, you should set up the training session.

`sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())`

## Task 6

The training process is already implemented. What you need to do is:

* get the next batch (use the `batch_size` int the `mnist.train.next_batch`)
* set the `feed_data` for accuracy evaluation
* set the `feed_batch` for the `train_step` run
