We want you to perform three separate machine learning trainings. The reason is for you to see how does the accuracy changes when you use different data splits:
** 70%-30%
** 50%-50%
** 100%-0%

Notice that the third ration means that we are not producing any test data, so we'll only check the algorithm performance based on the training data. You can use [train_test_split](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) from the `sklearn.model_selection` package.
