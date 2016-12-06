Explicit conversions work also for complex types like lists, matrixes or data frames.

Suppose you have a vector and what you need is a list.
You can still use `as.list` function:

`v <- 1:5
v
l <- as.list(v)
l`{{execute}}

You can do similar things with matrixes and data frames, but using vectors for this is not really that interesting:

`as.matrix(v)
as.data.frame(v)
as.data.frame(l)`{{execute}}

Notice that for the data frame conversion creates the *column* for the vector and *row* for the list.

Conversions between matrixes and data frames are much more compelling.
As you may remember matrixes are 2 dimensional structures containing values of the same type, while data frames have the type constraint only in the column spectrum.

Using matrix to create a data frame can be achieved by conversion function `as.data.frame` or just creation `data.frame`:

`A <- matrix(1:15, ncol=3, nrow=5)
A
as.data.frame(A)
data.frame(A)`{{execute}}

The reverse conversion is very often only available using explicit function `as.matrix`:

`df <- data.frame(c1 = 1:5, c2 = 6:10, c3 = 11:15)
df
as.matrix(df)`{{execute}}

Notice that in a situation when the columns in a data frame have different types there will be used implicit conversion:

`df <- data.frame(c1 = 1:5, c2 = letters[6:10], c3 = 11:15)
df
as.matrix(df)`{{execute}}
