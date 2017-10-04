Numpy arrays can be indexed and iterated like other Python sequences. Indexing starts with 0.

`a = np.array([2, 3, 5, 20, 2, 1, 4, 6, 1, 8, 10, 3])
a[2:4]`{{execute}}

For multidimensional arrays, you can use indices per axis.

`b = a.reshape(4, 3)
b
b[3, 1] # Element in the 4th row and 2nd column
b[:, 2] # 3-rd column
b[1, :] # 2nd row`{{execute}}

For short you can use minus values when accessing an element from the end.

`a[-1]
b[-2, :]
b[:, -1]`{{execute}}
