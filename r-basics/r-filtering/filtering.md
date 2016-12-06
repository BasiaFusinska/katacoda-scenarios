Instead of `[]` parenthesis, one could use dedicated functions: `Filter` or `subset`. They may not seem much at the moment but they bring value once working with data frames instead of simple vectors and lists.

`Filter` function takes 2 parameters - condition function and data container. Condition function needs to take 1 argument, which will be mapped for every element of the vector or list.

`Filter(evenNumber, a)`{{execute}}

To use `greaterThan` function (that takes also `than` as an argument) to limit result to only elements greater than 4 one could use inline function syntax:

`Filter(function(x) { greaterThan(x, 4) }, a)`{{execute}}

Another useful function is `subset`. For vectors and lists it works very similarly to the `[]` filtering.

Using a bare condition:

`subset(a, a > 4)`{{execute}}

Using functions in `subset`:

`subset(A, greaterThan(A, 4))`{{execute}}
`subset(b, ofLenght(b, 2))`{{execute}}
