# Week 1

## Giới thiệu tổng quan về Data Engineering

### Tại sao cần Data Engineer (Why)

Giúp **hoạch định Data Strategy** và **xây dựng Data Platform** cho tổ chức:

1. Ingesting các nguồn dữ liệu định dạng khác nhau.
2. Integrating với hệ thống để vận hành trơn tru.
3. Transforming và quản lý hiệu quả lượng lớn dữ liệu gần như vô hạn.
4. Để phục vụ quá trình khai thác và phân tích dữ liệu với chi phí có thể chấp nhận được (cost-effectively).

Các bài toán thường gặp

- Data migration (on-premise to cloud).
- Data architecturing (storage, computation).
- Data transformation (optimization).
- Data ingestion (1st, 2nd, 3rd parties data).
- Data products (machine learning models).
- Data governance (strategy, security, quality and monitoring).

### Vai trò của Data Engineer (What)

- Data Strategy
- Data Infrastructure Management
- Data Governance
- Data Quality
- Data Security
- Data Integration
- Data Pipeline Development
- Data Warehousing
- Data Transformation & ETL
- Collaboration with Data Scientist and Analysts
- Documentation

### Các kĩ năng cần thiết của Data Engineer (How)

- Database, Data warehouse, data lakes để lưu trữ các dữ liệu sau khi biến đổi xong nhằm phục vụ cho các ứng dụng và tính năng khác.
- Tự động hoá các luồng dữ liệu để triển khai hệ thống xử lý dữ liệu cho công ty.

### Component của Big Data architecture và Lambda, Kappa architectures

[Read here](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/big-data-architectures)

Khoá học này tập trung xây dựng `Lambda architecture`.

## Bài toán lưu trữ, phân biệt các loại dữ liệu

### Structured data

Dữ liệu có cấu trúc được gọi là dữ liệu quan hệ, được tổ chứ theo dạng lược đồ (schema).

#### CSV

Ứng dụng:

- Chuyển đổi và xuất dữ liệu từ các hệ thống quản lý dữ liệu như MySQL hoặc SQL Server
- Phân tích và quản lý dữ liệu

Ưu điểm:

- Human-readable.
- Được sử dụng rộng rãi và dễ dàng sử dụng.
- Dễ dàng cập nhập và chỉnh sửa dữ liệu.

Nhược điểm:

- Không hỗ trợ kiểu dữ liệu phức tạp và các quan hệ giữa các bảng.
- Cần phải khai báo đúng định dạng để tránh lỗi khi xử lý dữ liệu có chứa kí tự đặc biệt (dấu phẩy, dấu ngoặc kép, ...)
- Không bảo mật và không mang tính năng quản lý dữ liệu như một cơ sở dữ liệu.

### Semi-structured data

Dữ liệu bán cấu trúc hay NoSQL (Not only SQL) chứa các thẻ giúp tổ chức và phân cấp dữ liệu rõ ràng.

`Serialization` là quá trình chuyển đổi dữ liệu thành định dạng có thể truyền đi hoặc lưu trữ được.

Dùng để truyền dữ liệu giữa các hệ thống với nhau, lưu trữ lại đâu đó để sử dụng sau này.

#### JSON

Ứng dụng:

- Chuyển đổi và xuất dữ liệu từ các hệ thống quản lý dữ liệu như MySQL hoặc SQL Server
- Truyền tải dữ liệu giữa máy chủ và trình duyệt thông qua qua API.

Ưu điểm:

- Dữ liệu được lưu trữ dưới dạng đơn giản, dễ đọc và dễ hiểu.
- Không giới hạn chiều sâu của data stuctures.
- Giúp tối ưu việc lưu trữ và truyền tải dữ liệu.
- Tích hợp với hầu hết ngôn ngữ lập trình.

Nhược điểm:

- JSON không hỗ trợ kiểu dữ liệu phức tạp như các cơ sở dữ liệu quan hệ.
- Kích thước dữ liệu lớn hơn CSV.

#### XML

Ứng dụng:

- Gửi và chia sẻ dữ liệu giữa các ứng dụng và hệ thống khác nhau.
- Lưu trữ dữ liệu trên các ứng dụng web.
- Sử dụng trong các hệ thống quản lý nội dung để định dạng nội dung và tạo ra trang web.

Ưu điểm:

- Định dạng dữ liệu một cách linh hoạt, dễ đọc.
- Tích hợp với các ngôn ngữ lập trình và các công nghệ web khác như HTML và JSON.

Nhược điểm:

- Có kích thước dữ liệu lớn hơn so với các định dạng dữ liệu khác.
- Cần có kiến thức chuyên môn về các thuộc tính, thẻ và cú pháp.

#### YAML

Ứng dụng:

- Lưu trữ cấu hình, cài đặt, mô tả về hệ thống.
- Dùng trong các ứng dụng CI/CD.
- Dùng cho các hệ thống quản trị cấu hình, hệ thống giám sát và các ứng dụng khác liên quan đến dữ liệu cấu hình.

Ưu điểm:

- Cú pháp ngắn gọn, dễ đọc và dễ hiểu hơn XML và JSON.
- Tập trung vào nội dung dữ liệu hơn là định dạng và cấu trúc. Do đó, cho phép phát triển nhanh chóng hơn.

Nhược điểm:

- Hạn chế định dạng dữ liệu phức tạp.
- Không cung cấp tính năng mã hoá.

### Unstructured data

- Media files, photos, videos và audio files.
- Microsoft 365 fiels: Word, excel, ...
- Text files
- Log files

### Dùng MinIO để lưu trữ dữ liệu phân tán

MinIO là một Open-source Object Storage, cũng tương tự như AWS S3.

### Dùng Pyspark để phân tích dữ liệu phân tán

### Column-oriented and Row-oriented storage

| Row-oriented Database                 | Column-oriented Database                    |
| ------------------------------------- | ------------------------------------------- |
| Easier to add, update and delete data | Data modification could be more complicated |
| Ideal for OLTP                        | Ideal for OLAP                              |
| Slower data aggregation               | Fast data aggregation                       |
| Poor compression                      | High-speed compression                      |
| Requires more space for data storage  | Require less space for data storage         |

[Read more](https://datapot.vn/luu-tru-du-lieu-row-based-storage-vs-column-based-storage/?srsltid=AfmBOoqARQcKhDTQlCMxDcB3r3xPMD5R59kpJ2zSG2cyfCgwwDHzo_Ew)

### Compression files

Compression giúp tiết kiệm chi phí lưu trữ

Các định dạng nén: Arvo, Parquet, ORC.
