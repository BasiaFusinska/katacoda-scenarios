Filtering data becomes much more interesting when working with complex types, especially data frames.

Let us create an example data frame. You can imagine it contains poll data gathering information of age, gender and if the person is a smoker.

`population <- data.frame(
  age=c(20, 15, 31, 45, 17, 27, 35, 41, 52, 23),
  gender=factor(c('F', 'F', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'M')),
  smoker=c(T, T, F, T, F, F, T, F, T, T))
population`{{execute}}

Every column is accessible using `$` symbol.

`population$age
population$gender
population$smoker`{{execute}}

To filter data by column information we can use `[]` similarly to how we did this for simple types. There is a tweak though, column information needs to come after the `,`.

Instead of `$` symbol you can choose to select the column by the number.

`population[, 2]
population[, 3]`{{execute}}

Or a list of numbers.

`population[, c(2, 3)]`{{execute}}

You can even change the order of columns this way.

`population[, c(1, 3, 2)]`{{execute}}

If you don't know the order of columns you can use names.

`population[, c('age', 'smoker')]`{{execute}}
