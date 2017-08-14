Let's query the server now.

`bazel-bin/tensorflow_serving/example/inception_client --server=server:9000 --image=/cat.jpg`{{execute}}
`bazel-bin/tensorflow_serving/example/inception_client --server=server:9000 --image=/puppydog.jpg`{{execute}}
`bazel-bin/tensorflow_serving/example/inception_client --server=server:9000 --image=/doge.jpg`{{execute}}
