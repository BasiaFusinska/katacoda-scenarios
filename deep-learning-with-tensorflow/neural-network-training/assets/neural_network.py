import helper as h
import numpy as np

data = h.read_data()
print data

X = data.as_matrix(['x1', 'x2'])
Y = data.as_matrix(['label'])

num_iteration = 10
hidden_size = 5
learning_rate = 0.1

feature_size = X.shape[1]
W1, b1 = initialise_weights(feature_size, hidden_size)
W2, b2 = initialise_weights(hidden_size, 1)

for i in range(0, num_iteration):
    output, zo, hidden, zh = h.forward_propagation(X, W1, b1, W2, b2)
    cost = h.cost(output, Y)
    dW1, db1, dW2, db2 = backward_propagation(X, Y, W1, W2, output, hidden)
    W1, b1, W2, b2 = update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate)

    if i % 2 == 0:
        print ("Cost after iteration %i: %f" %(i, cost))
