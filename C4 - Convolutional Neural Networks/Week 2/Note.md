## **[LeNet 5](https://www.analyticsvidhya.com/blog/2021/03/the-architecture-of-lenet-5/)**

![Lenet 5](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%202/images/Lenet%205.png)

## **[AlextNet]()**
+ Similar LeNet but bigger
+ Using activation ReLU
+ Training with multiple GPUs
+ Local Response Normalization (LRN) - Now we dont use it

![AlextNet](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%202/images/AlexNet.png)


## **[VGG-16]()**
+ Alot of parameters you have to train

![VCG-16](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%202/images/VCG%20-%2016.png)\


> Very many deep NN are difficulf to train because of problem vanishing and exploring gradient (bien mat dao ham)
+ Skip connection: take activation from one layer  and suddenly feed it to another layer even much deeper in the neural network

## **[ResNets](https://viblo.asia/p/gioi-thieu-mang-resnet-vyDZOa7R5wj)**
+ ResNet (Residual Network) được giới thiệu đến công chúng vào năm 2015 
+ Dứng vị trí đầu tiên trong cuộc thi ILSVRC and COCO 2015 với ImageNet Detection, ImageNet localization, Coco detection và Coco segmentation
> **Why appeared the ResNet network?**
+ Một vấn đề xảy ra khi xây dựng mạng CNN với nhiều lớp chập sẽ xảy ra hiện tượng Vanishing Gradient dẫn tới quá trình học tập không tốt.
+ Trước hết thì Backpropagation Algorithm là một kỹ thuật thường được sử dụng trong quá trình tranining.
+ bổ sung Input X vào đầu ra của layer,việc này sẽ **chống lại việc đạo hàm bằng 0**, do vẫn còn cộng thêm X.

![Resnet](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%202/images/Resnet.png)
