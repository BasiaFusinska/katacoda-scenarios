You didn't expect punctuation to be the most common "word". You probably din't expect it to be a word at all, right? Let's fix it as there are several ways of doing it.
You also have to remember that just removing punctuation is maybe not what you want to achieve when working with real text as there may be words you may want to keep that have include them (for instance I'm, wouldn't, etc.).

First you need to decide if you want to get rid of all the punctuation. You can also either replace the characters directly in the document or after tokenizing in the words.

One way is to remove the characters (for instance all the character from ''). You can also use the `isalpha` function. Keep in mind that it will nor remove the character but rather answer the question if the text is all alphanumeric.

`"abcd".isalpha()
"abcd0".isalpha()
"abcd,".isalpha()
"(abcd)".isalpha()
`{{execute}}

Another way is to use regular expressions. If there is a match to the expression the match will be returned (`None` is the output of there not being a match).

```
import re
pattern = re.compile("^[a-zA-Z]{2,}$") # Only words that are at least two characters long and letters of the alphabet

pattern.match("a")
pattern.match("ab")
pattern.match("a0b")
pattern.match("012")
pattern.match("(abc)")
pattern.match("abc.")
```{{execute}}

# Task

Chose the way of removing punctuation and apply it to the whole corpus (all documents).
