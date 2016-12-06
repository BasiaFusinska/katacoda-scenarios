Last step has shown that when applying multiple conditions, filtering statements can become quite complex and may not reflect the intentions clearly.

This is where the `subset` function can help. It allows you to skip constantly writing the name of the data frame by providing it as an argument.

If you want to filter data frame by age you could use the following syntax:

`subset(population, age > 30)`{{execute}}

You can of course use `ageGreaterThan` function created in last step, but it doesn't seem to improve the readability of the statement.

`subset(population, ageGreaterThan(population, 30))`{{execute}}

You can see `subset` function being useful when putting conditions together. For example the following statement is much easier to read when getting the population of males over 30:

`subset(population, gender == 'M' & age > 30)`{{execute}}

Apart from filtering samples you could use the function when picking up specific columns. Nothing should stop you from putting both filters together.

If you want to know only the gender and smoking information for people over 30 you could choose second and third column only.

`subset(population, age > 30, select=c(2,3))`{{execute}}

Or you can work with column names:

`subset(population, age > 30, select=c(gender,smoker))`{{execute}}

Note that this time column names don't have to come in as char types. If you want you could also use strings.

`subset(population, age > 30, select=c('gender','smoker'))`{{execute}}

Another simple way of removing the complexity of statements is to use `attach` and `detach` functions. They 'load' and 'unload' your data frame and give you the access to the columns directly. In our examples you could use the following code:

`attach(population)
gender
population[age > 30,]
detach(population)`{{execute}}
