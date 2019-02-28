Let's first download and load the data. First we need to define some useful scalars:

`file_name = 'shakespeare.txt'
dataset_uri = 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt'
sequence_len = 128
batch_size = 64`{{execute}}

The data will be stored in the `dataset`, `vocabulary`, `char2index`, `index2char`, `text` variables.

`data_path = help.download_data(dataset_uri, file_name)
dataset, vocabulary, char2index, index2char, text = help.load_data(data_path, sequence_len)`{{execute}}

You can have a look a the text by running:

`for input_text, target in  dataset.take(1):
  print ('Input: ', repr(''.join(index2char[input_text.numpy()])))
  print ('Target:', repr(''.join(index2char[target.numpy()])))`{{execute}}

Before we use the data for the training we want to shuffle it:

`dataset = dataset.shuffle(1000).batch(batch_size, drop_remainder=True)`{{execute}}

