# CHƯƠNG 5 — THỰC NGHIỆM (hướng B)

> **KHỐI TRẠNG THÁI** · 27/09/2026 (sửa đè, học viên cho phép)
>
> | Mục | Trạng thái | Chờ |
> |---|---|---|
> | 5.1 Thiết lập | `[ĐÃ VIẾT]` viết lại 27/09: bỏ đoạn "đi khác khung"; **bỏ mục 5.1.3 cũ** (so sánh theo cặp và số hạt giống): câu hiệu theo cặp gộp vào 5.1.2, ngưỡng đọc 3 điểm dời về 5.3.1; 5.1.4 cũ thành **5.1.3 Các phép so sánh chính** | — |
> | 5.2 Flower, lệch nhãn | `[ĐÃ VIẾT]` — mang sang từ `archive/…/05_chuong5.md` (khối 24/09) | — |
> | 5.3.1 Tái hiện bảng FedBR | `[ĐÃ VIẾT]` 26/09 — một hạt giống (12345) | — |
> | 5.3.2 So sánh các cách dùng mẫu trung bình | `[ĐÃ VIẾT]` — Bảng 5.9; **NaiveMix không chạy** (học viên 28/09: bỏ T1), hàng và đoạn FedMix − NaiveMix đã gỡ | — |
> | ~~5.3.3 Kiểm toán mã FedBR~~ | chuyển sang **Phụ lục A** (`07_phu-luc.md`), 25/09 | — |
> | **5.3.3 Mẫu trung bình còn giữ bao nhiêu thông tin cho tầng phân lớp** | `[ĐÃ VIẾT]` 26/09 — đặt thành **phép chẩn đoán**, không gọi là cách dùng thứ tư, nên Ch.4 (Bảng 4.1, Thuật toán 4.1, Hình 4.1) không phải sửa; Bảng 5.11, Hình 5.1 | — |
> | 5.4 Chi phí tài nguyên | `[ĐÃ VIẾT]` 27/09 — thêm chi phí truyền thông theo (4.1); câu nguyên nhân viết theo Bảng 4.1, nói rõ không đo tách; còn thiếu loại GPU | loại GPU |
> | **5.5 Cộng số hạng Taylor vào FedBR** | `[ĐÃ VIẾT]` 27/09 — **kết quả âm** của hướng A: (II) không tạo khác biệt, (III) ở biên độ công thức làm phân kỳ (NaN); Bảng 5.13, Hình 5.2, công thức (5.1) | kiểm tra (III)/B nếu còn thời gian |
> | 5.6 Tổng hợp và thảo luận | `[ĐÃ VIẾT]` 28/09 — bỏ câu T1 và đoạn "Giới hạn của các kết luận" (học viên) | — |
>
> **Đánh số bảng, hình, công thức (27/09, lượt 4, sau khi bỏ Bảng 5.3 cũ):** Bảng 5.1–5.2 thuộc mục 5.1; Bảng 5.3–5.7 thuộc mục 5.2; Bảng 5.8 thuộc 5.3.1; Bảng 5.9 thuộc 5.3.2; Bảng 5.10 và Hình 5.1 thuộc 5.3.3; Bảng 5.11 thuộc 5.4; Bảng 5.12, Hình 5.2 và công thức (5.1) thuộc 5.5. Hai phép so sánh chính S1/S2 viết thành câu ở 5.1.3, không còn bảng.
>
> **Quyết định 26/09 (học viên): nền tảng FedBR chỉ dùng hạt giống 12345.** Mỗi lượt FedBR 1000 vòng mất khoảng 7,5 giờ, không đủ thời gian cho ba hạt giống; **T0 bỏ**. Nền tảng Flower giữ ba hạt giống. Hệ quả trong chương này:
> - 5.1.3 viết lại: Flower dùng khoảng tin cậy trên ba hạt giống; FedBR dùng **ngưỡng đọc 3 điểm phần trăm**, lấy từ chênh lệch giữa lượt chạy lại và bảng công bố ở Bảng 5.9;
> - 5.1.4 bỏ kiểm định t và Holm (không làm được với một hạt giống); H1/H2 thành hai phép so sánh chính S1/S2 đọc theo ngưỡng;
> - 5.3.1, 5.3.2 viết xong từ `02_attempt`; 5.3.3 không còn chờ thêm hạt giống;
> - T2 (hướng A) đã có kết quả (27/09), một hạt giống, viết ở 5.5 như một **kết quả âm**. Đóng góp C4 nếu giữ thì phát biểu là phát hiện âm, không phải phương pháp cải thiện;
> - **bỏ đoạn FedBR chạy trên nền tảng Flower** ở 5.3.2 (học viên): bản cài FedBR bên kho Flower chưa được xác nhận khớp FedBR gốc, nên kết quả của nó không dùng trong luận văn.
>
> ⚠️ **Ch.1 và Ch.2 trong Word** còn vài câu nói "ba hạt giống" hoặc "khoảng tin cậy" chung cho mọi so sánh (1.2.1, 1.2.3, 1.3 đóng góp 2; 2.4.4 đóng góp 1–2). Học viên chọn không rà hai chương này ở lượt 26/09; khi rà lại thì sửa theo mục 5.1.3.
>
> **Sửa 25/09 trong thân chương:**
> - 5.2.2 bỏ câu hứa đo số hạng Taylor đúng biên độ ở 5.3.2, vì không sửa mã nên không có bản sửa;
> - 5.2.3 câu cuối trỏ sang 5.1.2 thay cho "giao thức ở Chương 4";
> - "mã nguồn FedBR" → "nền tảng FedBR" ở 5.2, 5.3 và tiêu đề 5.3;
> - 5.3.1 bỏ danh sách cấu hình, vì đã có ở Bảng 5.2;
> - 5.3.2 đổi danh sách hàng theo H1/H2;
> - 5.4 trỏ công thức (4.1), bỏ tên hàm trong mã;
> - (lượt 2) 5.3.3 chuyển sang Phụ lục A; câu Moon ở 5.3.1 trỏ sang Phụ lục A; 5.2.1 bỏ tên DevPranjal (tên chỉ còn ở bảng truy vết);
> - (lượt 2) số trích dẫn theo danh mục Word 25/09: FedBR [11] → **[2]**, CCVR [7] → **[8]**; trọng số $L_{\text{bal}}$ đổi ký hiệu thành $\gamma$ cho khớp khối sửa Ch.3.
>
> **Bốn câu của mục 5.2 đã sửa so với bản trong `archive/`** (lượt 24/09, đã thi hành trong văn bản dưới):
> 1. 5.2.2: *"Chương 4, mục 4.2.3"* → *"Chương 4, mục 4.3"*. (Vế *"được đo ở mục 5.3.2"* đã bỏ ở lượt 25/09.)
> 2. 5.2.3: câu cuối đoạn sau Bảng 5.7 không còn hứa dựng giao thức đường đặc tuyến, vì hướng B không quét ngân sách; thay bằng quy tắc *"kèm ngân sách tại đó nó được đo"*.
> 3. 5.2.4: kiểm soát kiến trúc không nằm trong kế hoạch hướng B → nói thẳng là không chạy.
> 4. 5.2.5: câu cuối trỏ sang mục 5.3 và mô tả đúng dạng lệch của nền tảng FedBR (lệch nhãn kèm xoay).
>
> **Sửa 28/09 (học viên):** bỏ T1 (NaiveMix không chạy): gỡ NaiveMix khỏi Bảng 5.2, Bảng 5.9, danh sách so sánh thăm dò ở 5.1.3 và đoạn FedMix − NaiveMix (77.4 / 81.2 / 80.6); bỏ đoạn "Giới hạn của các kết luận" ở 5.6 (các giới hạn chuyển sang Ch.6). **Định dạng số theo học viên: dấu chấm thập phân, dấu phẩy phân tách hàng nghìn cho số từ 5 chữ số** (20,000); số 4 chữ số viết liền (1000 vòng, 2000 mẫu). Đã đổi trong toàn thân Ch.5 md; Word cần đổi theo bảng rà soát 28/09 (`AUDIT_28-09.md`).
>
> **Sửa 27/09 (lượt 3), học viên: gỡ giọng rào đón toàn chương.** Bỏ mục 5.1.3 cũ (xem hàng 5.1). Các câu đã gỡ hoặc rút: 5.2 mở đầu (bỏ nhắc lại chuyện không so hai nền tảng); 5.2.1 câu kết đoạn đối chiếu; 5.2.2 câu dấu/khoảng tin cậy viết lại, câu "không khảo sát nhánh bậc hai vì phạm vi, không phải vì…"; 5.2.3 bỏ thuật ngữ "đường đặc tuyến"; 5.2.4 câu cuối rút còn phạm vi backbone; 5.2.5 đổi tên thành "Tóm tắt"; 5.3.1 ngưỡng đọc chuyển về đây; 5.3.2 bỏ "hai nền tảng không mâu thuẫn ở mức cơ chế"; 5.3.3 bỏ "trả lời một phần RQ3" (RQ không có trong thân bài), câu "đây là suy luận…" đổi thành "một cách giải thích"; 5.4 bỏ "không đo tách riêng"; 5.5 bỏ đoạn kết lặp ý và câu "chưa thử λ nhỏ hơn" (sang Ch.6); 5.6 bỏ câu dẫn "mỗi phát biểu nêu kèm điều kiện". Số liệu, bảng, hình không đổi.
>
> **Sửa 27/09 (lượt 2):** 5.1 viết lại theo góp ý của học viên (giọng rào đón, đoạn "đi khác khung" gây mâu thuẫn với Ch.4). Nội dung giữ nguyên: Bảng 5.1–5.3, ngưỡng đọc 3 điểm, S1/S2, hai đoạn cách đọc phép so sánh thăm dò; Bảng 5.3 bỏ cột "Cách đọc" vì quy tắc đã ở 5.1.3.
>
> **Sửa 27/09:** viết 5.5 (kết quả âm của hướng A) và 5.6; 5.4 thêm chi phí truyền thông, bỏ hai ghi chú ⚠️ (câu nguyên nhân viết lại theo Bảng 4.1, lý do không dùng cột bộ nhớ chuyển vào bảng truy vết); 5.2.2 câu cuối trỏ sang 5.5 vì số hạng Taylor ở biên độ công thức giờ đã được thử; 5.2.5 bỏ cụm "như đang được cài đặt"; Hình 5.1 đổi nhãn trục "local".
>
> **Trích dẫn (28/09):** danh mục Word đã đánh lại sau khi thêm MOON: [1] Zhao · [2] FedMix · [3] FedBR · [4] FedAvg · [10] CCVR. Thân md đã đổi theo ([1]→[2], [2]→[3], [8]→[10]).
>
> ⛔ **IR#10:** mục nào chưa có dữ liệu thì để `[CHỜ SỐ LIỆU: <mức>]`, không điền số dự kiến.

**Ánh xạ sang Word.** Word hiện có hai tiêu đề: *5.1 Thiết lập thực nghiệm* và *5.2 Tái hiện và kiểm toán tính tái lập*. Đổi thành:

| Word hiện tại | Sau khi sửa |
|---|---|
| 5.1 Thiết lập thực nghiệm | 5.1 Thiết lập thực nghiệm (giữ; thêm 5.1.1–5.1.3) |
| — | **5.2 Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower** (chèn, cùng 5.2.1–5.2.5) |
| 5.2 Tái hiện và kiểm toán tính tái lập | **5.3 So sánh các cách dùng mẫu trung bình trên nền tảng FedBR** (đổi tên; 5.3.1 Tái hiện · 5.3.2 So sánh) |
| — | **Phụ lục A. Kiểm toán mã nguồn FedBR** (chèn sau Tài liệu tham khảo; nội dung ở `07_phu-luc.md`) |
| — | 5.4 Chi phí tài nguyên · **5.5 Cộng số hạng Taylor vào FedBR** (5.5.1–5.5.3) · 5.6 Tổng hợp và thảo luận (chèn) |

---

## 5.1. Thiết lập thực nghiệm

Thực nghiệm chạy trên hai nền tảng. Nền tảng Flower dùng cho các thí nghiệm dưới lệch phân phối nhãn ở mục 5.2. Các thí nghiệm còn lại chạy trên bộ thực nghiệm công bố cùng bài báo FedBR [3], gọi tắt là nền tảng FedBR.

### 5.1.1. Hai nền tảng thực nghiệm

**Bảng 5.1.** Hai nền tảng thực nghiệm. Tham số Dirichlet ghi theo quy ước của Chương 3.

| | Nền tảng Flower | Nền tảng FedBR [3] |
|---|---|---|
| Client | 60, mỗi vòng chọn 15 | 10, tham gia mọi vòng |
| Backbone | VGG sửa đổi theo phụ lục của [2], không chuẩn hoá theo lô, $d = 512$ | VGG11 không chuẩn hoá theo lô, $d = 512$ |
| Lệch phân phối | nhãn: hai lớp mỗi client, hoặc Dirichlet nồng độ mỗi thành phần $\beta$ trên trục client, 60 thành phần | nhãn: Dirichlet $\alpha = 0.1$ nồng độ tổng trên trục lớp, kèm xoay theo client với $\alpha_{\text{rot}} = 1.0$ nồng độ tổng |
| Huấn luyện cục bộ | 2 epoch, lô 10 | 50 bước, lô 32 |
| Chỉ số chính | độ chính xác cao nhất theo vòng trên tập kiểm tra | trung bình năm độ chính xác cao nhất theo vòng trên phần dữ liệu giữ lại của các client |

Hai nền tảng khác nhau ở số client, backbone, cách phân hoạch và chỉ số, nên chương chỉ so sánh trong cùng một nền tảng. Giữa hai nền tảng, chương chỉ đối chiếu hiện tượng, không đối chiếu con số.

Bảng 5.2 ghi cấu hình của nền tảng FedBR, lấy theo bài báo [3].

**Bảng 5.2.** Cấu hình thực nghiệm trên nền tảng FedBR.

| Thành phần | Giá trị |
|---|---|
| Dữ liệu | CIFAR-10 xoay, 10 client; lệch phân phối như Bảng 5.1; 20% dữ liệu của mỗi client được giữ lại để đánh giá |
| Huấn luyện | 1000 vòng, mỗi vòng 50 bước cục bộ, lô 32; SGD tốc độ học 0.01, không momentum, không weight decay; tăng cường dữ liệu mặc định của nền tảng |
| Backbone | VGG11 không chuẩn hoá theo lô, $d = 512$ |
| Đánh giá | mỗi 5 vòng |
| FedMix | $\lambda = 0.1$; mỗi bước cục bộ lấy một lô 32 mẫu trung bình mới, mỗi mẫu là trung bình của 10 ảnh; FedMix chuẩn hoá số hạng Taylor theo cách nêu ở Chương 4, mục 4.3 |
| FedBR | 32 pseudo-sample cố định, dựng trước huấn luyện, mỗi mẫu là trung bình của 10 ảnh; $\tau_1 = \tau_2 = 2$, $\mu = 0.5$, $\gamma = 1.0$; tầng chiếu là MLP $d \to 2d \to d$ |
| Hạt giống | 12345, cho mọi thuật toán |

Cách lấy mẫu trung bình của FedMix giữ đúng như [3], để bảng tái hiện ở mục 5.3.1 so được với bảng công bố.

### 5.1.2. Chỉ số và các đại lượng được ghi nhận

Trên nền tảng FedBR, chỉ số chính là chỉ số của bài báo FedBR: trung bình năm độ chính xác cao nhất theo vòng, đo trên phần dữ liệu giữ lại của các client. Năm mốc này được chọn theo chính tập đánh giá nên chỉ số thiên lên một chút, và thiên nhiều hơn với phương pháp có đường học dao động. Các phép so sánh chính vì vậy báo cáo thêm trung bình năm mốc đánh giá cuối.

Mỗi mốc đánh giá ghi độ chính xác trên phần dữ liệu giữ lại của từng client, độ chính xác trên mười tập kiểm tra xoay góc cố định, và thời gian mỗi bước. Nhật ký không có độ chính xác theo lớp hay chuẩn của các vector trọng số theo lớp, nên phân tích dạng thiên lệch của tầng phân lớp ở mục 5.2.4 chỉ làm trên nền tảng Flower.

Mọi mức cải thiện trong chương là hiệu theo cặp: hai cấu hình đem so dùng cùng một hạt giống, nên có cùng phân hoạch dữ liệu, cùng trọng số khởi tạo và cùng thứ tự các lô. Với phương pháp có tham số ngân sách, như số đặc trưng ảo mỗi lớp của CCVR, mỗi con số đi kèm ngân sách tại đó nó được đo; mục 5.2.3 cho thấy vì sao.

### 5.1.3. Các phép so sánh chính

Trên nền tảng FedBR, chương xét hai phép so sánh chính: hiệu theo cặp giữa FedBR và FedAvg, gọi là S1, và giữa FedMix và FedAvg, gọi là S2. FedMix dùng $\lambda = 0.1$, giá trị mặc định của [3], và cách chuẩn hoá số hạng Taylor nêu ở Chương 4, mục 4.3. Các phép so sánh khác là thăm dò: FedProx, FedAvg + Mixup và FedBR + Mixup.

Hiệu FedBR − FedMix là hiệu giữa hai phương pháp hoàn chỉnh. Ngoài cách dùng mẫu trung bình, hai phương pháp còn khác nhau ở cách lấy mẫu trung bình (Bảng 5.2), tầng chiếu và bộ siêu tham số.

---

## 5.2. Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower

Mục này đo ba điều dưới lệch phân phối nhãn: FedMix có cải thiện so với FedAvg hay không; mức cải thiện của nhóm hiệu chuẩn tầng phân lớp từ thống kê lớp phụ thuộc thế nào vào ngân sách mẫu ảo; và thiên lệch của tầng phân lớp nằm ở độ lớn hay ở hướng. Mô hình được huấn luyện từ đầu trên nền tảng Flower.

### 5.2.1. Thiết lập

**Bảng 5.3.** Thiết lập thực nghiệm trên nền tảng Flower. $\beta$ là nồng độ Dirichlet **mỗi thành phần**, lấy mẫu trên trục **client** cho từng lớp, với 60 thành phần ứng với 60 client; nồng độ càng nhỏ thì lệch càng nặng. $M_c$ là số đặc trưng ảo sinh cho mỗi lớp khi huấn luyện lại tầng phân lớp; $d$ là số chiều đặc trưng.

| Thành phần | Giá trị |
|---|---|
| Khung | Flower, chế độ mô phỏng |
| Dữ liệu | CIFAR-10; CINIC-10 chỉ dùng cho phép so sánh các head hiệu chuẩn |
| Client | 60, mỗi vòng chọn 15 |
| Huấn luyện cục bộ | 2 epoch, lô 10, SGD với tốc độ học 0.01 giảm theo hệ số 0.999 mỗi vòng, không momentum, không weight decay |
| Backbone | VGG sửa đổi theo phụ lục bài báo FedMix [2]: 6 tầng tích chập và 3 tầng kết nối đầy đủ, không chuẩn hoá theo lô, $d = 512$ |
| Phân hoạch | hai lớp mỗi client, 500 vòng (phép so sánh FedMix); Dirichlet $\beta \in \{0.05, 0.1, 0.3\}$, 150 vòng (hiệu chuẩn tầng phân lớp) |
| FedMix | $\lambda = 0.05$; mỗi client gửi một ảnh trung bình của toàn bộ dữ liệu cục bộ kèm nhãn mềm; mỗi lô cục bộ ghép với một ảnh trung bình rút ngẫu nhiên |
| Hiệu chuẩn | CCVR [10] với $M_c \in \{100, 2000\}$, biến đổi Tukey 0.5, huấn luyện lại tầng cuối 10 epoch; head LDA dùng hiệp phương sai gộp co về đường chéo với hệ số 0.01 |
| Hạt giống | 42, 43, 44 |

Chỉ số của phép so sánh FedMix là độ chính xác cao nhất theo vòng trên tập kiểm tra. Chỉ số của phép hiệu chuẩn là chênh lệch độ chính xác trước và sau khi hiệu chuẩn, đo trên cùng một mô hình đã huấn luyện. Mọi dấu $\pm$ trong mục này là độ lệch chuẩn mẫu của ba hiệu theo cặp, mỗi hiệu ứng với một hạt giống.

Bài báo FedMix không công bố mã nguồn. Nền tảng được đối chiếu với một bản cài đặt FedMix công khai khác, trên cùng cấu hình, hạt giống 42. Độ chính xác tuyệt đối của hai bên chênh khoảng 3 điểm phần trăm (FedAvg 65.81% so với 68.69%; FedMix 63.67% so với 66.50%), nhưng hiệu theo cặp gần như trùng: −2.14 và −2.19 điểm. Bản cài đặt đó cũng là mốc dùng để hiệu chỉnh nền tảng, nên phép đối chiếu này chỉ là một kiểm tra tính nhất quán.

### 5.2.2. FedMix so với FedAvg

**Bảng 5.4.** Độ chính xác cao nhất theo vòng (%) của FedAvg và FedMix trên CIFAR-10, phân hoạch hai lớp mỗi client, 500 vòng, backbone VGG không chuẩn hoá ($d = 512$), $\lambda = 0.05$. Cột cuối là hiệu theo cặp FedMix − FedAvg, đơn vị điểm phần trăm. Hàng cuối: trung bình ± độ lệch chuẩn mẫu, $n = 3$.

| Hạt giống | FedAvg | FedMix | Hiệu |
|---|---|---|---|
| 42 | 68.69 | 66.50 | −2.19 |
| 43 | 67.42 | 66.47 | −0.95 |
| 44 | 64.74 | 62.31 | −2.43 |
| | | | **−1.86 ± 0.79** |

FedMix kém FedAvg ở cả ba hạt giống. Cận trên của khoảng tin cậy 95% một phía, với $t_{0.95;\,2} = 2.920$, là −0.52 điểm, nên ở cấu hình này có thể loại trừ khả năng FedMix cải thiện. Riêng dấu của ba hiệu thì chưa đủ làm bằng chứng: khi không có hiệu ứng, ba hiệu vẫn cùng dấu với xác suất 0.25.

Lấy độ chính xác ở vòng cuối thay cho vòng tốt nhất, ba hiệu là −3.55, −4.49 và +0.59: trung bình vẫn âm nhưng một hạt giống đổi dấu.

Nền tảng này tính số hạng Taylor theo cách nêu ở mục 4.3; với lô 10 ảnh, số hạng nhỏ hơn công thức (3.15) mười lần. Mục 5.5 thử số hạng này ở đúng biên độ công thức.

Nền tảng Flower cũng đo được biên độ của số hạng bậc hai trong khai triển Taylor so với số hạng bậc nhất, ở $\lambda = 0.05$. Tại khởi tạo ngẫu nhiên, trên 10 ảnh CIFAR-10, tỉ số là khoảng $1.3 \times 10^{-4}$. Trên ba mô hình đã huấn luyện 150 vòng với Dirichlet $\beta = 0.05$, tỉ số là 0.039, 0.224 và 0.025 theo từng hạt giống, tức lớn lên hai đến ba bậc khi mô hình được huấn luyện. Luận văn không khảo sát nhánh bậc hai.

**Bảng 5.5.** Hai biến thể thăm dò của FedMix. C1: mỗi client gửi một ảnh trung bình cho từng lớp, thay cho một ảnh trung bình trên toàn bộ dữ liệu cục bộ. C1+C2: C1 cộng thêm quy tắc ghép cặp chọn ảnh trung bình khác lớp có tích vô hướng với gradient theo đầu vào lớn nhất. Hiệu theo cặp so với FedAvg, trung bình ± độ lệch chuẩn mẫu, $n = 3$, đơn vị điểm phần trăm; cột cuối là cận trên của khoảng tin cậy 95% một phía.

| Biến thể | Phân hoạch, số vòng | Hiệu theo hạt giống | Trung bình | Cận trên |
|---|---|---|---|---|
| C1 | hai lớp mỗi client, 500 | −2.22 / −0.55 / −2.94 | −1.90 ± 1.23 | +0.16 |
| C1+C2 | Dirichlet $\beta = 0.3$, 150 | −1.36 / −2.95 / −0.60 | −1.64 ± 1.20 | +0.38 |

Cả hai biến thể âm về trung bình, nhưng cận trên đều dương nên chưa loại trừ được khả năng cải thiện. Hai biến thể này chỉ là thăm dò.

### 5.2.3. Hiệu chuẩn tầng phân lớp và ngân sách mẫu ảo

CCVR ước lượng trung bình và hiệp phương sai của đặc trưng theo từng lớp, sinh đặc trưng ảo từ các phân phối Gauss đó, rồi huấn luyện lại riêng tầng phân lớp. Số đặc trưng ảo mỗi lớp, $M_c$, là ngân sách của phương pháp.

**Bảng 5.6.** Mức chênh độ chính xác của CCVR so với mô hình trước hiệu chuẩn, trên CIFAR-10, 150 vòng, theo ngân sách mẫu ảo $M_c$ và nồng độ Dirichlet $\beta$ (quy ước ở Bảng 5.3). Hàng $\beta = 0.05$ gồm ba hạt giống (+3.88 / +4.30 / +4.90); các hàng còn lại chỉ có hạt giống 42. Đơn vị: điểm phần trăm.

| $M_c$ | $\beta$ | Mức chênh |
|---|---|---|
| 100 | 0.1 | +0.29 |
| 100 | 0.3 | −0.76 |
| 2000 | 0.1 | +0.97 |
| 2000 | 0.05 | +4.36 ± 0.51 |

Ở ngân sách 100 mẫu mỗi lớp, CCVR cải thiện mô hình ở $\beta = 0.1$ nhưng làm mô hình kém đi ở $\beta = 0.3$: cùng một phương pháp, hai dấu ngược nhau. Hai hàng $M_c = 100$ và hai hàng $M_c = 2000$ không so trực tiếp được với nhau, vì chúng dùng hai lần huấn luyện backbone khác nhau và tốc độ học của bước huấn luyện lại cũng đổi từ 0.01 sang 0.001. Một con số đo ở một ngân sách vì vậy không mô tả được phương pháp, và luận văn luôn ghi ngân sách đi kèm.

**Bảng 5.7.** Bốn cách huấn luyện lại tầng phân lớp từ cùng một thống kê lớp, trên cùng mô hình đã huấn luyện 150 vòng với Dirichlet $\beta = 0.05$, $M_c = 2000$, $d = 512$, tức $M_c/d \approx 3.9$. Hiệu so với mô hình trước hiệu chuẩn, trung bình ± độ lệch chuẩn mẫu, $n = 3$; độ chính xác trước hiệu chuẩn là 54.66 / 54.55 / 48.14%. Hàng "hội tụ" và dòng "LDA − Newton" lấy từ một lượt chạy riêng trên cùng ba hạt giống, trong đó LDA đạt +6.39 ± 1.24. CINIC-10 chứa ảnh của CIFAR-10, nên cột CINIC-10 chỉ để đọc mô tả, không dùng để suy luận thống kê. Đơn vị: điểm phần trăm.

| Head | CIFAR-10 | CINIC-10 |
|---|---|---|
| LDA dạng đóng | +6.45 ± 1.29 | +5.93 ± 0.33 |
| CCVR | +4.41 ± 1.19 | +4.26 ± 0.12 |
| Newton cross-entropy, một bước | +2.98 ± 1.04 | +1.95 ± 3.17 |
| Bậc nhất, một bước | +0.36 ± 0.12 | +0.24 ± 0.08 |
| Newton cross-entropy, hội tụ | +6.14 ± 1.37 | +5.65 ± 0.28 |
| Bậc nhất tốt nhất (tốc độ học 0.1, 2000 bước) | +5.29 ± 1.09 | +5.32 ± 0.29 |
| **LDA − Newton hội tụ** | **+0.25 ± 0.18** | **+0.35 ± 0.06** |

Thứ hạng khớp với dự đoán của Chương 3. Trên tác vụ ảo sinh từ phân phối Gauss, head LDA dạng đóng cho mức cải thiện cao nhất. Các head phân biệt, khi được tối ưu tới hội tụ, tiến sát LDA nhưng vẫn thấp hơn ở cả ba hạt giống trên CIFAR-10 (0.31 / 0.39 / 0.05 điểm). Phép đo ở $M_c/d \approx 3.9$, tức chế độ mẫu hữu hạn.

### 5.2.4. Dạng thiên lệch của tầng phân lớp

Hai giả thuyết của Chương 3 được kiểm tra trên ba mô hình của hàng $\beta = 0.05$, $M_c = 2000$ ở Bảng 5.6, trước và sau khi hiệu chuẩn bằng CCVR.

Tỉ số giữa chuẩn $\ell_2$ lớn nhất và nhỏ nhất của các vector trọng số theo lớp ở tầng cuối là 1.099, 1.147 và 1.172 theo từng hạt giống, tức các chuẩn gần như bằng nhau. Độ lệch ở số hạng tự do cũng nhỏ: trung bình trị tuyệt đối của $b_c$ khoảng 0.16, so với chuẩn trung bình của $w_c$ khoảng 1.17. Trong khi đó, hiệu chuẩn lại tầng cuối nâng recall của lớp kém nhất từ 18.0% lên 61.9% (lớp tàu thuỷ, hạt giống 42), từ 16.9% lên 61.8% (lớp chó, hạt giống 43), và từ 22.3% lên 48.6% (lớp hươu, hạt giống 44). Lớp kém nhất được xác định sau khi đo, riêng cho từng hạt giống.

Một chênh lệch chuẩn dưới 20% không thể tạo ra biến thiên recall cỡ 26 đến 45 điểm nếu thiên lệch nằm ở độ lớn. Số đo vì vậy ủng hộ giả thuyết thứ hai: thiên lệch nằm ở hướng của ranh giới quyết định, và hiệu chuẩn xoay ranh giới ấy. Phép đo này làm trên backbone không dùng chuẩn hoá theo lô.

### 5.2.5. Tóm tắt

Mục 5.2 cho ba kết quả. Dưới lệch phân phối nhãn, FedMix không cải thiện so với FedAvg. Mức cải thiện của nhóm hiệu chuẩn tầng phân lớp phụ thuộc ngân sách mẫu ảo và có thể đổi dấu. Thiên lệch của tầng phân lớp nằm ở hướng. Mục 5.3 chuyển sang nền tảng FedBR, nơi lệch nhãn đi kèm lệch đặc trưng do phép xoay.

---

## Truy vết — không chép vào Word

Gốc đường dẫn: `C:\Users\KietVu\Testplace\uit-msc-dp-adaptive-fedmix\`. Tra thêm ở `INDEX_ma-nguon-va-ket-qua.md` §3.

| Bảng / số liệu | Tệp thô | Tái tính |
|---|---|---|
| Bảng 5.3 | `configs/cifar10/paper_k2.yaml`, `configs/cifar10/fedmix.yaml`, `configs/cifar10/dirichlet_sweep/ccvr_b005_paperhp.yaml`, `runs/runs/e2/config_resolved.yaml` | — |
| Đối chiếu bản cài đặt FedMix khác (DevPranjal; tên không đưa vào Word) | `runs/_archive/hydra_reference/results/cifar10_{0.1}/`; `docs/reproductions/REPRODUCTION_CIFAR10_GATE.md:57–69` | — |
| Bảng 5.4 | `runs/_archive/fedmca_closed/negative_k2/{fedavg,fedmix}_cifar10_k2{,_s43,_s44}/<ts>/metrics.csv`; timestamp đúng ở chỉ mục §3 | `python -m scripts.aggregate_negatives_k2 --log-root runs/_archive/fedmca_closed/negative_k2` |
| Cận trên −0.52 / +0.16 / +0.38 | tính từ các hiệu theo hạt giống, $t_{0.95;2} = 2.920$ | chỉ mục F2 |
| Số hạng bậc hai tại khởi tạo | `docs/reproductions/REPRODUCTION_FEDMCA_C1_GATE.md:55` | `scripts/check_t2_magnitude.py` |
| Số hạng bậc hai trên mô hình đã huấn luyện (0.039 / 0.224 / 0.025) | `runs/gate_2nd/second_order_gate.json`, trường `trained.seed4x.m1.ratio_B_over_A` | `experiments/run_second_order_gate.py` |
| Bảng 5.5 | C1: `negative_k2/fedmca_c1_cifa10_k2` (s42), `fedmca_c1_cifar10_k2_{s43,s44}`; C1+C2: `runs/fedtc/*_b030_screen` (s42), `runs/_archive/fedmca_closed/*_screen_s43/s44` | C1: script trên; C1+C2: tự tính từ `metrics.csv` |
| Bảng 5.6 | $M_c=100$: `runs/_archive/void_superseded/fedtc4/ccvr_cifar10_dir_b0{10.30}_screen/`; $M_c=2000$: `runs/fedtc5/ccvr_b010_paperhp`, `runs/fedtc5/ccvr_b005_paperhp{,_s43,_s44}` (`calibration_metrics.json`) | `scripts/make_paper_figures.py` `make_fig1` |
| Bảng 5.7 | `runs/runs/e2/head_methods_summary.json`, `runs/runs/e2_cinic/…`; hàng hội tụ: `runs/runs/e3/e3_fair_baselines.json`, `runs/runs/e3_cinic/…` | `experiments/run_head_methods.py`, `experiments/run_e3_fair_baselines.py` |
| Mục 5.2.4 | `runs/fedtc5/ccvr_b005_paperhp*/calibration_metrics.json`: `head_weight_l2_before`, `recall_before`, `recall_after`, `head_bias_before` | `make_paper_figures.py` `make_fig2` |

⚠️ **Ba điểm cần biết khi bảo vệ:**
- Hàng $M_c = 100$ của Bảng 5.6 nằm trong thư mục `void_superseded`: đây là các lượt screen cũ, được giữ vì là lượt duy nhất ở ngân sách đó.
- Mục 5.2.3 nói thẳng rằng ngân sách và tốc độ học huấn luyện lại đổi cùng lúc giữa hai nhóm hàng. Không viết lại theo kiểu "trên cùng một checkpoint" (chỉ mục F6).
- Chỉ số "tỉ số bậc hai / bậc nhất trên mô hình đã huấn luyện" lấy nhánh Hessian (`ratio_B_over_A`). Không dùng các tỉ số có hậu tố `_gn`, vì chúng chuẩn hoá không nhất quán (chỉ mục F4).

---

## 5.3. So sánh các cách dùng mẫu trung bình trên nền tảng FedBR

### 5.3.1. Tái hiện bảng CIFAR-10 của FedBR

Bảng 5.8 đặt kết quả chạy lại trên nền tảng FedBR cạnh bảng CIFAR-10 của bài báo FedBR [3]. Cấu hình theo Bảng 5.2, chỉ số theo mục 5.1.2.

**Bảng 5.8.** Độ chính xác (%) trên CIFAR-10 xoay, 10 client, 1000 vòng, VGG11 không chuẩn hoá ($d = 512$). Cột thứ hai là giá trị công bố trong Bảng 1 của [3]; cột thứ ba là lượt chạy lại trên nền tảng FedBR với hạt giống 12345. Chỉ số của cả hai cột là trung bình năm độ chính xác cao nhất theo vòng trên phần dữ liệu giữ lại của các client. FedMix chạy với $\lambda = 0.1$ và cách chuẩn hoá ở Chương 4, mục 4.3, tức số hạng Taylor nhỏ hơn (3.15) 32 lần.

| Thuật toán | Công bố [3] | Chạy lại | Chênh |
|---|---|---|---|
| FedAvg | 58.99 | 59.45 | +0.46 |
| FedProx | 59.14 | 59.14 | 0.00 |
| Moon | 58.23 | 52.95 | −5.28 |
| DANN | 58.29 | 55.60 | −2.69 |
| GroupDRO | 56.57 | 59.23 | +2.66 |
| FedBR | 64.65 | 65.82 | +1.17 |
| FedAvg + Mixup | 58.57 | 59.44 | +0.87 |
| FedMix | 57.37 | 57.16 | −0.21 |
| FedBR + Mixup | 65.32 | 66.47 | +1.15 |

Sáu trong chín thuật toán cách giá trị công bố không quá 1.2 điểm. Moon thấp hơn 5.28 điểm; thuật toán này mang một lỗi nêu ở Phụ lục A: mô hình cục bộ của vòng trước, thứ mà hàm mất mát tương phản của Moon cần, không bao giờ được cập nhật. DANN thấp hơn 2.69 điểm và GroupDRO cao hơn 2.66 điểm; luận văn không tìm nguyên nhân của hai chênh lệch này.

Bảng 5.8 cũng cho biết hai lần chạy cùng một cấu hình có thể cách nhau bao xa: bỏ Moon, lượt chạy lại lệch bảng công bố từ −2.69 đến +2.66 điểm. Trên nền tảng FedBR, mỗi thuật toán chỉ chạy một lần, với hạt giống 12345, vì một lượt FedBR 1000 vòng đã mất khoảng 7.5 giờ (Bảng 5.11). Các hiệu trên nền tảng này vì vậy được đọc bằng một **ngưỡng đọc 3 điểm phần trăm**: hiệu nhỏ hơn mức đó coi là không phân biệt được.

### 5.3.2. Các cách dùng mẫu trung bình

Bảng 5.9 đặt các cách dùng mẫu trung bình cạnh FedAvg và FedProx, trên cùng lượt chạy của Bảng 5.8.

**Bảng 5.9.** Hiệu theo cặp so với FedAvg trên nền tảng FedBR (CIFAR-10 xoay, 10 client, 1000 vòng, VGG11 không chuẩn hoá, $d = 512$), hạt giống 12345. "Chỉ số chính" là trung bình năm độ chính xác cao nhất theo vòng; "năm mốc cuối" là trung bình năm mốc đánh giá cuối cùng; cả hai đo trên phần dữ liệu giữ lại của các client, đơn vị %. FedMix dùng $\lambda = 0.1$ và cách chuẩn hoá ở Chương 4, mục 4.3, tức số hạng Taylor nhỏ hơn (3.15) 32 lần. Ngưỡng đọc 3 điểm theo mục 5.3.1.

| Thuật toán | Chỉ số chính | Hiệu | Năm mốc cuối | Hiệu |
|---|---|---|---|---|
| FedAvg | 59.45 | — | 57.70 | — |
| FedProx | 59.14 | −0.31 | 57.79 | +0.09 |
| FedAvg + Mixup | 59.44 | −0.01 | 59.08 | +1.38 |
| FedMix (S2) | 57.16 | −2.29 | 57.12 | −0.58 |
| FedBR (S1) | 65.82 | +6.37 | 65.05 | +7.35 |
| FedBR + Mixup | 66.47 | +7.02 | 65.88 | +8.18 |

S1 vượt ngưỡng đọc ở cả hai chỉ số: FedBR hơn FedAvg 6.37 điểm theo chỉ số chính và 7.35 điểm theo năm mốc cuối. Bảng 1 của [3] cho FedBR hơn FedAvg 5.66 điểm, cùng chiều và cùng cỡ. FedBR + Mixup cho hiệu cùng cỡ với FedBR.

S2 nằm dưới ngưỡng. FedMix kém FedAvg 2.29 điểm theo chỉ số chính ([3] báo cáo kém 1.62 điểm) và 0.58 điểm theo năm mốc cuối. Hiệu co lại vì đường học của FedAvg lên đỉnh cao hơn rồi giảm dần về cuối, còn đường của FedMix gần như phẳng. Cả hai chỉ số đều không cho thấy FedMix cải thiện, cùng chiều với kết quả trên nền tảng Flower ở mục 5.2.2.


### 5.3.3. Mẫu trung bình còn giữ bao nhiêu thông tin cho tầng phân lớp

Mục 5.2.3 cho thấy, trên nền tảng Flower, huấn luyện lại tầng phân lớp trên thống kê đặc trưng toàn cục là can thiệp cho mức cải thiện lớn nhất. Mục này dùng chính can thiệp đó làm phép đo: huấn luyện lại tầng phân lớp trên mẫu trung bình thì mô hình được lợi hay bị hại, và điều đó đổi thế nào theo số ảnh $M$ gộp trong mỗi mẫu. Câu trả lời cho biết mẫu trung bình còn giữ bao nhiêu thông tin về ranh giới giữa các lớp.

Thủ tục như sau. Lấy mô hình toàn cục ở vòng cuối của mỗi thuật toán trong Bảng 5.8 và đóng băng bộ trích xuất đặc trưng $\phi$. Mỗi client dựng 2000 mẫu trung bình theo (3.11), mỗi mẫu gộp $M$ ảnh rút ngẫu nhiên từ dữ liệu huấn luyện của client đó, kèm nhãn mềm là histogram nhãn của $M$ ảnh ấy. Máy chủ tính đặc trưng $\phi(\bar x)$ của 20,000 mẫu, rồi thay tầng phân lớp $\omega$ bằng bộ phân lớp LDA dạng đóng như ở mục 5.2.3: trung bình theo lớp lấy trọng số theo nhãn mềm, một ma trận hiệp phương sai chung co về $(\mathrm{tr}/d)\,I$ với hệ số 0.01, tiên nghiệm đều. Độ chính xác được đo trên phần dữ liệu giữ lại của các client, trước và sau khi thay tầng phân lớp. $M$ quét trên $\{1, 2, 3, 5, 10\}$; $M = 1$ là trường hợp chia sẻ ảnh thô, còn $M = 10$ là giá trị mà FedMix và FedBR dùng trong Bảng 5.2.

Theo (4.1), chiều lên với $N = 10$, $n_V = 2000$, $d_x = 3072$, $C_y = 10$ và 4 byte mỗi giá trị là khoảng 247 MB, trả một lần. Máy chủ tự huấn luyện lại tầng phân lớp nên mẫu trung bình không phải phát lại cho client. Con số này vẫn nhỏ hơn lưu lượng một vòng truyền thông, khoảng 738 MB.

**Bảng 5.10.** Mức thay đổi độ chính xác trên phần dữ liệu giữ lại (điểm phần trăm) khi thay tầng phân lớp của mô hình vòng cuối bằng bộ phân lớp LDA huấn luyện trên 2000 mẫu trung bình mỗi client, theo số ảnh mỗi mẫu $M$. Cột "Trước" là độ chính xác của mô hình vòng cuối trên cùng tập, hạt giống 12345; giá trị này khác cột "Chạy lại" của Bảng 5.8, vốn là trung bình năm vòng cao nhất. Moon mang lỗi nêu ở Phụ lục A, nên hàng của nó chỉ để tham khảo.

| Thuật toán | Trước | $M=1$ | $M=2$ | $M=3$ | $M=5$ | $M=10$ |
|---|---|---|---|---|---|---|
| FedAvg | 55.98 | +5.83 | +3.27 | −1.60 | −7.81 | −16.39 |
| FedProx | 56.94 | +4.12 | +1.97 | −2.46 | −9.24 | −16.51 |
| GroupDRO | 57.54 | +3.94 | +2.09 | −1.33 | −6.73 | −14.12 |
| DANN | 55.14 | +4.52 | +1.85 | −2.34 | −8.47 | −14.02 |
| FedAvg + Mixup | 59.83 | +1.03 | −0.16 | −3.66 | −8.59 | −13.89 |
| FedMix | 57.21 | +4.84 | +2.51 | −3.38 | −12.48 | −25.33 |
| FedBR | 65.92 | +1.34 | −0.19 | −6.02 | −17.58 | −54.46 |
| FedBR + Mixup | 65.64 | +1.73 | +0.96 | −2.64 | −12.30 | −46.23 |
| Moon | 46.61 | +10.95 | +8.68 | +3.24 | −5.04 | −12.96 |

![Hình 5.1](figures/hinh5_1.png)

**Hình 5.1.** Số liệu của Bảng 5.10 vẽ theo $M$. Bốn đường màu là FedAvg, FedProx, FedMix và FedBR; bốn đường xám liền là GroupDRO, DANN, FedAvg + Mixup và FedBR + Mixup; đường xám đứt là Moon. Ba giá trị tại $M = 10$ nằm dưới trục được ghi ở góc trên bên phải.

Bảng 5.10 cho ba nhận xét.

Thứ nhất, phép lấy trung bình làm mất thông tin hiệu chuẩn rất nhanh. Mức cải thiện chỉ dương ở $M \le 2$, chuyển sang âm ở $M = 3$ với mọi thuật toán trừ Moon, và ở $M = 10$ việc hiệu chuẩn làm giảm độ chính xác của mọi mô hình, từ 13 đến 54 điểm. Với 2000 mẫu mỗi client, ảnh thô đủ để huấn luyện lại tầng phân lớp, còn ảnh trung bình của mười ảnh thì không.

Thứ hai, ở $M = 1$, mức cải thiện tách hai nhóm thuật toán. FedAvg, FedProx, GroupDRO, DANN và FedMix được từ +3.9 đến +5.8 điểm; FedBR và FedBR + Mixup chỉ được +1.3 và +1.7, gần với FedAvg + Mixup (+1.0). Sau khi hiệu chuẩn, FedBR đạt 67.26% còn FedAvg đạt 61.81%. Trong khoảng cách 9.9 điểm giữa hai mô hình vòng cuối, khoảng 4.5 điểm biến mất khi cả hai được huấn luyện lại tầng phân lớp trên ảnh thô, còn khoảng 5.4 điểm giữ nguyên; cả hai phần đều vượt ngưỡng đọc. Điều này khớp với vai trò của $L_{\text{bal}}$ trong (3.19): thành phần cân bằng tầng phân lớp của FedBR đã làm trong lúc huấn luyện phần việc mà hiệu chuẩn sau huấn luyện làm cho FedAvg.

Thứ ba, FedBR sụt mạnh nhất ở $M = 10$. Thành phần tương phản (3.17) cho một cách giải thích: nó kéo đặc trưng của pseudo-data, vốn là ảnh trung bình mười ảnh, ra xa đặc trưng của ảnh thật cục bộ. Bộ trích xuất của FedBR vì vậy đặt ảnh trung bình vào một vùng đặc trưng riêng, và tầng phân lớp học trên vùng đó không dùng được cho ảnh thật.

Hai kiểm tra bổ sung cho cùng kết luận. Với 200 mẫu mỗi client, tức 200 mẫu cho mỗi lớp trong không gian $d = 512$ chiều, bộ phân lớp LDA thua mô hình gốc ở mọi $M$; đây là chế độ mẫu hữu hạn mà mục 3.6 mô tả. Huấn luyện lại tầng phân lớp bằng cross-entropy với nhãn mềm, ở hai cấu hình tốc độ học, cho cùng thứ tự các thuật toán tại $M = 1$ với biên độ nhỏ hơn LDA (FedAvg +4.6, FedBR +0.6) và cùng chiều giảm theo $M$.

Chiều giảm theo $M$ lặp lại ở cả chín mô hình, với biên độ lớn hơn nhiều so với ngưỡng đọc. Kết quả cũng khớp với mục 5.2.3: trên cả hai nền tảng, huấn luyện lại tầng phân lớp trên dữ liệu cân bằng lớp nâng được độ chính xác của FedAvg.

## 5.4. Chi phí tài nguyên

Chi phí truyền thông tính theo (4.1). Tập 32 pseudo-sample của FedBR tốn khoảng 4.3 MB, trả một lần. Thêm nhãn mềm như FedMix thì con số gần như không đổi, vì mỗi nhãn chỉ có 10 giá trị so với 3072 giá trị của một ảnh. Mức này nhỏ hơn nhiều so với khoảng 738 MB mà mỗi vòng truyền thông tốn để trao đổi tham số.

Chi phí tính toán lấy từ thời gian mỗi bước ghi trong nhật ký của lượt chạy ở Bảng 5.8.

**Bảng 5.11.** Thời gian huấn luyện quy về 1000 vòng truyền thông, lượt chạy một hạt giống ở Bảng 5.8. Cột cuối là tỉ lệ so với FedAvg. `[CẦN ĐIỀN: loại GPU]`.

| Thuật toán | Giờ / 1000 vòng | So với FedAvg |
|---|---|---|
| FedAvg | 2.3 | 1.0× |
| FedProx | 2.7 | 1.2× |
| FedMix | 5.8 | 2.5× |
| FedBR | 7.5 | 3.3× |
| FedBR + Mixup | 7.6 | 3.3× |

FedMix tốn gấp khoảng hai lần rưỡi FedAvg và FedBR gấp khoảng ba lần. Mức tăng khớp với phần tính toán thêm ở Bảng 4.1: FedMix cần một lượt lan truyền ngược bậc hai để lấy gradient theo đầu vào, FedBR cần thêm các lượt truyền xuôi trên pseudo-data và một bước cập nhật riêng cho tầng chiếu. Với cùng ngân sách tính toán, FedBR chạy được khoảng một phần ba số vòng của FedAvg.

## 5.5. Cộng số hạng Taylor vào FedBR

Mục 5.3.2 cho thấy FedBR là cách dùng mẫu trung bình duy nhất vượt ngưỡng đọc, còn FedMix thì không. Mục này thử cơ chế dựa trên khai triển Taylor ở chỗ thuận lợi nhất cho nó: giữ nguyên FedBR và cộng thêm hai số hạng mang mẫu trung bình của FedMix. Nếu số hạng Taylor chở được thông tin hữu ích mà FedMix không tận dụng được, một phương pháp đã mạnh là nơi thông tin đó dễ lộ ra nhất.

### 5.5.1. Thiết kế

Pseudo-data giữ đúng như FedBR: 32 mẫu dựng một lần, mỗi mẫu là trung bình của 10 ảnh. Mỗi mẫu $u_k$ mang thêm một nhãn $t_k$. Mục tiêu cục bộ là

$$L_A = L_{\text{FedBR}} \;+\; \lambda\Big[-\frac{1}{B}\sum_{k=1}^{B}\sum_{c=1}^{C} t_{k,c}\log \mathrm{softmax}\big(\omega(\phi(x_k))\big)_c\Big] \;+\; \delta\,\lambda(1-\lambda)\,\frac{1}{B}\sum_{k=1}^{B}\big\langle \nabla_x \ell\big(f(x_k), y_k\big),\, u_k \big\rangle, \tag{5.1}$$

trong đó $L_{\text{FedBR}}$ là (3.19), số hạng thứ hai là số hạng nhãn (II) của (3.15), số hạng thứ ba là số hạng Taylor (III), và $\delta \in \{0, 1\}$ bật hoặc tắt (III).

(5.1) khác FedMix ở hai chỗ. Ảnh cục bộ không bị co về $(1-\lambda)x_k$, và cross-entropy của FedBR giữ trọng số 1; hai số hạng của FedMix được cộng vào như hai số hạng điều chuẩn. Số hạng (III) dùng phép chuẩn hoá theo công thức, nên lớn hơn số hạng tương ứng của FedMix ở Bảng 5.9 đúng $B = 32$ lần (Chương 4, mục 4.3).

Nhãn $t_k$ có hai cấu hình: histogram nhãn của mười ảnh tạo nên $u_k$ (nhãn mềm, như FedMix), hoặc $t_k = \frac{1}{C}\mathbf{1}$ (nhãn đều, không lộ thêm thông tin so với FedBR). Ghép với hai giá trị của $\delta$ được bốn cấu hình. Hiệu giữa cấu hình có và không có (III) đo riêng số hạng Taylor; hiệu giữa cấu hình không có (III) và FedBR đo riêng số hạng nhãn. $\lambda = 0.1$ như FedMix; $\mu$, $\gamma$, $\tau_1$, $\tau_2$ như FedBR ở Bảng 5.2; hạt giống 12345; 1000 vòng. Bốn cấu hình và các phép so sánh này được xác định trước khi chạy thực nghiệm.

Các lượt chạy này đánh giá mỗi 2 vòng, dày hơn lượt chạy ở Bảng 5.8 (mỗi 5 vòng). Chỉ số chọn năm mốc cao nhất được lợi khi có nhiều mốc hơn, nên Bảng 5.12 tính mọi chỉ số trên 101 mốc chung của hai lịch đánh giá, tức mỗi 10 vòng.

### 5.5.2. Kết quả

**Bảng 5.12.** FedBR cộng các số hạng mẫu trung bình của FedMix theo (5.1), trên nền tảng FedBR (CIFAR-10 xoay, 10 client, 1000 vòng, VGG11 không chuẩn hoá, $d = 512$), hạt giống 12345, $\lambda = 0.1$. Độ chính xác (%) trên phần dữ liệu giữ lại của các client, tính trên 101 mốc đánh giá chung (mỗi 10 vòng); vì vậy hàng FedAvg và FedBR lệch nhẹ so với Bảng 5.9. Cột cuối là hiệu theo chỉ số chính so với FedBR; ngưỡng đọc 3 điểm theo mục 5.3.1. "NaN": hàm mất mát thành NaN trong lúc huấn luyện.

| Cấu hình | Nhãn $t_k$ | (III) | Chỉ số chính | Năm mốc cuối | Hiệu so với FedBR |
|---|---|---|---|---|---|
| FedAvg | — | — | 59.19 | 58.41 | −6.48 |
| FedBR | — | — | 65.67 | 65.38 | — |
| FedBR + (II) | mềm | không | 65.63 | 65.61 | −0.04 |
| FedBR + (II) | đều | không | 65.05 | 64.96 | −0.62 |
| FedBR + (II) + (III) | mềm | có | 32.69 | 10.00 (NaN) | −32.98 |
| FedBR + (II) + (III) | đều | có | 32.89 | 10.00 (NaN) | −32.78 |

![Hình 5.2](figures/hinh5_2.png)

**Hình 5.2.** Đường học của FedAvg, FedBR và bốn cấu hình của (5.1), hạt giống 12345. Trục tung là độ chính xác trên phần dữ liệu giữ lại của các client. Màu tím: FedBR + (II), không có (III); màu cam: có (III); nét liền là nhãn mềm, nét đứt là nhãn đều. Dấu × đánh dấu vòng mà hàm mất mát thành NaN; sau đó mô hình chỉ còn đoán ngẫu nhiên.

Số hạng nhãn (II) không tạo khác biệt đo được. So với FedBR, hai cấu hình không có (III) lệch −0.04 và −0.62 điểm theo chỉ số chính, +0.23 và −0.42 điểm theo năm mốc cuối; nhãn mềm hơn nhãn đều 0.58 điểm. Mọi hiệu đều dưới ngưỡng đọc, và đường học của hai cấu hình gần như trùng FedBR suốt 1000 vòng (Hình 5.2). Histogram nhãn của mẫu trung bình, thứ FedMix chia sẻ thêm so với FedBR, không mang lại gì thấy được.

Số hạng Taylor (III) làm huấn luyện hỏng. Hai cấu hình có (III) đi cùng FedBR tới khoảng vòng 100, rồi dừng lại quanh 30–33% trong khi FedBR tiếp tục lên. Cross-entropy trên dữ liệu cục bộ đứng quanh 2.0 trong suốt giai đoạn đó; ở cấu hình không có (III), cùng đại lượng đã xuống khoảng 1.5 vào vòng 400. Hàm mất mát thành NaN ở vòng 396 với nhãn đều và vòng 644 với nhãn mềm, sau đó độ chính xác về 10%. Hai cấu hình nhãn hỏng theo cùng một kiểu, nên nguyên nhân nằm ở (III).

Trong cùng loạt chạy, (III) làm thời gian tăng từ khoảng 8.7–8.8 lên 9.9–10.0 giờ mỗi 1000 vòng. Loạt chạy này khác thời điểm với Bảng 5.11, nên con số không đặt cạnh bảng đó.

### 5.5.3. Đọc kết quả

FedMix ở Bảng 5.9 mang số hạng Taylor bị thu nhỏ 32 lần theo cách chuẩn hoá ở mục 4.3, và huấn luyện ổn định. Trong (5.1), số hạng ấy ở đúng biên độ công thức làm huấn luyện phân kỳ. Cấu trúc của (III) cho một cách giải thích: số hạng này tuyến tính theo gradient đầu vào $\nabla_x \ell$, nên không bị chặn dưới. Bộ tối ưu có thể giảm mục tiêu bằng cách làm gradient đầu vào lớn và ngược hướng với $u_k$, trong khi cross-entropy đứng yên, đúng như cross-entropy đứng quanh 2.0 ở mục 5.5.2. Nếu vậy, phép chia thừa cho $B$ ở mục 4.3 vừa làm số hạng Taylor nhỏ đi, vừa là thứ giữ cho FedMix huấn luyện được.

Cách giải thích này chưa được kiểm chứng. Ngoài biên độ của (III), (5.1) còn khác FedMix ở việc không co ảnh cục bộ và ở phần mục tiêu của FedBR mà các số hạng được cộng vào; nhật ký cũng không ghi giá trị của (III). Phép kiểm tra trực tiếp là chạy lại (5.1) với (III) chia cho $B$, tức đúng biên độ của FedMix: nếu cấu hình đó ổn định thì nguyên nhân là biên độ.

Ở cấu hình đã chạy, cộng các số hạng mẫu trung bình của FedMix vào FedBR không cải thiện FedBR: số hạng nhãn không tạo khác biệt đo được, còn số hạng Taylor ở đúng biên độ công thức làm huấn luyện phân kỳ.

## 5.6. Tổng hợp và thảo luận

Mục này gom kết quả của chương theo các mục tiêu cụ thể ở Chương 1.

**Cách dùng mẫu trung bình dựa trên khai triển Taylor không nâng được hiệu suất ở mọi cấu hình đã đo.** Trên nền tảng Flower, dưới lệch phân phối nhãn, FedMix kém FedAvg 1.86 ± 0.79 điểm, và cận trên của khoảng tin cậy 95% một phía là −0.52 điểm (mục 5.2.2). Trên nền tảng FedBR, dưới lệch phân phối nhãn kèm xoay, hiệu của FedMix so với FedAvg là −2.29 điểm theo chỉ số chính và −0.58 điểm theo năm mốc cuối, cả hai dưới ngưỡng đọc (mục 5.3.2). Cộng số hạng Taylor vào FedBR cũng không giúp: ở đúng biên độ công thức, nó làm huấn luyện phân kỳ (mục 5.5). Các kết quả FedMix đều dùng cách chuẩn hoá ở mục 4.3, với $\lambda$ cố định trong mỗi nền tảng (0.05 trên Flower, 0.1 trên nền tảng FedBR).

**Trên cùng một loại mẫu trung bình, FedBR là cách dùng duy nhất cho mức cải thiện đọc được.** FedBR hơn FedAvg 6.37 điểm theo chỉ số chính và 7.35 điểm theo năm mốc cuối, cùng chiều và cùng cỡ với bảng công bố của [3] (mục 5.3.2). Vì FedBR và FedMix khác nhau cả ở tập mẫu trung bình, tầng chiếu và bộ siêu tham số, hiệu giữa chúng không quy riêng được cho cách dùng (mục 5.1.3). Mục 5.3.3 cho biết thêm một phần nguồn gốc của hiệu: khoảng 4.5 trong 9.9 điểm FedBR hơn FedAvg ở mô hình vòng cuối biến mất khi cả hai được huấn luyện lại tầng phân lớp trên ảnh thô, khớp với vai trò của $L_{\text{bal}}$.

**Mẫu trung bình rẻ về truyền thông nhưng mất thông tin nhanh.** Chia sẻ 32 mẫu trung bình tốn khoảng 4.3 MB một lần, nhỏ hơn nhiều so với khoảng 738 MB mỗi vòng truyền thông (mục 5.4). Nhưng ở $M = 10$ ảnh mỗi mẫu, mẫu trung bình không còn đủ thông tin để huấn luyện lại tầng phân lớp: phép hiệu chuẩn chỉ có lợi khi $M \le 2$ và làm mọi mô hình sụt từ 13 đến 54 điểm ở $M = 10$ (mục 5.3.3). Trên nền tảng Flower, mức cải thiện của CCVR đổi dấu theo ngân sách mẫu ảo (mục 5.2.3). Về tính toán, FedMix tốn gấp khoảng 2.5 lần và FedBR khoảng 3.3 lần thời gian của FedAvg (Bảng 5.11).

**Trên nền tảng Flower, thiên lệch của tầng phân lớp nằm ở hướng.** Tỉ số giữa chuẩn lớn nhất và nhỏ nhất của các vector trọng số theo lớp chỉ từ 1.10 đến 1.17, trong khi hiệu chuẩn lại tầng cuối đổi recall của lớp kém nhất từ 26 đến 45 điểm (mục 5.2.4). Nhật ký của nền tảng FedBR không ghi các đại lượng theo lớp, nên phép đo này chỉ có trên Flower.

---

## Truy vết mục 5.3–5.5 — không chép vào Word

| Số liệu | Tệp thô |
|---|---|
| Bảng 5.2 (cấu hình nền tảng FedBR) | dòng đầu của `results.jsonl` mỗi thuật toán trong `C:\Users\KietVu\Testplace\FedBR\output\cifar10\02_attempt_20260916\`, trường `args` (`holdout_fraction` 0.2; `checkpoint_freq` 250 bước = 5 vòng; `local_steps` 50; `steps` 50000) và `hparams` (`lr` 0.01; `momentum` 0; `weight_decay` 0; `data_augmentation` true; `fedbr_tau1/tau2` 2; `fedbr_mu` 0.5; `fedbr_lambda` 1.0); hạt giống: `Makefile`, biến `SEEDS` |
| Bảng 5.8, cột "Chạy lại" | `C:\Users\KietVu\Testplace\FedBR\output\cifar10\02_attempt_20260916\summary.csv` (cột `Acc (%)`); đã tái tính khớp từ từng `results.jsonl` (`INDEX` §5.2) |
| Bảng 5.9 | cùng thư mục, `<thuật toán>/results.jsonl`: độ chính xác mỗi mốc = trung bình `env00_out_acc` … `env09_out_acc`; chỉ số chính = trung bình 5 mốc cao nhất (khớp `summary.csv`), năm mốc cuối = trung bình 5 mốc cuối trong 201 mốc. Hiệu Bảng 1 của [3]: FedBR − FedAvg = 64.65 − 58.99 = 5.66; FedMix − FedAvg = 57.37 − 58.99 = −1.62 |
| Bảng 5.8, cột "Công bố" | `paper/ref/Guo et al. - 2023 - FedBR….pdf`, Bảng 1, cột CIFAR10 (VGG11) |
| Bảng 5.10, Hình 5.1 | `C:\Users\KietVu\Testplace\FedBR\output\cifar10\02_attempt_20260916\calibrate_head_lda2000\*.json` ($M = 1, 2$) và `…\calibrate_head_lda2000_M3-10\*.json` ($M = 3, 5, 10$), trường `baseline.local` và `rows[].delta.local`; sinh bằng `make calibrate-head OUT=… CALIB_ARGS="--M … --n_per_client 2000 --method lda --eval_envs local"`. Hai kiểm tra bổ sung: `…\calibrate_head\` (200 mẫu/client, CE và LDA, cả global) và `…\calibrate_head_ce_lr01\`. Bảng tổng hợp ở `INDEX` §5.2b. Hình: `figures/hinh5_1.py` |
| Bảng 5.11 | cùng `summary.csv`, cột `h/1000rd`. Cột `VRAM (GB)` không dùng: ghi 0.0 cho nhiều thuật toán, kể cả `fedbr-taylor-uniform`, trong khi `fedbr-taylor-soft` ghi 3.1, nên nhiều khả năng là lỗi ghi nhận |
| Bảng 5.12, Hình 5.2 | `C:\Users\KietVu\Testplace\FedBR\output\cifar10\fedbr_taylor\fedbr-taylor-{soft,uniform}{,-noiii}\results.jsonl` (thuật toán `FedBRTaylor`, `checkpoint_freq` 100 bước = 2 vòng, 501 mốc; hparams `fedbrt_lambda` 0.1, `fedbrt_taylor` 1/0, `fedbrt_label` soft/uniform) và `02_attempt_20260916\{fedavg,fedbr}\results.jsonl`; mốc chung = bước chia hết cho 500 (101 mốc). NaN: bước 19,800 (uniform) và 32,200 (soft) theo trường `loss`. Thời gian: `fedbr_taylor\summary.csv`, cột `h/1000rd` (9.9 / 10.0 có (III); 8.7 / 8.8 không). Cross-entropy ≈ 2.0 là trường `loss` (chỉ cross-entropy cục bộ); giá trị (III) không được `train_fed` ghi. Mã: `fedbr/algorithms.py`, lớp `FedBRTaylor` (commit `b0bb3e2`); thiết kế chốt 26/09 ở cuối `04_chuong4.md`. Hình: `figures/hinh5_2.py` |
| ~~Port FedBR lên Flower~~ | **không dùng** (học viên, 26/09): bản cài FedBR trên nền tảng Flower chưa được xác nhận khớp với FedBR gốc, nên số liệu của nó có thể sai lệch vì cài đặt. Thư mục gốc để tra: kho Flower `runs/paper_{fedavg,fedbr}_rot{,_noaug}_r500/` |
