TensorFlow proved to be very successful with many AI tasks. One of the most popular in computer vision in the [ImageNet](http://www.image-net.org/) exercise. The exercise is to test the model against the database if the images and their proper labels.

[Inception in Tensorflow](https://github.com/tensorflow/models/tree/master/inception) is a project that showcases the training of the [Inception V3](http://arxiv.org/abs/1512.00567) architecture.

<img src="/basiafusinska/courses/tensorflow-in-3-sentences/tensorflow-inception/assets/inception_v3_architecture.png" alt="Inception V3 Architecture">

Once trained it can be used to classify new examples. To make things easier instead of building the model, packaging and maintaining it yourself, one can build the docker image. Katacoda offers the `katacoda/tensorflow_serving` so there is no need for us to create one for the examples.
