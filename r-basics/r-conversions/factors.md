*Factors* are a specific type in R that represents enumeration or category.
This type resembles char type, but plays a different role.
Category can be represented by a number and text, the difference is how it is treated.

Regardless of the representation it cannot be used in calculations or text operations. You should consider it as the enumerable type. In languages like C# or Java it's equivalent to *enum* type.

To create a factor one should use `factor` function.

`categories <- factor(c('B', 'A', 'B', 'B', 'C', 'B', 'A', 'C', 'A', 'A'))
categories`{{execute}}

You can see that when displaying the whole vector, R automatically recognizes that there are only 3 unique values (levels): `A`, `B` and `C`.

You can check the type of `categories` by using `typeof` or `[0]` index.

`typeof(categories)
categories[0]`{{execute}}

First there is `factor` returned as a type, second instruction returns `integer`. You may be familiar with integers from different programming languages, but in R it plays different role - a *factor*.

You can check that there are no calculations available for factors:

`categories[1] + categories[2]`{{execute}}

R provides several functions for the factor type.
One is `summary`, second is `levels`. `summary` shows you factors values distributions.

`summary(categories)`{{execute}}

For the `category` variable, there are 4 elements of values `A` and `B` and 2 of value `C`.

`levels` function gives you the list of unique factors. Notice this list is sorted and the levels are not shown in the order of how they appear in the `categories` variable.

`levels(categories)`{{execute}}
