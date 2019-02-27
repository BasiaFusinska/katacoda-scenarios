We will be using Keras to build the network architecture. The main processing type of layer would be [LSTM](https://www.tensorflow.org/versions/r1.12/api_docs/python/tf/keras/layers/LSTM). But first we need to define some variables.

`vocabulary_size = len(vocabulary)
embedding_size = 128
lstm_units = 512`{{execute}}

Then we can define the model:

```
def build(vocabulary_size, embedding_size, batch_size, lstm_units):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Embedding(vocabulary_size, embedding_size, batch_input_shape=[batch_size, None]))
    model.add(tf.keras.layers.LSTM(lstm_units, recurrent_activation='sigmoid',
                                return_sequences=True, recurrent_initializer='glorot_uniform', stateful=True))
    model.add(tf.keras.layers.Dense(vocabulary_size))
    return model

```{{execute}}

Let's build the model:

`model = build(vocabulary_size, embedding_size, batch_size, lstm_units)`{{execute}}

And have a look at the structure:

`model.summary()`{{execute}}
