TensorFlow uses something called deferred execution. This means that first you are building your *computational graph* and then once you have all the elements put together, you run it.

The graph works on the tensors as input and output. Some of the nodes don't take any inputs, because they are tensors themselves. Let's build a simple example adding two numbers: 2 and 5. The graph would look like this (obtained by with TensorBoard):

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-core/assets/add-graph.png" alt="Adding Graph">

The values of the numbers are stored in the *placeholders*. The implicit type is float, but you can specify it using `dtype` argument:

`input1 = tf.constant(2.0)
input2 = tf.constant(5.0)`{{execute}}

Because we are still building the graph, printing the inputs won't display the stored values. They will be shown once the nodes are evaluated.

`print(input1, input2)`{{execute}}
