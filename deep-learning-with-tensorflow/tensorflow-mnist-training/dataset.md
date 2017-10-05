The goal of the current scenario, you're going to build a deeper neural network. This means you will add a hidden layer before the output one.

We've prepared the backbone of the code for you in the `neural_network.py`{{open}} file. The tasks have been pointed out.

## Task 1

The first task is to lead the MNIST dataset. You can use the `input_data.read_data_sets` function. Use a path of your choice and the `one_hot` encoding.

The images are of the 28 x 28 size. The hidden layer has 1024 neurons and there are 10 labels.

`image_size = 28
labels_size = 10
hidden_size = 1024`
