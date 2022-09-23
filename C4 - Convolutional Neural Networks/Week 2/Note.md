## Knowdlege this week : **[Week 2]**(https://marcossilva.github.io/en/2019/08/04/coursera-deep-learning-module-4-week-2.html)


## **[LeNet 5](https://www.analyticsvidhya.com/blog/2021/03/the-architecture-of-lenet-5/)**

![Lenet 5](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%202/images/Lenet%205.png)

## **[AlextNet](https://www.phamduytung.com/blog/2018-06-15-understanding-alexnet/)**
+ Similar LeNet but bigger
+ Using activation ReLU
+ Training with multiple GPUs
+ Local Response Normalization (LRN) - Now we dont use it

![AlextNet](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%202/images/AlexNet.png)


## **[VGG-16](https://www.geeksforgeeks.org/vgg-16-cnn-model/)**
+ Alot of parameters you have to train

![VCG-16](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%202/images/VCG%20-%2016.png)\


> Very many deep NN are difficulf to train because of problem vanishing and exploring gradient (bien mat dao ham)
+ Skip connection: take activation from one layer  and suddenly feed it to another layer even much deeper in the neural network

## **[ResNets](https://viblo.asia/p/gioi-thieu-mang-resnet-vyDZOa7R5wj)**
>**[Mobile Net v2](https://machinethink.net/blog/mobilenet-v2/)**
>
+ ResNet (Residual Network) được giới thiệu đến công chúng vào năm 2015 
+ Dứng vị trí đầu tiên trong cuộc thi ILSVRC and COCO 2015 với ImageNet Detection, ImageNet localization, Coco detection và Coco segmentation
> **Why appeared the ResNet network?**
+ Một vấn đề xảy ra khi xây dựng mạng CNN với nhiều lớp chập sẽ xảy ra hiện tượng Vanishing Gradient dẫn tới quá trình học tập không tốt.
+ Trước hết thì Backpropagation Algorithm là một kỹ thuật thường được sử dụng trong quá trình tranining.
+ bổ sung Input X vào đầu ra của layer,việc này sẽ **chống lại việc đạo hàm bằng 0**, do vẫn còn cộng thêm X.

![Resnet](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C4%20-%20Convolutional%20Neural%20Networks/Week%202/images/Resnet.png)

## **[Inception Networks - GoogleNet](https://towardsdatascience.com/deep-learning-understand-the-inception-module-56146866e652 )**
> 1 x 1 Chuyển đổi
> Mục đích : Giảm kích thước của dữ liệu đi qua mạng, mang lại lợi ích bổ sung là tăng chiều rộng và chiều sâu của mạng.
> 
> Các chập 1x1 làm giảm kích thước của các đầu vào trong mạng. Các chập 1x1 được định cấu hình để có số lượng bộ lọc giảm, do đó, các đầu ra thường có số lượng kênh giảm so với đầu vào ban đầu.

+ Độ phân giải 3 x 3 và 5 x 5
Mục đích : Cho phép mạng tìm hiểu các mẫu không gian khác nhau ở các quy mô khác nhau do kích thước bộ lọc chuyển đổi khác nhau.

## **Data Agmentation**
+ Mirroring, Cropping, Color shifting
+ Rotation, Shearing, Local warping
+ **PCA color Augmentation (RB) - AlexNet**

## **State of Computer Vision**
## **NOTE**
![TIP]()