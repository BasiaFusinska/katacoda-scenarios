To evaluate the computational graph, or any node for that matter, you need to run it within a *session*. The session can be created using the following code:

`sess = tf.Session()`{{execute}}

Once the session is on, you can use `run` method to get the values. Try doing it for constant inputs:

`print(sess.run([input1, input2]))`{{execute}}

Notice that this time the output is the actual expected number values: 2.0 and 5.0.

To finish the graph we need the third node and the `add` method:

`add_node = tf.add(input1, input2)`{{execute}}

As previously you can see different outputs depending if the node was or wasn't evaluated.

`print(add_node)
print(sess.run(add_node))`{{execute}}

The first line displays the tensor information, second - the result of adding calculation: 7.0.
