import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path

def read_data(file_name='dataset.csv'):
    df = pd.read_csv(file_name)
    return df

def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s

def initialise_weights(in_size, out_size):
    W = np.random.randn(out_size, in_size) * 0.01
    b = np.zeros((1, out_size))
    return W, b

def layer(Input, W, b):
    output = np.matmul(Input, W.T) + b
    return output

def forward_propagation(X, W1, b1, W2, b2):
    hidden = np.tanh(layer(X, W1, b1))
    output = sigmoid(layer(hidden, W2, b2))

    return output, hidden

def cost(output, Y):
    m = Y.shape[1]
    return -(np.sum(np.multiply(np.log(output),Y)) + np.sum(np.multiply(np.log(1 - output), 1 - Y)))/m

def backward_propagation(X, Y, W1, W2, output, hidden):
    m = Y.shape[0]

    dZ2 = output - Y
    dW2 = np.dot(dZ2.T, hidden)/m
    db2 = np.sum(dZ2, axis=0, keepdims=True)/m
    dZ1 = np.dot(dZ2, W2)*(1 - np.power(hidden, 2))
    dW1 = np.dot(dZ1.T, X)/m
    db1 = np.sum(dZ1, axis=0, keepdims=True)/m

    return dW1, db1, dW2, db2

def update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate):
    W1 -= learning_rate*dW1
    b1 -= learning_rate*db1
    W2 -= learning_rate*dW2
    b2 -= learning_rate*db2

    return W1, b1, W2, b2

def predict(X, W1, b1, W2, b2):
    output, _ = forward_propagation(X, W1, b1, W2, b2)
    labels = np.zeros(output.shape)
    labels[output > 0.5] = 1
    return labels

def plot_decision_boundary(model, X, labels, out_file='decision_boundary.png'):
    # Set min and max values and add a little padding
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.ylabel('x2')
    plt.xlabel('x1')
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap=plt.cm.Spectral)
    plt.savefig(out_file)
