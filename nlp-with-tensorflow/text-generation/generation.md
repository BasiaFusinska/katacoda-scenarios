Once you're confident about the model performance you can use it for text generation. Let us define the function to do it:

```
def generate_text(model, start_text, generate_len = 1000):
    input_indexes = tf.expand_dims([char2index[s] for s in start_text], 0)
    generated_text = []
    model.reset_states()
    for idx in range(generate_len):
        predictions = tf.squeeze(model(input_indexes), 0)
        predicted_index = tf.multinomial(predictions, num_samples=1)[-1,0].numpy()
        input_indexes = tf.expand_dims([predicted_index], 0)
        generated_text.append(index2char[predicted_index])
    return '{0}{1}'.format(start_text, ''.join(generated_text))
```{{execute}}

We can use it for the trained model:

`print(generate_text(generative_model, u"ROMEO: "))`{{execute}}

