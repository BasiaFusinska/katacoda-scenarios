Both vectors and lists are indexed starting from 1 (0 index is reserved for storing the type). To access specific elements you can use bot `[]` and `[[]]` brackets.

The rule is that single brackets are to access the specific elements and double are to access a value. Vectors elements are vectors themselves, so you can use any type of brackets to get an element:

`x <- 1:10
x[4]
x[[4]]`{{execute}}

For lists, elements are lists, so usage of specific brackets makes a difference:

`l <- as.list(1:10)
l[4]
l[[4]]`{{execute}}

When using named elements there are more possibilities to explore. Basically you can use a name achieved from an external function and the use it when accessing specific elements.

`elemName <- 'b'`{{execute}}

For vectors accessing the value could be achieved in the following name:

`y <- c(a='a', b='b', c='c')
y[elemName]
y[[elemName]]`{{execute}}

And for lists:

`m <- list(a='a', b='b', c='c')
m[elemName]
m[[elemName]]`{{execute}}

With lists we also get easy way to get to the named elements. Using `$` symbol. Notice that this time you cannot use calculated `elemName` value

`m$b`{{execute}}
