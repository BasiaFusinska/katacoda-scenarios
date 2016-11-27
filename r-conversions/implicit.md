There are two types of conversions in R: *implicit* and *explicit*.
Implicit conversions happens without specifically introducing them by the programmer and when the direct conversion from one type to the other exists.

Take a look at the following example.
Let's create a vector of integers ranging form 1 to 10:

`a <- 1:10
a`{{execute}}

As you may expect the type of the vector is integer:

`typeof(a)`{{execute}}

Now let us put a value of some other type there:

`a[5] <- 'some text'`{{execute}}

You can see that the type of the whole vector has changed as implicit conversion to string typed happened:

`a
typeof(a)`{{execute}}
