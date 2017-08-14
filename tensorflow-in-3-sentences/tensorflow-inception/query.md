Let's query the server now.

First we try the cat.

`bazel-bin/tensorflow_serving/example/inception_client --server=server:9000 --image=/cat.jpg`{{execute}}

You can see in the output that it has done pretty well recognising the breed. Obviously the network needs more training because no recognition of the grumpiness.

Wi the picture of the puppy dog we have similar situation:

`bazel-bin/tensorflow_serving/example/inception_client --server=server:9000 --image=/puppydog.jpg`{{execute}}

As a bonus we get the tennis ball as the classification label, although one would argue if this is the sport you would use this ball for.

For the doge the results are more conservative:

`bazel-bin/tensorflow_serving/example/inception_client --server=server:9000 --image=/doge.jpg`{{execute}}
