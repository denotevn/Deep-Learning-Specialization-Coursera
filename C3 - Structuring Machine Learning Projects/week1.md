# **Week -1:**
   + Single Number Evalution: Idea -> Code -> Experiment -> Idea:
       + Model training quickly, Andrew Ng recommend do not use early stopping. 
       + Precision, Recal
       + F-1 score - Harmonnic mean between Precision (P) and Recal (R): **F1-score = 2/ (1/R + 1/P)**
       + dev set + Single number evaluation metric: speed up iterating (Tăng tốc quá trình cải thiện lặp đi lặp lại của model)
       + If we have many labels and for each other have error, we can compute average of this for easier choose what model is better.
   + Satisficing and Optimizing Metric (Số liệu thỏa mãn và tối ưu hóa)
       + cost = accuracy - -2.5 * running time
       + Optimizing: Accuracy
       + Satisficing: Running time
   + Train/dev/test distributions
       + development set hold out cross validation
       + The devst and test suite should both have the same distribution. That is, you must provide enough data of all the labels for the training set. Since then, the new model is effective when optimizing with a training set.
       + The dataset should both have all type. For example, analysis of solvency needs to have all the data of low-income people, high-income people, middle-income people, ...
       + **The dev set and test set on the same distributions (phan phoi)**
# **Week 1:**
   + Single Number Evalution: Idea -> Code -> Experiment -> Idea:
       + Model training quickly, Andrew Ng recommend do not use early stopping. 
       + Precision, Recal
       + F1 score - Harmonnic mean between Precision (P) and Recal (R): **F1-score = 2/ (1/R + 1/P)**
       + dev set + Single number evaluation metric: speed up iterating (Tăng tốc quá trình cải thiện lặp đi lặp lại của model)
       + If we have many labels and for each other have error, we can compute average of this for easier choose what model is better.
   + Satisficing and Optimizing Metric (Số liệu thỏa mãn và tối ưu hóa)
       + cost = accuracy - 0.5 * running time
       + Optimizing: Accuracy
       + Satisficing: Running time
   + Train/dev/test distributions
       + development set hold out cross validation
       + The devst and test suite should both have the same distribution. That is, you must provide enough data of all the labels for the training set. Since then, the new model is effective when optimizing with a training set.
       + The dataset should both have all type. For example, analysis of solvency needs to have all the data of low-income people, high-income people, middle-income people, ...
       + **The dev set and test set on the same distributions (phan phoi)**
## What is human-level performance?
+ How do we measure human-level performance?
    + Bạn cần phải trải qua quá trình dán nhãn thủ công để đo lường điều này.
    + Yêu cầu một nhóm người gắn nhãn một mẫu phân tầng và sau đó đo sai số trung bình.
    + **Đây cũng là Lỗi Bayes. Đây là lỗi thấp nhất mà một mô hình ML có thể đạt được.**
    + Ví dụ,  trong một bài toán nhận dạng thực thể tên, nếu trung bình một con người mắc 15 lỗi trong số 100 thực thể, thì hiệu suất ở cấp độ con người là 15%. Nếu lỗi huấn luyện là 15,2%. Tức chỉ sia lệch 0.2% thì môi hình của bạn vẫn được coi là tốt. Vì lỗi Bayes là thấp nhất (15%)
 
## The goal is to have one metric that focuses the development effort and increases iteration velocity

## When to change dev/test sets and metrics:
+ Ví dụ: Alogorithm A: 3%, Algorithm B: 5 5 error. Nhưng Algorithm B lại được đánh giá tốt hơn cho bài toán của bạn. Trong khi đó metrics vẫn cho rằng A là thuật toán tốt hơn. **Đó là dâu hiệu bạn cần thay đổi metrics**
## Avoidable Bias: **Cat classification:**
+ **Tùy thuộc vào Human perfomance**
+ Case 1:
    + Humman: 1% 
    + Training error: 8% 
    + Dev error: 10 %
    + ==> **Focus on bias**: model complex model, ...
+ Another:
    + Humman: 7.5 %
    + Training error: 8% 
    + Dev error: 10 %
    + ==> **Focus on variance**: Decrease Regularization, ...
+ **Sự khác biệt giữa Error Bayes hoặc lỗi sấp xỉ Bayes với training error là Avoidable Bias**
+ Sự khác biệt giữa Dev error và training error: **Variance**
## The two fundamental asumptions of supervised learning
+ You can fit the training set pretty well: **Advoidable bias**
+ The training set performance generalizes pretty well to the dev/test set: **Variance**
## **Sumarry**
+ Advoidable bias: 
    + Train bigger model
    + Train longer/better optimization algorithms: momentum, RMSpop, Adam
    + NN architecture/ hyperparameters search: RNN, CNN
+ Variance:
    + More data
    + Regularization: l2, dropuot, data agumentation
    + NN architecture/ hyperparameters search

## Nếu train error và dev error quá lệch so với human-performance thì ta giải quyết error có độ chênh lệch với human-performance trước. 
+ Human: 1%
+ train_error: 5%
+ dev_error: 7%
+ **==> Ta nên giải quyết về dev error trước**