# PLAN — Kế hoạch thực nghiệm hướng B

**Lập:** 24/09/2026 · **Thay thế:** `archive/2026-09-24_huong-bien-gioi-hieu-luc/PLAN_ke-hoach-8-tuan.md` · **Nguyên tắc:** chạy theo thứ tự T0 → T1 → T2. Không bắt đầu mức sau khi mức trước chưa có đủ số liệu.

> **Cập nhật 26/09 (học viên):** T0 **bỏ**, nền tảng FedBR chỉ dùng hạt giống 12345 vì mỗi lượt FedBR 1000 vòng mất khoảng 7,5 giờ. T2 (hướng A) đang chạy trên Vast, một hạt giống. T1 chỉ còn NaiveMix, tuỳ chọn. Các mục dưới về T0 và mốc "Sau T0" giữ làm lịch sử; cách đọc kết quả một hạt giống ở Ch.5 mục 5.1.3 và dàn bài IR#5.

---

## 1. Ba mức

| Mức | Mục đích | Trả lời | Chương dùng |
|---|---|---|---|
| **T0** | Đưa bảng so sánh trên mã FedBR từ 1 lên 3 hạt giống, để có khoảng tin cậy | RQ1 và RQ2, nửa lệch nhãn kèm xoay | Ch.5 mục 5.3.1–5.3.2 |
| **T1** | Tách số hạng Taylor: FedMix với chuẩn hoá đã sửa, và NaiveMix | RQ1 (Taylor có mang tín hiệu không), RQ2 | Ch.5 mục 5.3.2 |
| **T2 (A)** | FedBR cộng số hạng Taylor | đóng góp C4 | Ch.5 mục 5.5 — chỉ khi có số liệu |

## 2. Cấu hình chung

Giữ đúng cấu hình của `output/cifar10/02_attempt_20260916`, để $n = 3$ gộp được với hạt giống đã có:

| Tham số | Giá trị |
|---|---|
| Dữ liệu | RotatedCIFAR10 (lệch nhãn Dirichlet $\alpha = 0{,}1$ kèm xoay $\alpha_{\text{rot}} = 1{,}0$, nồng độ tổng) |
| Client, vòng, bước cục bộ | 10 client, 1000 vòng, 50 bước cục bộ |
| Tối ưu | SGD, lr 0,01, lô 32, **momentum 0** |
| Backbone | vgg11 không BN, $d = 512$ |
| Đánh giá | `--eval_envs local+global` |
| FedMix, NaiveMix | $\lambda = 0{,}1$ |
| Hạt giống | **12345** (đã có), **23456**, **34567**; đây là quy ước `SEEDS` của target `table8-errorbar` trong Makefile |
| Thư mục kết quả | `OUT=./output/cifar10-seed<s>`, theo đúng quy ước của Makefile |

Chạy `make probe` trên đúng GPU vừa thuê trước khi cam kết ngân sách.

## 3. Danh sách chạy và ngân sách

Đơn giá lấy từ cột `h/1000rd` của `02_attempt_20260916/summary.csv`. **Đo lại bằng `make probe` trước khi tin.**

| Mức | Thuật toán | Hạt giống mới | Giờ mỗi lần chạy | GPU-giờ |
|---|---|---|---|---|
| T0 | FedAvg (`run-fedavg`) | 23456, 34567 | 2,3 | 4,6 |
| T0 | FedProx (`run-fedprox`) | 23456, 34567 | 2,7 | 5,4 |
| T0 | FedMix bản gốc (`run-fedmix`) | 23456, 34567 | 5,8 | 11,6 |
| T0 | FedBR (`run-fedbr`) | 23456, 34567 | 7,5 | 15,0 |
| T0 | FedBR + Mixup (`run-fedbr-mixup`) | 23456, 34567 | 7,6 | 15,2 |
| | **Cộng T0** | | | **≈ 52** |
| T1 | FedMix bản sửa chuẩn hoá (cần M1) | 12345, 23456, 34567 | ≈ 5,8 | ≈ 17 |
| T1 | NaiveMix (cần M2) | 12345, 23456, 34567 | chưa đo; không có phép lấy đạo hàm kép nên dự kiến rẻ hơn FedMix | `[ĐO: make probe]` |
| | **Cộng T1** | | | **≈ 17 + NaiveMix** |
| T2 | FedBR + Taylor (`run-fedbr-taylor LABEL=soft TAYLOR=1`) | **12345 trước**; 23456, 34567 nếu còn thời gian | chưa đo; ước ≈ FedBR 7,5 + phần lan truyền ngược bậc hai của FedMix ≈ 3,5, tức ≈ 11 | `[ĐO: make probe]` |
| T2 | FedBR + nhãn mềm, không (III) (`… LABEL=soft TAYLOR=0`) | như trên | ≈ FedBR | `[ĐO]` |
| T2 | FedBR + Taylor, nhãn đều (`… LABEL=uniform TAYLOR=1`) | như trên | ≈ 11 | `[ĐO]` |
| T2 | FedBR + nhãn đều, không (III) (`… LABEL=uniform TAYLOR=0`) | như trên | ≈ FedBR | `[ĐO]` |

Với 2 GPU, T0 mất khoảng 26 giờ lịch và T1 khoảng 10–15 giờ lịch.

Không chạy lại Moon, DANN, GroupDRO, Mixup. Chúng chỉ có mặt trong bảng tái hiện một hạt giống. Moon còn mang lỗi D4, nên số của nó không so sánh được.

## 4. Việc lập trình (kho `FedBR`)

| # | Việc | Chặn |
|---|---|---|
| M1 | Cờ chọn cách chuẩn hoá `loss3` ở `fedbr/algorithms.py:850`. Bản sửa: bỏ phép chia cho `len(all_augmentation_y)`, vì `grad` đã mang $1/B$. Mặc định giữ hành vi gốc để `run-fedmix` không đổi | T1 |
| M2 | Target `run-naivemix` trong Makefile, theo mẫu `run-fedmix` | T1 |
| M3 | ✅ **Xong 26/09.** Lớp `FedBRTaylor` (`fedbr/algorithms.py`, kế thừa `FedBR`), hparam `fedbrt_lambda` 0,1 · `fedbrt_taylor` 1/0 · `fedbrt_label` soft/uniform; pseudo-data dựng một lần bằng `get_augmentation_fedmix_data` (trùng ảnh với FedBR ở cùng hạt giống); target `run-fedbr-taylor` và `t2`; 13 test CPU ở `fedbr/test/test_fedbr_taylor.py`. Thiết kế chốt ở khối 26/09 cuối `04_chuong4.md`. Chưa commit | T2 |
| M4 | *(thấp)* Sửa lỗi môi trường 0°, hoặc chấm lại các `model.pkl` bằng `eval_checkpoint.py`. Chỉ ảnh hưởng cột Global | — |

Mỗi thay đổi có một test chứng minh bản gốc không đổi khi cờ tắt. Với M1, thêm test số học: tỉ lệ giữa hai cách chuẩn hoá phải đúng bằng $B$. Mẫu có sẵn ở `scratchpad/check_loss3.py` của phiên 24/09; chép vào `tests/` nếu cần giữ.

## 5. Mốc kiểm soát

| Mốc | Kiểm tra | Nếu không đạt |
|---|---|---|
| Trước T0 | `make probe` chạy được trên GPU mới; đơn giá gần bảng §3 | tính lại ngân sách trước khi chạy |
| Sau T0 | FedBR − FedAvg theo cặp có khoảng tin cậy loại trừ 0 không | Không sao, cả hai kết cục đều là kết quả. Nhưng nếu không loại trừ được 0 thì Ch.5 **không được** viết "FedBR cải thiện" (IR#2, IR#5) |
| Sau T1 | FedMix bản sửa khác bản gốc bao nhiêu | Kết quả này đi vào kiểm toán (C3) và quyết định có nên làm T2 hay không: nếu số hạng Taylor ở đúng biên độ vẫn không mang tín hiệu thì A khó có lý do tồn tại |
| Trước T2 | T0 và T1 đã xong, Ch.5 mục 5.3 đã có bản nháp. Mã M3 viết trước được, chỉ việc *chạy* phải chờ | không chạy T2 |
| Trong T2 | Chạy theo thứ tự `soft/1 → soft/0 → uniform/1 → uniform/0` (đúng thứ tự của `make t2`); ngừng sớm nếu `soft/1` không hơn FedBR ở hạt giống 12345 | các cấu hình sau chỉ chạy khi cấu hình đầu cho tín hiệu |