# CHƯƠNG 3 — CƠ SỞ LÝ THUYẾT (hướng B)

> **KHỐI TRẠNG THÁI** · 24/09/2026
>
> | Mục (sau khi sửa) | Nguồn | Trạng thái |
> |---|---|---|
> | 3.1 Học liên kết và local SGD | Word | `[GIỮ]` + hàng 1–2 |
> | 3.2 Mô hình hoá dữ liệu không đồng nhất | Word | `[GIỮ]` |
> | 3.3 Global Mixup và xấp xỉ Taylor bậc nhất | Word | `[GIỮ]` + hàng 3 |
> | 3.4 Thiên lệch trong học cục bộ | Word | `[SỬA]` hàng 4–9, khối S1 |
> | **3.5 FedBR: dùng mẫu trung bình để giảm thiên lệch học cục bộ** | — | `[VIẾT]`, **mục mới, trọng tâm của chương theo hướng B**. Yêu cầu viết ở cuối file |
> | 3.6 Bộ phân lớp sinh so với phân biệt | Word mục 3.5 cũ | `[SỬA]` hàng 10–11, khối S2; **đổi số 3.5 → 3.6** |
>
> **Việc trong Word:**
> - chèn tiêu đề cấp 2 *"FedBR: dùng mẫu trung bình để giảm thiên lệch học cục bộ"* ngay trước *"Bộ phân lớp sinh so với phân biệt"*;
> - nếu tiêu đề dùng kiểu Heading tự đánh số thì Word tự dịch số;
> - sửa tay mọi chỗ thân bài viết "mục 3.5" (hàng 4 đã tính việc này).
>
> **Ràng buộc:**
> - Chương 3 không chứa số đo của luận văn; mọi số đo nằm ở Ch.5.
> - Mục 3.5 mô tả FedBR như phương pháp của Guo và cộng sự [11] (IR#11), và mô tả thành phần 2 đúng là ghép cặp theo từng mẫu (IR#6).
>
> Bảng dưới được chép từ `archive/2026-09-24_huong-bien-gioi-hieu-luc/03_chuong3.md`, khối `YÊU CẦU SỬA — 24/09/2026 (lượt 2)`. Cột "Trước" đã đối chiếu nguyên văn với Word ngày 24/09. Chỉ đổi hàng 4 (mục 3.5 → 3.6) và nhãn số mục ở hàng 10–11.

---

# YÊU CẦU SỬA — 24/09/2026 · Ch.3 theo hướng B

| # | Mục | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 3.1.1, đoạn "Mô hình được tách thành hai phần", **vế cuối** | `hai mục cuối chương xác định đó là thành phần nào` | …nó tập trung ở một trong hai thành phần, và hai mục cuối chương xác định đó là thành phần nào, theo cơ chế gì. | …nó tập trung ở một trong hai thành phần. Hai mục cuối chương nêu các giả thuyết về thành phần đó và về cơ chế hình thành thiên lệch; Chương 5 kiểm tra chúng bằng số đo. | Chương 3 không còn số đo |
| 2 | 3.1.1, đoạn ký hiệu $w_c$, **vế cuối** | `phần phân tích cơ chế ở cuối chương` | …là đại lượng trung tâm của phần phân tích cơ chế ở cuối chương. | …là đại lượng trung tâm của phần phân tích cơ chế ở Chương 5. | Như trên |
| 3 | 3.3.4, đoạn "Ánh xạ sang cài đặt", **câu cuối** | `ở đó nó là một chỗ mà mã và lý thuyết khớp nhau` | Chương 5 dùng quan sát này làm mốc đối chiếu cho phần kiểm toán mã nguồn, ở đó nó là một chỗ mà mã và lý thuyết khớp nhau. | Có một chỗ không khớp: số hạng thứ ba trong mã được lấy trung bình trên lô hai lần, nên đi vào mục tiêu với hệ số nhỏ hơn ⟨công thức: λ(1−λ)⟩ một thừa số bằng kích thước lô. Chương 4 trình bày hệ quả của sai lệch này đối với phép cô lập số hạng Taylor, và Chương 5 ghi nó vào danh mục kiểm toán. | Câu cũ sai một nửa: hệ số λ(1−λ) đúng, nhưng phép chuẩn hoá theo lô thì không (`INDEX_ma-nguon-va-ket-qua.md` F1) |
| 4 | 3.4.1, đoạn cuối, **vế cuối** | `mục tiếp theo làm việc đó bằng một kết quả lý thuyết cổ điển` | …nên phạm vi hiệu lực của nó cần được phát biểu cẩn thận; mục tiếp theo làm việc đó bằng một kết quả lý thuyết cổ điển. | …nên phạm vi hiệu lực của nó cần được phát biểu cẩn thận; mục 3.6 làm việc đó bằng một kết quả lý thuyết cổ điển. | Lỗi có sẵn: mục ngay sau là 3.4.2, không phải kết quả cổ điển |
| 5 | **3.4.2, tiêu đề** | `Thiên lệch ở bộ phân lớp là thiên lệch định hướng` | Thiên lệch ở bộ phân lớp là thiên lệch định hướng | Thiên lệch ở bộ phân lớp: độ lớn hay hướng | Tiêu đề cũ khẳng định một kết quả đo; Chương 3 chỉ đặt câu hỏi |
| 6 | 3.4.2, đoạn 1 | `Một trực giác phổ biến cho rằng` | *(giữ nguyên)* | *(giữ nguyên)* | — |
| 7 | 3.4.2, **đoạn 2 và đoạn 3** | `Tuy nhiên, kết quả thực nghiệm mâu thuẫn` và `Một chênh lệch chuẩn ở mức dưới 20%` | Tuy nhiên, kết quả thực nghiệm mâu thuẫn với trực giác đó. Trên một backbone không dùng chuẩn hoá theo lô, tỉ lệ giữa ⟨công thức⟩ và ⟨công thức⟩ ở tầng cuối chỉ vào khoảng 1.10 đến 1.17, tức gần như đồng đều. Trong khi đó, việc hiệu chuẩn lại tầng cuối làm thay đổi độ chính xác vài điểm phần trăm và nâng recall của lớp bị phục vụ kém nhất lên rất mạnh. ‖ Một chênh lệch chuẩn ở mức dưới 20% không thể tạo ra biến thiên recall lớn như vậy nếu cơ chế là co giãn độ lớn. Kết luận là thiên lệch nằm ở hướng của ranh giới quyết định, và hiệu chuẩn xoay ranh giới chứ không co giãn nó. | **Xoá cả hai đoạn, thay bằng đoạn thứ nhất và thứ hai của khối S1** | Số đo 1,10–1,17 và phần recall chuyển sang Ch.5 mục 5.2.4 |
| 8 | 3.4.2, **đoạn 4** | `Kết luận này quan trọng với luận văn vì hai lý do` | Kết luận này quan trọng với luận văn vì hai lý do. Thứ nhất, nó xác nhận chẩn đoán mà đề tài dựa vào: … Thứ hai, nó đặt ra câu hỏi mà Chương 5 trả lời: … | **Thay cả đoạn bằng đoạn thứ ba của khối S1** | Không còn "kết luận" nào ở Chương 3 |
| 9 | 3.4.2, **đoạn 5** | `Phạm vi của kết luận cần được nêu kèm` | Phạm vi của kết luận cần được nêu kèm: nó được đo trên một họ kiến trúc không dùng chuẩn hoá theo lô, và nguồn tự cảnh báo rằng… | **Xoá cả đoạn** | Chuyển sang Ch.5 mục 5.2.4; cụm "nguồn tự cảnh báo" coi bài hội nghị là nguồn ngoài |
| 10 | 3.5.2 (thành **3.6.2**), đoạn 1, **câu cuối** | `xác nhận thứ hạng này` | Đo lường trong [17] xác nhận thứ hạng này: head LDA dạng đóng cho mức cải thiện cao nhất, còn các phương án phân biệt tiệm cận nhưng không vượt. | Chương 5 kiểm tra thứ hạng này bằng thực nghiệm trên chính bài toán huấn luyện lại tầng cuối. | Không trích bài hội nghị. Thêm nữa, trong danh mục Word [17] là Ng–Jordan, nên câu cũ đang trích sai nguồn |
| 11 | 3.5.2 (thành **3.6.2**), **đoạn 3** | `Chế độ mẫu của phép đo cũng thuộc về phát biểu` | Chế độ mẫu của phép đo cũng thuộc về phát biểu. Phép đo trong [17] thực hiện ở ⟨công thức⟩, tức số mẫu ảo dùng để huấn luyện lại tầng cuối chỉ gấp khoảng bốn lần số chiều đặc trưng. Đây là chế độ mẫu hữu hạn, … như số liệu ở cuối chương cho thấy. | **Thay cả đoạn bằng khối S2** | Bỏ trích [17] và bỏ trỏ tới "cuối chương". Con số cụ thể của tỉ số chuyển sang Ch.5 |

### S1 — thân mới của mục 3.4.2, sau đoạn "Một trực giác phổ biến…"

Trực giác này là một giả thuyết đo được, và có một giả thuyết cạnh tranh với nó. Theo giả thuyết thứ nhất, thiên lệch nằm ở độ lớn: chuẩn $\ell_2$ của các vector trọng số theo lớp chênh nhau rõ rệt, và co giãn lại các chuẩn ấy là đủ để sửa phần lớn sai lệch. Theo giả thuyết thứ hai, thiên lệch nằm ở hướng của ranh giới quyết định: chuẩn của các vector trọng số gần như bằng nhau, nhưng ranh giới giữa các lớp bị xoay về phía những lớp chiếm đa số tại chỗ.

Hai giả thuyết để lại hai dấu vết khác nhau. Nếu thiên lệch nằm ở độ lớn, tỉ số giữa $\max_c \lVert w_c \rVert_2$ và $\min_c \lVert w_c \rVert_2$ phải xa 1. Nếu thiên lệch nằm ở hướng, tỉ số ấy gần 1, vậy mà hiệu chuẩn lại tầng cuối vẫn làm recall của lớp kém nhất đổi mạnh; một chênh lệch chuẩn nhỏ không thể tạo ra biến thiên recall lớn nếu cơ chế chỉ là co giãn. Hai đại lượng này đo được trên cùng một mô hình, và Chương 5 đo cả hai.

Việc phân định quan trọng với luận văn vì hai lý do. Mục tiêu của đề tài là tăng cường đặc trưng tại các vùng ranh giới quyết định để giảm sai lệch nhãn, và mục tiêu đó chỉ có cơ sở nếu thiên lệch thực sự nằm ở ranh giới, tức giả thuyết thứ hai đúng. Khi đó câu hỏi tiếp theo là đòn bẩy trộn trung bình có xoay được ranh giới ấy không, hay chỉ tác động lên những chiều ít mang thông tin.

### S2 — đoạn thay thế đoạn 3 của mục 3.5.2 (thành 3.6.2)

Chế độ mẫu cũng thuộc về phát biểu. Gọi $M_c$ là số mẫu ảo sinh cho mỗi lớp và $d$ là số chiều đặc trưng; tỉ số $M_c/d$ cho biết tầng cuối được huấn luyện lại trên bao nhiêu mẫu so với số chiều cần ước lượng. Khi tỉ số này nhỏ, mô hình ở chế độ mẫu hữu hạn, nơi khoảng cách giữa hai họ bộ phân lớp còn đo được; kết quả tiệm cận của Efron dự đoán khoảng cách ấy thu hẹp khi tỉ số tăng. Thứ hạng đo được ở một ngân sách mẫu ảo vì vậy không ngoại suy sang các ngân sách khác, và bản thân ngân sách mẫu ảo có thể làm đổi dấu mức cải thiện, như Chương 5 cho thấy.

*(Trong Word: $M_c$, $d$ và $M_c/d$ nhập bằng công cụ công thức.)*

**Tự kiểm lối viết trên S1 và S2:**
- không có dấu `—` chêm;
- một khuôn tương phản (*"hay chỉ tác động lên…"*), là câu hỏi nghiên cứu chứ không phải câu chốt;
- không có cụm sáo, không có câu rào.

Sau khi đoạn 5 của mục 3.4.2 bị xoá, Chương 3 không còn câu rào nào ngoài câu ở mục 3.5.1 *"Nó không phải một chặn cứng ở mọi cỡ mẫu."*; câu đó thuộc phát biểu toán học, không tính.

---

## Yêu cầu viết mục 3.5 — FedBR (chưa viết, chờ lượt sau)

**Độ dài:** khoảng 2–2,5 trang. **Vị trí trong lập luận:** mục 3.3 đã dẫn xuất hai cách dùng mẫu trung bình dựa trên Mixup (NaiveMix, FedMix); mục 3.4 nêu thiên lệch học cục bộ và hai giả thuyết về dạng của nó. Mục 3.5 trình bày cách dùng thứ ba: FedBR [11] dùng **cùng loại** mẫu trung bình để chống trực tiếp hai biểu hiện của thiên lệch học cục bộ.

**Nội dung bắt buộc:**
1. **Pseudo-data RSM.** Mỗi mẫu là trung bình của một nhóm ảnh cục bộ, đúng như mẫu trung bình đại diện ở (3.11). Khác biệt duy nhất: FedBR bỏ nhãn mềm, gán nhãn đều $1/C$. Nhánh Mixture của FedBR thì khác; chỉ nhắc một câu. Nêu rõ đây là **cùng kênh dữ liệu** với FedMix. Đó là lý do luận văn đặt ba phương pháp vào cùng một khung ở Chương 4.
2. **Thành phần 1: cân bằng đầu ra tầng phân lớp trên pseudo-data.** Viết hàm mất mát.
3. **Thành phần 2: bài toán min-max tương phản trên không gian đặc trưng.**
   - Một tầng chiếu được tối đa hoá để phân biệt đặc trưng cục bộ và toàn cục.
   - Bộ trích xuất cục bộ được tối thiểu hoá để đặc trưng của pseudo-data gần đặc trưng toàn cục và xa đặc trưng của dữ liệu thật cục bộ.
   - **Ghép cặp theo từng mẫu** (IR#6). Viết hàm mất mát, nêu hệ số $\mu$, $\lambda$, nhiệt độ $\tau$.
4. **Liên hệ với mục 3.4.** Thành phần 1 nhắm vào biểu hiện thứ nhất, bộ phân lớp thiên lệch. Thành phần 2 nhắm vào biểu hiện thứ hai và thứ ba, đặc trưng lệch và kém phân tách. Nêu câu hỏi cho Ch.5: nếu thiên lệch mang tính định hướng, thành phần nào của FedBR tác động lên hướng ranh giới quyết định.
5. **So với FedMix trên cùng kênh**, một đoạn ngắn: FedMix đưa thông tin của mẫu trung bình vào qua đầu vào và nhãn mềm; FedBR đưa vào qua đầu ra tầng phân lớp và không gian đặc trưng, không dùng nhãn. Không đánh giá hơn kém ở đây; việc đó thuộc Ch.5.

**Nguồn công thức, theo thứ tự ưu tiên:**
- (a) bài FedBR, `paper/ref/Guo et al. - 2023 - FedBR….pdf`, Mục 4 (phương pháp) và Thuật toán 1;
- (b) mã `fedbr/algorithms.py`, lớp `FedBR`, để biết mã thực sự tính gì;
- (c) bản chép lại `src/fedbr_repro/algo.py:207–315` trong kho Flower, có test chẵn lẻ với mã gốc.

Chỗ nào bài và mã lệch nhau thì viết theo bài ở Ch.3 và ghi độ lệch vào danh mục kiểm toán ở Ch.5. Hai độ lệch đã biết (IR#7): $\lambda$ = 0,1 trong bài và 1,0 trong mã; projection 256/128 trong bài và 1024/512 trong mã. **Không viết công thức theo trí nhớ.**

**Lối viết:** theo §7.7 của dàn bài. Mục này dễ rơi vào khuôn *"FedBR không phải … mà là …"*; dùng tối đa một lần, cho IR#6.

---

# PHIÊN BẢN CHỈNH SỬA — 24/09/2026 · mục 3.5 (mới): FedBR

> **Cách đọc.** Chỉ-append. Khối này là **thân mục 3.5 mới**, chép vào Word ngay trước mục *"Bộ phân lớp sinh so với phân biệt"*, mục này dịch thành 3.6. Các mục 3.1–3.4 và 3.6 sửa theo bảng ở khối `YÊU CẦU SỬA — 24/09/2026` phía trên.
>
> **Nguồn công thức: mã nguồn công bố của [11]**, theo yêu cầu của học viên, vì đó là bản mà thực nghiệm ở Chương 5 chạy. Đối chiếu từng công thức:
>
> | Công thức | Mã nguồn (kho `FedBR`) |
> |---|---|
> | (3.16) pseudo-data | `fedbr/scripts/train_fed.py:34–48` (`get_augmentation_mean_data`), gọi một lần trước vòng lặp ở `:420` |
> | $\phi_g$ chụp đầu mỗi vòng | `fedbr/algorithms.py:1120–1124`; cờ bật lại sau bước tổng hợp ở `train_fed.py:488` |
> | tầng chiếu $h$, chiều ẩn $2d$ | `algorithms.py:967–970` |
> | (3.17) $\ell_{\text{con}}$, ghép cặp theo chỉ số $k$ | `algorithms.py:1146–1151`; hàm `sim` là cosine, `:1036–1037` |
> | lượt tối đa hoá trên $h$ | `algorithms.py:1132–1143` (đặc trưng `detach`, dấu ngược, chỉ `disc_opt` bước) |
> | (3.18) $L_{\text{bal}}$, $q = 1/C$ | `algorithms.py:1114, 1158` |
> | (3.19) mục tiêu lượt tối thiểu hoá, $\mu = 0{,}5$, $\lambda = 1{,}0$, $\tau_1 = \tau_2 = 2$ | `algorithms.py:1091–1095, 1155–1170` |
> | nhánh Mixture | `algorithms.py:1060–1074, 1117–1118` |
> | nhánh Mixup | `algorithms.py:1076–1085, 1104–1107` |
>
> **Số phương trình (3.16)–(3.19)** tiếp nối (3.15) của FedMix trong Word. Nếu sửa chỗ hai phương trình cùng mang số (3.2) trong Word thì mọi số từ đó trở đi dịch lên một, kể cả bốn số này.
>
> **Tự kiểm §7.7:**
> - không có dấu `—` chêm, không có cụm sáo;
> - không có khuôn *"không phải … mà …"*;
> - không có câu rào; câu về nguồn công thức là phát biểu phương pháp, không phải câu rào;
> - IR#6: ghép cặp theo từng mẫu được nêu một lần, ở mục 3.5.3.

## 3.5. FedBR: dùng mẫu trung bình để giảm thiên lệch học cục bộ

Hai thuật toán ở mục 3.3 đưa mẫu trung bình đại diện vào mô hình qua đầu vào hoặc qua số hạng gradient. FedBR [11] dùng nó theo một lối khác: làm điểm tựa để chống trực tiếp các biểu hiện của thiên lệch học cục bộ nêu ở mục 3.4. Mục này mô tả phương pháp theo mã nguồn mà [11] công bố, vì đó là bản mà các thực nghiệm ở Chương 5 chạy; những chỗ mã nguồn khác mô tả trong bài báo được ghi ở phần kiểm toán của Chương 5.

### 3.5.1. Pseudo-data

Trước vòng truyền thông đầu tiên, FedBR dựng một tập pseudo-data gồm $P$ mẫu. Mỗi mẫu được tạo bằng cách chọn ngẫu nhiên một client, rút ngẫu nhiên có hoàn lại $M$ ảnh trong dữ liệu của client đó, rồi lấy trung bình:

$$u_p = \frac{1}{M}\sum_{m=1}^{M} x_{p,m}, \qquad p = 1, \ldots, P. \tag{3.16}$$

Trong mã nguồn, $P$ bằng kích thước lô cục bộ $B = 32$ và $M = 10$. Tập $\{u_p\}$ được dựng một lần, rồi dùng chung cho mọi client ở mọi bước huấn luyện.

So với (3.11), $u_p$ chính là mẫu trung bình đại diện $\bar x_g$, chỉ thiếu nhãn mềm $\bar y_g$. FedBR không dùng nhãn của pseudo-data. Mỗi mẫu được gán nhãn đều $q = \frac{1}{C}\mathbf{1}$, tức mô hình được yêu cầu không nghiêng về lớp nào khi nhìn một ảnh trung bình. Như vậy NaiveMix, FedMix và FedBR nhận cùng một loại dữ liệu từ các client khác, và chỉ khác nhau ở cách dữ liệu ấy đi vào hàm mất mát cục bộ. Chương 4 dựng khung thực nghiệm trên đúng nhận xét này.

Mã nguồn còn một nhánh gọi là Mixture: mỗi pseudo-sample được trộn đều với một ảnh cục bộ $x_j$ chọn ngẫu nhiên, và nhãn đi kèm là $\frac{1}{2}\big(\frac{1}{C}\mathbf{1} + y_j\big)$. Luận văn không dùng nhánh này.

### 3.5.2. Ký hiệu

Giữ ký hiệu của mục 3.1: $\phi$ là bộ trích xuất đặc trưng và $\omega$ là bộ phân lớp của client đang huấn luyện. Ký hiệu thêm:
- $\phi_g$: bản sao của bộ trích xuất toàn cục mà client nhận ở đầu vòng truyền thông hiện tại. Bản sao này không được cập nhật trong suốt vòng.
- $h$: một **tầng chiếu**, là mạng MLP ánh xạ $\mathbb{R}^d \to \mathbb{R}^d$ với chiều ẩn $2d$.
- $s(\cdot,\cdot)$: độ tương tự cosine.

Ở mỗi bước cục bộ, client có một lô $\{(x_k, y_k)\}_{k=1}^{B}$ và tập pseudo-data $\{u_k\}_{k=1}^{B}$ cùng kích thước. Mẫu thứ $k$ của hai tập được ghép với nhau theo chỉ số. Với mỗi $k$, đặt

$$a_k = h\big(\phi(u_k)\big), \qquad b_k = h\big(\phi_g(u_k)\big), \qquad c_k = h\big(\phi(x_k)\big).$$

Ba vector này lần lượt là hình chiếu của: đặc trưng cục bộ của pseudo-sample, đặc trưng toàn cục của cùng pseudo-sample đó, và đặc trưng cục bộ của một ảnh thật.

### 3.5.3. Thành phần tương phản

FedBR định nghĩa cho mỗi $k$ một hàm mất mát tương phản với một cặp dương và một cặp âm:

$$\ell_{\text{con}}(k) = -\log \frac{\exp\big(\tau_1\, s(a_k, b_k)\big)}{\exp\big(\tau_1\, s(a_k, b_k)\big) + \exp\big(\tau_2\, s(a_k, c_k)\big)}, \tag{3.17}$$

trong đó $\tau_1$ và $\tau_2$ là hai hệ số nhiệt độ. Cặp dương gồm đặc trưng cục bộ và đặc trưng toàn cục của **cùng một** pseudo-sample. Cặp âm gồm đặc trưng cục bộ của pseudo-sample và đặc trưng cục bộ của một ảnh thật. $\ell_{\text{con}}(k)$ nhỏ khi bộ trích xuất cục bộ nhìn pseudo-sample giống như bộ trích xuất toàn cục nhìn nó, đồng thời khác với cách nó nhìn dữ liệu của chính client.

Phép ghép cặp diễn ra theo từng mẫu, trên cùng một đầu vào đi qua hai bộ trích xuất. Ràng buộc này chặt hơn một phép căn chỉnh phân phối biên: căn chỉnh biên chỉ đòi hai tập đặc trưng có cùng thống kê tổng, còn (3.17) đòi từng đặc trưng cục bộ gần đúng đặc trưng toàn cục của cùng mẫu.

Thành phần này được tối ưu theo lối min-max, với hai lượt cập nhật trong mỗi bước cục bộ.

**Lượt tối đa hoá** chỉ cập nhật tầng chiếu $h$. Đặc trưng $\phi(u_k)$ và $\phi(x_k)$ được tách khỏi đồ thị tính gradient, và $h$ được cập nhật để **tăng** trung bình $\frac{1}{B}\sum_k \ell_{\text{con}}(k)$. Tầng chiếu vì vậy học cách làm nổi bật chỗ khác nhau giữa đặc trưng cục bộ và đặc trưng toàn cục của pseudo-data, tức tìm những hướng mà bộ trích xuất cục bộ đã trôi xa nhất.

**Lượt tối thiểu hoá** giữ $h$ cố định và cập nhật $\phi$, $\omega$ theo mục tiêu ở mục 3.5.5. Trong lượt này $\phi$ phải kéo đặc trưng cục bộ của pseudo-data về gần đặc trưng toàn cục, dọc theo đúng những hướng mà $h$ vừa làm nổi bật.

### 3.5.4. Thành phần cân bằng tầng phân lớp

Thành phần thứ hai nhìn vào đầu ra của tầng phân lớp trên pseudo-data:

$$L_{\text{bal}} = -\frac{1}{B}\sum_{k=1}^{B}\sum_{c=1}^{C} q_c \log \mathrm{softmax}\big(\omega(\phi(u_k))\big)_c, \qquad q_c = \frac{1}{C}. \tag{3.18}$$

$L_{\text{bal}}$ là cross-entropy giữa phân phối dự đoán trên một pseudo-sample và phân phối đều. Các pseudo-sample được rút từ những client chọn ngẫu nhiên, nên xét trên cả tập, pseudo-data không nghiêng về các lớp chiếm đa số của riêng client đang huấn luyện. Một tầng phân lớp đã nghiêng về các lớp chiếm đa số tại chỗ sẽ gán cho các ảnh trung bình này xác suất cao ở chính những lớp đó, và $L_{\text{bal}}$ phạt đúng xu hướng ấy.

### 3.5.5. Mục tiêu cục bộ

Lượt tối thiểu hoá cập nhật $\phi$ và $\omega$ theo

$$L_{\text{FedBR}} = \underbrace{-\frac{1}{B}\sum_{k=1}^{B}\sum_{c=1}^{C} y_{k,c}\,\log \mathrm{softmax}\big(\omega(\phi(x_k))\big)_c}_{\text{cross-entropy trên dữ liệu cục bộ}} \;+\; \mu\,\frac{1}{B}\sum_{k=1}^{B}\ell_{\text{con}}(k) \;+\; \lambda\,L_{\text{bal}}, \tag{3.19}$$

với $y_k$ ở dạng one-hot. Mã nguồn đặt $\mu = 0{,}5$, $\lambda = 1{,}0$ và $\tau_1 = \tau_2 = 2{,}0$.

Hai thành phần nhắm vào các biểu hiện khác nhau của thiên lệch học cục bộ ở mục 3.4.1. $L_{\text{bal}}$ tác động lên đầu ra của tầng phân lớp, tức biểu hiện thứ nhất. $\ell_{\text{con}}$ tác động lên không gian đặc trưng: nó kéo đặc trưng cục bộ về gần đặc trưng toàn cục (biểu hiện thứ hai) và giữ khoảng cách giữa pseudo-data với dữ liệu cục bộ (biểu hiện thứ ba).

Mã nguồn còn cho phép thay lô cục bộ bằng các ảnh cục bộ được trộn theo Mixup, với trọng số trộn rút từ phân phối $\mathrm{Beta}(0{,}2;\ 0{,}2)$ và nhãn trộn theo cùng tỉ lệ. Biến thể này, gọi là FedBR + Mixup, chỉ đổi số hạng cross-entropy trong (3.19); cách FedBR dùng pseudo-data giữ nguyên.

### 3.5.6. So với FedMix trên cùng một loại dữ liệu

Đặt (3.19) cạnh (3.15) thì thấy hai phương pháp lấy thông tin từ mẫu trung bình ở hai chỗ khác nhau của mô hình.
- **FedMix** dùng cả ảnh trung bình lẫn nhãn mềm. Ảnh đi vào qua tích vô hướng với gradient của hàm mất mát theo đầu vào; nhãn đi vào qua số hạng (II).
- **FedBR** bỏ nhãn. Ảnh trung bình đi vào qua đầu ra của tầng phân lớp, với đích là phân phối đều, và qua không gian đặc trưng, với đích là đặc trưng toàn cục của chính nó.

Theo hai giả thuyết ở mục 3.4.2, nếu thiên lệch của tầng phân lớp nằm ở hướng của ranh giới quyết định, thì phương pháp nào tác động được lên hướng đó mới có cơ hội cải thiện. Mục này không đánh giá phương pháp nào tốt hơn. Chương 4 đặt ba cách dùng vào cùng một khung, và Chương 5 so sánh chúng bằng thực nghiệm.

---

# RÀ SOÁT — 25/09/2026 · Chương 3 theo Word hiện tại
> **Cách đọc.** Chỉ-append (Chương 3 đã có trong Word). Rà trên bản Word lưu lúc 01:18 ngày 25/09, đối chiếu với các quyết định 25/09: Ch.4 chỉ trình bày đề xuất, thiết lập thực nghiệm nằm ở Ch.5 mục 5.1, kiểm toán mã chuyển sang Phụ lục A, không nói về mã nguồn trong thân bài. Mỗi cụm ở cột *Tìm trong Word* đã kiểm là xuất hiện **đúng một lần** trong văn bản Word. `⟨…⟩` là chỗ có công thức trong Word.
>
> **Số trích dẫn.** Danh mục Word hiện đánh [1] FedMix, **[2] FedBR**, [3] FedAvg, [8] CCVR, [10] Mixup, [11] VHL. Word Ch.3 đã dùng [2] cho FedBR; các khối cũ trong file này (bảng 24/09, thân mục 3.5 bên trên) còn ghi **[11]**, khi chép phải đổi thành **[2]**.
>
> **Tự kiểm §7.7** trên các câu mới: không có dấu `—` chêm, không thêm khuôn tương phản mới (ba gạch đầu dòng ở hàng 17 là câu cũ của học viên, giữ theo AI#10), không có câu rào.

## A. Sửa các đoạn đã có trong Word

| # | Mục | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 3.1.1, đoạn "Mô hình được tách thành hai phần", **câu cuối** | `Hai mục cuối chương nêu các giả thuyết về thành phần đó` | Hai mục cuối chương nêu các giả thuyết về thành phần đó và về cơ chế hình thành thiên lệch; Chương 5 kiểm tra chúng bằng số đo. | Mục 3.4 nêu các giả thuyết về thành phần đó và về cơ chế hình thành thiên lệch; Chương 5 kiểm tra chúng bằng số đo. | Hai mục cuối chương giờ là 3.5 FedBR và 3.6 bộ phân lớp sinh/phân biệt; các giả thuyết nằm ở 3.4 |
| 2 | 3.1.1, đoạn "Chiều đặc trưng", **cả đoạn** | `với ResNet20-GN` | Chiều đặc trưng ⟨d⟩ phụ thuộc kiến trúc và được ghi rõ ở mọi bảng kết quả: ⟨…⟩ với VGG11 và ResNet18, ⟨…⟩ với CCT, ⟨…⟩ với ResNet20-GN. Đây không phải một hằng số của bài toán, và hai kết quả đo trên hai backbone khác nhau là hai kết quả ở hai chiều đặc trưng khác nhau. | Chiều đặc trưng ⟨d⟩ phụ thuộc kiến trúc và được ghi rõ ở mọi bảng kết quả. Cả hai backbone dùng trong luận văn đều cho ⟨d = 512⟩ (Chương 5, Bảng 5.1). | ResNet18, CCT, ResNet20-GN không có trong thực nghiệm của luận văn |
| 3 | 3.1.2, đoạn "Hai đại lượng điều khiển", **câu cuối** | `cấu hình đã đăng ký và khảo sát trục thứ hai` | Luận văn giữ ⟨K⟩ cố định ở giá trị của cấu hình đã đăng ký và khảo sát trục thứ hai, nên mọi so sánh trong Chương 5 diễn ra ở cùng một ngân sách bước cục bộ. | Luận văn giữ ⟨K⟩ cố định trong mỗi nền tảng thực nghiệm, nên mọi so sánh trong cùng một nền tảng ở Chương 5 diễn ra ở cùng một ngân sách bước cục bộ. | Hai nền tảng có ⟨K⟩ khác nhau (2 epoch và 50 bước, Bảng 5.1); "cấu hình đã đăng ký" là cách gọi của hướng cũ |
| 4 | 3.1.2, đoạn "Cần phân biệt client drift", **vế cuối** | `phần sau của chương trả lời nó bằng bằng chứng đo được` | …là một câu hỏi tách biệt, và phần sau của chương trả lời nó bằng bằng chứng đo được. | …là một câu hỏi tách biệt. Mục 3.4 nêu các giả thuyết về câu hỏi này, và Chương 5 kiểm tra chúng bằng số đo. | Chương 3 không còn số đo; câu cũ còn lặp chữ "bằng bằng" |
| 5 | 3.2.1, đoạn "Hai trục này độc lập", **vế cuối** | `quay lại nó với số đo cụ thể` | …và phần phân tích thiên lệch ở cuối chương quay lại nó với số đo cụ thể. | …và mục 3.4 quay lại nó. | Chương 3 không còn số đo |
| 6 | 3.2.2, công thức đơn hình ngay sau "Phân phối Dirichlet bậc" | `Phân phối Dirichlet bậc` | công thức mang số (3.2), trùng số với mục tiêu của hệ thống ở 3.1.1 | **bỏ số phương trình** của công thức đơn hình; các số (3.3) trở đi giữ nguyên | Hai phương trình cùng số (3.2). Bỏ số ở công thức đơn hình thì không phải đánh lại (3.3)–(3.19), vốn được Ch.4 và Ch.5 viện dẫn. Kiểm tra trước là không có chỗ nào viện dẫn công thức đơn hình |
| 7 | 3.2.2, đoạn "Theo quy ước trên", **đầu câu** | `cấu hình đã đăng ký là` | Theo quy ước trên, cấu hình đã đăng ký là ⟨…⟩ trên CIFAR-10… | Theo quy ước trên, cấu hình của nền tảng FedBR (Chương 5, mục 5.1) là ⟨…⟩ trên CIFAR-10… | "Cấu hình đã đăng ký" là cách gọi của hướng cũ |
| 8 | 3.2.3, gạch đầu dòng thứ nhất, **câu cuối** | `Đường đặc tuyến theo` | Đường đặc tuyến theo ⟨α_rot⟩ trong Chương 5 vì vậy là một nhánh, không đối xứng hai phía. | Luận văn chỉ chạy ở cấu hình mặc định này, nên mọi kết luận về lệch đặc trưng chỉ áp cho mức lệch nặng đó. | Hướng B không quét ⟨α_rot⟩; Chương 5 không có đường đặc tuyến nào theo trục xoay |
| 9 | 3.3.4, đoạn "Phép bỏ số hạng (IV)", **vế cuối** | `lấy chính điều đó làm một trong các yếu tố gây nhiễu` | …mức cải thiện đo được cũng phụ thuộc ⟨λ⟩ theo một cách không đơn điệu hiển nhiên, và Chương 4 lấy chính điều đó làm một trong các yếu tố gây nhiễu phải loại trừ. | …mức cải thiện đo được cũng phụ thuộc ⟨λ⟩ theo một cách không đơn điệu hiển nhiên. Luận văn vì vậy giữ ⟨λ⟩ cố định trong mỗi nền tảng thực nghiệm (Chương 5, mục 5.1) và không so mức cải thiện giữa hai giá trị ⟨λ⟩ khác nhau. | Chương 4 không còn mục yếu tố gây nhiễu theo ⟨λ⟩. **Cùng chỗ này:** Word đang có một dấu xuống đoạn thừa ngay trước ⟨λ⟩ ở câu *"…cũng phụ thuộc ⟨λ⟩ theo một cách…"*, làm đoạn bị cắt đôi; nối lại thành một đoạn |
| 10 | 3.3.4, câu ngay sau công thức tỉ lệ (IV)/(III) | `Tỷ lệ này nhận giá trị` | Tỷ lệ này nhận giá trị… | Tỉ lệ này nhận giá trị… | Câu ngay trước viết "Tỉ lệ"; thống nhất một cách viết |
| 11 | 3.3.4, đoạn **"Ánh xạ sang cài đặt"** | `Ánh xạ sang cài đặt` | Ánh xạ sang cài đặt. Ba số hạng của ⟨…⟩ (3.15) ứng một-một với ba đại lượng trong thực nghiệm FedMix của nền tảng FedBR [2]: … Chương 4 trình bày hệ quả của sai lệch này đối với phép cô lập số hạng Taylor, và Chương 5 ghi nó vào danh mục kiểm toán. | **Xoá cả đoạn** | Đoạn nói về tên biến và thứ tự tính trong mã. Phần có giá trị khoa học (hệ số ⟨λ(1−λ)⟩ đúng, thừa ⟨1/B⟩) đã nằm ở Ch.4 mục 4.3 dưới dạng lập luận; phần về mã nằm ở Phụ lục A. "Phép cô lập số hạng Taylor" là mục tiêu của hướng cũ |
| 12 | 3.4.1, đoạn "FedBR [2]phân tách" | `[2]phân tách` | FedBR [2]phân tách… | FedBR [2] phân tách… | Thiếu dấu cách |
| 13 | 3.4.1, đoạn "Hiện tượng thứ hai", **câu đầu** | `Hiện tượng thứ hai xác nhận bằng số đo` | Hiện tượng thứ hai xác nhận bằng số đo điều mà phép phân rã phân phối ở đầu chương mới chỉ nêu ở mức khái niệm. | Hiện tượng thứ hai, được [2] ghi nhận bằng thực nghiệm, cho thấy cụ thể điều mà phép phân rã phân phối ở mục 3.2.1 mới chỉ nêu ở mức khái niệm. | Số đo là của [2], không phải của luận văn; phép phân rã nằm ở 3.2.1, không ở đầu chương |
| 14 | 3.5.1, câu ngay sau (3.16) | `bằng kích thước lô cục bộ` | ⟨P⟩ bằng kích thước lô cục bộ ⟨B = 32⟩ và ⟨M = 10⟩. | Trong các thực nghiệm ở Chương 5, ⟨P⟩ bằng kích thước lô cục bộ ⟨B = 32⟩ và ⟨M = 10⟩. | Câu đang mở đầu bằng ký hiệu toán; nói rõ đây là giá trị thực nghiệm |
| 15 | 3.5.1, đoạn "So với công thức (3.11)", **câu cuối** | `dựng khung thực nghiệm trên đúng nhận xét này` | Chương 4 dựng khung thực nghiệm trên đúng nhận xét này. | Chương 4 dựng khung đề xuất trên đúng nhận xét này. | Chương 4 giờ là khung đề xuất; thiết lập thực nghiệm nằm ở Chương 5 |
| 16 | 3.5.1, đoạn cuối | `Mã nguồn còn một nhánh gọi là Mixture` | Mã nguồn còn một nhánh gọi là Mixture: … | FedBR còn có một biến thể gọi là Mixture: … | Không nói về mã nguồn trong thân chương |
| 17 | 3.6.3, đoạn mở và ba gạch đầu dòng | `tức mẫu trung bình đại diện kết hợp khai triển Taylor` | Cơ chế mà luận văn nghiên cứu, tức mẫu trung bình đại diện kết hợp khai triển Taylor, không lấy mẫu từ bất kỳ mô hình Gaussian nào. Nó thao tác trên: ‖ Không gian đầu vào, không phải không gian đặc trưng; ‖ Dữ liệu thật đã được lấy trung bình, không phải mẫu tổng hợp; ‖ Thống kê bậc nhất của dữ liệu thô, không phải moment của đặc trưng. | Các cách dùng mẫu trung bình mà luận văn nghiên cứu, gồm NaiveMix, FedMix và FedBR, không lấy mẫu từ bất kỳ mô hình Gaussian nào. Dữ liệu mà chúng dùng: ‖ nằm trong không gian đầu vào, không phải không gian đặc trưng; ‖ là dữ liệu thật đã được lấy trung bình, không phải mẫu tổng hợp; ‖ mang thống kê bậc nhất của dữ liệu thô, không phải moment của đặc trưng. | Theo hướng B, luận văn nghiên cứu ba cách dùng, và FedBR không dùng khai triển Taylor. FedBR đặt hàm mất mát trên không gian đặc trưng, nên câu dẫn đổi sang "dữ liệu mà chúng dùng" để gạch đầu dòng thứ nhất vẫn đúng |
| 18 | 3.6.3, đoạn cuối, **câu đầu** | `Trần LDA vì vậy không ràng buộc cơ chế này` | Trần LDA vì vậy không ràng buộc cơ chế này. | Trần LDA vì vậy không ràng buộc các cách dùng này. | Đi theo hàng trên |

*`‖` trong một ô là ranh giới giữa hai đoạn hoặc hai gạch đầu dòng.*

## B. Khi chép 3.5.2–3.5.6 vào Word

Word hiện mới có mục 3.5 đến hết 3.5.1. Các tiểu mục 3.5.2–3.5.6 lấy từ khối `PHIÊN BẢN CHỈNH SỬA — 24/09/2026 · mục 3.5` bên trên, với bốn thay đổi:

1. **[11] → [2]** ở mọi chỗ.
2. **Đổi ký hiệu trọng số của $L_{\text{bal}}$ từ $\lambda$ sang $\gamma$**, vì $\lambda$ đã là trọng số trộn của NaiveMix và FedMix ở mục 3.3. Công thức (3.19) thành

$$L_{\text{FedBR}} = \underbrace{-\frac{1}{B}\sum_{k=1}^{B}\sum_{c=1}^{C} y_{k,c}\,\log \mathrm{softmax}\big(\omega(\phi(x_k))\big)_c}_{\text{cross-entropy trên dữ liệu cục bộ}} \;+\; \mu\,\frac{1}{B}\sum_{k=1}^{B}\ell_{\text{con}}(k) \;+\; \gamma\,L_{\text{bal}}, \tag{3.19}$$

   Đã kiểm trong file Word: chữ $\gamma$ thường chưa xuất hiện ở đâu (chỉ có $\Gamma$ hoa của hàm Gamma trong mật độ Dirichlet). Ch.5 Bảng 5.2 đã đổi theo.
3. **3.5.5, câu ngay sau (3.19).** Trước: *"với $y_k$ ở dạng one-hot. Mã nguồn đặt $\mu = 0{,}5$, $\lambda = 1{,}0$ và $\tau_1 = \tau_2 = 2{,}0$."* Sau: *"với $y_k$ ở dạng one-hot. Các thực nghiệm ở Chương 5 dùng $\mu = 0{,}5$, $\gamma = 1{,}0$ và $\tau_1 = \tau_2 = 2{,}0$ (Bảng 5.2)."*
4. **3.5.5, đoạn cuối.** Trước: *"Mã nguồn còn cho phép thay lô cục bộ bằng các ảnh cục bộ được trộn theo Mixup,"* Sau: *"FedBR còn có một biến thể thay lô cục bộ bằng các ảnh cục bộ được trộn theo Mixup,"*. Phần còn lại của câu giữ nguyên.

Câu *"Mục này mô tả phương pháp theo mã nguồn mà [11] công bố…"* ở đoạn mở mục 3.5 của khối bên trên **không chép**; Word đã bỏ câu này, và nên giữ như vậy.

## C. Ngoài Chương 3, phát hiện khi rà

- **Ch.4 trong Word, mục 4.4:** *"cấu hình pseudo-data của [11]"* phải là **[2]**. Đã ghi ở cuối `04_chuong4.md`.
- **Ch.2 trong Word:** tiêu đề *"Cô lập số hạng khai triển Taylor"* ở mục Khoảng trống luận văn là mục tiêu của hướng cũ. Bảng sửa Ch.2 (`02_chuong2.md`) cần một lượt rà tương tự.
- **Ch.1, Ch.2 (md):** các bảng sửa ở hai file này còn ghi FedBR là [11]; khi chép vào Word dùng [2].

---

# PHIÊN BẢN CHỈNH SỬA — 26/09/2026 · mục 3.5 viết lại, bỏ tiểu mục "Ký hiệu"

> **Cách đọc.** Chỉ-append. Khối này **thay** thân mục 3.5 của khối `PHIÊN BẢN CHỈNH SỬA — 24/09/2026 · mục 3.5` bên trên, và thay luôn phần B của khối `RÀ SOÁT — 25/09/2026`. Khi chép 3.5.2 trở đi vào Word, dùng khối này.
>
> **Đã có trong Word, giữ nguyên:** đoạn mở mục 3.5 và tiểu mục 3.5.1 Pseudo-data, cùng ba sửa ở hàng 14–16 của khối `RÀ SOÁT — 25/09/2026`. Văn bản dưới chép lại hai phần này, đã áp ba hàng đó, để đọc liền mạch; trong Word chỉ cần sửa theo ba hàng ấy.
>
> **Thay đổi so với bản 24/09:**
> - **bỏ tiểu mục "3.5.2 Ký hiệu".** Mỗi ký hiệu được giới thiệu ngay tại chỗ nó xuất hiện lần đầu: $\phi_g$, $h$, $s(\cdot,\cdot)$ và cách ghép cặp ở đầu tiểu mục thành phần tương phản;
> - đánh lại tiểu mục: 3.5.2 Thành phần tương phản trên không gian đặc trưng · 3.5.3 Thành phần cân bằng tầng phân lớp · 3.5.4 Mục tiêu cục bộ · 3.5.5 So với FedMix trên cùng một loại dữ liệu. **Số phương trình (3.16)–(3.19) giữ nguyên.** Không chương nào khác viện dẫn số tiểu mục của 3.5;
> - câu "lượt tối thiểu hoá … theo mục tiêu ở mục 3.5.5" đổi thành "mục 3.5.4";
> - bỏ mọi chỗ nói về mã nguồn: kích thước tầng chiếu chuyển sang Ch.5 Bảng 5.2; giá trị $\mu$, $\gamma$, $\tau$ ghi là giá trị thực nghiệm; nhánh Mixture và biến thể Mixup viết là biến thể của FedBR;
> - trọng số của $L_{\text{bal}}$ dùng $\gamma$ (lý do ở khối `RÀ SOÁT — 25/09/2026`, phần B); trích dẫn FedBR là [2].
>
> **Tự kiểm §7.7:**
> - không có dấu `—` chêm, không có cụm sáo, không có câu rào;
> - một khuôn tương phản, giữ từ bản 24/09: *"căn chỉnh biên chỉ đòi …, còn (3.17) đòi …"* ở 3.5.2, dùng cho IR#6;
> - câu *"Việc so sánh diễn ra sau một tầng chiếu"* viết thẳng, tránh khuôn *"không so trực tiếp … mà qua …"*.

## 3.5. FedBR: dùng mẫu trung bình để giảm thiên lệch học cục bộ

Hai thuật toán ở mục 3.3 đưa mẫu trung bình đại diện vào mô hình qua đầu vào hoặc qua số hạng gradient. FedBR [2] dùng nó theo một lối khác: làm điểm tựa để chống trực tiếp các biểu hiện của thiên lệch học cục bộ nêu ở mục 3.4.

### 3.5.1. Pseudo-data

Trước vòng truyền thông đầu tiên, FedBR dựng một tập pseudo-data gồm $P$ mẫu. Mỗi mẫu được tạo bằng cách chọn ngẫu nhiên một client, rút ngẫu nhiên có hoàn lại $M$ ảnh trong dữ liệu của client đó, rồi lấy trung bình:

$$u_p = \frac{1}{M}\sum_{m=1}^{M} x_{p,m}, \qquad p = 1, \ldots, P. \tag{3.16}$$

Trong các thực nghiệm ở Chương 5, $P$ bằng kích thước lô cục bộ $B = 32$ và $M = 10$. Tập $\{u_p\}$ được dựng một lần, rồi dùng chung cho mọi client ở mọi bước huấn luyện.

So với (3.11), $u_p$ chính là mẫu trung bình đại diện $\bar x_g$, chỉ thiếu nhãn mềm $\bar y_g$. FedBR không dùng nhãn của pseudo-data. Mỗi mẫu được gán nhãn đều $q = \frac{1}{C}\mathbf{1}$, tức mô hình được yêu cầu không nghiêng về lớp nào khi nhìn một ảnh trung bình. Như vậy NaiveMix, FedMix và FedBR nhận cùng một loại dữ liệu từ các client khác, và chỉ khác nhau ở cách dữ liệu ấy đi vào hàm mất mát cục bộ. Chương 4 dựng khung đề xuất trên đúng nhận xét này.

FedBR còn có một biến thể gọi là Mixture: mỗi pseudo-sample được trộn đều với một ảnh cục bộ $x_j$ chọn ngẫu nhiên, và nhãn đi kèm là $\frac{1}{2}\big(\frac{1}{C}\mathbf{1} + y_j\big)$. Luận văn không dùng biến thể này.

### 3.5.2. Thành phần tương phản trên không gian đặc trưng

Thành phần thứ nhất so sánh cách hai bộ trích xuất đặc trưng nhìn cùng một pseudo-sample. Bộ trích xuất cục bộ $\phi$, ký hiệu như ở mục 3.1, thay đổi sau mỗi bước huấn luyện. Ở đầu mỗi vòng truyền thông, client giữ lại thêm một bản sao $\phi_g$ của bộ trích xuất toàn cục vừa nhận, và bản sao này đứng yên trong suốt vòng. Việc so sánh diễn ra sau một tầng chiếu $h$, là một mạng MLP nhỏ ánh xạ $\mathbb{R}^d$ vào chính nó, và độ giống nhau giữa hai vector được đo bằng độ tương tự cosine $s(\cdot,\cdot)$.

Ở mỗi bước cục bộ, client có một lô $\{(x_k, y_k)\}_{k=1}^{B}$ và tập pseudo-data $\{u_k\}_{k=1}^{B}$ cùng kích thước; mẫu thứ $k$ của hai tập được ghép với nhau theo chỉ số. Với mỗi $k$, đặt

$$a_k = h\big(\phi(u_k)\big), \qquad b_k = h\big(\phi_g(u_k)\big), \qquad c_k = h\big(\phi(x_k)\big).$$

Ba vector này lần lượt là hình chiếu của đặc trưng cục bộ của pseudo-sample, đặc trưng toàn cục của cùng pseudo-sample đó, và đặc trưng cục bộ của một ảnh thật. FedBR định nghĩa cho mỗi $k$ một hàm mất mát tương phản với một cặp dương và một cặp âm:

$$\ell_{\text{con}}(k) = -\log \frac{\exp\big(\tau_1\, s(a_k, b_k)\big)}{\exp\big(\tau_1\, s(a_k, b_k)\big) + \exp\big(\tau_2\, s(a_k, c_k)\big)}, \tag{3.17}$$

trong đó $\tau_1$ và $\tau_2$ là hai hệ số nhiệt độ. Cặp dương gồm đặc trưng cục bộ và đặc trưng toàn cục của **cùng một** pseudo-sample. Cặp âm gồm đặc trưng cục bộ của pseudo-sample và đặc trưng cục bộ của một ảnh thật. $\ell_{\text{con}}(k)$ nhỏ khi bộ trích xuất cục bộ nhìn pseudo-sample giống như bộ trích xuất toàn cục nhìn nó, đồng thời khác với cách nó nhìn dữ liệu của chính client.

Phép ghép cặp diễn ra theo từng mẫu, trên cùng một đầu vào đi qua hai bộ trích xuất. Ràng buộc này chặt hơn một phép căn chỉnh phân phối biên: căn chỉnh biên chỉ đòi hai tập đặc trưng có cùng thống kê tổng, còn (3.17) đòi từng đặc trưng cục bộ gần đúng đặc trưng toàn cục của cùng mẫu.

Thành phần này được tối ưu theo lối min-max, với hai lượt cập nhật trong mỗi bước cục bộ.

**Lượt tối đa hoá** chỉ cập nhật tầng chiếu $h$. Đặc trưng $\phi(u_k)$ và $\phi(x_k)$ được tách khỏi đồ thị tính gradient, và $h$ được cập nhật để **tăng** trung bình $\frac{1}{B}\sum_k \ell_{\text{con}}(k)$. Tầng chiếu vì vậy học cách làm nổi bật chỗ khác nhau giữa đặc trưng cục bộ và đặc trưng toàn cục của pseudo-data, tức tìm những hướng mà bộ trích xuất cục bộ đã trôi xa nhất.

**Lượt tối thiểu hoá** giữ $h$ cố định và cập nhật $\phi$, $\omega$ theo mục tiêu ở mục 3.5.4. Trong lượt này $\phi$ phải kéo đặc trưng cục bộ của pseudo-data về gần đặc trưng toàn cục, dọc theo đúng những hướng mà $h$ vừa làm nổi bật.

### 3.5.3. Thành phần cân bằng tầng phân lớp

Thành phần thứ hai nhìn vào đầu ra của tầng phân lớp trên pseudo-data:

$$L_{\text{bal}} = -\frac{1}{B}\sum_{k=1}^{B}\sum_{c=1}^{C} q_c \log \mathrm{softmax}\big(\omega(\phi(u_k))\big)_c, \qquad q_c = \frac{1}{C}. \tag{3.18}$$

$L_{\text{bal}}$ là cross-entropy giữa phân phối dự đoán trên một pseudo-sample và phân phối đều. Các pseudo-sample được rút từ những client chọn ngẫu nhiên, nên xét trên cả tập, pseudo-data không nghiêng về các lớp chiếm đa số của riêng client đang huấn luyện. Một tầng phân lớp đã nghiêng về các lớp chiếm đa số tại chỗ sẽ gán cho các ảnh trung bình này xác suất cao ở chính những lớp đó, và $L_{\text{bal}}$ phạt đúng xu hướng ấy.

### 3.5.4. Mục tiêu cục bộ

Lượt tối thiểu hoá cập nhật $\phi$ và $\omega$ theo

$$L_{\text{FedBR}} = \underbrace{-\frac{1}{B}\sum_{k=1}^{B}\sum_{c=1}^{C} y_{k,c}\,\log \mathrm{softmax}\big(\omega(\phi(x_k))\big)_c}_{\text{cross-entropy trên dữ liệu cục bộ}} \;+\; \mu\,\frac{1}{B}\sum_{k=1}^{B}\ell_{\text{con}}(k) \;+\; \gamma\,L_{\text{bal}}, \tag{3.19}$$

với $y_k$ ở dạng one-hot, $\mu$ và $\gamma$ là trọng số của hai thành phần. Các thực nghiệm ở Chương 5 dùng $\mu = 0{,}5$, $\gamma = 1{,}0$ và $\tau_1 = \tau_2 = 2$ (Bảng 5.2).

Hai thành phần nhắm vào các biểu hiện khác nhau của thiên lệch học cục bộ ở mục 3.4.1. $L_{\text{bal}}$ tác động lên đầu ra của tầng phân lớp, tức biểu hiện thứ nhất. $\ell_{\text{con}}$ tác động lên không gian đặc trưng: nó kéo đặc trưng cục bộ về gần đặc trưng toàn cục (biểu hiện thứ hai) và giữ khoảng cách giữa pseudo-data với dữ liệu cục bộ (biểu hiện thứ ba).

FedBR còn có một biến thể thay lô cục bộ bằng các ảnh cục bộ được trộn theo Mixup, với trọng số trộn rút từ phân phối $\mathrm{Beta}(0{,}2;\ 0{,}2)$ và nhãn trộn theo cùng tỉ lệ. Biến thể này, gọi là FedBR + Mixup, chỉ đổi số hạng cross-entropy trong (3.19); cách FedBR dùng pseudo-data giữ nguyên.

### 3.5.5. So với FedMix trên cùng một loại dữ liệu

Đặt (3.19) cạnh (3.15) thì thấy hai phương pháp lấy thông tin từ mẫu trung bình ở hai chỗ khác nhau của mô hình.
- **FedMix** dùng cả ảnh trung bình lẫn nhãn mềm. Ảnh đi vào qua tích vô hướng với gradient của hàm mất mát theo đầu vào; nhãn đi vào qua số hạng (II).
- **FedBR** bỏ nhãn. Ảnh trung bình đi vào qua đầu ra của tầng phân lớp, với đích là phân phối đều, và qua không gian đặc trưng, với đích là đặc trưng toàn cục của chính nó.

Theo hai giả thuyết ở mục 3.4.2, nếu thiên lệch của tầng phân lớp nằm ở hướng của ranh giới quyết định, thì phương pháp nào tác động được lên hướng đó mới có cơ hội cải thiện. Mục này không đánh giá phương pháp nào tốt hơn. Chương 4 đặt ba cách dùng vào cùng một khung, và Chương 5 so sánh chúng bằng thực nghiệm.

---

# SỬA — 26/09/2026 · hai câu "Mã nguồn…" còn trong Word mục 3.5.4

> Chỉ-append. Rà trên bản Word lưu lúc 09:42 ngày 26/09. Word đã theo cấu trúc mới của mục 3.5, đã dùng $\gamma$ trong (3.19), nhưng hai câu ở tiểu mục *Mục tiêu cục bộ* vẫn là câu của bản 24/09. "Mã nguồn" trong hai câu đó là mã nguồn mà Guo và cộng sự công bố cùng bài FedBR [2]. Hai câu được viết trước khi có quy tắc không nói về mã nguồn trong thân bài; bản 26/09 phía trên đã sửa, chỉ là Word chưa nhận.

| # | Mục | Tìm trong Word | Trước | Sau |
|---|---|---|---|---|
| 1 | 3.5.4, câu ngay sau (3.19) | `Mã nguồn đặt` | với ⟨y_k⟩ ở dạng one-hot. Mã nguồn đặt ⟨μ = 0.5⟩, ⟨γ = 1.0⟩ và ⟨τ1 = τ2 = 2.0⟩. | với ⟨y_k⟩ ở dạng one-hot, ⟨μ⟩ và ⟨γ⟩ là trọng số của hai thành phần. Các thực nghiệm ở Chương 5 dùng ⟨μ = 0,5⟩, ⟨γ = 1,0⟩ và ⟨τ1 = τ2 = 2⟩ (Bảng 5.2). |
| 2 | 3.5.4, đoạn cuối | `Mã nguồn còn cho phép thay lô cục bộ` | Mã nguồn còn cho phép thay lô cục bộ bằng các ảnh cục bộ được trộn theo Mixup, … | FedBR còn có một biến thể thay lô cục bộ bằng các ảnh cục bộ được trộn theo Mixup, … (phần còn lại giữ nguyên) |
| 3 | 3.5.4, cùng đoạn cuối | `và nhãn trộn theo cùng tỉ lệ` | đoạn bị cắt đôi: *"…rút từ phân phối"* ‖ *"⟨Beta(0,2; 0,2)⟩ và nhãn trộn theo cùng tỉ lệ…"* | nối lại thành một đoạn; công thức Beta để dạng nội dòng |
| 4 | 3.5, sau tiểu mục *Mục tiêu cục bộ* | — | *(chưa có)* | chèn tiểu mục **3.5.5 So với FedMix trên cùng một loại dữ liệu** từ khối 26/09 phía trên |

**Ghi chú:** số trong công thức của Word đang dùng dấu chấm thập phân (0.5, 1.0, 2.0); thân bài tiếng Việt dùng dấu phẩy (0,5). Nên thống nhất một kiểu cho cả luận văn.
