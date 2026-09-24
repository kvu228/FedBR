# INDEX — Mã nguồn và kết quả thực nghiệm dùng cho luận văn

> **Vai trò.** Chỉ mục để agent và người viết tra ngược mọi con số, cấu hình và đoạn mã mà luận văn dựa vào, không phải đọc lại cả hai kho mã. Lập 24/09/2026 từ việc đọc trực tiếp mã, cấu hình, `paper/conference/main.tex` và các tệp kết quả thô. Mọi đường dẫn `file:dòng` được đọc tại commit ghi ở §0. Commit mới hơn có thể làm lệch số dòng; khi lệch thì tra theo tên hàm.
>
> **Quy ước.** `[FL]` = kho Flower `uit-msc-dp-adaptive-fedmix`. `[BR]` = kho FedBR/DomainBed `FedBR`. `[DP]` = mã tham chiếu DevPranjal. Đường dẫn tương đối tính từ gốc kho tương ứng.

---

## 0. Bốn nguồn và cách tra

| Ký hiệu | Đường dẫn | Commit đã đọc | Nội dung | Dùng cho |
|---|---|---|---|---|
| `[FL]` | `C:\Users\KietVu\Testplace\uit-msc-dp-adaptive-fedmix` | `ccbc42a` | Stack Flower của Bài 1 (bài hội nghị): FedAvg, FedMix, CCVR, các head LDA/Newton, cổng bậc hai; bản port FedBR lên Flower; bản chép lại FedBR `src/fedbr_repro/` | Ch.3 (kết quả nền), Ch.4 (định cỡ $s$), IR#9 |
| `[FL]/runs` | `…\uit-msc-dp-adaptive-fedmix\runs` | *(không trong git)* | Kết quả thô của Bài 1 và các cổng | truy vết số liệu Ch.3 |
| `[FL]/paper/conference` | `…\uit-msc-dp-adaptive-fedmix\paper\conference` | *(không trong git)* | `main.tex`, `refs.bib`, `figures/`, `response/`, `reviews/`; `Calibration-reproduce.pdf` là bản **trước phản biện** | trích dẫn Bài 1 |
| `[BR]` | `C:\Users\KietVu\Testplace\FedBR` | `4cf6409` | Mã LINs-lab/FedBR (DomainBed) đã vá; nền tảng thực nghiệm của Ch.5 | Ch.4, Ch.5 |
| `[BR]/output` | `C:\Users\KietVu\Testplace\FedBR\output\cifar10` | *(không trong git)* | Kết quả chạy `[BR]`: `01_attempt_20260916`, `02_attempt_20260916` | Ch.5 §5.2 (tái hiện) |
| `[DP]` | `C:\Users\KietVu\Testplace\fedmix\fedmix` | `771e725` (git@github.com:DevPranjal/fedmix) | Bản cài đặt FedMix mã mở mà `[FL]` hiệu chỉnh theo | đối chiếu cài đặt |

**Tra cứu trong `[FL]`.** Từ 24/09, `runs/` và `paper/` đã được bỏ khỏi `.gitignore` (chỉ trên máy, học viên không commit), nên công cụ Grep tìm được bình thường trong cả hai, kể cả `runs/runs/`. Hai thư mục này **không có trong git**: `git ls-files` và `git log` không thấy chúng, nên lấy chúng từ ổ đĩa chứ đừng tra qua git. `storage/` (dữ liệu CIFAR, CINIC) vẫn bị ignore và không cần tìm trong đó. Nếu sau này `.gitignore` được khôi phục, Grep sẽ lại bỏ qua hai thư mục này; lúc đó dùng `grep -rn` qua Bash. Tài liệu định hướng của `[FL]` nằm ở `CLAUDE.md` và `docs/NEXT_STEPS.md` §0. Chúng ghi hướng "FedMix → FedBR trên Flower" từ 07/09. Hướng hiện hành của luận văn là dàn bài `00_outline.md`, **không phải** hai tệp đó.

---

## 1. Phát hiện phải biết trước khi viết

**F1. Cả ba bản cài đặt FedMix chia số hạng Taylor thêm một lần cho kích thước lô.** Hệ số hiệu dụng của số hạng (III) là $\lambda(1{-}\lambda)/B\cdot\mathrm{mean}_i\langle\nabla\ell_i,\bar x_i\rangle$, trong khi (3.15) yêu cầu $\lambda(1{-}\lambda)\cdot\mathrm{mean}_i$. Nguyên nhân chung: `l1` lấy trung bình trên lô trước khi lấy đạo hàm theo đầu vào, rồi số hạng thứ ba lại lấy trung bình hoặc chia cho $B$ một lần nữa.

| Kho | Vị trí | $B$ trong cấu hình | Số hạng Taylor nhỏ hơn công thức |
|---|---|---|---|
| `[BR]` | `fedbr/algorithms.py:847–850` (`loss3 = sum(λ·grad·x̄)/B`) | 32 | 32 lần. Đã kiểm bằng số: tỉ lệ 8,000 ở $B=8$; 32,000 ở $B=32$ |
| `[FL]` | `src/data/augmentation.py:322, 343–344` (`t1_x = lam·(grad_x·x̄).sum(1).mean()`) | 10 (`configs/cifar10/paper_k2.yaml:22`) | 10 lần. `tests/test_higher_order_taylor.py:13–14` tự ghi nhận "implicit 1/B"; các test dùng $B=1$ nên không bắt được |
| `[DP]` | `fedmix/client.py:185–197` (`criterion = CrossEntropyLoss()` lấy trung bình; `l3 = torch.mean(λ·inner(grad, x̄))`) | theo cấu hình của `[DP]` | $B$ lần |

**Hệ quả.** Kết quả FedMix −1,86 pp của Bài 1 **cũng** được đo với số hạng Taylor đã bị thu nhỏ. Câu "đây là kết quả về chính cơ chế" ở Ch.3 mục 3.6 (md 23/09) cần một hạn định. Đây là quy ước chung của cả ba bản mã mở chứ không riêng FedBR. Bài báo FedMix không có mã chính thức (`main.tex:324`), nên luận văn không khẳng định được tác giả gốc dùng cách nào. Phát biểu an toàn: *"cả ba bản cài đặt mã mở mà luận văn đối chiếu đều chuẩn hoá số hạng này theo lô hai lần"*.

**F2. Ba con số luận văn đang trích từ Bài 1 không có trong bài.**

| Con số | Đang dùng ở | Thực tế |
|---|---|---|
| Cận trên 95% một phía **−0,53 pp** (FedMix); kèm +0,17 (C1), +0,38 (C1+C2) | `00_outline.md` IR#2, §3.3 *(đã sửa 24/09)*; Ch.3 mục 3.6 | Không có trong `main.tex` hay bất kỳ tệp nào của `[FL]`. Bài chỉ có khoảng tin cậy hai phía $[-3{,}82;\ +0{,}10]$ trong `response/RESPONSE_TO_REVIEWERS.md:293–299`, và khoảng này **bị cắt khỏi bài** vì giới hạn trang (`response/CHANGELOG_main_tex.md:58`). **Con số cũ không sai, chỉ khác độ làm tròn đầu vào.** Với $t_{0{,}95;2}=2{,}920$, $n=3$: tính từ ba hiệu theo hạt giống thì FedMix **−0,518**, C1 **+0,164**, C1+C2 **+0,385**; tính từ trung bình và độ lệch chuẩn đã làm tròn trong bài (−1,86 ± 0,79; −1,90 ± 1,23; −1,64 ± 1,20) thì ra −0,528, +0,174, +0,383. Luận văn dùng **−0,52 / +0,16 / +0,38**, vì đó là giá trị ai cũng tái lập được từ số theo hạt giống đã in trong bài, và **ghi rõ là phép tính của luận văn** trên số liệu của [TG]. Kết luận không đổi: chỉ FedMix loại trừ được khả năng cải thiện |
| $s \approx 1{,}2$ pp | `00_outline.md` §5.2; Ch.4 mục 4.5.4 | Không có nguyên văn. Các độ lệch chuẩn mẫu gần 1,2 trong bài: CCVR ±1,19 (Bảng IV), C1 ±1,23 và C1+C2 ±1,20 (Bảng III). Toàn bộ khoảng trong bài: 0,79 (FedMix) đến 1,37 (Newton hội tụ) |
| $n/d \approx 3{,}9$ | Ch.3 mục 3.5.2 | Không có nguyên văn. Đó là $M_c/d = 2000/512 = 3{,}906$; cả hai thành phần có trong bài (`main.tex:297`, `:610`) |

**F3. Mọi dấu ± trong Bài 1 là độ lệch chuẩn mẫu (chia $n-1$) của ba hiệu theo cặp.** Nguồn: `scripts/aggregate_negatives_k2.py` dùng `statistics.stdev`, và các trường `std` trong JSON khớp. **Ngoại lệ:** thanh sai số Hình 1 dùng độ lệch chuẩn tổng thể (`scripts/make_paper_figures.py:111`, `pstdev`), vẽ ±0,42 trong khi chữ ghi ±0,51.

**F4. Số hạng bậc hai "≈10⁻⁴" chỉ đúng tại khởi tạo.** Trên backbone đã huấn luyện, tỉ số theo từng hạt giống là **0,039 / 0,224 / 0,025** (`runs/gate_2nd/second_order_gate.json`, trường `trained.seed4x.m1.ratio_B_over_A`). Con số **9,62·10⁻²** mà `docs/BAI1_DOSSIER.md:99–116` ghi là erratum chính là trung bình của ba tỉ số này; nó bị hạt giống 43 kéo lên, nên Ch.5 mục 5.2.2 báo cáo cả ba giá trị thay cho trung bình. Bài 1 có rào ở `main.tex:337–338`. Ch.3 mục 3.3.6 (md) đang ghi đúng "tại khởi tạo", nhưng nên nêu thêm con số trên backbone đã huấn luyện. ⚠️ `experiments/run_second_order_gate.py:144–163` chuẩn hoá các số hạng GN không nhất quán với số hạng A (lệch khoảng $B(1{-}\lambda)$). Tỉ số B_hess/A thì nhất quán. Chỉ trích tỉ số đó.

**F5. "M" nghĩa khác nhau ở hai stack.** Luận văn không được viết như thể hai bên dùng cùng một $M$.
- `[FL]`: một mẫu trung bình = trung bình **toàn bộ** dữ liệu cục bộ của client (khoảng 833 ảnh ở K=2, 60 client). Pool có 60 hàng, dựng một lần. **Một** hàng pool ghép với cả lô.
- `[BR]`: $M=10$ viết cứng. 32 mẫu dựng lại ở **mỗi bước**, từ dữ liệu thô của mọi client, ghép một-một với lô.

Bảng đối chiếu đầy đủ ở §6.

**F6. Những chỗ lời văn Bài 1 lệch với nhật ký thô.** Giữ nguyên khi trích bài; không lặp lại các cụm này trong luận văn như sự thật đã kiểm.
- "Parity within ±2 pp" (`main.tex:264, 313`): nhật ký ghi +2,88 / +2,83 pp (`docs/reproductions/REPRODUCTION_CIFAR10_GATE.md:3, 69, 83`).
- Câu "same frozen checkpoint" cho bước +0,29 → +0,97 (`main.tex:400–402`): thực tế là hai backbone huấn luyện riêng (66,99% ở vòng 147 và 65,86% ở vòng 138), và lr huấn luyện lại head cũng đổi từ 0,01 sang 0,001 (`REPRODUCTION_G0_CCVR_GATE.md:94`).
- `paper/conference/README.md:8–10` và `docs/BAI1_DOSSIER.md` còn số một hạt giống cũ (C1 −2,22; C1+C2 −1,36) và một sign test $p=0{,}016$ không còn trong bài.

---

## 2. Bài 1 — thông tin trích dẫn (IR#9)

| Mục | Giá trị | Nguồn |
|---|---|---|
| Tiêu đề | *When Does Classifier Calibration Reproduce Under Non-IID Federated Learning? A Controlled Study on a Faithful Flower Stack* | `main.tex:26–28` |
| Tác giả | Vu Tuan Kiet; Nguyen Tan Cam (tác giả liên hệ, camnt@uit.edu.vn). Khoa Khoa học và Kỹ thuật Thông tin, Trường ĐH Công nghệ Thông tin, ĐHQG-HCM | `main.tex:29–44` |
| Hội nghị | **2026 10th IEEE Symposium on Wireless Technology & Applications (ISWTA 2026)** | `CLAUDE.md:54`; `response/RESPONSE_TO_REVIEWERS.md:5`; `paper/conference/slides/README.md:68` |
| Trạng thái | Accepted (2 Weak Accept, 1 Strong Accept); camera-ready đã nộp. **Chưa có DOI / chỉ mục IEEE Xplore / số trang** trong kho | `CLAUDE.md:54–58`; `paper/conference/reviews/` |
| Bản camera-ready | build từ commit **`cdac4ae`** (31/08/2026), tệp `paper/conference/main.pdf`, 6 trang. Chuỗi trước đó: `dd94f71` (bản nộp đầu), `a52af17` (sửa theo phản biện, 11/08) → `Calibration-reproduce-revised.pdf` | `git log`; `response/CHANGELOG_main_tex.md:3–4` |
| Tài trợ | UIT, ĐHQG-HCM, đề tài **CS4-2026-80299** | `main.tex:621–622` |
| ⚠️ Tên hội nghị lệch | `main.tex:13` (chú thích), `refs.bib:4`, `docs/GLOSSARY.md:99` ghi **ISCIT**, là tên nơi nộp trước đó (`RESPONSE_TO_REVIEWERS.md:35`). Hạng CORE B chỉ gắn với ISCIT. **Không gắn hạng CORE cho ISWTA** trong luận văn | — |
| ⚠️ Tệp PDF trong `paper/ref/` của luận văn | `FedBR/paper/ref/Calibration-reproduce.pdf` trùng bản **trước phản biện** (01/07, còn cụm "class-distribution-oblivious" đã bị gỡ). Trích bài thì đối chiếu với `main.pdf` | — |

⚠️ **Từ 24/09 (`00_outline.md` §1.5), thân luận văn không trích bài này.** Kết quả của bài là kết quả của luận văn (Ch.5 mục 5.2). Bài chỉ xuất hiện ở *Danh mục công bố khoa học của tác giả* và *Lời cam đoan*; câu mẫu cho cả hai ở cuối `01_chuong1.md`. Dạng liệt kê trong Danh mục công bố:
*Vu Tuan Kiet, Nguyen Tan Cam, "When Does Classifier Calibration Reproduce Under Non-IID Federated Learning? A Controlled Study on a Faithful Flower Stack," 2026 10th IEEE Symposium on Wireless Technology & Applications (ISWTA 2026), 2026. (Đã được chấp nhận đăng.)* Trang và DOI bổ sung khi có kỷ yếu.

Các cột "Vị trí trong `main.tex`" ở §3 vẫn hữu ích: chúng giúp đối chiếu để lời văn luận văn không mâu thuẫn với bài đã đăng.

---

## 3. Truy vết số liệu Bài 1 mà luận văn dùng

Đường dẫn `runs/…` tính từ `[FL]`. "Best" = độ chính xác cao nhất theo vòng trong `metrics.csv`, cột `accuracy` (phân số 0–1).

| Số liệu | Vị trí trong `main.tex` | Tệp thô | Tái tính bằng |
|---|---|---|---|
| FedAvg 68,69 / 67,42 / 64,74; FedMix 66,50 / 66,47 / 62,31 → Δ **−2,19 / −0,95 / −2,43**, **−1,86 ± 0,79** (K=2, 500 vòng) | 122, 317–319, 378 | `runs/_archive/fedmca_closed/negative_k2/{fedavg,fedmix}_cifar10_k2{,_s43,_s44}/<ts>/metrics.csv`. Timestamp đúng: s42 `20260602_132821` / `20260602_151215`; s43 `20260629_193130` / `20260630_014147`; s44 `20260629_223551` / `20260630_060619` | `python -m scripts.aggregate_negatives_k2 --log-root runs/_archive/fedmca_closed/negative_k2` |
| ⚠️ Bẫy khi tái tính | — | `fedmix_cifar10_k2/` có thêm `20260603_142229` (chạy thử 1 vòng) và `20260603_143731` (`mash_augment false`, nhóm 4, best 63,10). **Không** dùng hai thư mục này. Cấu hình s42 thiếu khối `fedmix` (dùng mặc định của mã lúc đó); s43/s44 đặt `mash_augment: true` cho khớp | — |
| Δ vòng cuối (không phải số của bài) | — | cùng tệp: −3,55 / −4,49 / +0,59 | — |
| C1 −1,90 ± 1,23 (−2,22 / −0,55 / −2,94) | 122, 333–334, 379 | `negative_k2/fedmca_c1_cifa10_k2` (s42, tên thư mục viết sai sẵn "cifa10"), `fedmca_c1_cifar10_k2_{s43,s44}` | script trên |
| C1+C2 −1,64 ± 1,20 (−1,36 / −2,95 / −0,60), Dir β=0,3, 150 vòng | 345–347, 383 | s42: `runs/fedtc/{fedavg,fedmca_c1c2_…_lam005}_…_b030_screen/`; s43/s44: `runs/_archive/fedmca_closed/*_screen_s43/s44` | **không có script**; tự tính từ `metrics.csv` |
| LDA +6,45 ± 1,29; CCVR +4,41 ± 1,19; Newton-CE 1 bước +2,98 ± 1,04; bậc nhất 1 bước +0,36 ± 0,12 (CIFAR-10, β=0,05, 150 vòng) | 468–469, 511–513 (Bảng IV) | `runs/runs/e2/head_methods_summary.json`; CINIC-10: `runs/runs/e2_cinic/…` | `experiments/run_head_methods.py`, cấu hình `configs/cifar10/dirichlet_sweep/head_methods_3seed_b005.yaml` |
| Newton hội tụ +6,14 ± 1,37; bậc nhất tốt nhất +5,29 ± 1,09; LDA − Newton +0,25 ± 0,18 (CIFAR) / +0,35 ± 0,06 (CINIC) | 471–483, 525 | `runs/runs/e3/e3_fair_baselines.json`, `runs/runs/e3_cinic/…`. ⚠️ LDA ở E3 là +6,39, không phải +6,45 của E2 | `experiments/run_e3_fair_baselines.py` |
| CCVR $M_c=100$: +0,29 (β=0,1), **−0,76** (β=0,3) | 398–399 | `runs/_archive/void_superseded/fedtc4/ccvr_cifar10_dir_b0{10,30}_screen/…/calibration_metrics.json` | — |
| CCVR $M_c=2000$: +0,97 (β=0,1); +3,88 / +4,30 / +4,90 → **+4,36 ± 0,51** (β=0,05) | 130, 400–403, 584 | `runs/fedtc5/ccvr_b010_paperhp`, `runs/fedtc5/ccvr_b005_paperhp{,_s43,_s44}` | `scripts/make_paper_figures.py` `make_fig1` |
| Tỉ số chuẩn head max/min **1,10–1,17** (1,099 / 1,147 / 1,172) | 540, 550 | `runs/fedtc5/ccvr_b005_paperhp*/calibration_metrics.json`, trường `head_weight_l2_before`. E2 có trường riêng `head_l2_max_over_min` = 1,106 / 1,156 / 1,144 | `make_fig2` |
| Recall lớp kém nhất **+44 / +45 / +26** (ship 18,0→61,9; dog 16,9→61,8; deer 22,3→48,6) | 539, 567–568 | cùng tệp, `diagnostics.recall_before/after` | `make_fig2` |
| Độ chính xác trên tập ảo 62,6% so với tập kiểm tra 58,1% (s42) | 575–576 | `runs/fedtc5/ccvr_b005_paperhp/calibration_metrics.json` | — |
| T2 ≈ 10⁻⁴ (0,013%) tại $\lambda=0{,}05$, tại khởi tạo | 335–340 | `docs/reproductions/REPRODUCTION_FEDMCA_C1_GATE.md:55` | `scripts/check_t2_magnitude.py` (10 ảnh, $B=10$). Xem F4 |
| Tái hiện DevPranjal: FedAvg 65,81, FedMix 63,67 → −2,14 | 111, 263–265, 320–321 | `runs/_archive/hydra_reference/results/cifar10_{0,1}/` | `REPRODUCTION_CIFAR10_GATE.md:57–69` |

**Giới hạn tự khai của Bài 1** (dòng trong `main.tex`, dùng cho IR#1):
- "consistency check, not independent validation": 112, 266–267, 322–323
- "one architecture family (BN-free VGG) … one heterogeneity type (label skew), and C=10": 588–590
- CINIC-10 "descriptively rather than as an inference test": 483–485
- "CINIC-10 contains CIFAR-10": 590–591
- "The BN-free backbone is load-bearing": 592–594
- "the mechanism's natural home is feature skew": 361 (xem thêm 497–498, 607–609)
- không tuyên bố riêng tư / (ε,δ): 114–116, 615–619

---

## 4. `[FL]` — stack Flower

### 4.1. Cấu hình chính của Bài 1

| Mục | Giá trị | Nguồn |
|---|---|---|
| Khung | Flower `flwr` simulation, PyTorch, `uv` | `CLAUDE.md:134–140` |
| Dữ liệu | CIFAR-10 (chính); CINIC-10 chỉ cho phép so sánh head | `main.tex:239–249` |
| Client | $N=60$; `fraction_fit` 0,25 → 15 client mỗi vòng | `configs/cifar10/paper_k2.yaml:10, 29–31` |
| Vòng | 500 (K=2) / 150 (Dirichlet) | `paper_k2.yaml:11`; `dirichlet_sweep/*_screen.yaml` |
| Huấn luyện cục bộ | $E=2$ epoch, $B=10$, SGD lr 0,01, momentum 0, wd 0, decay 0,999 mỗi vòng. **Số bước cục bộ không cố định** (theo epoch) | `paper_k2.yaml:22–26, 34` |
| Backbone | `CustomVGG`: 6 conv + 3 FC, dropout 0,1, **không BatchNorm**; $d=512$ (sau `fc1`+ReLU); 3.491.530 tham số ($C=10$) | `src/models/vgg.py:9–84`; $d$ ở `:12` |
| Phân hoạch K=2 | mỗi client K lớp, theo `_partition_cifar_new` của `[DP]`; dùng `np.random.seed` toàn cục | `src/data/partition.py:167–243` |
| Phân hoạch Dirichlet | **cho từng lớp, rút vector trên 60 client**: `Dirichlet(np.full(num_clients, β))`. β là nồng độ **mỗi thành phần**, trục **client**, 60 thành phần (quy ước NIID-Bench). ⚠️ docstring `:97` và `docs/GLOSSARY.md:16` ghi sai thành `1_C` | `partition.py:114–119` |
| $\lambda$ FedMix | 0,05 | `configs/cifar10/fedmix.yaml:22–24` |
| Hạt giống | 42 / 43 / 44 | `fedmix_s43.yaml`, `fedmix_s44.yaml`, `fedavg_s4{3,4}.yaml` |
| CCVR | $M_c=2000$ mẫu ảo mỗi lớp (rút $2M_c$, chia đôi huấn luyện/đánh giá); Tukey 0,5; huấn luyện lại head 10 epoch, lr 0,001 | `src/calibration/ccvr.py:108–138, 274–326`; `dirichlet_sweep/ccvr_b005_paperhp.yaml:14` |
| LDA | $\bar\Sigma$ = trung bình **không trọng số** của các $\Sigma_c$, co về $(\mathrm{tr}/D)I$ với hệ số 0,01 | `src/calibration/head_methods.py:53–76` |

### 4.2. Bản đồ mã

| Thư mục / tệp | Nội dung chính | Trạng thái |
|---|---|---|
| `src/data/augmentation.py` | `compute_mashed_pair` `:167` (trung bình toàn bộ dữ liệu cục bộ), `group_pool_entries` `:188` (gom nhóm $m$ ở máy chủ, FedMix Phụ lục J), `build_fedmix_pool_blob` `:221`, `fedmix_loss` `:297–360`, bậc hai T2 `:350–360` | hoạt động |
| `src/client/fedmix_client.py` | `FedMixClient.fit` `:45–159`; chọn **một** hàng pool cho cả lô `:125–145`; RNG `server_round*10000+cid` `:80–81`; không loại pool của chính client | FedMix: hướng đã đóng |
| `src/client/base_client.py` | FedAvg `NumPyClient`; client rỗng trả 0 mẫu `:109–123` | hoạt động |
| `src/server/strategy.py` | `FedAvgBaselineStrategy` (lr decay, checkpoint tốt nhất `:201–205`), `FedMixStrategy` `:389–422` (gửi pool mỗi vòng qua `FitIns.config`), `FedBRStrategy` `:341–386` | hoạt động |
| `src/data/partition.py` | γ-IID `:35`, Dirichlet `:87`, K-shard `:167` | hoạt động |
| `src/data/rotation.py` | xoay theo client: $q\sim\mathrm{Dir}(\alpha\cdot 1_{10})$ trên $\{0,15,…,135\}$ `:74–111`. ⚠️ Mặc định `dirichlet_alpha` 1,0 **mỗi thành phần**, khác `[BR]` (0,1 mỗi thành phần); `final_audit.md` R2 | port FedBR |
| `src/data/fedbr.py`, `src/client/fedbr_client.py` | pseudo-data RSM (nhãn đều $1/C$), hàm mất mát tương phản min-max | port FedBR |
| `src/calibration/` | `feature_stats.py` (μ, Σ, **counts** theo lớp), `ccvr.py`, `head_methods.py` (LDA `:65`, bậc nhất `:142`, Newton `:173`, Newton nhiều bước `:220`), `stat_heterogeneity.py`, `transform_methods.py` (Q3a, đã đóng) | bằng chứng Bài 1, đóng băng |
| `src/models/` | `vgg.py` (CustomVGG), `vgg11.py` (torchvision vgg11 không BN, 9,23 M tham số), `fedbr_net.py` (projection 256), `etf_head.py` (`balanced_softmax_loss` `:67`), `lenet.py` | — |
| `src/fedbr_repro/` | bản chép lại `[BR]` tại artifact `6c4c539`, **không dùng Flower**; xem §5.3 | tham chiếu |
| `src/utils/` | `run_paths.py` (thư mục chạy), `logger.py` (`seed_everything` `:20`, ghi `metrics.csv` mỗi vòng `:200–242`), `config.py` (gộp `base_configs`) | — |
| `src/privacy/`, `src/adaptive/` | tệp rỗng | đóng băng |

**Thư mục một lần chạy:** `runs/<slug>/<YYYYMMDD_HHMMSS>/` gồm `config_resolved.{yaml,json}`, `metrics.csv` và `metrics.json` (ghi lại mỗi vòng; cột `round, train_loss, eval_loss, accuracy, …`), tệp TensorBoard. Các runner calibration ghi thêm `calibration_metrics.json`, `head_methods_*.json`, `e3_fair_baselines*.json`, `backbone.pt`. Stack này không có `.jsonl`.

**Runner** (`uv run python -m experiments.<tên> --config …`): `run_baseline` (FedAvg), `run_fedmix`, `run_ccvr`, `run_head_smoke`, `run_head_methods` (E2), `run_e3_fair_baselines` (E3), `run_second_order_gate`, `run_fedbr`, `run_fedmca` (đóng), `run_efron_gate`, `run_bfa_clientview` (đóng), `run_etf_preflight`, `run_fednac_additivity` (tạm dừng). Script (`python -m scripts.<tên>`): `aggregate_negatives_k2`, `make_paper_figures`, `make_head_convergence_fig`, `check_t2_magnitude`, `summarize_gate`, `summarize_ccvr_diagnostics`, `run_negatives_seeds`, `download_datasets`.

### 4.3. `runs/` — thư mục nào chứa gì

| Thư mục | Thí nghiệm | Số chính |
|---|---|---|
| `runs/runs/{e2,e2_cinic,e3,e3_cinic,e3_local}` | **Bảng IV và Hình 3 của Bài 1** | §3. ⚠️ `runs/runs/e3/metrics.csv` chỉ có 33 vòng; số E3 lấy từ JSON |
| `runs/fedtc5/` | **Cổng CCVR G0**, $M_c=2000$; Hình 1 và Hình 2 | +4,36 ± 0,51 |
| `runs/fedtc/` | các screen β=0,3, s42 | C1+C2 −1,36 |
| `runs/fedtc6/` | thống kê không đồng nhất trên backbone β=0,05 s42 | H trung vị 1,30, "FLAT" |
| `runs/gate_2nd/` | cổng số hạng bậc hai trên backbone E2 | B/A = 0,096 (xem F4) |
| `runs/efron_gate_s4{2,3,4}/` | CCVR so với boundary so với trần LDA | "TRAP CONFIRMED" |
| `runs/fedbr_a_cifar10_dir_b005_*` | port FedBR lên Flower, β=0,05, 150 vòng | best 45,96 / 51,41 / 48,05, so với FedAvg 54,21 |
| `runs/paper_{fedavg,fedbr}_rot{,_noaug}_r500/` | cấu hình bài FedBR trên Flower (10 client, α=0,1, xoay, VGG11, $B=32$, 50 bước, 500 vòng) | trung bình top-5: FedAvg 57,49 / FedBR 57,26 (có augment); 55,18 / 56,04 (không augment) |
| `runs/_archive/fedmca_closed/negative_k2/` | **Bảng III của Bài 1** (K=2, 3 hạt giống) | §3 |
| `runs/_archive/hydra_reference/` | chạy `[DP]` | −2,14 |
| `runs/_archive/void_superseded/fedtc4/` | CCVR $M_c=100$ | +0,29 / −0,76 |
| `runs/_archive/duplicates_of_runs_runs/` | bản trùng byte với `negative_k2/` và `e3/` | không dùng |
| `runs/bfa_*`, `runs/etf_preflight_*`, `runs/fednac_*` | các hướng đã đóng | không dùng cho luận văn |

⚠️ `docs/reproductions/REPRODUCTION_CIFAR10_GATE.md` còn ghi đường dẫn cũ `runs/fedavg_cifar10_k2/…`. Bảng đổi đường dẫn nằm ở `runs/_archive/README.md`. `docs/BAI1_DOSSIER.md` trỏ tới `runs/fedtc9`, thư mục này **không tồn tại**.

---

## 5. `[BR]` — nền tảng FedBR của Ch.5

### 5.1. Mã

Vị trí mã chính đã có ở `00_outline.md` §3.1. Bổ sung:
- `fedbr/algorithms.py:845–851` `FedMix.update`: xem F1.
- `fedbr/scripts/train_fed.py:62–75` `get_augmentation_fedmix_data`: $M=10$ viết cứng; mỗi mẫu trung bình lấy từ một client ngẫu nhiên; số mẫu bằng `batch_size`.
- `fedbr/scripts/train_fed.py:439–442`: gọi lại ở **mỗi bước**, từ `in_splits` thô của mọi client.
- `fedbr/scripts/summarize.py:87–131`: chỉ số = trung bình top-$k$ vòng (`--top_k 5`); `--metric local` = tập giữ lại 20% của client (`env00..09_out`, chỉ số của bài FedBR); `--metric global` = 10 tập kiểm tra góc cố định (`env10..19_in`).
- `fedbr/scripts/eval_checkpoint.py`: chấm lại `model.pkl` (vòng cuối) trên mọi env/split.
- Bố cục thư mục kết quả: `REPRODUCE.md` §8.

### 5.2. `output/cifar10/` — kết quả

Cấu hình chung của cả hai lần chạy: RotatedCIFAR10, 10 client, `seed 12345`, **một hạt giống**, `local_steps 50`, `steps 50000` (1000 vòng), đánh giá mỗi 5 vòng, `vgg11`, lr 0,01, $B=32$, `fedmix_lambda 0,1`. Mỗi lần chạy có `out.txt`, `err.txt`, `results.jsonl` (bản ghi đầu chứa `args` và `hparams`), `model.pkl` (vòng cuối), `done`.

| Lần chạy | Mã | Khác biệt | Có dùng được không |
|---|---|---|---|
| `01_attempt_20260916` | trước `c0c3c43` | momentum **0,9** cho ERM/Moon; chỉ ghi tập kiểm tra góc (`eval_test_only`), nên **không có** chỉ số của bài; fedbr-mixup và moon dừng giữa chừng (130 và 275 vòng) | ❌ không trích. Giữ để kiểm toán (lý do commit `9550587`, `c0c3c43`) |
| `02_attempt_20260916` | sau `c0c3c43` | momentum 0; ghi `local+global`; đủ 9 thuật toán, 1000 vòng | ✅ **bản để trích** |

`02_attempt_20260916/summary.csv` (Acc = local top-5, Global = tập kiểm tra góc top-5; đã tái tính khớp từ `results.jsonl`):

| Run | Acc (%) | Global (%) | Vòng tới 55% | h/1000 vòng |
|---|---|---|---|---|
| fedavg (ERM) | 59,45 | 40,39 | 710 | 2,3 |
| fedbr | 65,82 | 40,67 | 435 | 7,5 |
| fedbr-mixup | 66,47 | 39,91 | 425 | 7,6 |
| **fedmix** | **57,16** | 41,11 | 875 | 5,8 |
| fedprox | 59,14 | 40,12 | 735 | 2,7 |
| groupdro | 59,23 | 39,76 | 750 | 2,3 |
| mixup | 59,44 | 39,90 | 750 | 2,2 |
| dann | 55,60 | 39,06 | 945 | 2,9 |
| moon | 52,95 | 39,05 | – | 8,8 |

Kèm `cifar10_convergence.png`. FedBR và FedProx cho số Global giống hệt nhau ở hai lần chạy (40,67 / 40,12). Điều đó xác nhận chỗ thay đổi giữa hai lần chỉ là momentum và cách ghi split.

⚠️ **Khi dùng các số này trong luận văn:**
- Một hạt giống, nên chỉ làm bảng tái hiện ở Ch.5 §5.2.1, không làm bằng chứng so sánh.
- FedMix ở đây chạy $\lambda = 0{,}1$ với số hạng Taylor thu nhỏ 32 lần (F1).
- Môi trường 0° còn lỗi `if not angle` (T12 chưa sửa trong lần chạy này).
- Đây là thư mục **không có mặt trong git**. Nhắc tới nó thì ghi đường dẫn đầy đủ theo IR#8.

### 5.3. `[FL]/src/fedbr_repro/` — bản chép lại `[BR]`, dùng để đối chiếu kiểm toán

- Chép từ artifact `6c4c539`, worktree `C:\Users\KietVu\Testplace\FedBR-artifact`.
- 334 test chẵn lẻ (parity), 0 skip.
- Báo cáo: `src/fedbr_repro/porting_report/README.md:177–201` (các phát hiện liên quan tới luận văn) và `final_audit.md`.

Các phát hiện khớp hoặc bổ sung cho danh mục kiểm toán D1–D13 ở Ch.5:
- Phân hoạch gần như một lớp mỗi client. `lda_partition` rút **theo client, trên các lớp còn lại**, vào một shard cố định 5000 ảnh; `final_audit.md:647–661` gọi đây là "hai thuật toán khác nhau, không phải hai giá trị tham số".
- Client huấn luyện trên 4000 ảnh; mỗi môi trường đánh giá có 8000 ảnh.
- Môi trường 0° không phải ảnh thẳng (D1).
- FedAvg có momentum 0,9, FedBR là SGD thuần (D5).
- Projection 1024 thay cho 256/128 (P3).
- Bài báo FedBR ghi $\lambda=0{,}1$ cho CIFAR-10, mã ghi 1,0 (P2).
- Pseudo-data của FedMix và FedBR trùng từng byte trừ nhãn (`tests/fedbr_repro/test_data_parity.py:356`).
- `make_fedmix_pseudo_data` (`data.py:459`) dựng lại mỗi bước; `make_pseudo_data` (`:410`) dựng một lần.
- Trung bình top-5 là thống kê của bài (chú thích Bảng 8; `test_run_parity.py:334`).

---

## 6. Đối chiếu ba stack cho FedMix

| | `[FL]` (Bài 1) | `[BR]` (Ch.5) | `[DP]` |
|---|---|---|---|
| Ảnh mỗi mẫu trung bình | toàn bộ dữ liệu cục bộ của client | $M=10$ (viết cứng) | toàn bộ dữ liệu cục bộ |
| Số mẫu trung bình | 1 mỗi client (60); gom nhóm $m$ ở máy chủ (`server_pool_group_size`, bài dùng $m=1$) | 32 mỗi bước, mỗi mẫu từ một client ngẫu nhiên | 1 mỗi client |
| Dựng khi nào | một lần trước huấn luyện; gửi lại mỗi vòng qua `FitIns` | **mỗi bước**, từ dữ liệu thô | một lần |
| Ghép với lô | **một** mẫu cho cả lô | một-một | một mẫu cho cả lô (`random.choice`) |
| Ảnh dùng để tính trung bình | đã chuẩn hoá; có augment ở cả 3 hạt giống của Bài 1 | `ToTensor` theo tập env | theo cấu hình `[DP]` |
| $\lambda$ | 0,05 | 0,1 | theo cấu hình |
| $B$ | 10 | 32 | theo cấu hình |
| Chuẩn hoá số hạng Taylor | thừa $1/B$ (F1) | thừa $1/B$ (F1) | thừa $1/B$ (F1) |
| Hệ số $\lambda(1{-}\lambda)$ | đúng | đúng | đúng |
| NaiveMix | **không có** | có (`algorithms.py:809`) | không có |
| Backbone | CustomVGG, không BN, $d=512$ | vgg11 không BN, $d=512$ | CustomVGG |
| Chỉ số | best theo vòng trên tập kiểm tra | top-5 theo vòng, tập giữ lại của client | theo `[DP]` |

---

## 7. Tra nhanh

| Cần | Xem |
|---|---|
| Trích dẫn đầy đủ Bài 1 | §2 |
| Tái tính −1,86 ± 0,79 | §3 hàng 1–2; `scripts/aggregate_negatives_k2.py` |
| Vì sao viết −0,52 chứ không phải −0,53, và cách ghi nguồn | F2 |
| Quy ước Dirichlet của Bài 1 (cho Bảng 3.3 của Ch.3) | §4.1: nồng độ mỗi thành phần, trục client, 60 thành phần |
| $d$ và số tham số từng backbone | §4.1; `src/models/` |
| Số hạng Taylor trong mã có đúng công thức không | F1 |
| Bảng tái hiện FedBR cho Ch.5 | §5.2, lần chạy 02 |
| Danh mục sai lệch mã ↔ bài FedBR đã kiểm độc lập | §5.3; `05_chuong5.md` §5.2 |
| Hai stack khác nhau ở đâu | §6 |
