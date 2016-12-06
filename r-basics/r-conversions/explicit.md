So far we covered implicit automatic conversions that happen often without the knowledge of the programmer. Of course R offers a way to convert types intentionally.

First thing you might want to do when using explicit conversion is to check if the variable is of a desired type. You can use `is.<type>` functions for this. For example:

`is.character('abc')
is.numeric(TRUE)`{{execute}}

Once you know that the conversions exists you can use `as.<type>` to make it happen.

As you probably imagine conversions to text usually succeed:

`as.character(5)
as.character(factor('a'))
as.character(FALSE)`{{execute}}

With logical and numeric types it depends on the actual values. For booleans you can always retrieve a value from the numeric variable. Everything except `0` becomes `TRUE`:

`as.logical(0)
as.logical(5)`{{execute}}

When working with strings you need to use stringified names of logical values (`'TRUE'`, `'True'`, `'true'`, `'FALSE'`, `'False'`, `'false'`):

`as.logical('TRUE')
as.logical('FALSE')`{{execute}}

For numbers there is always the conversion from logical type:

`as.numeric(TRUE)
as.numeric(FALSE)`{{execute}}

But the same is not true for strings. Converted test value needs to be in a proper form:

`as.numeric('57')
as.numeric('2.3')`{{execute}}
