If you want to work with the parameters that can change their values when running the computational graph, you should consider using *variables*. In machine learning training process, the goal is to adjust some coefficients to fit the optimised function best.

Let's consider simple linear model and discover how you can manually change the values of variables. We'll provide x and y values of the data points in the placeholders:

`x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)`{{execute}}

The linear model has a form of **f(x) = a*x + b**. The **a** and **b** are the parameters. We'll use variables to define them and assign some default values.

`a = tf.Variable([1], dtype=tf.float32)
b = tf.Variable([-2], dtype=tf.float32)`{{execute}}

The linear model can them be defined as:

`linear_model = a*x + b`{{execute}}

To run the computational graph, you need first to initialize the variables. Their values won't be assigned like to the constants unless you explicitly do it:

`init = tf.global_variables_initializer()
sess.run(init)`{{execute}}

Now the model is ready to be evaluated. Note that because the linear model is not taking into account y values, there is no need to provide them in the `feed_dict` parameter.

`print(sess.run(linear_model, {x:[0,1,2,3,4,5]}))`{{execute}}

We'll use y values to verify how good the model is in the next step.
