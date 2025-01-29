# K8s installation

## 4. Các cách cài đặt Kubernetes cluster

- Có trên dưới 40 cách cài Kubernetes, tuy nhiên cần lựa chọn giải pháp cài đặt phù hợp với giải pháp hiện tại.
- `Kubeadm` cài đặt thủ công và rành mạch từng bước, có thể cài đặt version mới nhất.
- Cài đặt tự động: `kubespray`, `rke`, ... Tuy nhiên `kubespray` không đảm bảo cài đặt được version mới nhất.

## 5. Cài đặt Kubernetes cluster trên On-premise

Xem video và hướng dẫn ở [link](https://devopsedu.vn/courses/khoa-hoc-kubenetes-thuc-te/lesson/bai-5-trien-khai-kubernetes-cluster-tren-on-premise-2/)

### 5.1 Mô hình k8s cluster

- **Lưu ý:** Không nên triển khai ứng dụng lên server chạy `control plane`. Ứng dụng cao tải có thể chiếm tài nguyên của `control plan` làm ảnh hưởng đến cả quy trình điều phối của `control plan` và ảnh hưởng đến các dự án khác. Thông thường, cần một server riêng cho `control plane`.

## 6. Cài đặt Kubernetes cluster trên Cloud

Xem video và hướng dẫn ở [link](https://devopsedu.vn/courses/khoa-hoc-kubenetes-thuc-te/lesson/bai-6-trien-khai-kubernetes-cluster-tren-cloud-gke-2/)
