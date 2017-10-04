Numpy offers a lot of functionalities for the linear algebra computations. You can easily transpose the matrix, create an identic matrix, multiply them or calculate the trace.

Transposing is as easy as:

`a = np.array([[1, 2, 3], [0, 1, 3]])
a
a.T
a.transpose()`{{execute}}

Use eye function to create the identic matrix:

`np.eye(3)`{{execute}}

To multiply matrices use `dot` or `matmul` functions. Remember that this operation takes into consideration the dimensions. If the matrix `b` is 2 x 2, we can see the `b x a` product:

`b = np.array([[2, 1], [3, 2]])
np.dot(b, a)`{{execute}}

While the `a x b` will throw the error:

`np.dot(a, b)`{{execute}}
