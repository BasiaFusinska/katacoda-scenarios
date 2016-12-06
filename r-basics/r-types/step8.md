Data frames are structures used the most frequently in R world. They are structured in a way tables are in relational databases.

This means they have columns and rows, but columns can differ on the containing type. Of course all the values of the same column must be of the same type.

The simplest way to create a data frame is to just list columns:

`dataFrame <- data.frame(col1=c(1,2,3), col2=c('a','b','c'))
dataFrame`{{execute}}

If you try to find out the type of the created data frame it will be a list:

`typeof(dataFrame)`{{execute}}

Similarly to lists we get an easy way to access the columns, using `$` symbol.

`dataFrame$col2`{{execute}}
