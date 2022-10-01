## **Outputing the non-max supressed outputs**
+ For each grid call, get 2 predicted bounding boxes
+ Get rid of low probability predictions
+ For each class (pedestrian, car, motorcycle) use non-max suppression to generate final predictions.
## **Region Proposals:** Segmentation algorithm
+ RCNN: Propose regions. Classify proposed regions one at a time. Output label + bouding box
+ Fast R-CNN: Propose regions. Use the convolutional implementation of sliding windows to classify all the proposed regions.
+ Faster R-CNN: Use convolutional network to propose regions. (Faster alittle than Fast R-CNN)
+ YOLO inthis time is the faster that RCNN, Fast and Faster RCNN
<img src="/home/tuandinh/Desktop/Deep Learning/Deep-Learning-Specialization-Coursera/C4 - Convolutional Neural Networks/week 3/images/Region proposals.png" alt="Region proposals" width="600" height="300">

## **Semantic Segmentation with U-Net**
+ Examples: 

<img src="/home/tuandinh/Desktop/Deep Learning/Deep-Learning-Specialization-Coursera/C4 - Convolutional Neural Networks/week 3/images/object detection vs Semantic segmentation.png" alt="object detection vs Semantic segmentation" width="600" height="300">

<img src="/home/tuandinh/Desktop/Deep Learning/Deep-Learning-Specialization-Coursera/C4 - Convolutional Neural Networks/week 3/images/Example segmentation.png" alt= "images" width="600" height= "300">

## **Transpose Convolutions**
+ The transposed convolutional layer does exactly what a standard convolutional layer does but on a modified input feature map
+ Using to generate an output feature map that has a spatial dimension greater than that of the input feature map.
+ Just like the standard convolutional layer, the transposed convolutional layer is also defined by the padding and stride.
+ The idea behind transposed convolution is to carry out trainable upsampling
+ Transposed convolutions are standard convolutions but with a modified input feature map.
+ For examples: 

<img src="/home/tuandinh/Desktop/Deep Learning/Deep-Learning-Specialization-Coursera/C4 - Convolutional Neural Networks/week 3/images/transpose1.png" alt="1" width="500" height="250">

<img src="/home/tuandinh/Desktop/Deep Learning/Deep-Learning-Specialization-Coursera/C4 - Convolutional Neural Networks/week 3/images/transpose2.png" alt="2" width="500" height="250">

<img src="/home/tuandinh/Desktop/Deep Learning/Deep-Learning-Specialization-Coursera/C4 - Convolutional Neural Networks/week 3/images/transpose3.png" alt="1" width="500" height="250">

<img src="/home/tuandinh/Desktop/Deep Learning/Deep-Learning-Specialization-Coursera/C4 - Convolutional Neural Networks/week 3/images/transpose4.png" alt="1" width="500" height="250">