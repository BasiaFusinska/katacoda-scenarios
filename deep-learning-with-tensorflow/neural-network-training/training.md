Now it's time for us to perform the training. This will happen using the Gradient Descent algorithm one step at the time. The code is available in the `neural_network.py`{{open}} file.

The first thing we need to do is to load the data and set up some process _hyperparameters_: number f iterations, the size of the hidden layer, learning rate.
`num_iteration = 10000
hidden_size = 5
learning_rate = 1.2`

Then we will initialise the weights and use them in the iterative process. In every step of the process, we do the following tasks (inside the loop: `for i in range(0, num_iteration):`):
* forward propagation
* loss function calculation
* gradients calculations (backward propagation)
* updating the weights and biases

Every 1000 steps the current loss function value is printed.
