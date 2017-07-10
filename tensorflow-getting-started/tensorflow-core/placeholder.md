Another structure TensorFlow provides is a *placeholder*. Unlike the constants, where you provide the value when defining the node, a placeholder is expecting the values when the graph is being evaluated. Let's try to use it for the previous example.

`p1 = tf.placeholder(tf.float32)
p2 = tf.placeholder(tf.float32)`{{execute}}

We've just defined two placeholders expecting float values. The adding node can be built using both `add` method or `+` operator.

`add_ph = p1 + p2`{{execute}}

Evaluating the graph that is built with placeholders differs from the one constructed only with constants. For starters, it expects the placeholders values in the `feed_dict` parameter. It's a dictionary of placeholders names and corresponding values. You can then run the same graph with different settings.

`print(sess.run(add_ph, {p1: 2, p2: 5}))
print(sess.run(add_ph, {p1: 1.2, p2: 3.5}))
print(sess.run(add_ph, {p1: [1, 2], p2: [5, 8]}))`{{execute}}
