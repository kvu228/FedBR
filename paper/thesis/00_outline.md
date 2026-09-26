# 00 — DÀN BÀI LUẬN VĂN · HƯỚNG B (từ 24/09/2026)

> **Vai trò.** Dàn bài và bản giao ước cho mọi agent và người viết từ 24/09/2026. Đọc hết §0–§3 và §7 trước khi viết bất kỳ chương nào.
>
> **Bối cảnh đổi hướng.** Dàn bài trước (hướng "xác định biên giới hiệu lực của cơ chế Taylor") và các bản thảo chương đi kèm đã được chuyển nguyên trạng vào `archive/2026-09-24_huong-bien-gioi-hieu-luc/`. Commit `c5ff78a` là ảnh chụp đầy đủ trước khi chuyển. Tra lịch sử quyết định, IRON RULES gốc và các bảng trước/sau đã lập ngày 24/09 ở đó. **Không thực hiện theo tài liệu trong `archive/`**, trừ những phần được dàn bài này dẫn tên.

---

## 0. Siêu dữ liệu

| | |
|---|---|
| **Tên đề tài (VI)** | NÂNG CAO HIỆU SUẤT HỌC LIÊN KẾT THÔNG QUA TĂNG CƯỜNG DỮ LIỆU DỰA TRÊN KHAI TRIỂN TAYLOR — **giữ nguyên**, không đổi tên, không làm giải trình chỉnh sửa |
| **Tên đề tài (EN)** | ENHANCING FEDERATED LEARNING PERFORMANCE VIA DATA AUGMENTATION BASED ON TAYLOR EXPANSION |
| Học viên | Vũ Tuấn Kiệt — MSHV 240201043, Khóa 2024 Đợt 02, CNTT 8480201 |
| CBHD | PGS.TS. Nguyễn Tấn Cầm |
| Hướng | Nghiên cứu, 15 TC · 12 tháng |
| Độ dài mục tiêu | 50–60 trang (không kể phụ lục, tài liệu tham khảo). Format: A4 · Times New Roman 13 · giãn dòng 1,5 · lề trên/dưới 2,5 cm · trái 3,5 cm · phải 2 cm |
| **Bản chính (Word)** | `C:\Users\KietVu\OneDrive\Study\UIT\Master\16_FinalThesis\LuanVan\VuTuanKiet_KLTN_Thsi_2026.docx` — **khi `.md` và Word lệch nhau, Word đúng**. Đọc bằng cách giải nén `word/document.xml`; công thức là OMML nên trích văn bản thuần sẽ mất công thức, chỉ còn số phương trình. File bị khoá khi đang mở trong Word |
| **Chỉ mục mã nguồn & kết quả** | **`INDEX_ma-nguon-va-ket-qua.md`** — đọc trước khi viết bất kỳ con số, cấu hình hay mô tả cài đặt nào. Phủ kho Flower `C:\Users\KietVu\Testplace\uit-msc-dp-adaptive-fedmix`, kho `FedBR` này, kết quả `C:\Users\KietVu\Testplace\FedBR\output\cifar10\02_attempt_20260916`, và mã DevPranjal |
| Đề cương đã duyệt | `Decuong_DataAugmentationFL_VuTuanKiet.pdf` |
| Bài báo nền | FedMix: Yoon et al., ICLR 2021. FedBR: Guo, Tang, Lin, ICML 2023 — `paper/ref/Guo et al. - 2023 - FedBR….pdf` |
| **Công bố của luận văn** | *When Does Classifier Calibration Reproduce Under Non-IID Federated Learning? A Controlled Study on a Faithful Flower Stack* — V. T. Kiet, N. T. Cam, **ISWTA 2026** (2026 10th IEEE Symposium on Wireless Technology & Applications), đã được chấp nhận đăng; chưa có DOI. **Không trích trong thân bài** (xem IR#9) |

---

## 1. Khung chiến lược — đọc trước khi viết

### 1.1. Hướng B trong một đoạn

Luận văn xây dựng **khung học liên kết chia sẻ mẫu trung bình đại diện** đúng như sơ đồ trong đề cương: client tạo mẫu trung bình $V_i$, máy chủ gom thành $V = \bigcup_i V_i$ và phát lại, client dùng $V$ trong vòng lặp huấn luyện cục bộ. Điểm cốt lõi của khung là **cách dùng mẫu trung bình là một thành phần thay được**. Luận văn cài và so sánh ba cách dùng trên cùng một kênh dữ liệu:
- qua **khai triển Taylor bậc nhất** của hàm mất mát (FedMix), đúng cơ chế đề cương nêu tên;
- **trộn trực tiếp** vào đầu vào (NaiveMix), làm đối chứng cho số hạng Taylor;
- làm **mốc cân bằng và mốc đặc trưng toàn cục** (FedBR), bỏ nhãn.

Kết quả thực nghiệm trên hai nền tảng cho biết cách dùng nào nâng được hiệu suất, dưới dạng lệch phân phối nào, với chi phí bao nhiêu.

**Hướng A (làm nếu còn thời gian).** Đề xuất một cách dùng thứ tư: **FedBR cộng số hạng Taylor**. Giữ hai thành phần của FedBR, giữ nhãn mềm $\bar y_g$, và thêm số hạng tăng cường theo khai triển Taylor bậc nhất vào mục tiêu cục bộ. Đây là phần duy nhất có thể gọi là "phương pháp đề xuất" theo nghĩa hẹp. Luận văn **không phụ thuộc** vào A: nếu A không chạy kịp hoặc cho kết quả âm, luận văn vẫn đứng trên B. Chừng nào A chưa có số liệu, **không chương nào được nhắc tới A** ngoài Ch.6 (hướng phát triển).

### 1.2. Vì sao B khớp đề cương

| Đề cương hứa | B giao ở đâu |
|---|---|
| Framework tăng cường dữ liệu dựa trên mẫu đại diện trung bình (sơ đồ trang 5) | Ch.4: khung chia sẻ mẫu trung bình, dựng theo đúng bốn giai đoạn của sơ đồ |
| "Tính loss với Taylor Expansion" | Ch.3 dẫn xuất; Ch.4 đặt FedMix làm cách dùng mặc định của khung và chỉ ra chỗ lệch $1/B$ của cách chuẩn hoá hiện có (mục 4.3); Ch.5 đo FedMix với cách chuẩn hoá hiện có |
| Mô hình toàn cục có độ chính xác cao hơn | Ch.5: so sánh các cách dùng với FedAvg và FedProx trên hai nền tảng |
| Báo cáo cân bằng hiệu suất và chi phí tài nguyên | Ch.4 công thức chi phí truyền thông; Ch.5 thời gian mỗi 1000 vòng (cột bộ nhớ chưa dùng được) |
| Baseline FedAvg, FedProx | có ở cả hai nền tảng |
| Tăng cường tại vùng ranh giới quyết định | Ch.3 nêu hai giả thuyết (thiên lệch ở độ lớn hay ở hướng); Ch.5 mục 5.2.4 đo |
| Hỗ trợ hồi quy; mở rộng vùng lân cận đơn phương/song phương | **Không giao.** Gác từ 22/09; nêu ở Ch.6 như hướng phát triển. Học viên cần báo CBHD |

Chỗ B còn yếu, phải nói thẳng: kết quả đo được có thể là **cách dùng dựa trên Taylor không nâng được hiệu suất**, còn cách dùng của FedBR thì nâng được. Tên đề tài vẫn trung thực, vì luận văn nghiên cứu và cài đặt đúng kỹ thuật tăng cường dữ liệu dựa trên khai triển Taylor trong một khung có kiểm soát. Nhưng Ch.1 không được viết như thể đã biết Taylor sẽ thắng.

### 1.3. Câu hỏi nghiên cứu

| | Câu hỏi | Trả lời ở |
|---|---|---|
| **RQ1** | Dùng mẫu trung bình qua khai triển Taylor bậc nhất (FedMix) có nâng hiệu suất so với FedAvg và FedProx không, dưới lệch nhãn và dưới lệch nhãn kèm lệch đặc trưng? | Ch.5 mục 5.2.2, 5.3 |
| **RQ2** | Trên cùng kênh mẫu trung bình, cách dùng nào nâng hiệu suất nhiều nhất: Taylor, trộn trực tiếp, hay mốc cân bằng và đặc trưng? | Ch.5 mục 5.3 |
| **RQ3** | Mức cải thiện đổi thế nào theo lượng thông tin được chia sẻ, và chi phí truyền thông, tính toán là bao nhiêu? | Ch.5 mục 5.2.3, 5.3.3, 5.4 |
| **RQ4** | Thiên lệch do dữ liệu không đồng nhất nằm ở độ lớn hay ở hướng của ranh giới quyết định? | Ch.5 mục 5.2.4 |

### 1.4. Đóng góp (bản làm việc; phát biểu cuối cùng sau khi có số liệu T0–T1)

- **C1 — Khung chia sẻ mẫu trung bình với cách dùng thay được** (Ch.4): bốn giai đoạn, ba cách dùng NaiveMix, FedMix, FedBR. Luận văn **không sửa** phép chuẩn hoá của FedMix; phát hiện thừa $1/B$ thuộc C3.
- **C2 — Đánh giá có kiểm soát trên hai nền tảng.**
  - Flower, lệch nhãn, ba hạt giống: FedMix không cải thiện (cận trên −0,52); mức cải thiện của hiệu chuẩn tầng phân lớp đổi dấu theo ngân sách mẫu ảo; thiên lệch mang tính định hướng.
  - FedBR, lệch nhãn kèm xoay, **một hạt giống** (ngưỡng đọc 3 pp): FedBR hơn FedAvg 6,37 điểm, cùng chiều với bài FedBR; FedMix không phân biệt được với FedAvg; mẫu trung bình ở $M = 10$ không còn đủ thông tin để hiệu chuẩn tầng phân lớp (mục 5.3.3).
- **C3 — Kiểm chứng lại các kết quả đã công bố**: đo lại FedMix và nhóm hiệu chuẩn trên Flower; tái hiện bảng CIFAR-10 của FedBR; chỉ ra rằng cách tính số hạng Taylor theo lô làm nó nhỏ hơn công thức $B$ lần (Ch.4 mục 4.3). Danh mục kiểm toán mã FedBR nằm ở Phụ lục A. Khớp đóng góp thứ ba đã sửa ở Ch.1, Ch.2 (khối rà soát 26/09).
- *(C4 — chỉ khi A có số liệu)* Cách dùng kết hợp FedBR và số hạng Taylor.

**Mọi phát biểu về tính mới phải có hạn định trong câu (IR#3).** Bảng CIFAR-10 của bài FedBR **có** FedMix làm đối chứng (57,37%). Vì vậy cấm viết "chưa ai so FedBR với FedMix". Điều chưa có trong bài FedBR là NaiveMix và việc so các cách dùng như những thành phần của **cùng một khung**.

---

## 2. IRON RULES — ràng buộc bắt buộc

Kế thừa từ dàn bài cũ (bản gốc ở `archive/…/00_outline.md` §2), có sửa theo hướng B. **Vi phạm bất kỳ quy tắc nào = viết lại mục đó.**

**IR#1 — Kỷ luật báo cáo cho kết quả Flower.**
- Phép đối chiếu với DevPranjal là *kiểm tra tính nhất quán, không phải kiểm chứng độc lập*: bản cài đặt đó cũng là mốc mà nền tảng được hiệu chỉnh theo. **Cấm dùng từ "độc lập"** cho phép đối chiếu này.
- C1 và C1+C2 mang nhãn **thăm dò**.
- CINIC-10 chứa ảnh CIFAR-10, nên chỉ đọc **mô tả**, không suy luận thống kê.

**IR#2 — Phát biểu bằng khoảng tin cậy, không bằng dấu.** Ba hiệu cùng âm là sign test $p = 0{,}25$, không phải bằng chứng. Cận trên 95% một phía, tính từ các hiệu theo hạt giống với $t_{0,95;2} = 2{,}920$: FedMix **−0,52**, C1 **+0,16**, C1+C2 **+0,38**. Chỉ FedMix loại trừ được khả năng cải thiện. Đây là phép tính của luận văn (`INDEX` F2).

**IR#3 — Không phát biểu phủ định toàn cầu.** Cấm "chưa ai làm". Hạn định nằm **trong chính câu**, ưu tiên thu về một đối tượng kiểm chứng được: *"Cấu hình như vậy không xuất hiện trong bài báo FedMix, kể cả ở phần phụ lục."* Nhật ký khảo sát văn liệu để ở `NOTE_khao-sat-van-lieu.md`, không vào thân bài.

**IR#4 — Kỷ luật trong cùng nền tảng.** Cấm so con số tuyệt đối giữa nền tảng Flower (mục 5.2) và mã FedBR (mục 5.3 trở đi). Mọi mức cải thiện là **hiệu theo cặp** trên cùng hạt giống và cùng phân hoạch. Phát biểu bắc qua hai nền tảng chỉ ở mức cơ chế.

**IR#5 — Khai báo số hạt giống và cách đọc** (sửa 26/09). Mỗi bảng kết quả ghi số hạt giống và phép kiểm định hoặc quy tắc đọc.
- **Nền tảng Flower: ba hạt giống.** Hiệu theo cặp kèm khoảng tin cậy. Với $n = 3$ và $s \approx 1{,}2$, nửa rộng khoảng tin cậy 95% là **2,98 pp**; hiệu nhỏ hơn mức đó chỉ báo cáo dưới dạng khoảng.
- **Nền tảng FedBR: một hạt giống (12345) cho mọi thuật toán** (quyết định của học viên 26/09: mỗi lượt FedBR 1000 vòng mất khoảng 7,5 giờ). Không có khoảng tin cậy. Hiệu theo cặp **dưới 3 pp không được diễn giải** thành khác biệt giữa hai phương pháp; từ 3 pp trở lên là quan sát đơn lẻ, đối chiếu chiều với bảng của [2]. Ngưỡng lấy từ chênh lệch giữa lượt chạy lại và bảng công bố (−2,69 đến +2,66, bỏ Moon). Chi tiết ở Ch.5 mục 5.1.3.

**IR#6 — Không mô tả sai FedBR, FedMix.**
- Thành phần 2 của FedBR ghép cặp **theo từng mẫu** trên cùng pseudo-data. Cấm gọi là "căn chỉnh phân phối biên".
- Pseudo-data RSM của FedBR và mẫu trung bình của FedMix là **cùng dữ liệu**, trừ nhãn: FedBR dùng nhãn đều $1/C$ (nhánh Mixture thì khác). Căn cứ: `tests/fedbr_repro/test_data_parity.py:356` trong kho Flower.
- Không tuyên bố riêng tư cho mẫu trung bình. Viết *"chia sẻ mẫu trung bình"*, không viết "bảo mật" hay "riêng tư" như một bảo đảm. Chính tác giả FedBR thừa nhận rủi ro rò rỉ; đó là lý do có nhánh Mixture.

**IR#7 — Báo cáo tham số đúng như mã nguồn, không như văn bản mô tả.**
- $\alpha_{\text{rot}}$ trong mã FedBR là nồng độ **tổng** 1,0, tức 0,1 mỗi thành phần.
- Dirichlet trên nền tảng Flower là nồng độ **mỗi thành phần**, trục client, 60 thành phần.
- Chiều đặc trưng $d$ ghi trong mọi bảng.
- Projection MLP của FedBR: bài ghi 256/128, mã dùng 1024/512.
- $\lambda$ của FedBR cho CIFAR-10: bài ghi 0,1, mã dùng 1,0.

**IR#8 — Mọi con số truy vết được.** Mỗi bảng có khối *Truy vết* (không chép vào Word) trỏ tới tệp thô. Nguồn: `INDEX_ma-nguon-va-ket-qua.md`.

**IR#9 — Công bố của luận văn.** Bài ISWTA 2026 là công bố **của luận văn**, không phải nguồn trích. Thân bài **không trích** bài đó: không `[TG]`, không "công trình trước của tác giả". Bài chỉ xuất hiện ở *Danh mục công bố khoa học của tác giả* và một câu trong *Lời cam đoan* (câu mẫu ở `archive/…/01_chuong1.md`, khối 24/09).

**IR#10 — Không viết kết quả chưa chạy.** Mục nào chưa có dữ liệu thì để `[CHỜ SỐ LIỆU: <exp-id>]`. Cấm số minh hoạ, số ước lượng, số "dự kiến".

**IR#11 — FedBR là phương pháp của Guo và cộng sự** (mới, 24/09). Luận văn **cài và đánh giá** FedBR như một cách dùng mẫu trung bình trong khung. Luận văn **không đề xuất** FedBR. Chương 4 trình bày khung và cách các phương pháp được đặt vào khung; mọi mô tả FedBR đi kèm trích dẫn [2].

**Số trích dẫn theo danh mục Word (kiểm 25/09):** [1] FedMix · [2] FedBR · [3] FedAvg · [4] NIID-Bench · [5] Hsu–Qi–Brown · [8] CCVR · [10] Mixup · [11] VHL · [16] Efron · [17] Ng–Jordan. Các bảng sửa trong md viết trước ngày này còn ghi FedBR là [11]; khi chép vào Word dùng số ở đây.

**IR#12 — Phép chuẩn hoá số hạng Taylor phải được nêu mỗi lần báo kết quả FedMix** (mới, 24/09). Ghi rõ đó là bản cài đặt gốc (số hạng Taylor nhỏ hơn công thức $B$ lần) hay bản đã sửa. Kết quả FedMix ở mục 5.2 và ở `02_attempt` đều là **bản cài đặt gốc**. `FedBRTaylor` (hướng A) dùng chuẩn hoá đúng theo công thức; khi A có số liệu thì câu *"biên độ của số hạng Taylor theo đúng (3.15) không được đo trong luận văn"* ở Ch.4 mục 4.3 không còn đúng và phải sửa.

---

## 3. Tài sản — cái gì đã có

### 3.1. Kết quả đã có số liệu

| Tài sản | Nền tảng | Số hạt giống | Dùng ở | Trạng thái |
|---|---|---|---|---|
| FedMix so với FedAvg, K=2: −1,86 ± 0,79; C1, C1+C2 thăm dò; số hạng bậc hai | Flower | 3 | Ch.5 mục 5.2.2 | **đã viết** |
| CCVR theo ngân sách mẫu ảo; bốn head hiệu chuẩn; trần LDA | Flower | 1–3 | Ch.5 mục 5.2.3 | **đã viết** |
| Thiên lệch định hướng: tỉ số chuẩn 1,10–1,17, recall lớp kém nhất | Flower | 3 | Ch.5 mục 5.2.4 | **đã viết** |
| Bảng tái hiện CIFAR-10 của FedBR, 9 thuật toán, 1000 vòng | FedBR | **1** (seed 12345) | Ch.5 mục 5.3.1, 5.3.2 | **đã viết** (26/09) |
| Danh mục kiểm toán mã FedBR D1–D13, cộng phép chuẩn hoá $1/B$ | FedBR | — | **Phụ lục A** (`07_phu-luc.md`) | bản nháp ở `archive/…/05_chuong5.md` §5.2.2–5.2.6 |
| Hiệu chuẩn tầng phân lớp bằng mẫu trung bình, quét $M$ (LDA, 2000 mẫu/client) | FedBR | 1 | Ch.5 mục 5.3.3 | **đã viết** (26/09); số liệu `INDEX` §5.2b |
| ~~Port FedBR lên Flower: FedBR ≈ FedAvg (−0,24; +0,86)~~ | Flower | 1 | **không dùng** | học viên 26/09: bản cài FedBR bên kho Flower chưa được xác nhận khớp FedBR gốc |

**Đối chiếu bảng tái hiện với bài FedBR** (Bảng 1 của bài, CIFAR-10, VGG11; `02_attempt` dùng chỉ số local top-5 của cùng bài):

| Thuật toán | Bài FedBR | `02_attempt` |
|---|---|---|
| FedAvg | 58,99 | 59,45 |
| FedProx | 59,14 | 59,14 |
| Moon | 58,23 | **52,95** (lệch; khớp lỗi D4) |
| DANN | 58,29 | 55,60 |
| GroupDRO | 56,57 | 59,23 |
| FedBR | 64,65 | 65,82 |
| FedAvg + Mixup | 58,57 | 59,44 |
| FedMix | 57,37 | 57,16 |
| FedBR + Mixup | 65,32 | 66,47 |

### 3.2. Mã nguồn cần viết thêm (kho `FedBR`)

| # | Việc | Phục vụ | Ưu tiên |
|---|---|---|---|
| ~~M1~~ | ~~Cờ chọn cách chuẩn hoá số hạng Taylor cho FedMix~~ | — | **bỏ**: không sửa FedMix (24/09) |
| **M2** | Target Makefile `run-naivemix` (`NaiveMix` đã có ở `algorithms.py:809`) | T1 | cao |
| **M3** | Lớp `FedBRTaylor`: `FedBR.update` cộng số hạng (II) và (III) của FedMix trên pseudo-data có nhãn mềm | T2 (A) | **đã cài** (`b0bb3e2`); đang chạy trên Vast |
| M4 | Sửa lỗi môi trường 0° (`if not angle`), hoặc chấm lại bằng `eval_checkpoint.py` | cột Global | thấp; chỉ số chính không bị ảnh hưởng |
| M5 | Cờ `--fedmix_M` | quét $M$ | tuỳ chọn |

⚠️ **Quyết định `[QUYẾT]` về tập $V$.** Mã FedBR dựng lại mẫu trung bình của FedMix và NaiveMix **ở mỗi bước**, từ dữ liệu thô. Pseudo-data của FedBR thì dựng **một lần**. Đề xuất: **giữ nguyên hành vi của mã** cho T0–T1, để kết quả so được với bảng của bài FedBR và với `02_attempt`. Ch.4 mô tả thẳng rằng đây là lối tắt của mô phỏng; Ch.6 nêu nó là hạn chế.

---

## 4. Dàn bài chi tiết

> **Ký hiệu trạng thái:** `[GIỮ]` dùng lại nội dung Word hiện có · `[SỬA]` dùng lại có sửa · `[VIẾT]` viết mới · `[CHẠY]` chờ số liệu · `[ĐÃ VIẾT]` có bản nháp trong file chương.

### CHƯƠNG 1 — GIỚI THIỆU · 3–4 trang

Giới thiệu thuần tuý: bối cảnh, vấn đề, mục tiêu, phạm vi, đóng góp, cấu trúc. Không khảo sát văn liệu (việc của Ch.2), không lập luận thiết kế đo (việc của Ch.4).

- **1.1 Lý do chọn đề tài** `[SỬA]`. Word đã có năm đoạn tốt. Chỉ đoạn cuối phải đổi theo hướng B: bỏ *"Luận văn vì vậy không đề xuất một thuật toán mới, mà xác định biên giới hiệu lực…"*, thay bằng khung chia sẻ mẫu trung bình và câu hỏi cách dùng nào nâng được hiệu suất.
- **1.2 Mục tiêu, đối tượng, phạm vi** `[SỬA]`. Mục tiêu tổng quát trích đề cương. Mục tiêu cụ thể viết lại theo RQ1–RQ4, đánh số 1–4. Đối tượng: khung chia sẻ mẫu trung bình và **ba** cách dùng. Phạm vi giữ phần lớn Word; sửa câu về hai nền tảng theo bảng hàng 1 ở `archive/…/01_chuong1.md`.
- **1.3 Đóng góp** `[VIẾT]` theo §1.4 dàn bài này.
- **1.4 Cấu trúc** `[VIẾT]`.

### CHƯƠNG 2 — CÁC NGHIÊN CỨU LIÊN QUAN · 9–10 trang

- **2.1 Học liên kết và dữ liệu không đồng nhất** `[GIỮ]`: khái niệm FL; ba dạng non-IID theo NIID-Bench; quy ước Dirichlet.
- **2.2 Các hướng khắc phục** `[GIỮ]`: hướng không chia sẻ dữ liệu (FedProx, SCAFFOLD, MOON); hướng có chia sẻ dữ liệu (Zhao; mean-augmented FL; dữ liệu ảo; chưng cất; hiệu chuẩn tầng phân lớp; căn chỉnh prototype; FedBR). Áp hai hàng sửa của `archive/…/02_chuong2.md` khối 24/09 (FedBR không còn là nền tảng duy nhất).
- **2.3 Bảng đối chiếu các họ phương pháp** `[GIỮ]`.
- **2.4 Khoảng trống** `[SỬA]` theo hướng B:
  - (a) số hạng Taylor của FedMix chưa được tách khỏi phép trộn (giữ 2.4.1 Word, sửa lỗi *"mẫu trung bình vẫn tham gia lượt truyền xuôi như ở FedMix"*);
  - (b) FedMix và FedBR dùng **cùng một kênh dữ liệu** theo hai cách khác nhau; bài FedBR so hai phương pháp như hai thuật toán riêng, chưa như hai cách dùng trong một khung, và không có NaiveMix. Hạn định theo IR#3;
  - (c) tính tái lập của các kết quả đã công bố (giữ 2.4.3);
  - (d) định vị luận văn.

### CHƯƠNG 3 — CƠ SỞ LÝ THUYẾT · 9–10 trang

- **3.1 Học liên kết và local SGD** `[GIỮ]`.
- **3.2 Mô hình hoá dữ liệu không đồng nhất** `[GIỮ]`: Dirichlet; phép xoay.
- **3.3 Global Mixup và xấp xỉ Taylor bậc nhất** `[GIỮ]` + sửa câu cuối mục 3.3.4 về phép chuẩn hoá (hàng 3 của `archive/…/03_chuong3.md` khối lượt 2).
- **3.4 Thiên lệch học cục bộ** `[SỬA]`: 3.4.1 giữ; 3.4.2 viết lại thành hai giả thuyết (khối S1 ở `archive/…/03_chuong3.md`).
- **3.5 FedBR: dùng mẫu trung bình để giảm thiên lệch học cục bộ** `[VIẾT]` — **mục mới, trọng tâm của chương theo hướng B**:
  - pseudo-data RSM (trùng mẫu trung bình của FedMix, bỏ nhãn);
  - thành phần 1: cân bằng đầu ra tầng phân lớp trên pseudo-data;
  - thành phần 2: bài toán min-max tương phản trên không gian đặc trưng, ghép cặp theo từng mẫu;
  - công thức lấy từ bài FedBR (`paper/ref/`) và đối chiếu với `fedbr/algorithms.py` (lớp `FedBR`) cùng `src/fedbr_repro/algo.py:207–315` của kho Flower. **Không viết công thức theo trí nhớ.**
- **3.6 Bộ phân lớp sinh so với phân biệt** `[SỬA]` (mục 3.5 cũ của Word): áp hàng 10–11 và khối S2 ở `archive/…/03_chuong3.md`. Giữ vì Ch.5 mục 5.2.3 cần nó.

Ch.3 **không chứa số đo của luận văn**; mọi số đo nằm ở Ch.5.

### CHƯƠNG 4 — KHUNG ĐỀ XUẤT · 8–10 trang

**Nguyên tắc (học viên, 25/09):** Ch.4 chỉ trình bày đề xuất. Không bàn về mã nguồn, bản cài đặt của ai, hay thiết lập thực nghiệm; những thứ đó nằm ở Ch.5. Không tiểu mục khi mục không đủ nội dung.

- **4.1 Kiến trúc khung chia sẻ mẫu trung bình** `[ĐÃ VIẾT]`, một mục không tiểu mục: bốn giai đoạn, lớp ghi nhận, Thuật toán 4.1, Hình 4.1 (`figures/hinh4_1.png`).
- **4.2 Các cách dùng mẫu trung bình** `[ĐÃ VIẾT]`: đoạn dẫn, Bảng 4.1, 4.2.1 NaiveMix, 4.2.2 FedMix, 4.2.3 FedBR.
- **4.3 Chuẩn hoá số hạng Taylor** `[ĐÃ VIẾT]`: chỉ nêu logic thừa $1/B$ và phép thử số tỉ lệ bằng $B$; hai yếu tố gây nhiễu (biên độ gradient, phép co đầu vào).
- **4.4 Chi phí tài nguyên** `[ĐÃ VIẾT]`, một mục không tiểu mục: công thức (4.1), ví dụ 4,3 MB so với 738 MB mỗi vòng; chi phí tính toán trỏ sang 5.4.
- ~~4.5 Giao thức đo lường~~ → chuyển sang Ch.5 mục 5.1 (25/09).

Các thiết kế của hướng cũ **không mang sang** hướng B: cấu hình C, trục Drop với P0–P4, mặt $(\lambda, M)$ đầy đủ. Chúng nằm trong `archive/`, có thể dùng lại nếu còn thời gian sau T2.

### CHƯƠNG 5 — THỰC NGHIỆM · 15–16 trang

- **5.1 Thiết lập** `[ĐÃ VIẾT]`: 5.1.1 hai nền tảng (Bảng 5.1) và cấu hình nền tảng FedBR (Bảng 5.2, từ `args`/`hparams` của `02_attempt`), kèm chỗ thiết lập đi khác khung; 5.1.2 chỉ số và đại lượng ghi nhận; 5.1.3 so sánh theo cặp và số hạt giống (Flower ba, FedBR một với ngưỡng đọc 3 pp); 5.1.4 hai phép so sánh chính S1/S2 (Bảng 5.3) và cách đọc các phép so sánh thăm dò.
- **5.2 Thực nghiệm dưới lệch nhãn trên nền tảng Flower** `[ĐÃ VIẾT]`, 5.2.1–5.2.5 — xem `05_chuong5.md`.
- **5.3 So sánh các cách dùng mẫu trung bình trên nền tảng FedBR** `[ĐÃ VIẾT, một hạt giống]`:
  - 5.3.1 tái hiện bảng CIFAR-10 của bài FedBR (`02_attempt`, Bảng 5.9);
  - 5.3.2 FedBR (S1), FedMix (S2), FedBR + Mixup, FedProx, FedAvg + Mixup (Bảng 5.10); NaiveMix chờ T1 nếu chạy; không có FedMix bản sửa;
  - 5.3.3 mẫu trung bình còn giữ bao nhiêu thông tin cho tầng phân lớp: phép chẩn đoán, quét $M$ (Bảng 5.11, Hình 5.1). Kiểm toán mã chuyển sang Phụ lục A;
- **5.4 Chi phí tài nguyên** `[SỬA]`: thời gian mỗi 1000 vòng (Bảng 5.12; cột bộ nhớ trong `summary.csv` chưa dùng được), chi phí truyền thông theo (4.1).
- *(5.5 — chỉ khi A có số liệu)* FedBR cộng số hạng Taylor `[CHẠY: T2]`.
- **5.6 Tổng hợp và thảo luận** `[CHẠY]`: trả lời RQ1–RQ4, mỗi câu một đoạn kèm điều kiện hiệu lực; threats to validity.

### CHƯƠNG 6 — KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN · 4–5 trang

- 6.1 Kết luận; 6.2 Đóng góp; 6.3 Hạn chế; 6.4 Hướng phát triển.
- Bản nháp mục 6.3–6.4 ở `archive/…/06_chuong6.md` dùng lại được một phần.
- Hướng phát triển bắt buộc có: hồi quy; mở rộng vùng lân cận song phương; lệch đặc trưng thật (PACS…); phân tích riêng tư hình thức; và A nếu chưa làm.

---

## 5. Kế hoạch thực nghiệm

Chi tiết và ngân sách ở `PLAN_huong-B.md`. Tóm tắt:

| Mức | Nội dung | Điều kiện |
|---|---|---|
| ~~T0~~ | ~~Thêm 2 hạt giống trên nền tảng FedBR~~ | **bỏ** (26/09): FedBR chạy quá lâu; nền tảng FedBR dùng một hạt giống |
| **T1** | NaiveMix, hạt giống 12345 (FedMix bản sửa bỏ cùng M1) | tuỳ chọn |
| **T2 (A)** | FedBR cộng số hạng Taylor (M3), hạt giống 12345 | **đang chạy trên Vast** (26/09) |

---

## 6. Ánh xạ sang bản Word

| Chương Word | Việc | Nguồn hướng dẫn |
|---|---|---|
| Ch.1 | sửa 1.1 đoạn cuối, viết lại 1.2.1, 1.2.2, 1.3, 1.4 | `01_chuong1.md` |
| Ch.2 | giữ gần như nguyên; sửa 2.4 | `02_chuong2.md` |
| Ch.3 | giữ 3.1–3.3; sửa 3.4.2; **thêm 3.5 FedBR**; 3.5 cũ thành 3.6 | `03_chuong3.md` |
| Ch.4–Ch.6 | Word mới có tiêu đề; đổi tiêu đề theo dàn bài này | `04`–`06_chuong*.md` |
| Lời cam đoan, Danh mục công bố | điền theo IR#9 | `archive/…/01_chuong1.md`, khối 24/09 |

---

> **§7 chép nguyên văn từ `archive/…/00_outline.md` ngày 24/09, còn nguyên hiệu lực.** Ngoại lệ duy nhất: các câu nhắc tới cấu trúc chương cũ (số trang Ch.1 cũ, mục "§1.2.1 đánh số 1–4") thì đọc theo §4 dàn bài này. Hạn ngạch AI#1–AI#10 và ba lệnh tự kiểm áp cho **mọi** chương theo hướng B.

## 7. Quy ước viết

### 7.1. Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $N$, $i$ | số client, chỉ số client |
| $\mathcal{D}_i$, $p_i$ | tập dữ liệu và trọng số client $i$ |
| $\phi$, $\omega$ | bộ trích xuất đặc trưng, bộ phân lớp |
| $d$ | chiều đặc trưng — **luôn ghi rõ theo backbone** |
| $C$ | số lớp |
| $\lambda$ | trọng số trộn (`fedmix_lambda`) |
| $M$ | số ảnh gộp mỗi mẫu đại diện |
| $\bar{x}_g,\bar{y}_g$ | mẫu trung bình đại diện và nhãn mềm |
| $\alpha$ | nồng độ Dirichlet label skew (mặc định 0.1, quy ước $\alpha\cdot p$) |
| $\alpha_{\text{rot}}$ | nồng độ Dirichlet feature skew — **quy ước tuyệt đối**, mặc định ≈0.1 |
| $\Delta$ | paired difference (pp) |
| $\Delta_{\text{Taylor}}$ | FedMix − NaiveMix |

### 7.2. Thuật ngữ VI/EN (nhất quán toàn luận văn)

Học liên kết (Federated Learning) · dữ liệu không đồng nhất / không phân phối đồng nhất (non-IID) · lệch phân phối nhãn (label skew) · lệch phân phối đặc trưng (feature skew) · thiên lệch học cục bộ (local learning bias) · mẫu trung bình đại diện (mean-augmented / representative sample) · khai triển Taylor (Taylor expansion) · bộ phân lớp / tầng phân lớp (classifier head) · ranh giới quyết định (decision boundary) · hiệu chuẩn (calibration) · đường đặc tuyến vận hành (operating curve) · vòng truyền thông (communication round) · so sánh theo cặp (paired comparison)

#### Bên tham gia: chốt một từ — *(chốt 22/09)*

Bản Word ngày 22/09 gọi cùng một thứ bằng **ba** từ: `client` (51 lần), `thiết bị` (18 lần), `bên` (11 lần). Trong cùng mục 2.1.3 có cả *"chia dữ liệu đều cho các **client**"* lẫn *"giao tỉ lệ số mẫu của lớp $j$ cho **bên** $i$"*. Không sai, nhưng người đọc mất một nhịp mỗi lần chuyển từ, và đây là loại chỗ phản biện ghi ra lề.

Quy ước từ nay:

- **Chương 1 dùng "thiết bị"**, xuyên suốt. Chương này cố ý phi kỹ thuật và "thiết bị" gần với trực giác về FL trên điện thoại.
- **Từ Chương 2 trở đi dùng "client"**, xuyên suốt. Giới thiệu đúng **một lần** ở 2.1.1, dạng *"mỗi bên tham gia huấn luyện, sau đây gọi là client"*, rồi không đổi nữa.
- **Không dùng "bên" như danh từ chỉ client**, kể cả khi thuật lại công trình khác — thuật lại thì cũng dùng "client". Chữ "bên" chỉ còn dùng trong nghĩa thông thường ("vế bên trái", "hai bên khớp nhau").
- Các từ khác cùng nghĩa — "máy khách", "nút", "người tham gia" — không dùng.

### 7.3. Trích dẫn
- Định dạng IEEE (khớp công trình hội nghị)
- File `.bib` dùng chung: `paper/thesis/refs.bib` `[CẦN TẠO]`
- **Mọi con số từ `Calibration-reproduce.pdf` phải kèm caveat theo IR#1**

### 7.4. Hình/bảng
- **Mọi bảng và mọi hình đều phải có số và tên** — *(chốt 21/09, không có ngoại lệ)*. Quy ước: `**Bảng <chương>.<thứ tự>.** <tên>` đặt **ngay trên** bảng (chuẩn IEEE), `**Hình <chương>.<thứ tự>.** <tên>` đặt **dưới** hình; đánh số liên tục trong từng chương
- Caption phải **tự đủ nghĩa** (đọc riêng vẫn hiểu, không cần thân bài) và **giải thích mọi ký hiệu** xuất hiện trong bảng/hình
- Thân bài gọi bằng **số bảng/hình** ("Bảng 2.2 cho thấy…"), không gọi bằng cách mô tả ("bảng đối chiếu ở mục sau"). Đây là ngoại lệ có chủ ý so với quy tắc cấm tham chiếu `§` ở §7.5 — số bảng tra được qua danh mục bảng, ký hiệu mục thì không
- Bảng trong **khối trạng thái** đầu mỗi file chương là siêu dữ liệu cho người viết, **không** đánh số và sẽ bị gỡ khi kết xuất bản nộp
- Mọi bảng kết quả ghi: exp-id, $n$ seed, số vòng, backbone + $d$, phép kiểm định
- Thanh sai số là **CI 95%**, không phải sd — ghi rõ trong caption

### 7.5. Văn bản phải đọc độc lập được — *(chốt 21/09, áp dụng mọi chương)*

Người đọc luận văn **không có** đề cương đã duyệt, **không có** tài liệu này, và **chưa đọc** các chương sau. Mọi chương phải hiểu được trong điều kiện đó.

- **Cấm viện dẫn đề cương như nguồn quyền uy.** Không viết "như đã đăng ký trong đề cương", "theo Output đã đăng ký". Nếu một lựa chọn cần biện minh thì biện minh bằng nội dung, tại chỗ.
- **Cấm đẩy lập luận ra tham chiếu mục.** Không viết "§X trình bày lý do", "xem §Y để biết vì sao". Lý do phải nằm trong câu; tham chiếu chỉ còn là chỉ dẫn đọc thêm.
- **Gọi tên phương pháp cụ thể**, không viết "công trình gốc", "một phương pháp hiệu chuẩn", "nền tảng thực nghiệm thứ hai" khi có thể nêu tên. Tên nêu lần đầu đi kèm trích dẫn.
- **Định nghĩa thuật ngữ ở lần xuất hiện đầu**, kể cả những thuật ngữ quen thuộc trong nhóm (label skew, feature skew, classifier head).

### 7.6. Kỷ luật độ dài — *(chốt 21/09)*

Format nộp: **A4 · Times New Roman 13 · giãn dòng 1,5 · lề trên/dưới 2,5 cm · trái 3,5 cm · phải 2 cm.** Mọi ước lượng số trang trong tài liệu này phải quy về format đó.

- **Chương 1 là chương giới thiệu, không phải chương khảo sát.** Trần cứng: §1.1 ≤ 1 trang. Cấm mở rộng phần khảo sát văn liệu ở §1.1 — đó là việc của Ch.2. Cấm trình bày lại lập luận về thiết kế đo ở §1.2 — đó là việc của Ch.4.
- **Mỗi ý viết một lần, ở đúng một chương.** Nếu một đoạn ở Ch.1 lặp nội dung Ch.2 hoặc Ch.4, cắt đoạn ở Ch.1.
- **Văn xuôi liền mạch cho Ch.1 và Ch.6.** Không tiểu mục ba cấp (`1.1.1`), không khối in đậm mở câu, không bảng — trừ khi bảng thực sự chở dữ liệu.
- ✅ **Ngoại lệ duy nhất, chốt 22/09: §1.2.1 được đánh số 1–4.** Bốn mục tiêu cụ thể trình bày thành danh sách đánh số, mỗi mục một câu, bỏ các từ "Thứ nhất / Thứ hai / …" vì số thứ tự đã làm việc đó. Lý do phá lệ: danh sách mục tiêu cụ thể là chỗ hội đồng đối chiếu với đề cương đã duyệt, và nhồi bốn câu dài vào một đoạn văn xuôi khiến không tra được. **Agent sau không được gỡ số về lại văn xuôi.** Ngoại lệ **chỉ áp cho §1.2.1**; §1.1, §1.2.2, §1.2.3, §1.3, §1.4 vẫn văn xuôi liền mạch. ⚠️ Cần đối chiếu mẫu trình bày của khoa về danh sách đánh số trong thân bài trước khi định dạng trong Word.
- ⚠️ **Ngân sách trang ở §4 của tài liệu này đã lỗi thời cho Ch.1.** §4 ghi 6–7 trang; bản 21/09 chỉ khoảng **3–3,5 trang** và đó là **có chủ ý**. Agent sau **không được** viết phồng Ch.1 trở lại cho khớp con số cũ. Phần trang tiết kiệm được chuyển sang Ch.2 và Ch.5.

### 7.7. Chống giọng văn máy — *(chốt 22/09)*

Bản Ch.1–Ch.2 ngày 22/09 đã được đọc rà riêng cho lối viết. Kết luận: văn **sạch** — không sáo rỗng, không hô khẩu hiệu, không bôi chữ — nhưng **đều nhịp tới mức lộ**. Người đọc không bắt được lỗi nào cụ thể mà vẫn thấy "nghe như máy viết". Nguyên nhân không nằm ở từ ngữ mà ở chỗ **cùng một khuôn câu lặp lại quá dày**.

Vì vậy các quy tắc dưới đây là **hạn ngạch, không phải lệnh cấm**. Mỗi khuôn câu bị hạn ngạch đều hợp lệ và có chỗ dùng đúng; cái phải tránh là để nó thành nhịp.

**AI#1 — Hạn ngạch cấu trúc tương phản.** Khuôn *"X chứ không phải Y"* / *"không phải X, mà Y"* / *"Y thay vì X"*: tối đa **ba lần mỗi chương**, không quá một lần mỗi trang, và **không bao giờ hai lần trong cùng một đoạn**. Dành hạn ngạch cho chỗ thật sự phải phân định ranh giới — ví dụ *"ghép cặp theo từng mẫu, mạnh hơn căn chỉnh biên, không yếu hơn"* ở mục FedBR, nơi cả câu tồn tại để sửa một cách hiểu sai. Ở những chỗ còn lại, viết câu khẳng định thẳng: *"Luận văn xác định biên giới hiệu lực của cơ chế đã có."* thay cho *"Luận văn không đề xuất thuật toán mới, mà xác định biên giới hiệu lực của cơ chế đã có."*

**AI#2 — Không để đoạn nào cũng đáp xuống bằng một câu chốt.** Câu kết có nhịp đối, kiểu *"…một khoảng hẹp quanh 0 vẫn là một kết luận, còn một kiểm định không có ý nghĩa thống kê thì không."*, tối đa **một lần mỗi mục hai cấp**. Từng câu như vậy đều hay; nhưng nếu đoạn nào cũng kết như vậy thì cả chương thành văn châm ngôn. **Cho phép đoạn kết nhạt** — kết bằng một con số, một chi tiết kỹ thuật, hay một mệnh đề phụ là chuyện bình thường trong văn học thuật, và chính sự không đều đó mới giống người viết.

**AI#3 — Nhịp ba.** Liệt kê đúng ba thành phần (*"A, B, và C"*) tối đa **một lần mỗi trang**. Có bốn thứ thì viết bốn, có hai thì viết hai; không bớt đi hay thêm vào cho tròn ba.

**AI#4 — Một câu rào cho mỗi chương.** Câu tự giới hạn phạm vi (*"đây là mục tiêu nghiên cứu, không phải cam kết…"*, *"chỉ có hiệu lực trong phạm vi khảo sát mà Chương 2 mô tả"*, *"hai thành phần đầu đứng vững độc lập với…"*) giữ **đúng một câu mỗi chương**, đặt ở chỗ cần nhất. Phần còn lại dồn về **Ch.6 §6.3 Hạn chế** — đó là nơi người đọc đi tìm giới hạn. Nhiều câu rào rải khắp chương không làm luận văn chắc hơn; nó chỉ làm giọng nghe như đang cãi với một phản biện vô hình. *(Đây là quy tắc "cấm giọng phòng thủ" chốt 22/09, nay có hạn ngạch cụ thể.)*

**AI#5 — Đa dạng độ dài và cách mở câu.** Không để **ba câu liên tiếp** cùng khuôn: cùng mở bằng trạng ngữ, cùng dạng *"X là Y"*, hoặc cùng dài 25–35 từ. Sau một câu dài phải có một câu ngắn. Hai đoạn liền nhau không mở đầu bằng cùng một loại cụm từ.

**AI#6 — Dấu gạch ngang chêm.** Dấu `—` chêm giữa câu tối đa **một lần mỗi trang**; chỗ khác dùng dấu phẩy, ngoặc đơn, hoặc tách thành câu riêng. Bản 22/09 dùng rất dày và đây là dấu hiệu dễ nhận nhất đối với người đọc quen.

**AI#7 — Thuật ngữ tự đặt phải trả giá.** Mỗi cụm danh từ hoá do luận văn tự đặt — *"biên giới hiệu lực"*, *"mặt vận hành"*, *"đường đặc tuyến"*, *"ngân sách tinh chỉnh"*, *"trục độ nghiêm trọng"* — phải được **định nghĩa bằng một câu ngay tại lần xuất hiện đầu**; không định nghĩa được thì thay bằng cách nói thường. Toàn luận văn không dùng quá **năm** thuật ngữ tự đặt. *(Hiện Ch.1 §1.3 dùng "đường đặc tuyến" và "ngân sách tinh chỉnh" mà chưa định nghĩa ở đâu — phải sửa.)*

**AI#8 — Cụm sáo cấm dùng.** "đóng vai trò quan trọng" · "không chỉ… mà còn" · "điều đáng chú ý là" · "cần nhấn mạnh rằng" · "có thể thấy rằng" · "nhìn chung" · "về cơ bản" · "trong bối cảnh … ngày càng" · "mở ra hướng đi mới" · "đầy hứa hẹn" · "toàn diện" · "mạnh mẽ" (khi đang dịch *robust* / *strong*). Thay bằng phát biểu trực tiếp có nội dung.

**AI#9 — Mỗi đoạn một việc, và nói việc đó ngay câu đầu.** Không mở đoạn bằng câu dẫn nhập rỗng (*"Trước khi đi vào chi tiết, cần làm rõ…"*). Nếu câu đầu bỏ đi mà đoạn vẫn đủ nghĩa thì bỏ.

**AI#10 — Giữ câu của học viên.** Khi agent sửa một đoạn do học viên tự viết, chỉ sửa cái **sai** (ngữ pháp hỏng, thuật ngữ sai, trích dẫn sai). **Không làm mượt** một câu chỉ vì nó mộc. Văn mộc không đều là thứ duy nhất không giả được, và làm mượt hết chính là cách bản 22/09 trở nên đều nhịp.

#### Cách tự kiểm trước khi nộp mỗi chương

Chạy trên file chương rồi ghi số đếm vào khối trạng thái đầu file:

```bash
rg -c "chứ không|không phải .*mà |thay vì"   # AI#1 — quá 3/chương thì cắt
rg -o "—" | wc -l                            # AI#6 — chia cho số trang, quá 1 thì cắt
rg -ni "đóng vai trò quan trọng|không chỉ.*mà còn|đáng chú ý là|cần nhấn mạnh|nhìn chung|về cơ bản|đầy hứa hẹn|mở ra hướng"   # AI#8 — phải ra 0
```

Phép thử cuối, không tự động được: **đọc to ba đoạn liên tiếp bất kỳ.** Nếu cả ba cùng kết bằng một câu chốt, hoặc cả ba cùng chứa một cặp tương phản, viết lại hai trong ba.

---

## 8. Quy ước file

| File | Vai trò |
|---|---|
| `00_outline.md` | tài liệu này: dàn bài và giao ước hướng B |
| `01_chuong1.md` … `06_chuong6.md` | bản nháp các chương theo hướng B. Mỗi file mở bằng khối trạng thái và bảng ánh xạ với Word |
| `PLAN_huong-B.md` | kế hoạch thực nghiệm T0–T2 và ngân sách |
| `INDEX_ma-nguon-va-ket-qua.md` | chỉ mục mã nguồn và kết quả, dùng chung cho mọi hướng |
| `NOTE_khao-sat-van-lieu.md`, `NOTE_bien-ban-binh-duyet.md` | ghi chép khảo sát văn liệu và bình duyệt; dữ kiện văn liệu vẫn dùng được, phần kết luận chiến lược thuộc hướng cũ |
| `archive/2026-09-24_huong-bien-gioi-hieu-luc/` | toàn bộ bản thảo hướng cũ, kể cả dàn bài cũ và các bảng trước/sau ngày 24/09. Chỉ tra, không thực hiện theo, trừ phần dàn bài này dẫn tên |

**Chỉ-append trong file chương** (giữ từ 22/09): yêu cầu sửa gom thành khối `# YÊU CẦU SỬA — <ngày>` ở cuối file; bản đã sửa chép xuống dưới mốc `# PHIÊN BẢN CHỈNH SỬA — <ngày>`. Mọi khối cũ giữ nguyên. Khi sửa Word, mỗi khối yêu cầu có **bảng trước/sau** (Mục · Tìm trong Word · Trước · Sau · Lý do), cột "Trước" chép nguyên văn từ Word. Đổi hướng lớn thì chuyển cả bộ file vào `archive/` và commit ảnh chụp trước.

---

## 9. Nhật ký trạng thái

| Ngày | Sự kiện |
|---|---|
| 2026-09-24 | **Đổi sang hướng B** theo quyết định của học viên, sau khi so với đề cương. Hướng cũ ("xác định biên giới hiệu lực của cơ chế Taylor") được commit làm ảnh chụp (`c5ff78a`) rồi chuyển vào `archive/2026-09-24_huong-bien-gioi-hieu-luc/`. Hướng B: khung chia sẻ mẫu trung bình với ba cách dùng thay được (FedMix/Taylor, NaiveMix, FedBR), đánh giá trên hai nền tảng. Hướng A (FedBR cộng số hạng Taylor) giữ làm phần tuỳ chọn, chỉ chạy sau T0–T1. Giữ nguyên tên đề tài. Kế thừa §7 lối viết nguyên văn; IRON RULES kế thừa có sửa, thêm IR#11 (FedBR là phương pháp của Guo và cộng sự) và IR#12 (luôn nêu cách chuẩn hoá số hạng Taylor). Mục 5.2 (Flower) viết ngày 24/09 được mang sang nguyên văn. Đã kiểm với bài FedBR: Bảng 1 **có** FedMix làm đối chứng, nên khoảng trống ở Ch.2 mục 2.4 phải phát biểu hẹp (§1.4) |
| 2026-09-24 *(lượt 2)* | **Viết xong phần lý thuyết Ch.3 và Ch.4, không sửa mã** (quyết định của học viên: tạm chưa đụng code). Ch.3: thêm **mục 3.5 FedBR**, công thức (3.16)–(3.19) **lấy theo mã nguồn** `fedbr/algorithms.py` và `train_fed.py` theo yêu cầu học viên, kèm bảng đối chiếu dòng mã. Ch.4: thân chương đầy đủ 4.1–4.5 (khung bốn giai đoạn, Bảng 4.1 ba cách dùng, chuẩn hoá số hạng Taylor, công thức chi phí truyền thông (4.1), giao thức đo). Hệ quả của việc không sửa mã: mọi kết quả FedMix dùng cách chuẩn hoá của mã phát hành; không có B′; không có đại lượng chẩn đoán theo lớp trên mã FedBR, nên mục tiêu 4 chỉ đo trên Flower; bỏ TOST vì với $n = 3$ nửa rộng khoảng tin cậy khoảng 3 pp. **Phát hiện mới:** trong mã FedBR, FedMix và NaiveMix nhận 32 mẫu trung bình mới mỗi bước, còn FedBR dùng 32 pseudo-sample cố định. Phép so FedBR − FedMix vì vậy là so hai phương pháp hoàn chỉnh, không tách được ảnh hưởng của cách dùng; hàng 5 của Ch.1 đã sửa theo (khối bổ sung cuối `01_chuong1.md`). **Còn chờ học viên:** họ giả thuyết chính ở Ch.4 mục 4.5.5 (H1 FedBR − FedAvg, H2 FedMix − FedAvg, Holm) phải chốt trước T0; Hình 4.1 chưa vẽ |
| 2026-09-25 | **Ch.4 chỉ còn phần đề xuất; Ch.5 mục 5.1 viết xong** (học viên: hội đồng không quan tâm mã nguồn). Ch.4: thêm Thuật toán 4.1 và Hình 4.1 (`figures/hinh4_1.py`); 4.1 và 4.4 bỏ tiểu mục; bỏ 4.1.2 (khung trên mã nguồn) và 4.2.4 (đọc các phép so sánh); Bảng 4.1 chuyển vào 4.2; 4.3 chỉ nêu logic, không nhắc bản cài đặt của ai; 4.5 chuyển sang Ch.5 mục 5.1. Ch.5: viết 5.1.1–5.1.4, đánh lại số bảng (5.1–5.3 ở 5.1; cũ 5.1–5.7 thành 5.4–5.10); "mã nguồn FedBR" → "nền tảng FedBR". Ch.4 và Ch.5 được sửa đè vì chưa đưa vào Word. Chờ học viên quyết: đoạn DevPranjal ở 5.2.1, mục 5.3.3 kiểm toán mã. |
| 2026-09-25 *(lượt 2)* | **Phụ lục A và rà Ch.3.** Mục 5.3.3 (kiểm toán mã FedBR) chuyển sang `07_phu-luc.md`, Phụ lục A. Ch.5 bỏ tên DevPranjal khỏi thân bài, sửa số trích dẫn theo Word (FedBR [2], CCVR [8]), trọng số $L_{	ext{bal}}$ đổi ký hiệu thành $\gamma$. Ch.3 rà trên bản Word 25/09: khối `RÀ SOÁT — 25/09/2026` cuối `03_chuong3.md`, 18 hàng (bỏ đoạn "Ánh xạ sang cài đặt", bỏ số của công thức đơn hình để hết trùng (3.2), gỡ các câu còn theo hướng cũ). Ch.3 và Ch.4 chỉ-append vì đã có trong Word; Ch.5 sửa đè. |
| 2026-09-26 | **Rà Ch.1, Ch.2, Ch.3 theo Word 26/09** (chỉ-append). Ch.3: mục 3.5 viết lại không có tiểu mục "Ký hiệu" (3.5.1–3.5.5), sửa hai câu "Mã nguồn…" còn trong Word. Ch.1 (11 hàng) và Ch.2 (15 hàng): bỏ mọi chỗ nói về mã nguồn; **đóng góp thứ ba đổi thành "kiểm chứng lại các kết quả đã công bố"** (đo lại trên Flower, tái hiện bảng FedBR, chỉ ra thừa $1/B$), danh mục kiểm toán sang Phụ lục A; bỏ câu "khung sửa phép chuẩn hoá" vì không sửa mã; 2.4.1 đổi tiêu đề thành "Đối chứng giữa FedMix và NaiveMix" và nói rõ không chạy cấu hình cô lập; sửa trích dẫn sai ([2]→[4] ở 2.1.2; MOON [6] là FedProx, MOON thiếu trong danh mục). |
| 2026-09-26 *(lượt 2)* | **Hướng A: chốt thiết kế và cài M3** (`FedBRTaylor`). Bốn quyết định của học viên: giữ nguyên mục tiêu FedBR và *cộng thêm* $\lambda$(II) + $\lambda(1{-}\lambda)$(III), không co ảnh; hai cấu hình nhãn soft/uniform; đối chứng không-(III) bằng cờ; chỉ chuẩn hoá theo công thức; hạt giống 12345 trước. Thiết kế đầy đủ ở khối 26/09 cuối `04_chuong4.md`; mã và test ở `INDEX` §5.1; kế hoạch chạy ở `PLAN_huong-B.md` §3–§5. Mã chưa commit. Thân Ch.4, Ch.5 **chưa** nhắc A (dàn bài §1.1). Thứ tự chạy T0 → T1 → T2 giữ nguyên |
| 2026-09-26 *(lượt 3)* | **Thăm dò hiệu chuẩn tầng phân lớp bằng mẫu trung bình, có số liệu.** Script `fedbr/scripts/calibrate_head.py` (`make calibrate-head`) chạy trên `model.pkl` của 9 thuật toán trong `02_attempt`: đóng băng $\phi$, huấn luyện lại $\omega$ trên mẫu trung bình có nhãn mềm, quét $M$. Kết quả (LDA, 2000 mẫu/client, một hạt giống): cải thiện chỉ dương ở $M \le 2$ (FedAvg +5,8 ở $M=1$), âm từ $M=3$, ở $M=10$ mọi mô hình sụt 14–54 điểm; FedBR chỉ +1,3 ở $M=1$, nên khoảng 4,5 trong 9,9 điểm FedBR hơn FedAvg nằm ở tầng phân lớp. Viết thành **Ch.5 mục 5.3.3** (Bảng 5.10, Hình 5.1; bảng chi phí thành Bảng 5.11); số liệu ở `INDEX` §5.2b. Đây là cách dùng thứ tư của mẫu trung bình, sau huấn luyện; Bảng 4.1 chưa có hàng cho nó `[QUYẾT: có đưa vào 4.2 không]`. T2 (hướng A) đang chạy trên Vast, chưa có số liệu. Script, test, hình và các tệp luận văn lượt này chưa commit |
| 2026-09-26 *(lượt 4)* | **Nền tảng FedBR chỉ dùng một hạt giống (12345); T0 bỏ** (quyết định của học viên: mỗi lượt FedBR 1000 vòng mất khoảng 7,5 giờ). Nền tảng Flower giữ ba hạt giống. Thứ tự chạy thực tế vì vậy đổi so với lượt 2: T0 bỏ, T2 đang chạy trên Vast, T1 (NaiveMix) tuỳ chọn. Ch.5 sửa đè: 5.1.3 thêm **ngưỡng đọc 3 pp** cho nền tảng FedBR (lấy từ chênh lệch lượt chạy lại so với bảng công bố); 5.1.4 bỏ kiểm định t và Holm, H1/H2 thành S1/S2; 5.3.2 viết xong (Bảng 5.10, cả chỉ số chính và năm mốc cuối: FedBR − FedAvg +6,37 / +7,35; FedMix − FedAvg −2,29 / −0,58); 5.3.3 đặt lại thành phép chẩn đoán, không còn gọi là cách dùng thứ tư, nên Ch.4 không phải sửa, thêm chi phí chia sẻ 2000 mẫu/client (khoảng 247 MB) và bỏ hai câu so độ lớn giữa hai nền tảng; đánh lại số: bảng hiệu chuẩn thành 5.11, bảng chi phí thành 5.12. Dàn bài: §1.4, IR#5, IR#12, §3, §4, §5 cập nhật. **Ch.1, Ch.2 trong Word còn câu "ba hạt giống" cho mọi so sánh; học viên chọn chưa rà.** |
| | *(agent tiếp theo cập nhật vào đây)* |
