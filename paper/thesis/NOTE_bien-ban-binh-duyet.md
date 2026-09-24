# Biên bản bình duyệt & Lộ trình sửa

**Đối tượng:** `De-xuat-dieu-chinh-huong-luan-van.md`
**Chế độ:** ARS academic-paper-reviewer v1.11.1, `full` — panel 5 ghế tách vai
**Ngày:** 15/09/2026 — Vòng 1
**Calibration status:** `NOT_CALIBRATED` · `criteria_binding_unavailable` (không có bộ tiêu chí chính thức của UIT; mọi phán xét là field-general, không phải tuyên bố venue-alignment)

> **Ghi chú về tính độc lập:** 5 ghế commit báo cáo mà không thấy output của nhau (Iron Rule #2), chạy trên các ngữ cảnh tách biệt. Đây là **tách vai có ghi nhận**, KHÔNG phải bằng chứng về các quá trình lỗi độc lập. Cùng một model family cho cả 5 ghế → có tương quan lỗi tiềm tàng. Sự hội tụ của nhiều ghế vào một phát hiện là tín hiệu **củng cố**, không phải xác nhận độc lập.

---

## 1. Quyết định biên tập

### **MAJOR REVISION**

| Ghế | Khuyến nghị | Confidence |
|---|---|---|
| Journal-Fit | Major Revision | 4 |
| R1 — Methodology | Major Revision | 4 |
| R2 — Domain | Major Revision | 4 |
| R3 — Perspective (thống kê chiều cao) | Major Revision | 4 |
| Devil's Advocate | (không chấm điểm) — 3 CRITICAL | — |

**Đồng thuận 5/5.** Không có ghế nào đề nghị Reject; cũng không ghế nào đề nghị nhẹ hơn Major.

**Phán xét cốt lõi:** Quyết định **bỏ đề cương cũ là đúng** và được bằng chứng định lượng hậu thuẫn (xem §3.1). Nhưng **phương pháp đề xuất CCFA (đóng góp C2) không sống sót qua bình duyệt ở dạng hiện tại** — bốn khiếm khuyết CRITICAL độc lập, mỗi cái tự nó đủ làm vô hiệu Chương 6. Hai đóng góp còn lại (C1 khung chẩn đoán, C3 kiểm toán confound) **đứng vững** và không bị bất kỳ finding nào làm suy yếu.

---

## 2. Adjudication các CRITICAL của Devil's Advocate

*(Iron Rule #4: mọi DA CRITICAL phải được phân xử công khai)*

| # | Nội dung | Phán xử | Căn cứ |
|---|---|---|---|
| **C1** | Tiêu chuẩn kép: dùng bằng chứng label-skew để giết đề cương cũ, đồng thời lập luận label-skew không quyết định hành vi feature-skew để cứu CCFA | **VALIDATED (một phần, và phần đó chịu tải)** | R1 W13 định lượng độc lập: chỉ hàng FedMix ($m{=}1$) loại trừ được gain ≥0 ở cận trên 95% một phía (−0.53 pp); C1 (+0.17) và C1+C2 (+0.38) **không**. DA đúng khi nói 2/4 dòng bị tái gán nhãn, và đúng khi tự loại trừ dòng FedMix. **Kết luận bỏ đề cương vẫn đứng** vì cơ chế lõi của đề cương *là* dòng FedMix |
| **C2** | Cổng Thí nghiệm 0 đo sai đại lượng; pseudo-data đã bình quân hóa feature skew | **VALIDATED (phần 1) / SỬA CƠ CHẾ (phần 2)** | Phần 1: R1 W1 + R3 W1 + R2 W5 hội tụ độc lập — 4/5 ghế. Phần 2: kiểm chứng trực tiếp `train_fed.py:408–409` cho thấy pseudo-data rút **đều trên mọi client**, mỗi mẫu là trung bình 10 ảnh **trong một client ngẫu nhiên** — không phải trung bình xuyên client như DA mô tả. Hệ quả chịu tải vẫn đứng (pool bất khả tri client + làm mịn nặng; FedBR Appendix B: *"close to random noise"*) |
| **C3** | Ba trong bốn dòng "đã bị bác bỏ" được nguồn gắn nhãn exploratory/single-seed, và việc tái gán nhãn đi vào văn bản hành chính | **VALIDATED** | R1 W12 + R3 W8 + R2 W8 hội tụ — 4/5 ghế. R1 đối chiếu nguyên văn: nguồn viết *"the four extensions we report as exploratory, not as failures of published methods"* và *"the exploratory probes remain single-seed and untuned"* |

**Phát hiện khóa khung của DA** (không phải khiếm khuyết, nhưng ảnh hưởng quyết định): đề cương đã đăng ký đặt **Mục tiêu tổng quát** là *"Nghiên cứu cơ sở lý thuyết về các kỹ thuật làm phong phú không gian đặc trưng và phương pháp xấp xỉ hàm mất mát dựa trên khai triển Taylor"* — một mục tiêu **nghiên cứu**, không phải cam kết cải thiện hiệu suất. Cải thiện chỉ xuất hiện ở mục *Kết quả dự kiến*. **ADJUDICATED: hợp lệ và chưa được xét.** Nó mở ra một phương án rẻ hơn mà đề xuất không nhắc tới một lần (xem §5).

---

## 3. Phát hiện theo mức độ hội tụ

### 3.1. Điều gì SỐNG SÓT (không bị finding nào làm suy yếu)

| Nội dung | Ghế xác nhận |
|---|---|
| **Quyết định bỏ đề cương cũ là đúng về mặt thống kê** — cơ chế lõi (mean-augmented input, FedMix $m{=}1$) có cận trên 95% một phía là −0.53 pp, loại trừ được gain | R1 W13 (phát biểu tường minh), Journal-Fit S1 |
| **C3 — Kiểm toán confound** là đóng góp thật, độc lập, kiểm chứng được | DA (Quan sát), R2 S4 (kiểm chứng độc lập MLP width 4×), Journal-Fit S4 |
| **C1 — Khung chẩn đoán 2×2** có giá trị độc lập với số phận CCFA (sau khi sửa confound test-set) | R3 S5, Journal-Fit S5 |
| **Kỷ luật within-stack §6.6** là đoạn phương pháp luận vững nhất tài liệu | R1 S2, DA (Quan sát) |
| **Mục 1.2** (tự thu hẹp phạm vi kết quả T2) là chuẩn mực đúng | Cả 5 ghế nêu, DA gọi là "đoạn trung thực nhất tài liệu" |
| **Thiết kế soft-label tại client né được chi phí uplink $d^2$** mà nguồn định giá là đắt | R2 S2, DA (Quan sát) |
| **Phụ lục A neo mã nguồn phần lớn ĐÚNG** (đối chiếu 8/8 số dòng) | R1 (bảng đối chiếu), DA (4/4 neo) |

### 3.2. CRITICAL — mỗi mục tự nó đủ vô hiệu hóa Chương 6

**K1. Cổng Thí nghiệm 0 đo đại lượng trực giao với đại lượng CCFA khai thác** — *4/5 ghế*

| | $D$ (§6.1) | $\mathcal L_{\mathrm{CCFA}}$ (§5.3) |
|---|---|---|
| Biến thiên | **dữ liệu** (client $i$ vs $j$) | **featurizer** ($\phi_i$ vs $\phi_g$) |
| Cố định | featurizer (một checkpoint chung) | dữ liệu (cùng 32 pseudo-data) |
| Không gian | toàn bộ $d{=}512$ | không gian con $\le 32$ chiều do pseudo-data căng ra |

Cổng **không phải điều kiện cần cũng không phải điều kiện đủ**. $D\gg0$ không kéo theo CCFA có gradient (nếu hướng phân kỳ không được 32 điểm kích thích); $D\approx0$ không kéo theo $\mathcal L_{\mathrm{CCFA}}=0$ (vì $\phi_i$ vẫn trôi khỏi $\phi_g$ sau 50 bước cục bộ ở **mọi** ô, kể cả ô A IID).

**K2. Mắt xích 4 đúng trong không gian dữ liệu, sai trong không gian đặc trưng học được** — *3/5 ghế*

Phân ba trường hợp: (a) không gian dữ liệu — $p_i(x|y)$ trùng nhau **theo định nghĩa phân hoạch** ✅; (b) đặc trưng dưới $\phi$ chung đóng băng — vẫn trùng ✅, **và đây chính là chế độ paper hội nghị đo** (Table IV: *"one frozen backbone, identical statistics"*); (c) đặc trưng với $\phi_i$ riêng từng client — **sai** ❌.

Mấu chốt: **chính label skew sinh ra $\phi_i \ne \phi_j$** — đó là hiện tượng FedBR được đặt tên theo (*Local Learning Bias*). Do đó dự đoán "CCFA trơ dưới label skew" mất cơ sở, và **thiết kế falsifiable của §4 không diễn giải được ở cả hai nhánh**.

**K3. $\Sigma_c$ không ước lượng được ở $n{=}32$, $d{=}512$; shrinkage là phi-giảm-thiểu** — *2/5 ghế, định lượng đầy đủ*

- Tham số cần ước lượng: $C\cdot d(d{+}1)/2 \times 2 = 2{,}626{,}560$ từ **32 điểm**. Tỉ lệ $8.2\times10^4$.
- Cỡ mẫu hiệu dụng mỗi lớp: $32/10 = 3.2$ → hạng $\hat\Sigma_c \le 3$ trên 512 chiều. $n/d = 0.006$.
- **Shrinkage không cải thiện SNR của một hiệu**: $(1-\delta)$ nhân đều tín hiệu lẫn nhiễu. Lợi ích thật của shrinkage (khả nghịch) thì CCFA không dùng tới.
- Ở $\delta^\star_{\text{LW}}=1$ (bão hòa khi $r\ge31$): $\hat\Sigma_c \to \frac{\mathrm{tr}S_c}{d}I$, số hạng bậc hai **suy biến thành một vô hướng mỗi lớp** — 10 số thay cho 1,313,280.
- **Ngưỡng khả thi**: 500–5,000 pseudo-data để tín hiệu vừa vượt nhiễu; 5,000–130,000 để dùng được. Mặc định 32 → cần **16×–160×**, tức **phá vỡ ưu thế data-efficiency của FedBR** (vượt qua ngân sách 2000 của VHL).
- Chi phí: P6 từ 4 GPU-ngày lên **32–320**, tức 1.6×–16× **toàn bộ** ngân sách luận văn.
- **Lối thoát "chiếu xuống chiều thấp" đóng bằng số học**: cần $k\le7$ để sai số ≤50%, nhưng $k=7 < C=10$ không đủ tách 10 trung bình lớp. Cửa sổ là **tập rỗng** ở $n=32$.
- **Ngoại lệ có thật**: `resnet20_gn` có $d{=}64$ (`networks.py:106–109`) — đây là cấu hình duy nhất CCFA-2 còn bảo vệ được.

**K4. Tuyên bố khoảng trống nghiên cứu sai — phản ví dụ nằm trong baseline của chính FedBR** — *3/5 ghế*

| Thành tố của CCFA | Đã tồn tại ở |
|---|---|
| Căn chỉnh **có điều kiện lớp** trên **đặc trưng thật**, **dưới feature skew** | **VHL (Tang et al. 2022)** — baseline của FedBR, chạy trên **đúng** RotatedCIFAR10 (Table 2), **đã cài sẵn** trong repo (`make table2-vhl`). FedBR mô tả nguyên văn: *"forces the local features to be close to the features of the same class virtual data"* |
| Bậc nhất có điều kiện lớp (prototype alignment) | FedProto và dòng prototype-based FL |
| Ước lượng $\Sigma_c$ trong FL | CCVR — **chính đề xuất đã trích** |
| Bậc hai trong alignment | Deep CORAL (2016) — **trong ref list của FedBR**; FedDecorr — **đã cài trong repo**, bị comment ngay trong `FedBR.update` (`algorithms.py:1162–1164`) |
| Soft pseudo-label từ mô hình toàn cục | FedNTD (baseline của FedBR), FedDF; **và chính FedBR Eq. (4)** dưới `use_Mixture` |
| C1: "chưa nghiên cứu nào tách hai loại skew có kiểm soát" | **NIID-Bench (Li et al. ICDE 2022)** — là reference **[3] trong chính paper hội nghị** |

Grep toàn văn đề xuất cho `prototype|FedProto|MOON|VHL|FedNTD|FedDecorr|CORAL|distill`: **đúng 1 hit** (VHL ở §6.4, chỉ nói về ngân sách pseudo-data). **Không có quy trình tìm kiếm văn liệu nào.**

**K5. Công suất thống kê: 3 seed không phân giải được hiệu ứng mà luận văn cần** — *1 ghế, định lượng, không bị bác*

Với $s=1.2$ pp (lấy từ Table III của nguồn), $n=3$, $df=2$:
- Ngưỡng ý nghĩa: $|\Delta| \ge 2.98$ pp · **MDE@80% = 3.92 pp**

Kiểm chứng ngược trên chính nguồn: FedMix (−1.86±0.79) $p{=}.055$ **không đạt**; C1 (−1.90±1.23) $p{=}.116$ **không đạt**; LDA (+6.45±1.29) $p{=}.013$ đạt. Giao thức 3 seed phân giải được **đúng khoảng ≥3 pp và không gì nhỏ hơn**.

Số phép so sánh tối thiểu theo chính đề xuất: **≈53**. FWER không hiệu chỉnh ở $m{=}20$: **64.2%**; ngưỡng Bonferroni: **13.8 pp** — gấp đôi hiệu ứng lớn nhất trong toàn bộ văn liệu được trích.

**Nhánh null không thực hiện được**: "CCFA trơ" là mệnh đề null; một t-test không ý nghĩa ở $n{=}3$ không chứng minh nó. Cần TOST, biên hẹp nhất khả thi ở $n{=}3$ là **±2.02 pp** — rộng hơn cả gain CCVR ở $\beta{=}0.1$ (+0.97 pp).

**K6. Ô "Mô hình đề xuất" của biểu mẫu có nguy cơ để trống** — *1 ghế (đúng remit)*

§9.2 tự nhận chưa biết chương trình có bắt buộc phương pháp mới hay không, trong khi §6.1 quy định dừng nhánh CCFA nếu cổng đóng, và §11 nói *"Không viết một dòng code CCFA nào trước khi có kết quả này"*. Ở nhánh cổng-đóng, biểu mẫu nộp lên có ô **"Mô hình đề xuất"** trống. Đồng thời §9.1 điểm 4 (kết quả âm có động cơ lý thuyết) **chỉ tồn tại nếu CCFA đã được chạy** — hai nhánh thất bại khác nhau đang bị gộp làm một.

### 3.3. MAJOR

| # | Phát hiện | Ghế |
|---|---|---|
| M1 | **Ma trận 2×2 bị confound ở phía đánh giá.** `CleanCIFAR10` truyền `[None]*(train_envs+10)` với `identity_dataset` → **10 môi trường test là 10 bản sao giống hệt nhau**; `RotatedCIFAR10` → 10 góc khác nhau. Cột trái/phải đo trên hai phân phối test khác nhau ⇒ **trục không trực giao**, không chạy được kiểm định tương tác | R1 W3, R2 W6, DA M3 |
| M2 | **Đảo ngược phụ thuộc lịch.** §6.1 cần cả 4 ô ở tháng 2; §8.2 xếp dataset class ô B vào tháng 3. Tháng 2 chỉ có C và D — cả hai đều có label skew, nên dự đoán "$D\approx0$ dưới label skew thuần" **không kiểm chứng được** | R1 W4 |
| M3 | **Ngân sách thiếu 1.6–5× ở bốn hàng**; ba hạng mục không có dòng ngân sách nào (CIFAR-100, đường cong CCFA×$\alpha_{\text{rot}}$, quét $\nu/\eta/T_0$). Tổng hiệu chỉnh ≈28.5 thay vì 20.2 ⇒ **biên an toàn 2× thực chất bằng 0** | R1 W5, Journal-Fit W10, DA M7 |
| M4 | **Biên an toàn đặt sai tài nguyên.** GPU không bao giờ là ràng buộc (<10% thời gian lịch ở mọi giai đoạn); tài nguyên khan là **tháng lịch**. §8.2 không có tháng đệm, và tháng 7 (cài CCFA, ≥5 lựa chọn thiết kế) không có cổng, không có float, không có dự phòng | R1 W6 |
| M5 | **CCFA mang đúng các confound mà §6.4 tố cáo FedBR.** $\nu$ là siêu tham số thứ 4 trên mục tiêu vốn đã tune cho 3 số hạng; CCFA-2 có $(\nu,\eta)$ còn CCFA-1 chỉ có $(\nu)$ → ablation bất đối xứng; $\mathcal L_{\mathrm{CCFA}}$ **không bất biến theo tỉ lệ đặc trưng** ($\|z\|^2$ vs $\|z\|^4$) nên $\eta$ hiệu dụng **trôi theo vòng**; $T_0$ là phân số của tổng vòng nên bảng headline 1000 vòng chạy **một phương pháp khác** với khảo sát 300 vòng | R1 W7, DA M7 |
| M6 | **Thiếu nhóm đối chứng quyết định.** Điểm bất động của $\mathcal L_{\mathrm{CCFA}}$ là $\phi_i\equiv\phi_g$ ⇒ về cấu trúc nó là **số hạng proximal trong không gian đặc trưng** (họ FedProx/MOON). Không có baseline FedProx, không có baseline feature-proximal thuần $\|\phi_i(x_p)-\phi_g(x_p)\|^2$ ⇒ nếu CCFA thắng, **không phân định được** với client-drift regularization | R3 W5, R2 W2 |
| M7 | **Efron/Ng–Jordan dùng quá phạm vi + mâu thuẫn nội tại.** Nguồn viết *"can at best tie LDA **asymptotically** and is worse **in expectation** at a finite sample budget"*; đề xuất bỏ cả hai hạn định thành "không thể vượt". Nặng hơn: mắt xích 1 tựa vào trần **shared-covariance** (Efron chỉ áp dụng khi $\Sigma_c\equiv\Sigma$) trong khi §5.3 giả định $\Sigma_c$ **khác nhau** — tức chế độ **QDA**, nơi kết quả Efron không áp dụng. Thêm: trần đo ở $n/d\approx3.9$, CCFA vận hành ở $n/d\approx0.06$ — **kém 62×–625×** | R3 W6 |
| M8 | **Xoay ảnh là nhiễu class-shared.** Mỗi client rút **một** $q_i\in\mathbb R^{10}$ rồi rút góc cho từng ảnh **độc lập với nhãn** ⇒ toán tử trộn góc **chung cho mọi lớp**. $D>0$ và cổng sẽ mở, nhưng toàn bộ phân kỳ sinh bởi **một tham số 9 bậc tự do dùng chung cho 10 lớp** — một phép căn chỉnh **bất khả tri về lớp** (đúng Component 2) đã nhận diện gần trọn. Cần đặt cổng trên $\|E_{i,c}\|_F/\|\Delta_i\|_F$ (phần dư phụ thuộc lớp / phần class-shared) | R2 W3 |
| M9 | **$D$ có sàn nhiễu 0.14–2.3, không phải ≈0, và sàn TĂNG theo độ nặng label skew.** $D_{\text{null}}\approx\sqrt{2(r{+}1)/n}$. Ô C (lớp thiểu số $n_{i,c}$ 0–50) → $D_{\text{null}}\approx1.4$; ô B ($n_{i,c}\approx500$) → $\approx0.45$. Cổng **lệch về phía một lệnh DỪNG giả**. Thêm: `REPRODUCE.md` §7 xác nhận $n_{i,c}=0$ xảy ra ⇒ $\Sigma_{i,c}$ không xác định | R3 W4, R1 W9 |
| M10 | **Mô tả Component 2 sai.** Nó ghép cặp **theo từng mẫu** trên **cùng** $x_p$ — **mạnh hơn** căn chỉnh biên, không yếu hơn. Nếu $\phi_i(x_p)=\phi_g(x_p)$ thì $\mathcal L_{\mathrm{CCFA}}\equiv0$ với **mọi** $\eta$ và mọi sơ đồ trọng số ⇒ CCFA là **phiếm hàm thô hơn của cùng một phần dư**, không phải tín hiệu trực giao | R2 W2 |
| M11 | **"FedBR bất khả tri về lớp" bỏ qua nhánh `use_Mixture`.** Eq. (4): $\tilde y_p=\frac{1}{K+1}(\frac1C\mathbf 1+\sum y_k)$ — soft label **mang nhãn thật**. `get_unlabeled_by_self` (`algorithms.py:1060–1074`) hiện thực đúng vậy. Mixture không phải nhánh phụ: FedBR khuyến nghị nó để bảo mật, Table 3 dùng nó, Fig. 6(c) cho thấy nó có thể **vượt** RSM | R2 W4, DA M9 |
| M12 | **Trọng số mềm tạo vòng tự củng cố, và ba chế độ hỏng nhân nhau trên lớp thiểu số.** $\tilde p_c$ là posterior của chính $\omega_g$ ⇒ CCFA chính quy hóa client theo hướng **tái tạo ma trận nhầm lẫn của mô hình toàn cục** (self-distillation, không phải hiệu chỉnh chệch). Với lớp thiểu số: $\tilde p_c$ **kém tin cậy nhất** × khối lượng **nhỏ nhất** ⇒ $n_{\text{eff}}$ **nhỏ nhất** ⇒ $\hat\Sigma_c$ **nhiễu nhất** — ba yếu tố cùng chiều, trên đúng lớp cần căn chỉnh nhất. Warm-up $T_0$ làm $\tilde p$ **tự tin hơn**, không **đúng hơn**. Thêm: **$w_c$ không được định nghĩa ở đâu**; $\eta$ không có thang đo | R3 W7 |
| M13 | **Pseudo-data là ảnh trộn — "hiệp phương sai có điều kiện lớp" của nó là khái niệm không xác định.** FedBR Appendix B: *"The constructed augmentation data is close to random noise."* Và nguồn vừa công bố kết quả âm cho **chính** ý tưởng gán ý nghĩa lớp cho đầu vào trộn | R2 W5, R3 W7 |
| M14 | **Rủi ro quy chế hoàn toàn vắng mặt.** Grep toàn văn cho `trùng lắp\|đạo văn\|Turnitin\|bản quyền\|quy chế`: **0 kết quả**. "Đồng tác giả" xuất hiện đúng 1 lần, ở §1.4, thuần túy như **lợi thế tu từ**. Chương 3 là công trình 2 tác giả trong đó tác giả thứ hai **chính là CBHD — người sẽ ký duyệt** | Journal-Fit W3, DA m1, m2 |
| M15 | **Không nêu tên hội nghị / trạng thái công bố.** Toàn bộ 400 dòng chỉ gọi "paper hội nghị" — không tên, năm, DOI, chỉ mục, ngày chấp nhận. Trong khi đó luận cứ trung tâm của đơn xin đổi hướng là *"đã được bình duyệt"* ⇒ **không kiểm chứng được từ hồ sơ** | Journal-Fit W4 |
| M16 | **Dùng sai công cụ thủ tục.** §10 coi việc chuyển hướng như điền ô *GIẢI TRÌNH CHỈNH SỬA*, nhưng biểu mẫu ghi rõ ô đó để *"ghi ý kiến của ĐVCM trong thông báo kết quả xét duyệt"* — để **trả lời góp ý**, không phải tự khởi xướng đổi hướng. Quy mô thay đổi (tên đề tài VI+EN, Input, Output, Mục tiêu, Mô hình đề xuất, Kế hoạch) là **đổi đề tài**, không phải "điều chỉnh" | Journal-Fit W5, DA (bên liên quan) |
| M17 | **Lịch 12 tháng vẽ lại từ "Tháng 1" mà không đối chiếu mốc đã đăng ký.** Đề cương ghi "12 tháng, từ tháng ___/2026" (ô trống). Không có câu nào nêu mốc bắt đầu, số tháng đã trôi, thời hạn theo quyết định giao đề tài, hay nhu cầu gia hạn | Journal-Fit W6 |

### 3.4. MINOR

| # | Phát hiện | Ghế |
|---|---|---|
| m1 | **Nồng độ Dirichlet của phép xoay là 0.1/thành phần, không phải 1.0.** `p = ones(10)/10` rồi `Dirichlet(1.0*p)` → nồng độ hiệu dụng 0.1. Mô phỏng 20,000 lần rút: $E[\max q]=0.666$, **số góc hiệu dụng = 2.08**. Feature skew mặc định **đã ở gần cực trị** ⇒ `--rot_alpha` chỉ quét được về phía **nhẹ hơn**, đường cong sẽ **bất đối xứng** với Fig. 1. `REPRODUCE.md` §2 cũng mô tả sai là "Dir(1.0)" | R1 W10, R2 W9 |
| m2 | **Phân hoạch góc là nguồn phương sai giữa seed lớn nhất, chưa định lượng.** Số góc trội phân biệt trong 10 client: mean 6.52, sd 1.00, khoảng 3–10 ⇒ **độ nặng feature skew thay đổi đáng kể giữa seed**. Nên tách `partition_seed` khỏi `train_seed` | R1 W10 |
| m3 | **$d$ không phải hằng số 512.** `cct` (mặc định code phát hành) = **256**; `vgg11`/`resnet18*` = 512; `resnet20_gn` = **64**. Chênh 8×, và điều đó **thay đổi kết luận khả thi** của CCFA-2 | R3 W9 |
| m4 | **P4 giả định có checkpoint best-accuracy, nhưng không tồn tại.** Kiểm chứng trực tiếp: `train_fed.py:564–565` — `--save_model_every_checkpoint` ghi đè **cùng một** `model.pkl` mỗi lần. Cờ có tên gây hiểu nhầm ⇒ **một sai lệch code↔tài liệu mới cho C3**. Phải thêm việc lưu checkpoint theo vòng vào **tháng 1**, trước P1, nếu không checkpoint của P1 mất vĩnh viễn | R1 W11 + kiểm chứng của chủ tọa |
| m5 | **Confound #4 rẻ hơn tưởng.** Lỗi `if not angle` chỉ ảnh hưởng **môi trường test** (môi trường train luôn nhận `None` tại `datasets.py:400`) ⇒ delta đo được bằng **re-evaluation trên checkpoint đã lưu, không cần huấn luyện lại** | R1 W11 |
| m6 | **Sai gán "6 cặp".** §4.1 ghi *"Đo được trên 6 cặp dataset–seed: LDA +6.45±1.29, CCVR +4.41±1.19, Newton-CE +2.98±1.04"* — ba con số này là **cột CIFAR-10, 3 seed**. "6 cặp" chỉ thuộc phát biểu về *shortfall*. Nguồn còn gắn nhãn phi suy luận: *"Since CINIC-10 contains CIFAR-10, we read these pairs descriptively, not as an inference test"* | R1 (đối chiếu) |
| m7 | **"reimplementation mở *độc lập*" đảo ngược caveat của nguồn.** Nguồn phủ định đúng từ này hai lần: *"a consistency check, **not independent validation**"*, *"not as independent external validation, since it is also our calibration target"* | R1 W12, DA M5 |
| m8 | **Phụ lục B mất caveat quan trọng nhất của hàng CCVR**: nguồn ghi +0.29 pp ở $\beta{=}0.1$ **và −0.76 pp ở $\beta{=}0.3$** — gain **đảo dấu** theo skew khi ngân sách thiếu. Đề xuất chỉ chép vế dương | R1 (đối chiếu) |
| m9 | **"40% khối lượng đã nằm trong tay"** cung cấp sẵn cho phản biện một cách diễn đạt bất lợi: gần một nửa luận văn không phải sản phẩm mới của riêng học viên | Journal-Fit W8, DA m1 |
| m10 | **Chỉ có feature skew tổng hợp bằng phép xoay**, trong khi repo đã sẵn `PACS`, `VLCS`, `OfficeHome`, `DomainNet`, `WILDSCamelyon`, `WILDSFMoW` và FedBR đã chạy PACS. Xoay là tác động nhóm **khả nghịch, thuần hình học, độc lập lớp** — cực **dễ nhất** của phổ feature skew | R2 W7 |
| m11 | **$D$ là metric sai loại trên đa tạp SPD**, và $\bar\Sigma_c$ không được định nghĩa. Nên bổ sung khoảng cách Grassmann giữa không gian riêng top-$k$ ($k\approx5$–10) — điều kiện tốt hơn nhiều ở $n\ll d$ | R3 W10 |
| m12 | **Giao thức `ROUNDS=300` chưa có hiện vật bằng chứng.** Nguồn là một câu khẳng định trong runbook, không kèm bảng/hình. Và "bảo toàn thứ hạng giữa các phương pháp đã có" không nói gì về độ ổn định của **paired Δ dưới 1 pp** — đúng đại lượng Chương 6 đo | Journal-Fit W9, DA m3 |

---

## 4. Lộ trình sửa

### 4.1. BLOCKING — phải xong TRƯỚC khi trình CBHD

| # | Việc | Nguồn | Chi phí |
|---|---|---|---|
| **B1** | **Quyết định số phận C2.** Chọn một trong ba: (a) **thu hẹp** CCFA về `resnet20_gn` ($d{=}64$) + quét ngân sách pseudo-data, và biến chính ngưỡng khả thi thành phát biểu có tiên đoán trước; (b) **thay** CCFA bằng một hướng khác; (c) **hạ** C2 xuống chương phụ, lấy C1+C3 làm trục. **Không được giữ CCFA ở dạng hiện tại.** | K3, K4, M6, M10 | Quyết định |
| **B2** | **Viết tổng quan văn liệu feature/prototype alignment trong FL** (tối thiểu: VHL, FedProto + dòng prototype, CCVR, MOON, FedDecorr, CORAL, NIID-Bench, FedNTD/FedDF), kèm bảng đối chiếu 4 trục (có điều kiện lớp? bậc mấy? đặc trưng thật hay tổng hợp? chi phí truyền thông? chế độ skew đã đo?). CCFA phải là **một hàng trong bảng**, không phải ô trống. Thay tuyên bố phủ định toàn cầu bằng tuyên bố **tổ hợp có hạn định** kèm phạm vi tìm kiếm cụ thể | K4 | 1–2 tuần |
| **B3** | **Thêm VHL và một phương pháp prototype vào baseline Chương 6.** VHL đã chạy được (`make table2-vhl`). Không có chúng thì bảng kết quả CCFA **không diễn giải được** | K4 | Ngân sách |
| **B4** | **Sửa cổng Thí nghiệm 0 để đo đúng estimand**: $\|\Sigma_c(\phi_i(x_p)) - \Sigma_c(\phi_g(x_p))\|_F$ trên đúng 32 pseudo-data với đúng $\tilde p_c$ — đây là forward pass, **rẻ hơn** cổng hiện tại. Giữ $D$ làm chẩn đoán phụ cho C1. Bổ sung: **null hoán vị** ($B{=}200$), **null split-half**, **cân bằng $n$** giữa các ô, **đường cong $D$ theo $n$**, và **ngưỡng quyết định bằng số** thay cho "rõ rệt" | K1, M9, m11 | ~0.5 GPU-ngày |
| **B5** | **Viết lại mắt xích 4 với phạm vi ba trường hợp** (dữ liệu / $\phi$ chung đóng băng / $\phi_i$ riêng). Phát biểu lại dự đoán thành **"phân kỳ do featurizer (có ở mọi ô) so với phân kỳ do dữ liệu (chỉ ô B/D)"**. Thêm **ô đối chứng nhiễu-SGD**: hai client dữ liệu y hệt, khác seed — đó là sàn thật của $\mathcal L_{\mathrm{CCFA}}$ | K2 | 1 tuần + 1 run ngắn |
| **B6** | **Khai báo cỡ hiệu ứng mục tiêu $\Delta^*$ và suy số seed từ đó.** Khai báo trước **họ giả thuyết chính** (≤4–6 Δ) + hiệu chỉnh Holm; mọi thứ khác gắn nhãn **thăm dò**. Cho nhánh "trơ": định trước **biên tương đương** và dùng **TOST** — hoặc nói thẳng rằng thiết kế không đạt được biên đó | K5 | Quyết định + ngân sách |
| **B7** | **Trả lời câu hỏi §9.2 với CBHD và Phòng ĐTSĐH trước khi nộp**, rồi viết lại §9.2 thành phát biểu dứt khoát. Ô **"Mô hình đề xuất"** của biểu mẫu không được để trống | K6 | Một cuộc trao đổi |
| **B8** | **Sửa mâu thuẫn §6.1 ↔ §9.1**: đổi cổng từ **cổng dừng** sang **cổng phân bổ nguồn lực** (dù $D$ ra sao vẫn cài và chạy C2 tối thiểu), và viết lại §9.1 thành hai nhánh tách bạch, ghi rõ nhánh nào giữ được "đóng góp số 4" | K6 | Viết lại |
| **B9** | **Bổ sung mục Tuân thủ quy chế**: (1) tuyên bố Chương 3 dựa trên công trình đã công bố + trích dẫn đầy đủ ở đầu chương và Lời cam đoan; (2) văn bản xác nhận của đồng tác giả (CBHD) về đồng ý sử dụng và phân định đóng góp; (3) đối chiếu điều khoản tái sử dụng của nhà xuất bản; (4) chủ động khai báo tỉ lệ trùng lắp dự kiến **trước** khi quét | M14 | 1 tuần |
| **B10** | **Nêu tên hội nghị, năm, trạng thái (accepted/published), DOI/chỉ mục** ở §0, §7, §10 và Phụ lục B. Đính kèm thư chấp nhận vào hồ sơ | M15 | Ngay |
| **B11** | **Xác nhận quy trình đúng với Phòng ĐTSĐH** cho thay đổi quy mô này. Tách thành (a) tờ trình 1–2 trang có chữ ký CBHD, (b) đề cương mới theo biểu mẫu. **Ghi rõ đây là thay đổi tên đề tài**, không né bằng chữ "điều chỉnh". Đối chiếu mốc bắt đầu đã đăng ký và nêu nhu cầu gia hạn nếu có | M16, M17 | Một cuộc trao đổi |
| **B12** | **Khôi phục mọi caveat của nguồn** ở §1.1, §4 mắt xích 1/2/4, §10 và Phụ lục B: bỏ chữ "độc lập"; đánh dấu mắt xích 2 là **thăm dò, một seed, chưa tune**; sửa sai gán "6 cặp"; thêm hàng CCVR $M_c{=}100$ ở $\beta{=}0.3$ (**−0.76 pp, đảo dấu**); thêm nhãn † cho C1/C1+C2. Trong §1.1 và §10, phát biểu bằng **khoảng tin cậy** thay vì dấu — neo vào hàng FedMix (cận trên 95% một phía **−0.53 pp**), là hàng duy nhất loại trừ được gain **và** là hàng tương ứng đúng với cơ chế đề cương | K1-adj, K6, m6, m7, m8 | 2–3 ngày |
| **B13** | **Thêm baseline FedProx và feature-proximal thuần** $\|\phi_i(x_p)-\phi_g(x_p)\|^2$ vào P6. Không có chúng, ablation CCFA-1 vs CCFA-2 không đủ — **cả hai đều là proximal** | M6 | Ngân sách |
| **B14** | **Sửa confound đánh giá của ma trận 2×2**: đánh giá **mọi ô trên cùng bộ môi trường test** (đề xuất: giữ 10 góc ở mọi ô), báo cáo tách biệt in-distribution (0°) và OOD (10 góc). ~5 dòng trong `CleanCIFAR10.__init__`; evaluation là forward pass nên chi phí không đáng kể | M1 | ~1 ngày |
| **B15** | **Dời ba knob hạ tầng lên tháng 1** (song song P1 — code không tranh GPU), **và thêm việc lưu checkpoint theo vòng TRƯỚC P1** — nếu không checkpoint của P1 mất vĩnh viễn và P4 không chạy được | M2, m4 | Lịch |
| **B16** | **Dựng lại §8.1** với cột "số lần chạy × giờ/lần" và cột "điều kiện tiên quyết"; bổ sung ba hàng thiếu (CIFAR-100, đường cong CCFA×$\alpha_{\text{rot}}$, quét $\nu/\eta/T_0$); **phát biểu lại biên an toàn theo ngày lịch**, không theo GPU-ngày; thêm **cổng thứ hai cuối tháng 7** và một tháng đệm | M3, M4 | 2–3 ngày |
| **B17** | **Thêm §6.4b — Kiểm toán confound trên CCFA**, đối xứng với §6.4: $\nu$, $\eta$, $T_0$, shrinkage, chiều chiếu, số pseudo-data. **Ngân sách tune bằng nhau** cho CCFA và FedBR. **Chuẩn hóa $\mathcal L_{\mathrm{CCFA}}$ theo tỉ lệ** (chia cho $\|\mu_c^{\text{glob}}\|^2$, $\|\Sigma_c^{\text{glob}}\|_F^2$) để $\eta$ không trôi. **Định nghĩa $w_c$.** Báo cáo $T_0$ theo phân số tổng vòng | M5, M12 | 1 tuần |

### 4.2. NICE-TO-HAVE — nên làm, không chặn

| # | Việc | Nguồn |
|---|---|---|
| N1 | Sửa mắt xích 1 bám nguyên văn nguồn ("ngang bằng **tiệm cận**, kém hơn **trong kỳ vọng**, dưới giả thiết Gaussian đúng **và hiệp phương sai chung**"); thêm mắt xích 1b xử lý mâu thuẫn shared-covariance ↔ $\Sigma_c$ khác nhau — viết đúng thì điều này **củng cố** động cơ CCFA; ghi rõ trần đo ở $n/d\approx3.9$ còn CCFA ở $n/d\approx0.06$ | M7 |
| N2 | Đổi tiêu chí cổng sang $\|E_{i,c}\|_F/\|\Delta_i\|_F$ (phần dư phụ thuộc lớp / phần class-shared); nếu tỉ số nhỏ, thiết kế chế độ feature skew **phụ thuộc lớp** — đó mới đúng là "Ô B đóng góp riêng" | M8 |
| N3 | Sửa mô tả Component 2 (bỏ "căn chỉnh biên", thay bằng "ghép cặp theo từng mẫu, sau phép chiếu đối kháng, dưới độ đo cosine"); viết lại mắt xích 5 phân biệt Component 1 (`use_Mixture`, có thông tin lớp) với Component 2 (không điều kiện lớp) | M10, M11 |
| N4 | Chẩn đoán bắt buộc, chi phí ~0: log **$n_{\text{eff},c}$ và entropy của $\tilde p_c$ theo từng vòng, từng lớp**; log **$\delta^\star$ thực đo**. Nếu $\delta^\star\to1$, nói thẳng rằng số hạng bậc hai đã suy biến thành khớp vết và **đổi tên biến thể** cho trung thực | K3, M12 |
| N5 | Sonde phá vòng lặp: chạy biến thể dùng **nhãn thật** của pseudo-data (chỉ để chẩn đoán). Khoảng cách với soft-label **chính là chi phí của vòng tự củng cố**, đo trực tiếp | M12 |
| N6 | Cân nhắc tính $\mu_c,\Sigma_c$ trên **đặc trưng của dữ liệu cục bộ thật** (có nhãn thật, không cần pseudo-label, vẫn không tốn truyền thông) thay vì trên pseudo-data — giải quyết luôn cả M13 lẫn vấn đề 32 mẫu | M13, M12 |
| N7 | Định nghĩa `--rot_alpha` theo nồng độ **tuyệt đối**, ghi rõ mặc định ≈0.1 (2.08 góc hiệu dụng), quét **lên** phía nhẹ hơn; sửa mô tả sai ở `REPRODUCE.md` §2; **bổ sung mơ hồ "Dir(1.0)" vào danh mục C3** | m1 |
| N8 | Tách `partition_seed` khỏi `train_seed`; tăng số `partition_seed` (nguồn phương sai trội); báo cáo thống kê cấu hình góc như **hiệp biến** để hút phương sai và tăng công suất mà không thêm run | m2 |
| N9 | Ghi $d$ theo từng backbone trong mọi bảng; **thăng `resnet20_gn` ($d{=}64$) lên trục sizing chính của C2**, giữ $d{=}512$ làm stress case — miễn phí về kế hoạch vì P8 đã có | m3, K3 |
| N10 | Thêm **một** benchmark domain shift thật (PACS rẻ nhất, WILDSCamelyon mạnh nhất về tính "FL thật"). Nếu ngân sách chặt, đổi lấy P8 | m10 |
| N11 | Thay t-test theo từng ô bằng **kiểm định xu hướng trên đường cong $\alpha_{\text{rot}}$** (hồi quy hệ số góc của Δ theo $\log\alpha_{\text{rot}}$, seed là hiệu ứng ngẫu nhiên) — gộp thông tin qua nhiều điểm, mạnh hơn nhiều so với 4 ô rời rạc | K5 |
| N12 | Xuất bảng đối chiếu thứ hạng 300 vòng ↔ 1000 vòng từ `results.jsonl` của P1 (chi phí ~0) làm hiện vật bằng chứng cho giao thức `ROUNDS=300`; **xác minh lại cho phương pháp có warm-up**, không mượn bằng chứng của FedBR | m12, M5 |
| N13 | Bỏ con số "40%", thay bằng phát biểu theo hướng nền tảng + định lượng phần mới | m9 |
| N14 | Bổ sung khoảng cách Grassmann giữa không gian riêng top-$k$ vào bộ chẩn đoán; định nghĩa $\bar\Sigma_c$; báo cáo $D$ theo từng lớp | m11 |
| N15 | Chuyển confound #4 ra khỏi P5 — đo được bằng **re-evaluation**, không cần huấn luyện lại | m5 |
| N16 | Cân nhắc dùng pseudo-data **không trộn** (`use_Mixture=False`) cho nhánh CCFA — điều kiện lớp trên ảnh không trộn ít nhất là khái niệm xác định | M13 |

---

## 5. Lối đi bị bỏ qua — panel yêu cầu xét trước khi chốt B1

Devil's Advocate nêu, và không ghế nào bác:

**P1. Kiểm chứng lại cơ chế đề cương CŨ dưới feature skew.** Paper nguồn viết về **chính** các phần mở rộng bị coi là chết: *"so the mechanism's natural home is feature skew."* Chạy lại FedMix/C1/C1+C2 trên ma trận 2×2 ô B và ô D trả lời **đúng** câu Future Work, dùng **đúng** hạ tầng đang định xây, **giữ nguyên tên đề tài đã đăng ký**, và **không cần giải trình đổi hướng**. Đề xuất không nhắc tới một lần.

**P2. Đọc kết quả âm như sự hoàn thành mục tiêu đã đăng ký.** Mục tiêu tổng quát trong đề cương là *"Nghiên cứu cơ sở lý thuyết..."* — mục tiêu **nghiên cứu**, không phải cam kết cải thiện. §9.1 đã nêu đúng nguyên lý này, chỉ là không áp cho hướng cũ.

**P3. Đảo trọng số: C3 + C1 làm trục chính, C2 làm chương phụ.** Chính §9.2 thừa nhận cấu trúc này *"đã là một luận văn chặt chẽ và rủi ro thấp hơn nhiều"*, nhưng lịch vẫn dành ~7.5 GPU-ngày (tháng 7–10) cho CCFA.

**P4. Khai thác trực tiếp khoảng trống Ng–Jordan mà nguồn chỉ đích danh** — *"a discriminative head could win if trained on real features"*. So head huấn luyện trên đặc trưng thật **có nhãn thật, xuyên client** với trần LDA, trên checkpoint đã lưu. §8.1 ghi P4 là "~0.2 GPU-ngày (gần như miễn phí)". Rẻ nhất, gần lý thuyết nhất, và **đúng nghĩa "trained on"** mà CCFA hiện không thỏa (CCFA chỉ *compared on*).

**P5. Chạy kiểm soát cross-architecture TRƯỚC, không phải P8 tháng 10.** Nguồn cảnh báo *"a normalized backbone may reshape both the directional-bias and Gaussian-ceiling findings"*, và `resnet18_gn`/`resnet20_gn` dùng GroupNorm — đúng trường hợp cảnh báo. Nếu nó lật cơ chế, Chương 3, 5, 6 sụp **cùng lúc**. 1 GPU-ngày ở tháng 1 là bảo hiểm rẻ nhất trong toàn kế hoạch.

**P6. Nhánh hồi quy là nhánh ÍT bị bằng chứng phủ nhất, không phải nhiều nhất.** Cơ chế giải thích mọi negative là **thiên lệch ở classifier head dưới label skew**. Hồi quy không có head phân lớp và không có label skew theo nghĩa phạm trù ⇒ cơ chế đó **không áp dụng được**. §1.3 loại nó bằng lập luận từ sự vắng mặt.

---

## 6. Bên liên quan vắng mặt

- **ĐVCM / hội đồng xét duyệt đề cương** — bên duy nhất có thẩm quyền chấp nhận đổi tên đề tài
- **Phòng ĐTSĐH** — quản lý biểu mẫu đã ký; quy trình thực tế chưa được hỏi
- **Nhóm tác giả FedBR (Guo et al.)** — đối tượng của kiểm toán C3, trong đó có lỗi code mà §6.4 gọi là "đáng công bố". Không có mục nào về thông báo trước hay cơ hội phản hồi
- **Người bình duyệt paper hội nghị** — đã chấp nhận công trình **với** các nhãn "exploratory" và "not independent validation"
- **Bên cấp tài nguyên GPU** — ~40 GPU-ngày không gắn với nguồn chi trả nào
