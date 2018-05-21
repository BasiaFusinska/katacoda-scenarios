NLTK is a powerful library that can do much more than simply tokenizing the text. For example, it allows easily to recognize the part of speech by using `pos_tag` function.

Let's try it for different sentences:

```
from nltk import pos_tag

pos_tag("Mary was wearing the hat while walking down the street")
pos_tag("Now there is something completely different going on")
pos_tag("Let's see if you can guess this one")
```{{execute}}

NLTK provides the documentation for the tags. Let's see some of them:

```
import nltk

nltk.help.upenn_tagset('NN')
nltk.help.upenn_tagset('CC')
nltk.help.upenn_tagset('RB')
nltk.help.upenn_tagset('VB')
```{{execute}}
