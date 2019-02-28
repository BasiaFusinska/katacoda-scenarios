RNN state is passed from timestep to timestep, so only fixed size of the batch is accepted. To make it work with the batch size of 1 you need to restore it and rebuild.
Let us define a functin to do this task:

```
def load_saved_model(checkpoint):
    model = build(vocabulary_size, embedding_size, 1, lstm_units)
    model.load_weights(checkpoint)
    model.build(tf.TensorShape([1, None]))
    return model
```{{execute}}

And restore the model:

`generative_model = load_saved_model(tf.train.latest_checkpoint(checkpoint_dir))`{{execute}}
