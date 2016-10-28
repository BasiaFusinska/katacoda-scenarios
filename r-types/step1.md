Like many other languages, R has a variety of basic types and more complex types that can be created from the 'atomic' ones. Basic types in R are:

* numeric (real)
* integer
* character
* logical
* complex

Creating a variable of a specific type can be done by using assign `<-` operator:

`num <- 10`{{execute}}

For initialising text variable you can use both ' and ":

`chr <- "some text"`{{execute}}

Logical values can be created using `TRUE`/`FALSE` or just `T`/`F`:

`log <- TRUE`{{execute}}

Notice that R is dynamic when it comes to types, so you can assign character value to the variable that previously was set to different type:

`myVar <- 10`{{execute}}

`myVar <- 'text value'`{{execute}}
