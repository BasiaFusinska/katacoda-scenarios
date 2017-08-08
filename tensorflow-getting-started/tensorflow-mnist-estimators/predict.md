The trained model can also be used to make prediction on the new data. Let's get the first 10 samples from the validation dataset and use the classifier on them.

`features = mnist.validation.images[:10]
labels = mnist.validation.labels[:10].astype(np.int32)
predictions = list(classifier.predict(x=features))`

Now we can and check the predictions against the real .values

`print("\nPredicted labels from validation set: %s"%predictions)
print("Underlying values: %s"%list(labels))`

You can run the whole process using the following command:

`python estimators.py`{{execute}}
