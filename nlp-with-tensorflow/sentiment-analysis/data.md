Let's first download and load the data.

The data will be stored in the `train_data` and `test_data` variables.

`dataset_path = download_dataset(dataset_name, dataset_uri, True)
train_data, test_data = load_data()`{{execute}}

You can have a look a the headers by running:

`train_data.head()`{{execute}}

And:

`test_data.head()`{{execute}}

The classificator will be trained to fit the `sentiment` feature.