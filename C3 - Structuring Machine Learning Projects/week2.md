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