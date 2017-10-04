Now we know what we're going to optimise. For the weights and biases adjustments, we will use the [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent) process. You can go into much more details using the provided links, but in short, the flow looks like this:

* Initialise the values you want to adjust
* Calculate the _gradients_
* _Update the values_ using gradients

The process will result in moving into the direction of the _optimal values_ for the loss function.

In the helper.py file you can see the `backward_propagation` and `update_parameters` functions implementing the process.
