To start working with Python use the following command:

`python`{{execute}}

Instead of using words as features when building the vocabulary one can use n-grams. Let's start simple and create bigrams for the following array of words:

`sentence_tokens = ['This', 'is', 'where', 'all', 'the', 'people', 'are', 'going', 'on', 'Friday']`{{execute}}

To create a bigram use `zip` to go through two lists having different starting point:

```
def bigrams(tokens):
    return zip(tokens, tokens[1:])
```{{execute}}

Let's have a look:

`list(bigrams(sentence_tokens))`{{execute}}

## Task: Create Trigrams function

Create function for trigram generation. Use `zip` function to go through three lists with different starting points.

`def trigrams(tokens):`{{execute}}

Once done print out the trigrams:

`list(trigrams(sentence_tokens))`{{execute}}
