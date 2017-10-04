_Numpy_ package is one the most widely used library in the Python environment. It enables straightforwardly [vectorising](https://en.wikipedia.org/wiki/Array_programming) the operations.  In the world of Deep Learning and Neural Networks, this is a desirable quality.

Numpy's main object is a multidimensional array storing elements of the same type, usually numbers. The arrays (_umpy.array_) created using the library differ from the ones in Python standard library (_array.array_). Let us first run the Python command line and import the package.

`python`{{execute}}

`import numpy as np`{{execute}}

There are several ways on how to create the arrays. The easiest is to provide the set of value, by passing a regular Python list or tuple using the array function.

`np.array([2, 4, 15])
np.array([[1, 2], [3, 4], [5, 6]])`{{execute}}

The transformations change sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on. Notice that the following line will return with the error:

`np.array(2, 4, 15)`{{execute}}

To find out about the shape of the array use the following:

`a = np.array([[1, 2], [3, 4], [5, 6]])
a.shape`{{execute}}

To change it, use the reshape function:

`a.reshape(2, 3)`{{execute}}

You may find the functions zeros and ones useful to create arrays containing only 0s or 1s:

`np.zeros((3, 4))
np.ones((2, 3))`{{execute}}

For the randomly generated numbers apply:

`np.random.random((2,3))`{{execute}}
