Once you're confident about the model performance you can use it for predictions. Let us define a function that will get new reviews and print the prediction results:

`def predict_sentiment(reviews):
        predict_input_fn = tf.estimator.inputs.pandas_input_fn(pd.DataFrame({'review': reviews}), shuffle=False)
        predictions = sentiment_classifier.predict(input_fn=predict_input_fn)
        for index, prediction in enumerate(predictions):
            print("Review: {} --> Sentiment: {}".format(new_reviews[index], "Negative" if prediction["classes"][0] == b'0' else "Positive"))`{{execute}}

We can define some new reviews:
`new_reviews = ["This was an awful movie", "I think it was great"]`{{execute}}

And then check about the train model predictions:

`predict_sentiment(new_reviews)`{{execute}}

