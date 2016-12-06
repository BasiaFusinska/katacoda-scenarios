There are several ways to find out the type of the data. The easiest is to use `typeof(x)` function. It returns type or storage mode of any object in R.

`x <- 5
typeof(x)`{{execute}}

You can also use index 0 of the variable (more on indexes later):

`x[0]`{{execute}}

You can use `class(x)` function, although this one has deeper meaning when it comes to objects in R:

`class(x)`{{execute}}

Notice that sometimes names of the types or even types differ when using different ways of retrieving them. Try to check those types.
