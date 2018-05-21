
In this lab we will play with [words embeddings](https://en.wikipedia.org/wiki/Word_embedding). We will use already prepare dataset downloaded from [fasttext](https://fasttext.cc/docs/en/english-vectors.html). Our vocabulary will be limited and containing only 10000 words (for the performance reasons).

The file includes lines representing word and the vector of embedding values. For instance:

`day 0.0320 0.0381 -0.0299 -0.0745 -0.0624 ...`

Let us download the embeddings file:

`curl -LO https://github.com/BasiaFusinska/katacoda-scenarios/raw/master/nlp-with-python/embeddings/assets/vectors.vec`{{execute}}

To start working with Python use the following command:

`python`{{execute}}

The task of reading the vectors is simple going through every line and building the dictionary {word: [embeddings]}. We've prepared a function to read data in the *data_reader* module.

`import data_reader
embeddings, words = data_reader.load_embeddings()`{{execute}}

Variable `embeddings` is a dictionary, `words` is just an array of words (read in the order presented in the file). Let's print some of the embeddings to get some feel of the data.

```
for word in words[:10]:
    print(word, embeddings[word])
```{{execute}}
