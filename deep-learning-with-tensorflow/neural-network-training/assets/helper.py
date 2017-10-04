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
    b = np.zeros((out_size, 1))
    return W, b

def layer(Input, W, b):
    output = np.matmul(Input, W.T) + b
    return output

def forward_propagation(X, W1, b1, W2, b2):
    zh = layer(X, W1, b1)
    hidden = np.tanh(zh)
    zo = layer(hidden, W2, b2)
    output = sigmoid(zo)

    return output, zo, hidden, zh

def cost(output, Y):
    m = Y.shape[1]
    return -1/m *(np.sum(np.multiply(np.log(output),Y)) + np.sum(np.multiply(np.log(1 - output), 1 - Y)))

def backward_propagation(X, Y, W1, W2, output, hidden):
    dZ2 = output - Y
    dW2 = 1/m * np.dot(dZ2, hidden.T)
    db2 = 1/m * np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = np.dot(W2.T, dZ2)*(1 - np.power(hidden, 2))
    dW1 = 1/m * np.dot(dZ1, X.T)
    db = 1/m * np.sum(dZ1, axis=1, keepdims=True)

    return dW1, db1, dW2, db2

def update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate):
    W1 -= learning_rate*dW1
    b1 -= learning_rate*db1
    W2 -= learning_rate*dW2
    b2 -= learning_rate*db2

    return W1, b1, W2, b2
