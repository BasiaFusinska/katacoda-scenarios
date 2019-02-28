Once the network is set up it has to be trained. To do this let us first compile the model.

`model.compile(optimizer = tf.train.AdamOptimizer(), loss = tf.keras.losses.sparse_categorical_crossentropy)`{{execute}}

And define some training variables:

`epochs_number = 3
epoch_steps = (len(text)//sequence_len)//batch_size`{{execute}}

We'll want to save the model so let us set up the configuration for the checkpoints:

```
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")
checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)
```{{execute}}

Than we can perform the training

`model.fit(dataset.repeat(), epochs=epochs_number, steps_per_epoch=epoch_steps, callbacks=[checkpoint_callback])`{{execute}}
