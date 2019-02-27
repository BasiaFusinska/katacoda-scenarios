import tensorflow as tf
tf.enable_eager_execution()

import numpy as np
import os

def download_data(uri, file_name):
    return tf.keras.utils.get_file(file_name, uri)

def load_text(file_path):
    return open(file_path, 'rb').read().decode(encoding='utf-8')

def build_vocabulary(text):
    vocabulary = sorted(set(text))
    char2index = {char:idx for idx, char in enumerate(vocabulary)}
    index2char = np.array(vocabulary)
    return vocabulary, char2index, index2char

def generate_input(input_text):
    return input_text[:-1], input_text[1:]

def prepare_dataset(text, sequence_len):
    vocabulary, char2index, index2char = build_vocabulary(text)
    text_indexed = np.array([char2index[char] for char in text])
    dataset = tf.data.Dataset.from_tensor_slices(text_indexed).batch(sequence_len + 1, drop_remainder = True).map(generate_input)
    
    return dataset, vocabulary, char2index, index2char, text

def load_data(file_path, sequence_len):
    text = load_text(file_path)
    return prepare_dataset(text, sequence_len)