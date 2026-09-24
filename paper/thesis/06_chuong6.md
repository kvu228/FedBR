# CHƯƠNG 6 — KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN (hướng B)

> **KHỐI TRẠNG THÁI** · 24/09/2026
>
> | Mục | Trạng thái | Chờ |
> |---|---|---|
> | 6.1 Kết luận | `[CHỜ SỐ LIỆU]` | Ch.5 mục 5.6 |
> | 6.2 Đóng góp | `[CHỜ SỐ LIỆU]` | T0, T1 |
> | 6.3 Hạn chế | `[SỬA]`: dùng lại một phần `archive/…/06_chuong6.md` §6.3 | — |
> | 6.4 Hướng phát triển | `[SỬA]`: dùng lại một phần `archive/…/06_chuong6.md` §6.4 | — |
>
> Ch.6 là **văn xuôi liền mạch** (§7.6): không tiểu mục ba cấp, không khối in đậm mở câu. Mọi câu rào về giới hạn dồn về 6.3 (AI#4).

## 6.3 Hạn chế — những gì phải có

Dùng lại từ bản cũ các ý còn đúng với hướng B:
- phép xoay nằm ở cực dễ của phổ dịch chuyển miền và độc lập với lớp;
- chỉ quét được một phía của mức lệch;
- chẩn đoán cơ chế dùng mô hình ở vòng cuối;
- không có tuyên bố riêng tư hình thức;
- mô phỏng trên một máy, mọi client tham gia mọi vòng.

**Bỏ** các ý chỉ thuộc hướng cũ: trục Drop, ô D của lưới, số vòng rút gọn 300.

**Thêm** các ý của hướng B:
- chỉ ba hạt giống mỗi cấu hình, nên hiệu dưới khoảng ba điểm phần trăm không phân giải được;
- trên mã FedBR, lệch đặc trưng chỉ đi cùng lệch nhãn, nên không tách được tác động riêng của từng loại;
- mẫu trung bình của FedMix và NaiveMix được dựng lại mỗi bước từ dữ liệu thô, một lối tắt của mô phỏng;
- một họ kiến trúc không chuẩn hoá theo lô, và không chạy kiểm soát kiến trúc;
- số hạng Taylor trong mọi bản cài đặt mã mở bị thu nhỏ $B$ lần, nên kết quả FedMix đã công bố ở các nơi khác đều đo trên bản cài đặt đó.

## 6.4 Hướng phát triển — những gì phải có

- **Tác vụ hồi quy.** Đề cương có đăng ký; luận văn gác từ 22/09. Nền lý thuyết (Mệnh đề 4.1 về hàm mất mát bình phương) nằm ở `archive/…/04_chuong4.md` §4.6, dùng được làm điểm xuất phát.
- **Mở rộng vùng lân cận song phương**, như đề cương mô tả.
- **FedBR cộng số hạng Taylor** (hướng A), nếu chưa làm.
- **Lệch phân phối đặc trưng tách riêng và lệch đặc trưng thật.** Mã FedBR có sẵn PACS và WILDS Camelyon.
- **Phân tích riêng tư hình thức** cho giao thức chia sẻ mẫu trung bình.