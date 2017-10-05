The Deep Learning training rarely works on the whole dataset. It happens to be much more efficient to use batches. With TensorFlow MNIST dataset this task is made very easy. You should just use the next_batch function with the proper batch size.

`images1, labels1 = mnist.train.next_batch(100)
len(images1)
images2, labels2 = mnist.train.next_batch(50)
len(images2)`{{execute}}
