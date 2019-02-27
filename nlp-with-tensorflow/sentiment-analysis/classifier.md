For the sentece to be the input of the neural network it has to be transformed into a set of features. In this example we are going to use [nnlm_en_dim128_encoder](https://tfhub.dev/google/nnlm-en-dim128/1), the encoder available from [TensorFlow Hub](https://www.tensorflow.org/hub/) that is performing this transformation. The following code is preparing the column from the free text:

`text_column = tf_hub.text_embedding_column("review", "https://tfhub.dev/google/nnlm-en-dim128/1")`{{execute}}

Once we have the features defined we can build canned estimaton that will prepare the fully connected neural network. The code below is building the network with 2 hidden layers (of sizez 512 and 128 respectively). It uses Adam Optimizer with the learning rate of 0.003.

```
sentiment_classifier = tf.estimator.DNNClassifier(
    hidden_units=[512, 128],
    feature_columns=[text_column],
    n_classes=2,
    optimizer=tf.train.AdagradOptimizer(learning_rate=0.003))

```{{execute}}
