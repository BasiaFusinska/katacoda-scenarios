We will use now those two representations (vector count and tf-idf) to train two separate models. As the machine learning algorithm we will use multinomial Naive Bayes which is offered in *sklearn* by class *MultinomialNB*. Once we fit to the training data (which were created by transforming *train_documents*), the model can be used to make future predictions.

```
from sklearn.naive_bayes import MultinomialNB

one_hot_model = MultinomialNB().fit(one_hot, train_labels)
tfidf_model = MultinomialNB().fit(tfidf, train_labels)
```{{execute}}

Let's check how both models perform on the training and test datasets. As we already have the vectorised presentations for the training set, we need to do the same for the test documents. This time we will use *transform* method for both vectorizers ans we no longer need to fit them.

Then we use underlying truth (*train_labels* and *test_labels*) to score both models.

```
test_one_hot = vectorizer.transform(test_documents)
test_tfidf = vectorizer_tfidf.transform(test_documents)

print("One hot train score: ", one_hot_model.score(one_hot, train_labels))
print("One hot test score: ", one_hot_model.score(test_one_hot, test_labels))
print("Tfidf train score: ", one_hot_model.score(tfidf, train_labels))
print("Tfidf test score: ", one_hot_model.score(test_tfidf, test_labels))
```{{execute}}

The results are not amazing but sufficient enough regarding we only did basic feature engineering and didn't really tune the algorithms. The model show good generalization, but to trully evaluate them other matrics should be used to account for classes imbalance.
