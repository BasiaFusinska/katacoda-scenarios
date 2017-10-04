The goal of optimisation problem is to find the values that minimise or maximise the value of the loss function. TensorFlow is making this process more comfortable than we had the chance to observe in the Neural Network training scenario.

The first function we'll deal with is going to be the quadratic function:

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/function-optimisation/assets/equation.png" alt="Quadratic function equation">

You can see its plot below:

<img src="/basiafusinska/courses/deep-learning-with-tensorflow/function-optimisation/assets/quadratic.png" alt="Quadratic function">

The function has the minimum (of value -1) in the point 5. This one happens to have the analytical solution, but it's not usually the case. In the situation like this, you should use the math instead of the iterative optimisation process. Nonetheless, we will use the TensorFlow, for learning.

To start working with TensorFlow use the following command:

`python`{{execute}}

And import the library:

`import tensorflow as tf`{{execute}}

To define the function in TensorFlow, we will use tf.Variable for x starting from the value -10. Then we'll set up the function itself.

`x = tf.Variable(-10., dtype=tf.float32)
y = x**2 - 10*x + 24`{{execute}}
