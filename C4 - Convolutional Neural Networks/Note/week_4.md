## **Learning Objectives**
  + Differentiate between face recognition and face verification
  + Implement one-shot learning to solve a face recognition problem
  + Apply the triplet loss function to learn a network's parameters in the context of face recognition
  + Explain how to pose face recognition as a binary classification problem
  + Map face images into 128-dimensional encodings using a pretrained model
  + Perform face verification and face recognition with these encodings
  + Implement the Neural Style Transfer algorithm
  + Generate novel artistic images using Neural Style Transfer
  + Define the style cost function for Neural Style Transfer
  + Define the content cost function for Neural Style Transfer

## **What is Face Recognition:**
   + **Vertification:**
      + Input image, name/ID
      + Output whether the input images is that of the claimed person
   + **Recognition:**
      + Has database of K person
      + Get an input images 
      + Output ID if the image is any of the K person (or not recognized)
## **One Shot Learning Problem:**
   + We have just one image for training and we need to reconize this person
   + Learning a 'similarity' fuction:
      + d(img1, img2) = degree of difference between images
      + If d(img1, img2) <= T (T - Hyperparameter): The same person
      + If d(img1,img2) > T: fifference person
      > **It's vertification problem**
> So you can compare between input image with your image(just 1 image for training - it's very small), and then depends on value of function **d(img1, img2) - img1 (training), img2 (input image)** to vertification it is same or differenc person.
## **Siamese Network (SNN): Use Siamese network to solve One shot learning problem**
  + A siamese neural network (SNN) is a class of neural network architectures that contain two or more identical sub-networks. “Identical” here means they have the same configuration with the same parameters and weights.
  + it’s used to find similarities between  inputs by comparing its feature vectors
  + ![Siamese Networks](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%204/images/Siamese%20Network.png)
  + As we can see they compute diferrence between two images, and vertification
  ![SSN learning](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%204/images/SNN%20learning.png)

## **Face REcognition: Triplet Loss**
  + A-Anchor, P-Positive image, N-Negative images
  + we want ||f(A)-f(P)||^2 <= ||f(A)-f(N)||^2     **(d(A,P) <= d(A,N))**
  + ||f(A)-f(P)||^2 - ||f(A)-f(N)||  + alpha <= 0  **alpha (Hyperparameter)**
> **Loss function:**
  + Given 3 images A, P, N
  + L(A,P,N) = max( ||f(A)-f(P)||^2 - ||f(A)-f(N)||^2) + alpha, 0 )
  + J = SUM( L(A(i),P(i),N(i)) ), i = 1...n
> **How to choose the triplets A,P,N:**
  + During training, if A,P,N are chosen randomly, d(A,P) + alpha < d(A,N) is easily satisfied.
> **Summary:**
  + Training set using triplets loss: Anchor, Positive, Negative
  + ||f(A) - f(P)||^2 + alpha <= ||f(A)-f(N)||^2)
## **Face Verification and Binary Classification:**
  + Alternatives to triplet loss
  + ![Binary clf](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%204/images/Bianry%20classification%20video.png)

## **What is Neural Style Transfer?**
  + Create a new image from the style of another image
  + In order to implement Neural Style Transfer, you need to look at the features extracted by ConvNet at various layers, the shallow and the deeper layers of a ConvNet
## **What are deep ConvNets learning?**
  + ![ConvNet](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%204/images/ConvNet_Learning.png)
## **Cost function**
 + ![Neural Style Transfer](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%204/images/Neural%20Style%20Tranfer.png)
  + Tasks generated image G
    + Initiate G randomly: G: 100x100x3
    + Use gradient descent to minimize J(G)
## **We have Content cost function and Style Cost Function**
  + Content cost function:
    + ![Cost](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%204/images/Content%20Cost%20Function.png)
  + Style Cost Function:
    + ![Cost](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%204/images/Style%20Cost%20Function.png)
  + Summary:
    + ![Costs SUmmary](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%204/images/Summarry%20Style%20and%20Content%20Cost%20function.png)

