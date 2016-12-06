What if conversion doesn't exist? R offers a `NA` value for the situation like this.

`as.numeric('abc')
as.logical('right')`{{execute}}

Notice that conversions are not nested. For example there is a conversion from string `'TRUE'` to logical value `TRUE`. The same is for the conversion from boolean `TRUE` to the numeric `1`, but you cannot expect it to happen automatically. Those are after all explicit conversions:

`as.numeric('TRUE')`{{execute}}

`NA` value can be used like any other value with the exception that it fits into any type:

`characters <- c('abc', NA, 'def', 'ghi')
characters
numbers <- c(1, 2, NA, 4, 5)
numbers
logics <- c(TRUE, FALSE, NA, TRUE)
logics`{{execute}}
