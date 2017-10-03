import helper as h
import numpy as np

data = h.read_data()
print data

def output_layer_fp(Input, W, b):
    # W shape: (1, input_size)
    # b shape: (1, 1)

    output = np.matmul(Input, W.T) + b
    return h.sigmoid(output)

def hidden_layer_fp(Input, W, b):
    # W shape: (hidden_size, feature_size)
    # b shape: (1, hidden_size)

    # Task 1: Perform sum(xi*wi) + b for every input value
    output = # TODO: use np.dot or np.matmul function
    return # TODO: Use the tanh function from the numpy package

# Task 2: Prepare the network parameters
X = data.as_matrix(['x1', 'x2'])
hidden_size = 10

W1 = # TODO: Create the (hidden_size, feature_size) array of weights
b1 = # TODO: Set the value of the bias

W2 = # TODO: Create the (1, hidden_size) array of weights
b2 = # TODO: Set the value of the bias

# Task 3: Build the network
def forward_propagation(X, W1, b1, W2, b2):
    return # TODO: Return the predictions

predictions = forward_propagation(X, W1, b1, W2, b2)
labels = np.zeros(len(predictions))
labels[predictions > 0.5] = 1

print labels
print data['label']
