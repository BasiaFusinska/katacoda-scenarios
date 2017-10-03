import helper as h
import sklearn
import sklearn.datasets
import sklearn.linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Task 1: Read and visualise the data
data = # TODO: use read_data or read_and_visualise_data from helper
print data

# Task 2: Split the data into train and test with 70:30 and 50:50 ratios
train70, test30 = # TODO: use train_test_split from sklearn.model_selection
train50, test50 =

# Task 3: Create and train three models
model70 = # TODO: use LogisticRegressionCV from sklearn.linear_model and fit the model
model50 =
model100 =

# Task 4: Predict the values using trained models
pred_train70 = # TODO: Use predict function
pred_test70 =
pred_train50 =
pred_test50 =
pred_train100 =

# Accuracy calculations
accuracy_train70 = accuracy_score(train70['label'], pred_train70) * 100
accuracy_test70 = accuracy_score(test30['label'], pred_test70) * 100
accuracy_train50 = accuracy_score(train50['label'], pred_train50) * 100
accuracy_test50 = accuracy_score(test50['label'], pred_test50) * 100
accuracy_train100 = accuracy_score(data['label'], pred_train100) * 100

print 'Train accuracy 70-30: %d %%' % accuracy_train70
print 'Test accuracy 70-30: %d %%' % accuracy_test70
print 'Train accuracy 50-50: %d %%' % accuracy_train50
print 'Test accuracy 50-50: %d %%' % accuracy_test50
print 'Train accuracy 100-0: %d %%' % accuracy_train100

# Plot decision boundary
h.plot_decision_boundary(lambda x: model70.predict(x), data[['x1', 'x2']].values, data['label'], out_file='decision_boundary70.png')
h.plot_decision_boundary(lambda x: model50.predict(x), data[['x1', 'x2']].values, data['label'], out_file='decision_boundary50.png')
h.plot_decision_boundary(lambda x: model100.predict(x), data[['x1', 'x2']].values, data['label'])
