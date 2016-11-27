We've seen that numbers are easily converted to char types.
The same is true when the original vector values are text:

`b <- letters[1:10]
b
typeof(b)`{{execute}}

If you set up one of the values as numeric, another conversion happens:

`b[5] <- 3
b
typeof(b)`{{execute}}

The 5th value of the vector was converted to char type, because there is no implicit conversion from text to integer.

There is an automatic conversion from boolean type to numeric though.

`c <- c(TRUE, FALSE, TRUE, TRUE, FALSE)
c`{{execute}}

Once you assign numeric value the type changes:

`c[3] <- 4
c
typeof(c)`{{execute}}

Implicit conversions can introduce several problems because they just happen automatically and don't notify the programmer.

One can easily imagine a situation when while reading data from a file they are treated like text/factor/integer instead of the desired type. Just because there is a typo in the file or a missing value.
