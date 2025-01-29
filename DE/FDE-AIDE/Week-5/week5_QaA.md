1. Tại sao Spark được sinh ra để thay thế MapReduce, Spark đã thay đổi việc tính toán trên Cluster như thế nào?
- Hadoop bị bottleneck về network, ReadWrite throughput trên đĩa. Spark dùng RDD dùng được mọi transformation trên Memory nhưng vẫn đảm bảo fault tolerance.
