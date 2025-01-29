# [Week 5](https://classroom.google.com/c/NzE2MDIxNDIyMjQx/m/NzM1NjU5MzcxMDc2/details)

## Map Reduce algorithm
### Dẫn nhập Big Data
### Giới thiệu Map reduce algorithm
### Map reduce implementation
Hadoop hiện thực mô hình MapReduce, mô hình mà ứng dụng sẽ được chia
nhỏ ra thành nhiều phân đoạn khác nhau được chạy song song trên nhiều
node khác nhau.

## Hadoop
### HDFS Architecture

## Hadoop vs Spark
## Spark
### Spark Runtime Architecture
Spark sử dụng master/slave architecture:
- Một coordinator (driver)
- Nhiều distributed workers (executors)

### Spark Contex
### Spark RDD
### RDD's DAGs example
Shuffle (gom các key giống nhau về chung một partition) trong MapReduce sẽ tốn rất nhiều tài nguyên. Vì vậy, để tối ưu Spark cần giảm shuffle nhiều nhất có thể (có cơ hội nên làm Narrow dependencies)
### Spark cache
Nhờ có cache mà Spark vượt qua được Hadoop về tốc độ tính toán trong iterative computing như: gradient descent, .... do trong iterative computing xuất hiện rất nhiều vòng lặp, nếu không caching lại thì tính toán sẽ rất chậm. Trong Spark hỗ trợ caching, do đó những vòng lặp tiếp theo sẽ tái sử dụng lại những kết quả trước đó => Tăng tốc độ tính toán.
### Spark broadcast
Sử dụng khi join 2 table: 1 table nhỏ, và 1 table rất lớn.

### Demo
Spark dataframe tốc độ aggregate thường sẽ nhanh hơn 4-6 lần so với thao tác trên RDD.
