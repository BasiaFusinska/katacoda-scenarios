The definition of the loss function, the rest of the computational graph and the training process have been provided for you in the `train_evaluate_network` function in the `helper.py` file. The loss function is defined as follows:

`loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=output))`

And we have used Adam Optimiser to minimise it:

`train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss)`

Once you decide the code is ready run it with the following command:

`python neural_network.py`{{execute}}
