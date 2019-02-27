Once the network is set up it has to be trained. To do this you have to define the input function:

`input_fn = tf.estimator.inputs.pandas_input_fn(train_data, train_data['sentiment'], num_epochs=None, shuffle=True)`{{execute}}

Now we will use it to train the model for 1000 steps:

`sentiment_classifier.train(input_fn=input_fn, steps=1000)`{{execute}}

