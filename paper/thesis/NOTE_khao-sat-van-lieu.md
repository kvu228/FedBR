# Kết quả Phase A — Khảo sát văn liệu & Kiểm toán mã nguồn

**Ngày:** 16/09/2026 · **Phương thức:** 6 agent song song, ngữ cảnh tách biệt · **Đầu ra:** nền cho Chương 2, §5.2, và phát biểu lại đóng góp

> **Cảnh báo về "xác nhận độc lập":** ba agent (1, 3, 4) cùng đọc toàn văn FedMix và khớp nhau. Đó là **ba lần đọc cùng một tài liệu**, không phải ba bằng chứng độc lập. Giá trị nằm ở chỗ cả ba đều trích nguyên văn phương trình — kết luận chắc chắn về **nội dung tài liệu**, không phải về mặt thống kê.

---

## 1. Hai đóng góp phải phát biểu lại

### 1.1. C1 — ablation Taylor ĐÃ TỒN TẠI trong chính bài FedMix

**Phát hiện:** `NaiveMix` không phải baseline do repo FedBR thêm vào. Nó là **Eq. (1) của FedMix (ICLR 2021)**, xuất hiện trong **Bảng 1 — bảng kết quả chính** — và lặp lại ở Bảng 3, 4, 6, 7, 9, 10, 17, 18, Hình 3, cùng nền FedProx.

Hai phương trình nguyên văn:

```
ℓ_NaiveMix = (1−λ)·ℓ(f((1−λ)x + λx̄_g), y) + λ·ℓ(f((1−λ)x + λx̄_g), ȳ_g)
ℓ_FedMix   = (1−λ)·ℓ(f((1−λ)x),        y) + λ·ℓ(f((1−λ)x),        ȳ_g) + λ·(∂ℓ/∂x)·x̄_g
```

Số liệu Bảng 1 (FEMNIST@200 / CIFAR-10@500 / CIFAR-100@500):

| | FEMNIST | CIFAR-10 | CIFAR-100 |
|---|---|---|---|
| FedAvg | 85.3 | 73.8 | 50.4 |
| NaiveMix | 85.9 | 77.4 | 53.8 |
| FedMix | **86.5** | **81.2** | **56.7** |
| Global Mixup (oracle, vi phạm riêng tư) | 88.2 | 88.2 | 61.4 |

**Nhưng đây KHÔNG phải cô lập chặt.** Chuyển từ NaiveMix sang FedMix đổi **hai thứ cùng lúc**: (a) thêm số hạng Taylor, (b) rút $\bar x_g$ **khỏi đầu vào forward pass**. Lưới giai thừa đầy đủ có bốn ô, hai ô còn trống:

| Nhánh | Điểm đánh giá ℓ | Taylor | Trạng thái |
|---|---|---|---|
| **A** `NaiveMix` | $(1-\lambda)x + \lambda\bar x_g$ | ✗ | đã có |
| **B** `FedMix` | $(1-\lambda)x$ | ✓ | đã có |
| **C** | $(1-\lambda)x$ | ✗ | **chưa công bố** |
| **D** | $(1-\lambda)x + \lambda\bar x_g$ | ✓ | **chưa công bố** |

$B-C$ và $D-A$ cô lập số hạng Taylor ở hai điểm đánh giá; $A-C$ và $D-B$ cô lập phép trộn.
⚠️ Nhánh D cho $\bar x_g$ vào **hai lần** → là **nhánh chẩn đoán**, không phải phương pháp có nguyên tắc. Phải nói rõ.

**Bốn khe hở còn lại (đều xác minh được):**
1. **Nhánh C và D chưa từng công bố** — agent 3 kiểm tra cả thân bài lẫn phụ lục A–J qua ar5iv; agent 2 quét vét cạn **toàn bộ** bảng ablation (Bảng 1–7, Hình 3, App. D/Bảng 9, F/Bảng 10, H/Bảng 11–13, I/Bảng 14, J/Bảng 15–18).
2. **λ được tune riêng từng nhánh.** Bảng 8 (Phụ lục B): CIFAR-10 dùng λ=0.1 cho NaiveMix, λ=0.05 cho FedMix. ⚠️ **Agent 2 mâu thuẫn ở điểm này** — cho rằng Bảng 1 dùng λ chung. **Cần xác minh (V9).**
3. **Chưa ai tái lập độc lập.** FedBR có FedMix làm baseline nhưng **không báo cáo NaiveMix ở bất kỳ bảng nào**. FedAvP (NeurIPS 2024) dùng Taylor bậc nhất nhưng cho *policy gradient*, không có NaiveMix.
4. **Chưa từng chạy dưới feature skew.** Chỉ label skew (#lớp/client, Dirichlet) và quantity skew (FEMNIST).

**Luận cứ mạnh nhất cho khoảng trống — hai trục trực giao.** FedMix **Phụ lục D, Bảng 9** ablate **trục NGƯỢC LẠI**: giữ nguyên số hạng gradient, thay dữ liệu đưa vào nó.

| | FEMNIST | CIFAR-10 | CIFAR-100 |
|---|---|---|---|
| NaiveMix | 85.9 | 77.4 | 53.8 |
| Mixup w/ random noise | 86.1 | 77.9 | 51.2 |
| Mixup w/ local means | 85.5 | 73.5 | 51.0 |
| **FedMix** | **86.5** | **81.2** | **56.7** |

Nguyên văn: *"if averaged data for MAFL is substituted for randomly generated noise or locally generated images, it does not show the level of performance FedMix is able to show."*

> **Diễn giải:** FedMix đã chứng minh **$\bar x_g$ phải là trung bình toàn cục thật** (không thay được bằng nhiễu hay trung bình cục bộ), nhưng **chưa bao giờ chứng minh bản thân số hạng $\nabla_x\ell\cdot\bar x_g$ là cần thiết**. Hai trục trực giao; trục thứ hai còn bỏ trống.

**⚠️ Hai điểm BẤT LỢI phải trình bày trung thực** (nếu giấu, phản biện sẽ bắt được):

- **Bảng 10** (quét số local epoch): bài ghi nhận FedMix là *"a close second after NaiveMix"* ở một cấu hình — tức **có setting NaiveMix thắng**.
- **Bảng 17** (quét λ của NaiveMix, CIFAR-10): **79.5 / 79.9 / 80.6 / 29.8** tại λ = 0.05 / 0.1 / 0.2 / 0.5. Đỉnh của NaiveMix (**80.6** tại λ=0.2) **rất sát** FedMix (81.2), và cả hai sụp đổ ở λ=0.5. Nghĩa là **khoảng cách hẹp lại đáng kể khi λ được tinh chỉnh riêng cho từng nhánh** — con số headline 77.4 → 81.2 **nói quá giá trị của số hạng Taylor**.

**Văn liệu mixup ngoài FL — đã quét, đều KHÔNG có ablation này:**
- Zhang, Deng, Kawaguchi, Ghorbani, Zou, *"How Does Mixup Help With Robustness and Generalization?"*, ICLR 2021, arXiv:2010.04819 — kiểm chứng xấp xỉ Taylor **như một tổng thể**, không ablate từng số hạng.
- Carratino, Cissé, Jenatton, Vert, *"On Mixup Regularization"*, JMLR 23(325):1–31, 2022, arXiv:2006.06049 — bốn khối thí nghiệm, **không có dòng leave-one-term-out nào**.
  ⚠️ **Một "gần trúng" cần xử lý cẩn thận:** Carratino §5 nêu họ *"dropped the term R₂(f) in the regularization since it empirically induces numerical instability"*. Đây là số hạng **bậc HAI**, bị bỏ vì lý do **số học**, bên trong baseline của chính họ — **KHÔNG phải ablation có kiểm soát**. Nếu trích, trích như một *ghi chú cài đặt*; trình bày sai là bị bắt ngay.

**Phát biểu C1 mới:**
> Tái lập độc lập đối chứng FedMix ↔ NaiveMix ở λ đồng nhất với nhiều seed và CI, bổ sung hai nhánh chưa công bố (C, D) để cô lập chặt số hạng Taylor tại điểm đánh giá cố định, và mở rộng đối chứng sang chế độ feature skew.

**Việc khép kín bắt buộc:** cả ba agent đều khuyến nghị tra **citation graph của FedMix** (Semantic Scholar / Google Scholar) — đây là cách duy nhất biến "không tìm thấy" thành phát biểu đủ mạnh.

---

### 1.2. C2 — NIID-Bench ĐÃ tách feature khỏi label skew

**Phát hiện:** NIID-Bench (Li, Diao, Chen, He — ICDE 2022) có **6 chiến lược phân hoạch**, và **noise-based feature skew được thiết kế có chủ ý để feature skew là biến duy nhất**. Nguyên văn: *"We first divide the whole dataset into multiple parties randomly and equally. For each party, we add different levels of Gaussian noise"* — tức phân phối nhãn giữa các bên là **IID**. FCUBE cũng giữ nhãn cân bằng bằng cách gán các khối đối xứng qua gốc.

NIID-Bench **chạm tới cả bốn ô** của ma trận 2×2, kể cả ô "mixed" (label-dir + noise), kết quả ở Bảng V.

> ⛔ **CẤM viết "chưa ai tách feature khỏi label skew".** Điều đó SAI.

**Năm khoảng trống thật (agent 5 xác minh từ toàn văn):**

1. **Ô "mixed" chỉ là MỘT ĐIỂM, không phải một mặt phẳng.** Chỉ CIFAR-10, 10 bên, hai tổ hợp. Không có lưới β × σ ⇒ **không biết hai loại skew cộng tính hay tương tác**.
2. **Không có hiệu chuẩn độ nghiêm trọng.** β và σ không cùng đơn vị; NIID-Bench không đề xuất cách làm "mức feature skew" so sánh được với "mức label skew". **Đây là điều kiện tiên quyết để ma trận 2×2 có nghĩa nhân quả — và là đóng góp phương pháp luận mạnh nhất còn trống.**
3. **Hai loại skew bị buộc vào các dataset khác nhau.** Feature skew "thật" chỉ có ở FEMNIST/FCUBE; không thể lấy FEMNIST rồi thêm label skew có kiểm soát. Ô (feature skew thật × label skew có kiểm soát) **không tồn tại**.
4. **Nhiễu Gauss là feature skew yếu về ngữ nghĩa** — nhiễu cộng độc lập pixel, không phụ thuộc lớp, không phụ thuộc nội dung. Nó đo *nhiễu cảm biến*, không đo *dịch chuyển miền*.
5. **Ô mixed chỉ đo 4 thuật toán:** FedAvg, FedProx, SCAFFOLD, FedNova. **MOON, FedDyn, FedBR, FedMix vắng mặt.** Vì MOON/FedBR/FedMix can thiệp ở tầng *biểu diễn* còn SCAFFOLD/FedNova ở tầng *optimizer*, giả thuyết "hai họ phản ứng khác nhau theo ô" **chưa từng được kiểm định**.

**So sánh benchmark khác:** LEAF, FLamby, Flower không tách (skew trọn gói tự nhiên). FedBN tách hẳn về phía feature nhưng **không biến thiên label skew**. FedRC (ICML 2024) tách ba loại shift nhưng **gán ngẫu nhiên độc lập cho từng client, không phải thiết kế factorial**.

**Phát biểu C2 mới:**
> Thiết kế factorial 2×2 {label skew} × {feature skew} với **độ nghiêm trọng được hiệu chuẩn giữa hai trục**, chạy trên họ mean-augmented (FedMix/NaiveMix) vốn vắng mặt trong khảo sát mixed-skew của NIID-Bench.

---

## 2. Quy ước Dirichlet — vấn đề nghiêm trọng, ảnh hưởng trực tiếp tới báo cáo số liệu

Văn liệu dùng **hai quy ước với cùng chữ cái**, và chúng **lấy mẫu trên hai trục khác nhau**:

| | Quy ước B (Hsu et al. 2019) | Quy ước A (NIID-Bench 2022) |
|---|---|---|
| Công thức | $q \sim \text{Dir}(\alpha\cdot p)$ | $p_k \sim \text{Dir}_N(\beta)$ |
| α/β là | nồng độ **TỔNG** | nồng độ **MỖI THÀNH PHẦN** |
| Lấy mẫu | mỗi **client**, trên các **LỚP** | mỗi **lớp**, trên các **BÊN** (chuyển vị!) |
| Ai theo | FedRC, dòng "LDA partition" | MOON, hệ sinh thái Xtra-Computing |

Với CIFAR-10 (10 lớp, 10 bên): `α=0.5` (Hsu) ⟺ mỗi thành phần **0.05**; `β=0.5` (NIID-Bench) ⟺ mỗi thành phần **0.5**. **Cùng ký hiệu "0.5", khác nhau 10 lần.**

### Và repo dùng CẢ HAI quy ước trong cùng một file

| Vị trí | Mã | Quy ước | Nồng độ mỗi thành phần |
|---|---|---|---|
| `datasets.py:132–133` (CIFAR-100) | `p = torch.ones((len,))` — **chưa chuẩn hoá** | **A** | **0.1** (tổng = 10.0 trên 100 lớp) |
| `datasets.py:317–325` (CIFAR-10) | `p = classes_by_index_len / sum(...)` — **đã chuẩn hoá** | **B** | **0.01** (tổng = 0.1 trên 10 lớp) |

**Cùng hằng số `0.1` trong cùng file, nhưng CIFAR-10 nghiêng hơn CIFAR-100 khoảng 1000× về nồng độ mỗi thành phần.** Thêm nữa, việc cắt `p[available]` khi lớp cạn dần làm **tổng nồng độ thay đổi động trong quá trình phân hoạch**.

**Quy tắc bắt buộc cho luận văn:** mọi lần báo cáo Dirichlet phải nêu bộ ba **(vector nồng độ đầy đủ, trục lấy mẫu, số thành phần)**, kèm dòng quy đổi $\alpha_{\text{Hsu}} = N \cdot \beta_{\text{NIID-Bench}}$ khi $p$ đều.

---

## 3. Feature skew phụ thuộc lớp — khoảng trống sạch nhất

**Mọi benchmark FL chuẩn dùng biến đổi ĐỘC LẬP với lớp:**

| Cách mô phỏng | Công trình | Phụ thuộc lớp? |
|---|---|---|
| Nhiễu Gauss cộng | NIID-Bench | ✗ |
| Phân vùng đặc trưng tổng hợp (FCUBE) | NIID-Bench | ✗ (cố ý giữ nhãn cân bằng) |
| Nguồn/người viết thật | FEMNIST, LEAF | ✗ (tương quan ngẫu nhiên, không kiểm soát) |
| Đa miền thật | FedBN (Digits-Five, DomainNet) | ✗ |
| Corruption chuẩn hoá | FedRC (CIFAR-10-C, 20 style) | ✗ |
| **Xoay ảnh** | FedBR (RotatedMNIST), DomainBed | ✗ |

**Chỉ hai tiền lệ phụ thuộc lớp, và cả hai đều NGOÀI hệ sinh thái benchmark FL:**

- **ColoredMNIST** (Arjovsky et al., IRM 2019) — màu **sinh từ nhãn**, cường độ tương quan màu–nhãn thay đổi theo client. Đúng định nghĩa dịch chuyển $P(x|y)$ khác nhau giữa client. **Repo đã có sẵn lớp `ColoredMNIST` tại `datasets.py:582` với 15 environment.**
- **Rieger, Høegh, Hansen (2020)** — nhúng → PCA → K-means **theo từng lớp** → mỗi client nhận một bộ tâm cụm. Nguyên văn động cơ: *"clients express a particular class differently ... features that are (even class conditionally) non-IID."*

**Ý nghĩa:** phát hiện này hội tụ với cảnh báo của ghế Domain ở vòng bình duyệt — phép xoay trong `RotatedCIFAR10` là nhiễu **class-shared** (một $q_i$ dùng chung cho 10 lớp), nên phần "có điều kiện lớp" gần như không thêm bậc tự do nhận dạng nào. Giờ ta biết đây là **thuộc tính chung của benchmark FL**, không riêng RotatedCIFAR10.

---

## 4. Kiểm toán mã nguồn — C3 được củng cố mạnh

### 4.1. Ba phát hiện đủ sức làm trọng tâm §5.2

| # | Phát hiện | Neo mã | Neo paper |
|---|---|---|---|
| **N1** | **τ dùng làm hệ số NHÂN, không phải CHIA.** `exp(sim(e1,e2) * tau1)` vs Eq. (5)(6) `exp(sim(...)/τ)`. Với τ=2.0 nhiệt độ hiệu dụng là **0.5** — lệch 4×. **Bằng chứng nội tại trong chính paper:** Bảng 11 có hàng τ₂ = 0, *không xác định* dưới phép chia nhưng hợp lệ dưới phép nhân ($e^0=1$) | `algorithms.py:1136, 1150` | tr. 6, Eq. (5)(6); Bảng 11 tr. 16 |
| **N2** | **μ của FedProx bị ghi đè cứng thành 0.1 ngay đầu `step()`**, xoá giá trị constructor ở mỗi bước. Hparam `fedprox_mu`, knob Makefile, và lưới quét {0.001, 0.01, 0.1} của paper — **cả ba vô hiệu**. Cùng kiểu lỗi ở `FedCM.step` và `SCAFFOLD_OPT.step` | `algorithms.py:222` (và `106`, `298`) | tr. 13, App. A |
| **N10** | **Pseudo-data dựng MỘT LẦN, nhưng mặc định của paper là MỖI VÒNG.** Nhánh dựng-mỗi-vòng bị comment. Mã phát hành **không thể** tạo cấu hình đã sinh ra Bảng 1; ablation Hình 6(b) không tái lập được | dựng: `train_fed.py:415–423`; comment: `520–527` | tr. 7 |

### 4.2. Bốn cơ chế độc lập làm suy yếu baseline

| # | Phát hiện |
|---|---|
| **N3** | **Mô hình local vòng trước của Moon không bao giờ được cập nhật** — lệch tên thuộc tính (`previous_featurizer` gán vào `train_fed.py:513`, `previous_feature` đọc ra `algorithms.py:650`). Là mạng khởi tạo ngẫu nhiên **đóng băng suốt 1000 vòng**. Hàng "Moon" của Bảng 1 không phải Moon |
| **N14** | **FedBR, DANN, FedProx không có đường nào bật momentum**; mọi lớp con `ERM` mặc định 0.9 ⇒ **optimizer không đồng nhất giữa các baseline ngay trong mã phát hành**. Bảng 9 yêu cầu momentum 0.9 — FedBR không thể có |
| **N8** | **GroupDRO LUÔN áp Mixup** bất kể `--use_Mixup` ⇒ hàng "GroupDRO" thực chất là GroupDRO+Mixup |
| **N24** | **DANN chỉ nhận một nửa số bước cập nhật** cho featurizer/classifier (lịch xen kẽ `update_count % 2`) — 25 000 so với 50 000 |

> ⚠️ **Giới hạn bắt buộc nêu:** mã cho thấy baseline bị suy yếu, nhưng **không có cơ sở lượng hoá** mỗi cơ chế đóng góp bao nhiêu điểm. **Cấm** viết câu nào hàm ý đã đo được.

### 4.3. Phát hiện đe doạ trực tiếp thí nghiệm lõi

**`FedMix.update` lấy gradient của `loss1`, mà `loss1` đã chứa $(1-\lambda)$:**

```python
loss1 = (1 - λ) * F.cross_entropy(...)
grad  = autograd.grad(loss1, all_x, create_graph=True)[0]   # = (1-λ)·∂CE/∂x
loss3 = torch.sum(λ * grad * all_augmentation_x) / n         # = λ(1-λ)·∂CE/∂x·x̄
```

Thực thi là $\lambda(1-\lambda)\nabla\ell\cdot\bar x_g$, không phải $\lambda\nabla\ell\cdot\bar x_g$. Ở λ=0.1 lệch hệ số 0.9. Thêm nữa, code **chỉ** lấy gradient của số hạng `y`, không của số hạng `ȳ_g`.

**⛔ Phải giải quyết trước khi chạy E1.** Toàn bộ C1 đo `loss3`.

### 4.4. Khác

- **N16:** 10 mô hình local **không** được khởi tạo từ mô hình toàn cục; vòng đồng bộ là no-op. Hàng "Local" của Bảng 1 là 10.00/14.67/1.31 — **đúng mức ngẫu nhiên 1/C ở cả ba dataset**. *(Suy luận, chưa kết luận — cần chạy `make run-local` để xác nhận.)*
- **N20:** `SCAFFOLD_algo` **không chạy được** (`TypeError`), vắng mặt trong `ALGORITHMS`. Bảng 13/14 hàng SCAFFOLD không tái lập được.
- **N23:** **VHL căn chỉnh LOGIT chứ không phải ĐẶC TRƯNG** (`self.predict(x)` trả logit 10 chiều). Paper tr.13 nói "for feature alignment".
- **N15:** **`RotatedCIFAR100` không hề gọi `dataset_transform`** ⇒ CIFAR100 **không được xoay** bất chấp tên lớp; 10 env test giống hệt nhau. *(Agent 5 báo cáo một lỗi khác ở cùng vùng — `angle` bị ghi đè bằng `np.random.randint(0,180)` sau khi lấy mẫu Dirichlet. Hai claim cần đối chiếu — xem §6.)*

### 4.5. Đính chính cho `REPRODUCE.md`

1. **§7 nói bản vá `add_` "đã được thay"** — 5 vị trí vẫn dùng dạng cũ (`algorithms.py:129, 148, 245, 263, 321`). Vẫn chạy trên torch 2.6.0, chỉ cảnh báo deprecated.
2. **`M = 10` hardcode ở BA chỗ** (`train_fed.py:41, 53, 62`), và **paper không bao giờ công bố M** ⇒ mô tả lại là *thiếu thông tin trong paper*, không phải mâu thuẫn.
3. **Dirichlet góc xoay không phải lỗi** — `Dir(α·p)` đúng là định nghĩa LDA của Hsu et al. mà paper trích. Trình bày là **ký hiệu mơ hồ**, kèm hệ quả: mỗi client thực tế chỉ xoay theo **1–2 góc**.
4. **`CleanCIFAR10` 10 env test giống nhau là khiếm khuyết của BẢN TÁI LẬP**, không phải của tác giả.
5. **§4 hướng dẫn quét `fedprox_mu` không hoạt động** (do N2).
6. **§2 ghi "transferred once at the start"** — đúng với mã, **sai với mặc định của paper** (do N10).

---

## 5. Cạm bẫy trích dẫn

| Cạm bẫy | Chi tiết |
|---|---|
| **FedMix có 3 thực thể trùng tên** | (1) Yoon et al., ICLR 2021 — *đối tượng nghiên cứu*; (2) Wicaksana et al., IEEE TMI 2023 — "Mixed Supervised", **hoàn toàn không liên quan**; (3) — |
| **FedFA có 2 bài khác nhau** | Zhou & Konukoglu, ICLR 2023 (*Feature Augmentation*, class-agnostic) vs Zhou/Zhang/Tsang, IEEE TMC 2024 (*Feature Anchors*, class-conditional). Đặt tên riêng: **FedFA-Aug** / **FedFA-Anchor** |
| **FedDecorr KHÔNG phải "căn chỉnh"** | Nó ép ma trận tương quan cục bộ về đơn vị (decorrelation), **không so client với global**. Phải chủ động phân biệt |
| **SphereFed, Fed3R là bậc 2 KHÔNG điều kiện lớp** | Gram không tâm hoá trên toàn bộ mẫu. **Không giả định đặc trưng mỗi lớp là Gaussian.** Xếp chung với CCVR sẽ hỏng lập luận ở §3.5 |
| **FedCOF đổi tiêu đề giữa các bản arXiv** | Dùng tiêu đề bản NeurIPS 2025 (*"...Training-free Federated Learning"*) |
| **Venue chưa xác minh** | Mime, FedCM (dblp chỉ ghi CoRR) → trích là arXiv preprint. FedPFT → preprint. LEAF, FedML, Flower, Hsu et al. → arXiv/workshop, không phải hội nghị chính |

---

## 6. Việc xác minh thủ công — theo thứ tự ưu tiên

| # | Việc | Vì sao chặn |
|---|---|---|
| **V1** | **Đọc Eq. (5) của Yoon et al. và quyết định:** `loss3` nên là $\lambda\nabla\ell\cdot\bar x_g$ hay $\lambda(1-\lambda)\nabla\ell\cdot\bar x_g$? Có cần gradient của số hạng `ȳ_g` không? | Chặn E1 — toàn bộ C1 đo số hạng này |
| **V2** | **Tra citation graph của FedMix** (Semantic Scholar / Google Scholar) cho nhánh C, D | Khép kín phát biểu C1 ở §2.6 |
| **V3** | **Đối chiếu hai claim mâu thuẫn về `RotatedCIFAR100`**: không gọi `dataset_transform` (agent 6) vs `angle` bị ghi đè bởi `np.random.randint(0,180)` (agent 5) | Ảnh hưởng §5.2; có thể cả hai đều đúng |
| **V4** | `arXiv:2603.04062` "FedCova" — tác giả/venue chưa xác minh; abstract có "class feature covariances" | Related work bắt buộc nếu đúng |
| **V5** | **Phụ lục C.5 của FedDecorr** — "another type of heterogeneity"; nếu là feature skew thì §2.3.5 phải sửa | Chương 2 |
| **V6** | **CCVR: hiệp phương sai đầy đủ hay đường chéo?** Nếu đường chéo thì không thực sự căn chỉnh cấu trúc bậc hai | Chương 2, §3.5 |
| **V7** | Đối chiếu số liệu Bảng 1 FedMix từ ar5iv với **bản PDF ICLR chính thức** | Mọi con số trong Chương 2 |
| **V8** | Chạy `make run-local` 1000 vòng — xác nhận hay bác bỏ giả thuyết N16 | §5.2 |
| **V9** | **Bảng 1 của FedMix dùng λ CHUNG hay λ RIÊNG từng nhánh?** Agent 1 (dẫn Bảng 8, Phụ lục B) nói riêng: NaiveMix 0.1, FedMix 0.05. Agent 2 nói chung. Quyết định liệu con số headline có bị confound hay không | C1, §5.3 |
| **V10** | **Mở thủ công OpenReview `Ogga20D2HO-`** (WebFetch + cả hai API đều trả 403 `ChallengeRequiredError`). Tìm từ khoá "third term", "gradient term", "ablation", "necessity" | **Rủi ro duy nhất còn lại có thể lật ngược C1** — nếu phản biện ICLR đã yêu cầu đúng ablation này và tác giả trả lời trong rebuttal |
| **V11** | Repo `github.com/wizard1203/VHL` — xác nhận trực tiếp con số 2.000 / 20.000 mẫu ảo (hiện chỉ có nguồn gián tiếp qua FedBR App. A) | Chương 2 §2.3.2 |
| **V12** | Danh sách tác giả FedNTD — arXiv ghi 5, một nguồn thứ cấp ghi 4 | `refs.bib` |

### Quy tắc viết bằng chứng phủ định — **bắt buộc**

Bằng chứng phủ định có **hai mức độ mạnh khác nhau**, phải viết đúng mức:

| Mức | Phạm vi | Cách viết |
|---|---|---|
| **Mạnh** | Quét vét cạn **toàn bộ** bảng ablation của FedMix | "Bài FedMix không báo cáo biến thể này ở bất kỳ bảng nào (đã đối chiếu Bảng 1–7, Hình 3, Phụ lục D, F, H, I, J)." |
| **Yếu hơn** | ~1.000 bài trích dẫn FedMix **KHÔNG** được duyệt vét cạn — chỉ tìm theo từ khoá và theo một số nhánh đã nêu | "**Trong phạm vi khảo sát của chúng tôi**, chưa tìm thấy công trình nào…" |

⛔ **CẤM** viết "chưa có công trình nào…" cho mức thứ hai.

---

## 7. Cập nhật bắt buộc cho `00_outline.md`

| Mục | Thay đổi |
|---|---|
| §1.3 C1 | Phát biểu lại theo §1.1 — **replication + 2 nhánh mới**, không phải "cô lập lần đầu" |
| §1.3 C2 | Phát biểu lại theo §1.2 — **hiệu chuẩn độ nghiêm trọng + họ mean-augmented ở ô mixed** |
| §1.3 C3 | Mở rộng: N1, N2, N10 làm trọng tâm; thêm nhóm "baseline bị suy yếu"; thêm mâu thuẫn quy ước Dirichlet |
| §2 IRON RULES | **Thêm IR#11:** cấm viết "chưa ai tách feature khỏi label skew" (NIID-Bench có tách). **Thêm IR#12:** mọi báo cáo Dirichlet phải nêu bộ ba (nồng độ, trục, số thành phần) |
| §2.4 bảng | Tách cột "Bậc thống kê" thành **`Bậc truyền`** và **`Bậc khai thác`** (vì FedCOF) |
| §3.2 P-list | Thêm: sửa N2 (FedProx μ), sửa N3 (Moon), thống nhất momentum (N14), quyết định cấu hình pseudo-data (N10) |
| §5.1 | Ghi rõ **cấu hình FedBR baseline nào** được dùng (một lần vs mỗi vòng) |
| §6 mốc | Thêm **T0.5: giải quyết V1 trước khi chạy E1** |