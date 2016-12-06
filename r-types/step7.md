Matrix is a structure similar to the table with the limitation it can only contain elements of the same type.

The simplest way to construct a matrix is to use `matrix` function:

`A <- matrix(c(1,2,3,4,5))
A`{{execute}}

This command will create one column matrix filled with values from 1 to 5. If you check the type of the matrix it will be simple numeric.

`typeof(A)`{{execute}}

If you want to create matrix with more than one column, you need to use `ncol` and/or `nrow` parameters:

`B <- matrix(c(1,2,3,4,5,6), ncol=3, nrow=2)
B`{{execute}}

If number of the elements doesn't fit ncol*nrow R will try to figure it out by either cutting of some elements or filling the missing values by using the collection from the beginning. This case you will get some warnings.

`C <- matrix(c(1,2,3,4,5,6,7), ncol=3, nrow=2)
C`{{execute}}

`D <- matrix(c(1,2,3,4), ncol=3, nrow=2)
D`{{execute}}

To access the elements of the matrix you can use `[,]`.

`B[1,2]`{{execute}}
