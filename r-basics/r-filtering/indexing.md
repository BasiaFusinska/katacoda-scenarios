One of the ways of choosing the data is indexing. You can do it in two ways. One is to specify the position of the data, second is to provide a logical value.

If you know the numbers of the elements you can easily provide the list and filter by it. Let's say we want 1st, 4th and 7th element.

`indexes <- c(1, 4, 7)
a[indexes]`{{execute}}

To get the rest of the elements you can use `-` operator.

`a[-indexes]`{{execute}}

If you already have the logical values for the elements you want to include or exclude, you can use it to filer also. This is consistent with how applying logical conditions works.

`logical <- c(T, T, F, T, T, F, F, T, F, F)
a[logical]`{{execute}}

Analogically to get the excluded elements you can use `-` operator.

`a[-logical]`{{execute}}
