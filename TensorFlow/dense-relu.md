Our first network isn't impressive regarding accuracy level. But because of the simplicity, it runs very fast. You could try out changing the learning rate or steps number in the `train_test_model` function to check if it influences the results.

For this part of the scenario, we will add another *dense layer* to our network and place it between the *input* and *output* ones. This type is called a *hidden layer* and can be visualised like this:

![Dense hidden layer](assets/images/Dense-hidden.png)

If you open the `DenseReLU.py`{{open}} file, you can see the minor changes when comparing with the previous architecture. First of all, there is another parameter `hidden_size` indicating the size (number of neurones) of the hidden layer. The definition itself takes the input data and connects to the output layer:

`hidden = tf.layers.dense(inputs=x_input, units=hidden_size, activation=tf.nn.relu)`

Notice that this time we used `activation` parameter. It is set to run whatever comes out of the neurone through the activation function which in this case is [ReLU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks). It has been proven to work quite well with deep architectures.

The rest of the code is unchanged and can be executed by using the following command:

`python DenseReLU.py`{{execute}}

You should notice a slight decrease in performance. Our network is becoming deeper which mean it's getting more parameters to be tuned and this makes the training process longer. On the other hand, this will make the accuracy more tuned.
