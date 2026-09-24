# 00 — DÀN BÀI LUẬN VĂN THẠC SĨ & HƯỚNG DẪN THỰC HIỆN

> **Tài liệu này có hai vai trò:** (1) dàn bài để viết luận văn 50–60 trang; (2) **bản giao ước cho mọi agent/người viết ở các bước sau**. Đọc hết §0–§2 trước khi viết bất kỳ chương nào.

---

## 0. Siêu dữ liệu

| | |
|---|---|
| **Tên đề tài (VI)** | NÂNG CAO HIỆU SUẤT HỌC LIÊN KẾT THÔNG QUA TĂNG CƯỜNG DỮ LIỆU DỰA TRÊN KHAI TRIỂN TAYLOR |
| **Tên đề tài (EN)** | ENHANCING FEDERATED LEARNING PERFORMANCE VIA DATA AUGMENTATION BASED ON TAYLOR EXPANSION |
| **Trạng thái tên đề tài** | **GIỮ NGUYÊN — KHÔNG ĐỔI.** Không có đơn đổi đề tài, không có giải trình chỉnh sửa, không xét duyệt lại |
| Học viên | Vũ Tuấn Kiệt — MSHV 240201043, Khóa 2024 Đợt 02, CNTT 8480201 |
| CBHD | PGS.TS. Nguyễn Tấn Cầm |
| Hướng | Nghiên cứu, 15 TC · 12 tháng |
| Độ dài mục tiêu | 50–60 trang (không kể phụ lục, tài liệu tham khảo) |
| Ngôn ngữ | Tiếng Việt; thuật ngữ chuyên ngành giữ tiếng Anh trong ngoặc ở lần xuất hiện đầu |
| Tài liệu nền | `paper/ref/Calibration-reproduce.pdf` · `paper/ref/Guo et al. - 2023 - FedBR...pdf` · `paper/thesis/Decuong_DataAugmentationFL_VuTuanKiet.pdf` · `REPRODUCE.md` · mã nguồn `fedbr/` |
| **Chỉ mục mã nguồn & kết quả** | **`paper/thesis/INDEX_ma-nguon-va-ket-qua.md`** — đọc trước khi viết bất kỳ con số, cấu hình hay mô tả cài đặt nào. Phủ bốn nguồn: (1) kho Flower của Bài 1 `C:\Users\KietVu\Testplace\uit-msc-dp-adaptive-fedmix` (mã, `runs/`, `paper/conference/`; bài hội nghị = `Calibration-reproduce.pdf` là **bản trước phản biện**, bản camera-ready là `paper/conference/main.pdf` @ `cdac4ae`); (2) kho `FedBR` này; (3) kết quả chạy FedBR `C:\Users\KietVu\Testplace\FedBR\output\cifar10` (chỉ trích `02_attempt_20260916`); (4) mã tham chiếu DevPranjal `C:\Users\KietVu\Testplace\fedmix\fedmix`. §1 của chỉ mục liệt kê sáu phát hiện ảnh hưởng trực tiếp tới luận văn |
| **Bài 1 (IR#9)** | *When Does Classifier Calibration Reproduce Under Non-IID Federated Learning? A Controlled Study on a Faithful Flower Stack* — V. T. Kiet, N. T. Cam. **2026 10th IEEE Symposium on Wireless Technology & Applications (ISWTA 2026)**, accepted, camera-ready đã nộp; chưa có DOI. Tài trợ CS4-2026-80299. ⚠️ Không dùng tên "ISCIT" và hạng CORE B còn sót trong `refs.bib` của kho Flower — xem chỉ mục §2 |
| **Bản chính (Word)** | `C:\Users\KietVu\OneDrive\Study\UIT\Master\16_FinalThesis\LuanVan\VuTuanKiet_KLTN_Thsi_2026.docx` — **khi file `.md` và bản Word lệch nhau, bản Word đúng** (chốt 22/09). Đọc bằng cách giải nén `word/document.xml`; công thức là OMML nên trích văn bản thuần sẽ mất nội dung công thức, chỉ còn số phương trình |
| Biên bản bình duyệt | `paper/thesis/Bien-ban-binh-duyet-va-lo-trinh-sua.md` — **mọi finding BLOCKING trong đó đã được nội hoá thành IRON RULES ở §2** |

---

## 1. Khung chiến lược — đọc trước khi viết

### 1.1. Luận văn này là **thực hiện** đề cương đã duyệt, không phải thay nó

Mục tiêu tổng quát đã đăng ký:

> *"**Nghiên cứu cơ sở lý thuyết** về các kỹ thuật làm phong phú không gian đặc trưng và phương pháp xấp xỉ hàm mất mát dựa trên khai triển Taylor trong môi trường học máy phân tán."*

Đây là mục tiêu **nghiên cứu**, không phải cam kết thắng baseline. Luận văn hoàn thành nó bằng cách xác định **cơ chế này hoạt động khi nào, không hoạt động khi nào, và vì sao**.

### 1.2. Câu hỏi nghiên cứu

> **RQ tổng quát:** Tăng cường dữ liệu dựa trên khai triển Taylor cải thiện Học liên kết trên dữ liệu không đồng nhất trong điều kiện nào?

| | Câu hỏi con | Trả lời ở |
|---|---|---|
| **RQ1** | Số hạng khai triển Taylor bậc nhất có mang tín hiệu **tách biệt** khỏi bản thân phép trộn trung bình không? | Ch.5 §5.3 (E1) |
| **RQ2** | Kết luận âm thu được dưới **label skew** có chuyển sang **feature skew** — chế độ mà cơ chế được cho là có "nhà tự nhiên" — không? | Ch.5 §5.4 (E3) |
| **RQ3** | Gain phụ thuộc thế nào vào ngân sách vận hành $(\lambda, M)$, và đánh đổi với chi phí truyền thông / độ nén bảo mật ra sao? | Ch.5 §5.5 (E2) |
| **RQ4** | Cơ chế nào giải thích kết quả? Thiên lệch có nằm ở ranh giới quyết định như đề cương giả định không? | Ch.5 §5.7 (E5) |
| ~~**RQ5**~~ | ~~Lời giải thích cơ chế (thiên lệch ở classifier head) có còn hiệu lực ở tác vụ **không có** classifier head — tức hồi quy?~~ | **`[GÁC]` từ 22/09** — xem §10 |

> **RQ5 đã được gác lại (22/09, quyết định của học viên).** Luận văn hiện làm **bốn** câu hỏi nghiên cứu. Nội dung nhánh hồi quy được giữ nguyên tại chỗ ở §3.2 (P-9), §4 (Ch.4 §4.6, Ch.5 §5.8), §5.1 (E6) và §5.3, đánh dấu `[GÁC]`, để mở lại mà không phải dựng lại. **Chừng nào chưa mở lại thì không chương nào được nhắc tới hồi quy** — kể cả như một câu phụ trong phần phạm vi.

### 1.3. Ba đóng góp

**C1 — Cô lập số hạng Taylor bậc nhất.** Cặp `FedMix` / `NaiveMix` tách số hạng $\nabla_x\mathcal{L}\cdot\bar{x}_g$ khỏi bản thân phép trộn trung bình. Theo khảo sát của chúng tôi, phép tách này chưa được thực hiện trong văn liệu — **phải kiểm chứng lại bằng tìm kiếm văn liệu có ghi chép (xem IRON RULE #3) trước khi phát biểu.**

**C2 — Mặt vận hành $(\lambda, M)$ và ba chế độ lệch phân phối.** Báo cáo gain như một **đường đặc tuyến vận hành**, không phải một con số, trên ma trận 2×2 {label skew} × {feature skew} cộng trục độ nặng $\alpha_{\text{rot}}$ — trực tiếp giao Output đã đăng ký của đề cương ("báo cáo phân tích về sự cân bằng giữa hiệu suất và chi phí tài nguyên").

**C3 — Mở rộng phạm vi hiệu lực của công trình hội nghị + kiểm toán tính tái lập.** Gỡ ba giới hạn ngoại vi mà paper hội nghị **tự tuyên bố**: (a) *"within-stack only"* → stack thứ hai (DomainBed/FedBR); (b) *"one heterogeneity type (label skew)"* → feature skew; (c) *"BN-free backbone is load-bearing"* → backbone chuẩn hoá. Kèm danh mục sai lệch code↔paper phát hiện trong quá trình tái hiện.

### 1.4. Vì sao tên đề tài vẫn trung thực

Tên nói "nâng cao hiệu suất **thông qua** tăng cường dữ liệu dựa trên khai triển Taylor". Luận văn nghiên cứu **chính kỹ thuật đó** và xác định biên giới hiệu lực của nó. Nếu kết quả cho thấy cơ chế chỉ hiệu quả trong một vùng hẹp (hoặc không hiệu quả), đó là **kết quả nghiên cứu**, không phải mâu thuẫn với tên đề tài — và Mục tiêu tổng quát đã đăng ký là điều khoản chi phối.

→ **Ch.1 §1.1 phải nêu điều này tường minh.** Không né, không viết như thể đã biết kết quả sẽ dương.

### 1.5. Bài hội nghị là công bố của luận văn, không phải nguồn trích — *(quyết định của học viên, 24/09)*

Luận văn viết **như thể chưa có bài hội nghị**. Các thực nghiệm trên stack Flower là thực nghiệm của chính luận văn:
- FedMix dưới lệch nhãn;
- C1 và C1+C2 (thăm dò);
- số hạng bậc hai;
- CCVR theo ngân sách mẫu ảo;
- bốn head hiệu chuẩn và trần LDA;
- thiên lệch định hướng.

Các kết quả này được trình bày ở **Ch.5 mục 5.2 mới** "Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower", đặt trước các thực nghiệm trên mã nguồn FedBR. Bài ISWTA 2026 là **điểm cộng**: nó cho thấy một phần kết quả luận văn đã qua phản biện và được nhận đăng.

Ràng buộc kéo theo, áp cho mọi agent:
1. **Thân bài không trích bài hội nghị**: không `[TG]`, không `[17]` cho bài đó, không "công trình trước của tác giả", không "nguồn tự khai". Bài chỉ xuất hiện ở *Danh mục công bố khoa học của tác giả* và *Lời cam đoan*. Câu mẫu cho cả hai ở cuối `01_chuong1.md`, khối 24/09.
2. **Ch.3 chỉ giữ lý thuyết.** Mục 3.6 bỏ hẳn. Mục 3.4.2 viết lại thành hai giả thuyết (thiên lệch ở độ lớn hay ở hướng), còn số đo nằm ở Ch.5 mục 5.2.4. Mục 3.5.2 không còn "đo lường trong [17]". Bảng trước/sau ở cuối `03_chuong3.md`.
3. **Hai nền tảng đều của luận văn**: Flower cho lệch nhãn, FedBR cho lệch đặc trưng. Kỷ luật within-stack (IR#4) giữ nguyên.
4. **Kỷ luật báo cáo của IR#1 vẫn áp**, nay cho chính kết quả Flower: nhãn thăm dò cho C1 và C1+C2; phép đối chiếu với DevPranjal là *kiểm tra tính nhất quán, không phải kiểm chứng độc lập*; CINIC-10 chỉ đọc mô tả.
5. Mọi bảng trước/sau để sửa Word nằm ở khối `YÊU CẦU SỬA — 24/09/2026` cuối mỗi file chương 01–05.

---

## 2. IRON RULES — ràng buộc bắt buộc cho mọi agent/người viết

> Các quy tắc dưới đây phát sinh từ một vòng bình duyệt 5 ghế đã tìm ra 4 khiếm khuyết CRITICAL trong bản đề xuất trước. **Vi phạm bất kỳ quy tắc nào = viết lại mục đó.**

**IR#1 — Không bao giờ trích dẫn paper hội nghị mạnh hơn mức nó tự tuyên bố.**
> ⚠️ **Sửa 24/09 (§1.5).** Thân bài không còn trích bài hội nghị. Ba caveat dưới đây **vẫn giữ nguyên hiệu lực**, nhưng nay là kỷ luật báo cáo cho chính kết quả Flower ở Ch.5 mục 5.2, không phải quy tắc trích dẫn. Chỗ nào dưới đây viết "nguồn" thì hiểu là "luận văn".
Ba caveat bắt buộc phải đi kèm mỗi lần dùng số liệu từ `Calibration-reproduce.pdf`:
- Reimplementation thứ hai là *"a consistency check, **not independent validation** ... since it is also our calibration target"*. **Cấm dùng từ "độc lập".**
- C1, C1+C2, T2 và feature-space transform được nguồn gắn nhãn **exploratory**; T2 và transform là **single-seed, untuned**. Nguồn viết: *"the four extensions we report as exploratory, not as failures of published methods."*
- Kết quả CINIC-10 ↔ CIFAR-10: *"Since CINIC-10 contains CIFAR-10, we read these pairs **descriptively, not as an inference test**."*

**IR#2 — Phát biểu bằng khoảng tin cậy, không bằng dấu.**
Cấm viết "âm trên mọi seed" như bằng chứng chính (đó là sign test 3/3, exact $p=0.25$). Viết: cận trên 95% một phía. Chỉ **FedMix ($m{=}1$)** loại trừ được gain ≥0 (**−0.52 pp**); C1 (+0.16) và C1+C2 (+0.38) **không**.
⚠️ **Sửa 24/09 — ghi nguồn đúng.** Ba cận trên này **không có trong Bài 1**; khoảng tin cậy đã bị cắt khỏi bài vì giới hạn 6 trang. Chúng là **phép tính của luận văn** trên ba hiệu theo hạt giống mà Bài 1 báo cáo, với $t_{0,95;2}=2{,}920$, $n=3$. Trong luận văn viết dạng: *"Từ ba hiệu theo cặp −2,19 / −0,95 / −2,43 báo cáo trong [TG], cận trên khoảng tin cậy 95% một phía là −0,52 điểm phần trăm."* Các giá trị cũ −0,53 và +0,17 là kết quả tính từ trung bình và độ lệch chuẩn **đã làm tròn** (−1,86 ± 0,79; −1,90 ± 1,23), không sai nhưng không tái lập được từ số theo hạt giống. Chi tiết: `INDEX_ma-nguon-va-ket-qua.md` F2.

**IR#3 — Không phát biểu tuyên bố mới lạ phủ định toàn cầu mà không có tìm kiếm văn liệu có ghi chép.**
Cấm các câu dạng "chưa ai làm", "chưa có nghiên cứu nào". Thay bằng tuyên bố **có hạn định**.

> ⚠️ **Sửa cách thi hành, 22/09.** Hạn định phải nằm **trong chính câu phát biểu**, không phải trong một mục mô tả quy trình tìm kiếm. **Cấm đưa vào thân luận văn** danh sách nguồn, tên viết tắt hội nghị, danh mục truy vấn, mốc thời gian khảo sát, hay các câu tự bình luận kiểu "phạm vi này được mô tả để người đọc tự đánh giá" — đó là văn của tổng quan hệ thống PRISMA, không phải của luận văn, và không cho người đọc thông tin gì. Nhật ký khảo sát để ở `NOTE_khao-sat-van-lieu.md` và phụ lục.
>
> Hai cách hạn định được chấp nhận, theo thứ tự ưu tiên: (a) **thu hẹp về một đối tượng kiểm chứng được** — "Cấu hình như vậy không xuất hiện trong bài báo FedMix, kể cả ở phần phụ lục"; (b) **một mệnh đề hạn định ngắn** khi buộc phải nói về cả một mảng văn liệu — "Trong số các công trình trích dẫn FedMix mà luận văn khảo sát được, chưa có công trình nào…". Không dùng quá một lần mỗi khoảng trống. Ch.2 phải phủ tối thiểu: NIID-Bench, MOON, VHL, FedDF, FedNTD, FedGen, CCVR, FedProto và dòng prototype.
>
> ⚠️ **Sửa 22/09.** **Deep CORAL** và **FedDecorr** đã được **gỡ khỏi danh mục phủ tối thiểu**. Lý do: bản Word không trình bày hai công trình đó, và quyết định 22/09 là bảng đối chiếu ở §4/Ch.2 mục 2.3 **chỉ chứa phương pháp đã xuất hiện trong thân bài**. Việc này đóng mục xung đột IR#3 còn treo từ 22/09. Nếu sau này đưa hai công trình trở lại thân bài thì đưa lại vào danh mục này.

**IR#4 — Kỷ luật within-stack.**
Cấm so sánh số tuyệt đối giữa stack Flower (Ch.3, công trình hội nghị) và stack DomainBed/FedBR (Ch.5). Mọi gain là **paired Δ trên cùng checkpoint, cùng lần rút phân hoạch**. Claim xuyên stack chỉ được là **cơ chế lặp lại được**, không phải con số.

**IR#5 — Công suất thống kê phải được khai báo TRƯỚC.**
Mỗi bảng kết quả phải ghi: số seed, cỡ hiệu ứng mục tiêu $\Delta^*$, phép kiểm định, và thủ tục hiệu chỉnh so sánh bội. Với $s\approx1.2$ pp: $n{=}3$ cho MDE **3.92 pp** — không đủ. Xem §5.2 để biết thiết kế bắt buộc.
**Nhánh "không có tín hiệu" phải dùng TOST với biên tương đương định trước** — một t-test không ý nghĩa KHÔNG chứng minh null.

**IR#6 — Không mô tả sai FedBR/FedMix.**
- FedBR Component 2 ghép cặp **theo từng mẫu** trên **cùng** $x_p$ — **mạnh hơn** căn chỉnh biên, không yếu hơn. Cấm gọi là "căn chỉnh phân phối biên".
- FedBR **có** thông tin lớp dưới nhánh `use_Mixture` (Eq. 4: $\tilde y_p=\frac{1}{K+1}(\frac1C\mathbf1+\sum y_k)$). "Label-agnostic" nghĩa là *không cần biết phân phối nhãn cục bộ và không cần proxy data có nhãn*, không phải "hàm mất mát không điều kiện theo lớp".

**IR#7 — Báo cáo tham số đúng như mã nguồn, không như văn bản mô tả.**
- Nồng độ Dirichlet của phép xoay: `p = ones(10)/10` rồi `Dirichlet(1.0*p)` → **0.1 mỗi thành phần** (≈**2.08 góc hiệu dụng**/client), tức feature skew mặc định **đã ở gần cực trị**. `REPRODUCE.md` §2 và paper FedBR đều mô tả mơ hồ là "Dir(1.0)".
- Chiều đặc trưng $d$ **không phải hằng số**: `cct`=256 (mặc định code phát hành), `vgg11`/`resnet18*`=512, `resnet20_gn`=**64**. Ghi $d$ trong mọi bảng.
- Projection MLP của FedBR: Appendix A ghi 256/128, mã ghi đè thành **1024/512**.

**IR#8 — Mọi con số trong luận văn phải truy vết được.**
Mỗi bảng/hình ghi rõ: experiment ID (§5.1), số run, số seed, số vòng, backbone, $d$, và đường dẫn `results.jsonl`. Cấm con số không nguồn.

**IR#9 — Khai báo tái sử dụng công trình đã công bố.**
> ⚠️ **Sửa 24/09 (§1.5).** Kết quả của bài hội nghị là kết quả của luận văn, nên phần "trích dẫn đầy đủ ở đầu chương" **bỏ**. Còn lại ba việc:
> 1. liệt kê bài ở *Danh mục công bố khoa học của tác giả* (tên hội nghị, năm và trạng thái đã có ở §0; DOI khi có);
> 2. một câu trong *Lời cam đoan* khai báo phần kết quả đã công bố, với CBHD là đồng tác giả;
> 3. các việc hành chính A2–A4 ở §9, nếu quy chế của Trường đòi.
Ch.3 dựa trên công trình đã được chấp nhận đăng, đồng tác giả là CBHD. Bắt buộc: trích dẫn đầy đủ ở đầu chương + Lời cam đoan; văn bản xác nhận của đồng tác giả; đối chiếu điều khoản tái sử dụng của nhà xuất bản; khai báo tỉ lệ trùng lắp dự kiến **trước** khi quét. **Phải nêu tên hội nghị, năm, trạng thái (accepted/published), DOI/chỉ mục** — cấm gọi chung chung "paper hội nghị".

**IR#10 — Không viết kết quả chưa chạy.**
Mọi mục Ch.5 đánh dấu `[CẦN CHẠY]` phải để trống hoặc ghi `[CHỜ SỐ LIỆU: <exp-id>]`. **Cấm điền số minh hoạ, số ước lượng, hay số "dự kiến".**

---

## 3. Bản đồ tài sản — cái gì đã có, cái gì phải làm

### 3.1. Mã nguồn đã có (đã kiểm chứng trực tiếp)

| Thành phần | Vị trí | Vai trò |
|---|---|---|
| `FedMix` — **có số hạng Taylor bậc nhất** | `fedbr/algorithms.py:832–861`; số hạng là `grad = autograd.grad(loss1, all_x, create_graph=True)[0]` rồi `loss3 = Σ(λ·grad·x̄_g)/n` | Nhánh có Taylor của E1 |
| `NaiveMix` — **cùng cơ chế, KHÔNG Taylor** | `fedbr/algorithms.py:809–830` | Nhánh đối chứng của E1 |
| `get_augmentation_fedmix_data` — mẫu trung bình $V_i$ + nhãn mềm | `fedbr/scripts/train_fed.py:62–74`; **M=10 hardcode** | Cơ chế "nén bảo mật" của đề cương |
| `fedmix_lambda` với lưới `{0.01, 0.1, 0.2}` | `fedbr/hparams_registry.py:85–86` | Trục $\lambda$ của E2 |
| `RotatedCIFAR10` — label + feature skew | `fedbr/datasets.py:417` | Ô D |
| `CleanCIFAR10` — label skew thuần | `fedbr/datasets.py:470` | Ô C |
| Baseline `FedAvg`(ERM), `FedProx_algo` | `fedbr/algorithms.py:370, 560` | Đúng hai baseline đề cương nêu tên |
| Hạ tầng uv / Makefile / cache / resume / summarize / probe | `Makefile`, `REPRODUCE.md` | Đã hoàn tất |

### 3.2. Việc lập trình cần làm — TRƯỚC khi chạy bất cứ gì

| # | Việc | Vị trí | Lý do |
|---|---|---|---|
| **P-1** | **Sửa lưu checkpoint theo vòng** | `train_fed.py:564–565` — hiện `--save_model_every_checkpoint` ghi đè **cùng một** `model.pkl` | Không có checkpoint best-accuracy ⇒ E5 (cơ chế) và mọi phân tích hậu nghiệm **không chạy được**. Nếu không sửa trước E0.2, checkpoint mất vĩnh viễn |
| **P-2** | **Sửa confound test-set của ma trận 2×2** | `CleanCIFAR10.__init__` (`datasets.py:477–479`) hiện cho **10 môi trường test giống hệt nhau**; `RotatedCIFAR10` cho 10 góc | Cột trái/phải ma trận đo trên **hai phân phối test khác nhau** ⇒ trục không trực giao, không so sánh được. Sửa: dùng cùng bộ 10 góc ở mọi ô, báo cáo tách biệt 0° (in-distribution) và trung bình 10 góc (OOD) |
| **P-3** | Thêm cờ `--fedmix_M` | `get_augmentation_fedmix_data(..., M=10)` | Trục $M$ của E2 — độ nén/bảo mật |
| **P-4** | Thêm target `run-naivemix` | `Makefile` (theo mẫu `run-fedmix:243–245`) | Nhánh đối chứng E1 |
| **P-5** | Thêm cờ `--rot_alpha` | `datasets.py:438` | Trục độ nặng feature skew (E3) |
| **P-6** | Dataset class **ô B** (feature skew thuần) | `datasets.py` — thay `get_noniid_class_and_labels` bằng phân hoạch đồng đều, giữ `rotate_dataset` | Ô B là ô quan trọng nhất của E1/E3 |
| **P-7** | Tách `partition_seed` khỏi `train_seed` | `train_fed.py` | Phân hoạch góc là **nguồn phương sai trội** (số góc trội phân biệt: mean 6.52, sd 1.00) |
| **P-8** | Log chẩn đoán: per-class head $\ell_2$ norm, per-class recall, confusion | `train_fed.py` / `summarize.py` | E5 |
| ~~**P-9**~~ | ~~Nhánh hồi quy: target liên tục + MSE/MAE~~ — **`[GÁC]` từ 22/09** | `datasets.py`, `algorithms.py` | Không lập trình cho tới khi nhánh hồi quy được mở lại |

### 3.3. Tài sản từ paper hội nghị

> ⚠️ **Sửa 24/09 (§1.5).** Các tài sản dưới đây nay là **kết quả của luận văn**, trình bày ở Ch.5 mục 5.2, không phải số trích. Cột "Dùng ở" nhắc tới Ch.3 là lỗi thời: Ch.3 chỉ còn lý thuyết. Số liệu đã kiểm lại với tệp thô ngày 24/09; đường dẫn ở `INDEX_ma-nguon-va-ket-qua.md` §3.

| Tài sản | Dùng ở | Caveat bắt buộc (IR#1) |
|---|---|---|
| FedMix vs FedAvg, K=2 shard: −1.86±0.79 pp | Ch.3, Ch.5 §5.4 (đối chứng) | 3 seed; per-seed −2.19/−0.95/−2.43; cận trên 95% một phía −0.52 pp — **phép tính của luận văn**, không có trong Bài 1 (xem IR#2) |
| C1: −1.90±1.23 · C1+C2 (Dir 0.3): −1.64±1.20 | Ch.3 | **exploratory (†)**; không loại trừ được gain ≥0 |
| T2 ≈ $10^{-4}$ (0.013%) của bậc nhất | Ch.3, Ch.4 (đóng nhánh bậc hai) | **"at initialization"**; nguồn không tuyên bố nó nhỏ suốt huấn luyện |
| Trần LDA +6.45±1.29; CCVR +4.41±1.19; Newton-CE +2.98±1.04 (1 bước) / +6.14±1.37 (hội tụ) | Ch.3 | Cột **CIFAR-10, 3 seed**. "6 cặp" chỉ thuộc phát biểu về *shortfall*, không phải ba con số này |
| CCVR: $M_c{=}100$ → **+0.29 pp ở β=0.1 nhưng −0.76 pp ở β=0.3**; $M_c{=}2000$ → +0.97 (β=0.1), +4.36±0.51 (β=0.05) | Ch.3, Ch.4 (mẫu hình "gain là đường đặc tuyến") | **Bắt buộc nêu vế −0.76 pp** — gain đảo dấu khi ngân sách thiếu |
| Cơ chế: norm head max/min 1.10–1.17 ⇒ thiên lệch **định hướng**; worst-class recall +44/+45/+26 | Ch.3, Ch.5 §5.7 | Lớp worst chọn hậu nghiệm **theo từng seed**; mean 19→57%; kèm sụt nhẹ ở lớp được ưu ái |
| Giới hạn tự khai: *"one architecture family (BN-free VGG)"*, *"one heterogeneity type (label skew)"*, *"BN-free backbone is load-bearing"* | Ch.1 §1.1, Ch.6 | **Đây là danh sách việc của luận văn** |

---

## 4. Dàn bài chi tiết

> **Ký hiệu trạng thái:** `[VIẾT]` viết được ngay · `[CHẠY]` chờ số liệu thực nghiệm · `[QUYẾT]` cần quyết định của học viên/CBHD · `[TRA]` cần tìm kiếm văn liệu

### CHƯƠNG 1 — GIỚI THIỆU · ~~6–7 trang~~ → **3–3,5 trang** *(sửa 21/09 — xem §7.6)*

> ⚠️ **Mục này mô tả bản 16/09, đã bị thay.** Bản hiện hành của Ch.1 nằm dưới mốc `# PHIÊN BẢN CHỈNH SỬA — 21/09/2026` trong `01_chuong1.md`, ngắn hơn đáng kể và **không** chia tiểu mục ba cấp. Giữ mục này để tra cứu ý định ban đầu; khi hai bên mâu thuẫn, **bản Word là bản đúng**, rồi mới tới file chương.
>
> ⚠️ **Sửa 22/09 — §1.2.1 còn ĐÚNG BỐN mục tiêu cụ thể.** Mục tiêu thứ năm (mở rộng sang hồi quy) đã được **gác lại** theo quyết định của học viên. Ba ràng buộc kéo theo, bắt buộc với mọi agent sau:
>
> 1. **Không chương nào được nhắc tới hồi quy** khi nhánh này còn `[GÁC]`. Rà lại §1.2.3 Phạm vi (bản 21/09 còn câu *"Phần hồi quy chỉ có kết quả lý thuyết, không có bằng chứng thực nghiệm"*) và §1.4 Cấu trúc (còn cụm *"kết quả lý thuyết về mở rộng sang tác vụ hồi quy"* trong đoạn giới thiệu Chương 4). Cả hai phải bỏ.
> 2. **Trục thứ tư của §1.2.2 Đối tượng mất hết mức.** Bản 21/09 tháo cơ chế thành bốn thành phần thay đổi độc lập, thành phần thứ tư là *"tác vụ cùng hàm mất mát đi kèm"*. Bỏ hồi quy thì trục đó chỉ còn một mức, tức không còn là một trục. ✅ **Đã chốt 22/09: rút về BA thành phần** — bỏ hẳn vế tác vụ. Ba sửa đổi cụ thể trên cùng một đoạn, ghi ở khối `# QUYẾT ĐỊNH — 22/09/2026` cuối `01_chuong1.md`. Từ nay **không mô tả cơ chế là có bốn trục** ở bất kỳ chương nào.
> 3. Cùng lý do, §4 Ch.4 mục 4.1 (bốn khả năng của framework) và §5.9 (*"Trả lời RQ1–RQ5"*) đã được sửa theo; xem dấu `[GÁC]` tại chỗ.

**1.1. Lý do chọn đề tài** *(2–2.5 tr)* `[VIẾT]`
- Bối cảnh FL: học phân tán, quyền riêng tư, ràng buộc băng thông
- Vấn đề non-IID: client drift, suy giảm hội tụ, phân rã mô hình tổng hợp
- Vì sao **tăng cường dữ liệu** là hướng hấp dẫn: không cần dữ liệu công khai, chi phí truyền thông thấp hơn chia sẻ dữ liệu thô
- Vì sao **khai triển Taylor**: cho phép xấp xỉ mục tiêu global Mixup mà chỉ cần **mẫu trung bình** — cơ chế nén bảo mật
- **Khoảng trống:** các công bố báo cáo gain lớn nhưng (a) khó so sánh giữa các stack, (b) siêu tham số ngân sách hiếm khi được ablate, (c) hầu như chỉ đo dưới **label skew**
- **Nêu tường minh** (theo §1.4): luận văn là nghiên cứu **xác định biên giới hiệu lực**; Mục tiêu tổng quát đã đăng ký là nghiên cứu lý thuyết, nên kết quả âm có kiểm soát cũng là kết quả

**1.2. Mục tiêu, đối tượng và phạm vi** *(1.5 tr)* `[VIẾT]`
- 1.2.1. Mục tiêu tổng quát — trích nguyên văn đề cương đã duyệt
- 1.2.2. Mục tiêu cụ thể — RQ1–RQ4 (§1.2) *(RQ5 gác từ 22/09)*
- 1.2.3. Đối tượng: cơ chế mean-augmentation + xấp xỉ Taylor bậc nhất trong FL giám sát
- 1.2.4. Phạm vi và **giới hạn tự khai** — nêu ngay từ đầu, không giấu xuống Ch.6:
  - CIFAR-10/CIFAR-100, ảnh 32×32; không có dữ liệu FL thực tế
  - Feature skew tổng hợp bằng **phép xoay** — tác động nhóm khả nghịch, thuần hình học, độc lập nhãn; là **cực dễ** của phổ feature skew
  - Mô phỏng, không triển khai thiết bị thật
  - **Không có tuyên bố differential privacy hình thức**; giao thức chỉ là "class-distribution-oblivious"
  - So sánh **chỉ within-stack** (IR#4)

**1.3. Đóng góp của luận văn** *(1–1.5 tr)* `[VIẾT]`
- C1, C2, C3 (§1.3) — mỗi đóng góp một đoạn, kèm **phạm vi hạn định** (IR#3)

**1.4. Cấu trúc luận văn** *(0.5 tr)* `[VIẾT]`

---

### CHƯƠNG 2 — CÁC NGHIÊN CỨU VÀ HƯỚNG TIẾP CẬN LIÊN QUAN · **9–10 trang**

> **Chương chịu rủi ro cao nhất.** Bản đề xuất trước bị bác vì tuyên bố mới lạ không có tìm kiếm văn liệu. Chương này tồn tại để việc đó không lặp lại.

> ⚠️ **Cấu trúc hiện hành — cập nhật 22/09 (lần 2).** Ch.2 có **bốn mục 2.1–2.4**:
>
> | Mục | Nội dung | Trạng thái |
> |---|---|---|
> | 2.1 | Học liên kết và thách thức dữ liệu không đồng nhất — ba tiểu mục: khái niệm · ba dạng không đồng nhất · quy ước Dirichlet | đã có trong Word |
> | 2.2 | Tăng cường dữ liệu và chia sẻ thống kê trong FL — hai hướng, đánh số bốn cấp | đã có trong Word |
> | **2.3** | **Bảng đối chiếu các họ phương pháp** | **đưa trở lại 22/09 — chưa có trong Word** |
> | 2.4 | Khoảng trống luận văn — **bốn** tiểu mục: cô lập số hạng Taylor · phạm vi đánh giá theo loại lệch · **tính tái lập của các kết quả đã công bố** *(viết mới, chốt 22/09)* · định vị luận văn | ba tiểu mục đã có trong Word, **đang mang số 2.3, phải dịch lên 2.4** |
>
> Lịch sử đánh số, để tra cứu: 16/09 có sáu mục; 21/09 gộp `2.2`+`2.3` làm một và dịch `2.4→2.3`, `2.5→2.4`, `2.6→2.5`; 22/09 lần 1 bỏ bảng đối chiếu và mục tính tái lập, còn `2.1–2.3`; 22/09 lần 2 đưa bảng đối chiếu trở lại thành `2.3`, Khoảng trống thành `2.4`.
>
> **Khi tài liệu này và bản Word mâu thuẫn, bản Word là bản đúng** — trừ mục 2.3 dưới đây, là việc còn phải làm trong Word.

**2.1. Học liên kết và thách thức dữ liệu không đồng nhất** *(1.5 tr)* `[VIẾT]`
- FedAvg; phân loại các dạng non-IID theo **NIID-Bench (Li et al., ICDE 2022)**: label distribution skew / **feature distribution skew** / quantity skew
- **Bắt buộc trích NIID-Bench** — đây là tài liệu tham khảo [3] của chính paper hội nghị, và là phản chứng cho mọi tuyên bố "chưa ai tách hai loại skew"
- 2.1.2 bổ sung ngoài dàn bài gốc: hai quy ước tham số hoá Dirichlet và hệ quả đối với tính tái lập

**2.2. Tăng cường dữ liệu và chia sẻ thống kê trong FL** *(4–4.5 tr)* `[TRA]` — **trọng tâm chương**

Chia theo **hai hướng**, phân biệt bởi câu hỏi "ngoài tham số mô hình có truyền thêm thông tin về dữ liệu không". Đánh số **bốn cấp** — ⚠️ cần đối chiếu quy định trình bày của khoa trước khi nộp.

- **2.2.1. Hướng không chia sẻ thông tin và giới hạn của nó** — trần của hướng này là lý do hướng kia hình thành, nên phải đứng trước
  - 2.2.1.1. Ràng buộc trên bộ tham số — FedProx (proximal); **một trong hai baseline của luận văn**
  - 2.2.1.2. Hiệu chỉnh hướng gradient — SCAFFOLD (variance reduction)
  - 2.2.1.3. Ràng buộc trên biểu diễn — MOON. **Đây là nơi định nghĩa phép tách mạng thành bộ trích xuất đặc trưng + tầng phân lớp** (lần xuất hiện đầu); 2.2.2.4 chỉ nhắc lại
  - 2.2.1.4. Giới hạn chung — cải thiện hội tụ nhưng không chạm tới thiên lệch ở classifier head
- **2.2.2. Hướng tiếp cận có chia sẻ dữ liệu** — dẫn nhập: Zhao et al. (chia sẻ dữ liệu thô), tổ tiên chung của cả năm nhánh
  - 2.2.2.1. **Mean-augmented FL**: Mixup; FedMix (Yoon et al., ICLR 2021) — global Mixup xấp xỉ bằng khai triển Taylor bậc nhất trên mẫu trung bình; **NaiveMix**
  - 2.2.2.2. **Dữ liệu ảo**: VHL (Tang et al., 2022) — **ép đặc trưng cục bộ gần đặc trưng dữ liệu ảo CÙNG LỚP**; cần nhãn và ~2000 mẫu ảo
  - 2.2.2.3. **Chưng cất tri thức**: FedDF, FedNTD, FedGen — dùng logits/softmax của mô hình toàn cục trên proxy data không nhãn
  - 2.2.2.4. **Hiệu chuẩn head từ thống kê lớp**: CCVR (μ_c và **Σ_c**); trần Gauss để Ch.3 §3.5 xử lý
  - 2.2.2.5. **Căn chỉnh đặc trưng có điều kiện lớp**: FedProto và dòng prototype. ⚠️ *Sửa 22/09: **Deep CORAL** và **FedDecorr** đã được gỡ khỏi mục này trong bản Word và gỡ khỏi danh mục phủ tối thiểu của IR#3. Không đưa lại trừ khi có quyết định mới — nếu đưa lại thì phải sửa cả IR#3 lẫn bảng 2.3.*
  - 2.2.2.6. **FedBR** (Guo et al., ICML 2023) — hai thành phần; Component 2 ghép cặp **theo từng mẫu** (IR#6)

**2.3. Bảng đối chiếu các họ phương pháp** *(1 tr)* `[VIẾT]` — **đưa trở lại 22/09**

> **Quy tắc nội dung, chốt 22/09: bảng chỉ chứa phương pháp đã được trình bày trong thân bài Ch.2.** Không thêm công trình mới chỉ để lấp bảng — đây là bản tóm tắt của chương, không phải một khảo sát riêng. Thân bài thêm hay bớt phương pháp thì bảng đổi theo; và ngược lại, muốn một phương pháp có mặt trong bảng thì phải viết nó vào thân bài trước.
>
> **Mixup không vào bảng.** Nó là kỹ thuật tăng cường dữ liệu trong học tập trung, không phải phương pháp học liên kết; trong thân bài nó chỉ đóng vai dẫn vào global Mixup.

Sáu cột — gộp hai cột "bậc truyền"/"bậc khai thác" làm một theo quyết định 21/09, và bỏ cột "đặc trưng thật hay tổng hợp" vì nội dung đó đã nằm trong cột thông tin chia sẻ:

| Cột | Nghĩa | Nguồn điền |
|---|---|---|
| Phương pháp | tên + số trích dẫn | thân bài |
| Thông tin chia sẻ thêm | ngoài tham số mô hình; đồng thời là trục riêng tư | thân bài |
| Cần nhãn? | có / không / nhãn mềm | thân bài |
| Bậc thống kê | không · bậc nhất (trung bình) · bậc hai (hiệp phương sai) | thân bài |
| Chi phí truyền thông thêm | so với FedAvg | thân bài; `[TRA]` nếu chương chưa nói |
| Chế độ lệch đã đo | chế độ mà **công trình gốc thực sự đo** | `[TRA]` — **cột chịu lực** |

**Bản nháp các hàng** — dựng từ chính thân bài Ch.2 trong Word, cột cuối chưa điền:

| Phương pháp | Thông tin chia sẻ thêm | Cần nhãn? | Bậc thống kê | Chi phí truyền thông thêm | Chế độ lệch đã đo |
|---|---|---|---|---|---|
| FedProx | không | – | – | không | `[TRA]` |
| SCAFFOLD | biến kiểm soát (ước lượng độ lệch gradient) | không | – | **gấp đôi** | `[TRA]` |
| MOON | không | – | – | không | `[TRA]` |
| Zhao và cộng sự | tập dữ liệu thô nhỏ, cân bằng lớp | có, nhãn cứng | dữ liệu thô | một lần, theo cỡ tập | `[TRA]` |
| NaiveMix | ảnh trung bình của $M$ ảnh cục bộ + nhãn mềm; trộn thẳng vào đầu vào | nhãn mềm | bậc nhất | theo số mẫu đại diện | `[TRA]` |
| FedMix | cùng thông tin như NaiveMix; vào mục tiêu qua tích vô hướng với $\nabla_x\mathcal{L}$ | nhãn mềm | bậc nhất | như NaiveMix | `[TRA]` |
| VHL | tập dữ liệu ảo sinh từ nhiễu (~2.000 mẫu cho CIFAR-10, ~20.000 cho CIFAR-100) | có — phải gán nhãn cho tập ảo | không lấy từ dữ liệu thật | một lần | `[TRA]` |
| FedDF | logits của mô hình toàn cục trên tập proxy | không cần nhãn cho proxy | – | tập proxy đặt ở máy chủ | `[TRA]` |
| FedNTD | phần phân phối trên các lớp không phải nhãn đúng | dùng nhãn cục bộ sẵn có | – | không | `[TRA]` |
| FedGen | bộ sinh nhẹ học tại máy chủ | `[TRA]` | – | truyền tham số bộ sinh | `[TRA]` |
| CCVR | $\mu_c$ và $\Sigma_c$ của đặc trưng theo từng lớp | có, thống kê theo lớp | **bậc hai** | một lần, $C\times(d+d^2)$ | `[TRA]` |
| FedProto | prototype — trung bình đặc trưng theo lớp | có | bậc nhất | $C$ vector $d$ chiều mỗi vòng | `[TRA]` |
| FedBR | tập pseudo-data dùng chung (Random Sample Mean hoặc Mixture) | nhãn mềm ở nhánh Mixture | bậc nhất | theo cỡ pseudo-data | `[TRA]` |

Ràng buộc khi hoàn thiện:

- **Cột cuối phải điền từ chính công trình gốc, không suy đoán.** Ô nào chưa tra thì để `[TRA]`, không đoán theo trực giác (IR#8). Đây là cột chở toàn bộ lập luận về khoảng trống: nếu phần lớn các hàng chỉ đo lệch phân phối nhãn thì bảng tự nói ra cái khoảng trống mà mục 2.4 phát biểu, và mục 2.4 không còn phải tự khẳng định.
- **Số trích dẫn trong bảng phải khớp danh mục tài liệu tham khảo đã sửa ngày 22/09**, không dùng lại số của bản cũ.
- Caption đặt **trên** bảng, tự đủ nghĩa, giải thích mọi ký hiệu (§7.4). Bản nháp: *"**Bảng 2.2.** Đối chiếu các phương pháp khắc phục dữ liệu không đồng nhất được trình bày trong chương này, theo lượng thông tin trao đổi thêm ngoài tham số mô hình. $M$ là số ảnh cục bộ được gộp trong một mẫu trung bình đại diện; $C$ là số lớp; $d$ là số chiều vector đặc trưng; $\mu_c$ và $\Sigma_c$ là vector trung bình và ma trận hiệp phương sai của đặc trưng thuộc lớp $c$. Cột cuối ghi chế độ lệch phân phối mà công trình gốc thực sự đo, không phải chế độ mà phương pháp có thể áp dụng."*
- Bảng 6 cột × 13 hàng: nếu tràn khổ dọc thì **xoay ngang trang** hoặc hạ cỡ chữ trong bảng, **không cắt bớt hàng** cho vừa trang.
- Sau bảng, **một đoạn 3–5 câu đọc bảng**, chỉ ra vị trí của FedMix/NaiveMix so với các họ còn lại. Không thuật lại từng hàng — hàng đã tự nói.

> **Mục "Tính tái lập trong FL" vẫn ở trạng thái đã bỏ** (quyết định 22/09 lần 1). Ba quy tắc báo cáo trong đó — so sánh theo cặp · đường đặc tuyến vận hành · chỉ so sánh trong cùng nền tảng — phải phát biểu ở **Ch.4, mục giao thức đo lường**; ví dụ CCVR đảo dấu theo ngân sách chuyển về **Ch.3**.
>
> ✅ **Đã chốt 22/09: phương án (a) — trả lại phần nền văn liệu.** Đóng góp thứ ba của luận văn là *kiểm toán tính tái lập*; sau khi bỏ mục này thì Ch.2 không còn dòng nào đặt nền cho nó. Nay trả lại **một tiểu mục ngắn khoảng nửa trang** đặt trong mục 2.4, thành tiểu mục thứ ba trong bốn; bản nháp nội dung và các ràng buộc ở khối `# QUYẾT ĐỊNH — 22/09/2026` cuối `02_chuong2.md`.
>
> ⚠️ **Chỉ trả lại phần nền văn liệu.** Ba quy tắc báo cáo — so sánh theo cặp · đường đặc tuyến vận hành · chỉ so sánh trong cùng nền tảng — **vẫn thuộc Ch.4**, và ví dụ CCVR đảo dấu theo ngân sách **vẫn thuộc Ch.3**. Không kéo chúng ngược về Ch.2.
>
> Mặc định **không thêm mục nào vào danh mục tài liệu tham khảo**: đoạn này dựng được từ NIID-Bench và phần Dirichlet mà chính chương đã trình bày.

**2.4. Khoảng trống luận văn** *(1–1.5 tr)* — đã viết trong Word, **đang mang số 2.3, phải dịch lên 2.4**

- **Bốn** tiểu mục sau khi chốt 22/09: cô lập số hạng khai triển Taylor · phạm vi đánh giá theo loại lệch phân phối · **tính tái lập của các kết quả đã công bố** *(viết mới)* · định vị luận văn
- ⚠️ Tiểu mục định vị luận văn đang mở bằng *"Ba đóng góp sau tương ứng với **hai** khoảng trống vừa trình bày"* → đổi thành **"ba khoảng trống"**. Sau sửa đổi này ba khoảng trống ứng một-một với ba đóng góp
- Tuyên bố khoảng trống dạng **hạn định**, và hạn định nằm **trong chính câu** (IR#3 bản sửa 22/09). Mẫu đang dùng trong Word và nên giữ: *"Cấu hình như vậy không xuất hiện trong bài báo FedMix, kể cả ở phần phụ lục."*
- ⚠️ **Nhật ký khảo sát không vào thân bài.** Bản 16/09 của mục này yêu cầu ghi nguồn tra cứu, truy vấn và mốc thời gian ngay trong chương; yêu cầu đó **đã bị IR#3 bản sửa 22/09 huỷ**. Nhật ký để ở `NOTE_khao-sat-van-lieu.md` và phụ lục.
- ⚠️ **Còn một phủ định không hạn định trong Word**: *"Chưa có cách quy đổi độ nghiêm trọng của hai loại lệch về cùng một thang."* Phải thêm hạn định.
- **CẤM** "chưa ai làm" (IR#3)

---

### CHƯƠNG 3 — CƠ SỞ LÝ THUYẾT · **9–10 trang**

> ⚠️ **Ranh giới Ch.2 ↔ Ch.3 — chốt 22/09, đọc trước khi viết một dòng nào của chương này.**
>
> Bản Word của Ch.2 **đã** làm hai việc mà dàn bài giao cho Ch.3: mục 2.1.1 trình bày bài toán FedAvg kèm phương trình (2.1), local steps và nguồn gốc client drift; mục 2.1.3 trình bày phân hoạch Dirichlet khá kỹ, gồm cả hai quy ước tham số hoá và hệ quả đối với tính tái lập. Viết Ch.3 mà không chốt trước sẽ rơi vào một trong hai kết cục: **viết lại** những gì Ch.2 đã nói, vi phạm §7.6 *"mỗi ý viết một lần, ở đúng một chương"*; hoặc **né** phần đó, khiến Ch.3 mất phần mở đầu và người đọc nhảy thẳng vào dẫn xuất Taylor mà không có ký hiệu nền.
>
> **Ranh giới: Ch.2 giữ phần khái niệm, Ch.3 giữ phần hình thức.**
>
> | | Ch.2 giữ | Ch.3 giữ |
> |---|---|---|
> | FedAvg | FL là gì, vì sao chỉ trao đổi tham số, vì sao nhiều bước cục bộ sinh ra drift. Phương trình (2.1) ở lại như một câu giới thiệu | Ký hiệu đầy đủ, local SGD viết ra từng bước, bản phát biểu **chính thức** mà Ch.4–Ch.6 tham chiếu |
> | Dirichlet | Dirichlet dùng để làm gì, $\alpha$ điều khiển cái gì, hai quy ước lệch nhau mười lần và hệ quả tái lập | Định nghĩa chính quy phân phối Dirichlet; $\text{Dir}(\alpha\cdot p)$ với $\alpha$ thực dùng trong luận văn; nồng độ thực theo IR#7 |
> | Lệch đặc trưng | định vị phép xoay trong phân loại của NIID-Bench, một câu | Mô hình hoá $q_i$, số góc hiệu dụng, phân rã hai trục |
>
> Hai ràng buộc kèm theo: **(a)** Ch.3 phát biểu lại đầy đủ chứ không viết *"như đã trình bày ở Chương 2"* — §7.5 cấm đẩy lập luận ra tham chiếu, và Ch.3 là chương mà người đọc quay lại tra ký hiệu; **(b)** Ch.2 **không** được bổ sung thêm chi tiết hình thức khi sửa, kể cả khi thấy thiếu — chỗ thiếu đó thuộc Ch.3.

**3.1. Bài toán FL và local SGD** *(1 tr)* `[VIẾT]`
- $f^*=\min_\omega \sum_i p_i f_i(\omega)$; vòng truyền thông; local steps; nguồn gốc client drift
- **Phát biểu đầy đủ**, không rút gọn vì Ch.2 đã nhắc — xem ranh giới ở đầu chương

**3.2. Mô hình hoá dữ liệu không đồng nhất** *(1.5 tr)* `[VIẾT]`
- Label skew: LDA $\text{Dir}(\alpha\cdot p)$, $\alpha=0.1$
- Feature skew: phân phối góc xoay mỗi client, $q_i\sim\text{Dir}$; **nồng độ thực 0.1/thành phần ⇒ ≈2.08 góc hiệu dụng** (IR#7)
- **Phân rã hai trục** → ma trận 2×2 (§5.1 E3)

**3.3. Global Mixup và xấp xỉ Taylor bậc nhất** *(2.5–3 tr)* `[VIẾT]` — **trọng tâm chương**
- 3.3.1. Mixup và global Mixup lý tưởng (cần dữ liệu thô của client khác → vi phạm FL)
- 3.3.2. Mẫu trung bình đại diện: $\bar{x}_g=\frac1M\sum x_m$, $\bar{y}_g=\frac1M\sum y_m$; $M$ là **tham số nén**
- 3.3.3. **Khai triển Taylor**: $\mathcal{L}((1{-}\lambda)x+\lambda\bar{x}_g,\,\cdot)\approx(1{-}\lambda)\mathcal{L}(x,y)+\lambda\mathcal{L}(x,\bar{y}_g)+\lambda\,\nabla_x\mathcal{L}\cdot\bar{x}_g$
  → **ánh xạ từng số hạng sang mã**: `loss1`, `loss2`, `loss3` tại `algorithms.py:849–853`
- 3.3.4. **`NaiveMix` là gì**: trộn đầu vào trực tiếp, **không** có `loss3` ⇒ hiệu `FedMix − NaiveMix` **cô lập đúng số hạng Taylor**
- 3.3.5. Số hạng bậc hai: vì sao đóng nhánh — T2 ≈ $10^{-4}$ của bậc nhất **tại khởi tạo** (IR#1)

**3.4. Thiên lệch học cục bộ: đặc trưng và bộ phân lớp** *(2 tr)* `[VIẾT]`
- Ba hiện tượng của FedBR (biased local classifier, biased local feature)
- **Kết quả cơ chế từ công trình hội nghị**: thiên lệch head là **định hướng** (norm max/min 1.10–1.17), hiệu chuẩn **xoay** ranh giới quyết định, gain tập trung ở lớp thiểu số
- **Liên kết then chốt với đề cương:** mục tiêu đã đăng ký là *"tăng cường đặc trưng tại các vùng ranh giới quyết định để giảm sai lệch nhãn"* — kết quả trên **xác nhận chẩn đoán** đó. Câu hỏi còn lại là đòn bẩy nào xoay được ranh giới.

**3.5. Sinh so với phân biệt: trần LDA** *(1.5 tr)* `[VIẾT]`
- Efron (1975), Ng–Jordan (2001) — **phát biểu đúng phạm vi**: ngang bằng **tiệm cận**, kém hơn **trong kỳ vọng** ở ngân sách mẫu hữu hạn, **dưới giả thiết Gaussian đúng và hiệp phương sai chung**
- Khi $\Sigma_c$ khác nhau ⇒ biên Bayes là **bậc hai (QDA)**, kết quả Efron không áp dụng
- Trần đo ở $n/d\approx3.9$ — **ghi rõ chế độ**, không ngoại suy
- Vai trò trong luận văn: giải thích vì sao các phương pháp dựa trên thống kê Gaussian tổng hợp có trần, và vì sao đối tượng của luận văn (mean-augmentation, dùng **đầu vào thật**) nằm ngoài trần đó

> ⚠️ **Sửa 24/09 (§1.5): mục 3.6 BỎ.** Nội dung chuyển sang Ch.5 mục 5.2. Mục 3.4.2 chỉ còn hai giả thuyết (độ lớn hay hướng), không chứa số đo. Ghi chú dưới đây giữ để tra lịch sử.

**3.6. Kết quả nền từ công trình đã công bố của tác giả** *(1–1.5 tr)* `[VIẾT]` — **IR#9 áp dụng**
- Mở đầu bằng khai báo tái sử dụng + trích dẫn đầy đủ (tên hội nghị, năm, DOI/trạng thái)
- Tóm lược có caveat: kết quả âm FedMix dưới label skew; các mở rộng **exploratory**; cơ chế định hướng; confound ngân sách của CCVR (**kèm vế −0.76 pp**)
- **Kết luận chương**: nửa label skew đã có; nửa feature skew, việc cô lập số hạng Taylor, và stack thứ hai là phần luận văn này bổ sung

---

### CHƯƠNG 4 — ĐỀ XUẤT · **10–11 trang**

> Chương này điền ô **"Mô hình đề xuất"** của biểu mẫu. Sản phẩm đã đăng ký trong "Kết quả dự kiến" là **framework**, không phải một thuật toán mới — và đó là thứ được giao ở đây.

**4.1. Tổng quan framework** *(2 tr)* `[VIẾT]`
- Sơ đồ khối (giữ cấu trúc sơ đồ trong đề cương: Server Orchestrator ↔ Client Local Training)
- Bốn khả năng: (a) hoán đổi cơ chế tăng cường (`FedMix`/`NaiveMix`/không); (b) tham số hoá ngân sách $(\lambda, M)$; (c) hoán đổi chế độ lệch phân phối (4 ô + trục $\alpha_{\text{rot}}$); (d) hoán đổi tác vụ và hàm mất mát — **`[GÁC]` 22/09: chỉ còn phân loại, xem ràng buộc 2 ở khối Ch.1**
- **Ánh xạ sang "Kết quả dự kiến" đã đăng ký**: *"framework ... hỗ trợ đa dạng các loại tác vụ và các loại hàm mất mát khác nhau"*

**4.2. Cô lập số hạng khai triển Taylor** *(2 tr)* `[VIẾT]`
- Phát biểu hình thức: $\Delta_{\text{Taylor}} = \text{Acc}(\text{FedMix}) - \text{Acc}(\text{NaiveMix})$, paired trên cùng phân hoạch
- Vì sao hiệu này **chính là** số hạng `loss3` và không gì khác (đối chiếu hai hàm `update`)
- Ba giả thuyết đối chứng cần loại trừ: chênh lệch thang gradient, tương tác với $\lambda$, hiệu ứng $M$

**4.3. Ma trận chế độ lệch phân phối** *(2 tr)* `[VIẾT]` + `[CHẠY]` phần P-6
- Bảng 2×2: A (IID) · B (feature skew thuần) · C (label skew thuần) · D (cả hai)
- **P-2 bắt buộc**: mọi ô đánh giá trên **cùng** bộ môi trường test; báo cáo tách biệt 0° và trung bình 10 góc
- Trục liên tục $\alpha_{\text{rot}}$; **ghi rõ mặc định ≈0.1 và quét LÊN phía nhẹ hơn** (IR#7)

**4.4. Mặt vận hành $(\lambda, M)$** *(2 tr)* `[VIẾT]`
- $\lambda$: trọng số trộn — lưới đã đăng ký `{0.01, 0.1, 0.2}`, mở rộng thêm điểm
- $M$: số ảnh gộp mỗi mẫu đại diện — **đồng thời là tham số nén/bảo mật** của đề cương
- Ba đại lượng báo cáo cùng nhau: **độ chính xác** × **chi phí truyền thông** (byte/vòng của $V_i$) × **độ nén** ($M$)
- Đây là "Output: báo cáo phân tích về sự cân bằng giữa hiệu suất và chi phí tài nguyên" đã đăng ký

**4.5. Giao thức đo lường** *(1.5 tr)* `[VIẾT]` — **IR#5**
- Paired before/after trên cùng checkpoint, cùng lần rút phân hoạch
- Kỷ luật within-stack
- **Khai báo trước**: $\Delta^*$, họ giả thuyết chính, hiệu chỉnh Holm, TOST cho nhánh null
- Tách `partition_seed` / `train_seed`; báo cáo thống kê cấu hình góc như hiệp biến

**4.6. Mở rộng sang hồi quy** *(1.5 tr)* — **`[GÁC]` từ 22/09, giữ nguyên nội dung để mở lại**

> Không viết mục này vào luận văn chừng nào nhánh hồi quy còn gác. Toàn bộ ghi chú bên dưới giữ nguyên trạng.
- **Lập luận cơ chế:** lời giải thích cho mọi kết quả âm là *thiên lệch ở classifier head dưới label skew*. Hồi quy **không có** classifier head và **không có** label skew theo nghĩa phạm trù ⇒ cơ chế đó **không áp dụng được**. Đây là phép kiểm tra tính tổng quát của lời giải thích, không phải một ứng dụng phụ.
- **Thiết kế đề xuất (cần kiểm tra khả thi):** hồi quy **góc xoay liên tục** trên chính pipeline RotatedCIFAR10 — cùng ảnh, cùng client, cùng phân hoạch; chỉ đổi đích từ nhãn lớp sang góc (liên tục). Phân phối góc mỗi client vốn đã lệch theo $q_i$ ⇒ có sẵn tương tự "target skew" mà không cần benchmark mới.
- Khớp mục tiêu đã đăng ký: *"mở rộng không gian mẫu theo hướng song phương để nắm bắt sự biến thiên liên tục của giá trị dự báo"*
- Metric: MAE/MSE (đúng đề cương); hàm mất mát: MSE/Huber
- **Phạm vi giới hạn**: một tác vụ, một chế độ skew, ngân sách nhỏ. Không tuyên bố tổng quát cho mọi bài hồi quy.
- ⚠️ **Cần kiểm tra khả thi trước khi cam kết** (§6, mốc T2)

---

### CHƯƠNG 5 — KẾT QUẢ THỰC NGHIỆM · **15–16 trang**

> ⚠️ **Sửa 24/09 (§1.5): thêm mục 5.2 "Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower"** (khoảng 3 trang, **đã viết**, số liệu đã kiểm với tệp thô), gồm năm tiểu mục: 5.2.1 Thiết lập · 5.2.2 FedMix so với FedAvg (cùng C1, C1+C2 thăm dò và số hạng bậc hai) · 5.2.3 Hiệu chuẩn tầng phân lớp và ngân sách mẫu ảo · 5.2.4 Dạng thiên lệch của tầng phân lớp · 5.2.5 Những gì chuyển sang các mục sau. **Các mục dưới đây dịch số thêm một** (5.2 → 5.3, …, 5.9 → 5.10). Bảng 5.1–5.5 thuộc mục 5.2 mới. Chi tiết ở cuối `05_chuong5.md`.

**5.1. Thiết lập thực nghiệm** *(2 tr)* `[VIẾT]`
- Bảng cấu hình: dataset, phân hoạch, số client, local steps, optimizer, lr, batch, backbone (**ghi $d$**), số vòng
- **Bảng đăng ký thí nghiệm** (§5.1 của tài liệu này) — mỗi exp-id một hàng
- Phần cứng, chi phí, công cụ; đường dẫn `results.jsonl`
- **Giao thức `ROUNDS=300`**: kèm **hiện vật bằng chứng** bảo toàn thứ hạng 300↔1000 trích từ E0.2, và cảnh báo rằng bảo toàn thứ hạng không đảm bảo ổn định của paired Δ dưới 1 pp

**5.2. Tái hiện và kiểm toán tính tái lập** *(2.5 tr)* `[CHẠY: E0.2]`
- Bảng tái hiện cột CIFAR-10 của FedBR Table 1
- **Danh mục sai lệch code↔paper** (đóng góp C3):
  - Lỗi `if not angle` làm hỏng môi trường test 0° — **đo delta bằng re-evaluation, không cần huấn luyện lại**
  - Projection MLP 1024/512 thay vì 256/128
  - `--save_model_every_checkpoint` **ghi đè cùng một file** — tên cờ gây hiểu nhầm
  - `M=10` hardcode trong `get_augmentation_fedmix_data`
  - Mơ hồ "Dir(1.0)" ↔ nồng độ thực 0.1/thành phần
  - Dirichlet concentration không dương (đã vá)
  - Các lỗi chặn import (`cv2`, `parso`, `fedbr/src/__init__.py`)

**5.3. RQ1 — Số hạng Taylor bậc nhất có mang tín hiệu không?** *(3 tr)* `[CHẠY: E1]`
- Bảng chính: $\Delta_{\text{Taylor}}$ = FedMix − NaiveMix, paired, 4 ô, $n$ seed, CI 95%
- Bảng phụ: FedMix − FedAvg, NaiveMix − FedAvg
- Kiểm định theo họ giả thuyết chính đã khai báo; TOST nếu null
- Đường cong hội tụ

**5.4. RQ2 — Kết luận label skew có chuyển sang feature skew không?** *(3 tr)* `[CHẠY: E3]`
- Ma trận 2×2, cùng bộ test env (P-2)
- Đường đặc tuyến theo $\alpha_{\text{rot}}$ + **kiểm định xu hướng** (hồi quy hệ số góc của Δ theo $\log\alpha_{\text{rot}}$, seed là hiệu ứng ngẫu nhiên) — mạnh hơn t-test rời rạc từng ô
- **Đối chiếu với kết quả stack Flower ở Ch.3 — chỉ ở mức cơ chế, không so số tuyệt đối** (IR#4)

**5.5. RQ3 — Mặt vận hành $(\lambda, M)$** *(2.5 tr)* `[CHẠY: E2]`
- Heatmap/đường cong gain theo $\lambda$ và theo $M$
- Bảng ba chiều: accuracy × chi phí truyền thông × $M$
- **Đối chiếu mẫu hình với confound $M_c$ của CCVR** (gain đảo dấu khi ngân sách thiếu — có tái lập ở đây không?)

**5.6. Kiểm soát ngoại vi** *(1.5 tr)* `[CHẠY: E4]`
- Backbone: `vgg11` ($d$=512) · `resnet18_gn` · `resnet20_gn` ($d$=64) · `cct` ($d$=256)
- **Ưu tiên cao**: paper hội nghị cảnh báo *"a normalized backbone may reshape both the directional-bias and Gaussian-ceiling findings"* ⇒ nếu backbone chuẩn hoá lật cơ chế, **Ch.3 và Ch.5 sụp cùng lúc**. Chạy sớm (§6 mốc T1)
- CIFAR-100 (số lớp cao)

**5.7. RQ4 — Phân tích cơ chế** *(2 tr)* `[CHẠY: E5]`
- Per-class head $\ell_2$ norm; worst-class recall; confusion matrix
- **Câu hỏi trung tâm**: đòn bẩy mean-augmentation có **xoay** ranh giới quyết định không, hay chỉ co giãn?
- Lặp lại chẩn đoán Section VII của công trình hội nghị trên stack 2 — **claim là cơ chế lặp lại được, không phải con số** (IR#4)

**5.8. RQ5 — Nhánh hồi quy** *(1.5 tr)* — **`[GÁC]` từ 22/09**
- MAE/MSE, đường cong hội tụ, so FedAvg
- Diễn giải: lời giải thích "thiên lệch ở head" có còn hiệu lực ở tác vụ không có head không?

**5.9. Tổng hợp và thảo luận** *(1.5 tr)* `[CHẠY]`
- Trả lời RQ1–RQ4, mỗi câu một đoạn, **kèm điều kiện hiệu lực** *(RQ5 gác từ 22/09)*
- **Threats to validity** — bắt buộc, theo mẫu của công trình hội nghị

---

### CHƯƠNG 6 — KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN · **4–5 trang**

**6.1. Kết luận** *(1.5 tr)* `[CHẠY]` — đối chiếu từng mục tiêu cụ thể đã đăng ký với kết quả đạt được

**6.2. Đóng góp** *(1 tr)* `[VIẾT]` — C1, C2, C3 với phạm vi hạn định

**6.3. Hạn chế** *(1 tr)* `[VIẾT]` — feature skew tổng hợp bằng phép xoay (cực dễ của phổ); một họ dataset; mô phỏng; công suất thống kê; không có DP hình thức

**6.4. Hướng phát triển** *(1–1.5 tr)* `[VIẾT]`
- Benchmark domain shift thật (PACS, WILDSCamelyon — **đã có trong repo**)
- Feature skew **phụ thuộc lớp** (phép xoay hiện là nhiễu class-shared, một $q_i$ dùng chung cho 10 lớp)
- Phân tích $(\varepsilon,\delta)$ hình thức cho giao thức chia sẻ mẫu trung bình
- Head huấn luyện trên **đặc trưng thật có nhãn, xuyên client** so với trần LDA — khoảng trống Ng–Jordan mà công trình hội nghị chỉ đích danh

---

## 5. Kế hoạch thực nghiệm

### 5.1. Đăng ký thí nghiệm

| ID | Nội dung | Cấu hình | Phụ thuộc | Mục dùng |
|---|---|---|---|---|
| **E0.1** | Hạ tầng | P-1…P-8 | — | — |
| **E0.2** | Tái hiện Table 1 CIFAR-10 + hiện vật 300↔1000 | 1000 vòng | E0.1 | §5.2, §5.1 |
| **E1** | **Cô lập Taylor** | {FedAvg, NaiveMix, FedMix} × 4 ô × $n$ seed @300 | E0.1 | §5.3 |
| **E2** | Mặt $(\lambda, M)$ | $\lambda\in\{0.01,0.05,0.1,0.2\}$ × $M\in\{1,5,10,20,50\}$, ô B+D | E1 | §5.5 |
| **E3** | Ma trận skew + $\alpha_{\text{rot}}$ | $\alpha_{\text{rot}}\in\{0.1,0.5,1,5,\infty\}$ | E1 | §5.4 |
| **E4** | Kiểm soát ngoại vi | 4 backbone + CIFAR-100 | E0.1 | §5.6 |
| **E5** | Cơ chế | hậu nghiệm trên checkpoint E1 | E1, P-1 | §5.7 |
| ~~**E6**~~ | ~~Hồi quy~~ — **`[GÁC]` 22/09** | góc liên tục, ô B+D | P-9 | §5.8 |
| **E7** | Headline | 1000 vòng, ô B+C | E1 | §5.3, §5.4 |

### 5.2. Công suất thống kê — **bắt buộc chốt trước khi chạy E1**

Với $s\approx1.2$ pp (từ Table III công trình hội nghị):

| $n$ seed | Ngưỡng ý nghĩa | MDE @80% |
|---|---|---|
| 3 | 2.98 pp | **3.92 pp** |
| 5 | 1.49 pp | 2.09 pp |
| 8 | 1.00 pp | 1.39 pp |

**Khuyến nghị: $\Delta^* = 2.0$ pp, $n = 8$ seed cho họ giả thuyết chính.** Khả thi vì `FedMix`/`NaiveMix` kế thừa `ERM` ⇒ chạy ở **giá FedAvg** (~5.5h/1000 vòng, ~1.8h/300 vòng), rẻ hơn FedBR (~9.5h).

**Họ giả thuyết chính (hiệu chỉnh Holm, $m=4$):**
- H1: $\Delta_{\text{Taylor}}$ ở ô B (feature skew thuần)
- H2: $\Delta_{\text{Taylor}}$ ở ô C (label skew thuần)
- H3: FedMix − FedAvg ở ô B
- H4: FedMix − FedAvg ở ô C

Mọi so sánh khác (ô A, ô D, quét $\lambda$/$M$, backbone, CIFAR-100) gắn nhãn **thăm dò** tường minh.
**Nhánh null:** TOST, biên tương đương định trước (đề xuất ±1.5 pp ở $n{=}8$; **nếu không đạt phải nói thẳng trong luận văn**).

### 5.3. Ngân sách

⚠️ **Không tin bảng này.** Chạy `make probe` trên đúng card vừa thuê trước mỗi giai đoạn và nhân với giá thuê. Bảng dưới dùng đơn giá từ `REPRODUCE.md` §6 (FedAvg-like ≈5.5h @1000 vòng ⇒ ≈1.8h @300 vòng).

| ID | Số run × giờ/run | GPU-ngày | Điều kiện tiên quyết |
|---|---|---|---|
| E0.2 | 9 × 5.5–9.5 | ~2.6 | P-1 **phải xong trước** |
| E1 chính | 2 ô × 3 pp × 8 seed × 1.8h | ~3.6 | P-2, P-4, P-6 |
| E1 ngữ cảnh | 2 ô × 3 pp × 3 seed × 1.8h | ~1.3 | nt |
| E2 | ~40 run × 1.8h | ~3.0 | P-3 |
| E3 | ~40 run × 1.8h | ~3.0 | P-5, P-6 |
| E4 | ~16 run × 1.8–3h | ~1.6 | — |
| E5 | hậu nghiệm | ~0.2 | P-1, P-8 |
| ~~E6~~ *(gác)* | ~20 run × 1.8h | — | P-9 |
| E7 | ~18 run × 5.5h | ~4.1 | E1 |
| **Tổng** | | **~21** | |

Biên an toàn: **biên phải đặt trên LỊCH, không trên GPU-ngày.** Ở mọi giai đoạn, thời gian tính toán chiếm dưới 15% thời gian lịch — GPU không phải ràng buộc. Tài nguyên khan là **tháng**.

---

## 6. Mốc kiểm soát rủi ro

| Mốc | Thời điểm | Kiểm tra | Nếu thất bại |
|---|---|---|---|
| **T0** | Trước mọi run | P-1 và P-2 đã xong? | **Dừng.** Chạy trước khi sửa = mất checkpoint vĩnh viễn và ma trận 2×2 không dùng được |
| **T1** | Sau E4 (backbone) | Backbone chuẩn hoá có lật kết quả cơ chế của Ch.3 không? | Nếu có: Ch.3 phải phát biểu lại phạm vi; Ch.5 §5.7 đổi khung. **Chạy sớm — đây là rủi ro đơn lẻ lớn nhất** |
| ~~**T2**~~ *(gác cùng E6)* | Trước khi cam kết E6 | Hồi quy góc liên tục có hội tụ ở cấu hình FL này không? (1 run ngắn) | Đổi sang benchmark hồi quy dạng bảng, hoặc thu E6 về phần thuần lý thuyết ở §4.6 |
| **T3** | Sau E1 | $\Delta_{\text{Taylor}}$ có nằm trong biên TOST không? | Không sao — cả hai nhánh đều là kết quả. Nhưng **phải** đủ công suất để phân biệt, xem §5.2 |

---

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

## 8. Thứ tự viết đề xuất cho agent

| Bước | Chương/mục | Trạng thái | Ghi chú |
|---|---|---|---|
| 1 | Ch.2 toàn bộ | `[TRA]` | Làm **trước tiên** — rủi ro cao nhất, và bảng §2.4 định vị toàn bộ luận văn |
| 2 | Ch.3 §3.1–3.3 | `[VIẾT]` | Không phụ thuộc kết quả |
| 3 | Ch.3 §3.4–3.6 | `[VIẾT]` | IR#1, IR#9 |
| 4 | Ch.4 toàn bộ | `[VIẾT]` | §4.6 chờ mốc T2 |
| 5 | Ch.1 | `[VIẾT]` | Viết **sau** Ch.2–4 để đóng góp phát biểu đúng tầm |
| 6 | Ch.5 §5.1–5.2 | `[CHẠY: E0.2]` | |
| 7 | Ch.5 §5.3–5.8 | `[CHẠY]` | Theo thứ tự exp-id |
| 8 | Ch.5 §5.9, Ch.6 | `[CHẠY]` | |
| 9 | Tóm tắt VI/EN, mục lục, danh mục hình/bảng/từ viết tắt | `[VIẾT]` | |

**Quy ước file** — hai lớp tách biệt, **không dùng tiền tố số cho tài liệu hỗ trợ**:

| File | Vai trò |
|---|---|
| `00_outline.md` | tài liệu này — chỉ mục và giao ước |
| `01_chuong1.md` … `06_chuong6.md` | **các chương luận văn** (slot số dành riêng) |
| `NOTE_khao-sat-van-lieu.md` | kết quả Phase A — nền cho Ch.2 và §5.2 |
| `NOTE_bien-ban-binh-duyet.md` | biên bản bình duyệt 5 ghế |
| `PLAN_ke-hoach-8-tuan.md` | **kế hoạch thực thi hiện hành** — thay §5, §6 của tài liệu này |
| `ARCHIVE_*` | đã huỷ, chỉ để tra cứu lịch sử. **Không thực hiện theo.** |
| `refs.bib` | `[CẦN TẠO]` |

Mỗi file chương mở đầu bằng khối trạng thái ghi mục nào đã xong, mục nào chờ exp-id nào.

**Quy ước lịch sử sửa đổi trong file chương — *(chốt 22/09)*.** File chương **chỉ được append, không ghi đè**; học viên muốn lưu vết mọi thay đổi.

- Yêu cầu sửa gom thành một khối đặt ở **cuối file**, tiêu đề `# YÊU CẦU SỬA — <ngày>`, mô tả việc cần làm chứ không viết thay.
- Agent thực hiện sửa vào **bản Word** (bản chính), rồi chép phần đã sửa xuống **dưới** khối yêu cầu, dưới một mốc `# PHIÊN BẢN CHỈNH SỬA — <ngày>` mới.
- Mọi phiên bản cũ và mọi khối yêu cầu cũ **giữ nguyên tại chỗ**, không xoá, không gộp.
- Khi cần biết đâu là bản hiện hành: **mốc `PHIÊN BẢN CHỈNH SỬA` cuối cùng trong file**, và trên tất cả là bản Word.

---

## 9. Việc hành chính — song song, không chặn viết

| # | Việc | Nguồn |
|---|---|---|
| A1 | Nêu tên hội nghị, năm, trạng thái, DOI/chỉ mục; đính kèm thư chấp nhận | IR#9 |
| A2 | Văn bản xác nhận đồng tác giả (CBHD) về đồng ý sử dụng + phân định đóng góp | IR#9 |
| A3 | Đối chiếu điều khoản tái sử dụng của nhà xuất bản | IR#9 |
| A4 | Khai báo tỉ lệ trùng lắp dự kiến ở Ch.3 **trước** khi quét | IR#9 |
| A5 | Xác nhận mốc bắt đầu 12 tháng đã đăng ký và thời hạn theo quyết định giao đề tài | Biên bản M17 |
| A6 | Báo cáo CBHD rằng đề tài **không đổi tên**, chỉ là kế hoạch thực hiện cụ thể hoá | §1.1 |

---

## 10. Nhật ký trạng thái

| Ngày | Sự kiện |
|---|---|
| 2026-09-15 | Bình duyệt 5 ghế bản đề xuất đổi hướng → Major Revision, 4 CRITICAL. Biên bản: `Bien-ban-binh-duyet-va-lo-trinh-sua.md` |
| 2026-09-16 | Chốt hướng: **giữ nguyên đề cương**, thực hiện qua cặp `FedMix`/`NaiveMix` trên stack FedBR. Nhánh hồi quy: **phương án B** (lý thuyết + một thí nghiệm giới hạn). Outline này được tạo |
| 2026-09-21 | **Ch.1 viết lại toàn bộ** — `01_chuong1.md`. Bản nháp 16/09 **giữ nguyên tại chỗ**, bản hiện hành append phía dưới mốc `# PHIÊN BẢN CHỈNH SỬA — 21/09/2026`. §1.1 dùng nguyên văn tác giả + một đoạn ba câu; §1.2 chia ba tiểu mục Mục tiêu/Đối tượng/Phạm vi, bỏ bảng RQ; §1.3 bỏ tiêu đề C1/C2/C3; §1.4 thêm câu dẫn. Chốt hai quy ước viết mới — xem §7.5 và §7.6 |
| 2026-09-21 | **Ch.2 chỉnh lối viết** — `02_chuong2.md`, áp lối văn xuôi của Ch.1 theo §7.5 (bỏ khối in đậm mở câu và phần lớn gạch đầu dòng; định nghĩa thuật ngữ tại chỗ; không rút gọn mà viết giải thích rộng hơn). Ba thay đổi có ràng buộc tiếp diễn: (a) **bỏ toàn bộ tham chiếu chéo dạng `§2.x` trong thân bài** — người đọc không tra được ký hiệu mục; chỉ giữ tham chiếu cấp chương; (b) **bảng đối chiếu §2.4 rút từ 22 xuống 11 hàng**, một đại diện mỗi họ + 2 baseline + nền tảng thực nghiệm, và gộp hai cột "bậc truyền/bậc khai thác" làm một; (c) **danh mục tham khảo rút từ 44 xuống 19 mục và đánh số lại** — giữ đúng mười công trình IR#3 bắt buộc phủ (NIID-Bench, MOON, VHL, FedDF, FedNTD, FedGen, CCVR, FedProto, Deep CORAL, FedDecorr), tám mục không bỏ được (FedAvg, FedProx, SCAFFOLD, Mixup, Zhao, Hsu–Qi–Brown, FedMix, FedBR) và công trình của tác giả theo IR#9; **ngân sách trích dẫn còn lại dành cho Ch.3–Ch.6**. Công thức: bỏ `\boldsymbol` (bộ render in nguyên chuỗi lệnh), đưa về tập lệnh LaTeX lõi.<br>⚠️ Kéo theo cho Ch.3: trần LDA / giả thiết Gauss nay **không còn được dẫn ở Ch.2** — Ch.2 chỉ nêu giả thiết ấy tồn tại và chuyển sang Ch.3. Ch.3 §3.5 phải tự mang Efron, Ng–Jordan và các trích dẫn của mình |
| 2026-09-22 | **Ch.2 gộp mục và chuẩn hoá bảng.** (a) Gộp `2.2 Tối ưu hoá nhận biết không đồng nhất` + `2.3 Tăng cường dữ liệu…` thành **một mục `2.2`**, bên trong chia hai hướng `2.2.1` (không chia sẻ thông tin — nêu trần) và `2.2.2` (có chia sẻ dữ liệu), các phương pháp nằm ở **cấp thứ tư** `2.2.1.x` / `2.2.2.x`. ⚠️ Đánh số bốn cấp — **cần đối chiếu quy định trình bày của khoa**; cách hạ về ba cấp ghi ở khối trạng thái `02_chuong2.md`. Chương còn **2.1–2.5**; các mục sau dịch số. §4 của tài liệu này đã cập nhật theo. (b) **Mọi bảng/hình bắt buộc có số và tên** — quy ước mới ở §7.4, áp cho toàn luận văn; thân bài gọi bằng số bảng, đây là **ngoại lệ có chủ ý** so với quy tắc cấm tham chiếu `§`. Ch.2 hiện có Bảng 2.1 và Bảng 2.2. (c) Văn phong: cấm trích nguyên văn tiếng Anh trong thân bài, cấm giọng phòng thủ, cấm ẩn dụ trong ngoặc kép thay cho định nghĩa — chi tiết ở khối trạng thái `02_chuong2.md` |
| 2026-09-22 | **Bản Word trở thành bản chính.** Học viên cung cấp hiện trạng Ch.2 trong Word; từ nay `.md` chỉ là bản nháp soạn thảo, **khi lệch thì Word đúng**. Ch.2 trong Word: 2.1 có ba tiểu mục (khái niệm · ba dạng không đồng nhất · quy ước Dirichlet), 2.2 hai hướng với đánh số bốn cấp — **xác nhận mẫu của khoa cho phép bốn cấp**. Đã **bỏ khỏi chương** bảng đối chiếu các họ phương pháp và mục tính tái lập; `2.3 Khoảng trống luận văn` đã viết mới. **Việc kéo theo chưa làm:** (a) ba quy tắc báo cáo (paired · đường đặc tuyến · within-stack) phải chuyển vào **Ch.4 §4.5**; (b) ví dụ CCVR đảo dấu theo ngân sách chuyển vào **Ch.3 §3.6** kèm caveat IR#1; (c) **IR#3 bị vi phạm** — Deep CORAL và FedDecorr đã bị lược khỏi Ch.2 nhưng vẫn nằm trong danh mục phủ tối thiểu, phải đưa lại hoặc sửa IR#3; (d) danh mục tài liệu tham khảo trong Word có lỗi trùng số và khuyết số, chi tiết ở cuối `02_chuong2.md` |
| 2026-09-22 *(lần 3)* | **Rà lối viết Ch.1–Ch.2 + bốn quyết định.** (a) **Nhánh hồi quy gác lại** theo quyết định của học viên: §1.2.1 còn **bốn** mục tiêu cụ thể; RQ5 / E6 / P-9 / Ch.4 §4.6 / Ch.5 §5.8 chuyển trạng thái `[GÁC]`, nội dung giữ nguyên tại chỗ để mở lại khi cần. Hai việc kéo theo **chưa làm**, ghi ở khối Ch.1 trong §4: bỏ hai câu còn nhắc hồi quy ở §1.2.3 và §1.4; và quyết trục thứ tư của §1.2.2 — nay chỉ còn một mức — giữ bốn hay rút về ba. (b) **Học viên đã sửa danh mục trích dẫn**; việc kéo theo (d) của nhật ký phía trên coi như đóng. (c) **Thêm §7.7 — chống giọng văn máy**: mười hạn ngạch lối viết kèm ba lệnh `rg` tự kiểm. Phát sinh từ một lượt rà riêng cho lối viết: văn sạch nhưng đều nhịp — khuôn tương phản dùng hơn mười lần trong hai chương, gần như đoạn nào cũng kết bằng câu chốt, giọng phòng thủ còn ba câu ở Ch.1. (d) **Đưa bảng đối chiếu trở lại** thành mục `2.3`, Khoảng trống dịch lên `2.4`; bảng **chỉ chứa phương pháp đã có trong thân bài Word**, bản nháp 13 hàng đã dựng sẵn ở §4. Kéo theo: **IR#3 đã được sửa** — gỡ Deep CORAL và FedDecorr khỏi danh mục phủ tối thiểu, đóng mục xung đột treo từ lần 2. **Còn treo:** đóng góp thứ ba (kiểm toán tái lập) hiện không có nền văn liệu nào ở Ch.2 sau khi mục tính tái lập bị bỏ — cần quyết trả lại hay không. (e) **Chốt một từ cho bên tham gia** — Ch.1 dùng "thiết bị", từ Ch.2 trở đi dùng "client", bỏ hẳn "bên"; quy ước ở §7.2. (f) **Chốt ranh giới Ch.2 ↔ Ch.3** — Ch.2 giữ phần khái niệm, Ch.3 giữ phần hình thức; bảng phân vai ở đầu khối Ch.3 trong §4, phải đọc trước khi viết dòng nào của Ch.3. (g) **Đơn đặt việc cho Ch.1 và Ch.2 đã được append** vào cuối `01_chuong1.md` và `02_chuong2.md` dưới mốc `# YÊU CẦU SỬA — 22/09/2026`, **không ghi đè nội dung cũ** theo yêu cầu giữ lịch sử của học viên; agent thực hiện sửa vào bản Word rồi chép bản đã sửa xuống dưới khối đó |
| 2026-09-22 *(lần 4)* | **Chốt hai mục `[QUYẾT]` của Ch.1.** (a) **§1.2.2 rút về ba thành phần** — bỏ hẳn vế "tác vụ cùng hàm mất mát" sau khi nhánh hồi quy được gác; từ nay không chương nào mô tả cơ chế là có bốn trục. (b) **§1.2.1 được đánh số 1–4**, ngoại lệ có chủ ý so với §7.6 và là ngoại lệ **duy nhất** của Ch.1; đã ghi vào §7.6 kèm lệnh cấm agent sau gỡ số về lại văn xuôi. Chi tiết thi hành ở khối `# QUYẾT ĐỊNH — 22/09/2026` cuối `01_chuong1.md`. Lưu ý thi hành: sửa §1.2.2 **một lượt** cùng với việc chuyển câu kết đoạn khỏi khuôn tương phản (AI#1), vì hai việc nằm trên cùng một đoạn |
| 2026-09-22 *(lần 5)* | **Chốt C8 của Ch.2 — trả lại phần nền văn liệu về tính tái lập.** Mục Khoảng trống nay có **bốn** tiểu mục, tiểu mục thứ ba viết mới, khoảng nửa trang; bản nháp ở khối `# QUYẾT ĐỊNH — 22/09/2026` cuối `02_chuong2.md`. Ba ràng buộc: **chỉ** trả lại phần nền văn liệu — ba quy tắc báo cáo vẫn ở Ch.4, ví dụ CCVR vẫn ở Ch.3; **không thêm mục nào vào danh mục tài liệu tham khảo**, đoạn này dựng từ NIID-Bench và phần Dirichlet đã có trong chương; tiểu mục định vị luận văn đổi *"hai khoảng trống"* → *"ba khoảng trống"*. Kết quả: ba khoảng trống ứng một-một với ba đóng góp, đoạn định vị chặt hơn bản cũ. **Sau lần này, Ch.1 và Ch.2 không còn mục `[QUYẾT]` nào treo** |
| 2026-09-22 (lượt 3) | **Ch.2 — thi hành khối `# YÊU CẦU SỬA` và `# QUYẾT ĐỊNH`.** Bản sửa nối vào cuối `02_chuong2.md` dưới mốc `# PHIÊN BẢN CHỈNH SỬA — 22/09/2026 (lượt 2)`; phần cũ giữ nguyên theo quy ước chỉ-append. Đã làm: A1–A5 (danh mục đánh số lại liên tục 1–16, chèn MOON ở [7], CCVR dịch sang [15], FedProx thêm MLSys 2020) · B1 Bảng 2.2 13 hàng 6 cột · B2 dịch `2.3 Khoảng trống` → `2.4` · B3 đoạn bắc cầu sang Ch.3 · B4 giữ ranh giới khái niệm/hình thức · C1–C7 · C8 theo phương án (a), thêm tiểu mục `2.4.3 Tính tái lập của các kết quả đã công bố`, mục định vị đổi "hai khoảng trống" → "ba" · D1 chốt từ "client" · E1–E4. ✅ **Cột *Chế độ lệch đã đo* đã tra xong cùng ngày** từ bản toàn văn 13 công trình: **12/13 chỉ đo lệch nhãn**, chỉ FedBR có lệch đặc trưng tách biệt (RotatedMNIST, CIFAR-10 xoay, PACS). Bảng truy vết ở mục 6 *Ghi chú thi hành* trong `02_chuong2.md`. ⚠️ **Việc tra sửa một lỗi phát biểu:** FedMix **có** chạy FEMNIST, mà Bảng 2.1 xếp phân hoạch theo người viết vào nhóm lệch đặc trưng, nên câu *"chưa có công trình nào chạy nó dưới lệch phân phối đặc trưng"* là sai; phát biểu đã thu về *"lệch đặc trưng được tách riêng khỏi lệch nhãn"*. **Mọi chương sau dùng lại phát biểu khoảng trống phải theo bản đã thu này.** **Hai việc còn treo:** (b) A6–A7 là thao tác trong Word (cập nhật trường F9, bổ sung danh mục viết tắt); (c) **hạn mức AI#1 vượt khi đếm bằng máy** (6 chỗ) vì lệnh `rg` ở §7.7 bắt cả *"thay vì"* nghĩa cơ học — bốn trong sáu chỗ là câu mộc của học viên hoặc nguyên văn bản nháp caption trong tài liệu này, AI#10 cấm làm mượt; cần quyết định nới lệnh đếm hay chấp nhận vượt |
| 2026-09-24 | **Ch.4 — rà soát và viết lại.** Thêm đường dẫn bản Word vào §0. Nối vào cuối `04_chuong4.md` khối `# YÊU CẦU SỬA — 24/09/2026` và `# PHIÊN BẢN CHỈNH SỬA — 24/09/2026`; bản 16/09 giữ nguyên. Chương còn **năm mục 4.1–4.5** khớp tiêu đề Word, nhánh hồi quy đã bỏ khỏi bản hiện hành. Bốn lỗi thiết kế đã sửa: (a) đẳng thức cộng tính ở 4.2.1 sai dấu và thực ra là đồng nhất thức, $\Delta_{\text{gốc}} = \Delta_{\text{Taylor}} - \Delta_{\text{trộn}}$, nên không có "phần dư" để kiểm tra; (b) ⚠️ **`loss3` trong `fedbr/algorithms.py:850` chia thêm cho kích thước lô**, nên số hạng Taylor nhỏ hơn công thức 32 lần ở lô 32 (đã kiểm bằng số: tỉ lệ 8,000 ở B=8, 32,000 ở B=32). Phải sửa mã **trước E1/E2**, và câu *"mã và lý thuyết khớp nhau"* ở Word Ch.3 mục 3.3.4 sai một nửa; (c) trục Drop cần mốc IID theo từng họ lệch (P0 cho lệch nhãn, P0r với $\alpha_{\text{rot}}\to\infty$ cho lệch đặc trưng); (d) mã dựng lại tập mẫu trung bình ở mỗi bước từ dữ liệu thô, nên khung chuyển sang tập $V$ cố định. Nhận xét mới: trong $\mathcal{L}_{\text{C}}$, $\bar x_g$ không xuất hiện, nên C là mốc không dùng thông tin ảnh, còn A và B là hai đường đưa cùng thông tin ảnh vào. **Bảy mục `[QUYẾT]` còn treo** (Q1–Q7 ở *Ghi chú thi hành* cuối `04_chuong4.md`), quan trọng nhất là Q1: Word Ch.3 thiếu mục 3.3.5, 3.3.6, 3.6, nên lưới bốn cấu hình tạm đặt ở Ch.4. Ghi chú thi hành còn liệt kê lỗi phát hiện trong Word Ch.1–Ch.3 và việc kéo theo cho `05_chuong5.md` |
| 2026-09-24 *(lượt 2)* | **Tạo `INDEX_ma-nguon-va-ket-qua.md`** — chỉ mục mã nguồn và kết quả cho kho Flower của Bài 1, kho FedBR, `FedBR/output` và mã DevPranjal; thêm hai dòng vào §0. Bốn phát hiện kéo theo việc sửa, **chưa sửa ở đâu cả**, chờ học viên: (a) ⚠️ **cả ba bản cài đặt FedMix** (FedBR `algorithms.py:850`, Flower `augmentation.py:344`, DevPranjal `client.py:197`) đều chia số hạng Taylor thêm một lần cho kích thước lô, nên kết quả −1,86 pp của Bài 1 cũng đo với số hạng đã thu nhỏ ($B=10$). Câu *"kết quả về chính cơ chế"* ở Ch.3 mục 3.6 cần hạn định. Ch.4 mục 4.2.3 bản 24/09 đang mô tả lỗi này như của riêng FedBR, cần sửa cách nói (ghi ở cuối `04_chuong4.md`); (b) **cận trên −0,53 ở IR#2 và §3.3 không có trong Bài 1**, tính lại ra **−0,52**; $s\approx1{,}2$ và $n/d\approx3{,}9$ cũng không có nguyên văn trong bài — xem chỉ mục F2; (c) số hạng bậc hai ≈10⁻⁴ chỉ đúng tại khởi tạo, trên backbone đã huấn luyện là 9,6·10⁻² (chỉ mục F4); (d) "$M$" khác nghĩa giữa hai stack: Flower lấy trung bình toàn bộ dữ liệu client, FedBR lấy 10 ảnh (chỉ mục F5, §6) |
| 2026-09-24 *(lượt 3)* | **Quyết định của học viên: bài hội nghị là công bố của luận văn, không phải nguồn trích** (§1.5 mới). Luận văn viết như thể chưa có bài; kết quả Flower là kết quả của luận văn. Đã sửa: IR#1, IR#9, §3.3, ghi chú mục 3.6 và Ch.5 ở §4. Đã nối khối `YÊU CẦU SỬA — 24/09/2026` vào **cả năm file chương**, mỗi khối có **bảng trước/sau** để sửa Word bằng Ctrl+F; cột "Trước" của 19 hàng Ch.1–Ch.3 đã đối chiếu nguyên văn với Word ngày 24/09 (mỗi chuỗi xuất hiện đúng một lần). Nội dung: Ch.1 sáu hàng, kèm đoạn Lời cam đoan và mục Danh mục công bố; Ch.2 ba hàng; Ch.3 mười một hàng, kèm hai khối văn mới S1 (mục 3.4.2) và S2 (mục 3.5.2); Ch.4 tám hàng (bỏ `[TG]`, nối B′ với mục 5.2); **Ch.5 viết mới mục 5.2** (năm bảng, số liệu kiểm lại từ tệp thô) kèm bảng đổi tiêu đề trong Word. **Còn chờ học viên:** hàng 3 của Ch.1 và hàng 3 của Ch.2 (viết lại đóng góp thứ ba, `[QUYẾT]`); Q1–Q7 của Ch.4 |
| | *(agent tiếp theo cập nhật vào đây)* |