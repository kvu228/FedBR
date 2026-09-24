# CHƯƠNG 4 — ĐỀ XUẤT

> **KHỐI TRẠNG THÁI** · 16/09/2026
>
> | Mục | Trạng thái |
> |---|---|
> | 4.1 – 4.6 | `[BẢN NHÁP ĐẦY ĐỦ]` — chờ tác giả chỉnh lý |
> | Hình 4.1 (sơ đồ khối) | `[CẦN VẼ]` — mô tả bằng lời ở §4.1.2 |
> | §4.6 Mệnh đề 4.1 | ⚠️ **Kết quả lý thuyết mới** — cần tác giả kiểm lại đại số |
>
> Ký hiệu và trích dẫn tiếp nối `03_chuong3.md`. Quyết định thiết kế theo `PLAN_ke-hoach-8-tuan.md`.

---

Chương này trình bày **sản phẩm được đề xuất** của luận văn. Cần nói rõ ngay bản chất của nó: luận văn **không đề xuất một thuật toán học liên kết mới**. Sản phẩm là một **khung thực nghiệm (framework)** cho phép tháo rời và đo riêng từng thành phần của cơ chế tăng cường dữ liệu dựa trên khai triển Taylor, cùng với **giao thức đo lường** đi kèm.

Lựa chọn này khớp trực tiếp với mục tiêu tổng quát đã đăng ký — *nghiên cứu cơ sở lý thuyết về các kỹ thuật làm phong phú không gian đặc trưng và phương pháp xấp xỉ hàm mất mát dựa trên khai triển Taylor* — và với sản phẩm dự kiến đã đăng ký là *một framework hỗ trợ đa dạng các loại tác vụ và các loại hàm mất mát khác nhau*.

---

## 4.1. Tổng quan khung đề xuất

### 4.1.1. Nguyên tắc thiết kế

Khung được thiết kế quanh một nhận xét đã rút ra ở §3.3.5: cơ chế đang xét **không phải một khối đơn nhất** mà là tổ hợp của những thành phần có thể tháo rời độc lập. Cụ thể có bốn trục:

| Trục | Các giá trị | Mục đo |
|---|---|---|
| **Cơ chế tăng cường** | không / A / B / C (§3.3.5) | §4.2 |
| **Ngân sách** | $\lambda$ (trọng số trộn), $M$ (độ nén) | §4.4 |
| **Chế độ lệch phân phối** | vị trí trên trục độ nghiêm trọng | §4.3 |
| **Tác vụ và hàm mất mát** | phân lớp (CE) / hồi quy (MSE) | §4.6 |

Yêu cầu thiết kế then chốt: **bốn trục phải thay đổi được độc lập với nhau**, để mọi so sánh chỉ khác nhau ở đúng một trục. Đây là điều kiện cần để quy kết nhân quả, và cũng là điều mà cài đặt sẵn có không cho phép — vì ở đó cơ chế tăng cường và điểm đánh giá hàm mất mát bị buộc chặt vào nhau (§3.3.5).

### 4.1.2. Kiến trúc

Khung giữ nguyên cấu trúc hai phía của mô hình đã đăng ký trong đề cương, với các điểm mở rộng được đánh dấu.

**Phía client — giai đoạn chuẩn bị (một lần, trước huấn luyện).** Client $i$ chọn ngẫu nhiên $M$ mẫu cục bộ và tính cặp trung bình $(\bar{\mathbf{x}}_g, \bar y_g)$ theo (3.2). Tham số $M$ là **điểm mở rộng thứ nhất**: trong cài đặt gốc nó là hằng số, ở đây nó là tham số cấu hình. Phép lấy trung bình đóng vai trò cơ chế nén — ảnh riêng lẻ không rời thiết bị.

**Phía máy chủ — thu thập và phát tán.** Máy chủ gom các cặp $(\bar{\mathbf{x}}_g, \bar y_g)$ thành tập dùng chung $\mathcal{V}$ và phát ngược cho mọi client, để mỗi client có được một "cái nhìn" khái quát về phân phối toàn hệ thống mà không thấy dữ liệu cụ thể của bất kỳ ai.

**Phía client — vòng lặp huấn luyện.** Ở mỗi bước, client lấy một lô cục bộ và một mẫu từ $\mathcal{V}$, rồi tính hàm mất mát theo **một trong bốn cấu hình** của trục thứ nhất. Đây là **điểm mở rộng thứ hai** và là phần trung tâm: cài đặt sẵn có chỉ hiện thực hai trong bốn cấu hình, và hai cấu hình đó khác nhau ở hai chỗ đồng thời.

**Phía máy chủ — tổng hợp.** Trung bình có trọng số theo FedAvg, không thay đổi.

**Lớp đo lường** bao quanh toàn bộ quy trình, ghi lại ở mỗi vòng đánh giá: độ chính xác trên từng môi trường kiểm tra, thời gian mỗi bước, bộ nhớ đỉnh, và toàn bộ cấu hình siêu tham số. Đây là **điểm mở rộng thứ ba**, phục vụ yêu cầu báo cáo *chi phí tài nguyên* đã đăng ký trong đề cương.

> `[CẦN VẼ — Hình 4.1]` Sơ đồ khối hai cột (Server Orchestrator ↔ Client Local Training) theo bố cục đề cương, với ba điểm mở rộng được tô khác màu.

### 4.1.3. Quan hệ với nền tảng thực nghiệm

Khung được hiện thực trên nền tảng mã nguồn của [18], vốn đã có sẵn cấu hình A và B, cơ sở hạ tầng phân hoạch dữ liệu, và các thuật toán đối chứng. Phần bổ sung gồm: cấu hình C, tham số hoá $M$ và $\alpha_{\text{rot}}$, chế độ lệch phân phối đặc trưng thuần, và lớp đo lường mở rộng. Chương 5 §5.1 liệt kê đầy đủ các thay đổi.

---

## 4.2. Cô lập số hạng khai triển Taylor

### 4.2.1. Đại lượng được đo

Theo lưới ở §3.3.5, đại lượng trung tâm của luận văn là

$$\Delta_{\text{Taylor}} \;=\; \mathrm{Acc}(\mathcal{L}_{\text{B}}) \;-\; \mathrm{Acc}(\mathcal{L}_{\text{C}}), \tag{4.1}$$

trong đó $\mathcal{L}_{\text{B}}$ là (3.6) và $\mathcal{L}_{\text{C}}$ là (3.7). Hai cấu hình này khác nhau **đúng một số hạng**:

$$\mathcal{L}_{\text{B}} - \mathcal{L}_{\text{C}} = \lambda(1{-}\lambda)\,\nabla_{\mathbf{x}}\ell_{y_i}\cdot\bar{\mathbf{x}}_g,$$

và giống nhau ở mọi thứ còn lại: cùng điểm đánh giá $(1{-}\lambda)\mathbf{x}_i$, cùng nhãn mềm $\bar y_g$, cùng tập $\mathcal{V}$, cùng $\lambda$, cùng $M$, cùng phân hoạch dữ liệu, cùng hạt giống khởi tạo. Do đó (4.1) là phép cô lập chặt.

Để đối chiếu, luận văn cũng báo cáo đại lượng mà công trình gốc đo:

$$\Delta_{\text{gốc}} \;=\; \mathrm{Acc}(\mathcal{L}_{\text{B}}) \;-\; \mathrm{Acc}(\mathcal{L}_{\text{A}}), \tag{4.2}$$

với $\mathcal{L}_{\text{A}}$ là (3.3). Như §3.3.5 đã chỉ ra, (4.2) trộn lẫn hai hiệu ứng. **Chênh lệch giữa (4.1) và (4.2) chính là phần mà phép so sánh gốc quy nhầm cho số hạng Taylor** — và đó là một kết quả của luận văn, không phải một bước trung gian.

Đại lượng thứ ba, đo riêng hiệu ứng của điểm đánh giá:

$$\Delta_{\text{đánh giá}} \;=\; \mathrm{Acc}(\mathcal{L}_{\text{A}}) \;-\; \mathrm{Acc}(\mathcal{L}_{\text{C}}). \tag{4.3}$$

Theo cấu trúc lưới, $\Delta_{\text{gốc}} = \Delta_{\text{Taylor}} + \Delta_{\text{đánh giá}}$ nếu hai hiệu ứng cộng tính. Việc đẳng thức này có nghiệm đúng hay không tự nó là một phép kiểm tra tính cộng tính, và luận văn báo cáo phần dư.

### 4.2.2. Ô không được chạy

Lưới đầy đủ ở §3.3.5 có bốn ô; luận văn chạy ba. Ô D — giữ phép trộn ở đầu vào **và** thêm số hạng gradient — cho $\bar{\mathbf{x}}_g$ đi vào hàm mất mát **hai lần**, một lần qua lượt truyền xuôi và một lần qua đạo hàm. Nó không tương ứng với bất kỳ khai triển nhất quán nào của (3.1), nên nó là một **nhánh chẩn đoán** chứ không phải một thuật toán có nguyên tắc.

Hệ quả cần ghi nhận trong phần hạn chế: khi thiếu ô D, số hạng Taylor chỉ được cô lập tại **một** điểm đánh giá. Nếu tác động của số hạng này phụ thuộc vào điểm đánh giá, thiết kế hiện tại không phát hiện được.

### 4.2.3. Ba yếu tố gây nhiễu cần loại trừ

**Thang độ lớn của gradient.** Số hạng (III) có biên độ phụ thuộc vào thang của $\nabla_{\mathbf{x}}\ell$, vốn thay đổi trong quá trình huấn luyện. Luận văn ghi lại biên độ tương đối của (III) so với (I) ở các mốc vòng khác nhau, để phân biệt "số hạng không mang thông tin" với "số hạng có biên độ quá nhỏ ở cấu hình đang xét".

**Tương tác với $\lambda$.** Vì (III) mang hệ số $\lambda(1{-}\lambda)$ trong khi (II) mang hệ số $\lambda$, tỉ lệ giữa chúng phụ thuộc $\lambda$. Do đó $\Delta_{\text{Taylor}}$ **phải** được báo cáo như một hàm của $\lambda$, không phải tại một giá trị duy nhất — nội dung của §4.4.

**Hiệu ứng của $M$.** Độ nén càng cao thì $\bar{\mathbf{x}}_g$ càng mịn và càng ít mang cấu trúc. Vì $\bar{\mathbf{x}}_g$ đi vào cấu hình B qua tích vô hướng với gradient còn đi vào cấu hình A qua lượt truyền xuôi, hai cấu hình có thể phản ứng khác nhau với $M$. Trục này cũng thuộc §4.4.

---

## 4.3. Trục độ nghiêm trọng của lệch phân phối

### 4.3.1. Vì sao không dùng thiết kế giai thừa

Cách trình bày tự nhiên cho hai loại lệch phân phối là một ma trận $2\times2$: {có/không label skew} $\times$ {có/không feature skew}. Luận văn **không** dùng thiết kế này, vì một lý do có thể nêu chính xác.

Hai loại lệch phân phối được điều khiển bởi hai tham số **không cùng đơn vị**: $\alpha$ cho phân phối nhãn và $\alpha_{\text{rot}}$ cho phân phối góc. Không có cơ sở nào để khẳng định $\alpha = 0{,}1$ "nghiêm trọng tương đương" $\alpha_{\text{rot}} = 1{,}0$. Nếu ô feature skew cho $\Delta_{\text{Taylor}}$ lớn hơn ô label skew, chênh lệch đó **không phân biệt được** giữa hai cách giải thích: (i) số hạng Taylor thực sự hữu ích hơn dưới feature skew, hay (ii) mức feature skew được chọn đơn giản là nặng hơn.

Đây là bài toán **hiệu chuẩn độ nghiêm trọng**, và như §2.6.2 đã nêu, văn liệu hiện chưa giải. Luận văn không giải nó, mà dùng một phương án vận hành thay thế.

### 4.3.2. Trục chung: độ suy giảm của FedAvg

Thay vì hiệu chuẩn hai tham số với nhau, luận văn chiếu mọi cấu hình lên **một trục chung trong không gian kết quả**: độ suy giảm độ chính xác của FedAvg so với cấu hình đồng nhất.

$$\mathrm{Drop}(s) \;=\; \mathrm{Acc}_{\text{FedAvg}}(s_0) \;-\; \mathrm{Acc}_{\text{FedAvg}}(s), \tag{4.4}$$

với $s$ là một cấu hình lệch phân phối và $s_0$ là cấu hình IID. Mỗi cấu hình khi đó cho một điểm $\big(\mathrm{Drop}(s),\, \Delta_{\text{Taylor}}(s)\big)$, và cả hai loại lệch phân phối rơi lên cùng một trục hoành.

Phương án này có ba ưu điểm thực tế: nó **miễn phí** (FedAvg đã chạy ở mọi cấu hình làm tham chiếu cho so sánh theo cặp); nó biến câu hỏi từ *"loại skew nào tệ hơn"* — vốn không trả lời được — thành *"mức cải thiện biến thiên thế nào theo độ khó của bài toán"*, vốn trả lời được; và nó nhất quán với nguyên tắc báo cáo mức cải thiện dưới dạng đường đặc tuyến vận hành (§2.5).

**Giới hạn phải nêu thẳng.** $\mathrm{Drop}(s)$ trộn lẫn hai thứ: bài toán khó đến mức nào, và FedAvg hỏng theo cơ chế nào. Hai loại lệch phân phối khác nhau có thể cho cùng một giá trị $\mathrm{Drop}$ thông qua hai cơ chế hoàn toàn khác. Đây là một phép **căn chỉnh vận hành**, không phải căn chỉnh phân phối, và nó không thay thế được bài toán hiệu chuẩn thật sự. Luận văn ghi nhận bài toán gốc ở Chương 6 như một hướng phát triển.

### 4.3.3. Các cấu hình được khảo sát

| Ký hiệu | Cấu hình | Vai trò |
|---|---|---|
| **P0** | IID — phân hoạch đều, không xoay | mốc neo cho (4.4) |
| **P1** | Feature skew, $\alpha_{\text{rot}}$ mặc định | **điểm chính** |
| **P2** | Feature skew, $\alpha_{\text{rot}}$ trung bình | dựng đường cong |
| **P3** | Feature skew, $\alpha_{\text{rot}}$ nhẹ | dựng đường cong |
| **P4** | Label skew, $\alpha = 0{,}1$ (giá trị đã đăng ký) | **điểm chính** |

Ba cấu hình P1–P3 quét về phía **nhẹ dần**, vì như §3.2.3 đã nêu, cấu hình mặc định đã nằm gần cực trị nặng của trục $\alpha_{\text{rot}}$.

### 4.3.4. Yêu cầu về môi trường kiểm tra

So sánh xuyên cấu hình chỉ có nghĩa nếu **mọi cấu hình được đánh giá trên cùng một tập môi trường kiểm tra**. Nếu cấu hình label skew dùng một tập kiểm tra khác với cấu hình feature skew, trục hoành (4.4) không còn đo cùng một đại lượng, và toàn bộ §4.3.2 sụp đổ.

Đây không phải một chi tiết kỹ thuật: cài đặt sẵn có **vi phạm** điều kiện này, và việc sửa nó là một thay đổi bắt buộc được ghi ở §5.1. Luận văn báo cáo tách biệt hai chỉ số: độ chính xác trên môi trường không biến đổi (trong phân phối) và trung bình trên toàn bộ môi trường đã biến đổi (ngoài phân phối).

---

## 4.4. Mặt vận hành $(\lambda, M)$

Mục này hiện thực trực tiếp sản phẩm đã đăng ký trong đề cương: *báo cáo phân tích về sự cân bằng giữa hiệu suất và chi phí tài nguyên*.

### 4.4.1. Hai tham số ngân sách

$\lambda$ điều khiển **mức độ thông tin ngoại lai được đưa vào mục tiêu**. Khi $\lambda \to 0$, mọi cấu hình suy biến về FedAvg. Khi $\lambda$ lớn, xấp xỉ Taylor (3.4) mất hiệu lực vì điểm khai triển không còn gần. Luận văn quét $\lambda \in \{0{,}05;\ 0{,}1;\ 0{,}2\}$ — khoảng bao trùm các giá trị vận hành của cả hai công trình gốc. Giá trị $\lambda = 0{,}5$ được loại vì công trình gốc đã ghi nhận cả hai cấu hình đều sụp đổ ở đó.

$M$ điều khiển **độ nén của mẫu đại diện**, và đồng thời là tham số bảo mật của cơ chế: $M = 1$ tương đương chia sẻ ảnh thô, $M$ lớn cho ảnh gần như không nhận dạng được. Đây chính là *"cơ chế nén đặc trưng"* mà đề cương mô tả.

### 4.4.2. Ba đại lượng báo cáo cùng nhau

Với mỗi cấu hình $(\lambda, M)$, luận văn báo cáo đồng thời:

1. **Độ chính xác** — và mức cải thiện theo cặp so với FedAvg;
2. **Chi phí truyền thông** — số byte của tập $\mathcal{V}$, tính theo $|\mathcal{V}| \times \dim(\mathbf{x})$, phát sinh **một lần** trước huấn luyện, đặt cạnh chi phí truyền mô hình mỗi vòng để thấy tỉ lệ;
3. **Độ nén** — giá trị $M$, tức số ảnh gộp vào mỗi mẫu được chia sẻ.

Ba đại lượng này tạo thành mặt đánh đổi mà đề cương yêu cầu. Cần nêu rõ một giới hạn: $M$ là một **đại lượng đại diện** cho mức bảo mật, không phải một bảo đảm hình thức. Luận văn **không đưa ra tuyên bố riêng tư vi phân**; giao thức chỉ có tính chất không phụ thuộc phân phối lớp ở mức hệ thống, và một phân tích $(\varepsilon, \delta)$ hình thức nằm ngoài phạm vi.

### 4.4.3. Hai giá trị của $\lambda$, và khoảng cách giữa chúng

Đây là điểm thiết kế quan trọng nhất của mục này.

Công trình gốc tinh chỉnh $\lambda$ **riêng cho từng thuật toán**, rồi báo cáo chênh lệch giữa hai thuật toán như thể đó là hiệu ứng của cơ chế. Nhưng khi hai thuật toán chạy ở hai giá trị $\lambda$ khác nhau, chênh lệch quan sát được trộn lẫn hiệu ứng của cơ chế với hiệu ứng của việc tinh chỉnh. Chính công trình đó cung cấp bằng chứng cho vấn đề này: khi $\lambda$ của cấu hình A được quét, giá trị tốt nhất của nó tiến rất sát cấu hình B — khoảng cách thu hẹp đáng kể so với con số ở bảng chính.

Luận văn vì vậy báo cáo **hai con số** cho mỗi phép so sánh:

- $\Delta$ tại **$\lambda$ khớp** — mọi cấu hình dùng cùng một $\lambda$. Đây là phép cô lập sạch, và là con số trả lời câu hỏi nghiên cứu thứ nhất.
- $\Delta$ tại **$\lambda$ tối ưu riêng từng cấu hình** — mỗi cấu hình dùng giá trị tốt nhất của nó theo phép quét. Đây là phép so sánh công bằng giữa các phương pháp.

**Khoảng cách giữa hai con số là một kết quả của luận văn**, không phải một chi tiết phương pháp: nó định lượng phần mức cải thiện được báo cáo trong văn liệu mà thực chất đến từ ngân sách tinh chỉnh không đồng đều. Phép quét cần thiết cho con số thứ hai cũng đồng thời cung cấp đường cong cho §4.4.2, nên chi phí phụ trội bằng không.

---

## 4.5. Giao thức đo lường

### 4.5.1. So sánh theo cặp

Mọi mức cải thiện được báo cáo dưới dạng **chênh lệch theo cặp**: hai cấu hình được so sánh phải dùng **cùng một lần rút phân hoạch dữ liệu**, cùng hạt giống khởi tạo, cùng lịch học, và cùng số vòng. Cách này loại bỏ phương sai do phân hoạch — vốn là nguồn phương sai trội trong FL mô phỏng — và cho phép đo hiệu ứng nhỏ hơn nhiều so với so sánh không ghép cặp.

### 4.5.2. Kỷ luật trong cùng nền tảng

Luận văn sử dụng hai nền tảng thực nghiệm: nền tảng của công trình [44] cho các kết quả nền ở Chương 3, và nền tảng của [18] cho toàn bộ thực nghiệm mới ở Chương 5. Theo nguyên tắc ở §2.5, **không so sánh trực tiếp con số tuyệt đối giữa hai nền tảng**. Mọi phát biểu xuyên chương được đặt ở mức **cơ chế** — chẳng hạn "hiện tượng X quan sát được ở cả hai nền tảng" — chứ không ở mức "giá trị tăng từ $a$ lên $b$".

### 4.5.3. Ước lượng thay vì kiểm định

Câu hỏi nghiên cứu thứ nhất được đặt ở dạng **ước lượng**: $\Delta_{\text{Taylor}}$ **lớn bao nhiêu**, với khoảng tin cậy nào — chứ không phải nó có khác không một cách có ý nghĩa thống kê hay không.

Lý do là thực tế. Công trình gốc cho thấy khi $\lambda$ được quét, khoảng cách giữa hai cấu hình có thể chỉ ở mức dưới một điểm phần trăm. Với độ lệch chuẩn của chênh lệch theo cặp quan sát được trong [44] vào khoảng $1{,}2$ điểm phần trăm, nửa rộng khoảng tin cậy $95\%$ theo số hạt giống là:

| $n$ | 5 | **8** | 12 | 25 |
|---|---|---|---|---|
| Nửa rộng CI | $1{,}49$ | $\mathbf{1{,}00}$ | $0{,}76$ | $0{,}50$ |

Không có số hạt giống khả thi nào phân giải được một hiệu ứng cỡ $0{,}6$ điểm phần trăm. Thiết kế vì vậy được xây **cho** kết cục đó thay vì hy vọng tránh nó: luận văn đặt $n = 8$, cho nửa rộng khoảng tin cậy khoảng $1{,}0$ điểm phần trăm, và phát biểu kết quả dưới dạng *"$\Delta_{\text{Taylor}}$ nằm trong khoảng $[a, b]$, tức bị chặn dưới mức $c$ được báo cáo ở cấu hình tinh chỉnh không đồng đều"*.

Phát biểu này có giá trị **bất kể giá trị đo được là bao nhiêu** — đó là tính chất mà một thiết kế dưới sức ép thời gian cần có.

Độ lệch chuẩn $1{,}2$ nêu trên lấy từ một nền tảng khác và chỉ dùng để **định cỡ thiết kế**; giá trị thực trên nền tảng của Chương 5 được ước lượng từ chính $n = 8$ hạt giống và báo cáo tường minh.

### 4.5.4. Họ giả thuyết chính và nhánh không có hiệu ứng

Để kiểm soát so sánh bội, luận văn khai báo trước một **họ giả thuyết chính** gồm bốn phép so sánh, thực hiện ở hai cấu hình chính P1 và P4:

| | Giả thuyết |
|---|---|
| H1 | $\Delta_{\text{Taylor}} \ne 0$ tại P1 (feature skew) |
| H2 | $\Delta_{\text{Taylor}} \ne 0$ tại P4 (label skew) |
| H3 | $\mathrm{Acc}(\mathcal{L}_{\text{B}}) \ne \mathrm{Acc}_{\text{FedAvg}}$ tại P1 |
| H4 | $\mathrm{Acc}(\mathcal{L}_{\text{B}}) \ne \mathrm{Acc}_{\text{FedAvg}}$ tại P4 |

Họ này được hiệu chỉnh theo thủ tục Holm. **Mọi phép so sánh khác** — các cấu hình P0, P2, P3, toàn bộ phép quét $\lambda$ và $M$, và các kiểm soát ngoại vi — được gắn nhãn **thăm dò** một cách tường minh và không tham gia hiệu chỉnh.

Nếu $\Delta_{\text{Taylor}}$ không khác không một cách có ý nghĩa, đó **không** đủ để kết luận số hạng Taylor vô ích: một phép kiểm định không có ý nghĩa thống kê không chứng minh giả thuyết không. Luận văn vì vậy khai báo trước một **biên tương đương** $\pm 1{,}5$ điểm phần trăm và sử dụng thủ tục hai phép kiểm định một phía (TOST). Nếu thiết kế không đạt được biên đó, điều này được nêu thẳng trong phần kết quả thay vì bỏ qua.

### 4.5.5. Các đại lượng được ghi nhận

Ngoài độ chính xác, mỗi lần chạy ghi lại: thời gian mỗi bước và bộ nhớ đỉnh (phục vụ yêu cầu chi phí tài nguyên của đề cương); độ chính xác theo từng lớp và ma trận nhầm lẫn; chuẩn $\ell_2$ của từng vector trọng số lớp ở tầng cuối (phục vụ phân tích cơ chế ở §5.7); và toàn bộ cấu hình siêu tham số.

Phân tích cơ chế được thực hiện trên **mô hình ở vòng cuối** thay vì mô hình ở vòng có độ chính xác cao nhất. Lựa chọn này làm phân tích nhiễu hơn — độ chính xác dao động giữa các vòng trong FL không đồng nhất — nhưng không gây thiên lệch, vì mọi cấu hình được so sánh tại **cùng một vòng**. Các bảng độ chính xác không bị ảnh hưởng, vì chúng được tính từ nhật ký theo vòng chứ không từ tệp mô hình.

---

## 4.6. Mở rộng sang tác vụ hồi quy

Mục tiêu cụ thể đã đăng ký yêu cầu cơ chế hỗ trợ **cả tác vụ phân loại và hồi quy**. Mục này xử lý yêu cầu đó ở mức lý thuyết, và nêu rõ phần thực nghiệm nằm ngoài phạm vi luận văn.

### 4.6.1. Vì sao hồi quy là phép kiểm tra đúng chỗ

Lời giải thích cơ học cho các kết quả âm trong văn liệu — bao gồm kết quả nền ở §3.6 — định vị thiên lệch vào **bộ phân lớp** dưới **lệch phân phối nhãn** (§3.4). Nhưng bài toán hồi quy **không có bộ phân lớp** theo nghĩa phạm trù, và cũng không có label skew theo nghĩa phân phối trên tập nhãn rời rạc.

Nói cách khác, ở tác vụ hồi quy, **cơ chế được dùng để giải thích các kết quả âm không áp dụng được**. Điều này khiến hồi quy trở thành một phép kiểm tra tính tổng quát của chính lời giải thích, chứ không phải một ứng dụng phụ. Nếu cơ chế tăng cường trung bình cũng thất bại ở hồi quy, lời giải thích "thiên lệch nằm ở bộ phân lớp" là chưa đủ và cần một cơ chế rộng hơn.

Đây là lập luận ngược chiều với cách loại bỏ nhánh hồi quy bằng lý do "kế thừa cùng một cơ chế", và luận văn ghi nhận nó tường minh.

### 4.6.2. Khai triển Taylor có chuyển sang hồi quy không

Dẫn xuất ở §3.3 dựa vào một tính chất cụ thể của cross-entropy: **tuyến tính theo nhãn**, cho phép tách (3.1). Hàm mất mát bình phương không có tính chất đó — nó bậc hai theo nhãn. Câu hỏi là phép tách có còn hiệu lực hay không.

> **Mệnh đề 4.1.** Với hàm mất mát bình phương $\ell(f(\mathbf{x}), y) = \lVert f(\mathbf{x}) - y \rVert^2$ và nhãn trộn $\tilde y = (1{-}\lambda)y_i + \lambda\bar y_g$, ta có
> $$\ell\big(f(\tilde{\mathbf{x}}), \tilde y\big) \;=\; (1{-}\lambda)\,\ell\big(f(\tilde{\mathbf{x}}), y_i\big) + \lambda\,\ell\big(f(\tilde{\mathbf{x}}), \bar y_g\big) \;-\; \lambda(1{-}\lambda)\lVert y_i - \bar y_g \rVert^2 .$$
> Số hạng cuối **không phụ thuộc tham số mô hình**.

*Chứng minh.* Đặt $a = 1{-}\lambda$, $b = \lambda$, $a + b = 1$, và $f = f(\tilde{\mathbf{x}})$. Khi đó

$$a\lVert f - y_i\rVert^2 + b\lVert f - \bar y_g\rVert^2 = \lVert f\rVert^2 - 2 f^\top\!\big(a y_i + b\bar y_g\big) + a\lVert y_i\rVert^2 + b\lVert \bar y_g\rVert^2,$$

trong khi

$$\lVert f - \tilde y\rVert^2 = \lVert f\rVert^2 - 2 f^\top \tilde y + \lVert \tilde y\rVert^2, \qquad \tilde y = a y_i + b \bar y_g .$$

Hai vế trùng nhau ở hai số hạng đầu. Phần chênh lệch là

$$a\lVert y_i\rVert^2 + b\lVert \bar y_g\rVert^2 - \lVert \tilde y\rVert^2 = a(1{-}a)\lVert y_i\rVert^2 + b(1{-}b)\lVert \bar y_g\rVert^2 - 2ab\, y_i^\top \bar y_g,$$

và vì $1{-}a = b$, $1{-}b = a$, biểu thức này bằng $ab\big(\lVert y_i\rVert^2 - 2 y_i^\top\bar y_g + \lVert\bar y_g\rVert^2\big) = ab\lVert y_i - \bar y_g\rVert^2$. $\square$

**Hệ quả.** Phép tách theo nhãn mà cross-entropy thoả mãn **chính xác**, hàm mất mát bình phương thoả mãn **sai khác một hằng số độc lập tham số**. Vì hằng số đó có gradient bằng không, toàn bộ dẫn xuất từ (3.1) đến (3.6) — bao gồm khai triển Taylor bậc nhất và hệ số $\lambda(1{-}\lambda)$ — **chuyển nguyên vẹn sang tác vụ hồi quy với hàm mất mát bình phương**, và bốn cấu hình ở §3.3.5 được định nghĩa y hệt.

Hằng số $\lambda(1{-}\lambda)\lVert y_i - \bar y_g\rVert^2$ tuy không ảnh hưởng tối ưu hoá nhưng có ý nghĩa diễn giải: nó lớn khi đích cục bộ xa đích trung bình toàn cục, tức nó đo chính mức độ không đồng nhất của đích giữa các client.

### 4.6.3. Phạm vi

Mệnh đề 4.1 cho thấy khung đề xuất **mở rộng được sang hồi quy mà không cần thay đổi cấu trúc** — chỉ thay hàm mất mát và thay chỉ số đánh giá từ độ chính xác sang sai số tuyệt đối hoặc bình phương trung bình. Yêu cầu *hỗ trợ đa dạng tác vụ và hàm mất mát* của đề cương được đáp ứng ở mức thiết kế.

Phần **thực nghiệm** cho nhánh hồi quy không nằm trong phạm vi luận văn. Lý do là ràng buộc nguồn lực: nó đòi hỏi một bộ dữ liệu chuẩn mới, một bộ chỉ số đánh giá mới, và một tập baseline mới, trong khi đóng góp chính của luận văn nằm ở việc đo chính xác một đại lượng trong tác vụ phân loại. Chương 6 nêu đây là hướng phát triển gần nhất, với Mệnh đề 4.1 làm nền.

---

# YÊU CẦU SỬA — 24/09/2026 · lượt rà soát nội dung Chương 4

> **Cách đọc.** Khối này mô tả việc cần làm. Bản 16/09 phía trên giữ nguyên trạng theo quy ước chỉ-append (`00_outline.md` §8); bản đã thi hành nằm dưới mốc `# PHIÊN BẢN CHỈNH SỬA — 24/09/2026`.
>
> **Căn cứ rà soát:** bản Word `VuTuanKiet_KLTN_Thsi_2026.docx` (đường dẫn ở `00_outline.md` §0). Trong Word, Chương 4 mới có năm tiêu đề mục 4.1–4.5, chưa có thân bài; Ch.1–Ch.3 đã có thân bài. Kèm theo: `00_outline.md`, `PLAN_ke-hoach-8-tuan.md`, các file chương, `NOTE_khao-sat-van-lieu.md`, và mã nguồn `fedbr/`.
>
> **Điểm xuất phát:** Chương 4 mang dấu 16/09, viết trước mọi quyết định 21–23/09. Phần lớn lỗi mục A là hệ quả cơ học của việc đó. Riêng A2, A3, A4 là lỗi thật của thiết kế, và A3 ảnh hưởng tới cả Ch.3 lẫn Ch.5.

## A. Chặn — phải sửa trước khi chép vào Word

**A1. Nhánh hồi quy còn nguyên.** Mục 4.1.1 còn bốn trục, trục thứ tư là tác vụ và hàm mất mát; toàn bộ mục 4.6 cùng Mệnh đề 4.1; câu mở chương trích *"hỗ trợ đa dạng các loại tác vụ và các loại hàm mất mát"*. Trái ràng buộc `[GÁC]` 22/09. Bản hiện hành bỏ hết; Mệnh đề 4.1 giữ tại chỗ ở bản 16/09 để mở lại khi cần (đại số đã kiểm, đúng).

**A2. Đẳng thức cộng tính ở 4.2.1 sai dấu, và phép kiểm tra đi kèm không tồn tại.** Với $\Delta_{\text{Taylor}} = B - C$, $\Delta_{\text{đánh giá}} = A - C$, ta có $\Delta_{\text{gốc}} = B - A = \Delta_{\text{Taylor}} - \Delta_{\text{đánh giá}}$, dấu trừ. Hơn nữa đây là **đồng nhất thức** trên cùng các lần chạy, nên không có "phần dư" nào để báo cáo và không có tính cộng tính nào để kiểm tra. Muốn đo tương tác giữa hai trục thì phải có ô D. Kéo theo: Ch.5 mục 5.3 dòng *"kiểm tra tính cộng tính và báo cáo phần dư"* phải bỏ.

**A3. Mã FedBR tính số hạng (III) nhỏ hơn công thức đúng một hệ số bằng kích thước lô.** `fedbr/algorithms.py:847–850`: `loss1` là $(1{-}\lambda)$ nhân **trung bình** cross-entropy trên lô, nên `grad` theo từng ảnh đã mang $(1{-}\lambda)/B$; `loss3` cộng trên lô rồi **chia thêm cho $B$**. Hệ số hiệu dụng là $\lambda(1{-}\lambda)/B$. Đã kiểm bằng số (`scratchpad/check_loss3.py`, mạng tuyến tính nhỏ, chạy nguyên đoạn mã): tỉ lệ giữa trung bình lô của (III) tính trực tiếp và `loss3` của mã là **8,000** ở $B = 8$ và **32,000** ở $B = 32$. Với lô 32 của cấu hình thực nghiệm, cấu hình B chạy bằng mã phát hành gần như trùng C, nên $\Delta_{\text{Taylor}} \approx 0$ sẽ là hệ quả của phép chuẩn hoá chứ không phải của cơ chế. Kéo theo:
- Ch.4 phải định nghĩa B đúng theo (3.15) và ghi thay đổi mã.
- **Word Ch.3 mục 3.3.4, đoạn "Ánh xạ sang cài đặt"**, khẳng định mã và lý thuyết khớp nhau. Điều đó chỉ đúng với thừa số $\lambda(1{-}\lambda)$; phải thêm một câu về phép chuẩn hoá theo lô.
- Ch.5 mục 5.2.2 *"Một xác nhận âm tính"* phải viết lại, và danh mục kiểm toán thêm một sai lệch.

**A4. Trục chung Drop dùng một mốc IID không xoay cho mọi cấu hình.** P1–P3 huấn luyện trên ảnh xoay, P0 thì không. $\mathrm{Drop}(P1)$ vì vậy gộp cả phần chênh do tập huấn luyện có hay không có ảnh xoay; trên chỉ số trung bình mười góc nó có thể âm. Sửa: mỗi họ lệch một mốc IID có **cùng phân phối gộp**. Họ lệch nhãn giữ P0; họ lệch đặc trưng dùng mốc mới P0r ($\alpha_{\text{rot}} \to \infty$, mỗi ảnh xoay một góc rút đều), là phân phối gộp theo kỳ vọng của họ đó. Chỉ số chính cũng theo họ: 0° cho lệch nhãn, trung bình mười góc cho lệch đặc trưng. Chi phí thêm: FedAvg × 3 hạt giống ở P0r.

**A5. Tham chiếu, số phương trình, số trích dẫn.**
- Khoảng 20 tham chiếu `§` trong thân bài, trái quy tắc 21/09. Nhiều chỗ trỏ tới mục không còn tồn tại: §2.5, §2.6.2, §3.3.5 (Word Ch.3 không có 3.3.5).
- Số phương trình theo đánh số md cũ (3.1)–(3.7). Word Ch.3 đánh (3.1)–(3.15): $\mathcal{L}_{\text{GM}}$ là (3.10), mẫu trung bình (3.11), NaiveMix (3.12), khai triển Taylor (3.13), bốn số hạng (3.14), FedMix (3.15), $n_{\text{eff}}$ (3.7). ⚠️ Word Ch.3 hiện có **hai phương trình cùng mang số (3.2)** (mục tiêu toàn cục ở 3.1.1 và đơn hình xác suất ở 3.2.2). Nếu sửa chỗ trùng này thì mọi số từ đơn hình trở đi dịch lên một, và Ch.4 phải rà lại.
- Trích dẫn: [18] → **[11]** FedBR; [13] → **[1]** FedMix; [44] → công trình của tác giả, **chưa có số trong danh mục Word** (Word [17] hiện là Ng–Jordan). Bản hiện hành tạm ghi `[TG]`.

**A6. Word Ch.3 thiếu mục 3.3.5, 3.3.6 và 3.6 của bản 23/09.** Ch.4 bản 16/09 dựa hẳn vào 3.3.5 (lưới A/B/C/D và phương trình của C). Quyết định tạm của lượt này: **đưa lưới bốn cấu hình và phương trình của C vào Ch.4 mục 4.2** (Bảng 4.2, phương trình (4.1)), vì cấu hình C là phần luận văn đề xuất và Word Ch.3 hiện không có chỗ nào định nghĩa nó. `[QUYẾT]` Nếu học viên chép 3.3.5 vào Word thì thay Bảng 4.2 và (4.1) bằng tham chiếu. Nếu giữ phương án này thì sửa câu ở Word Ch.1 mục 1.4 *"dẫn xuất đầy đủ của khai triển Taylor bậc nhất và **bốn cấu hình sinh ra từ nó**"*.

## B. Nội dung — phải sửa trước khi chốt chương

**B1. Tập V không cố định trong mã.** Bản 16/09 mô tả V dựng một lần trước huấn luyện. Mã (`train_fed.py:439–442`) dựng lại **một lô mẫu trung bình mới ở mỗi bước cục bộ**, trực tiếp từ dữ liệu thô của mọi client, dùng chung cho mọi client trong bước đó. Chạy được trong mô phỏng, nhưng không có đối ứng triển khai, và không có tập V hữu hạn nào để tính chi phí truyền thông. Sửa: khung dùng tập V cố định với hai tham số $M$ và $n_V$ (số cặp mỗi client), ghi thay đổi mã.

**B2. Tiêu đề mục 4.3 trong Word ngược với nội dung.** Word ghi *"Ma trận chế độ lệch phân phối"*, trong khi mục này tồn tại để bác thiết kế ma trận $2\times2$. Đổi tiêu đề trong Word thành *"Chế độ lệch phân phối và trục độ nghiêm trọng"*.

**B3. P2, P3 chưa có giá trị; PLAN §3.2 ghi P2 = $\alpha_{\text{rot}}$ 1,0.** Theo quy ước nồng độ tổng của mã và của Ch.3, $\alpha_{\text{rot}} = 1{,}0$ **chính là** P1. Đề xuất P2 = 10, P3 = 100. Mô phỏng $2\times10^5$ lần rút cho $\mathbb{E}[n_{\text{eff}}]$ = 2,09 / 3,45 / 5,77 / 9,19 ở $\alpha_{\text{rot}}$ = 1 / 3 / 10 / 100, nên 10 và 100 trải gần đều khoảng từ P1 tới mốc P0r ($n_{\text{eff}} = 10$).

**B4. $\lambda$ khớp chưa được chọn trước.** Chọn sau khi xem kết quả quét thì giá trị được chọn thiên về cấu hình đang xem. Đề xuất chốt $\lambda = 0{,}1$ (mặc định của mã FedBR) trước mọi lần chạy.

**B5. Chương hứa mặt $(\lambda, M)$ nhưng không đâu đăng ký phép quét $M$.** Ch.5 E1–E6 và ngân sách PLAN §6 chỉ có quét $\lambda$. Mà mục tiêu cụ thể thứ ba ở Word Ch.1 cần trục $M$. Đề xuất: $M \in \{1; 10; 50\}$, cấu hình A/B/C, P1 và P4, 3 hạt giống; thêm 36 lần chạy (~65 GPU-giờ).

**B6. Chi phí truyền thông không phải một trục đánh đổi.** Với $n_V$ cố định, số byte của V không đổi theo $\lambda$ hay $M$. Bản 16/09 trình bày "độ chính xác × chi phí truyền thông × độ nén" như ba chiều cùng biến thiên. Bản mới nói thẳng: hai lát cắt cho đánh đổi giữa độ chính xác và mức nén **ở chi phí truyền thông cố định**, kèm công thức chi phí.

**B7. Mục 4.5.3 bản cũ.** (a) *"Không có số hạt giống khả thi nào phân giải được 0,6 pp"* nay đã định lượng: mô phỏng cho công suất 0,755 ở $n=30$, 0,821 ở $n=35$, tức cần **khoảng 34 hạt giống** cho công suất 80%. (b) Con số 0,6 pp là $B - A$ ($\Delta_{\text{gốc}}$) trong FedMix Bảng 17, không phải $\Delta_{\text{Taylor}}$; phải nói rõ. (c) $s \approx 1{,}2$ chưa nêu nguồn cụ thể; các độ lệch chuẩn trong công trình của tác giả nằm trong 0,79–1,37. (d) Câu *"đó là tính chất mà một thiết kế dưới sức ép thời gian cần có"* phải bỏ.

**B8. Chỉ số độ chính xác chưa được khai báo ở Ch.4.** Ch.5 dùng trung bình năm vòng cao nhất theo quy ước FedBR (`summarize.py --top_k 5`). Đây là thống kê chọn trên tập kiểm tra. Bổ sung chỉ số kiểm chứng: trung bình năm mốc đánh giá cuối.

**B9. Phép co $(1{-}\lambda)x_i$ ở B và C gây nhiễu cho H3/H4.** B và C huấn luyện trên ảnh đã co nhưng được đánh giá trên ảnh gốc. Yếu tố này triệt tiêu trong $\Delta_{\text{Taylor}}$ nhưng có mặt trong B so với FedAvg. Nêu ở mục gây nhiễu.

**B10. Viện dẫn đề cương như nguồn quyền uy, năm chỗ**, trái `00_outline.md` §7.5: câu mở chương, 4.1.2 (hai chỗ), 4.4, 4.4.1. Riêng câu miễn trừ riêng tư ở 4.4.2 lặp lại Word Ch.1 mục 1.2.3; cắt.

## C. Đã kiểm và **đúng** — giữ

- **C1.** Bảng nửa rộng khoảng tin cậy khớp phân phối t: 1,49 / 1,00 / 0,76 / 0,50 ở $n$ = 5 / 8 / 12 / 25 với $s = 1{,}2$.
- **C2.** $\mathcal{L}_{\text{B}} - \mathcal{L}_{\text{C}}$ đúng bằng số hạng (III). Thêm một nhận xét mà bản cũ bỏ sót: **trong $\mathcal{L}_{\text{C}}$, $\bar x_g$ không xuất hiện ở đâu cả**; C chỉ dùng nhãn mềm. C vì vậy là mốc chung không dùng thông tin ảnh, còn A và B là hai kênh đưa cùng thông tin ảnh vào. Bản mới dựng mục 4.2 quanh nhận xét này.
- **C3.** Cài đặt `NaiveMix` (`algorithms.py:809–830`) khớp (3.12).
- **C4.** Số liệu FedMix dùng trong chương khớp `NOTE_khao-sat-van-lieu.md`: Bảng 1 CIFAR-10, NaiveMix 77,4, FedMix 81,2; Bảng 17 NaiveMix 79,5 / 79,9 / 80,6 / 29,8 tại $\lambda$ = 0,05 / 0,1 / 0,2 / 0,5.
- **C5.** Mệnh đề 4.1 (hồi quy) đúng về đại số. Giữ ở bản 16/09 cho khi mở lại.

## D. Lối viết (đo trên thân bản 16/09)

AI#1 khuôn tương phản dày; khoảng một nửa số đoạn kết bằng câu chốt dạng *"… là một kết quả của luận văn, không phải một bước trung gian"*; dấu `—` chêm dày; ít nhất bốn câu rào (*"Giới hạn phải nêu thẳng"*, *"Cần nêu rõ một giới hạn"*, *"Hệ quả cần ghi nhận trong phần hạn chế"*, *"Nếu thiết kế không đạt được biên đó, điều này được nêu thẳng"*). Bản mới chỉ giữ một câu rào, cho giới hạn của trục Drop, vì giới hạn đó quyết định cách đọc mọi đồ thị ở Ch.5.

---

# PHIÊN BẢN CHỈNH SỬA — 24/09/2026

> **CÁCH ĐỌC.** Mọi phần phía trên giữ nguyên trạng để tra lịch sử. Phần dưới đây là **bản hiện hành** của Chương 4. Khi chép vào Word, chỉ lấy **thân chương**, tức từ đoạn mở đầu ngay dưới mốc này tới hết mục 4.5.6. Không lấy khối này và khối *Ghi chú thi hành* ở cuối.
>
> **Việc đã làm:** A1–A6 · B1–B10 · D.
>
> **Tự kiểm §7.7** (chạy trên thân chương):
>
> | Phép đếm | Kết quả | Hạn mức | |
> |---|---|---|---|
> | Ký hiệu `§` trong thân bài | **0** | phải bằng 0 | ✅ |
> | AI#1 — máy đếm `chứ không\|không phải .*mà \|thay vì` | **0** | ≤ 3 | ✅ |
> | AI#1 — khuôn tương phản mang chức năng tu từ, đếm tay | **3** (4.3.1 "Luận văn không giải bài toán quy đổi đó"; 4.5.2 "…và không bao giờ ở dạng…"; 4.5.4 "…là một hiệu $\Delta_{\text{gốc}}$, không phải $\Delta_{\text{Taylor}}$") | ≤ 3 | ✅ vừa đủ, không thêm |
> | AI#4 — câu rào | **1** (mục 4.3.2, giới hạn của trục Drop) | đúng 1 | ✅ |
> | AI#6 — dấu `—` chêm | **1**, nằm trong nhãn giữ chỗ `[CẦN VẼ — Hình 4.1]`, không chép vào Word | ≤ 1 mỗi trang | ✅ |
> | AI#8 — cụm sáo cấm dùng | **0** | phải bằng 0 | ✅ |
> | Viện dẫn đề cương | **0** | phải bằng 0 | ✅ |
> | Nhắc tới hồi quy | **0** | phải bằng 0 | ✅ |
>
> **Thuật ngữ tự đặt dùng trong chương, đều định nghĩa tại lần xuất hiện đầu trong chương:** *khung thực nghiệm* (mở chương), *trục độ nghiêm trọng* và *căn chỉnh vận hành* (4.3), *đường đặc tuyến* (4.3.2), *mặt vận hành* (4.4). Không thêm thuật ngữ mới nào ngoài năm cụm đã có ở Ch.1–Ch.3.
>
> **Số phương trình Chương 3 theo bản Word hiện tại:** (3.7) $n_{\text{eff}}$, (3.10) global Mixup, (3.11) mẫu trung bình, (3.12) NaiveMix, (3.13) khai triển Taylor, (3.14) bốn số hạng (I)–(IV), (3.15) FedMix. Xem cảnh báo về hai số (3.2) trùng nhau ở mục A5.
>
> **Phương trình và bảng mới của chương:** (4.1) $\mathcal{L}_{\text{C}}$ · (4.2) $\Delta_{\text{Taylor}}$ · (4.3) $\Delta_{\text{trộn}}$ · (4.4) đồng nhất thức · (4.5) Drop · (4.6) chi phí truyền thông · Bảng 4.1–4.5 · Hình 4.1 `[CẦN VẼ]`.
>
> **Độ dài:** thân chương ≈6.700 từ theo `wc -w` (tính cả ký hiệu công thức), tức khoảng 7,5–8 trang ở format đã chốt nếu lấy Ch.2 (≈8.256 từ cho 9–10 trang) làm thước, so với 10–11 trang giao ở `00_outline.md` §4. Không viết phồng: phần hồi quy (≈1,5 trang trong dàn bài) đã gác, và chương còn chỗ cho nội dung thật ở hai chỗ, là Hình 4.1 và một hình minh hoạ mặt vận hành nếu học viên muốn.
>
> ⚠️ **Còn treo `[QUYẾT]`** — liệt kê ở mục 1 của *Ghi chú thi hành*.

Chương này trình bày khung thực nghiệm (framework) mà luận văn đề xuất để đo cơ chế tăng cường dữ liệu bằng mẫu trung bình đại diện kết hợp khai triển Taylor bậc nhất. Khung không chứa thuật toán học liên kết mới nào. Việc của nó là tháo cơ chế thành những thành phần thay đổi được riêng rẽ, định nghĩa hình thức đại lượng được đo trên từng thành phần, và quy định cách đo sao cho các đại lượng ấy đặt cạnh nhau được.

Mục 4.1 mô tả kiến trúc của khung và quan hệ của nó với mã nguồn FedBR [11]. Phép cô lập số hạng Taylor, phần trung tâm của luận văn, được định nghĩa ở mục 4.2. Hai mục tiếp theo dựng hai trục còn lại: chế độ lệch phân phối ở mục 4.3, lượng thông tin phụ trợ được phép chia sẻ ở mục 4.4. Mục 4.5 là giao thức đo lường, áp chung cho mọi phép so sánh ở Chương 5.

## 4.1. Tổng quan framework

### 4.1.1. Ba trục thay đổi độc lập

Chương 3 dẫn xuất NaiveMix (3.12) và FedMix (3.15) từ cùng một mục tiêu global Mixup (3.10). Đặt hai công thức cạnh nhau thì thấy chúng khác nhau ở hai chỗ: điểm đánh giá hàm mất mát, và sự có mặt của số hạng gradient (III) trong (3.14). Muốn biết chỗ nào tạo ra chênh lệch hiệu năng, phải đổi được từng chỗ một. Lập luận ấy áp dụng y như vậy cho hai yếu tố khác mà kết quả phụ thuộc vào, là lượng thông tin phụ trợ và dạng dữ liệu không đồng nhất. Khung tổ chức cả ba thành ba trục, tóm tắt ở Bảng 4.1.

**Bảng 4.1.** Ba trục của khung thực nghiệm. A, B, C là ba cấu hình hàm mất mát định nghĩa ở mục 4.2: A là NaiveMix, B là FedMix, C là FedMix bỏ số hạng gradient. $\lambda$ là trọng số trộn; $M$ là số ảnh cục bộ gộp vào một mẫu trung bình đại diện; $\alpha_{\text{rot}}$ là nồng độ Dirichlet của phân phối góc xoay; $\alpha$ là nồng độ Dirichlet của phân phối nhãn. $\Delta_{\text{Taylor}}$, $\Delta_{\text{trộn}}$ và $\mathrm{Drop}$ là các đại lượng định nghĩa ở (4.2), (4.3) và (4.5).

| Trục | Các mức | Đại lượng đo |
|---|---|---|
| Cách mẫu trung bình đi vào mục tiêu huấn luyện | không dùng (FedAvg); A; B; C | $\Delta_{\text{Taylor}}$, $\Delta_{\text{trộn}}$ |
| Lượng thông tin phụ trợ | $\lambda \in \{0{,}05;\ 0{,}1;\ 0{,}2\}$; $M \in \{1;\ 10;\ 50\}$ | các đại lượng trên, theo $\lambda$ và theo $M$ |
| Chế độ không đồng nhất | lệch đặc trưng ở ba mức $\alpha_{\text{rot}}$; lệch nhãn với $\alpha = 0{,}1$; hai mốc IID | $\mathrm{Drop}$ |

Yêu cầu thiết kế chỉ có một, nhưng khắt khe: ba trục phải đổi được độc lập, để hai lần chạy bất kỳ được đem so chỉ khác nhau ở đúng một trục. Mã FedBR phát hành chưa đáp ứng yêu cầu này ở trục nào. Trục thứ nhất chỉ có A và B, hai cấu hình khác nhau ở hai chỗ cùng lúc. Ở trục thứ hai, $M$ là hằng số viết cứng bằng 10. Trục thứ ba cũng vậy: $\alpha_{\text{rot}}$ là hằng số, và không có chế độ nào lệch đặc trưng mà vẫn giữ phân phối nhãn đều.

Bốn mục tiêu cụ thể nêu ở Chương 1 ứng với các phần của khung theo đúng thứ tự. Mục tiêu thứ nhất được đo bằng $\Delta_{\text{Taylor}}$ tại một trọng số trộn chung. Mục tiêu thứ hai lặp phép đo đó dọc các chế độ không đồng nhất và đặt kết quả lên trục $\mathrm{Drop}$. Mục tiêu thứ ba dùng hai lát cắt theo $\lambda$ và theo $M$, kèm chi phí truyền thông. Mục tiêu thứ tư dựa vào các đại lượng chẩn đoán tầng phân lớp mà giao thức yêu cầu ghi lại ở mọi lần chạy.

### 4.1.2. Kiến trúc

Khung giữ cấu trúc hai phía quen thuộc của học liên kết, gồm máy chủ điều phối và client huấn luyện cục bộ (Hình 4.1). Mỗi lần chạy đi qua bốn giai đoạn.

Giai đoạn chuẩn bị ở client diễn ra một lần, trước vòng truyền thông đầu tiên. Client $i$ rút ngẫu nhiên $M$ ảnh cục bộ, tính ảnh trung bình $\bar x_g$ và nhãn mềm $\bar y_g$ theo (3.11), rồi lặp lại $n_V$ lần để có $n_V$ cặp. Các cặp này được gửi lên máy chủ. Ảnh riêng lẻ không rời client; thứ rời client là trung bình của $M$ ảnh.

Máy chủ gom các cặp của mọi client thành tập $V$ gồm $N n_V$ phần tử, rồi phát tập đó xuống mọi client, cũng một lần. Từ đây $V$ cố định suốt quá trình huấn luyện.

Ở mỗi bước cục bộ của vòng lặp huấn luyện, client lấy một lô $B$ ảnh của mình và rút có hoàn lại $B$ phần tử của $V$, ghép cặp một-một. Hàm mất mát được tính theo một trong các cấu hình của trục thứ nhất: FedAvg bỏ qua $V$, còn A, B và C dùng $V$ theo các công thức ở mục 4.2. Sau $K$ bước, máy chủ gộp tham số bằng trung bình có trọng số như FedAvg [2], không thay đổi gì.

Lớp ghi nhận bao quanh cả bốn giai đoạn. Ở mỗi mốc đánh giá, nó ghi độ chính xác trên từng môi trường kiểm tra, thời gian mỗi bước, bộ nhớ đỉnh, toàn bộ cấu hình siêu tham số, và các đại lượng chẩn đoán liệt kê ở mục 4.5.6.

Giai đoạn chuẩn bị là chỗ khung khác mã FedBR nhiều nhất. Trong mã phát hành, một lô mẫu trung bình mới được dựng ở mỗi bước cục bộ, lấy thẳng từ dữ liệu thô của mọi client, và dùng chung cho mọi client trong bước ấy. Mô phỏng chạy được như vậy vì toàn bộ dữ liệu nằm trên một máy. Trong triển khai thật thì cách làm đó không có đối ứng, và với nó cũng không tồn tại tập $V$ hữu hạn nào để tính chi phí truyền thông. Khung thay nó bằng tập $V$ cố định, dựng một lần; giá trị $n_V$ được đăng ký ở Chương 5.

> `[CẦN VẼ — Hình 4.1]` Sơ đồ hai cột, máy chủ bên trái, client bên phải. Ba khối tô khác màu: giai đoạn chuẩn bị (tham số $M$, $n_V$), bộ chọn cấu hình hàm mất mát (FedAvg / A / B / C), và lớp ghi nhận.

**Hình 4.1.** Kiến trúc khung thực nghiệm. Mũi tên nét đứt là trao đổi diễn ra một lần trước huấn luyện: các cặp mẫu trung bình đại diện đi lên máy chủ, tập $V$ đi xuống client. Mũi tên nét liền là trao đổi tham số mô hình ở mỗi vòng truyền thông. Ba khối tô màu là ba chỗ khung mở rộng mã nguồn FedBR [11].

### 4.1.3. Quan hệ với mã nguồn FedBR

Khung được cài trên mã nguồn công bố của FedBR [11]. Mã này có sẵn cấu hình A và B, bộ phân hoạch dữ liệu, bộ dữ liệu CIFAR-10 xoay, và các thuật toán đối chứng. Phần luận văn bổ sung gồm:

- cấu hình C;
- tập $V$ cố định, với $M$ và $n_V$ là tham số cấu hình;
- chuẩn hoá lại số hạng gradient của cấu hình B, trình bày ở mục 4.2.3;
- tham số $\alpha_{\text{rot}}$, cùng một chế độ lệch đặc trưng thuần có phân phối nhãn đều;
- mốc IID có xoay dùng cho trục $\mathrm{Drop}$;
- một tập môi trường kiểm tra chung cho mọi cấu hình;
- các đại lượng chẩn đoán trong lớp ghi nhận.

Chương 5 liệt kê từng thay đổi mã nguồn kèm lý do, và tách riêng những thay đổi làm đổi số liệu so với mã gốc.

## 4.2. Cô lập số hạng khai triển Taylor

### 4.2.1. Bốn cấu hình và cấu hình C

Hai chỗ khác nhau giữa NaiveMix và FedMix là hai trục nhị phân. Tổ hợp của chúng cho bốn cấu hình, xếp ở Bảng 4.2.

**Bảng 4.2.** Bốn cấu hình hàm mất mát sinh ra từ hai chỗ khác nhau giữa NaiveMix (3.12) và FedMix (3.15). Hàng là điểm đánh giá hàm mất mát, tức ảnh được đưa vào mô hình, trong đó $x_i$ là ảnh cục bộ, $\bar x_g$ là ảnh trung bình đại diện rút từ tập $V$, và $\lambda$ là trọng số trộn. Cột là sự có mặt của số hạng gradient (III) trong (3.14), tức $\lambda(1{-}\lambda)\,\nabla_x \ell_{y_i}\cdot\bar x_g$. A và B là hai thuật toán của bài báo FedMix [1]; C định nghĩa ở (4.1); D không được chạy.

| Điểm đánh giá | không có (III) | có (III) |
|---|---|---|
| $(1{-}\lambda)x_i + \lambda\bar x_g$ | A (NaiveMix) | D |
| $(1{-}\lambda)x_i$ | C | B (FedMix) |

Cấu hình C là FedMix sau khi bỏ đúng số hạng (III):

$$\mathcal{L}_{\text{C}} = (1{-}\lambda)\,\ell\big(f((1{-}\lambda)x_i),\, y_i\big) + \lambda\,\ell\big(f((1{-}\lambda)x_i),\, \bar y_g\big). \tag{4.1}$$

Trong (4.1), ảnh trung bình $\bar x_g$ không xuất hiện ở đâu cả. Thứ duy nhất C nhận từ client khác là nhãn mềm $\bar y_g$. Nhận xét này cho một cách đọc gọn cho cả ba cấu hình được chạy. C là mốc chung, dùng nhãn mềm mà không dùng chút thông tin ảnh nào. A và B thêm vào mốc đó cùng một lượng thông tin ảnh, qua hai đường khác nhau. A trộn $\bar x_g$ thẳng vào đầu vào, nên mô hình nhìn thấy ảnh đã trộn. B chỉ cho $\bar x_g$ đi vào qua tích vô hướng với gradient theo đầu vào, tức qua một xấp xỉ tuyến tính của chính phép trộn ấy.

Ô D giữ phép trộn ở đầu vào và đồng thời thêm số hạng (III), nên $\bar x_g$ vào hàm mất mát hai lần, một lần qua lượt truyền xuôi và một lần qua đạo hàm. Cấu hình này không ứng với khai triển nhất quán nào của (3.10), và luận văn không chạy nó.

### 4.2.2. Ba đại lượng và một đồng nhất thức

Ký hiệu $\mathrm{Acc}(X)$ là độ chính xác của mô hình toàn cục huấn luyện với cấu hình $X$, theo chỉ số ở mục 4.5.3. Mọi hiệu dưới đây tính theo cặp: hai lần chạy được đem trừ dùng cùng hạt giống, cùng phân hoạch, cùng tập $V$, cùng $\lambda$ và cùng $M$.

Đại lượng trung tâm của luận văn là

$$\Delta_{\text{Taylor}} = \mathrm{Acc}(\text{B}) - \mathrm{Acc}(\text{C}). \tag{4.2}$$

B và C có cùng điểm đánh giá và cùng hai số hạng đầu, nên hiệu giữa hai hàm mất mát đúng bằng số hạng (III). Theo cách đọc ở mục trước, $\Delta_{\text{Taylor}}$ đo lượng thông tin ảnh mà đường xấp xỉ tuyến tính chuyển được thành độ chính xác.

Đại lượng đối xứng với nó đo đường còn lại:

$$\Delta_{\text{trộn}} = \mathrm{Acc}(\text{A}) - \mathrm{Acc}(\text{C}). \tag{4.3}$$

Bài báo FedMix báo cáo chênh lệch giữa FedMix và NaiveMix. Trên cùng các lần chạy, chênh lệch đó được xác định hoàn toàn bởi hai đại lượng trên:

$$\Delta_{\text{gốc}} = \mathrm{Acc}(\text{B}) - \mathrm{Acc}(\text{A}) = \Delta_{\text{Taylor}} - \Delta_{\text{trộn}}. \tag{4.4}$$

(4.4) là một đồng nhất thức. Nó không phải giả thuyết để kiểm tra, và không để lại phần dư nào để báo cáo. Giá trị của nó nằm ở cách đọc. Một $\Delta_{\text{gốc}}$ dương có thể đến từ hai nguồn: đường tuyến tính mang được nhiều thông tin, tức $\Delta_{\text{Taylor}}$ lớn; hoặc phép trộn thẳng làm mô hình kém đi so với mốc chỉ dùng nhãn mềm, tức $\Delta_{\text{trộn}}$ âm. Nếu chỉ đo $\Delta_{\text{gốc}}$, như bài báo FedMix đã làm, hai trường hợp này không tách được. Đo (4.2) và (4.3) thì tách được.

Bỏ ô D có một hệ quả xác định. Số hạng (III) chỉ được đo tại một điểm đánh giá, $(1{-}\lambda)x_i$. Hiệu D − A đo cùng số hạng ấy tại điểm đánh giá còn lại; đặt D − A cạnh B − C sẽ cho biết tác động của (III) có đổi hay không khi $\bar x_g$ đồng thời có mặt trong lượt truyền xuôi. Với ba ô, tương tác đó không ước lượng được.

### 4.2.3. Chuẩn hoá số hạng gradient trong mã FedBR

Để B đúng là (3.15), cả ba số hạng phải được lấy trung bình trên lô theo cùng một cách. Cài đặt FedMix trong mã FedBR làm vậy với hai số hạng đầu, còn số hạng thứ ba thì không.

Trình tự tính trong mã như sau. `loss1` là $(1{-}\lambda)$ nhân trung bình cross-entropy trên lô $B$ ảnh đã co tỉ lệ, nên đạo hàm của nó theo từng ảnh mang sẵn thừa số $(1{-}\lambda)/B$. `loss3` nhân đạo hàm đó với $\bar x_g$, nhân thêm $\lambda$, cộng trên cả lô, rồi chia thêm một lần nữa cho $B$. Thừa số $1/B$ vì vậy xuất hiện hai lần, và số hạng (III) đi vào mục tiêu với hệ số $\lambda(1{-}\lambda)/B$ trong khi (3.15) đòi $\lambda(1{-}\lambda)$. Phần $\lambda(1{-}\lambda)$ được tính đúng, như Chương 3 đã đối chiếu; chỗ lệch nằm ở phép chuẩn hoá theo lô.

Luận văn kiểm tra điều này bằng một phép thử trực tiếp trên một mạng tuyến tính nhỏ. Đoạn mã tính `loss3` được chạy nguyên văn, rồi so với trung bình trên lô của số hạng (III) tính từ gradient của từng mẫu. Tỉ lệ giữa hai giá trị đúng bằng 8 khi lô có 8 ảnh, và bằng 32 khi lô có 32 ảnh. Với kích thước lô 32 của cấu hình thực nghiệm, số hạng Taylor trong mã phát hành nhỏ hơn công thức 32 lần.

Hệ quả cho phép cô lập là trực tiếp. Chạy B bằng mã phát hành thì B gần trùng C, và khi đó một $\Delta_{\text{Taylor}}$ xấp xỉ không chỉ phản ánh cách chuẩn hoá. Khung vì vậy cài B theo đúng (3.15), với số hạng (III) lấy trung bình trên lô như hai số hạng kia. Cách chuẩn hoá của mã phát hành được giữ lại làm một cấu hình phụ, ký hiệu B′, chạy ở hai cấu hình lệch chính với số hạt giống của phần thăm dò. Chương 5 báo cáo mức chênh giữa B và B′ trong phần kiểm toán tính tái lập.

### 4.2.4. Các yếu tố gây nhiễu

Bốn yếu tố có thể khiến $\Delta_{\text{Taylor}}$ đo được lệch khỏi đóng góp thật của số hạng (III). Khung xử lý mỗi yếu tố bằng một đại lượng ghi nhận hoặc một ràng buộc thiết kế.

**Biên độ của số hạng gradient.** Biên độ của (III) tỉ lệ với độ lớn của $\nabla_x\ell$, và gradient theo đầu vào đổi mạnh trong quá trình huấn luyện. Một $\Delta_{\text{Taylor}}$ gần không có thể do số hạng không mang thông tin, cũng có thể do nó quá nhỏ so với (I) ở cấu hình đang xét. Lớp ghi nhận lưu tỉ số giữa trung bình trên lô của $|\text{(III)}|$ và của (I) ở nhiều mốc vòng để tách hai trường hợp. Lỗi chuẩn hoá ở mục trước là ví dụ cực đoan của loại nhiễu này: nó đổi biên độ của (III) mà không đổi gì khác.

**Trọng số trộn.** $\lambda$ vào hệ số của (III) qua $\lambda(1{-}\lambda)$, và đồng thời quyết định độ tốt của chính phép xấp xỉ. Chương 3 đã tính tỉ lệ giữa hệ số của số hạng bị bỏ (IV) và số hạng được giữ (III) là $\lambda/(1{-}\lambda)$, tăng từ 0,053 ở $\lambda = 0{,}05$ lên 0,25 ở $\lambda = 0{,}2$. B vì vậy bám A càng kém khi $\lambda$ càng lớn, và $\Delta_{\text{gốc}}$ đổi theo $\lambda$ ngay cả khi mọi thứ khác đứng yên. $\Delta_{\text{Taylor}}$ phải được báo cáo tại từng giá trị $\lambda$; mục 4.4 dựng phép quét tương ứng.

**Mức nén.** $M$ càng lớn thì $\bar x_g$ càng mịn và càng mất cấu trúc riêng của từng ảnh. A và B nhận $\bar x_g$ qua hai đường khác nhau, nên có thể phản ứng khác nhau với $M$. $M$ vì vậy được quét, ở mục 4.4.

**Phép co đầu vào.** B và C huấn luyện trên ảnh đã co $(1{-}\lambda)x_i$, còn mô hình được đánh giá trên ảnh gốc. Với backbone không dùng chuẩn hoá theo lô, riêng độ lệch thang giữa lúc huấn luyện và lúc đánh giá đã có thể làm đổi độ chính xác. Yếu tố này triệt tiêu trong $\Delta_{\text{Taylor}}$, vì B và C co ảnh như nhau. Nó vẫn có mặt trong mọi so sánh giữa B hoặc C với FedAvg, nên các so sánh ấy được đọc như so sánh giữa hai phương pháp hoàn chỉnh và không được dùng để quy kết cho số hạng (III).

## 4.3. Chế độ lệch phân phối và trục độ nghiêm trọng

### 4.3.1. Vì sao không dùng ma trận $2 \times 2$

Có hai loại lệch phân phối thì thiết kế tự nhiên là một ma trận: có hoặc không lệch nhãn, nhân với có hoặc không lệch đặc trưng. Luận văn không dùng thiết kế đó, vì đơn vị của hai tham số điều khiển. Lệch nhãn được điều khiển bởi nồng độ Dirichlet $\alpha$ trên phân phối lớp; lệch đặc trưng, bởi nồng độ $\alpha_{\text{rot}}$ trên phân phối góc xoay. Không có căn cứ nào để nói $\alpha = 0{,}1$ nặng ngang $\alpha_{\text{rot}} = 1$. Giả sử ô lệch đặc trưng cho $\Delta_{\text{Taylor}}$ lớn hơn ô lệch nhãn. Người đọc sẽ không phân biệt được số hạng Taylor hữu ích hơn dưới lệch đặc trưng, hay mức lệch đặc trưng được chọn đơn giản là nặng hơn.

Chương 2 đã nêu rằng NIID-Bench [3] không đề xuất cách quy đổi độ nghiêm trọng của hai loại lệch về cùng một thang. Luận văn không giải bài toán quy đổi đó. Mọi cấu hình được chiếu lên một thang chung đo trong không gian kết quả, gọi là trục độ nghiêm trọng, định nghĩa ở mục tiếp theo.

### 4.3.2. Trục chung: độ suy giảm của FedAvg

Trục độ nghiêm trọng xếp các cấu hình lệch phân phối theo lượng độ chính xác mà chúng lấy đi của FedAvg. Với một cấu hình lệch $s$,

$$\mathrm{Drop}(s) = \mathrm{Acc}_{\text{FedAvg}}(s_0) - \mathrm{Acc}_{\text{FedAvg}}(s), \tag{4.5}$$

trong đó $s_0$ là cấu hình IID có cùng phân phối gộp với $s$: gộp dữ liệu của mọi client lại thì $s_0$ và $s$ có cùng phân phối, và hai cấu hình chỉ khác nhau ở cách chia dữ liệu đó cho các client. Mỗi cấu hình khi đó cho một điểm $\big(\mathrm{Drop}(s),\ \Delta_{\text{Taylor}}(s)\big)$, và cả hai loại lệch rơi lên cùng một trục hoành.

Điều kiện "cùng phân phối gộp" quyết định $\mathrm{Drop}$ có nghĩa hay không. Dùng một mốc IID không xoay chung cho mọi cấu hình thì hỏng ngay ở phía lệch đặc trưng. Các cấu hình lệch đặc trưng huấn luyện trên ảnh xoay, mốc không xoay thì không. Hiệu độ chính xác giữa hai bên vì vậy chứa cả phần chênh do tập huấn luyện có hay không có ảnh xoay, vốn chẳng liên quan gì tới cách chia dữ liệu. Trên chỉ số trung bình mười góc, $\mathrm{Drop}$ khi đó còn có thể âm, vì mô hình học từ dữ liệu lệch lại là mô hình duy nhất từng thấy ảnh xoay.

Khung vì vậy dùng hai mốc. Họ lệch nhãn lấy mốc IID không xoay. Họ lệch đặc trưng lấy mốc IID trong đó mỗi ảnh được xoay một góc rút đều trên mười góc, ứng với giới hạn $\alpha_{\text{rot}} \to \infty$ của chính họ Dirichlet đã dùng. Vì kỳ vọng của vector tỉ lệ góc mỗi client là phân phối đều, mốc này đúng bằng phân phối gộp của các cấu hình lệch đặc trưng, tính theo kỳ vọng.

Chỉ số độ chính xác dùng trong (4.5) và trong $\Delta_{\text{Taylor}}$ cũng đi theo họ. Họ lệch nhãn dùng độ chính xác trên môi trường kiểm tra 0°, vì dữ liệu huấn luyện của họ này lấy từ đúng phân phối ấy. Họ lệch đặc trưng dùng trung bình trên mười môi trường góc, với cùng lý do.

Phương án này có ba điểm lợi. Nó gần như không tốn thêm: FedAvg vốn chạy ở mọi cấu hình để làm tham chiếu cho so sánh theo cặp, và mốc IID có xoay chỉ thêm một cấu hình. Nó đổi câu hỏi "loại lệch nào nặng hơn", vốn không trả lời được, thành câu hỏi "$\Delta_{\text{Taylor}}$ biến thiên thế nào theo mức FedAvg bị hại", vốn trả lời được. Và nó cho kết quả ở dạng đường đặc tuyến, tức đồ thị của một đại lượng theo một biến điều khiển, thay cho một giá trị đo tại một điểm.

Giới hạn của trục này quyết định cách đọc mọi đồ thị ở Chương 5, nên cần nói ngay tại đây. $\mathrm{Drop}$ gộp hai thứ: bài toán khó đến đâu, và FedAvg hỏng theo cơ chế nào. Hai loại lệch có thể cho cùng một giá trị $\mathrm{Drop}$ qua hai cơ chế khác hẳn nhau, nên trục này chỉ là một phép căn chỉnh vận hành, tức một cách xếp các cấu hình theo kết quả đo của một thuật toán tham chiếu; nó không thay được bài toán quy đổi độ nghiêm trọng giữa hai loại lệch.

### 4.3.3. Các cấu hình được khảo sát

**Bảng 4.3.** Sáu cấu hình phân hoạch dữ liệu trên CIFAR-10 với 10 client. Tham số Dirichlet ghi theo quy ước của Chương 3. $\alpha_{\text{rot}}$ là nồng độ tổng của vector nồng độ $\alpha_{\text{rot}} \cdot u$ trên 10 góc xoay ($u$ đều), lấy mẫu theo trục góc cho từng client, nồng độ mỗi thành phần $\alpha_{\text{rot}}/10$. $\alpha$ là nồng độ tổng của $\alpha \cdot p$ trên 10 lớp ($p$ đều), lấy mẫu theo trục lớp cho từng client, nồng độ mỗi thành phần $\alpha/10$. $\mathbb{E}[n_{\text{eff}}]$ là kỳ vọng số góc hiệu dụng mỗi client theo (3.7), ước lượng từ $2 \times 10^5$ lần rút; nó bằng 10 khi client dùng đều cả mười góc. Cột *Mốc* là cấu hình $s_0$ trong (4.5).

| Ký hiệu | Phân phối nhãn | Phân phối góc mỗi client | $\mathbb{E}[n_{\text{eff}}]$ | Mốc | Vai trò |
|---|---|---|---|---|---|
| P0 | đều | không xoay | – | – | mốc của P4 |
| P0r | đều | đều trên 10 góc ($\alpha_{\text{rot}} \to \infty$) | 10 | – | mốc của P1–P3 |
| P1 | đều | $\alpha_{\text{rot}} = 1$, mặc định của mã FedBR | 2,09 | P0r | cấu hình chính |
| P2 | đều | $\alpha_{\text{rot}} = 10$ | 5,77 | P0r | dựng đường cong |
| P3 | đều | $\alpha_{\text{rot}} = 100$ | 9,19 | P0r | dựng đường cong |
| P4 | $\mathrm{Dir}(\alpha \cdot p)$, $\alpha = 0{,}1$ | không xoay | – | P0 | cấu hình chính |

P1 lấy mức lệch góc mặc định của mã FedBR nhưng giữ phân phối nhãn đều; bộ dữ liệu xoay gốc của FedBR lệch cả nhãn lẫn góc cùng lúc, nên không dùng được cho họ lệch đặc trưng thuần. Chương 3 đã chỉ ra rằng mức mặc định nằm gần cực trị nặng, mỗi client thực tế dùng khoảng hai góc. P2 và P3 vì vậy đi về phía nhẹ, tức $\alpha_{\text{rot}}$ tăng, mỗi bước một bậc độ lớn. Số góc hiệu dụng tăng từ khoảng 2 lên khoảng 6 rồi 9, trải gần đều khoảng giữa P1 và mốc P0r.

P4 dùng mức lệch nhãn $\alpha = 0{,}1$ của FedBR, cho nồng độ mỗi thành phần 0,01.

### 4.3.4. Tập môi trường kiểm tra chung

Mọi cấu hình được đánh giá trên cùng mười môi trường kiểm tra, mỗi môi trường là tập kiểm tra CIFAR-10 xoay một góc cố định trong tập góc $\Theta$ của Chương 3. Mã phát hành vi phạm điều kiện này ở hai chỗ. Bộ dữ liệu lệch nhãn cho mười môi trường kiểm tra giống hệt nhau, không xoay. Bộ dữ liệu xoay có lỗi ở điều kiện kiểm tra góc, khiến môi trường 0° bị thay bằng một tập xoay ngẫu nhiên; Chương 5 trình bày lỗi này trong phần kiểm toán.

Cả hai chỉ số, độ chính xác ở 0° và trung bình mười góc, được ghi cho mọi cấu hình. Chỉ số chính của mỗi họ đã nêu ở mục 4.3.2; chỉ số còn lại báo cáo kèm. Với họ lệch nhãn, trung bình mười góc đo khả năng tổng quát hoá sang phép xoay mà mô hình chưa từng gặp lúc huấn luyện. Nó được đọc như một đại lượng ngoài phân phối và không đi vào $\mathrm{Drop}$.

## 4.4. Mặt vận hành

Mức cải thiện của một phương pháp chia sẻ thông tin phụ thuộc vào lượng thông tin được phép chia sẻ, và có thể đổi dấu khi lượng ấy đổi; Chương 3 đã dẫn một ví dụ như vậy ở nhóm hiệu chuẩn tầng phân lớp. Với cơ chế tăng cường trung bình, lượng thông tin được điều khiển bởi hai tham số, $\lambda$ và $M$. Mặt vận hành là tập giá trị của một đại lượng, chẳng hạn $\Delta_{\text{Taylor}}$, trên mặt phẳng $(\lambda, M)$. Luận văn không quét toàn lưới mà đo hai lát cắt đi qua điểm mặc định: lát theo $\lambda$ tại $M = 10$, và lát theo $M$ tại $\lambda$ khớp.

### 4.4.1. Hai tham số ngân sách

$\lambda$ quyết định mẫu trung bình được kéo mục tiêu huấn luyện đi xa tới đâu. Khi $\lambda \to 0$, cả A, B và C suy biến về FedAvg. Khi $\lambda$ lớn, xấp xỉ Taylor (3.13) mất hiệu lực vì điểm khai triển không còn gần điểm cần xấp xỉ. Luận văn quét $\lambda \in \{0{,}05;\ 0{,}1;\ 0{,}2\}$. Lưới này trùng phép quét $\lambda$ của NaiveMix trong phụ lục bài báo FedMix [1] trên CIFAR-10, trừ giá trị 0,5, là giá trị mà ở đó độ chính xác của NaiveMix sụt xuống 29,8%.

$M$ quyết định mức nén của mỗi mẫu trung bình. $M = 1$ tương đương chia sẻ ảnh thô; $M$ lớn cho ảnh gần như không còn nhận dạng được. Mã FedBR viết cứng $M = 10$, còn bài báo FedMix không công bố giá trị $M$ đã dùng. Luận văn quét $M \in \{1;\ 10;\ 50\}$. $M = 1$ là mức không nén, cho biết lượng thông tin ảnh lớn nhất mà cơ chế có thể khai thác; ở mức này A trở thành global Mixup trên ảnh thô. $M = 10$ là giá trị mặc định, và $M = 50$ nén mạnh hơn một bậc. $M$ được dùng như đại lượng đại diện thô cho mức bảo mật, trong phạm vi đã nêu ở Chương 1.

### 4.4.2. Ba đại lượng báo cáo cùng nhau

Tại mỗi điểm trên hai lát cắt, luận văn báo cáo đồng thời:

1. độ chính xác, cùng mức chênh theo cặp so với FedAvg và so với C;
2. chi phí truyền thông phụ trội của tập $V$;
3. mức nén $M$.

Chi phí truyền thông của $V$ phát sinh một lần trước vòng đầu tiên, gồm chiều đi lên và chiều đi xuống. Với $N$ client, mỗi client gửi $n_V$ cặp; mỗi ảnh có $d_x$ giá trị, mỗi nhãn mềm có $C$ giá trị, mỗi giá trị chiếm $b$ byte. Chiều lên tốn $N n_V (d_x + C)\, b$ byte; chiều xuống gửi cả tập $V$ tới từng client, tốn $N$ lần chừng ấy. Tổng cộng

$$\mathrm{Cost}_V = N\, n_V\, (d_x + C)\, b\, (N + 1). \tag{4.6}$$

Với CIFAR-10, $d_x = 3 \times 32 \times 32 = 3072$ và $C = 10$. Chương 5 đặt con số này cạnh chi phí truyền mô hình mỗi vòng, $2N|\theta|\,b$ byte với $|\theta|$ là số tham số của mô hình.

Công thức (4.6) cho thấy một điều về hình dạng của phép đánh đổi. Với $n_V$ cố định, $\mathrm{Cost}_V$ không phụ thuộc $\lambda$ hay $M$: trung bình của 50 ảnh có cùng kích thước với trung bình của 1 ảnh. Đánh đổi mà hai lát cắt cho thấy vì vậy là giữa độ chính xác và mức nén, ở một chi phí truyền thông cố định. Muốn đổi chi phí truyền thông thì phải đổi $n_V$.

### 4.4.3. $\lambda$ khớp và $\lambda$ tối ưu riêng

Trên CIFAR-10, bảng kết quả chính của bài báo FedMix [1] cho NaiveMix 77,4% và FedMix 81,2%, cách nhau 3,8 điểm phần trăm. Trong phép quét $\lambda$ ở phụ lục của cùng bài báo, giá trị tốt nhất của NaiveMix là 80,6% tại $\lambda = 0{,}2$, chỉ còn cách FedMix 0,6 điểm. Phần lớn khoảng cách ở bảng chính biến mất khi NaiveMix được chỉnh $\lambda$. Con số 3,8 điểm vì vậy gộp hiệu ứng của cơ chế với hiệu ứng của việc hai thuật toán không được chỉnh $\lambda$ đồng đều.

Luận văn báo cáo hai con số cho mỗi phép so sánh:

- $\Delta$ tại $\lambda$ khớp: mọi cấu hình dùng cùng $\lambda = 0{,}1$, giá trị mặc định của mã FedBR. Đây là phép cô lập, và là con số trả lời câu hỏi nghiên cứu thứ nhất.
- $\Delta$ tại $\lambda$ tối ưu riêng: mỗi cấu hình dùng giá trị $\lambda$ tốt nhất của nó trên lưới quét. Đây là phép so sánh giữa các phương pháp khi mỗi phương pháp đã được chỉnh tới mức tốt nhất.

Giá trị $\lambda$ khớp được chốt trước mọi lần chạy. Nếu chọn nó sau khi xem kết quả quét, giá trị được chọn sẽ nghiêng về cấu hình mà người chọn đang nhìn, và phép cô lập mất tính trung lập.

Khoảng cách giữa hai con số là một kết quả riêng: nó định lượng phần mức cải thiện đến từ việc chỉnh $\lambda$ không đồng đều. Con số thứ hai thiên lạc quan, vì $\lambda$ tốt nhất được chọn và được đánh giá trên cùng các lần chạy quét; Chương 5 ghi điều này ngay cạnh con số. Phép quét cần cho con số thứ hai cũng chính là lát cắt theo $\lambda$ đã nêu, nên không tốn thêm lần chạy nào.

## 4.5. Giao thức đo lường

Ba quy tắc áp cho mọi phép so sánh ở Chương 5 là so sánh theo cặp, chỉ so sánh trong cùng một nền tảng, và báo cáo mức cải thiện dưới dạng đường đặc tuyến. Quy tắc thứ ba đã được dùng ở mục 4.3 và 4.4. Mục này trình bày hai quy tắc đầu, chỉ số độ chính xác, phần thống kê, và danh sách các đại lượng được ghi nhận.

### 4.5.1. So sánh theo cặp

Mọi mức cải thiện đều tính theo cặp. Hai cấu hình đem so dùng cùng một hạt giống, và hạt giống ấy quyết định cùng lúc lần rút phân hoạch dữ liệu, trọng số khởi tạo, tập $V$ và thứ tự các lô. Lịch học và số vòng cũng như nhau. Với mỗi hạt giống, hiệu độ chính xác giữa hai cấu hình là một quan sát, và khoảng tin cậy được tính trên các quan sát đó. Cách làm này loại khỏi phép so sánh phần phương sai do phân hoạch, vốn lớn trong học liên kết mô phỏng. Riêng với phép xoay, số góc hiệu dụng của một client đã dao động quanh kỳ vọng 2,09 với độ lệch chuẩn khoảng 0,80.

### 4.5.2. Chỉ so sánh trong cùng một nền tảng

Luận văn dựa trên hai nền tảng thực nghiệm. Nền tảng Flower trong công trình trước của tác giả [TG] là nguồn của các kết quả nền nêu ở Chương 3; mã nguồn FedBR [11] là nơi chạy toàn bộ thực nghiệm mới ở Chương 5. Hai nền tảng khác nhau ở cách phân hoạch, số client, backbone, tập thuật toán đối chứng, và công sức chỉnh siêu tham số dành cho từng thuật toán. Con số tuyệt đối của chúng vì vậy không đặt cạnh nhau. Mọi phát biểu bắc qua hai nền tảng đặt ở mức cơ chế, dạng "hiện tượng X xuất hiện ở cả hai", và không bao giờ ở dạng "độ chính xác tăng từ $a$ lên $b$".

### 4.5.3. Chỉ số độ chính xác

Chỉ số chính theo quy ước của FedBR [11]: trung bình năm giá trị độ chính xác cao nhất trong các mốc đánh giá của một lần chạy. Dùng chỉ số này thì bảng tái hiện ở Chương 5 so được với bảng của FedBR. Nhược điểm của nó là năm mốc được chọn theo chính độ chính xác trên tập kiểm tra, nên giá trị bị kéo lên. Độ thiên này tác động lên mọi cấu hình nhưng không nhất thiết như nhau: cấu hình có đường học dao động mạnh hơn được lợi nhiều hơn. Cho các phép so sánh trong họ giả thuyết chính, luận văn báo cáo kèm trung bình năm mốc đánh giá cuối cùng, một chỉ số không chọn theo tập kiểm tra. Nếu hai chỉ số cho $\Delta$ trái dấu, điều đó được báo cáo cùng kết quả.

### 4.5.4. Ước lượng và cỡ mẫu

Câu hỏi nghiên cứu thứ nhất được đặt ở dạng ước lượng: $\Delta_{\text{Taylor}}$ lớn bao nhiêu, với khoảng tin cậy nào. Lý do là cỡ hiệu ứng có thể rất nhỏ. Khoảng cách 0,6 điểm giữa NaiveMix đã chỉnh $\lambda$ và FedMix trong bài báo FedMix là một hiệu $\Delta_{\text{gốc}}$, không phải $\Delta_{\text{Taylor}}$. Dù vậy nó cho một thang tham khảo: hiệu ứng cần đo có thể nằm dưới một điểm phần trăm.

Để định cỡ thiết kế, luận văn lấy độ lệch chuẩn của hiệu theo cặp là $s \approx 1{,}2$ điểm phần trăm. Các độ lệch chuẩn mẫu báo cáo trong [TG] cho chênh lệch so với đường cơ sở nằm trong khoảng 0,79 đến 1,37 điểm; 1,2 gần đầu trên của khoảng đó. Bảng 4.4 cho nửa rộng khoảng tin cậy 95% ứng với một số giá trị $n$.

**Bảng 4.4.** Nửa rộng khoảng tin cậy 95% hai phía của trung bình hiệu theo cặp, tính bằng $t_{0{,}975;\,n-1}\, s/\sqrt{n}$ với $s = 1{,}2$ điểm phần trăm; $n$ là số hạt giống. Đơn vị: điểm phần trăm.

| $n$ | 5 | 8 | 12 | 25 |
|---|---|---|---|---|
| Nửa rộng | 1,49 | 1,00 | 0,76 | 0,50 |

Muốn phát hiện một hiệu 0,6 điểm với công suất 80%, ở mức ý nghĩa 5% hai phía, cần khoảng 34 hạt giống cho mỗi cấu hình; con số này ước lượng bằng mô phỏng. Như vậy là hơn bốn lần ngân sách. Thiết kế vì vậy xây quanh việc ước lượng. Luận văn đặt $n = 8$, cho nửa rộng khoảng một điểm phần trăm, phát biểu $\Delta_{\text{Taylor}}$ dưới dạng một khoảng, rồi so cận trên của khoảng đó với khoảng cách 3,8 điểm ở bảng chính của FedMix.

Giá trị $s = 1{,}2$ lấy từ một nền tảng khác và chỉ dùng để định cỡ. Độ lệch chuẩn thật trên FedBR được ước lượng từ chính tám hạt giống và báo cáo ở Chương 5.

### 4.5.5. Họ giả thuyết chính và nhánh không có hiệu ứng

Để kiểm soát so sánh bội, luận văn khai báo trước một họ giả thuyết chính gồm bốn phép so sánh ở hai cấu hình chính P1 và P4, tại $\lambda$ khớp và $M = 10$ (Bảng 4.5).

**Bảng 4.5.** Họ giả thuyết chính. Mỗi giả thuyết được kiểm định bằng phép kiểm định t theo cặp hai phía trên $n = 8$ hạt giống; cả họ hiệu chỉnh theo thủ tục Holm ở mức 5%. B là FedMix cài theo (3.15) với chuẩn hoá đã sửa; C là cấu hình (4.1); P1 và P4 là hai cấu hình của Bảng 4.3.

| | Giả thuyết không | Cấu hình |
|---|---|---|
| H1 | $\Delta_{\text{Taylor}} = 0$ | P1 |
| H2 | $\Delta_{\text{Taylor}} = 0$ | P4 |
| H3 | $\mathrm{Acc}(\text{B}) - \mathrm{Acc}_{\text{FedAvg}} = 0$ | P1 |
| H4 | $\mathrm{Acc}(\text{B}) - \mathrm{Acc}_{\text{FedAvg}} = 0$ | P4 |

Mọi phép so sánh khác được gắn nhãn thăm dò và không tham gia hiệu chỉnh. Nhóm này gồm các cấu hình P0, P0r, P2 và P3, hai lát cắt theo $\lambda$ và $M$, cấu hình phụ B′, và các đại lượng chẩn đoán.

Nếu H1 hoặc H2 không bị bác bỏ, kết quả đó chưa đủ để nói số hạng Taylor vô ích: một kiểm định không có ý nghĩa thống kê không chứng minh giả thuyết không. Cho trường hợp này, luận văn khai báo trước một biên tương đương $\pm 1{,}5$ điểm phần trăm và dùng thủ tục hai phép kiểm định một phía (TOST). Biên được đặt nhỏ hơn nhiều so với khoảng cách 3,8 điểm ở bảng chính của FedMix; một $\Delta_{\text{Taylor}}$ nằm trọn trong biên nghĩa là phần lớn khoảng cách ấy không đến từ số hạng Taylor. Với $n = 8$ và $s = 1{,}2$, nửa rộng khoảng tin cậy 90% dùng cho TOST vào khoảng 0,80 điểm, nên thủ tục chỉ kết luận được tương đương khi trung bình quan sát nằm trong khoảng $\pm 0{,}70$ điểm.

### 4.5.6. Các đại lượng được ghi nhận

Ngoài độ chính xác trên từng môi trường kiểm tra, mỗi lần chạy ghi lại:

- thời gian mỗi bước và bộ nhớ đỉnh, phục vụ phần chi phí tài nguyên;
- tỉ số biên độ giữa số hạng (III) và số hạng (I) ở các mốc vòng, phục vụ yếu tố gây nhiễu thứ nhất ở mục 4.2.4;
- độ chính xác theo từng lớp và ma trận nhầm lẫn;
- chuẩn $\ell_2$ của từng vector trọng số lớp $w_c$ ở tầng cuối.

Hai mục cuối phục vụ mục tiêu cụ thể thứ tư. Chương 3 cho thấy thiên lệch của tầng phân lớp dưới lệch nhãn mang tính định hướng: chuẩn của các $w_c$ gần như đều nhau, trong khi hiệu chuẩn lại tầng cuối làm recall của lớp kém nhất đổi rất mạnh. Nếu cơ chế tăng cường trung bình có tác động lên thiên lệch ấy, dấu vết của nó sẽ hiện ở recall theo lớp rõ hơn ở chuẩn trọng số, và hai đại lượng này được ghi để kiểm tra đúng điều đó.

Phân tích cơ chế dùng mô hình ở vòng cuối. Tuỳ chọn lưu mô hình của mã FedBR ghi đè cùng một tệp ở mỗi mốc, nên mô hình ở vòng có độ chính xác cao nhất không được giữ lại. Dùng vòng cuối làm phân tích nhiễu hơn, vì độ chính xác dao động giữa các vòng khi dữ liệu không đồng nhất. Nó không gây thiên lệch giữa các cấu hình, vì mọi cấu hình được lấy tại cùng một vòng; các bảng độ chính xác cũng không bị ảnh hưởng, vì chúng tính từ nhật ký theo vòng.

Chương 5 áp khung và giao thức này lên mã FedBR đã sửa, bắt đầu từ phần tái hiện và kiểm toán tính tái lập, rồi đi lần lượt qua các câu hỏi nghiên cứu theo thứ tự ba trục của Bảng 4.1.

---

## Tài liệu tham khảo (khối Chương 4)

> Chương này không thêm mục mới vào danh mục. Trích tới [1] FedMix, [2] FedAvg, [3] NIID-Bench, [11] FedBR, theo số của **danh mục trong bản Word** (khớp danh mục 1–16 của `02_chuong2.md` ở bốn số này). `[TG]` là công trình của tác giả trên nền tảng Flower (`03_chuong3.md` bản 23/09 cấp số [17]); **danh mục trong Word hiện chưa có mục này** và Word [17] đang là Ng–Jordan. Điền số sau khi danh mục Word được sửa theo IR#9.

---

## Ghi chú thi hành — đọc trước khi chép vào Word

**1. Các quyết định còn treo `[QUYẾT]` — cần học viên chốt.** Bản này đã viết theo phương án đề xuất ở từng mục; nếu học viên chọn khác thì sửa đúng những chỗ ghi kèm.

| # | Quyết định | Phương án đã viết vào bản này | Chỗ phải sửa nếu đổi |
|---|---|---|---|
| Q1 | Lưới bốn cấu hình và $\mathcal{L}_{\text{C}}$ đặt ở Ch.3 hay Ch.4 | Ch.4, Bảng 4.2 và (4.1) — vì Word Ch.3 hiện không có mục 3.3.5 | Bảng 4.2, (4.1), đoạn đầu mục 4.2.1; Word Ch.1 mục 1.4 |
| Q2 | $\lambda$ khớp | 0,1 (mặc định mã FedBR), chốt trước mọi lần chạy | 4.4.3, Bảng 4.5 |
| Q3 | Lưới $M$ và ngân sách thêm | $\{1; 10; 50\}$ × A/B/C × P1, P4 × 3 hạt giống = 36 lần chạy thêm, ~65 GPU-giờ | Bảng 4.1, 4.4.1; Ch.5 mục 5.1.3 |
| Q4 | P2, P3 | $\alpha_{\text{rot}}$ = 10 và 100 (nồng độ tổng) | Bảng 4.3; Ch.5 mục 5.1.1 |
| Q5 | Cấu hình phụ B′ (chuẩn hoá của mã phát hành) | chạy ở P1, P4 × 3 hạt giống = 6 lần chạy | 4.2.3, 4.5.5 |
| Q6 | $n_V$ (số cặp mẫu trung bình mỗi client) | chưa chọn; đăng ký ở Ch.5 | 4.1.2, (4.6) |
| Q7 | Tiêu đề mục 4.3 trong Word | *"Chế độ lệch phân phối và trục độ nghiêm trọng"* | tiêu đề Word |

Tổng số lần chạy thêm so với `PLAN_ke-hoach-8-tuan.md` §6: P0r (FedAvg × 3) + Q3 + Q5 ≈ 45 lần chạy, ~81 GPU-giờ, khoảng 1,7 ngày lịch trên 2 GPU. PLAN còn dư cho hai lần chạy lại, nên vẫn vừa, nhưng mất gần một lần dư.

**2. Việc lập trình phát sinh.** Hiện mã **chưa có** lớp cho cấu hình C, chưa có cờ `--fedmix_M` hay `--rot_alpha` (đã kiểm bằng `rg` trên `fedbr/`). Cần làm, theo thứ tự ưu tiên:

1. Lớp cho cấu hình C: sao `FedMix`, bỏ `grad` và `loss3`.
2. Sửa chuẩn hoá `loss3` của `FedMix`: bỏ phép chia thứ hai cho `len(all_augmentation_y)` (tức cộng trên lô rồi thôi, vì `grad` đã mang $1/B$), và giữ bản gốc dưới tên riêng làm B′. **Phải xong trước mọi lần chạy E1/E2**; chạy trước khi sửa thì toàn bộ nhánh B phải chạy lại.
3. Tập $V$ cố định: dựng một lần từ từng client với tham số $M$, $n_V$; mỗi bước rút có hoàn lại $B$ phần tử. Thay cho lời gọi `get_augmentation_fedmix_data` ở mỗi bước (`train_fed.py:439–442`).
4. Cờ `--rot_alpha`, chế độ lệch đặc trưng thuần, và mốc P0r ($\alpha_{\text{rot}} \to \infty$: rút góc đều).
5. Tập môi trường kiểm tra chung (P-2 / T5) và sửa lỗi môi trường 0° (T12).
6. Ghi tỉ số $|\text{(III)}| / \text{(I)}$ theo mốc vòng.

**3. Việc ở file khác và trong Word, phát sinh từ lượt này.**

- **Word Ch.3 mục 3.3.4**, đoạn "Ánh xạ sang cài đặt": thêm một câu nói `loss3` trong mã chia thêm cho kích thước lô, nên phép "khớp" chỉ đúng với thừa số $\lambda(1{-}\lambda)$. Câu hiện tại *"ở đó nó là một chỗ mà mã và lý thuyết khớp nhau"* sai một nửa.
- **Word Ch.3** thiếu ba mục của bản 23/09: 3.3.5 (lưới bốn cấu hình, xem Q1), 3.3.6 (số hạng bậc hai) và 3.6 (kết quả nền từ công trình của tác giả, gồm Bảng 3.3 về CCVR). Word mục 3.5.2 đang trỏ tới *"số liệu ở cuối chương"* mà cuối chương không có số liệu nào. Mục 4.4 bản này cũng dẫn *"Chương 3 đã dẫn một ví dụ như vậy ở nhóm hiệu chuẩn tầng phân lớp"*; câu đó chỉ đúng khi 3.6 có mặt trong Word.
- **Word Ch.3** đánh hai phương trình cùng số (3.2). Word mục 3.5.2 trích *"Đo lường trong [17]"* và *"Phép đo trong [17] thực hiện ở n/d ≈ 3,9"*, nhưng Word [17] là Ng–Jordan. Cả hai chỗ phải trỏ tới công trình của tác giả.
- **Word Ch.2 mục 2.4.1** viết cấu hình cô lập là cấu hình *"giữ nguyên điểm đánh giá hàm mất mát, tức mẫu trung bình **vẫn tham gia lượt truyền xuôi như ở FedMix**"*. Sai: ở FedMix, $\bar x_g$ **không** đi vào lượt truyền xuôi (Word Ch.3 mục 3.3.4, hệ quả thứ nhất). Sửa thành *"…tức giữ điểm đánh giá $(1{-}\lambda)x_i$ của FedMix, và chỉ loại bỏ số hạng đạo hàm"*.
- **Word Ch.2**, thấy trong lúc đọc: mục 2.4.3 trích NIID-Bench là [8] (đúng là [3]; [8] là Zhao và cộng sự); mục 2.4.4 còn *"hai khoảng trống"* và trỏ *"mục 2.3.1"* (nay là 2.4.1); mục 2.2.1.3 trích MOON là [6], trùng số với SCAFFOLD, và danh mục Word không có MOON.
- **Word Ch.1**: đoạn sau bốn mục tiêu cụ thể viết *"cả **năm** mục tiêu đều được phát biểu ở dạng ước lượng"*, mà mục tiêu nay còn bốn. Mục 1.2.2 vẫn tháo cơ chế thành bốn thành phần, còn vế *"tác vụ cùng hàm mất mát"* (quyết định 22/09 đã chốt rút về ba nhưng Word chưa sửa).
- **`05_chuong5.md`**: mục 5.3 bỏ *"kiểm tra tính cộng tính và báo cáo phần dư"* (A2), thay bằng báo cáo $\Delta_{\text{Taylor}}$, $\Delta_{\text{trộn}}$ và $\Delta_{\text{gốc}}$ theo (4.4). Mục 5.1.1 điền P2, P3 và thêm P0r. Mục 5.1.2 thêm các thay đổi mã ở mục 2 phía trên, trong đó sửa chuẩn hoá `loss3` thuộc nhóm **làm đổi kết quả**. Mục 5.1.3 đăng ký phép quét $M$ và B′. Mục 5.2.2 viết lại: hệ số $\lambda(1{-}\lambda)$ đúng, nhưng phép chuẩn hoá theo lô lệch một hệ số $B$; đây là một sai lệch mới trong danh mục kiểm toán, không còn là "xác nhận âm tính" trọn vẹn. Mục 5.3–5.8 đổi mọi tham chiếu phương trình (4.1)–(4.4) theo đánh số mới.
- **`00_outline.md` §3.1**: dòng ghi tắt `loss3 = Σ(λ·grad·x̄_g)/n` nay có thêm lý do phải chú thích lại: phép chia cho `n` chính là chỗ thừa $1/B$.
- **Đối chiếu nguồn còn mở:** (a) V9 trong `NOTE_khao-sat-van-lieu.md`, tức Bảng 1 của FedMix dùng $\lambda$ chung hay riêng từng nhánh. Word Ch.2 mục 2.4.1 đã khẳng định là riêng; mục 4.4.3 bản này tránh phụ thuộc vào V9 bằng cách chỉ dùng số liệu Bảng 1 và Bảng 17. (b) Thuật toán 1 của bài báo FedMix: mẫu trung bình được chia sẻ một lần hay định kỳ. Mục 4.1.2 bản này không dựa vào bài báo cho điểm này, nhưng nếu học viên muốn viết *"đúng với giao thức MAFL"* thì phải tra trước. (c) Nguồn của $s \approx 1{,}2$: mục 4.5.4 dựa vào khoảng 0,79–1,37 lấy từ `00_outline.md` §3.3 và `NOTE_bien-ban-binh-duyet.md`; đối chiếu lại với bản toàn văn của công trình tác giả.

**4. Vì sao đặt tên $\Delta_{\text{trộn}}$ thay cho $\Delta_{\text{đánh giá}}$ của bản 16/09.** A và C khác nhau ở điểm đánh giá, nên tên cũ không sai. Nhưng khi đọc C là mốc không dùng thông tin ảnh, hiệu A − C là phần đóng góp của phép trộn ảnh vào đầu vào, và tên mới nói đúng điều đó. Tên cũ còn gây hiểu nhầm rằng B − C thì không khác nhau ở điểm đánh giá vì một lý do đặc biệt nào đó, trong khi đó chỉ là cách lưới được dựng.

**5. Phép thử `loss3`.** Tệp `check_loss3.py` nằm trong thư mục scratchpad của phiên làm việc này, không nằm trong kho mã. Nếu muốn giữ làm hiện vật cho phần kiểm toán ở Ch.5, chép nó vào `scripts/` hoặc `tests/`; nó chạy trên CPU trong vài giây và chỉ cần `torch`.
---

## Bổ sung 24/09/2026 (lượt 2) — sau khi lập `INDEX_ma-nguon-va-ket-qua.md`

> Chỉ-append; phần trên giữ nguyên. Chưa sửa vào thân chương, chờ học viên chốt cách nói.

**Phép chuẩn hoá thừa $1/B$ không riêng của FedBR.** Mục 4.2.3 viết *"Cài đặt FedMix trong mã FedBR…"* như thể đây là lỗi của một kho. Đối chiếu cả ba bản mã mở cho thấy **cả ba** đều chia số hạng (III) thêm một lần cho kích thước lô. Căn cứ và số dòng ở chỉ mục F1:
- FedBR `algorithms.py:850`;
- stack Flower của Bài 1 `src/data/augmentation.py:344`, với $B = 10$;
- DevPranjal `fedmix/client.py:197`.

Bài báo FedMix không có mã chính thức. Ba việc cần làm:

1. **Mục 4.2.3.** Đổi câu mở thành *"Cả ba bản cài đặt FedMix mã mở mà luận văn đối chiếu, gồm mã FedBR, mã của công trình trước của tác giả và bản cài đặt của DevPranjal, đều…"*. Ví dụ tỉ lệ 8 và 32 giữ nguyên, vì đó là phép thử trên mã FedBR. Cấu hình phụ B′ nên gọi là *"cách chuẩn hoá chung của các bản cài đặt mã mở"*, không gọi là *"của mã phát hành"*.
2. **Ch.3 mục 3.6.** Câu *"Đây là kết quả về chính cơ chế mà luận văn nghiên cứu"* cần một hạn định: kết quả −1,86 pp đo với số hạng Taylor nhỏ hơn công thức 10 lần. Điều này **tăng** giá trị của phép đo B so với B′ ở Ch.5, vì đó là lần đầu số hạng được đo ở đúng biên độ của (3.15). Có thể nêu ý này ở Ch.4 mục 4.2.3 bằng một câu, không cần tuyên bố tính mới.
3. **Mục 4.5.4.** Khoảng 0,79–1,37 đã khớp với số liệu trong Bài 1. Câu *"luận văn lấy $s \approx 1{,}2$"* đúng là lựa chọn của luận văn, không phải con số của bài, và câu văn hiện tại đã nói đúng như vậy. Riêng `00_outline.md` IR#2 và §3.3 đang ghi cận trên −0,53 như số của Bài 1. Con số đó không có trong bài, và tính lại ra −0,52 (chỉ mục F2).

---

# YÊU CẦU SỬA — 24/09/2026 (lượt 3) · bỏ `[TG]`, nền tảng Flower là của luận văn

> **Căn cứ:** quyết định 24/09 (`00_outline.md` §1.5). Thân bài không trích bài hội nghị; các kết quả trên nền tảng Flower nay nằm ở Ch.5 mục 5.2.
>
> **Cách dùng.** Word chưa có thân Chương 4. Khi chép bản `PHIÊN BẢN CHỈNH SỬA — 24/09/2026` vào Word, áp các thay đổi trong bảng dưới. Cột *Trước* chép nguyên văn từ bản đó. Khối bổ sung *"lượt 2"* ngay phía trên (về phép chuẩn hoá $1/B$) được thi hành bằng hàng 1 và hàng 2. Chỉ-append.

| # | Mục | Trước | Sau | Lý do |
|---|---|---|---|---|
| 1 | 4.2.3, đoạn 1, câu 2 | Cài đặt FedMix trong mã FedBR làm vậy với hai số hạng đầu, còn số hạng thứ ba thì không. | Cả ba bản cài đặt FedMix mã mở mà luận văn đối chiếu, gồm mã FedBR, bản cài đặt trên nền tảng Flower dùng ở mục 5.2 và bản của DevPranjal, đều làm vậy với hai số hạng đầu nhưng không làm với số hạng thứ ba. Phần dưới trình bày chi tiết trên mã FedBR. | Lỗi $1/B$ không riêng FedBR (`INDEX_ma-nguon-va-ket-qua.md` F1) |
| 2 | 4.2.3, đoạn cuối, hai câu cuối | Cách chuẩn hoá của mã phát hành được giữ lại làm một cấu hình phụ, ký hiệu B′, chạy ở hai cấu hình lệch chính với số hạt giống của phần thăm dò. Chương 5 báo cáo mức chênh giữa B và B′ trong phần kiểm toán tính tái lập. | Cách chuẩn hoá chung của các bản cài đặt mã mở được giữ lại làm một cấu hình phụ, ký hiệu B′, chạy ở hai cấu hình lệch chính với số hạt giống của phần thăm dò. FedMix ở mục 5.2 được chạy đúng theo cách này, nên mức chênh giữa B và B′ cho biết kết quả âm ở đó có phụ thuộc vào biên độ của số hạng Taylor hay không. | B′ nay nối trực tiếp với kết quả mục 5.2 |
| 3 | 4.4, đoạn mở, vế sau câu 1 | …và có thể đổi dấu khi lượng ấy đổi; Chương 3 đã dẫn một ví dụ như vậy ở nhóm hiệu chuẩn tầng phân lớp. | …và có thể đổi dấu khi lượng ấy đổi; thực nghiệm ở mục 5.2 cho thấy điều đó ở nhóm hiệu chuẩn tầng phân lớp. | Ví dụ CCVR chuyển từ Ch.3 (mục 3.6 đã bỏ) sang Ch.5 |
| 4 | 4.5.2, câu 2 | Nền tảng Flower trong công trình trước của tác giả [TG] là nguồn của các kết quả nền nêu ở Chương 3; mã nguồn FedBR [11] là nơi chạy toàn bộ thực nghiệm mới ở Chương 5. | Nền tảng Flower là nơi chạy các thực nghiệm dưới lệch phân phối nhãn ở mục 5.2; mã nguồn FedBR [11] là nơi chạy các thực nghiệm còn lại của Chương 5. | Bỏ `[TG]` |
| 5 | 4.5.4, đoạn 2, câu 2 | Các độ lệch chuẩn mẫu báo cáo trong [TG] cho chênh lệch so với đường cơ sở nằm trong khoảng 0,79 đến 1,37 điểm; 1,2 gần đầu trên của khoảng đó. | Trên nền tảng Flower, độ lệch chuẩn mẫu của các hiệu theo cặp ở Bảng 5.2–5.5 phần lớn nằm trong khoảng 0,79 đến 1,37 điểm trên CIFAR-10; 1,2 gần đầu trên của khoảng đó. | Bỏ `[TG]`; nguồn nay là số đo của chính luận văn |
| 6 | 4.5.4, đoạn cuối, câu 1 | Giá trị $s = 1{,}2$ lấy từ một nền tảng khác và chỉ dùng để định cỡ. | Giá trị $s = 1{,}2$ lấy từ nền tảng Flower và chỉ dùng để định cỡ. | Như trên |
| 7 | 4.5.6, đoạn 2, câu 2 | Chương 3 cho thấy thiên lệch của tầng phân lớp dưới lệch nhãn mang tính định hướng: chuẩn của các $w_c$ gần như đều nhau, trong khi hiệu chuẩn lại tầng cuối làm recall của lớp kém nhất đổi rất mạnh. | Chương 3 nêu hai giả thuyết về dạng thiên lệch của tầng phân lớp, và mục 5.2.4 cho thấy dưới lệch nhãn thiên lệch mang tính định hướng: chuẩn của các $w_c$ gần như đều nhau, trong khi hiệu chuẩn lại tầng cuối làm recall của lớp kém nhất đổi rất mạnh. | Ch.3 chỉ còn giả thuyết; số đo ở Ch.5 |
| 8 | Khối *Tài liệu tham khảo (khối Chương 4)* | …`[TG]` là công trình của tác giả trên nền tảng Flower… Điền số sau khi danh mục Word được sửa theo IR#9. | Chương này trích [1] FedMix, [2] FedAvg, [3] NIID-Bench, [7] CCVR, [11] FedBR. Không trích công trình của tác giả; bài ISWTA 2026 chỉ nằm trong *Danh mục công bố khoa học của tác giả*. | Khối siêu dữ liệu, không vào Word |

**Tham chiếu tới Chương 5 trong bản 24/09 phải dịch số** theo cấu trúc mới của Ch.5, vì mục 5.2 mới đẩy các mục sau lên một số:
- *"danh mục kiểm toán ở Chương 5"* nay là mục 5.3;
- *"mục 5.1"* (kiểm soát kiến trúc, đăng ký thí nghiệm) giữ nguyên.

Thân Ch.4 hiện chỉ trỏ tới Chương 5 ở cấp chương, nên không có số mục nào cần đổi ngoài bảng trên.
