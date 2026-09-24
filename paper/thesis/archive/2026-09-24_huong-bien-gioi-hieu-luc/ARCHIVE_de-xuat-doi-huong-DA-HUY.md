> # ⛔ TÀI LIỆU ĐÃ HUỶ — KHÔNG THỰC HIỆN THEO
>
> **Ngày huỷ:** 16/09/2026
>
> Tài liệu này đề xuất **đổi hướng luận văn** và một phương pháp mới tên CCFA. Cả hai đều **đã bị bác bỏ**:
>
> - Một vòng bình duyệt 5 ghế tìm ra **4 khiếm khuyết CRITICAL** trong CCFA (xem `NOTE_bien-ban-binh-duyet.md`). Đáng chú ý nhất: $\Sigma_c$ với $d{=}512$ từ 32 pseudo-data **không ước lượng được**; tuyên bố khoảng trống bị phản chứng bởi VHL — baseline của chính FedBR.
> - Khảo sát văn liệu sau đó (`NOTE_khao-sat-van-lieu.md`) xác nhận thêm: FedMix Phụ lục J đã thử biến thể **có điều kiện lớp** và kết luận nó **làm hại** hiệu năng.
>
> **Hướng đã chốt:** GIỮ NGUYÊN đề cương đã duyệt, không đổi tên đề tài. Xem `00_outline.md` và `PLAN_ke-hoach-8-tuan.md`.
>
> Giữ file này chỉ để tra cứu lịch sử quyết định.

---

# Đề xuất điều chỉnh hướng luận văn thạc sĩ *(đã huỷ)*

**Học viên:** Vũ Tuấn Kiệt — MSHV 240201043, Khóa 2024 Đợt 02
**CBHD:** PGS.TS. Nguyễn Tấn Cầm
**Ngày soạn:** 15/09/2026
**Trạng thái:** đề xuất thay thế đề cương *"Nâng cao hiệu suất học liên kết thông qua tăng cường dữ liệu dựa trên khai triển Taylor"*

---

## 0. Tóm tắt điều hành

Đề cương hiện tại đề xuất một framework tăng cường dữ liệu trong FL dựa trên (1) các mẫu trung bình đại diện $V_i$ được chia sẻ toàn cục và (2) khai triển Taylor để xấp xỉ hàm mất mát trên dữ liệu trộn. **Đây chính là cơ chế của FedMix (Yoon et al., ICLR 2021)**, và paper hội nghị đã được chấp nhận của chính học viên — *"When Does Classifier Calibration Reproduce Under Non-IID Federated Learning?"* — đã kiểm chứng cơ chế này một cách có kiểm soát và thu được **kết quả âm nhất quán trên mọi seed và mọi chế độ non-IID đã thử**.

Nói cách khác: nếu tiếp tục đề cương cũ, học viên sẽ phải dành 12 tháng để mở rộng một cơ chế mà chính mình đã công bố bằng chứng cho thấy nó không hoạt động. Đây là rủi ro học thuật nghiêm trọng và không thể biện minh trước hội đồng.

Tài liệu này đề xuất một hướng thay thế **kế thừa trực tiếp** paper hội nghị (thay vì mâu thuẫn với nó), tận dụng toàn bộ hạ tầng tái hiện FedBR đã hoàn thiện trong repo, và giải quyết đúng một câu hỏi mà paper hội nghị đã tự đặt ra ở phần Future Work nhưng chưa trả lời được.

| | Đề cương cũ | Đề xuất mới |
|---|---|---|
| Cơ chế lõi | Mẫu trung bình chia sẻ + Taylor bậc 1/2 | Căn chỉnh đặc trưng có điều kiện lớp trên **đặc trưng thật** |
| Quan hệ với paper hội nghị | **Mâu thuẫn** (đã bị bác bỏ) | **Kế thừa** (trả lời Future Work) |
| Chế độ non-IID mục tiêu | Label skew | **Feature skew** (chưa ai kiểm chứng) |
| Hạ tầng thực nghiệm | Phải xây mới | Repo FedBR đã hoàn thiện |
| Rủi ro "không ra kết quả" | Cao — cơ chế đã chết | Thấp — có phương án dự phòng là một nghiên cứu đo lường hoàn chỉnh |

---

## 1. Tại sao đề cương hiện tại không phát triển được

### 1.1. Cơ chế lõi đã bị bác bỏ bằng thực nghiệm của chính học viên

Đề cương mô tả ba thành phần. Cả ba đều đã được đo trong paper hội nghị:

| Thành phần trong đề cương | Tương ứng trong paper hội nghị | Kết quả đo |
|---|---|---|
| "Tạo mẫu trung bình đại diện $V_i$", chia sẻ toàn cục, huấn luyện trên dữ liệu làm giàu | FedMix ($m=1$), mean-augmented inputs | **−1.86 ± 0.79 pp** so với FedAvg (K=2 shard); âm trên **mọi** seed |
| "Mở rộng vùng lân cận song phương (bilateral)" — ghép cặp mẫu có ý thức về lớp | C1 (class-aware pairing) | **−1.90 ± 1.23 pp**; âm trên mọi seed |
| "Khai triển Taylor bậc cao để xấp xỉ hàm loss" | T2 (input-space second-order Taylor correction) | Biên độ ở mức **$10^{-4}$ (0.013%)** của số hạng bậc nhất — thấp hơn bốn bậc độ lớn |
| Kết hợp cả hai mở rộng, chế độ skew nhẹ hơn | C1+C2, Dirichlet $\beta = 0.3$ | **−1.64 ± 1.20 pp**; âm trên mọi seed |

Kết luận nguyên văn trong paper: *"the mean-augmented (mashed-input) term, **which is the method's defining contribution**, yields no measurable gain on our stack."*

Điều quan trọng về mặt phương pháp luận: đây **không phải** lỗi cài đặt. Paper đã hiệu chuẩn (calibrate) cài đặt FedMix của mình với một reimplementation mở độc lập thứ hai và khớp trong phạm vi ±2 pp, đồng thời dùng giao thức **paired before/after trên cùng một checkpoint và cùng một lần rút phân hoạch** để loại bỏ phương sai giữa các lần chạy. Negative này là có kiểm soát.

### 1.2. Về số hạng Taylor bậc hai — cần phát biểu chính xác

Paper đo biên độ của số hạng bậc hai **tại thời điểm khởi tạo** và ghi rõ giới hạn của phép đo: *"We measure this at initialization and do not claim it stays negligible throughout training."*

Vì vậy phát biểu đúng là: **số hạng Taylor bậc hai không phải là một đòn bẩy hợp lý tại trọng số trộn vận hành $\lambda = 0.05$**, chứ không phải "đã chứng minh nó bằng 0 trong suốt quá trình huấn luyện". Học viên có thể trung thực nói với hội đồng rằng còn một khe hở lý thuyết ở đây — nhưng khe hở đó rộng bốn bậc độ lớn, và việc đặt cược 12 tháng luận văn vào việc thu hẹp nó là một lựa chọn rủi ro rất cao với kỳ vọng lợi ích rất thấp.

### 1.3. Nhánh hồi quy không cứu được đề cương

Phần duy nhất trong đề cương chưa bị kiểm chứng là nhánh bài toán hồi quy. Nhưng:

- Nó **kế thừa cùng một cơ chế** (mẫu trung bình + xấp xỉ Taylor) đã cho kết quả âm ở phân lớp. Không có lý do cơ học nào để kỳ vọng nó hồi sinh ở hồi quy.
- Nó **nhân đôi bề mặt thực nghiệm** (thêm một họ tác vụ, thêm bộ metric MAE/MSE, thêm benchmark) mà không thêm một cơ chế mới nào.
- FL trên hồi quy thiếu benchmark non-IID chuẩn hóa tương đương CIFAR-10 + Dirichlet, nên rất khó so sánh với văn liệu.

Khuyến nghị: **bỏ nhánh hồi quy**, đi sâu vào phân lớp.

### 1.4. Một lợi thế của tình huống này

CBHD — PGS.TS. Nguyễn Tấn Cầm — là **đồng tác giả** của paper hội nghị. Thầy đã nắm các kết quả âm này. Việc chuyển hướng vì thế không phải là học viên "bỏ cuộc" mà là **hệ quả logic trực tiếp từ kết quả nghiên cứu chung đã được bình duyệt và chấp nhận**. Đây là lập luận mạnh nhất cho phần *Giải trình chỉnh sửa*.

---

## 2. Những gì giữ lại được từ đề cương

Không phải bỏ hết. Ba thứ sau đây vẫn còn nguyên giá trị và nên được mang sang:

1. **Bài toán tổng quát**: non-IID làm suy giảm FL, và cần một can thiệp rẻ về truyền thông. Giữ nguyên.
2. **Ràng buộc "không chia sẻ dữ liệu thô"**: hướng mới vẫn tôn trọng ràng buộc này — thậm chí còn chặt hơn, vì phương pháp đề xuất **không tốn thêm một byte truyền thông nào** so với baseline.
3. **Tiêu chí đánh giá kép "hiệu suất ↔ chi phí tài nguyên"**: giữ nguyên, và nay có công cụ đo sẵn (`make probe`, cột `VRAM (GB)` và `step_time` trong `results.jsonl`).

Cần thay: tên đề tài, cơ chế đề xuất, và bộ benchmark.

---

## 3. Hướng đề xuất mới

### 3.1. Tên đề tài đề xuất

- **Tiếng Việt:** GIẢM THIÊN LỆCH HỌC CỤC BỘ TRONG HỌC LIÊN KẾT TRÊN DỮ LIỆU KHÔNG ĐỒNG NHẤT: CĂN CHỈNH ĐẶC TRƯNG CÓ ĐIỀU KIỆN LỚP DƯỚI CÁC CHẾ ĐỘ LỆCH PHÂN PHỐI KHÁC NHAU
- **Tiếng Anh:** REDUCING LOCAL LEARNING BIAS IN FEDERATED LEARNING ON HETEROGENEOUS DATA: CLASS-CONDITIONAL FEATURE ALIGNMENT ACROSS DISTRIBUTION SHIFT REGIMES

### 3.2. Câu hỏi nghiên cứu trung tâm

> Thiên lệch do cập nhật cục bộ trong FL không-IID nằm ở **bộ phân lớp (head)** hay ở **không gian đặc trưng**, và sự phân định đó phụ thuộc thế nào vào **loại** lệch phân phối (label skew so với feature skew)? Một cơ chế căn chỉnh đặc trưng có điều kiện lớp — vốn *trơ* dưới label skew — có phục hồi tín hiệu dưới feature skew hay không?

Đây là một câu hỏi **có thể bác bỏ được** (falsifiable), được phát biểu từ trước, với dự đoán rõ ràng. Đó là dạng câu hỏi mà hội đồng đánh giá cao nhất.

### 3.3. Ba đóng góp dự kiến

**C1 — Khung chẩn đoán 2×2 chế độ lệch phân phối.** Tách bạch label skew và feature skew thành hai trục độc lập, tạo bốn ô thực nghiệm, và đo trên cả bốn ô bằng cùng một giao thức paired. Văn liệu FL hiện trộn lẫn hai loại skew này; chưa có nghiên cứu nào tách chúng một cách có kiểm soát.

**C2 — Phương pháp đề xuất CCFA** (Class-Conditional Feature Alignment): căn chỉnh thống kê bậc hai có điều kiện lớp trên **đặc trưng thật** của pseudo-data, với **chi phí truyền thông bằng không** so với FedBR.

**C3 — Kiểm toán confound trên FedBR.** Áp dụng phương pháp luận "gain là một đường đặc tuyến vận hành, không phải một con số" từ paper hội nghị sang FedBR, và công bố các sai lệch giữa code phát hành và mô tả trong paper mà quá trình tái hiện đã phát hiện.

---

## 4. Cơ sở lý thuyết của phương pháp đề xuất

Chuỗi lập luận dẫn tới CCFA, mỗi mắt xích đều neo vào một kết quả đã có:

1. **Có một trần lý thuyết cho việc tính lại head từ thống kê Gaussian tổng hợp.** Paper hội nghị, Section VI: với các lớp Gaussian chia sẻ hiệp phương sai, một head phân biệt (discriminative) huấn luyện trên mẫu rút từ chính các Gaussian đó không thể vượt bộ phân biệt sinh (LDA), theo Efron (1975) và Ng–Jordan (2001). Đo được trên 6 cặp dataset–seed: LDA +6.45±1.29 pp, CCVR +4.41±1.19, Newton-CE +2.98±1.04.

2. **Trần đó cũng ràng buộc cả không gian đặc trưng.** Paper hội nghị, "fifth negative": một phép biến đổi đặc trưng có điều kiện lớp huấn luyện trên **cùng bộ thống kê Gaussian** hội tụ về đúng nghiệm LDA — headroom chỉ +0.4 pp, và số hạng hiệp phương sai không đóng góp gì đo được.

3. **Lối thoát duy nhất mà lý thuyết cho phép là dùng đặc trưng thật.** Nguyên văn: *"The only escape the theory allows is to use **real** features rather than Gaussian samples."*

4. **Nhưng dưới label skew thì không có gì để căn chỉnh.** Vì với label skew thuần, hiệp phương sai có điều kiện lớp của các client **trùng nhau** — mỗi client thấy cùng một phân phối $p(x \mid y)$, chỉ khác $p(y)$. Tín hiệu bậc hai có điều kiện lớp **vắng mặt theo cấu trúc**. Paper hội nghị kết luận: *"a class-conditional second-order feature alignment is inert under label skew ... but could carry signal under genuine **feature** skew — our next direction."*

5. **FedBR có dùng đặc trưng thật, nhưng căn chỉnh của nó là bất khả tri về lớp.** Đọc `fedbr/algorithms.py:1114`: pseudo-label mặc định là **đồng đều** $q = \mathbf{1}/C$, và hàm mất mát tương phản (Eq. 5–7) dùng cosine similarity trên đặc trưng đã chiếu **không hề điều kiện theo lớp**. FedBR căn chỉnh phân phối đặc trưng **biên**, không phải phân phối **có điều kiện lớp**. Tính "label-agnostic" là điểm bán hàng của FedBR — nhưng cũng chính là thứ khiến nó bỏ lỡ tín hiệu bậc hai.

6. **Khoảng trống**: chưa ai kiểm chứng căn chỉnh **có điều kiện lớp, bậc hai, trên đặc trưng thật, dưới feature skew**. Đó là giao của (3), (4) và (5) — và cũng chính là ô trống trong lý thuyết mà paper hội nghị để lại.

**Vì sao đây là thiết kế luận văn tốt:** dự đoán được phát biểu *trước* khi chạy. Nếu CCFA thắng dưới feature skew và trơ dưới label skew → xác nhận lý thuyết, đóng khe hở, có phương pháp mới. Nếu CCFA trơ ở **cả hai** → bác bỏ lý thuyết của chính paper hội nghị, cũng là một kết quả có giá trị công bố. Cả hai nhánh đều là luận văn.

---

## 5. Phương pháp đề xuất: CCFA

### 5.1. Trực giác

Mỗi client đã có sẵn trong bộ nhớ **hai** bộ trích xuất đặc trưng: bản cục bộ $\phi_i$ đang được huấn luyện, và bản toàn cục đóng băng $\phi_g$ nhận từ server đầu vòng (FedBR đã lưu sẵn: `self.original_feature`, `algorithms.py:1121`). Nó cũng đã có pseudo-data $x_p$ dùng chung toàn hệ thống.

CCFA yêu cầu: **trên cùng pseudo-data, thống kê đặc trưng có điều kiện lớp của $\phi_i$ phải khớp với của $\phi_g$**.

### 5.2. Lấy điều kiện lớp mà không cần nhãn

Vấn đề thiết kế cốt lõi: pseudo-data của FedBR cố tình không có nhãn thật (đó là tính chất bảo mật của nó). Giải pháp: dùng **soft label do chính mô hình toàn cục sinh ra**:

$$\tilde{p}_c(x_p) = \mathrm{softmax}\big(\,\omega_g(\phi_g(x_p))\,\big)_c$$

Mô hình toàn cục là bản tổng hợp của mọi client nên ít thiên lệch hơn bất kỳ mô hình cục bộ nào. Soft label này được tính **hoàn toàn tại client**, từ các tham số client vốn đã nhận — **không có upload, không có chia sẻ phân phối nhãn, không tăng chi phí truyền thông**. Đây là điểm mạnh cần nhấn trong luận văn.

### 5.3. Hàm mất mát

Với trọng số mềm $\tilde{p}_c$, tính trung bình và hiệp phương sai có điều kiện lớp theo kiểu có trọng số, trên cùng lô pseudo-data, cho cả $\phi_i$ và $\phi_g$:

$$\mu_c^{(\cdot)} = \frac{\sum_p \tilde{p}_c(x_p)\, z_p^{(\cdot)}}{\sum_p \tilde{p}_c(x_p)}, \qquad \Sigma_c^{(\cdot)} = \frac{\sum_p \tilde{p}_c(x_p)\,(z_p^{(\cdot)} - \mu_c^{(\cdot)})(\cdot)^\top}{\sum_p \tilde{p}_c(x_p)}$$

$$\mathcal{L}_{\mathrm{CCFA}} = \sum_{c=1}^{C} w_c \Big[ \underbrace{\|\mu_c^{\text{loc}} - \mu_c^{\text{glob}}\|_2^2}_{\text{bậc nhất}} + \eta \underbrace{\|\Sigma_c^{\text{loc}} - \Sigma_c^{\text{glob}}\|_F^2}_{\text{bậc hai — số hạng đang thử nghiệm}} \Big]$$

Cộng vào mục tiêu min-step của FedBR với hệ số $\nu$:

$$\mathcal{L}_{\text{gen}}' = \mathcal{L}_{\text{cls}} + \mu\,\mathcal{L}_{\text{con}} + \lambda\,\mathcal{L}_{\text{aug}} + \nu\,\mathcal{L}_{\mathrm{CCFA}}$$

**Hai biến thể bắt buộc phải tách để ablate:**
- **CCFA-1**: chỉ số hạng bậc nhất ($\eta = 0$) — đây là baseline nội bộ.
- **CCFA-2**: có cả bậc hai ($\eta > 0$) — đây mới là thứ lý thuyết dự đoán chỉ sống dưới feature skew.

Nếu không tách hai biến thể này thì **không thể** kết luận gì về tín hiệu bậc hai, và toàn bộ luận cứ lý thuyết ở Mục 4 sụp đổ. Đây là ablation quan trọng nhất của luận văn.

### 5.4. Lưu ý kỹ thuật cần xử lý

| Vấn đề | Ghi chú |
|---|---|
| $\Sigma_c$ với $d = 512$ từ 32 pseudo-data | Ma trận suy biến nặng. **Bắt buộc** shrinkage (Ledoit–Wolf hoặc shrinkage hằng số như paper hội nghị đã dùng: 0.01), hoặc chiếu xuống chiều thấp trước. Cần báo cáo rõ lựa chọn này — nó là một confound. |
| Chi phí tính toán | $C \times d^2$ phần tử cho hiệp phương sai. Với $C=10$, $d=512$: ~2.6M số mỗi bên mỗi bước. Cần đo `step_time` và báo cáo — luận văn có cam kết về chi phí tài nguyên. |
| Soft label lúc đầu huấn luyện | Mô hình toàn cục ở vòng 0 gần ngẫu nhiên → $\tilde{p}_c \approx 1/C$ → CCFA suy biến về căn chỉnh biên. Cần warm-up (bật CCFA sau $T_0$ vòng) và **báo cáo $T_0$ như một siêu tham số, không giấu**. |
| Tương tác với Component 2 của FedBR | CCFA và contrastive loss có thể chồng chéo. Phải chạy cả cấu hình **CCFA thay thế** Component 2 lẫn **CCFA cộng thêm** vào Component 2. |

---

## 6. Thiết kế thực nghiệm

### 6.1. Thí nghiệm 0 — cổng kiểm tra bắt buộc (làm TRƯỚC khi cài CCFA)

**Trước khi xây phương pháp khai thác một tín hiệu, phải đo xem tín hiệu đó có tồn tại không.** Đây là kỷ luật của chính paper hội nghị và phải được áp dụng lại.

Đo độ phân kỳ của hiệp phương sai đặc trưng có điều kiện lớp **giữa các client** trên cả bốn ô skew:

$$D = \frac{1}{C}\sum_c \frac{2}{N(N-1)}\sum_{i<j} \big\| \Sigma_{i,c} - \Sigma_{j,c} \big\|_F \Big/ \big\|\bar{\Sigma}_c\big\|_F$$

Dự đoán: $D \approx 0$ dưới label skew thuần, $D \gg 0$ dưới feature skew.

**Cổng quyết định:** nếu $D$ không tăng rõ rệt khi bật feature skew, thì CCFA không có gì để khai thác → dừng nhánh phương pháp, chuyển toàn bộ nguồn lực sang phương án dự phòng (Mục 9). Chi phí của Thí nghiệm 0: vài giờ GPU, vì chỉ cần checkpoint FedAvg ngắn.

### 6.2. Ma trận 2×2 chế độ lệch phân phối

| | Không feature skew | Có feature skew (xoay ảnh) |
|---|---|---|
| **Không label skew** | Ô A — IID *(baseline kiểm chứng)* | Ô B — **feature skew thuần** *(cần viết mới)* |
| **Có label skew (LDA α=0.1)** | Ô C — `CleanCIFAR10` *(đã có)* | Ô D — `RotatedCIFAR10` *(đã có, benchmark của FedBR)* |

Hai ô C và D đã có sẵn trong repo. Ô B cần một dataset class mới: thay `get_noniid_class_and_labels` bằng phân hoạch đồng đều, giữ nguyên phần xoay. Ô A là trường hợp suy biến của B.

**Ô B là đóng góp riêng của luận văn** — chưa có benchmark FL chuẩn nào cô lập feature skew khỏi label skew theo cách này.

### 6.3. Đường đặc tuyến vận hành theo độ nặng feature skew

`fedbr/datasets.py:438` đang hardcode `dirichlet.Dirichlet(1.0 * p).sample()` cho phân phối góc xoay của mỗi client. Thêm tham số `--rot_alpha` (khoảng 3 dòng code) sẽ tạo ra **trục độ nặng feature skew**, đóng đúng vai trò mà Dirichlet $\beta$ đóng cho label skew trong Fig. 1 của paper hội nghị.

Kết quả kỳ vọng: một hình đối xứng với Fig. 1 — *gain của CCFA theo $\alpha_{\text{rot}}$* — cho phép phát biểu gain như một đường đặc tuyến thay vì một con số. Đây là sự tiếp nối phương pháp luận rõ ràng nhất giữa hai công trình.

### 6.4. Kiểm toán confound trên FedBR (đóng góp C3)

Áp dụng nguyên xi phương pháp luận Section V của paper hội nghị. Bốn confound đã được phát hiện trong quá trình tái hiện và ghi trong `REPRODUCE.md`:

| # | Confound | Trạng thái |
|---|---|---|
| 1 | **Ngân sách pseudo-data** (mặc định 32) — đối ứng trực tiếp của $M_c$. FedBR quảng bá ưu thế là *data efficiency* (32 so với 2000 của VHL). Gain có phẳng theo ngân sách không? | Cần quét |
| 2 | **Độ mạnh baseline** — Appendix A nói baseline được tune trên lưới nhưng **không công bố giá trị thắng**. Baseline dưới-tune làm gain bị thổi phồng. | Cần sweep |
| 3 | **Projection MLP to gấp 4 lần paper mô tả** — Appendix A ghi width 256 / output 128; `FedBR.__init__` (`algorithms.py:967–970`) ghi đè thành width 1024 / output 512. Confound về *capacity* của Component 2, chưa ai báo cáo. | Cần quét |
| 4 | **Lỗi `if not angle`** — code phát hành thay môi trường test 0° (không xoay) bằng ảnh xoay ngẫu nhiên, nên trung bình trên 10 môi trường test được lấy trên 9 góc cố định + 1 góc ngẫu nhiên. Đã sửa trong repo; cần đo delta giữa số của code gốc và số sau khi sửa. | Đã sửa, cần đo |

Riêng mục 4 tự nó đã là một phát hiện về tính tái hiện đáng công bố.

### 6.5. Các kiểm soát ngoại vi

| Kiểm soát | Cách thực hiện | Vì sao cần |
|---|---|---|
| **Cross-architecture** | `BACKBONE=resnet18_gn` / `resnet20_gn` | Paper hội nghị liệt kê đây là external control chính còn thiếu. Nay chỉ cách một flag. |
| **Số lớp cao** | CIFAR-100 (repo đã hỗ trợ) | Giả thuyết neural-collapse trong paper hội nghị dự đoán hành vi khác ở $C$ lớn. |
| **Nhiều seed** | Tối thiểu 3 seed cho **mọi** con số báo cáo | Table III của paper hội nghị cho thấy spread ±1.2 pp trên paired Δ. Feature skew thêm một nguồn ngẫu nhiên (phân phối góc), phương sai có thể còn cao hơn. **Nếu buộc phải cắt chi phí thì cắt số phương pháp, không cắt seed.** |

### 6.6. Kỷ luật so sánh — nguyên tắc bất di bất dịch

Luận văn dùng **hai stack**: Flower (paper hội nghị) và DomainBed/FedBR (repo này). Paper hội nghị đã tự đặt ra nguyên tắc *"chỉ so sánh paired, within-stack"*. Nguyên tắc này phải được giữ trong luận văn:

- **Không** so sánh số tuyệt đối giữa chương Flower và chương FedBR.
- Claim xuyên chương phải là **cơ chế lặp lại được**, không phải con số.
- Mọi gain đều báo cáo dạng **paired Δ trên cùng checkpoint, cùng lần rút phân hoạch**.

Phát biểu rõ nguyên tắc này trong chương Phương pháp sẽ biến một điểm yếu tiềm tàng thành một điểm mạnh về phương pháp luận.

---

## 7. Cấu trúc luận văn đề xuất

| Chương | Nội dung | Nguồn |
|---|---|---|
| **1. Giới thiệu** | FL, non-IID, thiên lệch cục bộ; câu hỏi nghiên cứu; đóng góp | — |
| **2. Tổng quan** | Tối ưu hóa nhận biết non-IID; hiệu chuẩn head; MAFL; sinh so với phân biệt | Mở rộng từ Section II paper hội nghị |
| **3. Nền tảng: thiên lệch head dưới label skew** | Tóm lược có kiểm soát paper hội nghị: các negative, confound ngân sách/baseline, trần LDA, cơ chế định hướng | **Paper hội nghị (đã bình duyệt)** |
| **4. Tái hiện FedBR và kiểm toán confound** | Hạ tầng tái hiện, các sai lệch code↔paper, 4 confound ở Mục 6.4 | **Repo + REPRODUCE.md (đã xong)** |
| **5. Khung chẩn đoán 2×2 chế độ lệch phân phối** | Thí nghiệm 0, ma trận 2×2, đường đặc tuyến theo $\alpha_{\text{rot}}$ | Đóng góp C1 |
| **6. CCFA: phương pháp đề xuất** | Động cơ lý thuyết, thuật toán, ablation CCFA-1/CCFA-2, chi phí | Đóng góp C2 |
| **7. Phân tích cơ chế** | Norm head theo lớp, worst-class recall, confusion; CCFA xoay hay co giãn không gian đặc trưng? | Lặp lại Section VII paper hội nghị trên stack mới |
| **8. Kết luận** | Tổng hợp; giới hạn ngoại vi; hướng tiếp theo | — |

**Ưu điểm cấu trúc này:** Chương 3 và Chương 4 **đã có sẵn nội dung** — một đã được bình duyệt và chấp nhận, một đã được thực hiện xong trong repo. Luận văn khởi động với khoảng 40% khối lượng đã nằm trong tay.

---

## 8. Kế hoạch 12 tháng và ngân sách GPU

### 8.1. Ước tính chi phí tính toán

Từ `REPRODUCE.md` §6 (đã đo trên phần cứng thật, không phải ước lượng lý thuyết):

- Chạy đầy đủ 1000 vòng: FedAvg-like ≈ 5–6 h; FedBR-like ≈ 9–10 h (gồm cả đánh giá)
- Ở `ROUNDS=300`: xấp xỉ 1/3 chi phí, và `REPRODUCE.md` ghi nhận 300 vòng **bảo toàn thứ tự các phương pháp** và phần lớn câu chuyện hội tụ

**Quyết định phương pháp luận cần ghi vào luận văn:** dùng `ROUNDS=300` làm **giao thức chuẩn cho toàn bộ phần khảo sát**, và chỉ dành 1000 vòng đầy đủ cho **đúng một bảng headline**. Phải trình bày đây là lựa chọn có chủ đích kèm bằng chứng bảo toàn thứ tự — thay vì để hội đồng phát hiện ra như một chỗ cắt xén.

| Giai đoạn | Nội dung | Ước tính (GPU-ngày, 1 card) |
|---|---|---|
| P1 | Tái hiện Table 1 đầy đủ + error bar 3 seed | ~3 |
| P0 | Thí nghiệm 0 (cổng kiểm tra) | ~0.5 |
| P2 | Ma trận 2×2 × {FedAvg, FedBR} × 3 seed @ 300 vòng | ~2.5 |
| P3 | Quét $\alpha_{\text{rot}}$ (đường đặc tuyến) | ~2.5 |
| P4 | Hiệu chuẩn post-hoc trên checkpoint đã lưu | ~0.2 (gần như miễn phí) |
| P5 | Kiểm toán confound (ngân sách, baseline, MLP width) | ~3 |
| P6 | CCFA + ablation CCFA-1/CCFA-2 × 4 ô × 3 seed | ~4 |
| P7 | Bảng headline @ 1000 vòng | ~3.5 |
| P8 | Kiểm soát cross-architecture (`resnet18_gn`) | ~1 |
| | **Tổng** | **~20 GPU-ngày** |

Với biên an toàn 2× cho chạy lại và sai sót: **~40 GPU-ngày trên một card**, hoặc **~20 ngày lịch trên instance 2 GPU**. Trong khung 12 tháng, hoàn toàn khả thi.

> Không nên tin con số này một cách mù quáng. `make probe` in ra `h/1000rd` **trên đúng card vừa thuê** — chạy nó trước mỗi giai đoạn lớn và nhân với giá thuê theo giờ trước khi cam kết.

### 8.2. Lịch trình

| Tháng | Công việc | Sản phẩm |
|---|---|---|
| 1 | Hoàn tất tái hiện FedBR đầy đủ (P1); viết Chương 4 | Chương 4 bản nháp |
| 2 | **Thí nghiệm 0 — cổng quyết định** (P0); viết Chương 2, 3 | Quyết định đi/dừng nhánh CCFA |
| 3 | Cài `--rot_alpha`, dataset class ô B, switch ablation Table 4/Table 6 | Hạ tầng cho C1 |
| 4–5 | Ma trận 2×2 (P2) + đường đặc tuyến (P3) + hiệu chuẩn post-hoc (P4) | Chương 5 bản nháp |
| 6 | Kiểm toán confound (P5) | Hoàn thiện Chương 4 |
| 7 | Cài đặt CCFA; sửa lỗi; chạy thử ngắn | Code CCFA |
| 8–9 | CCFA + ablation đầy đủ (P6) | Chương 6 bản nháp |
| 10 | Bảng headline (P7) + cross-architecture (P8) | Số liệu cuối |
| 11 | Phân tích cơ chế (Chương 7); tổng hợp số liệu | Chương 7 |
| 12 | Hoàn thiện luận văn; chuẩn bị bảo vệ | Bản cuối |

**Mốc chặn:** Tháng 2 có cổng quyết định. Nếu Thí nghiệm 0 cho tín hiệu âm, chuyển sang phương án dự phòng ở Mục 9 ngay từ tháng 3 — vẫn còn 10 tháng, thừa sức hoàn thành một luận văn đo lường hoàn chỉnh.

Ngoài ra, có thêm ba việc lập trình nhỏ nên làm sớm (chúng mở khóa nhiều thí nghiệm cùng lúc):
1. `--rot_alpha` — trục độ nặng feature skew (~3 dòng)
2. Switch ablation từng component của FedBR — `REPRODUCE.md` §4 mục 2 ghi nhận Table 4 hiện **không** tái hiện được vì thiếu switch này
3. Đánh giá local model trước khi aggregate — `REPRODUCE.md` §4 mục 3; đây chính là **phép đo trực tiếp của "local learning bias"** mà cả hai paper đều cần

Ba mục này vừa phục vụ luận văn, vừa là đóng góp mã nguồn mở cho cộng đồng (hiện không ai chạy được các ablation đó từ code phát hành).

---

## 9. Quản trị rủi ro

### 9.1. Nếu CCFA không cải thiện

**Luận văn vẫn đứng vững.** Khi đó các đóng góp còn lại là:

1. Tái hiện FedBR có kiểm soát + danh mục sai lệch code↔paper (Chương 4)
2. Khung chẩn đoán 2×2 và đường đặc tuyến theo độ nặng feature skew (Chương 5)
3. Kiểm toán confound trên FedBR (Chương 4)
4. **Một kết quả âm có động cơ lý thuyết** đóng lại khe hở mà paper hội nghị để mở — tức là hoàn tất lý thuyết, chứ không phải thất bại

Điểm 4 rất quan trọng: nếu đặc trưng thật + có điều kiện lớp + feature skew mà **vẫn** không thoát được trần, thì trần đó tổng quát hơn nhiều so với những gì paper hội nghị dám tuyên bố. Đó là một kết quả mạnh hơn, không yếu hơn.

Học viên đã có tiền lệ được chấp nhận với một paper kết quả âm. Đây là năng lực đã được chứng minh, không phải hy vọng.

### 9.2. Rủi ro về kỳ vọng của hội đồng

Rủi ro thực sự lớn nhất **không phải** về kỹ thuật, mà là: **chương trình thạc sĩ hướng nghiên cứu (15 TC) tại UIT có bắt buộc phải có một phương pháp đề xuất mới hay không?**

- Nếu **có bắt buộc**: CCFA phải được ưu tiên và đẩy sớm trong lịch (cân nhắc dịch P6 lên tháng 6–7) để còn thời gian cho nó thất bại và xoay hướng.
- Nếu **không bắt buộc**: cấu trúc C1 + C3 + phân tích cơ chế đã là một luận văn chặt chẽ và rủi ro thấp hơn nhiều; CCFA trở thành chương "bonus".

**Đây là câu hỏi cần hỏi CBHD trước tiên**, vì câu trả lời quyết định trọng số giữa các chương và thứ tự lịch trình.

### 9.3. Rủi ro kỹ thuật cụ thể

| Rủi ro | Giảm thiểu |
|---|---|
| $\Sigma_c$ suy biến với 32 pseudo-data, $d=512$ | Shrinkage bắt buộc; hoặc quét số pseudo-data như một siêu tham số của CCFA (đằng nào cũng phải làm cho confound #1) |
| Soft label từ global model quá nhiễu ở đầu huấn luyện | Warm-up $T_0$; báo cáo $T_0$ công khai như siêu tham số |
| Chi phí tính toán CCFA quá cao | Đo `step_time` ngay từ chạy thử ngắn tháng 7; nếu quá đắt, chiếu đặc trưng xuống chiều thấp trước khi tính $\Sigma$ |
| Instance bị preempt giữa chừng | Repo đã có cơ chế `done` marker và resume — chạy lại cùng target là tiếp tục, không phải làm lại |

---

## 10. Nội dung cần sửa trong đề cương

Phục vụ mục *GIẢI TRÌNH CHỈNH SỬA* của biểu mẫu:

| Mục trong đề cương | Cần sửa thành |
|---|---|
| Tên đề tài (VI/EN) | Theo Mục 3.1 |
| Giới thiệu đề tài | Giữ phần bối cảnh FL/non-IID; thay đoạn về "mẫu trung bình đại diện" bằng bài toán phân định thiên lệch head ↔ feature |
| Input | Thêm: checkpoint FedAvg/FedBR đã lưu; bốn chế độ phân hoạch non-IID |
| Output | Thay bằng: khung chẩn đoán 2×2; phương pháp CCFA; báo cáo kiểm toán confound |
| Mục tiêu cụ thể | **Bỏ nhánh hồi quy.** Thay bằng: (a) phân định thiên lệch theo chế độ skew, (b) CCFA, (c) kiểm toán confound |
| Mô hình đề xuất | Thay sơ đồ FedMix-style bằng sơ đồ CCFA (Mục 5) |
| Phương pháp thực hiện | Bổ sung: giao thức paired before/after; kỷ luật within-stack; tối thiểu 3 seed |
| Kết quả dự kiến | Nêu rõ **cả hai nhánh kết quả** (CCFA hiệu quả / CCFA trơ) đều là đóng góp — thể hiện thiết kế nghiên cứu falsifiable |
| Tài liệu tham khảo | Bổ sung: Guo et al. ICML 2023 (FedBR); Vu & Nguyen (paper hội nghị); Efron 1975; Ng & Jordan 2001; Luo et al. NeurIPS 2021 (CCVR); Hsu et al. 2019 |
| Kế hoạch 12 tháng | Thay bằng bảng ở Mục 8.2 |

**Lập luận chính cho phần giải trình:**

> Trong quá trình thực hiện, nhóm nghiên cứu (gồm học viên và CBHD) đã kiểm chứng cơ chế lõi của đề cương ban đầu — chia sẻ mẫu trung bình đại diện kết hợp xấp xỉ Taylor của hàm mất mát — bằng một nghiên cứu có kiểm soát trên hai chế độ non-IID và ba seed. Kết quả cho thấy cơ chế này **không mang lại cải thiện đo được** và âm nhất quán trên mọi seed; công trình này đã được chấp nhận đăng tại hội nghị. Việc điều chỉnh hướng đề tài vì vậy là **hệ quả trực tiếp của kết quả nghiên cứu đã được bình duyệt**, nhằm chuyển nguồn lực sang một câu hỏi mà chính công trình đó đã xác định là còn bỏ ngỏ và có cơ sở lý thuyết rõ ràng.

---

## 11. Ba việc nên làm ngay

1. **Trao đổi với CBHD** về câu hỏi ở Mục 9.2 (có bắt buộc phương pháp mới không) — câu trả lời quyết định trọng số các chương.
2. **Chạy Thí nghiệm 0** (Mục 6.1) càng sớm càng tốt. Chi phí ~0.5 GPU-ngày, nhưng nó quyết định toàn bộ nhánh phương pháp. Không viết một dòng code CCFA nào trước khi có kết quả này.
3. **Cài ba knob ở cuối Mục 8.2** (`--rot_alpha`, switch ablation component, đánh giá local model). Chúng là hạ tầng dùng chung cho cả ba đóng góp, và đều là thay đổi nhỏ.

---

## Phụ lục A — Bản đồ mã nguồn

| Việc cần làm | Vị trí |
|---|---|
| Trục độ nặng feature skew | `fedbr/datasets.py:438` — `Dirichlet(1.0 * p)` đang hardcode |
| Dataset ô B (feature skew thuần) | `fedbr/datasets.py` — lớp mới, thay `get_noniid_class_and_labels` bằng phân hoạch đồng đều, giữ `rotate_dataset` |
| Dataset ô C (label skew thuần) | `fedbr/datasets.py:470` — `CleanCIFAR10`, **đã có** |
| Dataset ô D (label + feature) | `fedbr/datasets.py:417` — `RotatedCIFAR10`, **đã có** |
| Pseudo-label đồng đều của FedBR | `fedbr/algorithms.py:1114` |
| Featurizer toàn cục đóng băng (dùng cho CCFA) | `fedbr/algorithms.py:1121` — `self.original_feature` |
| Mục tiêu min-step (nơi cộng $\mathcal{L}_{\text{CCFA}}$) | `fedbr/algorithms.py:1160` — `gen_loss` |
| Projection MLP bị ghi đè kích thước (confound #3) | `fedbr/algorithms.py:967–970` |
| Chuyển backbone (kiểm soát cross-architecture) | `fedbr/networks.py:261–278` |
| Danh mục sai lệch code ↔ paper | `REPRODUCE.md` §4, §7 |
| Mô hình chi phí và `make probe` | `REPRODUCE.md` §5, §6 |

## Phụ lục B — Số liệu then chốt từ paper hội nghị (dùng cho Chương 3)

| Kết quả | Giá trị |
|---|---|
| FedMix ($m=1$) so với FedAvg, K=2 shard | −1.86 ± 0.79 pp (âm mọi seed) |
| C1 class-aware pairing | −1.90 ± 1.23 pp (âm mọi seed) |
| C1+C2, Dirichlet $\beta=0.3$ | −1.64 ± 1.20 pp (âm mọi seed) |
| Số hạng Taylor bậc hai (T2) tại khởi tạo | ~$10^{-4}$ (0.013%) của bậc nhất |
| CCVR, ngân sách thấp $M_c=100$, $\beta=0.1$ | +0.29 pp |
| CCVR, ngân sách paper $M_c=2000$, $\beta=0.1$ | +0.97 pp (gấp 3.3×) |
| CCVR, $M_c=2000$, $\beta=0.05$ | +4.36 ± 0.51 pp |
| LDA (sinh) — trần | +6.45 ± 1.29 pp (CIFAR-10) |
| CCVR | +4.41 ± 1.19 pp |
| Newton-CE (1 bước) | +2.98 ± 1.04 pp |
| Newton-CE (hội tụ, ~15 bước) | +6.14 ± 1.37 pp — vẫn **dưới** LDA trên cả 6 cặp |
| Tỉ lệ max/min norm head theo lớp | 1.10–1.17 → thiên lệch là **định hướng**, không phải độ lớn |
| Worst-class recall sau hiệu chuẩn, $\beta=0.05$ | +44 / +45 / +26 pp (seed 42/43/44) |