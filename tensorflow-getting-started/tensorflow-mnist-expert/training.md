As mentioned in the _MNIST for beginners_ tutorial, our deep learning process was defined by few steps:
* Reading training/testing dataset (MNIST)
* Defining the neural network architecture
* Defining the loss function and optimiser method
* Training the neural network based on data batches
* Evaluating the performance over the test data

Here we cumulated almost every step from this list and will be working strictly on the neural network architecture design part.

The whole process was defined in the `training.py`{{open}} file, and will be imported in the specific files including the code for different neural network architectures. The `dense.py`{{open}} includes the simple one output layer network, which is the same as presented in the beginners tutorial. Later in the scenario, we will create a more complex model.

You can run the network training by using the following command:

`python dense.py`{{execute}}
