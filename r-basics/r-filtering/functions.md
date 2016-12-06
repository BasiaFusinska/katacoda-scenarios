Logical conditions can become quite complex and it could be easier to create a function to deal with them.

`greaterThan <- function(x, than) { x > than }
evenNumber <- function(x) { x %% 2 == 0 }
ofLenght <- function(x, l) { nchar(x) == l }`{{execute}}

Once defined you can use those functions like you did for bare conditions.
The way it works is the function will be applied to every element of the vector or list.

Get elements greater than 4:
`a[greaterThan(a, 4)]`{{execute}}

Get only even numbers of the list:
`A[evenNumber(A)]`{{execute}}

Get only strings of the lenght 2:
`b[ofLenght(b, 2)]`{{execute}}
