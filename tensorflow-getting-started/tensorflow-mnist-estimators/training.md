For the convenience we defined a function to provide the data values and corresponding labels from the provided dataset. It will be further used during the training and evaluating phases.

`def input_fn(dataset):
    features = dataset.images
    labels = dataset.labels.astype(np.int32)
    return features, labels`

Classifier created in the previous step can now be used to fit the values of the weights in the neural network. The high level API provides us with the general function `fit` that will take data, labels, batch size and training steps number.

`features, labels = input_fn(mnist.train)
classifier.fit(x=features, y=labels, batch_size=100, steps=1000)`

Depending on the complexity of the model, training will take some time. After it's finished you can use the model to check the accuracy against the test set. To do this we can use `evaluate` function.

`features, labels = input_fn(mnist.test)
test_accuracy = classifier.evaluate(x=features, y=labels, steps=1)["accuracy"]
print("\nTest accuracy: %g %%"%(test_accuracy*100))`
