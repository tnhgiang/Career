# Week2 Q&A
## Theoretical lesson
1. Ingesting dữ liệu từ data sources nào? Làm sao quyết định sẽ lấy từ source nào?
- Hướng 1: brute force lấy hết data từ tất cả data sources bỏ hết vào data lake. Không cần biết data consumers cần gì, table nào không cần cũng lấy luôn, nên có thể không tối ưu chi phí và resource.
- Hướng 2: từ bussiness requirement quyết định nên ingest data từ data sources nào hoặc được chỉ định từ cấp trên và stakehoders. Việc ingest dữ liệu bị ảnh hưởng bởi nhiều thứ, ví dụ: chi phí mua data, phân quyền cho team data được truy cập vào những data ở level nào, ...

2.Với chiến lược full-load(append), không có nhu cầu de-duplicate để phân tích sự thay đổi là như thế nào? tưởng là append sẽ giúp lưu lại thay đổi ???

## Homework
1. Mục đích khi xử dụng `@contextmanager` khi khai báo `connect_mysql` để làm gì?
- Tài liệu contextmanager đã giải thích đủ, giảng viên không bổ sung gì thêm.
2. Khi lưu object lên MinIO, có cần check coi object đã tồn tại để tránh bị overwrite không? Hay sẽ sử dụng object versioning của MinIO?
- Không cần xử lý, partitioning có thể giải quyết việc file trùng nhau.
3. Tại sao `olist_orders_dataset` lại sử dụng `@multi-asset`. Giải thích rõ hơn về Multi-Assets? Về cách thức hoạt động của nó?
- Dùng asset cũng được, có điều phải specify `io_manager_key` cho `ins`.
4. Data trong `bronze layer` được chia thành 2 kiểu lưu trữ hot and cool. Những dữ liệu nào nên được lưu kiểu hot? kiểu dữ liệu nào nên được lưu kiểu cool? Làm sao để MinIO nhận biết được hot and cool storage?
