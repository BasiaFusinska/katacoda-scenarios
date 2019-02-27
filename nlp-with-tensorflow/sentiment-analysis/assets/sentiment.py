import tensorflow as tf
import numpy as np
import os
import pandas as pd

import help

# Load data
dataset_path = download_dataset(dataset_name, dataset_uri, True)
train_data, test_data = load_data()

print(train_data.head())

# Define the embedding column
text_column = tf_hub.text_embedding_column("review", "https://tfhub.dev/google/nnlm-en-dim128/1")

# Define the classifier
sentiment_classifier = tf.estimator.DNNClassifier(
    hidden_units=[512, 128],
    feature_columns=[text_column],
    n_classes=2,
    optimizer=tf.train.AdagradOptimizer(learning_rate=0.003))

# Train the model
input_fn = tf.estimator.inputs.pandas_input_fn(
    train_data, train_data['sentiment'], num_epochs=None, shuffle=True)

sentiment_classifier.train(input_fn=input_fn, steps=1000)

# Evaluate the model
def predict_input_fn(data, target):
    return tf.estimator.inputs.pandas_input_fn(data, data[target], shuffle=False)

train_eval = sentiment_classifier.evaluate(input_fn=predict_input_fn(train_data, 'sentiment'))
test_eval = sentiment_classifier.evaluate(input_fn=predict_input_fn(test_data, 'sentiment'))

print("Training set accuracy: {}".format(**train_eval))
print("Test set accuracy: {}".format(**test_eval))

# Predict new reviews sentiment
def predict_sentiment(reviews):
        predict_input_fn = tf.estimator.inputs.pandas_input_fn(pd.DataFrame({'review': reviews}), shuffle=False)
        predictions = sentiment_classifier.predict(input_fn=predict_input_fn)
        for index, prediction in enumerate(predictions):
            print("Review: {} --> Sentiment: {}".format(new_reviews[index],
                                             "Negative" if prediction["classes"][0] == b'0' else "Positive"))

new_reviews = ["This was an awful movie", "I think it was great"]
predict_sentiment(new_reviews)
