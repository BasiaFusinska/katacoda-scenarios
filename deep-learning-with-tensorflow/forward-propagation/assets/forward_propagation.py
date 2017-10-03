import helper as h
import numpy as np

# Task 1: Read data
linear_data = # TODO: Use read_data with 'linear.csv' file
non_linear_data = # TODO: Use read_data with 'non_linear.csv' file

print linear_data
print non_linear_data

def forward_propagation(X, W, b):
    # X shape: (data_size, feature_size)
    # W shape: (1, feature_size)
    # b shape: (1, 1)

    # Task 2: Perform sum(xi*wi) + b for every input example
    output = # TODO: use np.dot or np.matmul function

    # Task 3: Determin the output value
    return # TODO: use sigmoid function from the helper script

# Task 4: Prepare the function parameters
X_linear = # TODO: get only the features from the data
X_non_linear =

W = # TODO: Create the (1, feature_size) array of weights
b = # TODO: Set the value of the bias

# Task 5: Use forward_propagation for both datasets
fp_linear = # TODO: Use the function with the X_linear
fp_non_linear = # TODO: Use the function with the X_non_linear

linear_labels = (fp_linear > 0.5)
non_labels = (fp_non_linear > 0.5)

print linear_labels[:10]
print non_labels[:10]
