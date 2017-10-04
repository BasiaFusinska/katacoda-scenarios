Once we decided the network is trained, we should try to evaluate the results. One thing we can do is to use the sklearn accuracy_score function to calculate accuracy:

`accuracy = accuracy_score(Y, h.predict(X, W1, b1, W2, b2)) * 100
print 'Accuracy after the training: %d %%' % accuracy`

The last line is creating a decision boundary image, so you can see how does the network perform.

You can run the whole script using the following command:

`python neural_network.py`{{execute}}
