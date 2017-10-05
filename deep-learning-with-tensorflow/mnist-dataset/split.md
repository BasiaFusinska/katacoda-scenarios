The dataset is split into three parts, that should be use in the different phases of the machine learning process:

* training (55,000 records) - `mnist.train`,
* test (10,000 record) - `mnist.test`,
* validation (5,000 records) - `mnist.validation`.

Every set is split into two parts: the images and corresponding labels. You can access them by using .images and .labels fields:

`mnist.train.images[7]
mnist.train.labels[0:5]`{{execute}}

Each image an 28 x 28 pixels array:

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/mnist-dataset/assets/MNIST-Matrix.png" alt="MNIST Dataset">

Let's have a look at the data shapes:

`mnist.train.images.shape
mnist.train.labels.shape
mnist.test.images.shape
mnist.test.labels.shape
mnist.validation.images.shape
mnist.validation.labels.shape
`{{execute}}
