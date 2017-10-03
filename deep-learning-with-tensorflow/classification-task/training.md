The training of the model is the essential part of the machine learning process. This where all the fun and magic is happening. While going through the data, the algorithm is adjusting the coefficients to fit them the best.

In case of Linear Regression that we'll use it means it will take some _loss function_ into account and will try to _minimise_ it. Don't worry; we won't be writing it ourselves here. Instead, we're going to use the black-boxed class from the `sklearn` library.

<pre class="file" data-filename="classification.py" data-target="append">
# Create and train the model
model = sklearn.linear_model.LogisticRegressionCV();
model.fit(train[['x1', 'x2']], train['label']);
</pre>

Once the algorithm is done, we get the ready to use, _trained model_. Later it can be applied to predict new examples' colours.
