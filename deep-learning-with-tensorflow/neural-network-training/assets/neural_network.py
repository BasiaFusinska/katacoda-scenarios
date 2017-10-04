import helper as h
import numpy as np
from sklearn.metrics import accuracy_score

data = h.read_data()

X = data.as_matrix(['x1', 'x2'])
Y = data.as_matrix(['label'])

num_iteration = 10000
hidden_size = 5
learning_rate = 1.2

feature_size = X.shape[1]
W1, b1 = h.initialise_weights(feature_size, hidden_size)
W2, b2 = h.initialise_weights(hidden_size, 1)

for i in range(0, num_iteration):
    output, hidden = h.forward_propagation(X, W1, b1, W2, b2)
    cost = h.cost(output, Y)
    dW1, db1, dW2, db2 = h.backward_propagation(X, Y, W1, W2, output, hidden)
    W1, b1, W2, b2 = h.update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate)

    if i % 1000 == 0:
        print ("Cost after iteration %i: %f" %(i, cost))

accuracy = accuracy_score(Y, h.predict(X, W1, b1, W2, b2)) * 100
print 'Accuracy after the training: %d %%' % accuracy

h.plot_decision_boundary(lambda x: h.predict(x, W1, b1, W2, b2), X, Y)
