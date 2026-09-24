# CHƯƠNG 5 — THỰC NGHIỆM (hướng B)

> **KHỐI TRẠNG THÁI** · 24/09/2026
>
> | Mục | Trạng thái | Chờ |
> |---|---|---|
> | 5.1 Thiết lập | `[VIẾT]` — bảng cấu hình mã FedBR lấy từ bản ghi `args`/`hparams` đầu mỗi `results.jsonl` của `02_attempt` | — |
> | 5.2 Flower, lệch nhãn | `[ĐÃ VIẾT]` — mang sang từ `archive/…/05_chuong5.md` (khối 24/09), sửa bốn câu cho khớp hướng B (liệt kê dưới) | — |
> | 5.3.1 Tái hiện bảng FedBR | `[BẢN NHÁP, n = 1]` — số liệu `02_attempt`; bổ sung hạt giống khi T0 xong | T0 |
> | 5.3.2 So sánh các cách dùng mẫu trung bình | `[CHỜ SỐ LIỆU]` | T0, T1 |
> | 5.3.3 Kiểm toán mã FedBR | `[SỬA]` — dùng lại D1–D13 ở `archive/…/05_chuong5.md` §5.2.2–5.2.6, thêm phép chuẩn hoá $1/B$, viết lại "xác nhận âm tính" | — |
> | 5.4 Chi phí tài nguyên | `[BẢN NHÁP, n = 1]` | T0 |
> | 5.5 FedBR + Taylor | chỉ khi A có số liệu | T2 |
> | 5.6 Tổng hợp | `[CHỜ SỐ LIỆU]` | tất cả |
>
> **Bốn câu của mục 5.2 đã sửa so với bản trong `archive/`** (đã thi hành trong văn bản dưới):
> 1. 5.2.2: *"Chương 4, mục 4.2.3"* → *"Chương 4, mục 4.3"*; *"được đo ở các mục sau"* → *"được đo ở mục 5.3.2"*.
> 2. 5.2.3: câu cuối đoạn sau Bảng 5.4 không còn hứa Chương 4 dựng giao thức đường đặc tuyến, vì hướng B không quét ngân sách; thay bằng quy tắc *"kèm ngân sách tại đó nó được đo"*.
> 3. 5.2.4: kiểm soát kiến trúc không nằm trong kế hoạch hướng B → nói thẳng là không chạy.
> 4. 5.2.5: câu cuối trỏ sang mục 5.3 và mô tả đúng dạng lệch của nền tảng FedBR (lệch nhãn kèm xoay).
>
> **Đánh số bảng:** Bảng 5.1–5.5 thuộc mục 5.2; mục 5.3 bắt đầu từ Bảng 5.6.
>
> ⛔ **IR#10:** mục nào chưa có dữ liệu thì để `[CHỜ SỐ LIỆU: <mức>]`, không điền số dự kiến.

**Ánh xạ sang Word.** Word hiện có hai tiêu đề: *5.1 Thiết lập thực nghiệm* và *5.2 Tái hiện và kiểm toán tính tái lập*. Đổi thành:

| Word hiện tại | Sau khi sửa |
|---|---|
| 5.1 Thiết lập thực nghiệm | 5.1 Thiết lập thực nghiệm (giữ) |
| — | **5.2 Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower** (chèn, cùng 5.2.1–5.2.5) |
| 5.2 Tái hiện và kiểm toán tính tái lập | **5.3 So sánh các cách dùng mẫu trung bình trên mã nguồn FedBR** (đổi tên; 5.3.1 Tái hiện · 5.3.2 So sánh · 5.3.3 Kiểm toán mã nguồn) |
| — | 5.4 Chi phí tài nguyên · 5.6 Tổng hợp và thảo luận (chèn; 5.5 chỉ khi có A) |

---

## 5.1. Thiết lập thực nghiệm

`[VIẾT]` Đoạn mở giới thiệu hai nền tảng (câu mẫu ở `archive/…/05_chuong5.md`, khối 24/09 *"Luận văn chạy thực nghiệm trên hai nền tảng…"*, sửa vế cuối thành *"…chạy trên mã nguồn FedBR"*). Sau đó là bảng cấu hình mã FedBR theo `PLAN_huong-B.md` §2. Tham số Dirichlet ghi đủ bộ ba theo quy tắc của Chương 3.


---

## 5.2. Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower

Mục này đo ba điều dưới lệch phân phối nhãn: FedMix có cải thiện so với FedAvg hay không; mức cải thiện của nhóm hiệu chuẩn tầng phân lớp từ thống kê lớp phụ thuộc thế nào vào ngân sách mẫu ảo; và thiên lệch của tầng phân lớp nằm ở độ lớn hay ở hướng. Các thực nghiệm chạy trên một nền tảng mô phỏng dựng bằng Flower, mô hình huấn luyện từ đầu. Nền tảng này khác mã nguồn FedBR ở cách phân hoạch, số client, backbone và tập thuật toán đối chứng, nên con số của mục này không đặt cạnh con số của các mục sau; các mục sau chỉ đối chiếu với nó ở mức cơ chế.

### 5.2.1. Thiết lập

**Bảng 5.1.** Thiết lập thực nghiệm trên nền tảng Flower. $\beta$ là nồng độ Dirichlet **mỗi thành phần**, lấy mẫu trên trục **client** cho từng lớp, với 60 thành phần ứng với 60 client; nồng độ càng nhỏ thì lệch càng nặng. $M_c$ là số đặc trưng ảo sinh cho mỗi lớp khi huấn luyện lại tầng phân lớp; $d$ là số chiều đặc trưng.

| Thành phần | Giá trị |
|---|---|
| Khung | Flower, chế độ mô phỏng |
| Dữ liệu | CIFAR-10; CINIC-10 chỉ dùng cho phép so sánh các head hiệu chuẩn |
| Client | 60, mỗi vòng chọn 15 |
| Huấn luyện cục bộ | 2 epoch, lô 10, SGD với tốc độ học 0,01 giảm theo hệ số 0,999 mỗi vòng, không momentum, không weight decay |
| Backbone | VGG sửa đổi theo phụ lục bài báo FedMix [1]: 6 tầng tích chập và 3 tầng kết nối đầy đủ, không chuẩn hoá theo lô, $d = 512$ |
| Phân hoạch | hai lớp mỗi client, 500 vòng (phép so sánh FedMix); Dirichlet $\beta \in \{0{,}05;\ 0{,}1;\ 0{,}3\}$, 150 vòng (hiệu chuẩn tầng phân lớp) |
| FedMix | $\lambda = 0{,}05$; mỗi client gửi một ảnh trung bình của toàn bộ dữ liệu cục bộ kèm nhãn mềm; mỗi lô cục bộ ghép với một ảnh trung bình rút ngẫu nhiên |
| Hiệu chuẩn | CCVR [7] với $M_c \in \{100;\ 2000\}$, biến đổi Tukey 0,5, huấn luyện lại tầng cuối 10 epoch; head LDA dùng hiệp phương sai gộp co về đường chéo với hệ số 0,01 |
| Hạt giống | 42, 43, 44 |

Chỉ số của phép so sánh FedMix là độ chính xác cao nhất theo vòng trên tập kiểm tra. Chỉ số của phép hiệu chuẩn là chênh lệch độ chính xác trước và sau khi hiệu chuẩn, đo trên cùng một mô hình đã huấn luyện. Mọi dấu $\pm$ trong mục này là độ lệch chuẩn mẫu của ba hiệu theo cặp, mỗi hiệu ứng với một hạt giống.

Bài báo FedMix không công bố mã nguồn. Nền tảng được đối chiếu với bản cài đặt mã mở của DevPranjal, chạy trên cùng cấu hình với hạt giống 42. Hai bên chênh nhau khoảng 3 điểm phần trăm ở độ chính xác tuyệt đối (FedAvg 65,81% so với 68,69%; FedMix 63,67% so với 66,50%), nhưng hiệu theo cặp gần như trùng: −2,14 và −2,19 điểm. Vì bản cài đặt đó cũng là mốc mà nền tảng được hiệu chỉnh theo, phép đối chiếu này là một kiểm tra tính nhất quán, không phải một phép kiểm chứng độc lập.

### 5.2.2. FedMix so với FedAvg

**Bảng 5.2.** Độ chính xác cao nhất theo vòng (%) của FedAvg và FedMix trên CIFAR-10, phân hoạch hai lớp mỗi client, 500 vòng, backbone VGG không chuẩn hoá ($d = 512$), $\lambda = 0{,}05$. Cột cuối là hiệu theo cặp FedMix − FedAvg, đơn vị điểm phần trăm. Hàng cuối: trung bình ± độ lệch chuẩn mẫu, $n = 3$.

| Hạt giống | FedAvg | FedMix | Hiệu |
|---|---|---|---|
| 42 | 68,69 | 66,50 | −2,19 |
| 43 | 67,42 | 66,47 | −0,95 |
| 44 | 64,74 | 62,31 | −2,43 |
| | | | **−1,86 ± 0,79** |

FedMix kém FedAvg ở cả ba hạt giống. Với ba quan sát, riêng dấu của hiệu không đủ làm bằng chứng: khi không có hiệu ứng, xác suất để ba hiệu cùng dấu đã là 0,25. Phát biểu dựa vào khoảng tin cậy thì chặt hơn. Với $t_{0{,}95;\,2} = 2{,}920$, cận trên của khoảng tin cậy 95% một phía là −0,52 điểm, nên ở cấu hình này khả năng FedMix cải thiện được loại trừ.

Kết luận phụ thuộc vào chỉ số. Lấy độ chính xác ở vòng cuối thay cho vòng tốt nhất, ba hiệu là −3,55, −4,49 và +0,59: trung bình vẫn âm nhưng một hạt giống đổi dấu.

Bản cài đặt này có cùng đặc điểm với mọi bản cài đặt FedMix mã mở mà luận văn đối chiếu: số hạng Taylor được lấy trung bình trên lô hai lần, nên đi vào mục tiêu với hệ số nhỏ hơn công thức (3.15) mười lần ở lô 10 ảnh (Chương 4, mục 4.3). Kết quả ở Bảng 5.2 vì vậy là kết quả về FedMix như nó đang được cài đặt. Số hạng Taylor ở đúng biên độ của (3.15) được đo ở mục 5.3.2.

Nền tảng này cũng cho phép đo biên độ của số hạng bậc hai trong khai triển Taylor so với số hạng bậc nhất, ở $\lambda = 0{,}05$. Tại khởi tạo ngẫu nhiên, trên 10 ảnh CIFAR-10, tỉ số là khoảng $1{,}3 \times 10^{-4}$. Trên ba mô hình đã huấn luyện 150 vòng với Dirichlet $\beta = 0{,}05$, tỉ số giữa số hạng bậc hai và số hạng bậc nhất là 0,039, 0,224 và 0,025 theo từng hạt giống. Như vậy số hạng bậc hai lớn lên hai đến ba bậc khi mô hình được huấn luyện. Luận văn không khảo sát nhánh bậc hai vì phạm vi, không phải vì số hạng đó không đáng kể.

**Bảng 5.3.** Hai biến thể thăm dò của FedMix. C1: mỗi client gửi một ảnh trung bình cho từng lớp, thay cho một ảnh trung bình trên toàn bộ dữ liệu cục bộ. C1+C2: C1 cộng thêm quy tắc ghép cặp chọn ảnh trung bình khác lớp có tích vô hướng với gradient theo đầu vào lớn nhất. Hiệu theo cặp so với FedAvg, trung bình ± độ lệch chuẩn mẫu, $n = 3$, đơn vị điểm phần trăm; cột cuối là cận trên của khoảng tin cậy 95% một phía.

| Biến thể | Phân hoạch, số vòng | Hiệu theo hạt giống | Trung bình | Cận trên |
|---|---|---|---|---|
| C1 | hai lớp mỗi client, 500 | −2,22 / −0,55 / −2,94 | −1,90 ± 1,23 | +0,16 |
| C1+C2 | Dirichlet $\beta = 0{,}3$, 150 | −1,36 / −2,95 / −0,60 | −1,64 ± 1,20 | +0,38 |

Cả hai biến thể đều âm về trung bình, nhưng cận trên của cả hai đều dương, nên không loại trừ được khả năng có cải thiện. Chúng được giữ nhãn thăm dò và không tham gia kết luận của luận văn.

### 5.2.3. Hiệu chuẩn tầng phân lớp và ngân sách mẫu ảo

CCVR ước lượng trung bình và hiệp phương sai của đặc trưng theo từng lớp, sinh đặc trưng ảo từ các phân phối Gauss đó, rồi huấn luyện lại riêng tầng phân lớp. Số đặc trưng ảo mỗi lớp, $M_c$, là ngân sách của phương pháp.

**Bảng 5.4.** Mức chênh độ chính xác của CCVR so với mô hình trước hiệu chuẩn, trên CIFAR-10, 150 vòng, theo ngân sách mẫu ảo $M_c$ và nồng độ Dirichlet $\beta$ (quy ước ở Bảng 5.1). Hàng $\beta = 0{,}05$ gồm ba hạt giống (+3,88 / +4,30 / +4,90); các hàng còn lại chỉ có hạt giống 42. Đơn vị: điểm phần trăm.

| $M_c$ | $\beta$ | Mức chênh |
|---|---|---|
| 100 | 0,1 | +0,29 |
| 100 | 0,3 | −0,76 |
| 2000 | 0,1 | +0,97 |
| 2000 | 0,05 | +4,36 ± 0,51 |

Ở ngân sách 100 mẫu mỗi lớp, CCVR cải thiện mô hình ở $\beta = 0{,}1$ nhưng làm mô hình kém đi ở $\beta = 0{,}3$. Cùng một phương pháp cho hai dấu ngược nhau chỉ vì mức lệch thay đổi. Hai hàng $M_c = 100$ và hai hàng $M_c = 2000$ không so được trực tiếp với nhau: chúng dùng hai lần huấn luyện backbone khác nhau, và tốc độ học của bước huấn luyện lại cũng đổi từ 0,01 sang 0,001 cùng lúc với ngân sách. Kết luận rút ra được là giới hạn: một con số đo tại một điểm ngân sách không mô tả được phương pháp. Mức cải thiện phải được báo cáo như một đường đặc tuyến theo ngân sách, hoặc ít nhất kèm theo ngân sách tại đó nó được đo; giao thức ở Chương 4 áp quy tắc thứ hai cho mọi con số của luận văn.

**Bảng 5.5.** Bốn cách huấn luyện lại tầng phân lớp từ cùng một thống kê lớp, trên cùng mô hình đã huấn luyện 150 vòng với Dirichlet $\beta = 0{,}05$, $M_c = 2000$, $d = 512$, tức $M_c/d \approx 3{,}9$. Hiệu so với mô hình trước hiệu chuẩn, trung bình ± độ lệch chuẩn mẫu, $n = 3$; độ chính xác trước hiệu chuẩn là 54,66 / 54,55 / 48,14%. Hàng "hội tụ" và dòng "LDA − Newton" lấy từ một lượt chạy riêng trên cùng ba hạt giống, trong đó LDA đạt +6,39 ± 1,24. CINIC-10 chứa ảnh của CIFAR-10, nên cột CINIC-10 chỉ để đọc mô tả, không dùng để suy luận thống kê. Đơn vị: điểm phần trăm.

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

Hai giả thuyết của Chương 3 được kiểm tra trên ba mô hình của hàng $\beta = 0{,}05$, $M_c = 2000$ ở Bảng 5.4, trước và sau khi hiệu chuẩn bằng CCVR.

Tỉ số giữa chuẩn $\ell_2$ lớn nhất và nhỏ nhất của các vector trọng số theo lớp ở tầng cuối là 1,099, 1,147 và 1,172 theo từng hạt giống, tức các chuẩn gần như bằng nhau. Độ lệch ở số hạng tự do cũng nhỏ: trung bình trị tuyệt đối của $b_c$ khoảng 0,16, so với chuẩn trung bình của $w_c$ khoảng 1,17. Trong khi đó, hiệu chuẩn lại tầng cuối nâng recall của lớp kém nhất từ 18,0% lên 61,9% (lớp tàu thuỷ, hạt giống 42), từ 16,9% lên 61,8% (lớp chó, hạt giống 43), và từ 22,3% lên 48,6% (lớp hươu, hạt giống 44). Lớp kém nhất được xác định sau khi đo, riêng cho từng hạt giống.

Một chênh lệch chuẩn dưới 20% không thể tạo ra biến thiên recall cỡ 26 đến 45 điểm nếu thiên lệch nằm ở độ lớn. Số đo vì vậy ủng hộ giả thuyết thứ hai: thiên lệch nằm ở hướng của ranh giới quyết định, và hiệu chuẩn xoay ranh giới ấy. Phát hiện này đo trên một họ kiến trúc không dùng chuẩn hoá theo lô, và một backbone có chuẩn hoá có thể định hình lại nó; luận văn không chạy kiểm soát kiến trúc, nên giả thiết rằng phát hiện độc lập với kiến trúc vẫn chưa được kiểm tra.

### 5.2.5. Những gì chuyển sang các mục sau

Ba kết quả của mục này được mang sang phần còn lại của chương, ở mức cơ chế. Dưới lệch phân phối nhãn, FedMix như đang được cài đặt không cải thiện so với FedAvg. Mức cải thiện của nhóm hiệu chuẩn tầng phân lớp phụ thuộc ngân sách mẫu ảo và có thể đổi dấu. Thiên lệch của tầng phân lớp mang tính định hướng. Mục 5.3 chuyển sang mã nguồn FedBR, nơi lệch nhãn đi kèm lệch đặc trưng do phép xoay, và so FedMix với các cách dùng mẫu trung bình khác; con số của hai nền tảng không được đem so với nhau.

---

## Truy vết — không chép vào Word

Gốc đường dẫn: `C:\Users\KietVu\Testplace\uit-msc-dp-adaptive-fedmix\`. Tra thêm ở `INDEX_ma-nguon-va-ket-qua.md` §3.

| Bảng / số liệu | Tệp thô | Tái tính |
|---|---|---|
| Bảng 5.1 | `configs/cifar10/paper_k2.yaml`, `configs/cifar10/fedmix.yaml`, `configs/cifar10/dirichlet_sweep/ccvr_b005_paperhp.yaml`, `runs/runs/e2/config_resolved.yaml` | — |
| Đối chiếu DevPranjal | `runs/_archive/hydra_reference/results/cifar10_{0,1}/`; `docs/reproductions/REPRODUCTION_CIFAR10_GATE.md:57–69` | — |
| Bảng 5.2 | `runs/_archive/fedmca_closed/negative_k2/{fedavg,fedmix}_cifar10_k2{,_s43,_s44}/<ts>/metrics.csv`; timestamp đúng ở chỉ mục §3 | `python -m scripts.aggregate_negatives_k2 --log-root runs/_archive/fedmca_closed/negative_k2` |
| Cận trên −0,52 / +0,16 / +0,38 | tính từ các hiệu theo hạt giống, $t_{0,95;2} = 2{,}920$ | chỉ mục F2 |
| Số hạng bậc hai tại khởi tạo | `docs/reproductions/REPRODUCTION_FEDMCA_C1_GATE.md:55` | `scripts/check_t2_magnitude.py` |
| Số hạng bậc hai trên mô hình đã huấn luyện (0,039 / 0,224 / 0,025) | `runs/gate_2nd/second_order_gate.json`, trường `trained.seed4x.m1.ratio_B_over_A` | `experiments/run_second_order_gate.py` |
| Bảng 5.3 | C1: `negative_k2/fedmca_c1_cifa10_k2` (s42), `fedmca_c1_cifar10_k2_{s43,s44}`; C1+C2: `runs/fedtc/*_b030_screen` (s42), `runs/_archive/fedmca_closed/*_screen_s43/s44` | C1: script trên; C1+C2: tự tính từ `metrics.csv` |
| Bảng 5.4 | $M_c=100$: `runs/_archive/void_superseded/fedtc4/ccvr_cifar10_dir_b0{10,30}_screen/`; $M_c=2000$: `runs/fedtc5/ccvr_b010_paperhp`, `runs/fedtc5/ccvr_b005_paperhp{,_s43,_s44}` (`calibration_metrics.json`) | `scripts/make_paper_figures.py` `make_fig1` |
| Bảng 5.5 | `runs/runs/e2/head_methods_summary.json`, `runs/runs/e2_cinic/…`; hàng hội tụ: `runs/runs/e3/e3_fair_baselines.json`, `runs/runs/e3_cinic/…` | `experiments/run_head_methods.py`, `experiments/run_e3_fair_baselines.py` |
| Mục 5.2.4 | `runs/fedtc5/ccvr_b005_paperhp*/calibration_metrics.json`: `head_weight_l2_before`, `recall_before`, `recall_after`, `head_bias_before` | `make_paper_figures.py` `make_fig2` |

⚠️ **Ba điểm cần biết khi bảo vệ:**
- Hàng $M_c = 100$ của Bảng 5.4 nằm trong thư mục `void_superseded`: đây là các lượt screen cũ, được giữ vì là lượt duy nhất ở ngân sách đó.
- Mục 5.2.3 nói thẳng rằng ngân sách và tốc độ học huấn luyện lại đổi cùng lúc giữa hai nhóm hàng. Không viết lại theo kiểu "trên cùng một checkpoint" (chỉ mục F6).
- Chỉ số "tỉ số bậc hai / bậc nhất trên mô hình đã huấn luyện" lấy nhánh Hessian (`ratio_B_over_A`). Không dùng các tỉ số có hậu tố `_gn`, vì chúng chuẩn hoá không nhất quán (chỉ mục F4).

---

## 5.3. So sánh các cách dùng mẫu trung bình trên mã nguồn FedBR

### 5.3.1. Tái hiện bảng CIFAR-10 của FedBR — `[BẢN NHÁP, n = 1]`

Bảng 5.6 đặt kết quả chạy lại mã nguồn FedBR cạnh bảng CIFAR-10 của bài báo FedBR [11]. Cấu hình giữ đúng bài báo:
- 10 client, lệch nhãn Dirichlet kèm phép xoay;
- 1000 vòng, 50 bước cục bộ, VGG11 không chuẩn hoá theo lô;
- chỉ số là trung bình năm độ chính xác cao nhất theo vòng, đo trên phần dữ liệu giữ lại của các client.

Lượt chạy này chỉ có một hạt giống, nên bảng dùng để đối chiếu với con số đã công bố, không dùng để so các thuật toán với nhau.

**Bảng 5.6.** Độ chính xác (%) trên CIFAR-10 xoay, 10 client, 1000 vòng, VGG11 không chuẩn hoá ($d = 512$). Cột thứ hai là giá trị công bố trong Bảng 1 của [11]; cột thứ ba là lượt chạy lại mã nguồn phát hành của [11] với hạt giống 12345, momentum 0. Chỉ số của cả hai cột là trung bình năm độ chính xác cao nhất theo vòng trên phần dữ liệu giữ lại của các client. FedMix chạy với $\lambda = 0{,}1$ và phép chuẩn hoá gốc của mã, tức số hạng Taylor nhỏ hơn (3.15) 32 lần.

| Thuật toán | Công bố [11] | Chạy lại | Chênh |
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

Sáu trong chín thuật toán cho kết quả cách giá trị công bố không quá 1,2 điểm. Moon thấp hơn 5,28 điểm. Đây là thuật toán mang một lỗi trong danh mục kiểm toán ở mục 5.3.3: mô hình cục bộ của vòng trước, thứ mà hàm mất mát tương phản của Moon cần, không bao giờ được cập nhật. DANN thấp hơn 2,69 điểm và GroupDRO cao hơn 2,66 điểm; luận văn không tìm nguyên nhân của hai chênh lệch này.

`[CHỜ SỐ LIỆU: T0]` Khi có ba hạt giống, bổ sung trung bình và độ lệch chuẩn cho FedAvg, FedProx, FedMix, FedBR, FedBR + Mixup, rồi thay câu *"Lượt chạy này chỉ có một hạt giống…"*.

### 5.3.2. Các cách dùng mẫu trung bình

`[CHỜ SỐ LIỆU: T0, T1]` Bảng hiệu theo cặp so với FedAvg, $n = 3$, khoảng tin cậy 95%. Các hàng:
- FedMix bản gốc;
- FedMix bản sửa chuẩn hoá;
- NaiveMix;
- FedBR;
- FedBR + Mixup.

Kèm một dòng hiệu FedMix bản sửa − FedMix bản gốc, và một dòng hiệu FedMix bản sửa − NaiveMix. Ghi cách chuẩn hoá ở mọi hàng FedMix (IR#12).

Một đoạn mức cơ chế về bản port FedBR lên nền tảng Flower: FedBR 57,26% so với FedAvg 57,49% (có augment), 56,04% so với 55,18% (không augment), một hạt giống, 500 vòng. Lợi thế của FedBR **không** lặp lại trên nền tảng đó. Nguồn: `INDEX` §4.3 và `docs/FEDBR_PORT_DESIGN.md` §11–13 của kho Flower. Không so con số tuyệt đối với mục 5.3.1 (IR#4).

### 5.3.3. Kiểm toán mã nguồn FedBR

`[SỬA]` Dùng lại `archive/…/05_chuong5.md` §5.2.2–5.2.6 (D1–D13, giả thuyết chưa kết luận), với ba thay đổi:
1. **Mục "Một xác nhận âm tính" viết lại.** Hệ số $\lambda(1{-}\lambda)$ đúng, nhưng phép chuẩn hoá theo lô thừa $1/B$. Đây là một sai lệch mới trong danh mục, và nó có ở cả ba bản cài đặt mã mở (`INDEX` F1).
2. **Thay mọi `[18]` bằng `[11]`, mọi `[13]` bằng `[1]`**, và bỏ mọi ký hiệu `§` trong thân bài.
3. **Đối chiếu danh mục với `src/fedbr_repro/porting_report/final_audit.md`** trong kho Flower. Đó là lượt chép lại độc lập mã FedBR, có 334 test chẵn lẻ; các phát hiện trùng nhau thì ghi một lần.

## 5.4. Chi phí tài nguyên — `[BẢN NHÁP, n = 1]`

Chi phí truyền thông phụ trội tính theo công thức (4.6) của Chương 4. Chi phí tính toán lấy từ thời gian mỗi bước ghi trong nhật ký của lượt chạy ở Bảng 5.6.

**Bảng 5.7.** Thời gian huấn luyện quy về 1000 vòng truyền thông, lượt chạy một hạt giống ở Bảng 5.6. Cột cuối là tỉ lệ so với FedAvg. `[CẦN ĐIỀN: loại GPU]`.

| Thuật toán | Giờ / 1000 vòng | So với FedAvg |
|---|---|---|
| FedAvg | 2,3 | 1,0× |
| FedProx | 2,7 | 1,2× |
| FedMix | 5,8 | 2,5× |
| FedBR | 7,5 | 3,3× |
| FedBR + Mixup | 7,6 | 3,3× |

FedMix tốn gấp khoảng hai lần rưỡi FedAvg, chủ yếu do phép lấy đạo hàm theo đầu vào với `create_graph=True`, tức phải lan truyền ngược hai lần. FedBR tốn gấp khoảng ba lần, do có thêm bước tối đa hoá trên tầng chiếu.

⚠️ **Hai việc trước khi dùng bảng này:**
- **Nguyên nhân chi phí của FedMix và FedBR.** Hai câu giải thích trên là suy luận từ cấu trúc mã, chưa được đo tách riêng. Nếu không đo thì viết dạng *"có thể do…"* hoặc bỏ đi.
- **Cột bộ nhớ.** `summary.csv` ghi bộ nhớ đỉnh bằng 0,0 GB cho FedAvg, FedProx và FedMix, nhưng 3,1 GB cho FedBR. Nhiều khả năng đây là lỗi ghi nhận chứ không phải số đo, nên cột bộ nhớ **không đưa vào luận văn** cho tới khi kiểm lại `mem_gb` trong `results.jsonl`.

## 5.6. Tổng hợp và thảo luận

`[CHỜ SỐ LIỆU: tất cả]` Trả lời RQ1–RQ4, mỗi câu một đoạn, kèm điều kiện hiệu lực; threats to validity.

---

## Truy vết mục 5.3–5.4 — không chép vào Word

| Số liệu | Tệp thô |
|---|---|
| Bảng 5.6, cột "Chạy lại" | `C:\Users\KietVu\Testplace\FedBR\output\cifar10\02_attempt_20260916\summary.csv` (cột `Acc (%)`); đã tái tính khớp từ từng `results.jsonl` (`INDEX` §5.2) |
| Bảng 5.6, cột "Công bố" | `paper/ref/Guo et al. - 2023 - FedBR….pdf`, Bảng 1, cột CIFAR10 (VGG11) |
| Bảng 5.7 | cùng `summary.csv`, cột `h/1000rd` |
| Port FedBR lên Flower | kho Flower `runs/paper_{fedavg,fedbr}_rot{,_noaug}_r500/` |
