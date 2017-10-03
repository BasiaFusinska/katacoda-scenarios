import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path

def read_data(file_name='classification_data.csv'):
    df = pd.read_csv(file_name)
    return df

def visualise_data(X1, X2, labels, out_file):
    plt.scatter(X1, X2, c=labels, s=40, cmap=plt.cm.Spectral);
    plt.savefig(out_file)

def read_and_visualise_data(file_name='classification_data.csv', out_file='data.png'):
    df = read_data(file_name)
    if not os.path.isfile(out_file):
         visualise_data(df['x1'], df['x2'], df['label'], out_file)
    return df

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
