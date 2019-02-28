Let's first download and load the data. Let us define the source:

`dataset_uri = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
dataset_name = "aclImdb"`{{execute}}

The data will be stored in the `train_data` and `test_data` variables.

`dataset_path = help.download_dataset(dataset_name, dataset_uri, True)
train_data, test_data = help.load_data(dataset_path, dataset_name)`{{execute}}

You can have a look a the headers by running:

`train_data.head()`{{execute}}

And:

`test_data.head()`{{execute}}

The classificator will be trained to fit the `sentiment` feature.