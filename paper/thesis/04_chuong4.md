# CHƯƠNG 4 — KHUNG ĐỀ XUẤT (hướng B)

> **KHỐI TRẠNG THÁI** · 24/09/2026
>
> Word mới có tiêu đề chương và năm tiêu đề mục của hướng cũ, chưa có thân bài. File này ghi **tiêu đề mới** và **yêu cầu viết** cho từng mục. Phần dùng lại được nằm ở `archive/2026-09-24_huong-bien-gioi-hieu-luc/04_chuong4.md`, bản `PHIÊN BẢN CHỈNH SỬA — 24/09/2026` cùng các khối bổ sung lượt 2, lượt 3 phía sau nó. Gọi tắt là **bản 24/09**.
>
> **Ràng buộc riêng của chương:**
> - **IR#11:** chương này đề xuất **khung**, không đề xuất FedBR. Mọi mô tả FedBR đi kèm [11].
> - **Hướng A** (FedBR cộng số hạng Taylor) **chưa được nhắc** trong chương cho tới khi có số liệu T2 (dàn bài §1.1). Thiết kế A ghi ở cuối file này, ngoài thân chương.
> - **Chương không chứa số đo.** Riêng ví dụ tỉ lệ 8 và 32 của phép thử chuẩn hoá được phép giữ: đó là phép kiểm tra mã, không phải kết quả thực nghiệm.

## Đổi tiêu đề trong Word

| Word hiện tại | Sau khi sửa |
|---|---|
| Chương 4. ĐỀ XUẤT | Chương 4. KHUNG ĐỀ XUẤT |
| 4.1 Tổng quan framework | 4.1 Kiến trúc khung chia sẻ mẫu trung bình |
| 4.2 Cô lập số hạng khai triển Taylor | 4.2 Các cách dùng mẫu trung bình |
| 4.3 Ma trận chế độ lệch phân phối | 4.3 Chuẩn hoá số hạng Taylor |
| 4.4 Mặt vận hành | 4.4 Chi phí tài nguyên |
| 4.5 Giao thức đo lường | 4.5 Giao thức đo lường (giữ) |

---

## Yêu cầu viết từng mục

### Đoạn mở chương

Hai đoạn ngắn:
- **Đoạn 1:** chương trình bày khung học liên kết chia sẻ mẫu trung bình, trong đó cách dùng mẫu trung bình là thành phần thay được; khung dựng theo đúng bốn giai đoạn của mô hình đề xuất.
- **Đoạn 2:** lộ trình năm mục.

Không viện dẫn đề cương như nguồn quyền uy (§7.5). Lý do chọn kiến trúc phải nằm trong câu.

### 4.1 Kiến trúc khung chia sẻ mẫu trung bình

- **Dùng lại** mục 4.1.2 bản 24/09: bốn giai đoạn (chuẩn bị ở client, gom và phát ở máy chủ, huấn luyện cục bộ, tổng hợp), lớp ghi nhận, và Hình 4.1 kèm chú thích.
- **Sửa theo quyết định về tập $V$** (dàn bài §3.2). Khung mô tả tập $V$ dựng một lần. Riêng thực nghiệm trên mã FedBR giữ hành vi của mã: FedMix và NaiveMix nhận mẫu trung bình dựng lại ở mỗi bước từ dữ liệu thô, còn FedBR dựng pseudo-data một lần. Viết thẳng rằng đây là lối tắt của mô phỏng, giữ lại để kết quả so được với bài FedBR. Hạn chế này ghi ở Ch.6.
- **Dùng lại** mục 4.1.3 bản 24/09 (quan hệ với mã FedBR), bỏ các dòng thuộc hướng cũ: cấu hình C, tham số $\alpha_{\text{rot}}$, mốc IID có xoay, tập môi trường kiểm tra chung. Thêm: cờ chọn cách chuẩn hoá (M1), target NaiveMix (M2).
- **Bảng 4.1 mới:** ba cách dùng × {nhận gì từ $V$ · dùng nhãn mềm không · mẫu trung bình đi vào đâu (đầu vào / số hạng gradient / đầu ra tầng phân lớp và không gian đặc trưng) · chi phí tính toán thêm}.

### 4.2 Các cách dùng mẫu trung bình

Mỗi cách dùng một đoạn và một công thức mục tiêu cục bộ, tham chiếu về Chương 3:
- NaiveMix (3.12);
- FedMix (3.15);
- FedBR (mục 3.5).

Làm rõ cái chung (cùng loại mẫu trung bình, cùng vị trí trong khung) và cái riêng (cách tiêu thụ, có dùng nhãn hay không).

Nêu thẳng một điểm: FedMix và NaiveMix khác nhau ở hai chỗ cùng lúc (điểm đánh giá, số hạng gradient). Vì vậy phép so hai cách này **không** cô lập được riêng số hạng Taylor. Phát biểu đúng là so sánh hai cách dùng.

Lưới bốn cấu hình và cấu hình C của hướng cũ (bản 24/09 mục 4.2.1): **chỉ đưa vào nếu T1 có chạy cấu hình C.**

### 4.3 Chuẩn hoá số hạng Taylor

- **Dùng lại** mục 4.2.3 bản 24/09, áp hàng 1–2 của khối lượt 3: cả ba bản cài đặt mã mở cùng thừa $1/B$; ví dụ tỉ lệ 8 và 32; cấu hình B′.
- **Sửa câu nối B′** cho khớp hướng B: FedMix ở Ch.5 mục 5.2 (nền tảng Flower) và ở `02_attempt` đều là bản gốc; mục 5.3.2 so bản gốc với bản sửa.
- **Dùng lại** hai yếu tố gây nhiễu còn đúng từ mục 4.2.4 bản 24/09:
  - biên độ số hạng gradient;
  - phép co đầu vào $(1{-}\lambda)x_i$, vì nó ảnh hưởng mọi so sánh FedMix với FedAvg.

### 4.4 Chi phí tài nguyên

- **Dùng lại** công thức (4.6) và đoạn *"hình dạng của phép đánh đổi"* ở mục 4.4.2 bản 24/09. Sửa chữ $n_V$ cho khớp cách mã FedBR dựng dữ liệu: FedMix/NaiveMix mỗi bước dựng 32 mẫu, FedBR dựng 32 pseudo-data một lần.
- **Chi phí tính toán:** đo bằng thời gian mỗi bước và thời gian quy về 1000 vòng. Số đo nằm ở Ch.5 mục 5.4.

### 4.5 Giao thức đo lường

Dùng lại các tiểu mục của mục 4.5 bản 24/09, áp khối lượt 3 (bỏ `[TG]`):
- **4.5.1 so sánh theo cặp.** Giữ.
- **4.5.2 chỉ so trong cùng nền tảng.** Giữ.
- **4.5.3 chỉ số độ chính xác.** Giữ: top-5 theo quy ước FedBR, kèm trung bình 5 mốc cuối.
- **4.5.4 ước lượng và cỡ mẫu.** Sửa theo $n = 3$ của hướng B. Nửa rộng 2,98 pp ở $s = 1{,}2$; nói thẳng rằng hiệu dưới khoảng 3 điểm chỉ báo cáo được dưới dạng khoảng.
- **4.5.5 họ giả thuyết.** **Viết lại** cho hướng B: không còn P1/P4.
  - Đề xuất họ chính gồm hai phép so sánh trên mã FedBR: FedBR − FedAvg và FedMix bản sửa − FedAvg, hiệu chỉnh Holm.
  - Mọi phép so sánh khác mang nhãn thăm dò.
  - Chốt họ này **trước** khi chạy T0.
- **4.5.6 đại lượng ghi nhận.** Giữ, áp hàng 7 của khối lượt 3.

---

## Ngoài thân chương — thiết kế hướng A (chỉ đưa vào Ch.4 khi T2 có số liệu)

**FedBR cộng số hạng Taylor.** Mục tiêu cục bộ là mục tiêu của FedBR cộng hai số hạng (II) và (III) của FedMix, tính trên cùng pseudo-data nhưng giữ nhãn mềm $\bar y_g$ thay vì nhãn đều. Số hạng (III) dùng chuẩn hoá đã sửa.

**Câu hỏi thiết kế cần chốt trước khi cài M3:**
1. **Nhãn.** Pseudo-data của FedBR mang nhãn đều. Số hạng (II) cần nhãn mềm, nên phải giữ histogram nhãn khi dựng RSM. Điều đó làm lộ phân phối nhãn của nhóm ảnh, giống FedMix.
2. **Trọng số.** Dùng lại $\lambda$ của FedMix (0,1) hay quét.
3. **Đối chứng.** Cấu hình FedBR + (II), không có (III), để biết phần cải thiện, nếu có, đến từ nhãn mềm hay từ số hạng Taylor.

Không chạy T2 trước khi T0–T1 xong (PLAN §5).