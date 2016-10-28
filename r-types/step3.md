In R, the most primary structure is a vector. Even basic types are stored in this form. You can see it when trying to print any value:

`myVal <- "text"
myVal`{{execute}}

You can notice that before the displayed value there is `[1]` printed.

Vectors can only contain data of the same type. The easiest way to create a vector containing more elements, is to use `c` function (which stand for combine):

`myVector <- c('Anna', 'John', 'Eva')
myVector`{{execute}}

For sequential values you can use `:` operator:

`myVector <- 1:20
myVector`{{execute}}

`myVector <- letters[1:5]
myVector`{{execute}}

For initialisation of default values, just use type name. Default value for numeric types is 0, for string - '', for logical - 'F'. For example, the command:

`myVector <- numeric(10)
myVector`{{execute}}

creates 10-elements vector with all set to 0.
