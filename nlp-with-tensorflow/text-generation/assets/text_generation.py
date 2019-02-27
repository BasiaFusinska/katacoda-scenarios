import tensorflow as tf
tf.enable_eager_execution()

import numpy as np
import os

import help

# Load data
file_name = 'shakespeare.txt'
dataset_uri = 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt'
sequence_len = 128
batch_size = 64

print("Loading the data...\n")

data_path = help.download_data(dataset_uri, file_name)
dataset, vocabulary, char2index, index2char, text = help.load_data(data_path, sequence_len)
dataset = dataset.shuffle(1000).batch(batch_size, drop_remainder=True)


for input_text, target in  dataset.take(1):
  print ('Input: ', repr(''.join(index2char[input_text.numpy()])))
  print ('Target:', repr(''.join(index2char[target.numpy()])))

# Build the model
vocabulary_size = len(vocabulary)
embedding_size = 128
lstm_units = 512

def build(vocabulary_size, embedding_size, batch_size, lstm_units):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Embedding(vocabulary_size, embedding_size, batch_input_shape=[batch_size, None]))
    model.add(tf.keras.layers.LSTM(lstm_units, recurrent_activation='sigmoid',
                                return_sequences=True, recurrent_initializer='glorot_uniform', stateful=True))
    model.add(tf.keras.layers.Dense(vocabulary_size))
    return model

model = build(vocabulary_size, embedding_size, batch_size, lstm_units)
model.summary()

# Train the model
model.compile(optimizer = tf.train.AdamOptimizer(), loss = tf.keras.losses.sparse_categorical_crossentropy)

print("Training the model...")
epochs_number = 1
epoch_steps = (len(text)//sequence_len)//batch_size

model.fit(dataset.repeat(), epochs=epochs_number, steps_per_epoch=epoch_steps)

# Text generation
def generate_text(model, start_text, generate_len = 1000):
    input_indexes = tf.expand_dims([char2index[s] for s in start_text], 0)
    generated_text = []
    
    model.reset_states()
    for idx in range(generate_len):
        predictions = tf.squeeze(model(input_indexes), 0)
        predicted_index = tf.multinomial(predictions, num_samples=1)[-1,0].numpy()
        input_indexes = tf.expand_dims([predicted_index], 0)
        generated_text.append(index2char[predicted_index])
    return '{0}{1}'.format(start_text, ''.join(generated_text))

print(generate_text(model, u"ROMEO: "))