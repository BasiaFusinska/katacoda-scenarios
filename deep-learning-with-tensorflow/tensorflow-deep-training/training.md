Once you've built the computation graph, it's time to run the actual training. To do this TensorFlow requires opening the session and initialising the variables.

## Task 4

The training itself is performed in steps when the train_step is run. To make it work you need to feed the graph with the placeholders values. You can use previously defined X and Y for this task.

When the file is ready, run it using the following command:

`python neural_network.py`{{execute}}
