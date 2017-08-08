The code for the scenario can be found in `estimators.py`{{open}}. The resulting network will have the architecture show in the image below. This means we will create one hidden layer with the [reLU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) activation function. As you will see further, the API offer high level model, so you are not actually building the layers by hand.

<img src="/basiafusinska/courses/tensorflow-getting-started/tensorflow-mnist-estimators/assets/hidden.png" alt="Hidden layer">

TensorFlow has the dataset already built in, so there is no need to manually download it.

`from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=False)`

Note that we used `one_hot` parameter with the value `False`. This means the labels will be read as integer values instead of one hot encoded vectors.
