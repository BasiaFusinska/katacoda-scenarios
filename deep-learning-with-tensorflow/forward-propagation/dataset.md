We will be classifying the data used in the previous scenarios when we applied Logistic Regression to the task. We will focus here only on the _prediction_ phase, but you'll have the chance to implement the training in the later part of the course.

Below you can see the visualisation of the datasets, both _linearly separated and not_.

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/forward-propagation/assets/linear.png" alt="Linear dataset">

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/forward-propagation/assets/non_linear.png" alt="Non-linear dataset">

##Task 1

You're going to get the data from the files. The code will be written in the `forward_propagation.py`{{open}}. There are several help functions in the helper.py script. To load data use `read_data` function pointing to both data files: `linear.csv` and `non_linear.csv`.
