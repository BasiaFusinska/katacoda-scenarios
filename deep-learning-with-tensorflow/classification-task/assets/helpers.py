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

def read_and_visualise_data(file_name='classification_data.csv', out_file='dataset.png'):
    df = read_data(file_name)
    if not os.path.isfile(out_file):
         visualise_data(df['x'], df['y'], df['label'], out_file)
    return df
