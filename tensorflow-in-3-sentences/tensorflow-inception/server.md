In this step we will start the server that already contains the Tensorflow Inception trained model. The server can be later queried against new examples. To run the server use the command below. It will run the image and run the process to serve the inception model inside.

`docker run -d --name server -p 9000:9000 katacoda/tensorflow_serving bash -c "/serving/bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server --port=9000 --model_name=inception --model_base_path=/serving/inception-export"`{{execute}}

If you try it locally it will download the docker image first and then run the command.
