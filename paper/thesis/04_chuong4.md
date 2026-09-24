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
---

# PHIÊN BẢN CHỈNH SỬA — 24/09/2026 · thân Chương 4 (phần lý thuyết và thiết kế)

> **Cách đọc.** Chỉ-append. Khối này là **thân Chương 4 theo hướng B**, chép vào Word dưới các tiêu đề mới ở bảng đầu file. Chương không chứa kết quả thực nghiệm. Các con số xuất hiện trong chương là tham số cấu hình, phép tính từ công thức, hoặc số đã công bố trong bài báo khác.
>
> **Nguồn dùng lại:** `archive/2026-09-24_huong-bien-gioi-hieu-luc/04_chuong4.md` bản 24/09 (mục 4.1.2, 4.2.3, 4.2.4, 4.4.2, 4.5), đã sửa theo hướng B.
>
> **Viết theo mã hiện tại, không sửa mã** (quyết định của học viên, 24/09):
> - mọi kết quả FedMix trong luận văn dùng cách chuẩn hoá của mã phát hành;
> - không có cấu hình B′ đối chiếu;
> - không ghi thêm đại lượng chẩn đoán nào trên mã FedBR.
>
> Nếu sau này mã được sửa thì cập nhật mục 4.3 và 4.5.6.
>
> **Còn chờ học viên chốt `[QUYẾT]`:**
> - họ giả thuyết chính ở mục 4.5.5 phải chốt **trước khi chạy T0**;
> - Hình 4.1 chưa vẽ.
>
> **Phát hiện mới khi viết mục 4.2.4.** Trong mã FedBR, FedMix và NaiveMix nhận 32 mẫu trung bình mới ở mỗi bước, còn FedBR dùng một tập 32 pseudo-sample cố định. Phép so FedBR với FedMix vì vậy không chỉ khác ở cách dùng mẫu trung bình. Câu tương ứng trong `01_chuong1.md` (hàng 5, *"…quy được cho cách dùng"*) nói quá; bản sửa ở khối bổ sung cuối file đó.
>
> **Tự kiểm §7.7** (thân chương):
> - không có dấu `—` chêm, không có cụm sáo, không viện dẫn đề cương hay bài hội nghị;
> - AI#1: hai khuôn tương phản, ở mục 4.2.4 và 4.5.2, đều để phân định phạm vi phép so sánh;
> - AI#4: một câu rào, ở mục 4.3 (*"là kết quả về FedMix như nó đang được cài đặt"*).

Chương này trình bày khung học liên kết chia sẻ mẫu trung bình đại diện mà luận văn đề xuất. Khung đi qua bốn giai đoạn:
1. client tạo mẫu trung bình từ dữ liệu cục bộ;
2. máy chủ gom các mẫu ấy rồi phát lại cho mọi client;
3. client dùng mẫu trung bình trong huấn luyện cục bộ;
4. máy chủ tổng hợp tham số.

Điểm cốt lõi của khung là cách dùng mẫu trung bình ở giai đoạn thứ ba không bị cố định. Nó là một thành phần thay được, nên các phương pháp khác nhau đặt được vào cùng một khung và so được với nhau trên cùng một loại dữ liệu.

Mục 4.1 mô tả kiến trúc của khung và cách khung được cài trên mã nguồn FedBR [11]. Mục 4.2 trình bày ba cách dùng mẫu trung bình và cách đọc các phép so sánh giữa chúng. Mục 4.3 phân tích phép chuẩn hoá số hạng Taylor trong các bản cài đặt FedMix hiện có. Chi phí tài nguyên được tính ở mục 4.4. Mục 4.5 là giao thức đo lường, áp cho mọi phép so sánh ở Chương 5.

## 4.1. Kiến trúc khung chia sẻ mẫu trung bình

### 4.1.1. Bốn giai đoạn

**Giai đoạn chuẩn bị ở client** diễn ra một lần, trước vòng truyền thông đầu tiên.
- Client $i$ rút ngẫu nhiên $M$ ảnh cục bộ và tính ảnh trung bình cùng nhãn mềm theo (3.11), rồi lặp lại $n_V$ lần để có $n_V$ mẫu trung bình. Các mẫu này được gửi lên máy chủ.
- Ảnh riêng lẻ không rời client; thứ rời client là trung bình của $M$ ảnh.
- Tham số $M$ quyết định mức làm mịn: $M = 1$ tương đương gửi ảnh thô, còn $M$ lớn cho ảnh gần như không nhận dạng được. $M$ vì vậy là thước đo thô cho mức làm mịn của dữ liệu được chia sẻ.

**Máy chủ** gom mẫu của mọi client thành tập $V = \bigcup_i V_i$ gồm $N n_V$ phần tử, rồi phát tập đó xuống mọi client, cũng một lần. Từ đây $V$ cố định trong suốt quá trình huấn luyện.

**Trong vòng lặp huấn luyện cục bộ**, ở mỗi bước client lấy một lô $B$ ảnh của mình và $B$ phần tử của $V$, ghép với nhau theo chỉ số. Hàm mất mát được tính theo cách dùng đã chọn cho lần chạy (mục 4.2); FedAvg thì bỏ qua $V$. Sau $K$ bước, client gửi tham số lên máy chủ.

**Máy chủ tổng hợp** tham số bằng trung bình có trọng số như FedAvg [2], không thay đổi gì.

**Lớp ghi nhận** bao quanh cả bốn giai đoạn. Ở mỗi mốc đánh giá, nó ghi độ chính xác trên từng tập kiểm tra, thời gian mỗi bước, và toàn bộ cấu hình của lần chạy.

> `[CẦN VẼ — Hình 4.1]` Sơ đồ hai cột theo bố cục mô hình đề xuất: máy chủ bên trái, client bên phải. Khối "Huấn luyện cục bộ" có một bộ chọn ba nhánh: NaiveMix / FedMix / FedBR.

**Hình 4.1.** Kiến trúc khung chia sẻ mẫu trung bình. Mũi tên nét đứt là trao đổi diễn ra một lần trước huấn luyện: mẫu trung bình đi lên máy chủ, tập $V$ đi xuống client. Mũi tên nét liền là trao đổi tham số mô hình ở mỗi vòng truyền thông. Bộ chọn trong khối huấn luyện cục bộ quyết định mẫu trung bình được dùng theo cách nào.

### 4.1.2. Khung trên mã nguồn FedBR

Khung được cài trên mã nguồn công bố của [11]. Mã này đã có ba cách dùng dưới dạng ba thuật toán NaiveMix, FedMix và FedBR, cùng bộ dữ liệu CIFAR-10 xoay, bộ phân hoạch dữ liệu và các thuật toán đối chứng. Luận văn dùng các thuật toán ấy như ba lựa chọn của giai đoạn huấn luyện cục bộ, và giữ nguyên mã.

Mã nguồn đi khác sơ đồ ở giai đoạn chuẩn bị, và luận văn giữ nguyên chỗ khác đó.
- **FedBR** dựng pseudo-data đúng một lần trước huấn luyện: 32 mẫu, mỗi mẫu là trung bình của 10 ảnh. Cách này khớp với giai đoạn chuẩn bị.
- **NaiveMix và FedMix** dựng lại một lô 32 mẫu trung bình mới ở mỗi bước cục bộ, mỗi mẫu cũng là trung bình của 10 ảnh, lấy thẳng từ dữ liệu thô của mọi client.

Cách làm thứ hai chỉ chạy được trong mô phỏng, nơi mọi dữ liệu nằm trên một máy. Luận văn giữ nó để kết quả so được với bảng công bố của [11], và Chương 6 nêu nó trong phần hạn chế.

**Bảng 4.1.** Ba cách dùng mẫu trung bình trong khung. $x_i$ là ảnh cục bộ; $\bar x_g$ và $\bar y_g$ là ảnh trung bình và nhãn mềm theo (3.11); $u_p$ là pseudo-sample theo (3.16); $\lambda$ là trọng số trộn của NaiveMix và FedMix; $C$ là số lớp. Hàng cuối mô tả mã nguồn của [11] mà Chương 5 chạy.

| | NaiveMix | FedMix | FedBR |
|---|---|---|---|
| Nhận từ các client khác | ảnh trung bình và nhãn mềm | ảnh trung bình và nhãn mềm | ảnh trung bình |
| Nhãn gắn với mẫu trung bình | nhãn mềm $\bar y_g$ | nhãn mềm $\bar y_g$ | nhãn đều $1/C$ |
| Mẫu trung bình đi vào đâu | đầu vào mô hình, trộn với ảnh cục bộ | tích vô hướng với gradient theo đầu vào | đầu ra tầng phân lớp và không gian đặc trưng |
| Mục tiêu cục bộ | (3.12) | (3.15) | (3.19) |
| Tính toán thêm mỗi bước so với FedAvg | không đáng kể | một lượt lan truyền ngược bậc hai | các lượt truyền xuôi trên pseudo-data và tầng chiếu, cùng một bước cập nhật riêng cho tầng chiếu |
| Mẫu trung bình trong mã nguồn | 32 mẫu mới mỗi bước | 32 mẫu mới mỗi bước | 32 mẫu, dựng một lần |

## 4.2. Các cách dùng mẫu trung bình

### 4.2.1. Trộn trực tiếp: NaiveMix

NaiveMix thay mẫu của client khác trong global Mixup bằng mẫu trung bình, rồi dùng nguyên phép trộn (3.12). Mô hình nhìn thấy ảnh đã trộn $(1{-}\lambda)x_i + \lambda\bar x_g$, và hàm mất mát tách theo nhãn thành hai phần: phần ứng với nhãn cục bộ $y_i$ mang trọng số $1{-}\lambda$, phần ứng với nhãn mềm $\bar y_g$ mang trọng số $\lambda$. Mẫu trung bình đi qua toàn bộ mạng như một ảnh bình thường.

### 4.2.2. Qua khai triển Taylor: FedMix

FedMix xấp xỉ chính mục tiêu (3.12) bằng khai triển Taylor bậc nhất quanh ảnh cục bộ đã co tỉ lệ, rồi bỏ số hạng bậc hai của trọng số trộn, được (3.15). Mô hình chỉ nhìn thấy $(1{-}\lambda)x_i$. Ảnh trung bình đi vào mục tiêu qua tích vô hướng giữa $\bar x_g$ và gradient của hàm mất mát theo đầu vào, với hệ số $\lambda(1{-}\lambda)$; nhãn mềm đi vào qua số hạng (II). Đây là cơ chế xấp xỉ hàm mất mát bằng khai triển Taylor mà luận văn nghiên cứu, và là cách dùng mặc định của khung.

### 4.2.3. Làm điểm tựa: FedBR

FedBR bỏ nhãn của mẫu trung bình và dùng nó theo (3.19). Ở đầu ra tầng phân lớp, $L_{\text{bal}}$ kéo dự đoán trên pseudo-data về phân phối đều. Ở không gian đặc trưng, $\ell_{\text{con}}$ kéo đặc trưng cục bộ của pseudo-data về đặc trưng toàn cục của chính nó, qua một bài toán min-max với tầng chiếu. Mẫu trung bình không đi vào lượt truyền xuôi trên dữ liệu cục bộ, và không có trọng số trộn nào.

### 4.2.4. Đọc các phép so sánh

**Với FedAvg.** Hiệu giữa mỗi cách dùng và FedAvg đo mức cải thiện của một phương pháp hoàn chỉnh so với đường cơ sở. Đây là loại so sánh chính của Chương 5.

**FedMix với NaiveMix.** Hai cách dùng nhận cùng mẫu trung bình, cùng nhãn mềm và cùng trọng số trộn, nhưng khác nhau ở hai chỗ cùng lúc: điểm đánh giá hàm mất mát, và sự có mặt của số hạng gradient. Hiệu giữa chúng vì vậy so hai cách dùng cùng một thông tin, và không quy riêng được cho số hạng Taylor.

Việc dùng chung một trọng số trộn vẫn loại được một nguồn nhiễu có thật trong bài báo FedMix [1]. Ở bảng kết quả chính của bài báo đó, NaiveMix đạt 77,4% và FedMix 81,2% trên CIFAR-10. Trong phép quét trọng số trộn ở phụ lục, giá trị tốt nhất của NaiveMix là 80,6%, chỉ còn cách FedMix 0,6 điểm. Luận văn đặt $\lambda = 0{,}1$ cho cả hai, là giá trị mặc định của mã nguồn [11], và chốt giá trị này trước khi chạy.

**FedBR với FedMix.** Phép so này khác nhau ở nhiều chỗ hơn chỉ cách dùng mẫu trung bình. Trong mã nguồn, FedMix nhìn thấy một lô mẫu trung bình mới ở mỗi bước, còn FedBR chỉ có 32 pseudo-sample cố định. FedBR còn có thêm tầng chiếu, bước cập nhật riêng cho tầng chiếu, và bộ siêu tham số riêng. Hiệu giữa hai phương pháp vì vậy là hiệu giữa hai phương pháp hoàn chỉnh cùng dùng một loại dữ liệu, chứ không phải phép đo tách riêng ảnh hưởng của cách dùng.

## 4.3. Chuẩn hoá số hạng Taylor

Để FedMix đúng là (3.15), cả ba số hạng phải được lấy trung bình trên lô theo cùng một cách. Luận văn đối chiếu ba bản cài đặt FedMix mã mở: mã nguồn của [11], bản cài đặt trên nền tảng Flower dùng ở mục 5.2, và bản cài đặt của DevPranjal. Cả ba làm vậy với hai số hạng đầu, nhưng không làm với số hạng thứ ba.

Trình tự tính trong cả ba bản cài đặt giống nhau:
1. Số hạng thứ nhất là $(1{-}\lambda)$ nhân **trung bình** cross-entropy trên lô $B$ ảnh đã co tỉ lệ. Đạo hàm của nó theo từng ảnh vì vậy mang sẵn thừa số $(1{-}\lambda)/B$.
2. Số hạng thứ ba nhân đạo hàm đó với $\bar x_g$, nhân thêm $\lambda$, rồi lấy trung bình hoặc chia cho $B$ một lần nữa.

Thừa số $1/B$ xuất hiện hai lần. Số hạng (III) vì vậy đi vào mục tiêu với hệ số $\lambda(1{-}\lambda)/B$ thay cho $\lambda(1{-}\lambda)$. Thừa số $\lambda(1{-}\lambda)$ được tính đúng; chỗ lệch nằm ở phép chuẩn hoá theo lô.

Phép thử trực tiếp xác nhận điều này. Đoạn mã tính số hạng thứ ba của mã nguồn [11] được chạy nguyên văn trên một mạng tuyến tính nhỏ, rồi so với trung bình trên lô của số hạng (III) tính từ gradient của từng mẫu. Tỉ lệ giữa hai giá trị đúng bằng 8 khi lô có 8 ảnh và bằng 32 khi lô có 32 ảnh. Với kích thước lô trong cấu hình thực nghiệm, số hạng Taylor nhỏ hơn công thức 32 lần trên mã nguồn [11] và 10 lần trên nền tảng Flower.

Mọi kết quả FedMix trong luận văn đều dùng cách chuẩn hoá này, và mỗi bảng kết quả ghi rõ điều đó. Các kết quả ấy vì vậy là kết quả về FedMix như nó đang được cài đặt; biên độ của số hạng Taylor theo đúng (3.15) không được đo trong luận văn.

Hai yếu tố khác cũng ảnh hưởng tới cách đọc kết quả FedMix.

**Biên độ của số hạng gradient đổi theo quá trình huấn luyện.** Nó tỉ lệ với độ lớn của $\nabla_x\ell$. Một FedMix gần như trùng FedAvg có thể do số hạng không mang thông tin, cũng có thể do nó quá nhỏ ở cấu hình đang xét. Phép chuẩn hoá vừa nêu là một trường hợp cụ thể của khả năng thứ hai.

**Phép co đầu vào.** FedMix huấn luyện trên ảnh đã co $(1{-}\lambda)x_i$, trong khi mô hình được đánh giá trên ảnh gốc. Với backbone không dùng chuẩn hoá theo lô, riêng độ lệch thang này đã có thể làm đổi độ chính xác. NaiveMix không gặp vấn đề này, vì ảnh trộn giữ nguyên thang trung bình của ảnh gốc. So sánh FedMix với FedAvg hay với NaiveMix vì vậy luôn gộp cả ảnh hưởng của phép co.

## 4.4. Chi phí tài nguyên

### 4.4.1. Chi phí truyền thông

Theo thiết kế của khung, mẫu trung bình chỉ được truyền một lần trước vòng đầu tiên, theo hai chiều. Gọi:
- $N$ là số client, $n_V$ là số mẫu trung bình mỗi client gửi;
- $d_x$ là số giá trị của một ảnh, $C_y$ là số giá trị của nhãn đi kèm;
- $b$ là số byte mỗi giá trị.

$C_y = C$ khi nhãn mềm được gửi, như ở NaiveMix và FedMix, và $C_y = 0$ với FedBR. Chiều lên tốn $N n_V (d_x + C_y)\,b$ byte. Chiều xuống gửi toàn bộ $V$ tới từng client, tốn $N$ lần chừng ấy. Tổng cộng

$$\mathrm{Cost}_V = N\,n_V\,(d_x + C_y)\,b\,(N + 1). \tag{4.1}$$

Với CIFAR-10, $d_x = 3 \times 32 \times 32 = 3072$ và $C = 10$. Lấy cấu hình pseudo-data của mã nguồn [11]: 32 mẫu cho cả hệ thống, 10 client, số thực 4 byte. Khi đó (4.1) cho khoảng 4,3 MB, trả một lần. Để so sánh, VGG11 không chuẩn hoá theo lô có khoảng 9,23 triệu tham số. Mỗi vòng truyền thông với 10 client đi rồi về mất khoảng $2 \times 10 \times 9{,}23 \times 10^6 \times 4 \approx 738$ MB. Chi phí phụ trội của mẫu trung bình vì vậy dưới 1% lưu lượng của một vòng, và chỉ trả một lần.

Với $n_V$ cố định, (4.1) không phụ thuộc $M$ hay $\lambda$: trung bình của 10 ảnh có cùng kích thước với một ảnh. Muốn đổi chi phí truyền thông thì phải đổi số mẫu trung bình.

### 4.4.2. Chi phí tính toán

Chi phí tính toán được đo, không tính theo công thức: thời gian mỗi bước cục bộ ghi trong nhật ký của từng lần chạy, quy về 1000 vòng truyền thông. Theo cấu trúc ở Bảng 4.1:
- NaiveMix gần như không tốn thêm;
- FedMix tốn thêm một lượt lan truyền ngược bậc hai để lấy gradient theo đầu vào;
- FedBR tốn thêm các lượt truyền xuôi trên pseudo-data và tầng chiếu, cùng một bước cập nhật riêng.

Số đo nằm ở Chương 5 mục 5.4.

## 4.5. Giao thức đo lường

### 4.5.1. So sánh theo cặp

Mọi mức cải thiện được tính theo cặp. Hai cấu hình đem so dùng cùng một hạt giống, và hạt giống quyết định cùng lúc lần rút phân hoạch dữ liệu, trọng số khởi tạo và thứ tự các lô. Lịch học và số vòng cũng như nhau. Với mỗi hạt giống, hiệu độ chính xác giữa hai cấu hình là một quan sát; khoảng tin cậy được tính trên các quan sát đó. Cách làm này loại khỏi phép so sánh phần phương sai do phân hoạch dữ liệu, vốn lớn trong học liên kết mô phỏng.

### 4.5.2. Chỉ so sánh trong cùng một nền tảng

Luận văn chạy thực nghiệm trên hai nền tảng. Nền tảng Flower dùng cho các thực nghiệm dưới lệch phân phối nhãn ở mục 5.2; mã nguồn [11] dùng cho các thực nghiệm còn lại của Chương 5.

**Bảng 4.2.** Hai nền tảng thực nghiệm. Tham số Dirichlet ghi theo quy ước của Chương 3.

| | Nền tảng Flower | Mã nguồn FedBR [11] |
|---|---|---|
| Client | 60, mỗi vòng chọn 15 | 10, tham gia mọi vòng |
| Backbone | VGG sửa đổi theo phụ lục của [1], không chuẩn hoá theo lô, $d = 512$ | VGG11 không chuẩn hoá theo lô, $d = 512$ |
| Lệch phân phối | nhãn: hai lớp mỗi client, hoặc Dirichlet nồng độ mỗi thành phần $\beta$ trên trục client, 60 thành phần | nhãn: Dirichlet $\alpha = 0{,}1$ nồng độ tổng trên trục lớp, kèm xoay theo client với $\alpha_{\text{rot}} = 1{,}0$ nồng độ tổng |
| Huấn luyện cục bộ | 2 epoch, lô 10 | 50 bước, lô 32 |
| Chỉ số chính | độ chính xác cao nhất theo vòng trên tập kiểm tra | trung bình năm độ chính xác cao nhất theo vòng trên phần dữ liệu giữ lại của các client |

Hai nền tảng khác nhau ở gần như mọi thành phần của thiết lập, nên con số tuyệt đối của chúng không đặt cạnh nhau được. Mọi phát biểu bắc qua hai nền tảng đặt ở mức cơ chế, dạng "hiện tượng X xuất hiện ở cả hai", chứ không ở dạng "độ chính xác tăng từ $a$ lên $b$".

### 4.5.3. Chỉ số độ chính xác

Trên mã nguồn [11], chỉ số chính là chỉ số của bài báo FedBR: trung bình năm độ chính xác cao nhất theo vòng, đo trên phần dữ liệu giữ lại của các client. Dùng chỉ số này thì bảng tái hiện so được với bảng công bố.

Chỉ số này có một nhược điểm: năm mốc được chọn theo chính độ chính xác trên tập đánh giá, nên giá trị bị kéo lên. Độ thiên tác động lên mọi phương pháp, nhưng không nhất thiết như nhau; phương pháp có đường học dao động mạnh hơn được lợi nhiều hơn. Vì vậy, với các phép so sánh thuộc họ giả thuyết chính, luận văn báo cáo kèm trung bình năm mốc đánh giá cuối cùng, một chỉ số không chọn theo tập đánh giá. Nếu hai chỉ số cho hiệu trái dấu nhau, điều đó được báo cáo cùng kết quả.

### 4.5.4. Ước lượng và cỡ mẫu

Mỗi cấu hình trong phép so sánh chính chạy với ba hạt giống. Để định cỡ, luận văn lấy độ lệch chuẩn của hiệu theo cặp là $s \approx 1{,}2$ điểm phần trăm. Trên nền tảng Flower, độ lệch chuẩn của các hiệu theo cặp ở mục 5.2 phần lớn nằm trong khoảng 0,79 đến 1,37 điểm, và 1,2 gần đầu trên của khoảng đó.

Với $n = 3$ và $t_{0{,}975;\,2} = 4{,}303$, nửa rộng khoảng tin cậy 95% của trung bình hiệu là $4{,}303 \times 1{,}2 / \sqrt{3} \approx 2{,}98$ điểm phần trăm. Một hiệu nhỏ hơn khoảng ba điểm vì vậy không phân biệt được với không, và chỉ được báo cáo dưới dạng khoảng. Khi khoảng tin cậy chứa không, luận văn nói thẳng là phép đo không phân giải được hiệu đó. Luận văn không diễn giải kết quả ấy thành bằng chứng rằng hai phương pháp tương đương, vì một kiểm định không có ý nghĩa thống kê không chứng minh giả thuyết không.

Giá trị $s$ lấy từ nền tảng Flower và chỉ dùng để định cỡ. Độ lệch chuẩn thật trên mã nguồn [11] được ước lượng từ chính ba hạt giống và báo cáo ở Chương 5.

### 4.5.5. Họ giả thuyết chính

Để kiểm soát so sánh bội, luận văn khai báo trước một họ giả thuyết chính gồm hai phép so sánh trên mã nguồn [11], ở cấu hình của Bảng 4.2 với $\lambda = 0{,}1$ (Bảng 4.3).

**Bảng 4.3.** Họ giả thuyết chính. Mỗi giả thuyết được kiểm định bằng phép kiểm định t theo cặp hai phía trên ba hạt giống; cả họ hiệu chỉnh theo thủ tục Holm ở mức 5%. FedMix dùng cách chuẩn hoá số hạng Taylor của mã phát hành (mục 4.3).

| | Giả thuyết không |
|---|---|
| H1 | $\mathrm{Acc}_{\text{FedBR}} - \mathrm{Acc}_{\text{FedAvg}} = 0$ |
| H2 | $\mathrm{Acc}_{\text{FedMix}} - \mathrm{Acc}_{\text{FedAvg}} = 0$ |

Mọi phép so sánh khác mang nhãn thăm dò và không tham gia hiệu chỉnh: FedProx, NaiveMix, FedBR + Mixup, hiệu FedMix − NaiveMix, và các thuật toán chỉ có trong bảng tái hiện một hạt giống.

### 4.5.6. Các đại lượng được ghi nhận

Trên mã nguồn [11], mỗi lần chạy ghi lại ở mỗi mốc đánh giá:
- độ chính xác trên phần dữ liệu giữ lại của từng client;
- độ chính xác trên mười tập kiểm tra xoay góc cố định;
- thời gian mỗi bước;
- toàn bộ cấu hình siêu tham số.

Nhật ký của mã nguồn này không ghi độ chính xác theo từng lớp, cũng không ghi chuẩn của các vector trọng số theo lớp. Vì vậy phân tích dạng thiên lệch của tầng phân lớp, tức mục tiêu cụ thể thứ tư, chỉ thực hiện trên nền tảng Flower, ở mục 5.2.4.
