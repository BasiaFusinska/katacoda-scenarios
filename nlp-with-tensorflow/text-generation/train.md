Once the network is set up it has to be trained. To do this let us first compile the model.

`model.compile(optimizer = tf.train.AdamOptimizer(), loss = tf.keras.losses.sparse_categorical_crossentropy)`{{execute}}

And define some training variables:

`epochs_number = 3
epoch_steps = (len(text)//sequence_len)//batch_size`{{execute}}

Than we can perform the training

`model.fit(dataset.repeat(), epochs=epochs_number, steps_per_epoch=epoch_steps)`{{execute}}
