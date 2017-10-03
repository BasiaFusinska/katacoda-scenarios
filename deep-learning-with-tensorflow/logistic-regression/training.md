The essential part of the machine learning process is training. In this task, you will create and train all of your models on the three training datasets.

Use the [LogisticRegressionCV](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html) class from the `sklearn` library to create the model. The training itself is accomplished by applying the `fit` function. It will need the data to be split to features and labels columns. Below you can see the example how to do it for the whole dataset.

`features = data[['x1', 'x2']]
labels = data['label']`
