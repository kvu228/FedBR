# Kế hoạch rút gọn — dưới 8 tuần

**Ngày lập:** 16/09/2026 · **Ràng buộc:** < 8 tuần tới hạn · **Nguyên tắc chi phối:** chỉ đủ thời gian để sai **một lần**

> Thay thế §5 và §6 của `00_outline.md`. Dàn bài chương giữ nguyên.

---

## 1. Thay đổi cốt lõi trong cách đặt câu hỏi

**RQ1 chuyển từ kiểm định giả thuyết sang ƯỚC LƯỢNG.**

Lý do: Bảng 17 của FedMix cho thấy NaiveMix ở λ tinh chỉnh đạt **80.6** so với FedMix **81.2** — hiệu ứng thật ở λ khớp có thể chỉ **~0.6 pp**. Với $s \approx 1.2$, không có số seed khả thi nào phân giải được mức đó.

| $n$ seed | Nửa rộng CI 95% |
|---|---|
| 5 | 1.49 pp |
| **8** | **1.00 pp** |
| 12 | 0.76 pp |
| 25 | 0.50 pp |

**Phát biểu lại RQ1:**
> $\Delta_{\text{Taylor}}$ **lớn bao nhiêu** ở λ khớp, với khoảng tin cậy?

Kết luận dạng: *"$\Delta_{\text{Taylor}} = 0.4 \pm 1.0$ pp ở λ khớp, tức bị chặn dưới xa con số +3.8 pp được báo cáo ở λ không khớp."*

Đây **là** một kết quả — và là kết quả kiểu kiểm toán confound, đúng thế mạnh đã được chứng minh của tác giả. Thiết kế phải được xây **cho** kết cục này, không phải hy vọng tránh nó.

**Hệ quả:** báo cáo **CI, không phải p-value**. Nhánh null dùng TOST với biên định trước ±1.5 pp ($n{=}8$).

---

## 2. Cắt gì

| Hạng mục | Quyết định | Lý do |
|---|---|---|
| Ô A (IID) đầy đủ | **Cắt** — giữ **một** run FedAvg làm mốc neo | Cần mốc cho trục x, không cần cả bộ nhánh |
| Ô D (cả hai skew) | **Cắt hoàn toàn** | Không kết luận được về tương tác nếu không có lưới; nêu vào hạn chế |
| **Nhánh D** (giữ trộn + thêm Taylor) | **Cắt** | Là nhánh chẩn đoán, không phải phương pháp. Bỏ không mất luận cứ |
| Thí nghiệm hồi quy (E6) | **Cắt → chỉ giữ lý thuyết §4.6** | ⚠️ Đây là thay đổi so với lựa chọn B trước đó. Lập luận cơ chế (hồi quy không có classifier head ⇒ lời giải thích không áp dụng được) vẫn trung thành với đề cương, vì đề cương yêu cầu **nghiên cứu** cơ chế. Thí nghiệm không vừa |
| CIFAR-100 | **Cắt** | |
| Cross-architecture (E4) | **Tuỳ chọn** — chỉ chạy nếu còn thời gian ở tuần 6 | |
| Sửa N2 (FedProx μ), N3 (Moon) | **Không cần sửa** | Bốn nhánh cuối không dùng FedProx/MOON làm baseline ⇒ hai mục này thành **phát hiện C3 thuần tuý**, không phải việc chặn |
| P-7 (tách `partition_seed`) | **Cắt** | |
| Chẩn đoán mở rộng (P-8) | **Thu về tối thiểu** | norm head theo lớp + worst-class recall, hậu nghiệm, gần như miễn phí |

**Giữ tuyệt đối:**
- **Nhánh C** (bỏ `loss3`, giữ điểm đánh giá) — phần chưa ai công bố. Bỏ là mất C1.
- **Quét λ** — không còn tuỳ chọn. Không quét thì kết quả bị confound **đúng như bài gốc**.

---

## 3. Thiết kế cuối

### 3.1. Bốn nhánh

| Nhánh | Mục tiêu | Trạng thái mã |
|---|---|---|
| **FedAvg** | tham chiếu + mốc trục x | có sẵn |
| **A** `NaiveMix` | trộn chính xác, không Taylor | có sẵn |
| **B** `FedMix` | xấp xỉ Taylor đầy đủ | có sẵn |
| **C** `FedMixNoTaylor` | $(1-\lambda)x$ + `loss2`, **bỏ** `loss3` | **~10 dòng mới** |

### 3.2. Năm điểm trên đường độ nghiêm trọng (không phải "ô")

Bỏ khung "ma trận 2×2". Thay bằng **các điểm trên một trục chung**: độ suy giảm của FedAvg so với IID.

| Điểm | Cấu hình | Số seed |
|---|---|---|
| **P0** | IID (mốc neo) | 3 (chỉ FedAvg) |
| **P1** | Feature skew, $\alpha_{\text{rot}}$ = mặc định (≈0.1/thành phần) | **8** ← headline |
| **P2** | Feature skew, $\alpha_{\text{rot}}$ = 1.0 | 3 |
| **P3** | Feature skew, $\alpha_{\text{rot}}$ = 10.0 | 3 |
| **P4** | Label skew, $\alpha_{\text{label}}$ = 0.1 (giá trị đã đăng ký) | **8** ← headline |

**Trục x chung = độ suy giảm accuracy của FedAvg so với P0.** Miễn phí (FedAvg chạy ở mọi điểm). Mỗi cấu hình cho một điểm $(\text{FedAvg drop}, \Delta_{\text{Taylor}})$, và cả hai loại skew rơi lên **cùng một trục** — không cần hiệu chuẩn phân phối.

⚠️ **Giới hạn phải nêu thẳng trong luận văn:** FedAvg-drop trộn lẫn "bài toán khó đến đâu" với "FedAvg hỏng theo cách nào". Đây là **căn chỉnh vận hành**, không phải căn chỉnh phân phối. Hiệu chuẩn độ nghiêm trọng thật → Chương 6.

### 3.3. λ — hai con số, và khoảng cách giữa chúng là phát hiện

Quét λ ∈ {0.05, 0.1, 0.2} (khớp Bảng 17 của FedMix; λ=0.5 đã biết là sụp đổ).

Báo cáo **cả hai**:
- **Δ ở λ KHỚP** (mọi nhánh cùng λ) → phép cô lập sạch, trả lời RQ1
- **Δ ở λ TỐT NHẤT của từng nhánh** → so sánh công bằng giữa phương pháp

**Khoảng cách giữa hai con số chính là confound** mà bài gốc mắc phải. Không tốn gì thêm vì quét đã cho cả đường cong.

---

## 4. Lịch 8 tuần

| Tuần | GPU | Viết |
|---|---|---|
| **1** | Code (§5) — không dùng GPU | Ch.2 (§2.3.6, §2.5 viết được ngay) |
| **2** | **Scouting λ** khởi động | Ch.2 phần còn lại + Ch.3 §3.1–3.3 |
| **3** | **Main runs** khởi động | Ch.3 §3.4–3.6 |
| **4** | Main runs chạy tiếp | Ch.4 |
| **5** | Đệm chạy lại / 1000 vòng nếu kịp | Ch.1 + Ch.5 §5.1–5.2 |
| **6** | E4 nếu còn thời gian; chẩn đoán hậu nghiệm | Ch.5 §5.3–5.5 |
| **7** | — | Ch.5 §5.9 + Ch.6 |
| **8** | — | Hoàn thiện, tóm tắt, mục lục, rà soát |

**Mốc chặn tuần 4:** nếu main runs chưa xong, cắt P2/P3 (đường cong $\alpha_{\text{rot}}$) và giữ chỉ P1/P4 làm hai điểm.

---

## 5. Việc lập trình — tuần 1, không dùng GPU

| # | Việc | Ước lượng |
|---|---|---|
| **P-a** | Lớp `FedMixNoTaylor` — sao `FedMix`, bỏ `grad`/`loss3` | ~10 dòng |
| **P-b** | Target Makefile: `run-naivemix`, `run-fedmix-notaylor` | ~10 dòng |
| **P-c** | Cờ `--rot_alpha` (`datasets.py:438`) | ~3 dòng |
| **P-d** | Dataset feature-skew-thuần: phân hoạch nhãn đồng đều, giữ `rotate_dataset` | ~30 dòng |
| **P-e** | **Bộ môi trường test CHUNG cho mọi điểm** (sửa `CleanCIFAR10`) — bắt buộc, vì so sánh xuyên điểm | ~5 dòng |
| **P-f** | *(tuỳ chọn)* checkpoint best-so-far | ~5 dòng |

**⛔ Chặn trước tất cả — V1:** đọc Eq. (5) của Yoon et al. và quyết định `loss3` nên là $\lambda\nabla\ell\cdot\bar x_g$ hay $\lambda(1-\lambda)\nabla\ell\cdot\bar x_g$ (mã hiện tại là vế sau). Toàn bộ C1 đo số hạng này.

**V10 (song song, vài phút):** mở thủ công `openreview.net/forum?id=Ogga20D2HO-`, tìm "third term", "gradient term", "ablation". Rủi ro duy nhất còn lại có thể lật ngược C1.

---

## 6. Ngân sách tính toán

Đơn giá: nhánh loại ERM @300 vòng ≈ **1.8 h**.

| Giai đoạn | Số run | GPU-giờ | GPU-ngày | Ngày lịch (2 GPU) |
|---|---|---|---|---|
| Scouting λ: 3 nhánh × 3 λ × 2 điểm headline × 3 seed | 54 | 97 | 4.0 | **2.0** |
| Headline: 4 nhánh × 2 điểm (P1,P4) × 8 seed | 64 | 115 | 4.8 | **2.4** |
| Đường cong: 4 nhánh × 3 điểm (P0,P2,P3) × 3 seed | 36 | 65 | 2.7 | **1.4** |
| **Cộng** | **154** | **277** | **11.5** | **5.8** |
| *(tuỳ chọn)* 1000 vòng, 1 điểm × 4 nhánh × 3 seed | 12 | 66 | 2.8 | 1.4 |
| *(tuỳ chọn)* E4 backbone `resnet20_gn`, 1 điểm × 4 nhánh × 3 seed | 12 | 22 | 0.9 | 0.5 |

**Lõi ≈ 6 ngày lịch trên 2 GPU.** Trong 8 tuần, còn thừa cho **hai lần chạy lại** — vượt ngưỡng "sai một lần" đã đặt ra.

> ⚠️ Chạy `make probe` trên đúng card vừa thuê trước khi cam kết. Đơn giá trên lấy từ `REPRODUCE.md` §6.

---

## 7. Cái gì mất đi — ghi vào Ch.1 §1.2.4

- **Không có ô (label skew × feature skew đồng thời)** ⇒ không kết luận được về tương tác giữa hai loại skew
- **Không có nhánh D** ⇒ số hạng Taylor chỉ được cô lập ở **một** điểm đánh giá, không phải hai
- **Không có thí nghiệm hồi quy** ⇒ §4.6 là lập luận cơ chế, không phải bằng chứng thực nghiệm
- **Không có CIFAR-100** ⇒ không kiểm chứng ở số lớp cao
- **Cross-architecture là tuỳ chọn** ⇒ nếu không chạy, giả thiết "phát hiện độc lập với backbone" **chưa được kiểm tra**
- **Checkpoint vòng cuối, không phải vòng tốt nhất** ⇒ chẩn đoán cơ chế nhiễu hơn; không ảnh hưởng bảng accuracy (tính từ `results.jsonl`)

---

## 8. Ba đóng góp — bản cuối

**C1** — ba thành phần, xếp theo mức độ **độc lập với tuyên bố tính mới** (chi tiết: `02_chuong2.md` §2.6.3):

- **(a)** Tái lập độc lập FedMix ↔ NaiveMix trên nền tảng thứ hai, nhiều seed, báo cáo CI → giá trị nằm ở *chính việc tái lập*
- **(b)** Đo ở **λ khớp** + báo cáo cả λ tối ưu riêng từng nhánh → *kiểm toán confound*
- **(c)** Nhánh C (3.7) cô lập chặt + mở rộng sang feature skew → phần **duy nhất** cần tính mới

⚠️ **Nguyên tắc phòng thủ:** (a) và (b) phải đứng vững độc lập. Nếu V10 (OpenReview) cho thấy nhánh C đã từng được thực hiện, (c) chuyển thành **xác nhận độc lập** và C1 không suy suyển. **Không viết Chương 1 hay Chương 6 theo cách để C1 treo vào (c).**

**C2.** Đo họ **mean-augmented dọc theo trục độ nghiêm trọng skew** — họ này vắng mặt trong khảo sát mixed-skew của NIID-Bench (chỉ có FedAvg, FedProx, SCAFFOLD, FedNova). Báo cáo gain như **đường đặc tuyến vận hành** trên trục FedAvg-degradation chung.

**C3.** Kiểm toán tái lập FedBR: ba phát hiện trọng tâm (τ nhân thay vì chia; μ FedProx bị ghi đè; pseudo-data dựng một lần thay vì mỗi vòng), bốn cơ chế làm suy yếu baseline, mâu thuẫn quy ước Dirichlet trong cùng một file. **Phần lớn đã hoàn thành.**

⛔ **Không tuyên bố tính mới nào chưa qua kiểm chứng của `01_ket-qua-khao-sat-van-lieu.md` §6.**