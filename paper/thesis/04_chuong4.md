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
| 4.5 Giao thức đo lường | *(xoá tiêu đề; nội dung chuyển sang Chương 5, mục 5.1)* |

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
> Nếu sau này mã được sửa thì cập nhật mục 4.3 và Ch.5 mục 5.1.
>
> **Còn chờ học viên chốt `[QUYẾT]`:** họ giả thuyết chính, nay ở **Ch.5 mục 5.1.4**, phải chốt **trước khi chạy T0**.
>
> **Sửa 25/09 (học viên: chương chỉ trình bày đề xuất, không bàn về mã nguồn hay thiết lập thực nghiệm):**
> - mục 4.1 gộp thành một mục, không tiểu mục; bỏ hẳn mục cũ 4.1.2 "Khung trên mã nguồn FedBR"; Hình 4.1 đã vẽ (`figures/hinh4_1.png`, mã vẽ `figures/hinh4_1.py`);
> - Bảng 4.1 chuyển sang đầu mục 4.2, bỏ hàng "Mẫu trung bình trong mã nguồn";
> - bỏ mục 4.2.4 "Đọc các phép so sánh"; nội dung chuyển sang Ch.5 mục 5.1.4;
> - mục 4.3 chỉ nêu logic, không nhắc bản cài đặt nào hay của ai. Danh sách bản cài đặt và dòng mã nằm ở `INDEX_ma-nguon-va-ket-qua.md`, chỉ dùng khi hội đồng hỏi;
> - mục 4.4 gộp thành một mục, không tiểu mục;
> - **mục 4.5 chuyển toàn bộ sang Ch.5 mục 5.1** (Bảng 4.2 → Bảng 5.1, Bảng 4.3 → Bảng 5.3). Chỗ thiết lập thực nghiệm đi khác khung (NaiveMix/FedMix nhận mẫu trung bình mới mỗi bước) giờ nằm ở 5.1.1; Ch.6 vẫn phải nêu nó trong phần hạn chế.
>
> **Phát hiện mới khi viết mục 4.2.4.** Trong mã FedBR, FedMix và NaiveMix nhận 32 mẫu trung bình mới ở mỗi bước, còn FedBR dùng một tập 32 pseudo-sample cố định. Phép so FedBR với FedMix vì vậy không chỉ khác ở cách dùng mẫu trung bình. Câu tương ứng trong `01_chuong1.md` (hàng 5, *"…quy được cho cách dùng"*) nói quá; bản sửa ở khối bổ sung cuối file đó.
>
> **Tự kiểm §7.7** (thân chương):
> - không có dấu `—` chêm, không có cụm sáo, không viện dẫn đề cương hay bài hội nghị;
> - AI#1: khuôn tương phản ở mục 4.5.2 cũ đi theo sang Ch.5;
> - AI#4: một câu rào, ở mục 4.3 (*"nói về FedMix với số hạng Taylor đã bị thu nhỏ $B$ lần"*).
>
> **Thuật toán 4.1 (mục 4.1):**
> - mã giả mô tả **khung**, với $V$ dựng một lần; chỗ thiết lập thực nghiệm đi khác ghi ở Ch.5 mục 5.1.1;
> - dòng 12 chọn $S_t$ để phủ cả hai nền tảng: Flower chọn 15/60 client mỗi vòng, mã FedBR lấy cả 10 client;
> - dòng 18 chỉ ghi chú bước max của FedBR, chi tiết ở mục 3.5;
> - nếu thêm hoặc bớt dòng, sửa số "dòng 17" ở câu dẫn;
> - trong Word: đặt trong bảng một ô, phông đơn cách (Consolas), chú thích "Thuật toán 4.1" ở **phía trên**; tạo nhãn chú thích mới "Thuật toán" (References → Insert Caption → New Label).

Chương này trình bày khung học liên kết chia sẻ mẫu trung bình đại diện mà luận văn đề xuất. Khung đi qua bốn giai đoạn:
1. client tạo mẫu trung bình từ dữ liệu cục bộ;
2. máy chủ gom các mẫu ấy rồi phát lại cho mọi client;
3. client dùng mẫu trung bình trong huấn luyện cục bộ;
4. máy chủ tổng hợp tham số.

Điểm cốt lõi của khung là cách dùng mẫu trung bình ở giai đoạn thứ ba không bị cố định. Nó là một thành phần thay được, nên các phương pháp khác nhau đặt được vào cùng một khung và so được với nhau trên cùng một loại dữ liệu.

Mục 4.1 mô tả kiến trúc của khung. Mục 4.2 trình bày ba cách dùng mẫu trung bình. Mục 4.3 phân tích cách chuẩn hoá số hạng Taylor khi tính theo lô. Mục 4.4 tính chi phí tài nguyên của khung.

## 4.1. Kiến trúc khung chia sẻ mẫu trung bình

Hình 4.1 là sơ đồ của khung, gồm bốn giai đoạn đã nêu và một lớp ghi nhận bao quanh.

**Giai đoạn chuẩn bị ở client** diễn ra một lần, trước vòng truyền thông đầu tiên. Client $i$ rút ngẫu nhiên $M$ ảnh cục bộ, lấy trung bình của chúng theo (3.11) để được một ảnh trung bình, kèm nhãn mềm nếu cách dùng cần đến nhãn. Lặp lại $n_V$ lần, client có tập $V_i$ gồm $n_V$ mẫu trung bình và gửi tập này lên máy chủ. Ảnh riêng lẻ không bao giờ rời client. Tham số $M$ quyết định mức làm mịn của dữ liệu được chia sẻ: với $M = 1$, client gửi thẳng ảnh thô, còn $M$ càng lớn thì ảnh trung bình càng khó nhận ra nội dung.

**Máy chủ** gom mẫu của mọi client thành tập $V = \bigcup_i V_i$ gồm $N n_V$ phần tử, rồi phát tập đó xuống mọi client, cũng một lần. Từ đây $V$ cố định trong suốt quá trình huấn luyện.

**Trong vòng lặp huấn luyện cục bộ**, ở mỗi bước client lấy một lô $B$ ảnh của mình và $B$ phần tử của $V$, ghép với nhau theo chỉ số. Hàm mất mát được tính theo cách dùng đã chọn cho lần chạy (mục 4.2); FedAvg thì bỏ qua $V$. Sau $K$ bước, client gửi tham số lên máy chủ.

**Máy chủ tổng hợp** tham số bằng trung bình có trọng số như FedAvg [2], không thay đổi gì.

**Lớp ghi nhận** bao quanh cả bốn giai đoạn. Ở mỗi mốc đánh giá, nó ghi độ chính xác trên từng tập kiểm tra, thời gian mỗi bước, và toàn bộ cấu hình của lần chạy.

Thuật toán 4.1 tóm tắt bốn giai đoạn. Cách dùng mẫu trung bình chỉ xuất hiện ở dòng 17, qua hàm mất mát $\mathcal{L}_g$; đổi $g$ là đổi phương pháp, các dòng còn lại giữ nguyên.

**Thuật toán 4.1.** Khung học liên kết chia sẻ mẫu trung bình.

```text
Đầu vào: N client với dữ liệu cục bộ D_1, …, D_N; số vòng truyền thông T;
         số bước cục bộ K; kích thước lô B; tốc độ học η;
         số ảnh mỗi mẫu trung bình M; số mẫu trung bình mỗi client n_V;
         cách dùng g ∈ {FedAvg, NaiveMix, FedMix, FedBR}; tham số khởi tạo w_0
Đầu ra:  tham số mô hình toàn cục w_T

    ▷ Giai đoạn 1: chuẩn bị ở client (một lần)
 1: for mỗi client i = 1, …, N do
 2:     V_i ← ∅
 3:     for p = 1, …, n_V do
 4:         rút ngẫu nhiên M mẫu {(x_m, y_m)}, m = 1..M, từ D_i
 5:         x̄ ← (1/M) Σ_m x_m ;   ȳ ← (1/M) Σ_m y_m               ▷ (3.11)
 6:         V_i ← V_i ∪ {(x̄, ȳ)}                                  ▷ FedBR bỏ ȳ
 7:     end for
 8:     gửi V_i lên máy chủ
 9: end for
    ▷ Giai đoạn 2: gom và phát ở máy chủ (một lần)
10: V ← V_1 ∪ … ∪ V_N ;  gửi V tới mọi client
11: for t = 0, …, T − 1 do
12:     chọn tập client S_t tham gia vòng t
13:     for mỗi client i ∈ S_t, song song do
        ▷ Giai đoạn 3: huấn luyện cục bộ
14:         w ← w_t
15:         for k = 1, …, K do
16:             lấy lô {(x_b, y_b)}, b = 1..B, từ D_i và lô {(x̄_b, ȳ_b)}, b = 1..B, từ V
17:             ℒ ← ℒ_g(w; lô cục bộ, lô từ V)        ▷ (3.12), (3.15) hoặc (3.19); FedAvg bỏ qua V
18:             w ← w − η ∇_w ℒ                         ▷ FedBR: thêm bước cập nhật tầng chiếu
19:         end for
20:         gửi w_t^i ← w lên máy chủ
21:     end for
        ▷ Giai đoạn 4: tổng hợp ở máy chủ
22:     w_{t+1} ← Σ_{i∈S_t} ( |D_i| / Σ_{j∈S_t} |D_j| ) · w_t^i
23:     ghi độ chính xác, thời gian mỗi bước, cấu hình          ▷ lớp ghi nhận
24: end for
25: return w_T
```

![Hình 4.1](figures/hinh4_1.png)

**Hình 4.1.** Kiến trúc khung chia sẻ mẫu trung bình. Mũi tên nét đứt là trao đổi diễn ra một lần trước huấn luyện: mẫu trung bình đi lên máy chủ, tập $V$ đi xuống client. Mũi tên nét liền đậm là trao đổi tham số mô hình ở mỗi vòng truyền thông. Bộ chọn trong khối huấn luyện cục bộ quyết định mẫu trung bình được dùng theo cách nào. Số trong vòng tròn đen là bốn giai đoạn của Thuật toán 4.1; khung chấm bao ngoài là lớp ghi nhận.

## 4.2. Các cách dùng mẫu trung bình

Luận văn xét ba cách dùng mẫu trung bình ở giai đoạn huấn luyện cục bộ. Cả ba nhận cùng một loại mẫu trung bình và đứng ở cùng một vị trí trong khung; chúng khác nhau ở chỗ có dùng nhãn hay không và mẫu trung bình đi vào mục tiêu huấn luyện ở đâu. Bảng 4.1 tóm tắt các điểm này, các mục 4.2.1 đến 4.2.3 trình bày từng cách.

**Bảng 4.1.** Ba cách dùng mẫu trung bình trong khung. $x_i$ là ảnh cục bộ; $\bar x_g$ và $\bar y_g$ là ảnh trung bình và nhãn mềm theo (3.11); $u_p$ là pseudo-sample theo (3.16); $\lambda$ là trọng số trộn của NaiveMix và FedMix; $C$ là số lớp.

| | NaiveMix | FedMix | FedBR |
|---|---|---|---|
| Nhận từ các client khác | ảnh trung bình và nhãn mềm | ảnh trung bình và nhãn mềm | ảnh trung bình |
| Nhãn gắn với mẫu trung bình | nhãn mềm $\bar y_g$ | nhãn mềm $\bar y_g$ | nhãn đều $1/C$ |
| Mẫu trung bình đi vào đâu | đầu vào mô hình, trộn với ảnh cục bộ | tích vô hướng với gradient theo đầu vào | đầu ra tầng phân lớp và không gian đặc trưng |
| Mục tiêu cục bộ | (3.12) | (3.15) | (3.19) |
| Tính toán thêm mỗi bước so với FedAvg | không đáng kể | một lượt lan truyền ngược bậc hai | các lượt truyền xuôi trên pseudo-data và tầng chiếu, cùng một bước cập nhật riêng cho tầng chiếu |

### 4.2.1. Trộn trực tiếp: NaiveMix

NaiveMix thay mẫu của client khác trong global Mixup bằng mẫu trung bình, rồi dùng nguyên phép trộn (3.12). Mô hình nhìn thấy ảnh đã trộn $(1{-}\lambda)x_i + \lambda\bar x_g$, và hàm mất mát tách theo nhãn thành hai phần: phần ứng với nhãn cục bộ $y_i$ mang trọng số $1{-}\lambda$, phần ứng với nhãn mềm $\bar y_g$ mang trọng số $\lambda$. Mẫu trung bình đi qua toàn bộ mạng như một ảnh bình thường.

### 4.2.2. Qua khai triển Taylor: FedMix

FedMix xấp xỉ chính mục tiêu (3.12) bằng khai triển Taylor bậc nhất quanh ảnh cục bộ đã co tỉ lệ, rồi bỏ số hạng bậc hai của trọng số trộn, được (3.15). Mô hình chỉ nhìn thấy $(1{-}\lambda)x_i$. Ảnh trung bình đi vào mục tiêu qua tích vô hướng giữa $\bar x_g$ và gradient của hàm mất mát theo đầu vào, với hệ số $\lambda(1{-}\lambda)$; nhãn mềm đi vào qua số hạng (II). Đây là cơ chế xấp xỉ hàm mất mát bằng khai triển Taylor mà luận văn nghiên cứu, và là cách dùng mặc định của khung.

### 4.2.3. Làm điểm tựa: FedBR

FedBR bỏ nhãn của mẫu trung bình và dùng nó theo (3.19). Ở đầu ra tầng phân lớp, $L_{\text{bal}}$ kéo dự đoán trên pseudo-data về phân phối đều. Ở không gian đặc trưng, $\ell_{\text{con}}$ kéo đặc trưng cục bộ của pseudo-data về đặc trưng toàn cục của chính nó, qua một bài toán min-max với tầng chiếu. Mẫu trung bình không đi vào lượt truyền xuôi trên dữ liệu cục bộ, và không có trọng số trộn nào.

## 4.3. Chuẩn hoá số hạng Taylor

Để FedMix đúng là (3.15), cả ba số hạng phải được lấy trung bình trên lô theo cùng một cách. Cách tính theo lô thường gặp đáp ứng điều này với hai số hạng đầu, nhưng không đáp ứng với số hạng thứ ba.

Cách tính đó đi qua hai bước:
1. Số hạng thứ nhất là $(1{-}\lambda)$ nhân **trung bình** cross-entropy trên lô $B$ ảnh đã co tỉ lệ. Gradient theo đầu vào mà số hạng thứ ba cần được lấy bằng cách đạo hàm chính số hạng này, nên gradient của từng ảnh mang sẵn thừa số $(1{-}\lambda)/B$.
2. Số hạng thứ ba nhân gradient đó với $\bar x_g$, nhân thêm $\lambda$, rồi lấy trung bình trên lô, tức chia cho $B$ một lần nữa.

Thừa số $1/B$ xuất hiện hai lần. Số hạng (III) vì vậy đi vào mục tiêu với hệ số $\lambda(1{-}\lambda)/B$ thay cho $\lambda(1{-}\lambda)$. Thừa số $\lambda(1{-}\lambda)$ được tính đúng; chỗ lệch nằm ở phép chuẩn hoá theo lô.

Một phép thử số xác nhận điều này. Trên một mạng tuyến tính nhỏ, số hạng thứ ba tính theo hai bước trên được so với trung bình trên lô của số hạng (III) tính từ gradient của từng mẫu. Tỉ lệ giữa hai giá trị đúng bằng 8 khi lô có 8 ảnh và bằng 32 khi lô có 32 ảnh, tức đúng bằng $B$. Với lô 32 và lô 10 dùng ở Chương 5, số hạng Taylor vì vậy nhỏ hơn công thức lần lượt 32 và 10 lần.

Mọi kết quả FedMix trong luận văn đều dùng cách chuẩn hoá này, và mỗi bảng kết quả ghi rõ điều đó. Các kết quả ấy vì vậy nói về FedMix với số hạng Taylor đã bị thu nhỏ $B$ lần; biên độ của số hạng Taylor theo đúng (3.15) không được đo trong luận văn.

Hai yếu tố khác cũng ảnh hưởng tới cách đọc kết quả FedMix.

**Biên độ của số hạng gradient đổi theo quá trình huấn luyện.** Nó tỉ lệ với độ lớn của $\nabla_x\ell$. Một FedMix gần như trùng FedAvg có thể do số hạng không mang thông tin, cũng có thể do nó quá nhỏ ở cấu hình đang xét. Phép chuẩn hoá vừa nêu là một trường hợp cụ thể của khả năng thứ hai.

**Phép co đầu vào.** FedMix huấn luyện trên ảnh đã co $(1{-}\lambda)x_i$, trong khi mô hình được đánh giá trên ảnh gốc. Với backbone không dùng chuẩn hoá theo lô, riêng độ lệch thang này đã có thể làm đổi độ chính xác. NaiveMix không gặp vấn đề này, vì ảnh trộn giữ nguyên thang trung bình của ảnh gốc. So sánh FedMix với FedAvg hay với NaiveMix vì vậy luôn gộp cả ảnh hưởng của phép co.

## 4.4. Chi phí tài nguyên

Khung tốn thêm tài nguyên ở hai chỗ: truyền mẫu trung bình, và phần tính toán thêm của cách dùng ở giai đoạn huấn luyện cục bộ.

Theo thiết kế của khung, mẫu trung bình chỉ được truyền một lần trước vòng đầu tiên, theo hai chiều. Gọi:
- $N$ là số client, $n_V$ là số mẫu trung bình mỗi client gửi;
- $d_x$ là số giá trị của một ảnh, $C_y$ là số giá trị của nhãn đi kèm;
- $b$ là số byte mỗi giá trị.

$C_y = C$ khi nhãn mềm được gửi, như ở NaiveMix và FedMix, và $C_y = 0$ với FedBR. Chiều lên tốn $N n_V (d_x + C_y)\,b$ byte. Chiều xuống gửi toàn bộ $V$ tới từng client, tốn $N$ lần chừng ấy. Tổng cộng

$$\mathrm{Cost}_V = N\,n_V\,(d_x + C_y)\,b\,(N + 1). \tag{4.1}$$

Với CIFAR-10, $d_x = 3 \times 32 \times 32 = 3072$ và $C = 10$. Lấy cấu hình pseudo-data của [11]: 32 mẫu cho cả hệ thống, 10 client, số thực 4 byte. Khi đó (4.1) cho khoảng 4,3 MB, trả một lần. Để so sánh, VGG11 không chuẩn hoá theo lô có khoảng 9,23 triệu tham số. Mỗi vòng truyền thông với 10 client đi rồi về mất khoảng $2 \times 10 \times 9{,}23 \times 10^6 \times 4 \approx 738$ MB. Chi phí phụ trội của mẫu trung bình vì vậy dưới 1% lưu lượng của một vòng, và chỉ trả một lần.

Với $n_V$ cố định, (4.1) không phụ thuộc $M$ hay $\lambda$: trung bình của 10 ảnh có cùng kích thước với một ảnh. Muốn đổi chi phí truyền thông thì phải đổi số mẫu trung bình.

Phần tính toán thêm đã nêu ở hàng cuối Bảng 4.1. NaiveMix gần như không tốn thêm. FedMix cần thêm một lượt lan truyền ngược bậc hai để lấy gradient theo đầu vào. FedBR cần thêm các lượt truyền xuôi trên pseudo-data và tầng chiếu, cùng một bước cập nhật riêng cho tầng chiếu. Mức tốn thêm thực tế phụ thuộc phần cứng, nên luận văn đo nó bằng thời gian mỗi bước cục bộ quy về 1000 vòng truyền thông; số đo nằm ở mục 5.4.

---

# BỔ SUNG — 25/09/2026 · số trích dẫn theo danh mục Word

> Chỉ-append (Chương 4 đã có trong Word). Danh mục Word hiện đánh [1] FedMix, **[2] FedBR**, **[3] FedAvg**. Thân chương ở khối trên còn ghi FedAvg [2] và FedBR [11]; Word đã sửa FedAvg thành [3], còn một chỗ FedBR chưa sửa.

| # | Mục | Tìm trong Word | Trước | Sau |
|---|---|---|---|---|
| 1 | 4.4, đoạn ví dụ CIFAR-10 | `cấu hình pseudo-data của [11]` | Lấy cấu hình pseudo-data của [11]: | Lấy cấu hình pseudo-data của [2]: |

Ràng buộc IR#11 ở khối trạng thái đầu file đọc là "đi kèm [2]".
