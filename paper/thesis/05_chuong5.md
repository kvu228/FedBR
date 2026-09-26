# CHƯƠNG 5 — THỰC NGHIỆM (hướng B)

> **KHỐI TRẠNG THÁI** · 25/09/2026 (sửa đè, học viên cho phép)
>
> | Mục | Trạng thái | Chờ |
> |---|---|---|
> | 5.1 Thiết lập | `[ĐÃ VIẾT]` 25/09 — nhận toàn bộ mục 4.5 cũ của Ch.4 (Bảng 4.2 → 5.1, Bảng 4.3 → 5.3), phần "đọc các phép so sánh" của mục 4.2.4 cũ, và chỗ thiết lập đi khác khung; thêm Bảng 5.2 cấu hình nền tảng FedBR lấy từ `args`/`hparams` của `02_attempt` | — |
> | 5.2 Flower, lệch nhãn | `[ĐÃ VIẾT]` — mang sang từ `archive/…/05_chuong5.md` (khối 24/09) | — |
> | 5.3.1 Tái hiện bảng FedBR | `[ĐÃ VIẾT]` 26/09 — một hạt giống (12345) là số liệu cuối cùng của nền tảng FedBR | — |
> | 5.3.2 So sánh các cách dùng mẫu trung bình | `[ĐÃ VIẾT]` 26/09 — Bảng 5.10 từ `02_attempt`, cả chỉ số chính lẫn năm mốc cuối; hàng NaiveMix chờ T1 nếu chạy | T1 (tuỳ chọn) |
> | ~~5.3.3 Kiểm toán mã FedBR~~ | chuyển sang **Phụ lục A** (`07_phu-luc.md`), 25/09 | — |
> | **5.3.3 Mẫu trung bình còn giữ bao nhiêu thông tin cho tầng phân lớp** | `[ĐÃ VIẾT]` 26/09 — đặt thành **phép chẩn đoán**, không gọi là cách dùng thứ tư, nên Ch.4 (Bảng 4.1, Thuật toán 4.1, Hình 4.1) không phải sửa; Bảng 5.11, Hình 5.1 | — |
> | 5.4 Chi phí tài nguyên | `[BẢN NHÁP]` — còn thiếu loại GPU | — |
> | 5.5 FedBR + Taylor | chỉ khi A có số liệu | T2 |
> | 5.6 Tổng hợp | `[CHỜ SỐ LIỆU]` | tất cả |
>
> **Đánh số bảng (đánh lại 26/09, lượt 2):** Bảng 5.1–5.3 thuộc mục 5.1; Bảng 5.4–5.8 thuộc mục 5.2; Bảng 5.9 thuộc 5.3.1; **Bảng 5.10 thuộc 5.3.2 (mới)**; Bảng 5.11 và Hình 5.1 thuộc 5.3.3; Bảng 5.12 thuộc 5.4.
>
> **Quyết định 26/09 (học viên): nền tảng FedBR chỉ dùng hạt giống 12345.** Mỗi lượt FedBR 1000 vòng mất khoảng 7,5 giờ, không đủ thời gian cho ba hạt giống; **T0 bỏ**. Nền tảng Flower giữ ba hạt giống. Hệ quả trong chương này:
> - 5.1.3 viết lại: Flower dùng khoảng tin cậy trên ba hạt giống; FedBR dùng **ngưỡng đọc 3 điểm phần trăm**, lấy từ chênh lệch giữa lượt chạy lại và bảng công bố ở Bảng 5.9;
> - 5.1.4 bỏ kiểm định t và Holm (không làm được với một hạt giống); H1/H2 thành hai phép so sánh chính S1/S2 đọc theo ngưỡng;
> - 5.3.1, 5.3.2 viết xong từ `02_attempt`; 5.3.3 không còn chờ thêm hạt giống;
> - T2 (hướng A) đang chạy trên Vast, cũng một hạt giống; thân chương chưa nhắc A.
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
> ⛔ **IR#10:** mục nào chưa có dữ liệu thì để `[CHỜ SỐ LIỆU: <mức>]`, không điền số dự kiến.

**Ánh xạ sang Word.** Word hiện có hai tiêu đề: *5.1 Thiết lập thực nghiệm* và *5.2 Tái hiện và kiểm toán tính tái lập*. Đổi thành:

| Word hiện tại | Sau khi sửa |
|---|---|
| 5.1 Thiết lập thực nghiệm | 5.1 Thiết lập thực nghiệm (giữ; thêm 5.1.1–5.1.4) |
| — | **5.2 Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower** (chèn, cùng 5.2.1–5.2.5) |
| 5.2 Tái hiện và kiểm toán tính tái lập | **5.3 So sánh các cách dùng mẫu trung bình trên nền tảng FedBR** (đổi tên; 5.3.1 Tái hiện · 5.3.2 So sánh) |
| — | **Phụ lục A. Kiểm toán mã nguồn FedBR** (chèn sau Tài liệu tham khảo; nội dung ở `07_phu-luc.md`) |
| — | 5.4 Chi phí tài nguyên · 5.6 Tổng hợp và thảo luận (chèn; 5.5 chỉ khi có A) |

---

## 5.1. Thiết lập thực nghiệm

Luận văn chạy thực nghiệm trên hai nền tảng. Nền tảng Flower dùng cho các thực nghiệm dưới lệch phân phối nhãn ở mục 5.2. Các thực nghiệm còn lại chạy trên bộ thực nghiệm công bố cùng bài báo FedBR [2], gọi tắt là nền tảng FedBR. Mục này mô tả hai nền tảng và giao thức đo lường áp cho mọi phép so sánh trong chương; thiết lập chi tiết của nền tảng Flower nằm ở mục 5.2.1.

### 5.1.1. Hai nền tảng thực nghiệm

**Bảng 5.1.** Hai nền tảng thực nghiệm. Tham số Dirichlet ghi theo quy ước của Chương 3.

| | Nền tảng Flower | Nền tảng FedBR [2] |
|---|---|---|
| Client | 60, mỗi vòng chọn 15 | 10, tham gia mọi vòng |
| Backbone | VGG sửa đổi theo phụ lục của [1], không chuẩn hoá theo lô, $d = 512$ | VGG11 không chuẩn hoá theo lô, $d = 512$ |
| Lệch phân phối | nhãn: hai lớp mỗi client, hoặc Dirichlet nồng độ mỗi thành phần $\beta$ trên trục client, 60 thành phần | nhãn: Dirichlet $\alpha = 0{,}1$ nồng độ tổng trên trục lớp, kèm xoay theo client với $\alpha_{\text{rot}} = 1{,}0$ nồng độ tổng |
| Huấn luyện cục bộ | 2 epoch, lô 10 | 50 bước, lô 32 |
| Chỉ số chính | độ chính xác cao nhất theo vòng trên tập kiểm tra | trung bình năm độ chính xác cao nhất theo vòng trên phần dữ liệu giữ lại của các client |

Hai nền tảng khác nhau ở gần như mọi thành phần của thiết lập, nên con số tuyệt đối của chúng không đặt cạnh nhau được. Mọi phát biểu bắc qua hai nền tảng đặt ở mức cơ chế, dạng "hiện tượng X xuất hiện ở cả hai", chứ không ở dạng "độ chính xác tăng từ $a$ lên $b$".

Bảng 5.2 ghi đầy đủ cấu hình của nền tảng FedBR. Cấu hình giữ đúng bài báo [2], để bảng tái hiện ở mục 5.3.1 so được với bảng công bố.

**Bảng 5.2.** Cấu hình thực nghiệm trên nền tảng FedBR.

| Thành phần | Giá trị |
|---|---|
| Dữ liệu | CIFAR-10 xoay, 10 client; lệch phân phối như Bảng 5.1; 20% dữ liệu của mỗi client được giữ lại để đánh giá |
| Huấn luyện | 1000 vòng, mỗi vòng 50 bước cục bộ, lô 32; SGD tốc độ học 0,01, không momentum, không weight decay; tăng cường dữ liệu mặc định của nền tảng |
| Backbone | VGG11 không chuẩn hoá theo lô, $d = 512$ |
| Đánh giá | mỗi 5 vòng |
| NaiveMix, FedMix | $\lambda = 0{,}1$; mỗi bước cục bộ nhận 32 mẫu trung bình mới, mỗi mẫu là trung bình của 10 ảnh; FedMix chuẩn hoá số hạng Taylor theo cách nêu ở Chương 4, mục 4.3 |
| FedBR | 32 pseudo-sample dựng một lần trước huấn luyện, mỗi mẫu là trung bình của 10 ảnh; $\tau_1 = \tau_2 = 2$, $\mu = 0{,}5$, $\gamma = 1{,}0$ (trọng số của $L_{\text{bal}}$ trong (3.19)); tầng chiếu là MLP $d \to 2d \to d$ |
| Hạt giống | 12345, cho mọi thuật toán (mục 5.1.3) |

Bảng 5.2 cho thấy một chỗ thiết lập đi khác khung ở Chương 4. Trong khung, tập mẫu trung bình dựng một lần trước huấn luyện, và FedBR làm đúng như vậy. NaiveMix và FedMix thì nhận một lô 32 mẫu trung bình mới ở mỗi bước cục bộ, dựng thẳng từ dữ liệu của mọi client. Cách làm này chỉ thực hiện được trong mô phỏng, nơi dữ liệu của mọi client nằm trên cùng một máy. Luận văn giữ nó để kết quả so được với bảng công bố của [2]. Hệ quả là trong suốt quá trình huấn luyện, NaiveMix và FedMix thấy nhiều mẫu trung bình khác nhau hơn hẳn FedBR; Chương 6 nêu điểm này trong phần hạn chế.

### 5.1.2. Chỉ số và các đại lượng được ghi nhận

Trên nền tảng FedBR, chỉ số chính là chỉ số của bài báo FedBR: trung bình năm độ chính xác cao nhất theo vòng, đo trên phần dữ liệu giữ lại của các client. Dùng chỉ số này thì bảng tái hiện so được với bảng công bố.

Chỉ số này có một nhược điểm: năm mốc được chọn theo chính độ chính xác trên tập đánh giá, nên giá trị bị kéo lên. Độ thiên tác động lên mọi phương pháp, nhưng không nhất thiết như nhau; phương pháp có đường học dao động mạnh hơn được lợi nhiều hơn. Vì vậy, với các phép so sánh chính ở Bảng 5.3, luận văn báo cáo kèm trung bình năm mốc đánh giá cuối cùng, một chỉ số không chọn theo tập đánh giá. Nếu hai chỉ số cho hiệu trái dấu nhau, điều đó được báo cáo cùng kết quả.

Ở mỗi mốc đánh giá, nền tảng FedBR ghi độ chính xác trên phần dữ liệu giữ lại của từng client, độ chính xác trên mười tập kiểm tra xoay góc cố định, thời gian mỗi bước và toàn bộ cấu hình siêu tham số. Nhật ký không ghi độ chính xác theo từng lớp, cũng không ghi chuẩn của các vector trọng số theo lớp. Phân tích dạng thiên lệch của tầng phân lớp, tức mục tiêu cụ thể thứ tư, vì vậy chỉ thực hiện trên nền tảng Flower, ở mục 5.2.4.

Với phương pháp có tham số ngân sách, như số đặc trưng ảo mỗi lớp của CCVR, mọi con số được báo cáo kèm ngân sách tại đó nó được đo. Mục 5.2.3 cho thấy vì sao quy tắc này cần thiết.

### 5.1.3. So sánh theo cặp và số hạt giống

Mọi mức cải thiện được tính theo cặp. Hai cấu hình đem so dùng cùng một hạt giống, và hạt giống quyết định cùng lúc lần rút phân hoạch dữ liệu, trọng số khởi tạo và thứ tự các lô. Lịch học và số vòng cũng như nhau. Cách làm này loại khỏi phép so sánh phần phương sai do phân hoạch dữ liệu, vốn lớn trong học liên kết mô phỏng.

Hai nền tảng có số hạt giống khác nhau. Trên nền tảng Flower, mỗi cấu hình chạy với ba hạt giống; mỗi hạt giống cho một hiệu theo cặp, và khoảng tin cậy được tính trên ba hiệu đó. Với $n = 3$ thì $t_{0{,}975;\,2} = 4{,}303$, nên ở độ lệch chuẩn của hiệu cỡ 1,2 điểm phần trăm, nửa rộng khoảng tin cậy 95% là $4{,}303 \times 1{,}2 / \sqrt{3} \approx 2{,}98$ điểm. Khi khoảng tin cậy chứa không, luận văn nói thẳng là phép đo không phân giải được hiệu đó, và không diễn giải kết quả ấy thành bằng chứng rằng hai phương pháp tương đương.

Trên nền tảng FedBR, mỗi thuật toán chỉ chạy một lần, với hạt giống 12345. Một lượt FedBR 1000 vòng mất khoảng 7,5 giờ tính toán (Bảng 5.12), và thời gian của luận văn không đủ cho ba hạt giống ở mọi thuật toán. Không có lần chạy lặp thì không ước lượng được độ dao động giữa các hạt giống, nên các hiệu trên nền tảng này không có khoảng tin cậy.

Thay vào đó, luận văn dùng một thước đo thô lấy từ chính nền tảng này. Bảng 5.9 đặt lượt chạy lại cạnh bảng công bố của [2] cho cùng cấu hình. Bỏ Moon, thuật toán mang một lỗi đã biết, chênh lệch giữa hai bên nằm trong khoảng −2,69 đến +2,66 điểm. Chênh lệch này gộp cả dao động giữa các lần chạy lẫn khác biệt môi trường, nên nó chỉ cho biết cỡ của dao động. Quy tắc đọc vì vậy như sau: trên nền tảng FedBR, một hiệu theo cặp nhỏ hơn 3 điểm phần trăm không được diễn giải thành khác biệt giữa hai phương pháp; một hiệu từ 3 điểm trở lên được báo cáo như một quan sát đơn lẻ, và được đối chiếu chiều với bảng công bố của [2]. Ngưỡng này cùng cỡ với nửa rộng khoảng tin cậy của nền tảng Flower.

### 5.1.4. Các phép so sánh chính

Luận văn khai báo trước hai phép so sánh chính trên nền tảng FedBR, ở cấu hình của Bảng 5.2 (Bảng 5.3). Giá trị $\lambda = 0{,}1$ là mặc định trong thiết lập của [2] và được chốt trước khi chạy. Vì nền tảng này chỉ có một hạt giống, hai phép so sánh được đọc theo quy tắc ở mục 5.1.3, không qua kiểm định thống kê.

**Bảng 5.3.** Hai phép so sánh chính trên nền tảng FedBR. $\mathrm{Acc}$ là độ chính xác theo chỉ số chính của mục 5.1.2, báo cáo kèm trung bình năm mốc đánh giá cuối. Một hạt giống (12345). FedMix dùng cách chuẩn hoá số hạng Taylor nêu ở Chương 4, mục 4.3.

| | Hiệu theo cặp | Cách đọc |
|---|---|---|
| S1 | $\mathrm{Acc}_{\text{FedBR}} - \mathrm{Acc}_{\text{FedAvg}}$ | dưới 3 điểm: không phân biệt được; từ 3 điểm trở lên: quan sát đơn lẻ, đối chiếu chiều với Bảng 1 của [2] |
| S2 | $\mathrm{Acc}_{\text{FedMix}} - \mathrm{Acc}_{\text{FedAvg}}$ | như S1 |

Mọi phép so sánh khác mang nhãn thăm dò: FedProx, NaiveMix, FedBR + Mixup, hiệu FedMix − NaiveMix, và các thuật toán chỉ có trong bảng tái hiện.

Hai phép so sánh giữa các cách dùng mẫu trung bình cần được đọc đúng phạm vi. FedMix và NaiveMix nhận cùng mẫu trung bình, cùng nhãn mềm và cùng trọng số trộn, nhưng khác nhau ở hai chỗ cùng lúc: điểm đánh giá hàm mất mát, và sự có mặt của số hạng gradient. Hiệu giữa chúng vì vậy so hai cách dùng cùng một thông tin, và không quy riêng được cho số hạng Taylor. Việc dùng chung một trọng số trộn vẫn loại được một nguồn nhiễu có thật trong bài báo FedMix [1]. Ở bảng kết quả chính của bài báo đó, NaiveMix đạt 77,4% và FedMix 81,2% trên CIFAR-10; trong phép quét trọng số trộn ở phụ lục, giá trị tốt nhất của NaiveMix là 80,6%, chỉ còn cách FedMix 0,6 điểm.

FedBR và FedMix khác nhau ở nhiều chỗ hơn: tập mẫu trung bình (Bảng 5.2), tầng chiếu cùng bước cập nhật riêng của nó, và bộ siêu tham số. Hiệu giữa hai phương pháp là hiệu giữa hai phương pháp hoàn chỉnh cùng dùng một loại dữ liệu; nó không đo riêng ảnh hưởng của cách dùng mẫu trung bình.

---

## 5.2. Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower

Mục này đo ba điều dưới lệch phân phối nhãn: FedMix có cải thiện so với FedAvg hay không; mức cải thiện của nhóm hiệu chuẩn tầng phân lớp từ thống kê lớp phụ thuộc thế nào vào ngân sách mẫu ảo; và thiên lệch của tầng phân lớp nằm ở độ lớn hay ở hướng. Các thực nghiệm chạy trên một nền tảng mô phỏng dựng bằng Flower, mô hình huấn luyện từ đầu. Nền tảng này khác nền tảng FedBR ở cách phân hoạch, số client, backbone và tập thuật toán đối chứng, nên con số của mục này không đặt cạnh con số của các mục sau; các mục sau chỉ đối chiếu với nó ở mức cơ chế.

### 5.2.1. Thiết lập

**Bảng 5.4.** Thiết lập thực nghiệm trên nền tảng Flower. $\beta$ là nồng độ Dirichlet **mỗi thành phần**, lấy mẫu trên trục **client** cho từng lớp, với 60 thành phần ứng với 60 client; nồng độ càng nhỏ thì lệch càng nặng. $M_c$ là số đặc trưng ảo sinh cho mỗi lớp khi huấn luyện lại tầng phân lớp; $d$ là số chiều đặc trưng.

| Thành phần | Giá trị |
|---|---|
| Khung | Flower, chế độ mô phỏng |
| Dữ liệu | CIFAR-10; CINIC-10 chỉ dùng cho phép so sánh các head hiệu chuẩn |
| Client | 60, mỗi vòng chọn 15 |
| Huấn luyện cục bộ | 2 epoch, lô 10, SGD với tốc độ học 0,01 giảm theo hệ số 0,999 mỗi vòng, không momentum, không weight decay |
| Backbone | VGG sửa đổi theo phụ lục bài báo FedMix [1]: 6 tầng tích chập và 3 tầng kết nối đầy đủ, không chuẩn hoá theo lô, $d = 512$ |
| Phân hoạch | hai lớp mỗi client, 500 vòng (phép so sánh FedMix); Dirichlet $\beta \in \{0{,}05;\ 0{,}1;\ 0{,}3\}$, 150 vòng (hiệu chuẩn tầng phân lớp) |
| FedMix | $\lambda = 0{,}05$; mỗi client gửi một ảnh trung bình của toàn bộ dữ liệu cục bộ kèm nhãn mềm; mỗi lô cục bộ ghép với một ảnh trung bình rút ngẫu nhiên |
| Hiệu chuẩn | CCVR [8] với $M_c \in \{100;\ 2000\}$, biến đổi Tukey 0,5, huấn luyện lại tầng cuối 10 epoch; head LDA dùng hiệp phương sai gộp co về đường chéo với hệ số 0,01 |
| Hạt giống | 42, 43, 44 |

Chỉ số của phép so sánh FedMix là độ chính xác cao nhất theo vòng trên tập kiểm tra. Chỉ số của phép hiệu chuẩn là chênh lệch độ chính xác trước và sau khi hiệu chuẩn, đo trên cùng một mô hình đã huấn luyện. Mọi dấu $\pm$ trong mục này là độ lệch chuẩn mẫu của ba hiệu theo cặp, mỗi hiệu ứng với một hạt giống.

Bài báo FedMix không công bố mã nguồn. Nền tảng được đối chiếu với một bản cài đặt FedMix công khai khác, chạy trên cùng cấu hình với hạt giống 42. Hai bên chênh nhau khoảng 3 điểm phần trăm ở độ chính xác tuyệt đối (FedAvg 65,81% so với 68,69%; FedMix 63,67% so với 66,50%), nhưng hiệu theo cặp gần như trùng: −2,14 và −2,19 điểm. Vì bản cài đặt đó cũng là mốc mà nền tảng được hiệu chỉnh theo, phép đối chiếu này là một kiểm tra tính nhất quán, không phải một phép kiểm chứng độc lập.

### 5.2.2. FedMix so với FedAvg

**Bảng 5.5.** Độ chính xác cao nhất theo vòng (%) của FedAvg và FedMix trên CIFAR-10, phân hoạch hai lớp mỗi client, 500 vòng, backbone VGG không chuẩn hoá ($d = 512$), $\lambda = 0{,}05$. Cột cuối là hiệu theo cặp FedMix − FedAvg, đơn vị điểm phần trăm. Hàng cuối: trung bình ± độ lệch chuẩn mẫu, $n = 3$.

| Hạt giống | FedAvg | FedMix | Hiệu |
|---|---|---|---|
| 42 | 68,69 | 66,50 | −2,19 |
| 43 | 67,42 | 66,47 | −0,95 |
| 44 | 64,74 | 62,31 | −2,43 |
| | | | **−1,86 ± 0,79** |

FedMix kém FedAvg ở cả ba hạt giống. Với ba quan sát, riêng dấu của hiệu không đủ làm bằng chứng: khi không có hiệu ứng, xác suất để ba hiệu cùng dấu đã là 0,25. Phát biểu dựa vào khoảng tin cậy thì chặt hơn. Với $t_{0{,}95;\,2} = 2{,}920$, cận trên của khoảng tin cậy 95% một phía là −0,52 điểm, nên ở cấu hình này khả năng FedMix cải thiện được loại trừ.

Kết luận phụ thuộc vào chỉ số. Lấy độ chính xác ở vòng cuối thay cho vòng tốt nhất, ba hiệu là −3,55, −4,49 và +0,59: trung bình vẫn âm nhưng một hạt giống đổi dấu.

Nền tảng này tính số hạng Taylor theo cách nêu ở Chương 4, mục 4.3, nên với lô 10 ảnh số hạng đi vào mục tiêu với hệ số nhỏ hơn công thức (3.15) mười lần. Kết quả ở Bảng 5.5 vì vậy là kết quả về FedMix với số hạng Taylor đã bị thu nhỏ; luận văn không đo số hạng Taylor ở đúng biên độ của (3.15).

Nền tảng này cũng cho phép đo biên độ của số hạng bậc hai trong khai triển Taylor so với số hạng bậc nhất, ở $\lambda = 0{,}05$. Tại khởi tạo ngẫu nhiên, trên 10 ảnh CIFAR-10, tỉ số là khoảng $1{,}3 \times 10^{-4}$. Trên ba mô hình đã huấn luyện 150 vòng với Dirichlet $\beta = 0{,}05$, tỉ số giữa số hạng bậc hai và số hạng bậc nhất là 0,039, 0,224 và 0,025 theo từng hạt giống. Như vậy số hạng bậc hai lớn lên hai đến ba bậc khi mô hình được huấn luyện. Luận văn không khảo sát nhánh bậc hai vì phạm vi, không phải vì số hạng đó không đáng kể.

**Bảng 5.6.** Hai biến thể thăm dò của FedMix. C1: mỗi client gửi một ảnh trung bình cho từng lớp, thay cho một ảnh trung bình trên toàn bộ dữ liệu cục bộ. C1+C2: C1 cộng thêm quy tắc ghép cặp chọn ảnh trung bình khác lớp có tích vô hướng với gradient theo đầu vào lớn nhất. Hiệu theo cặp so với FedAvg, trung bình ± độ lệch chuẩn mẫu, $n = 3$, đơn vị điểm phần trăm; cột cuối là cận trên của khoảng tin cậy 95% một phía.

| Biến thể | Phân hoạch, số vòng | Hiệu theo hạt giống | Trung bình | Cận trên |
|---|---|---|---|---|
| C1 | hai lớp mỗi client, 500 | −2,22 / −0,55 / −2,94 | −1,90 ± 1,23 | +0,16 |
| C1+C2 | Dirichlet $\beta = 0{,}3$, 150 | −1,36 / −2,95 / −0,60 | −1,64 ± 1,20 | +0,38 |

Cả hai biến thể đều âm về trung bình, nhưng cận trên của cả hai đều dương, nên không loại trừ được khả năng có cải thiện. Chúng được giữ nhãn thăm dò và không tham gia kết luận của luận văn.

### 5.2.3. Hiệu chuẩn tầng phân lớp và ngân sách mẫu ảo

CCVR ước lượng trung bình và hiệp phương sai của đặc trưng theo từng lớp, sinh đặc trưng ảo từ các phân phối Gauss đó, rồi huấn luyện lại riêng tầng phân lớp. Số đặc trưng ảo mỗi lớp, $M_c$, là ngân sách của phương pháp.

**Bảng 5.7.** Mức chênh độ chính xác của CCVR so với mô hình trước hiệu chuẩn, trên CIFAR-10, 150 vòng, theo ngân sách mẫu ảo $M_c$ và nồng độ Dirichlet $\beta$ (quy ước ở Bảng 5.4). Hàng $\beta = 0{,}05$ gồm ba hạt giống (+3,88 / +4,30 / +4,90); các hàng còn lại chỉ có hạt giống 42. Đơn vị: điểm phần trăm.

| $M_c$ | $\beta$ | Mức chênh |
|---|---|---|
| 100 | 0,1 | +0,29 |
| 100 | 0,3 | −0,76 |
| 2000 | 0,1 | +0,97 |
| 2000 | 0,05 | +4,36 ± 0,51 |

Ở ngân sách 100 mẫu mỗi lớp, CCVR cải thiện mô hình ở $\beta = 0{,}1$ nhưng làm mô hình kém đi ở $\beta = 0{,}3$. Cùng một phương pháp cho hai dấu ngược nhau chỉ vì mức lệch thay đổi. Hai hàng $M_c = 100$ và hai hàng $M_c = 2000$ không so được trực tiếp với nhau: chúng dùng hai lần huấn luyện backbone khác nhau, và tốc độ học của bước huấn luyện lại cũng đổi từ 0,01 sang 0,001 cùng lúc với ngân sách. Kết luận rút ra được là giới hạn: một con số đo tại một điểm ngân sách không mô tả được phương pháp. Mức cải thiện phải được báo cáo như một đường đặc tuyến theo ngân sách, hoặc ít nhất kèm theo ngân sách tại đó nó được đo; mục 5.1.2 áp quy tắc thứ hai cho mọi con số của luận văn.

**Bảng 5.8.** Bốn cách huấn luyện lại tầng phân lớp từ cùng một thống kê lớp, trên cùng mô hình đã huấn luyện 150 vòng với Dirichlet $\beta = 0{,}05$, $M_c = 2000$, $d = 512$, tức $M_c/d \approx 3{,}9$. Hiệu so với mô hình trước hiệu chuẩn, trung bình ± độ lệch chuẩn mẫu, $n = 3$; độ chính xác trước hiệu chuẩn là 54,66 / 54,55 / 48,14%. Hàng "hội tụ" và dòng "LDA − Newton" lấy từ một lượt chạy riêng trên cùng ba hạt giống, trong đó LDA đạt +6,39 ± 1,24. CINIC-10 chứa ảnh của CIFAR-10, nên cột CINIC-10 chỉ để đọc mô tả, không dùng để suy luận thống kê. Đơn vị: điểm phần trăm.

| Head | CIFAR-10 | CINIC-10 |
|---|---|---|
| LDA dạng đóng | +6,45 ± 1,29 | +5,93 ± 0,33 |
| CCVR | +4,41 ± 1,19 | +4,26 ± 0,12 |
| Newton cross-entropy, một bước | +2,98 ± 1,04 | +1,95 ± 3,17 |
| Bậc nhất, một bước | +0,36 ± 0,12 | +0,24 ± 0,08 |
| Newton cross-entropy, hội tụ | +6,14 ± 1,37 | +5,65 ± 0,28 |
| Bậc nhất tốt nhất (tốc độ học 0,1, 2000 bước) | +5,29 ± 1,09 | +5,32 ± 0,29 |
| **LDA − Newton hội tụ** | **+0,25 ± 0,18** | **+0,35 ± 0,06** |

Thứ hạng khớp với dự đoán của Chương 3. Trên tác vụ ảo sinh từ phân phối Gauss, head LDA dạng đóng cho mức cải thiện cao nhất. Các head phân biệt, khi được tối ưu tới hội tụ, tiến sát LDA nhưng vẫn thấp hơn ở cả ba hạt giống trên CIFAR-10 (0,31 / 0,39 / 0,05 điểm). Phép đo ở $M_c/d \approx 3{,}9$, tức chế độ mẫu hữu hạn, nên thứ hạng này không ngoại suy sang các ngân sách mẫu ảo khác.

### 5.2.4. Dạng thiên lệch của tầng phân lớp

Hai giả thuyết của Chương 3 được kiểm tra trên ba mô hình của hàng $\beta = 0{,}05$, $M_c = 2000$ ở Bảng 5.7, trước và sau khi hiệu chuẩn bằng CCVR.

Tỉ số giữa chuẩn $\ell_2$ lớn nhất và nhỏ nhất của các vector trọng số theo lớp ở tầng cuối là 1,099, 1,147 và 1,172 theo từng hạt giống, tức các chuẩn gần như bằng nhau. Độ lệch ở số hạng tự do cũng nhỏ: trung bình trị tuyệt đối của $b_c$ khoảng 0,16, so với chuẩn trung bình của $w_c$ khoảng 1,17. Trong khi đó, hiệu chuẩn lại tầng cuối nâng recall của lớp kém nhất từ 18,0% lên 61,9% (lớp tàu thuỷ, hạt giống 42), từ 16,9% lên 61,8% (lớp chó, hạt giống 43), và từ 22,3% lên 48,6% (lớp hươu, hạt giống 44). Lớp kém nhất được xác định sau khi đo, riêng cho từng hạt giống.

Một chênh lệch chuẩn dưới 20% không thể tạo ra biến thiên recall cỡ 26 đến 45 điểm nếu thiên lệch nằm ở độ lớn. Số đo vì vậy ủng hộ giả thuyết thứ hai: thiên lệch nằm ở hướng của ranh giới quyết định, và hiệu chuẩn xoay ranh giới ấy. Phát hiện này đo trên một họ kiến trúc không dùng chuẩn hoá theo lô, và một backbone có chuẩn hoá có thể định hình lại nó; luận văn không chạy kiểm soát kiến trúc, nên giả thiết rằng phát hiện độc lập với kiến trúc vẫn chưa được kiểm tra.

### 5.2.5. Những gì chuyển sang các mục sau

Ba kết quả của mục này được mang sang phần còn lại của chương, ở mức cơ chế. Dưới lệch phân phối nhãn, FedMix như đang được cài đặt không cải thiện so với FedAvg. Mức cải thiện của nhóm hiệu chuẩn tầng phân lớp phụ thuộc ngân sách mẫu ảo và có thể đổi dấu. Thiên lệch của tầng phân lớp mang tính định hướng. Mục 5.3 chuyển sang nền tảng FedBR, nơi lệch nhãn đi kèm lệch đặc trưng do phép xoay, và so FedMix với các cách dùng mẫu trung bình khác; con số của hai nền tảng không được đem so với nhau.

---

## Truy vết — không chép vào Word

Gốc đường dẫn: `C:\Users\KietVu\Testplace\uit-msc-dp-adaptive-fedmix\`. Tra thêm ở `INDEX_ma-nguon-va-ket-qua.md` §3.

| Bảng / số liệu | Tệp thô | Tái tính |
|---|---|---|
| Bảng 5.4 | `configs/cifar10/paper_k2.yaml`, `configs/cifar10/fedmix.yaml`, `configs/cifar10/dirichlet_sweep/ccvr_b005_paperhp.yaml`, `runs/runs/e2/config_resolved.yaml` | — |
| Đối chiếu bản cài đặt FedMix khác (DevPranjal; tên không đưa vào Word) | `runs/_archive/hydra_reference/results/cifar10_{0,1}/`; `docs/reproductions/REPRODUCTION_CIFAR10_GATE.md:57–69` | — |
| Bảng 5.5 | `runs/_archive/fedmca_closed/negative_k2/{fedavg,fedmix}_cifar10_k2{,_s43,_s44}/<ts>/metrics.csv`; timestamp đúng ở chỉ mục §3 | `python -m scripts.aggregate_negatives_k2 --log-root runs/_archive/fedmca_closed/negative_k2` |
| Cận trên −0,52 / +0,16 / +0,38 | tính từ các hiệu theo hạt giống, $t_{0,95;2} = 2{,}920$ | chỉ mục F2 |
| Số hạng bậc hai tại khởi tạo | `docs/reproductions/REPRODUCTION_FEDMCA_C1_GATE.md:55` | `scripts/check_t2_magnitude.py` |
| Số hạng bậc hai trên mô hình đã huấn luyện (0,039 / 0,224 / 0,025) | `runs/gate_2nd/second_order_gate.json`, trường `trained.seed4x.m1.ratio_B_over_A` | `experiments/run_second_order_gate.py` |
| Bảng 5.6 | C1: `negative_k2/fedmca_c1_cifa10_k2` (s42), `fedmca_c1_cifar10_k2_{s43,s44}`; C1+C2: `runs/fedtc/*_b030_screen` (s42), `runs/_archive/fedmca_closed/*_screen_s43/s44` | C1: script trên; C1+C2: tự tính từ `metrics.csv` |
| Bảng 5.7 | $M_c=100$: `runs/_archive/void_superseded/fedtc4/ccvr_cifar10_dir_b0{10,30}_screen/`; $M_c=2000$: `runs/fedtc5/ccvr_b010_paperhp`, `runs/fedtc5/ccvr_b005_paperhp{,_s43,_s44}` (`calibration_metrics.json`) | `scripts/make_paper_figures.py` `make_fig1` |
| Bảng 5.8 | `runs/runs/e2/head_methods_summary.json`, `runs/runs/e2_cinic/…`; hàng hội tụ: `runs/runs/e3/e3_fair_baselines.json`, `runs/runs/e3_cinic/…` | `experiments/run_head_methods.py`, `experiments/run_e3_fair_baselines.py` |
| Mục 5.2.4 | `runs/fedtc5/ccvr_b005_paperhp*/calibration_metrics.json`: `head_weight_l2_before`, `recall_before`, `recall_after`, `head_bias_before` | `make_paper_figures.py` `make_fig2` |

⚠️ **Ba điểm cần biết khi bảo vệ:**
- Hàng $M_c = 100$ của Bảng 5.7 nằm trong thư mục `void_superseded`: đây là các lượt screen cũ, được giữ vì là lượt duy nhất ở ngân sách đó.
- Mục 5.2.3 nói thẳng rằng ngân sách và tốc độ học huấn luyện lại đổi cùng lúc giữa hai nhóm hàng. Không viết lại theo kiểu "trên cùng một checkpoint" (chỉ mục F6).
- Chỉ số "tỉ số bậc hai / bậc nhất trên mô hình đã huấn luyện" lấy nhánh Hessian (`ratio_B_over_A`). Không dùng các tỉ số có hậu tố `_gn`, vì chúng chuẩn hoá không nhất quán (chỉ mục F4).

---

## 5.3. So sánh các cách dùng mẫu trung bình trên nền tảng FedBR

### 5.3.1. Tái hiện bảng CIFAR-10 của FedBR — `[BẢN NHÁP, n = 1]`

Bảng 5.9 đặt kết quả chạy lại trên nền tảng FedBR cạnh bảng CIFAR-10 của bài báo FedBR [2]. Cấu hình theo Bảng 5.2, chỉ số theo mục 5.1.2.

Như mọi kết quả trên nền tảng này, bảng đến từ một hạt giống. Bảng có hai vai trò: đối chiếu với con số đã công bố, và cho thước đo dao động mà mục 5.1.3 dùng để đọc các phép so sánh.

**Bảng 5.9.** Độ chính xác (%) trên CIFAR-10 xoay, 10 client, 1000 vòng, VGG11 không chuẩn hoá ($d = 512$). Cột thứ hai là giá trị công bố trong Bảng 1 của [2]; cột thứ ba là lượt chạy lại trên nền tảng FedBR với hạt giống 12345. Chỉ số của cả hai cột là trung bình năm độ chính xác cao nhất theo vòng trên phần dữ liệu giữ lại của các client. FedMix chạy với $\lambda = 0{,}1$ và cách chuẩn hoá ở Chương 4, mục 4.3, tức số hạng Taylor nhỏ hơn (3.15) 32 lần.

| Thuật toán | Công bố [2] | Chạy lại | Chênh |
|---|---|---|---|
| FedAvg | 58,99 | 59,45 | +0,46 |
| FedProx | 59,14 | 59,14 | 0,00 |
| Moon | 58,23 | 52,95 | −5,28 |
| DANN | 58,29 | 55,60 | −2,69 |
| GroupDRO | 56,57 | 59,23 | +2,66 |
| FedBR | 64,65 | 65,82 | +1,17 |
| FedAvg + Mixup | 58,57 | 59,44 | +0,87 |
| FedMix | 57,37 | 57,16 | −0,21 |
| FedBR + Mixup | 65,32 | 66,47 | +1,15 |

Sáu trong chín thuật toán cho kết quả cách giá trị công bố không quá 1,2 điểm. Moon thấp hơn 5,28 điểm. Đây là thuật toán mang một lỗi trong danh mục kiểm toán ở Phụ lục A: mô hình cục bộ của vòng trước, thứ mà hàm mất mát tương phản của Moon cần, không bao giờ được cập nhật. DANN thấp hơn 2,69 điểm và GroupDRO cao hơn 2,66 điểm; luận văn không tìm nguyên nhân của hai chênh lệch này, và dùng chúng để đặt ngưỡng đọc ba điểm ở mục 5.1.3.


### 5.3.2. Các cách dùng mẫu trung bình

Bảng 5.10 đặt các cách dùng mẫu trung bình cạnh FedAvg và FedProx, trên cùng lượt chạy của Bảng 5.9.

**Bảng 5.10.** Hiệu theo cặp so với FedAvg trên nền tảng FedBR (CIFAR-10 xoay, 10 client, 1000 vòng, VGG11 không chuẩn hoá, $d = 512$), hạt giống 12345. "Chỉ số chính" là trung bình năm độ chính xác cao nhất theo vòng; "năm mốc cuối" là trung bình năm mốc đánh giá cuối cùng; cả hai đo trên phần dữ liệu giữ lại của các client, đơn vị %. FedMix và NaiveMix dùng $\lambda = 0{,}1$; FedMix dùng cách chuẩn hoá ở Chương 4, mục 4.3, tức số hạng Taylor nhỏ hơn (3.15) 32 lần. Ngưỡng đọc 3 điểm theo mục 5.1.3.

| Thuật toán | Chỉ số chính | Hiệu | Năm mốc cuối | Hiệu |
|---|---|---|---|---|
| FedAvg | 59,45 | — | 57,70 | — |
| FedProx | 59,14 | −0,31 | 57,79 | +0,09 |
| FedAvg + Mixup | 59,44 | −0,01 | 59,08 | +1,38 |
| FedMix (S2) | 57,16 | −2,29 | 57,12 | −0,58 |
| NaiveMix | `[CHỜ SỐ LIỆU: T1]` | | | |
| FedBR (S1) | 65,82 | +6,37 | 65,05 | +7,35 |
| FedBR + Mixup | 66,47 | +7,02 | 65,88 | +8,18 |

S1 vượt ngưỡng đọc ở cả hai chỉ số: FedBR hơn FedAvg 6,37 điểm theo chỉ số chính và 7,35 điểm theo năm mốc cuối. Bảng 1 của [2] cho FedBR hơn FedAvg 5,66 điểm, cùng chiều và cùng cỡ. FedBR + Mixup cho hiệu cùng cỡ với FedBR.

S2 nằm dưới ngưỡng. FedMix kém FedAvg 2,29 điểm theo chỉ số chính, còn [2] báo cáo kém 1,62 điểm. Theo năm mốc cuối, hiệu co lại còn −0,58 điểm: đường học của FedAvg lên đỉnh cao hơn rồi giảm dần về cuối, còn của FedMix gần như phẳng giữa hai chỉ số. Trên nền tảng này, một hạt giống không phân biệt được FedMix với FedAvg; điều đọc được là cả hai chỉ số đều không cho thấy FedMix cải thiện. Trên nền tảng Flower, mục 5.2.2 đã loại trừ khả năng FedMix cải thiện ở cấu hình của nó; hai nền tảng vì vậy không mâu thuẫn nhau ở mức cơ chế.

Hàng NaiveMix chờ lượt chạy T1. Nếu có, hiệu FedMix − NaiveMix được đọc theo mục 5.1.4 và ngưỡng ở mục 5.1.3.

`[VIẾT]` Một đoạn mức cơ chế về FedBR chạy trên nền tảng Flower, theo cấu hình của bài FedBR (10 client, Dirichlet $\alpha = 0{,}1$, xoay, VGG11, lô 32, 50 bước cục bộ), 500 vòng, một hạt giống: hiệu FedBR − FedAvg theo chỉ số chính là −0,23 điểm khi có tăng cường dữ liệu (57,26 so với 57,49) và +0,86 điểm khi không có (56,04 so với 55,18), cả hai dưới ngưỡng. Lợi thế của FedBR không lặp lại ở đó. Nguồn: `INDEX` §4.3. Nêu rõ 500 so với 1000 vòng; không so con số tuyệt đối với Bảng 5.10 (IR#4).

### 5.3.3. Mẫu trung bình còn giữ bao nhiêu thông tin cho tầng phân lớp

Mục 5.2.3 cho thấy, trên nền tảng Flower, huấn luyện lại tầng phân lớp trên thống kê đặc trưng toàn cục là can thiệp cho mức cải thiện lớn nhất. Mục này dùng chính can thiệp đó làm phép đo: huấn luyện lại tầng phân lớp trên mẫu trung bình thì mô hình được lợi hay bị hại, và điều đó đổi thế nào theo số ảnh $M$ gộp trong mỗi mẫu. Câu trả lời cho biết mẫu trung bình còn giữ bao nhiêu thông tin về ranh giới giữa các lớp.

Thủ tục như sau. Lấy mô hình toàn cục ở vòng cuối của mỗi thuật toán trong Bảng 5.9 và đóng băng bộ trích xuất đặc trưng $\phi$. Mỗi client dựng 2000 mẫu trung bình theo (3.11), mỗi mẫu gộp $M$ ảnh rút ngẫu nhiên từ dữ liệu huấn luyện của client đó, kèm nhãn mềm là histogram nhãn của $M$ ảnh ấy. Máy chủ tính đặc trưng $\phi(\bar x)$ của 20 000 mẫu, rồi thay tầng phân lớp $\omega$ bằng bộ phân lớp LDA dạng đóng như ở mục 5.2.3: trung bình theo lớp lấy trọng số theo nhãn mềm, một ma trận hiệp phương sai chung co về $(\mathrm{tr}/d)\,I$ với hệ số 0,01, tiên nghiệm đều. Độ chính xác được đo trên phần dữ liệu giữ lại của các client, tức cùng tập với chỉ số chính của Bảng 5.9, trước và sau khi thay tầng phân lớp. $M$ quét trên $\{1, 2, 3, 5, 10\}$; $M = 1$ là trường hợp chia sẻ ảnh thô và đóng vai trò cận trên, còn $M = 10$ là giá trị mà FedMix và FedBR dùng trong Bảng 5.2.

Lượng dữ liệu được chia sẻ ở đây lớn hơn nhiều so với khung ở Chương 4. Theo (4.1), chiều lên với $N = 10$, $n_V = 2000$, $d_x = 3072$, $C_y = 10$ và 4 byte mỗi giá trị là khoảng 247 MB, trả một lần; mẫu trung bình không phải phát lại cho client, vì máy chủ tự huấn luyện lại tầng phân lớp rồi phát cùng mô hình. Con số này vẫn nhỏ hơn lưu lượng của một vòng truyền thông (khoảng 738 MB, mục 4.4), nhưng lớn gấp nhiều lần tập pseudo-data 32 mẫu của FedBR.

**Bảng 5.11.** Mức thay đổi độ chính xác trên phần dữ liệu giữ lại (điểm phần trăm) khi thay tầng phân lớp của mô hình vòng cuối bằng bộ phân lớp LDA huấn luyện trên 2000 mẫu trung bình mỗi client, theo số ảnh mỗi mẫu $M$. Cột "Trước" là độ chính xác của mô hình vòng cuối trên cùng tập, hạt giống 12345; giá trị này khác cột "Chạy lại" của Bảng 5.9, vốn là trung bình năm vòng cao nhất. Moon mang lỗi nêu ở Phụ lục A, nên hàng của nó chỉ để tham khảo.

| Thuật toán | Trước | $M=1$ | $M=2$ | $M=3$ | $M=5$ | $M=10$ |
|---|---|---|---|---|---|---|
| FedAvg | 55,98 | +5,83 | +3,27 | −1,60 | −7,81 | −16,39 |
| FedProx | 56,94 | +4,12 | +1,97 | −2,46 | −9,24 | −16,51 |
| GroupDRO | 57,54 | +3,94 | +2,09 | −1,33 | −6,73 | −14,12 |
| DANN | 55,14 | +4,52 | +1,85 | −2,34 | −8,47 | −14,02 |
| FedAvg + Mixup | 59,83 | +1,03 | −0,16 | −3,66 | −8,59 | −13,89 |
| FedMix | 57,21 | +4,84 | +2,51 | −3,38 | −12,48 | −25,33 |
| FedBR | 65,92 | +1,34 | −0,19 | −6,02 | −17,58 | −54,46 |
| FedBR + Mixup | 65,64 | +1,73 | +0,96 | −2,64 | −12,30 | −46,23 |
| Moon | 46,61 | +10,95 | +8,68 | +3,24 | −5,04 | −12,96 |

![Hình 5.1](figures/hinh5_1.png)

**Hình 5.1.** Số liệu của Bảng 5.11 vẽ theo $M$. Bốn đường màu là FedAvg, FedProx, FedMix và FedBR; bốn đường xám liền là GroupDRO, DANN, FedAvg + Mixup và FedBR + Mixup; đường xám đứt là Moon. Ba giá trị tại $M = 10$ nằm dưới trục được ghi ở góc trên bên phải.

Bảng 5.11 cho ba nhận xét.

Thứ nhất, phép lấy trung bình làm mất thông tin hiệu chuẩn rất nhanh. Mức cải thiện chỉ còn dương ở $M \le 2$, chuyển sang âm ở $M = 3$ với mọi thuật toán trừ Moon, và ở $M = 10$ việc hiệu chuẩn làm giảm độ chính xác của mọi mô hình, từ 14 đến 54 điểm. Với ngân sách 2000 mẫu mỗi client, ảnh trung bình của mười ảnh không giữ đủ thông tin để huấn luyện lại tầng phân lớp, trong khi ảnh thô thì đủ. Kết quả này trả lời một phần RQ3: lượng thông tin mà kênh mẫu trung bình còn giữ ở $M = 10$ thấp hơn mức cần cho hiệu chuẩn tầng phân lớp.

Thứ hai, ở cận trên $M = 1$, mức cải thiện tách hai họ thuật toán. Các phương pháp không tác động trực tiếp lên tầng phân lớp trong huấn luyện được từ +3,9 đến +5,8 điểm; FedBR và FedBR + Mixup chỉ được +1,3 và +1,7. Sau khi cả hai được hiệu chuẩn, FedBR đạt 67,26% còn FedAvg đạt 61,81%. Trong khoảng cách 9,9 điểm giữa hai mô hình vòng cuối, khoảng 4,5 điểm biến mất khi cả hai được huấn luyện lại tầng phân lớp trên ảnh thô, còn khoảng 5,4 điểm vẫn giữ nguyên. Cả hai phần đều vượt ngưỡng đọc ở mục 5.1.3. Điều này phù hợp với vai trò của $L_{\text{bal}}$ trong (3.19): thành phần cân bằng tầng phân lớp của FedBR đã làm trong lúc huấn luyện phần việc mà hiệu chuẩn sau huấn luyện làm cho FedAvg.

Thứ ba, chính FedBR sụt mạnh nhất ở $M = 10$. Thành phần tương phản (3.17) của FedBR kéo đặc trưng của pseudo-data, vốn là ảnh trung bình mười ảnh, ra xa đặc trưng của ảnh thật cục bộ. Bộ trích xuất của FedBR vì vậy đặt ảnh trung bình $M = 10$ vào một vùng đặc trưng cách biệt với ảnh thật, và một tầng phân lớp học trên vùng đó không chuyển được sang ảnh thật. Đây là suy luận từ cấu trúc hàm mất mát, chưa được đo trực tiếp.

Hai kiểm tra bổ sung được chạy để loại trừ cách giải thích khác. Với 200 mẫu mỗi client, tức 200 mẫu cho mỗi lớp trong không gian $d = 512$ chiều, bộ phân lớp LDA thua mô hình gốc ở mọi $M$; đây là chế độ mẫu hữu hạn mà mục 3.6 mô tả, và tỉ số $M_c/d$ nhỏ hơn mười lần so với mục 5.2.3. Huấn luyện lại tầng phân lớp bằng cross-entropy với nhãn mềm, ở hai cấu hình tốc độ học, cho cùng thứ tự các thuật toán tại $M = 1$ với biên độ nhỏ hơn LDA (FedAvg +4,6, FedBR +0,6) và cùng chiều giảm theo $M$.

Mọi số ở mục này đến từ hạt giống 12345 và mô hình vòng cuối. Chiều giảm theo $M$ lặp lại ở cả chín mô hình và lớn hơn nhiều so với ngưỡng đọc ở mục 5.1.3, nên nó đứng được với một hạt giống. Điểm chung với mục 5.2.3 nằm ở cơ chế: trên cả hai nền tảng, huấn luyện lại tầng phân lớp trên dữ liệu có phân phối nhãn cân bằng nâng được độ chính xác của FedAvg.

## 5.4. Chi phí tài nguyên — `[BẢN NHÁP]`

Chi phí truyền thông phụ trội tính theo công thức (4.1) của Chương 4. Chi phí tính toán lấy từ thời gian mỗi bước ghi trong nhật ký của lượt chạy ở Bảng 5.9.

**Bảng 5.12.** Thời gian huấn luyện quy về 1000 vòng truyền thông, lượt chạy một hạt giống ở Bảng 5.9. Cột cuối là tỉ lệ so với FedAvg. `[CẦN ĐIỀN: loại GPU]`.

| Thuật toán | Giờ / 1000 vòng | So với FedAvg |
|---|---|---|
| FedAvg | 2,3 | 1,0× |
| FedProx | 2,7 | 1,2× |
| FedMix | 5,8 | 2,5× |
| FedBR | 7,5 | 3,3× |
| FedBR + Mixup | 7,6 | 3,3× |

FedMix tốn gấp khoảng hai lần rưỡi FedAvg, chủ yếu do phải lấy gradient theo đầu vào rồi lan truyền ngược qua chính gradient đó, tức lan truyền ngược hai lần. FedBR tốn gấp khoảng ba lần, do có thêm bước tối đa hoá trên tầng chiếu.

⚠️ **Hai việc trước khi dùng bảng này:**
- **Nguyên nhân chi phí của FedMix và FedBR.** Hai câu giải thích trên là suy luận từ cấu trúc mã, chưa được đo tách riêng. Nếu không đo thì viết dạng *"có thể do…"* hoặc bỏ đi.
- **Cột bộ nhớ.** `summary.csv` ghi bộ nhớ đỉnh bằng 0,0 GB cho FedAvg, FedProx và FedMix, nhưng 3,1 GB cho FedBR. Nhiều khả năng đây là lỗi ghi nhận chứ không phải số đo, nên cột bộ nhớ **không đưa vào luận văn** cho tới khi kiểm lại `mem_gb` trong `results.jsonl`.

## 5.6. Tổng hợp và thảo luận

`[CHỜ SỐ LIỆU: tất cả]` Trả lời RQ1–RQ4, mỗi câu một đoạn, kèm điều kiện hiệu lực; threats to validity.

---

## Truy vết mục 5.3–5.4 — không chép vào Word

| Số liệu | Tệp thô |
|---|---|
| Bảng 5.2 (cấu hình nền tảng FedBR) | dòng đầu của `results.jsonl` mỗi thuật toán trong `C:\Users\KietVu\Testplace\FedBR\output\cifar10\02_attempt_20260916\`, trường `args` (`holdout_fraction` 0,2; `checkpoint_freq` 250 bước = 5 vòng; `local_steps` 50; `steps` 50000) và `hparams` (`lr` 0,01; `momentum` 0; `weight_decay` 0; `data_augmentation` true; `fedbr_tau1/tau2` 2; `fedbr_mu` 0,5; `fedbr_lambda` 1,0); hạt giống: `Makefile`, biến `SEEDS` |
| Bảng 5.9, cột "Chạy lại" | `C:\Users\KietVu\Testplace\FedBR\output\cifar10\02_attempt_20260916\summary.csv` (cột `Acc (%)`); đã tái tính khớp từ từng `results.jsonl` (`INDEX` §5.2) |
| Bảng 5.10 | cùng thư mục, `<thuật toán>/results.jsonl`: độ chính xác mỗi mốc = trung bình `env00_out_acc` … `env09_out_acc`; chỉ số chính = trung bình 5 mốc cao nhất (khớp `summary.csv`), năm mốc cuối = trung bình 5 mốc cuối trong 201 mốc. Hiệu Bảng 1 của [2]: FedBR − FedAvg = 64,65 − 58,99 = 5,66; FedMix − FedAvg = 57,37 − 58,99 = −1,62 |
| Bảng 5.9, cột "Công bố" | `paper/ref/Guo et al. - 2023 - FedBR….pdf`, Bảng 1, cột CIFAR10 (VGG11) |
| Bảng 5.11, Hình 5.1 | `C:\Users\KietVu\Testplace\FedBR\output\cifar10\02_attempt_20260916\calibrate_head_lda2000\*.json` ($M = 1, 2$) và `…\calibrate_head_lda2000_M3-10\*.json` ($M = 3, 5, 10$), trường `baseline.local` và `rows[].delta.local`; sinh bằng `make calibrate-head OUT=… CALIB_ARGS="--M … --n_per_client 2000 --method lda --eval_envs local"`. Hai kiểm tra bổ sung: `…\calibrate_head\` (200 mẫu/client, CE và LDA, cả global) và `…\calibrate_head_ce_lr01\`. Bảng tổng hợp ở `INDEX` §5.2b. Hình: `figures/hinh5_1.py` |
| Bảng 5.12 | cùng `summary.csv`, cột `h/1000rd` |
| Port FedBR lên Flower | kho Flower `runs/paper_{fedavg,fedbr}_rot{,_noaug}_r500/` |
