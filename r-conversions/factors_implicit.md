The resemblance of factors to text is very often confusing.
This 'confusion' is kind of introduced with the default R behavior.

Let us create a data frame. First column is a vector of numbers, second of char type:

`myData <- data.frame(c1 = c(1, 2, 3), c2 = c('A', 'B', 'C'))`{{execute}}

Or is it? When checking the types of the data frame columns we get the following:

`myData$c1[0]
myData$c2[0]`{{execute}}

First column is numeric as expected, but second was automatically converted to factor. This behavior is dictated by the fact that when working with data using text in the data container usually means working with categories and names rather than text as such. When reading data from the file you will notice the same behavior.

Of course there is a possibility to revert this and don't treat text as factors by using the global `options`:

`options(stringsAsFactors = FALSE)`{{execute}}

Now when you repeat the instructions, the type of the second column is character:

`myData <- data.frame(c1 = c(1, 2, 3), c2 = c('A', 'B', 'C'))
myData$c2[0]`{{execute}}
