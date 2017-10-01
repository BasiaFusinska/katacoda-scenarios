Before we start the training phase, we are going to prepare the data. Usually, data we get from the real world are by no means clean or ready to use. They demand a lot of transformations, cleaning and very often feature engineering.

Our example is prepared especially for the scenario purposes, so the only thing we need to do is to split the data into the training and testing sets. The reason to do it is to check later how does the model perform on the data it didn't see in the training phase. Checking only the training data accuracy could be misleading, as the algorithms could have just memorised the records ([overfitting](https://en.wikipedia.org/wiki/Overfitting)) instead of generalising the rule.

Depending on the dataset we could think of different train-test split ratios. In our example, we'll just try 30%-70%.
