
> Note:
> **[“sparsity of connections”](https://datascience.stackexchange.com/questions/77439/how-does-sparsity-of-connections-in-cnns-causes-the-network-to-have-less-para)**

> **[Filter in CNN](https://kharshit.github.io/blog/2018/12/14/filters-in-convolutional-neural-networks)**

1. What do you think applying this filter to a grayscale image will do?\
+ Detecting image contrast.
+ **Detect vertical edges.**
+ Detect 45-degree edges.
+ Detect horizontal edges.
2. Suppose your input is a 128 by 128 color (RGB) image, and you are not using a convolutional network. If the first hidden layer has 64 neurons, each one fully connected to the input, how many parameters does this hidden layer have (including the bias parameters)?
+ 3145728
+ 1048640
+ 1048576
+ **3145792**
3. Suppose your input is a 256 by 256 color (RGB) image, and you use a convolutional layer with 128 filters that are each 7\times 77×7. How many parameters does this hidden layer have (including the bias parameters)?
+ **18944**
4. You have an input volume that is 63x63x16, and convolve it with 32 filters that are each 7x7, using a stride of 2 and no padding. What is the output volume? 
+ **29x29x32**
5. You have an input volume that is 15x15x8, and pad it using “pad=2”. What is the dimension of the resulting volume (after padding)?
+ **19x19x8**
6. You have a volume that is 121 x 121 x 32, and convolve it with 32 filters of 5×5, and a stride of 1. You want to use a "same" convolution. What is the padding?
+ **2**
7. You have an input volume that is 128x128x12, and apply max pooling with a stride of 4 and a filter size of 4. What is the output volume?
+ **32x32x12**
8. Because pooling layers do not have parameters, they do not affect the backpropagation (derivatives) calculation.
+ **Flase**
> Everything that influences the loss should appear in the backpropagation because we are computing derivatives. In fact, pooling layers modify the input by choosing one value out of several values in their input volume. Also, to compute derivatives for the layers that have parameters (Convolutions, Fully-Connected), we still need to backpropagate the gradient through the Pooling layers.
9. Which of the following are true about convolutional layers? (Check all that apply)
+ It allows parameters learned for one task to be shared even for a different task (transfer learning).
+ **It allows a feature detector to be used in multiple locations throughout the whole input volume.**
> Correct. Yes, since convolution involves sliding the filter throughout the whole input volume the feature detector is computed over all the volume.
+ It speeds up the training since we don't need to compute the gradient for convolutional layers.
+ **Convolutional layers provide sparsity of connections.**
> Yes, this happens since the next activation layer depends only on a small number of activations from the previous layer.
10. In lecture we talked about “sparsity of connections” as a benefit of using convolutional layers. What does this mean?
+ Regularization causes gradient descent to set many of the parameters to zero.
+ **Each activation in the next layer depends on only a small number of activations from the previous layer.**
+ Each filter is connected to every channel in the previous layer.
+ Each layer in a convolutional network is connected only to two other layers


