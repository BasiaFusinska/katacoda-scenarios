The matrix multiplication can result in any real value. This would make the label determination quite difficult. Fortunately, there is a way to transform the output into the value from the (0, 1) interval.

In the Deep Learning world, we use a [sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function) function for this case. Determining the label after applying this operation is simply checking if the value is bigger or smaller than some threshold (for our task we'll just use 0.5). If the result if smaller, this means the example is a class 0; 1 otherwise.

## Task 3

Wrap the matrix multiplication output with `sigmoid` function from the helper script. Use it to return the value of the `forward_propagation` function.
