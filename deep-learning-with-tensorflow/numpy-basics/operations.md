Arithmetic operations in the numpy library operate elementwise. They create a new table and fill it with the result values. Let's try it with a scalar:

`a = np.array([1., 2., 3., 4., 5.])
a + 1
a - 3
a / 2
a * 5
a**2`{{execute}}

This will also work with many built-in operations:

`np.sin(a)
np.exp(a)`{{execute}}

You can also use arrays to create the condition index:

`a > 3
a % 2 == 0`{{execute}}

Some operations are working in place, without creating a new array:

`a += 10
a /= 2
a`{{execute}}
