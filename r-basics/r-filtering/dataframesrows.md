When working with data frames filtering is usually applied to the samples. R platform is providing several interesting techniques.

First, if you treat columns of the data frames as vectors, you can easily filter them.

Get ages of the males in the population:

`population$age[population$gender == 'M']`{{execute}}

Get information about smoking for people over 30:

`population$smoker[population$age > 30]`{{execute}}

You can also put together both conditions:

`population$smoker[population$gender == 'M' & population$age > 30]`{{execute}}

As you can see the output is just the list of values of the corresponding column, without any other information of samples. To get them as the result, the filtering could be dome using `[]` and the `,`. Similarly to filtering by columns, this time the condition should be before the comma.

You can specify which rows you want to choose. For example get rows of indexes from 2 to 5 and the 8th one:

`population[c(2:5, 8), ]`{{execute}}

If you want to apply the condition, do it analogically to the vector/lists mechanisms. Following up the examples above we get rows for males, people over 30 and with the combined conditions.

`population[population$gender == 'M', ]`{{execute}}
`population[population$age > 30, ]`{{execute}}
`population[population$gender == 'M' & population$age > 30, ]`{{execute}}

You can achieve the same results using functions instead of bare conditions.

`ageGreaterThan <- function(x, than) { x$age > than }
population[ageGreaterThan(population, 30), ]`{{execute}}
