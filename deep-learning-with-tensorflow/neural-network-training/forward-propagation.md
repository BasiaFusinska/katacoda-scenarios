If you open the `helper.py`{{open}} file, you will see several functions we've written for you. Along with the `read_data` and `sigmoid` functions, there are three dedicated to the forward propagation process:

* `initialise_weights` - used before the training process starts to set up the initial _weights_ and _biases_ values,
* `layer` - matrix multiplication and bias add
* `forward_propagation` - uses layer function and performs forward propagation and returns the intermediate results

We applied _tanh_ as the hidden layer activation function and _sigmoid_ for the output. Forward propagation will be performed in every step and the result values will be used to update the weights and biases.
