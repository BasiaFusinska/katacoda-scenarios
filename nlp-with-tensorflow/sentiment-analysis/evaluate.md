To see the result of the training we will use `evaluate` function, but first let use define the reusable function to be fed as the input function to `evaluate` and `predict` methods:

`def predict_input_fn(data, target):
    return tf.estimator.inputs.pandas_input_fn(data, data[target], shuffle=False)`{{execute}}

Let's see how the model performs for the training and testing data:

```
train_eval = sentiment_classifier.evaluate(input_fn=predict_input_fn(train_data, 'sentiment'))
test_eval = sentiment_classifier.evaluate(input_fn=predict_input_fn(test_data, 'sentiment'))

print("Training accuracy: {accuracy}".format(**train_eval))
print("Test accuracy: {accuracy}".format(**test_eval))
```{{execute}}

