First, we need some values to be provided. We have 10 classes for our dataset, image size is 28 and the hidden layer size is set to 1024:

`image_size = 28
labels_size = 10
hidden_size = 1024`

To create the estimator we need the set of feature columns. TensorFlow offers the `tf.contrib.layers.real_valued_column` to build it. As our images are flattened we will use the `image_size*image_size` as dimension.

`feature_columns = [tf.contrib.layers.real_valued_column("", dimension=image_size*image_size)]`

Next step is to initiate the model itself. As mentioned before we use `DNNClassifier` as it uses deep neural network underneath. There is only one hidden layer, so the `hidden_units` parameter (which is a list of sizes) contains only one number. As an optimiser there will be used `AdamOptimizer`.

`classifier = tf.contrib.learn.DNNClassifier(
        feature_columns=feature_columns,
        hidden_units=[hidden_size],
        n_classes=labels_size,
        optimizer=tf.train.AdamOptimizer())`

Having this model we are ready to perform training.
