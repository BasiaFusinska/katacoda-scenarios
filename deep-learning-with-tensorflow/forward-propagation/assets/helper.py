import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path

def read_data(file_name):
    df = pd.read_csv(file_name)
    return df

def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s
