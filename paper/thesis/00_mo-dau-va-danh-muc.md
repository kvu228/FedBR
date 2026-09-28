# PHẦN ĐẦU VÀ PHẦN CUỐI LUẬN VĂN — Lời cam đoan, Danh mục ký hiệu và chữ viết tắt, Mở đầu, Danh mục công bố

> **KHỐI TRẠNG THÁI** · 28/09/2026
>
> - **Word (bản lưu 28/09 11:38):**
>   - Tiêu đề "DANH MỤC CÁC KÝ HIỆU VÀ CHỮ VIẾT TẮT" đã có, kèm một bảng hai cột ("Ký hiệu chữ viết tắt | Chữ viết đầy đủ") mới có hai dòng FL, non-IID. Thay bằng hai bảng ở mục 2.
>   - Tiêu đề "MỞ ĐẦU" đã có, chưa có nội dung. Chép mục 3 vào dưới tiêu đề.
>   - Tiêu đề "DANH MỤC CÔNG BỐ KHOA HỌC CỦA TÁC GIẢ" đã có, chưa có nội dung. Chép mục 4.
>   - "LỜI CAM ĐOAN" đang trống. Chép mục 1 (thêm 28/09, lượt 2; dựa trên bản đề xuất ở `archive/…/01_chuong1.md`, sửa "đã được công bố" thành "đã được chấp nhận đăng").
> - **Nguồn đã kiểm:**
>   - chữ viết tắt: quét toàn bộ thân bài Word Ch.1–6, chỉ giữ những chữ thực sự xuất hiện; **không liệt kê tên viết tắt của các phương pháp, công trình** (FedAvg, FedMix, FedBR, CCVR, …) theo học viên (28/09);
>   - ký hiệu: theo quy ước sau lượt rà `AUDIT_28-09.md` (tham số mô hình là $\theta$, bộ phân lớp là $\omega$, hàm mất mát viết $l$ như trong Word);
>   - công bố 1: Crossref cho DOI 10.1109/ACCESS.2023.3320045 trả về đúng arnumber 10265050 của đường dẫn IEEE Xplore;
>   - công bố 2: thư chấp nhận `conference/Acceptance Letter - ISWTA2026.pdf` (Ref ACC-ISWT-000686, 21/08/2026), thứ tự tác giả theo `conference/main.tex`.
> - **Mở đầu (rút gọn, lượt 2):** ba đoạn, khoảng 280 tiếng, khoảng hai phần ba trang. Nội dung khớp Ch.1 và Ch.6 (bản 28/09); không trích bài hội nghị (IR#9).

---

## 1. LỜI CAM ĐOAN

Tôi xin cam đoan luận văn này là công trình nghiên cứu của bản thân, được thực hiện dưới sự hướng dẫn khoa học của PGS.TS. Nguyễn Tấn Cầm. Các số liệu và kết quả trình bày trong luận văn là trung thực và do tôi trực tiếp thực hiện. Một phần kết quả của luận văn, gồm các thực nghiệm dưới lệch phân phối nhãn ở Chương 5, mục 5.2, nằm trong bài báo [2] ở Danh mục công bố khoa học của tác giả, đã được chấp nhận đăng, với người hướng dẫn khoa học là đồng tác giả. Các phương pháp, số liệu và bộ thực nghiệm của tác giả khác được sử dụng trong luận văn đều được trích dẫn đầy đủ.

<p align="right"><i>TP. Hồ Chí Minh, ngày … tháng … năm 2026</i><br>Học viên<br><br><br><b>Vũ Tuấn Kiệt</b></p>

*Ghi chú: đối chiếu với mẫu Lời cam đoan của Trường trước khi dùng. Câu thứ ba khai báo phần trùng nội dung giữa luận văn và bài báo [2], để phần kiểm tra trùng lặp không bị hỏi. Nếu Trường yêu cầu khai báo công cụ AI hỗ trợ viết, thêm một câu riêng.*

---

## 2. DANH MỤC CÁC KÝ HIỆU VÀ CHỮ VIẾT TẮT

*Gợi ý trình bày trong Word: hai bảng liền nhau, bảng ký hiệu trước, bảng chữ viết tắt sau; cột trái căn giữa, cột phải căn trái. Ký hiệu nhập bằng công cụ công thức để khớp với thân bài.*

### Ký hiệu

| Ký hiệu | Ý nghĩa |
|---|---|
| $N$, $i$ | số client; chỉ số client |
| $D_i$, $P_i$ | tập dữ liệu cục bộ và phân phối dữ liệu của client $i$ |
| $p_i$ | trọng số của client $i$ khi tổng hợp, tỉ lệ với lượng dữ liệu |
| $S_t$ | tập client tham gia vòng truyền thông $t$ |
| $T$, $t$ | số vòng truyền thông; chỉ số vòng |
| $K$ | số bước cập nhật cục bộ trong một vòng |
| $B$ | kích thước lô cục bộ |
| $\eta$ | tốc độ học |
| $\theta$ | vector tham số của mô hình; $\theta_t$ là tham số toàn cục ở vòng $t$, $\theta_t^i$ là tham số client $i$ gửi lên |
| $f(\cdot;\theta)$, $f_i$ | mô hình; hàm mục tiêu cục bộ của client $i$ |
| $l$ | hàm mất mát trên một mẫu (cross-entropy) |
| $x$, $y$ | ảnh đầu vào; nhãn ở dạng one-hot |
| $\phi$, $\omega$ | bộ trích xuất đặc trưng; bộ phân lớp (tầng phân lớp) |
| $\omega_c$, $b_c$ | vector trọng số và số hạng tự do của lớp $c$ ở tầng cuối |
| $d$ | số chiều đặc trưng |
| $C$, $c$ | số lớp; chỉ số lớp |
| $\lambda$ | trọng số trộn của Mixup, NaiveMix, FedMix |
| $M$ | số ảnh gộp trong một mẫu trung bình |
| $\bar x_g$, $\bar y_g$ | ảnh trung bình và nhãn mềm của một mẫu trung bình |
| $V_i$, $V$ | tập mẫu trung bình của client $i$; tập mẫu trung bình toàn cục |
| $n_V$ | số mẫu trung bình mỗi client gửi lên |
| (I)–(IV) | bốn số hạng trong khai triển Taylor của mục tiêu global Mixup (3.14); (III) là số hạng Taylor |
| $u_p$, $P$ | pseudo-sample của FedBR; số pseudo-sample |
| $\phi_g$ | bản sao bộ trích xuất toàn cục mà client nhận ở đầu vòng |
| $h$ | tầng chiếu của FedBR |
| $s(\cdot,\cdot)$ | độ tương tự cosine |
| $\tau_1$, $\tau_2$ | hai hệ số nhiệt độ của hàm mất mát tương phản |
| $l_{\text{con}}$ | hàm mất mát tương phản của FedBR (3.17) |
| $L_{\text{bal}}$ | số hạng cân bằng tầng phân lớp của FedBR (3.18) |
| $\mu$, $\gamma$ | trọng số của $l_{\text{con}}$ và của $L_{\text{bal}}$ trong (3.19) |
| $g$, $\mathcal{L}_g$ | cách dùng mẫu trung bình; hàm mất mát cục bộ tương ứng (Thuật toán 4.1) |
| $d_x$, $C_y$, $b$ | số giá trị của một ảnh, số giá trị của nhãn đi kèm, số byte mỗi giá trị trong công thức chi phí (4.1) |
| $\alpha$ | nồng độ Dirichlet của lệch phân phối nhãn (nồng độ tổng, trục lớp) |
| $\alpha_{\text{rot}}$ | nồng độ Dirichlet của phân phối góc xoay (nồng độ tổng) |
| $\beta$ | nồng độ Dirichlet mỗi thành phần, trục client (nền tảng Flower) |
| $M_c$ | số đặc trưng ảo sinh cho mỗi lớp khi hiệu chuẩn tầng phân lớp |
| $\mu_c$, $\Sigma_c$ | trung bình và ma trận hiệp phương sai của đặc trưng thuộc lớp $c$ |
| $t_k$, $\delta$ | nhãn gắn với pseudo-sample và công tắc bật số hạng (III) trong (5.1) |

### Chữ viết tắt

| Chữ viết tắt | Chữ viết đầy đủ |
|---|---|
| CIFAR-10, CIFAR-100 | bộ dữ liệu ảnh 10 lớp và 100 lớp của Canadian Institute for Advanced Research |
| CINIC-10 | CINIC-10 Is Not ImageNet or CIFAR-10 — bộ dữ liệu 10 lớp gộp ảnh CIFAR-10 và ImageNet |
| EMNIST, FEMNIST | Extended MNIST; Federated Extended MNIST — bộ chữ viết tay mở rộng, bản phân hoạch theo người viết |
| FL | Federated Learning — học liên kết |
| GPU | Graphics Processing Unit — bộ xử lý đồ hoạ |
| IID, non-IID | (Non-)Independent and Identically Distributed — (không) độc lập và cùng phân phối |
| LDA | Linear Discriminant Analysis — phân tích biệt thức tuyến tính |
| MLP | Multilayer Perceptron — mạng perceptron nhiều tầng |
| NaN | Not a Number — giá trị không xác định |
| QDA | Quadratic Discriminant Analysis — phân tích biệt thức bậc hai |
| SGD | Stochastic Gradient Descent — hạ gradient ngẫu nhiên |
| VGG | Visual Geometry Group — họ kiến trúc mạng tích chập (VGG11: 11 tầng có trọng số) |
| VRAM | Video Random Access Memory — bộ nhớ của GPU |

*Hai bảng dùng dấu "—" để ngăn tên tiếng Anh và nghĩa tiếng Việt; đây là bảng tra, không phải văn xuôi, nên không tính vào hạn ngạch AI#6. Nếu muốn, tách thành ba cột: Chữ viết tắt · Tiếng Anh · Tiếng Việt.*

---

---

## 3. MỞ ĐẦU

Học liên kết cho phép nhiều thiết bị cùng huấn luyện một mô hình mà không gửi dữ liệu đi, nhưng hiệu suất giảm rõ khi dữ liệu giữa các thiết bị không đồng nhất. Chia sẻ thêm mẫu trung bình, tức ảnh trung bình của một nhóm ảnh kèm nhãn mềm, là một cách khắc phục tốn rất ít truyền thông. FedMix dùng loại mẫu này qua khai triển Taylor bậc nhất của hàm mất mát, nhưng chưa rõ cách dùng đó có thực sự nâng được hiệu suất hay không. Đó là lý do chọn đề tài.

Luận văn nhằm trả lời câu hỏi trên trong một khung có kiểm soát: dựng một khung học liên kết chia sẻ mẫu trung bình, trong đó cách dùng mẫu trung bình thay được, rồi so sánh ba cách dùng NaiveMix, FedMix và FedBR về độ chính xác và chi phí. Phạm vi là phân loại ảnh CIFAR-10 dưới lệch phân phối nhãn, có hoặc không kèm lệch đặc trưng mô phỏng bằng phép xoay, trên hai nền tảng thực nghiệm.

Về khoa học, luận văn cho thấy trong các cấu hình đã đo, cách dùng dựa trên khai triển Taylor không nâng được hiệu suất, còn cách dùng mẫu trung bình làm điểm tựa như FedBR thì có; đồng thời chỉ ra rằng cách tính số hạng Taylor theo lô thường gặp làm số hạng này nhỏ hơn công thức một thừa số bằng kích thước lô. Về thực tiễn, kết quả giúp chọn cách dùng mẫu trung bình và cho biết chi phí cùng lượng thông tin mà kênh này còn giữ.

---

## 4. DANH MỤC CÔNG BỐ KHOA HỌC CỦA TÁC GIẢ

[1] N. T. Cam and V. T. Kiet, "FlwrBC: Incentive Mechanism Design for Federated Learning by Using Blockchain," *IEEE Access*, vol. 11, pp. 107855–107866, 2023, doi: 10.1109/ACCESS.2023.3320045.

[2] V. T. Kiet and N. T. Cam, "When Does Classifier Calibration Reproduce Under Non-IID Federated Learning? A Controlled Study on a Faithful Flower Stack," in *Proc. 2026 10th IEEE Symposium on Wireless Technology & Applications (ISWTA 2026)*, Kuala Lumpur, Malaysia, Nov. 21–22, 2026. Đã được chấp nhận đăng (thư chấp nhận ngày 21/08/2026, bài số 1099); chưa có DOI vì hội nghị chưa diễn ra.

*Ghi chú cho học viên:*
- Định dạng theo IEEE, cùng kiểu với Tài liệu tham khảo. Hai mục này đánh số riêng [1], [2], không trộn vào danh mục tài liệu tham khảo; không trích chúng trong thân bài (IR#9).
- Nếu khoa yêu cầu ghi mức độ liên quan với luận văn: bài [2] là kết quả của phần thực nghiệm trên nền tảng Flower (Ch.5 mục 5.2); bài [1] là công bố trước đó của tác giả về học liên kết, không thuộc nội dung luận văn.
- Khi hội đồng hoặc khoa hỏi minh chứng cho bài [2], đính kèm thư chấp nhận `Acceptance Letter - ISWTA2026.pdf`. Khi kỷ yếu được xuất bản, bổ sung số trang và DOI.