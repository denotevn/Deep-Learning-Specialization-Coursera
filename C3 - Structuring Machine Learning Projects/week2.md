# Carrying Out Error Analysis
+ Tập trung vào những phần có lỗi âm tính để thu được kết quả cao nhất: 
+ Ví dụ về phân loại chó mèo có 10% erorr trên tập dev. Lây 100 ví dụ từ những ví dụ sai về phân loại cho mèo
+ Đếm xem có 5 lỗi sai là chó ==> Không nên tập trung vào chó chỉ tăng độ chính xác là 5/100.
+ Giả sử đếm có 50 lỗi sai là mèo => nên tập trung về phân loại mèo rõ ràng thu được kết quả optimize tốt hơn (1/2 * 10%) = 5%
## Error for multiple labels:
> **Hoặc có thể bạn thấy rằng một số hình ảnh của mình bị mờ, và sẽ thật tuyệt nếu bạn có thể thiết kế thứ gì đó hoạt động tốt hơn trên những hình ảnh bị mờ**
+ Đếm các hình ảnh bị mờ và không bị mờ, Đếm những lỗi phân loại sai của các ảnh bị mờ. Từ đó thu về cái nhìn tổng quan nhất về các lỗi và nguyên nhân gây ra lỗi
# **Cleaning Up Incorrectly Labeled Data** 
+ Dữ liệu đào tạo của bạn có nhãn sai sẽ làm cho model của bạn thiếu độ chính xác. Để tăng độ chính xác ta cần xử lý vấn đề này
+ Cần phải đếm và so sánh lỗi của incorrect labels với lỗi của nguyên nhân khác. Sau đố fix nguyên nhân gây ra lỗi lớn nhất trước.
![NOTE](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C3%20-%20Structuring%20Machine%20Learning%20Projects/image/Screenshot%20from%202022-09-04%2021-35-24.png)

> **Correcting incorrect dev/test set samples:**
+ Apply the same process to your dev and test sets to make sure they continue to come from the same distribution (Tổng quát cho các bộ thử nghiệm, hoạt động tốt hơn khi dev và test đến từ cùng một phân phối)
+ Consider examining examples your algorithm got rights as well as ones it got wrong
+ Train/dev data may now come from slightly different distributionDữ liệu đào tạo / nhà phát triển hiện có thể đến từ các bản phân phối hơi khác nhau
# **Training and Testing on Different Distributions**
+ Data from web pages (200000) and data from mobile app (10000): Different Distributions
> **OPTION 1:** Trộn lẫn tất cả (210000 images) và chia ra train/dev/test set:
  + Cùng phân phối
  + Nhưng hầu hết phân phối đều đến từ tập dữ liệu web pages và đây là 1 nhược điểm lớn tren dev and test set
  + Mục tiêu sẽ trỏ thành tối ưu hoá các ảnh ở trên tập dữ liệu từ web app, nhưng chúng ta muốn là phân loại ảnh ở mobile app
  ![Knowledge](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C3%20-%20Structuring%20Machine%20Learning%20Projects/image/difference%20distributions.png)
**OPTION 2:** Dev and test set will be all data from mobile app
  + better then option 1
  + Bất lợi: Bộ dev và test set không cùng phân phối với bộ train set
![Knowledge](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C3%20-%20Structuring%20Machine%20Learning%20Projects/image/Speech%20recognition%20ex.png)

# **Bias and Variance with Mismatched Data Distributions**
![Cat examples](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C3%20-%20Structuring%20Machine%20Learning%20Projects/image/Mismatched%20training%20and%20devtest%20set.png)

![More examples](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C3%20-%20Structuring%20Machine%20Learning%20Projects/image/Bias%20Variance.png)

![More](https://github.com/denotevn/Deep-Learning-Specialization-Coursera/blob/main/C3%20-%20Structuring%20Machine%20Learning%20Projects/image/MOre%20general%20formulation.png)