When working with the vector data there is a simple way to use logical condition to filter it.

Let us create a vector of sequential numbers:

`a <- 1:10
a`{{execute}}

To get only values larger than 4 `[]` should be used for the condition:

`a[a > 4]`{{execute}}

The same rule could be applied to the char vector and the condition of strings of the length 2.

`b <- c("ab", "bc", "abc", "ac", "def")
b
b[nchar(b) == 2]`{{execute}}

Conditions and parenthesis can be used for lists too. Just remember that because list can store elements of different types, the condition needs to make sense for all of them.

`A <- as.list(1:10)
A
A[A > 4]`{{execute}}
