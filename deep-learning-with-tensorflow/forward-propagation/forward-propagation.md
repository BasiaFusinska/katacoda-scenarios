It's time to use the `forward_propagation` function. This will require getting the feature data from both datasets and setting the values for the weights and bias vectors.

##Task 4
The first thing you need to do is to filter the input data from the datasets (`linear_data` and `non_linear_data`). This means we do not include the label column. The following code is showing how to get the (x1,x2) columns and transform them into the np array.

`data_array = data.as_matrix(['x1', 'x2'])`

For the weights and biases use any values you want, just make sure the vectors have _proper shapes_.

## Task 5
Finally, you can use the `forward_propagation` function with specific parameters. The last lines of the code are displaying few predictions for both datasets.

Keep in mind that these predictions are not necessary tuned. We didn't put _any training_ in place. We will do it in one of the next scenarios.
