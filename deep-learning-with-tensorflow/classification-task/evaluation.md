You can test how the model performs by producing the predictions and checking them with the underlying truths. With the more data though, it's much more practical to calculate some statistics.

The most obvious one is [accuracy](https://en.wikipedia.org/wiki/Accuracy_and_precision), which is the fraction of how many times the model was right. There are other metrics, but for the sake of simplicity, we'll use accuracy only. We're going to calculate it for both training and test set. Those observations can help you further with deciding about tuning your algorithm or resolving the [bias-variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff).

Let's first use the model to predict the values for both training and testing sets:

<pre class="file" data-filename="classification.py" data-target="append">
# Predict the values using trained model
predictions_train = clf.predict(train[['x', 'y']])
predictions_test = clf.predict(test[['x', 'y']])

</pre>

Next we'll calculate the accuracy of the model:
<pre class="file" data-filename="classification.py" data-target="append">
# Accuracy calculations
accuracy_train = accuracy_score(train['label'], predictions_train)
accuracy_test = accuracy_score(test['label'], predictions_test)

print 'Train accuracy: %d' % accuracy_train
print 'Test accuracy: %d' % accuracy_test

</pre>

Run the script using the following command:
`python classification.py`{{execute}}

It looks like our algorithms performed quite well. But to be fair, we were running it on the very simple dataset. Next scenario will show you a couple of shortcomings if you are using lees nicely shaped data.
