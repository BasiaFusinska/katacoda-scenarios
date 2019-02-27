import tensorflow as tf
import numpy as np
import os
import pandas as pd

dataset_uri = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
dataset_name = "aclImdb"

def download_dataset(dataset_name, dataset_uri, extract=False, extract_ext="tar.gz"):
    fname = "{}.{}".format(dataset_name, extract_ext) if extract else dataset_name 
    return tf.keras.utils.get_file(
        fname=fname,
        origin=dataset_uri,
        extract=extract)

def load_reviews(directory):
    reviews = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        with tf.gfile.GFile(file_path, "r") as file:
            reviews.append(file.read())
    return reviews

def load_imdb_dataset(dataset_directory, is_train):
    subdir_name = "train" if is_train else "test"
    dir_name = os.path.join(dataset_directory, subdir_name)
    positive_reviews = pd.DataFrame({'review': load_reviews(os.path.join(dir_name, "pos"))})
    positive_reviews["sentiment"] = 1
    negative_reviews = pd.DataFrame({'review': load_reviews(os.path.join(dir_name, "neg"))})
    negative_reviews["sentiment"] = 0
    return pd.concat([positive_reviews, negative_reviews]).sample(frac=1).reset_index(drop=True)

def load_data(dataset_path, dataset_name):
    train_data = load_imdb_dataset(os.path.join(os.path.dirname(dataset_path), dataset_name), True)
    test_data = load_imdb_dataset(os.path.join(os.path.dirname(dataset_path), dataset_name), False)
    return train_data, test_data
