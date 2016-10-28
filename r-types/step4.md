Lists are special kind of vectors that allow to store elements of different types, including vectors, lists and more complex elements. And this is basically the main reason why they are used in R.

You can create list using `list` function. The following instruction creates 3-elements list:

`myList <- list(5, 'abc', c(1, 2, 3))
myList`{{execute}}

You may have noticed that printing a list shows that every element is indexed by double square brackets. Every element of a list is a vector. We will talk about indexing later.

As you may expect, the type of a list is list:

`typeof(myList)`{{execute}}
