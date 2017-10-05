There are some training hyperparameters set up:

`learning_rate = 1e-4
steps_number = 1000
batch_size = 100`

We have written the loss function which is the [softmax cross entropy with logits](https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits).

`loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=output))`

## Task 5

Your task is now to set up the optimisation to minimise the loss function. You should use the [Adam Optimiser](https://www.tensorflow.org/api_docs/python/tf/train/AdamOptimizer) with the provided `learning_rate`.
