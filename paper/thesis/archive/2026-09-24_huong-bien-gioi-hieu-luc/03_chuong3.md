# CHƯƠNG 3 — CƠ SỞ LÝ THUYẾT

> **KHỐI TRẠNG THÁI** · 16/09/2026
>
> | Mục | Trạng thái |
> |---|---|
> | 3.1 – 3.6 | `[BẢN NHÁP ĐẦY ĐỦ]` — chờ tác giả chỉnh lý |
> | §3.3.4 | ⚠️ **Chứa dẫn xuất giải quyết V1.** Cần đối chiếu ký hiệu Eq. (5) của [13] để xác nhận |
> | §3.6 | ⚠️ **IR#9** — phải điền tên hội nghị/DOI và khai báo tái sử dụng trước khi nộp |
>
> Ký hiệu thống nhất theo `00_outline.md` §7.1. Trích dẫn dùng chung danh mục của `02_chuong2.md`.

---

## 3.1. Bài toán Học liên kết và local SGD

### 3.1.1. Hình thức hoá

Hệ thống gồm $N$ client. Client $i$ giữ tập dữ liệu cục bộ $\mathcal{D}_i = \{(\mathbf{x}, y)\}$ lấy mẫu từ phân phối $P_i(\mathbf{x}, y)$, và định nghĩa hàm mục tiêu cục bộ

$$f_i(\boldsymbol\omega) = \mathbb{E}_{(\mathbf{x},y)\sim P_i}\big[\ell(f(\mathbf{x};\boldsymbol\omega),\, y)\big],$$

với $f(\cdot\,;\boldsymbol\omega)$ là mô hình và $\ell$ là hàm mất mát. Mục tiêu toàn cục là tổ hợp lồi $f(\boldsymbol\omega) = \sum_i p_i f_i(\boldsymbol\omega)$, $p_i = |\mathcal{D}_i| / \sum_j |\mathcal{D}_j|$.

Trong luận văn này, mô hình được tách thành **bộ trích xuất đặc trưng** $\phi: \mathcal{X} \to \mathbb{R}^d$ và **bộ phân lớp** $\omega: \mathbb{R}^d \to \mathbb{R}^C$, tức $f = \omega \circ \phi$. Phép tách này cần thiết vì phần lớn lập luận ở §3.4 và §3.5 định vị thiên lệch vào một trong hai thành phần.

Chiều đặc trưng $d$ **phụ thuộc kiến trúc** và được ghi rõ ở mọi bảng kết quả: $d = 512$ với VGG11 và ResNet18, $d = 256$ với CCT, $d = 64$ với ResNet20-GN.

### 3.1.2. FedAvg và nguồn gốc client drift

Ở vòng truyền thông $t$, FedAvg [1] thực hiện:

1. Máy chủ phát $\boldsymbol\omega_t$ tới tập client được chọn $\mathcal{S}_t$.
2. Mỗi client $i \in \mathcal{S}_t$ đặt $\boldsymbol\omega_i^0 \leftarrow \boldsymbol\omega_t$ rồi chạy $K$ bước SGD trên $f_i$, thu được $\boldsymbol\omega_i^K$.
3. Máy chủ gộp: $\boldsymbol\omega_{t+1} = \sum_{i \in \mathcal{S}_t} \tilde p_i\, \boldsymbol\omega_i^K$.

Khi $K = 1$ và mọi client tham gia, quy trình trùng với SGD tập trung trên $f$. Khi $K > 1$, mỗi client chạy nhiều bước trên mục tiêu **riêng** của nó. Nếu $P_i \ne P_j$ thì $\arg\min f_i \ne \arg\min f_j$, và sau $K$ bước, các $\boldsymbol\omega_i^K$ hội tụ về các điểm khác nhau. Trung bình của các điểm đã lệch nói chung **không** là một bước tiến tốt cho $f$ — đây là **client drift**.

Hai đại lượng điều khiển mức độ nghiêm trọng: **số bước cục bộ $K$** (càng lớn càng trôi xa) và **mức chênh lệch giữa các $P_i$**. Luận văn giữ $K$ cố định theo cấu hình đã đăng ký và khảo sát trục thứ hai.

---

## 3.2. Mô hình hoá dữ liệu không đồng nhất

### 3.2.1. Phân rã phân phối

Viết $P_i(\mathbf{x}, y) = P_i(y)\,P_i(\mathbf{x} \mid y)$ cho phép tách hai dạng lệch phân phối một cách hình thức:

- **Lệch phân phối nhãn (label skew):** $P_i(y) \ne P_j(y)$, trong khi $P_i(\mathbf{x} \mid y) = P(\mathbf{x} \mid y)$ với mọi $i$.
- **Lệch phân phối đặc trưng (feature skew):** $P_i(\mathbf{x} \mid y) \ne P_j(\mathbf{x} \mid y)$.

Hai trục này độc lập về mặt khái niệm, và luận văn khảo sát chúng riêng rẽ (§4.3). Cần nhấn mạnh rằng sự độc lập này chỉ đúng **ở mức phân phối dữ liệu**. Trong FL sâu, mỗi client huấn luyện một bộ trích xuất riêng $\phi_i$, nên ngay cả khi $P_i(\mathbf{x}\mid y)$ trùng nhau, phân phối **đặc trưng** $\phi_i(\mathbf{x}) \mid y$ vẫn có thể khác nhau giữa các client — chính vì $\phi_i \ne \phi_j$. Đây là một điểm dễ nhầm và được trở lại ở §3.4.

### 3.2.2. Mô phỏng label skew bằng Dirichlet

Luận văn dùng quy ước $\mathbf{q}_i \sim \mathrm{Dir}(\alpha \cdot \mathbf{p})$ theo [3], trong đó $\mathbf{p}$ là phân phối lớp tiên nghiệm với $\sum_c p_c = 1$, và $\alpha$ là **nồng độ tổng**. Nồng độ mỗi thành phần là $\alpha p_c$.

Theo quy ước này, cấu hình đã đăng ký $\alpha = 0{,}1$ trên CIFAR-10 với tiên nghiệm đều cho nồng độ mỗi thành phần $0{,}01$ — một chế độ **rất nghiêng**, trong đó mỗi client thực tế chỉ thấy một vài lớp.

Như §2.1.2 đã cảnh báo, ký hiệu này mơ hồ trong văn liệu. Mọi bảng kết quả trong luận văn ghi đủ bộ ba **(vector nồng độ, trục lấy mẫu, số thành phần)**.

### 3.2.3. Mô phỏng feature skew bằng phép xoay

Feature skew được mô phỏng bằng cách gán cho mỗi client một phân phối trên tập góc xoay $\Theta = \{0°, 15°, \ldots, 135°\}$. Client $i$ rút $\mathbf{q}_i^{\text{rot}} \sim \mathrm{Dir}(\alpha_{\text{rot}} \cdot \mathbf{u})$ với $\mathbf{u}$ đều trên $|\Theta| = 10$ góc, rồi mỗi ảnh cục bộ được xoay bởi một góc lấy mẫu độc lập theo $\mathbf{q}_i^{\text{rot}}$.

Kết quả là $P_i(\mathbf{x} \mid y) = \sum_{\theta} q_{i}^{\text{rot}}(\theta)\, P_0(R_\theta^{-1}\mathbf{x} \mid y)$, với $P_0$ là phân phối gốc và $R_\theta$ là phép xoay — tức các client khác nhau ở **toán tử trộn góc**, còn phân phối nhãn giữ nguyên.

Ba tính chất của cách mô phỏng này cần ghi nhận, vì chúng giới hạn phạm vi kết luận:

1. **Cấu hình mặc định đã ở gần cực trị.** Với $\alpha_{\text{rot}} = 1{,}0$ trên 10 góc, nồng độ mỗi thành phần là $0{,}1$, cho các mẫu $\mathbf{q}_i^{\text{rot}}$ **rất thưa** — mỗi client trên thực tế chỉ dùng một đến hai góc trội. Do đó trục $\alpha_{\text{rot}}$ chỉ quét được về phía **nhẹ hơn**, và đường đặc tuyến ở §5.4 là một nhánh chứ không đối xứng hai phía.

2. **Toán tử trộn dùng chung cho mọi lớp.** Góc được lấy mẫu **độc lập với nhãn**, nên phép biến đổi là như nhau cho mọi lớp trong một client. Đây là feature skew **không phụ thuộc lớp**.

3. **Phép xoay là biến đổi nhóm khả nghịch, thuần hình học.** Nó nằm ở cực dễ của phổ dịch chuyển miền, đơn giản hơn nhiều so với đổi cảm biến, đổi phong cách, hay đổi điều kiện thu thập.

Tính chất thứ hai đáng chú ý ở chỗ nó là **đặc điểm chung của văn liệu**, không riêng cách mô phỏng này: nhiễu Gauss, corruption chuẩn hoá, và phân hoạch theo nguồn thật đều độc lập với lớp. Feature skew **phụ thuộc lớp** — trong đó phép biến đổi khác nhau theo từng lớp — chỉ xuất hiện trong hai tiền lệ nằm ngoài các benchmark FL chuẩn. Luận văn ghi nhận đây là một giới hạn của thiết kế và trở lại ở Chương 6.

---

## 3.3. Global Mixup và xấp xỉ Taylor bậc nhất

Đây là mục trung tâm của chương: nó dẫn xuất chính xác đối tượng mà luận văn đo.

### 3.3.1. Mixup và trở ngại trong Học liên kết

Mixup [12] huấn luyện mô hình trên tổ hợp lồi của các cặp mẫu:

$$\tilde{\mathbf{x}} = (1-\lambda)\mathbf{x}_i + \lambda \mathbf{x}_j, \qquad \tilde{y} = (1-\lambda)y_i + \lambda y_j,$$

với $\lambda$ là **trọng số trộn** và nhãn ở dạng one-hot. Trong FL, phiên bản có ý nghĩa nhất — gọi là **global Mixup** — trộn mẫu của client $i$ với mẫu của client $j \ne i$, vì đó là phép trộn thực sự bắc cầu giữa các phân phối cục bộ. Nhưng nó đòi hỏi $\mathbf{x}_j$ **thô**, tức vi phạm ràng buộc nền tảng của FL.

### 3.3.2. Tách hàm mất mát theo nhãn

Với hàm mất mát cross-entropy, $\ell(f(\mathbf{x}), y) = -\sum_c y_c \log \mathrm{softmax}(f(\mathbf{x}))_c$ là **tuyến tính theo nhãn**. Do đó

$$\ell\big(f(\tilde{\mathbf{x}}),\, (1-\lambda)y_i + \lambda y_j\big) = (1-\lambda)\,\ell\big(f(\tilde{\mathbf{x}}), y_i\big) + \lambda\,\ell\big(f(\tilde{\mathbf{x}}), y_j\big).$$

Mục tiêu global Mixup viết lại thành

$$\mathcal{L}_{\text{GM}} = (1-\lambda)\,\ell\big(f((1{-}\lambda)\mathbf{x}_i + \lambda\mathbf{x}_j), y_i\big) + \lambda\,\ell\big(f((1{-}\lambda)\mathbf{x}_i + \lambda\mathbf{x}_j), y_j\big). \tag{3.1}$$

Toàn bộ phần còn lại của mục này là các cách khác nhau để xấp xỉ (3.1) mà không cần $\mathbf{x}_j$ thô.

### 3.3.3. Mẫu trung bình đại diện và NaiveMix

Khung **MAFL** [13] thay cặp $(\mathbf{x}_j, y_j)$ của một client khác bằng một **mẫu trung bình đại diện**: client $j$ chọn ngẫu nhiên $M$ mẫu cục bộ và tính

$$\bar{\mathbf{x}}_g = \frac{1}{M}\sum_{m=1}^{M} \mathbf{x}_m, \qquad \bar{y}_g = \frac{1}{M}\sum_{m=1}^{M} y_m, \tag{3.2}$$

trong đó $\bar y_g$ là một **nhãn mềm** — histogram nhãn đã chuẩn hoá của $M$ mẫu đó. Chỉ các cặp $(\bar{\mathbf{x}}_g, \bar y_g)$ được chia sẻ. Tham số $M$ điều khiển mức độ nén: $M = 1$ tương đương chia sẻ ảnh thô, $M$ lớn cho ảnh gần như không còn nhận dạng được.

Thay trực tiếp vào (3.1) cho thuật toán thứ nhất:

$$\boxed{\;\mathcal{L}_{\text{NaiveMix}} = (1{-}\lambda)\,\ell\big(f((1{-}\lambda)\mathbf{x}_i + \lambda\bar{\mathbf{x}}_g), y_i\big) + \lambda\,\ell\big(f((1{-}\lambda)\mathbf{x}_i + \lambda\bar{\mathbf{x}}_g), \bar y_g\big)\;} \tag{3.3}$$

Điểm cần nhớ: trong NaiveMix, $\bar{\mathbf{x}}_g$ đi vào **bên trong lượt truyền xuôi** — mô hình thực sự nhìn thấy ảnh đã trộn.

### 3.3.4. Khai triển Taylor bậc nhất và FedMix

Thuật toán thứ hai xuất phát từ nhận xét rằng khi $\lambda \ll 1$, điểm $(1{-}\lambda)\mathbf{x}_i + \lambda\bar{\mathbf{x}}_g$ nằm gần $(1{-}\lambda)\mathbf{x}_i$. Khai triển Taylor bậc nhất quanh điểm đó cho, với nhãn $y$ bất kỳ,

$$\ell\big(f((1{-}\lambda)\mathbf{x}_i + \lambda\bar{\mathbf{x}}_g), y\big) \;\approx\; \ell\big(f((1{-}\lambda)\mathbf{x}_i), y\big) \;+\; \lambda\, \nabla_{\mathbf{x}}\,\ell\big(f(\mathbf{x}), y\big)\Big|_{\mathbf{x}=(1-\lambda)\mathbf{x}_i} \cdot \bar{\mathbf{x}}_g. \tag{3.4}$$

Áp (3.4) vào **cả hai** số hạng của (3.3):

$$\mathcal{L} \approx \underbrace{(1{-}\lambda)\,\ell\big(f((1{-}\lambda)\mathbf{x}_i), y_i\big)}_{\text{(I)}} + \underbrace{\lambda\,\ell\big(f((1{-}\lambda)\mathbf{x}_i), \bar y_g\big)}_{\text{(II)}} + \underbrace{\lambda(1{-}\lambda)\,\nabla_{\mathbf{x}}\ell_{y_i} \cdot \bar{\mathbf{x}}_g}_{\text{(III)}} + \underbrace{\lambda^2\,\nabla_{\mathbf{x}}\ell_{\bar y_g} \cdot \bar{\mathbf{x}}_g}_{\text{(IV)}} \tag{3.5}$$

Số hạng (IV) là $O(\lambda^2)$. Ở chế độ vận hành $\lambda \in [0{,}05;\,0{,}2]$ mà cả hai công trình gốc sử dụng, nó nhỏ hơn (III) một bậc và được bỏ qua. Giữ ba số hạng đầu:

$$\boxed{\;\mathcal{L}_{\text{FedMix}} = (1{-}\lambda)\,\ell\big(f((1{-}\lambda)\mathbf{x}_i), y_i\big) + \lambda\,\ell\big(f((1{-}\lambda)\mathbf{x}_i), \bar y_g\big) + \lambda(1{-}\lambda)\,\nabla_{\mathbf{x}}\ell_{y_i} \cdot \bar{\mathbf{x}}_g\;} \tag{3.6}$$

**Ba hệ quả cần ghi nhận.**

*Thứ nhất, $\bar{\mathbf{x}}_g$ không còn đi vào lượt truyền xuôi.* Mô hình chỉ nhìn thấy $(1{-}\lambda)\mathbf{x}_i$ — ảnh cục bộ đã co tỉ lệ. Thông tin từ client khác đi vào **duy nhất** qua số hạng (III), dưới dạng một tích vô hướng với gradient theo đầu vào.

*Thứ hai, hệ số của số hạng gradient là $\lambda(1{-}\lambda)$, không phải $\lambda$.* Thừa số $(1{-}\lambda)$ kế thừa từ trọng số của số hạng (I) trong (3.3). Đây là điểm dễ nhầm khi đọc công thức rút gọn trong [13], nơi số hạng thứ ba được viết dưới dạng $\lambda\,(\partial\ell/\partial\mathbf{x})\cdot\bar{\mathbf{x}}_g$ mà không nói rõ $\partial\ell/\partial\mathbf{x}$ là đạo hàm của số hạng **đã nhân trọng số** hay của hàm mất mát **thuần**. Dẫn xuất (3.5) cho thấy chỉ cách đọc thứ nhất mới nhất quán. Cài đặt trong nền tảng thực nghiệm được sử dụng ở luận văn này tính đúng dạng $\lambda(1{-}\lambda)$, và Chương 5 ghi nhận điều đó như một xác nhận âm tính — tức một chỗ mà mã và lý thuyết **khớp nhau**, đối lập với các sai lệch được liệt kê ở §5.2.

*Thứ ba, $\bar y_g$ vẫn đi vào qua số hạng (II) ở cả hai thuật toán.* Do đó (3.3) và (3.6) **không** khác nhau ở việc có dùng nhãn mềm hay không.

### 3.3.5. Điều gì thực sự phân biệt hai thuật toán

So sánh trực tiếp (3.3) và (3.6) cho thấy chúng khác nhau ở **hai chỗ đồng thời**:

| | Điểm đánh giá $\ell$ | Số hạng gradient (III) |
|---|---|---|
| **NaiveMix** (3.3) | $(1{-}\lambda)\mathbf{x}_i + \lambda\bar{\mathbf{x}}_g$ | không có |
| **FedMix** (3.6) | $(1{-}\lambda)\mathbf{x}_i$ | có |

Đây là một quan sát có hệ quả trực tiếp. Chênh lệch hiệu năng giữa hai thuật toán **không** quy được hoàn toàn cho số hạng Taylor, vì việc rút $\bar{\mathbf{x}}_g$ khỏi lượt truyền xuôi cũng đồng thời thay đổi chế độ chính quy hoá và mức nhiễu của đầu vào.

Lưới đầy đủ của hai trục này có bốn ô:

| | không có (III) | có (III) |
|---|---|---|
| **Đánh giá tại $(1{-}\lambda)\mathbf{x}_i + \lambda\bar{\mathbf{x}}_g$** | **A** = NaiveMix | D |
| **Đánh giá tại $(1{-}\lambda)\mathbf{x}_i$** | **C** | **B** = FedMix |

Trong đó:

$$\mathcal{L}_{\text{C}} = (1{-}\lambda)\,\ell\big(f((1{-}\lambda)\mathbf{x}_i), y_i\big) + \lambda\,\ell\big(f((1{-}\lambda)\mathbf{x}_i), \bar y_g\big) \tag{3.7}$$

Hiệu $\mathcal{L}_{\text{B}} - \mathcal{L}_{\text{C}}$ cô lập **chính xác** số hạng (III), với điểm đánh giá giữ cố định. Đây là đại lượng mà đóng góp C1 đo, và biến thể (3.7) là phần chưa được công bố trong phạm vi khảo sát ở §2.6.

Ô D — giữ phép trộn và thêm số hạng gradient — cho $\bar{\mathbf{x}}_g$ đi vào **hai lần**, nên nó không phải một thuật toán có nguyên tắc mà là một nhánh chẩn đoán. Luận văn không chạy ô này và ghi nhận trong phần hạn chế.

### 3.3.6. Về số hạng bậc hai

Câu hỏi tự nhiên là liệu việc giữ thêm số hạng bậc hai trong khai triển (3.4) có cải thiện xấp xỉ hay không. Một phép đo trong [44] cho thấy số hạng hiệu chỉnh bậc hai trong không gian đầu vào có biên độ khoảng $10^{-4}$ so với số hạng bậc nhất **tại thời điểm khởi tạo**.

Phát biểu chính xác của kết quả này — theo đúng cách nguồn tự giới hạn — là: ở trọng số trộn vận hành $\lambda = 0{,}05$, số hạng bậc hai **không phải một đòn bẩy hợp lý**. Nguồn nêu rõ phép đo thực hiện tại khởi tạo và **không** tuyên bố biên độ đó giữ nguyên trong suốt quá trình huấn luyện. Luận văn kế thừa giới hạn phát biểu này và không khảo sát nhánh bậc hai.

---

## 3.4. Thiên lệch học cục bộ: đặc trưng và bộ phân lớp

### 3.4.1. Ba biểu hiện

Công trình [18] phân tách hệ quả của cập nhật cục bộ trên dữ liệu không đồng nhất thành ba hiện tượng, gọi chung là **thiên lệch học cục bộ**:

1. **Bộ phân lớp cục bộ bị thiên lệch.** Sau $K$ bước trên dữ liệu mà một số lớp chiếm đa số, $\omega_i$ có xu hướng gán mọi mẫu vào các lớp xuất hiện tại chỗ, kể cả mẫu thuộc lớp chưa từng thấy.
2. **Đặc trưng cục bộ lệch khỏi đặc trưng toàn cục.** Với cùng một đầu vào $\mathbf{x}$, $\phi_i(\mathbf{x})$ khác đáng kể so với $\phi_g(\mathbf{x})$.
3. **Đặc trưng cục bộ của các lớp khác nhau quá gần nhau.** $\phi_i$ mất khả năng phân tách các mẫu thuộc phân phối mà client $i$ không quan sát.

Hiện tượng (2) đáng chú ý về mặt khái niệm vì nó cho thấy — như §3.2.1 đã lưu ý — rằng **ngay cả dưới label skew thuần**, nơi $P_i(\mathbf{x}\mid y)$ trùng nhau theo định nghĩa phân hoạch, phân phối **đặc trưng** có điều kiện lớp vẫn khác nhau giữa các client, bởi vì chính $\phi_i$ đã trôi. Nói cách khác, label skew sinh ra lệch trong không gian đặc trưng **thông qua bộ trích xuất**, không phải thông qua dữ liệu.

### 3.4.2. Thiên lệch ở bộ phân lớp là thiên lệch định hướng

Một trực giác phổ biến cho rằng thiên lệch của bộ phân lớp thể hiện ở **độ lớn** của các vector trọng số: lớp chiếm đa số cục bộ có chuẩn lớn hơn, nên logit của nó lớn hơn.

Phép đo trong [44] mâu thuẫn với trực giác đó. Trên một backbone không dùng chuẩn hoá theo lô, tỉ lệ giữa chuẩn $\ell_2$ lớn nhất và nhỏ nhất trong các vector trọng số theo lớp của tầng cuối chỉ vào khoảng $1{,}10$–$1{,}17$ — gần như đồng đều. Trong khi đó, việc hiệu chuẩn lại tầng cuối làm thay đổi độ chính xác vài điểm phần trăm và nâng recall của lớp bị phục vụ kém nhất lên rất mạnh.

Một chênh lệch chuẩn ở mức dưới $20\%$ không thể tạo ra biến thiên recall lớn như vậy nếu cơ chế là co giãn độ lớn. Kết luận là **thiên lệch nằm ở hướng của ranh giới quyết định**, không ở độ lớn của các vector trọng số; hiệu chuẩn **xoay** ranh giới chứ không co giãn nó.

Kết luận này quan trọng với luận văn vì hai lý do. Thứ nhất, nó **xác nhận tiền đề** của đề tài đã đăng ký: mục tiêu cụ thể được phát biểu là tăng cường đặc trưng tại *các vùng ranh giới quyết định* để giảm sai lệch nhãn — và phép đo trên cho thấy ranh giới quyết định đúng là nơi thiên lệch cư trú. Thứ hai, nó đặt ra câu hỏi mà Chương 5 trả lời: đòn bẩy trộn trung bình có **xoay** được ranh giới đó không, hay chỉ tác động lên những chiều ít mang thông tin?

Phạm vi của kết luận cần được nêu kèm: nó được đo trên **một** họ kiến trúc không dùng chuẩn hoá theo lô, và nguồn tự cảnh báo rằng một backbone có chuẩn hoá có thể định hình lại phát hiện này. Luận văn giữ nguyên cảnh báo đó và xem việc kiểm tra trên kiến trúc có chuẩn hoá là một kiểm soát ngoại vi (§5.6).

---

## 3.5. Bộ phân lớp sinh so với phân biệt: trần LDA

Mục này cung cấp nền lý thuyết để định vị họ phương pháp ở §2.3.4 và để làm rõ **vì sao đối tượng nghiên cứu của luận văn nằm ngoài phạm vi của trần đó**.

### 3.5.1. Hai kết quả cổ điển

Xét bài toán phân lớp trong đó đặc trưng của mỗi lớp tuân theo phân phối Gaussian với **hiệp phương sai chung**: $\mathbf{z} \mid y{=}c \sim \mathcal{N}(\boldsymbol\mu_c, \boldsymbol\Sigma)$. Trong điều kiện này, bộ phân biệt tuyến tính (LDA) là bộ phân lớp sinh tối ưu, và ranh giới Bayes là tuyến tính.

Efron [45] chứng minh rằng hồi quy logistic — một bộ phân lớp **phân biệt** — có hiệu suất tiệm cận tương đối không vượt quá LDA dưới đúng các giả thiết trên. Ng và Jordan [46] bổ sung rằng bộ phân lớp phân biệt chỉ thắng khi có **đủ dữ liệu thật** *và* mô hình sinh bị đặc tả sai.

Hai điều kiện của phát biểu cần được giữ nguyên khi trích dẫn: kết quả là **tiệm cận** và **trong kỳ vọng**, dưới giả thiết **Gaussian đúng với hiệp phương sai chung**. Nó không phải một chặn cứng ở mọi cỡ mẫu.

### 3.5.2. Hệ quả cho hiệu chuẩn bộ phân lớp trong FL

Các phương pháp ở §2.3.4 ước lượng $(\boldsymbol\mu_c, \boldsymbol\Sigma_c)$ từ thống kê được truyền thông, rồi huấn luyện lại tầng cuối trên **mẫu ảo lấy từ chính mô hình Gaussian đó**. Theo §3.5.1, một head phân biệt huấn luyện trên dữ liệu sinh từ một Gaussian không thể vượt bộ phân biệt sinh tương ứng trên **tác vụ ảo** ấy. Đo lường trong [44] xác nhận thứ hạng này: head LDA dạng đóng cho mức cải thiện cao nhất, các phương án phân biệt tiệm cận nhưng không vượt.

Cần nêu rõ hai giới hạn. Thứ nhất, trần này áp dụng cho **tác vụ ảo**, không cho phân phối thật; nó nói rằng không thể khai thác thêm gì từ một Gaussian đã cho, chứ không nói Gaussian đó mô tả đúng dữ liệu. Thứ hai, khi hiệp phương sai của các lớp **khác nhau**, ranh giới Bayes là bậc hai và kết quả Efron không còn áp dụng.

### 3.5.3. Vì sao đối tượng của luận văn nằm ngoài trần này

Điều này giải thích một lựa chọn phạm vi của luận văn. Cơ chế mà đề tài nghiên cứu — mẫu trung bình đại diện kết hợp khai triển Taylor — **không lấy mẫu từ bất kỳ mô hình Gaussian nào**. Nó thao tác trên:

- **không gian đầu vào**, không phải không gian đặc trưng;
- **dữ liệu thật đã được lấy trung bình**, không phải mẫu tổng hợp;
- **thống kê bậc nhất của dữ liệu thô**, không phải moment của đặc trưng.

Trần LDA vì vậy **không ràng buộc** cơ chế này, và các phương pháp ở §2.3.4 không phải đối thủ trực tiếp mà là một họ song song giải quyết cùng triệu chứng bằng cơ chế khác. Luận văn trình bày §3.5 không để so sánh hiệu năng, mà để xác định rõ **ranh giới áp dụng** của một kết quả lý thuyết thường bị viện dẫn quá phạm vi trong văn liệu FL.

---

## 3.6. Kết quả nền từ công trình đã công bố của tác giả

> ⚠️ **IR#9 — bắt buộc trước khi nộp.** Mục này dựa trên công trình đã được chấp nhận đăng của chính học viên, đồng tác giả là cán bộ hướng dẫn. Phải bổ sung: (a) trích dẫn đầy đủ gồm tên hội nghị, năm, DOI hoặc chỉ mục; (b) tuyên bố tái sử dụng ở đầu mục và trong Lời cam đoan; (c) văn bản xác nhận của đồng tác giả; (d) khai báo tỉ lệ trùng lắp dự kiến với đơn vị quản lý đào tạo **trước** khi quét.

Công trình [44] khảo sát có kiểm soát nhóm phương pháp hiệu chuẩn bộ phân lớp và nhóm tăng cường trung bình, trên một nền tảng thực nghiệm huấn luyện từ đầu, dưới **lệch phân phối nhãn**. Bốn kết quả của công trình đó tạo thành nền cho luận văn này.

**Thứ nhất, cơ chế tăng cường trung bình không mang lại cải thiện đo được trên nền tảng đó.** Với ba hạt giống ngẫu nhiên, mức chênh so với FedAvg là $-1{,}86 \pm 0{,}79$ điểm phần trăm; cận trên $95\%$ một phía là $-0{,}53$ điểm, tức loại trừ được khả năng có cải thiện. Đây là kết quả về **chính cơ chế** mà luận văn nghiên cứu, và nó xác lập nửa label skew của câu trả lời.

Bốn biến thể mở rộng khác được công trình đó khảo sát — ghép cặp có ý thức về lớp, hiệu chỉnh bậc hai trong không gian đầu vào, và một phép biến đổi trong không gian đặc trưng — được nguồn gắn nhãn tường minh là **thăm dò**, và hai trong số đó chỉ chạy một hạt giống và chưa tinh chỉnh. Luận văn giữ nguyên nhãn này khi trích dẫn; mức bằng chứng của chúng thấp hơn hẳn kết quả thứ nhất.

**Thứ hai, mức cải thiện phụ thuộc ngân sách và đổi dấu.** Như §2.5 đã trình bày, cùng một phương pháp hiệu chuẩn cho $+0{,}29$, $-0{,}76$ và $+0{,}97$ điểm phần trăm tuỳ ngân sách mẫu ảo và độ nghiêm trọng skew. Đây là cơ sở thực nghiệm cho nguyên tắc "mức cải thiện là một đường đặc tuyến vận hành" mà Chương 4 áp dụng.

**Thứ ba, thiên lệch của bộ phân lớp là định hướng** — kết quả đã trình bày ở §3.4.2.

**Thứ tư, công trình đó tự khai ba giới hạn ngoại vi:** phạm vi bằng chứng gồm một họ kiến trúc, một phân phối ảnh $32\times32$, và **một loại lệch phân phối duy nhất là label skew**; đồng thời nguồn nêu rõ rằng backbone không chuẩn hoá theo lô là giả thiết chịu lực cho phần phân tích Gaussian.

Ba giới hạn tự khai này định nghĩa trực tiếp phạm vi đóng góp của luận văn: chuyển sang một **nền tảng thực nghiệm thứ hai**, mở sang chế độ **feature skew**, và kiểm tra trên kiến trúc **có chuẩn hoá**. Theo nguyên tắc so sánh trong cùng nền tảng (§2.5), mọi đối chiếu giữa Chương 3 và Chương 5 được phát biểu ở **mức cơ chế**, không ở mức con số tuyệt đối.

---

## Tài liệu tham khảo bổ sung cho Chương 3

*(tiếp nối danh mục của `02_chuong2.md`)*

[45] B. Efron, "The Efficiency of Logistic Regression Compared to Normal Discriminant Analysis," *Journal of the American Statistical Association*, vol. 70, no. 352, pp. 892–898, 1975.
[46] A. Y. Ng, M. I. Jordan, "On Discriminative vs. Generative Classifiers: A Comparison of Logistic Regression and Naive Bayes," *NeurIPS*, 2001.
---

# YÊU CẦU SỬA — 22/09/2026 · lượt rà soát nội dung Chương 3

> **Cách đọc.** Khối này mô tả việc cần làm, không viết thay. Phần thân chương phía trên giữ nguyên trạng theo quy ước chỉ-append (`00_outline.md` §8).
>
> **Căn cứ rà soát:** `00_outline.md` (IRON RULES §2, ranh giới Ch.2↔Ch.3 §4, quy ước viết §7) · bản hiện hành của Ch.2 dưới mốc `PHIÊN BẢN CHỈNH SỬA — 22/09/2026 (lượt 2)` · `04_chuong4.md`, `05_chuong5.md`, `06_chuong6.md` · mã nguồn `fedbr/`.
>
> **Điểm xuất phát:** Chương 3 mang dấu 16/09, tức viết **trước** hai lượt sửa lớn của Ch.2 ngày 21/09 và 22/09. Phần lớn lỗi dưới đây là hệ quả cơ học của việc đó, không phải lỗi lập luận. Phần dẫn xuất của chương **đã được kiểm và đứng vững** — xem mục C.

---

## A. Chặn nộp — phải sửa trước mọi việc khác

### A1. Toàn bộ số trích dẫn thuộc danh mục 44 mục đã bị huỷ

Ch.2 đã đánh số lại liên tục **1–16** ngày 22/09. Chương 3 vẫn dùng số của bản cũ, nên mọi trích dẫn trong chương hiện trỏ sai nguồn:

| Trong Ch.3 | Đang trỏ tới (ý định) | Số đúng theo danh mục Ch.2 |
|---|---|---|
| [1] §3.1.2 | FedAvg | **[2]** — [1] nay là FedMix |
| [3] §3.2.2 | quy ước Dirichlet $\mathrm{Dir}(\alpha\cdot p)$ | **[4]** Hsu–Qi–Brown — xem A2 |
| [12] §3.3.1 | Mixup | **[9]** |
| [13] §3.3.3, §3.3.4 (×2) | FedMix / khung MAFL | **[1]** |
| [18] §3.4.1 | FedBR | **[11]** |
| [44] §3.3.6, §3.4.2, §3.5.2, §3.6 | công trình hội nghị của tác giả | **chưa có số** — cấp [17] và bổ sung vào danh mục |
| [45], [46] | Efron; Ng–Jordan | **[18], [19]** sau khi [17] được cấp |

Sửa kèm: khối *Tài liệu tham khảo bổ sung cho Chương 3* ở cuối chương phải đánh số tiếp nối 1–16, và phải **thêm mục cho công trình của tác giả** — hiện chưa có mục nào, dù chương trích bốn lần.

⚠️ Đối chiếu lại với bản Word trước khi sửa; bản Word là bản chính.

### A2. §3.2.2 trích sai nguồn, không chỉ sai số

Câu *"Luận văn dùng quy ước $\mathbf{q}_i \sim \mathrm{Dir}(\alpha \cdot \mathbf{p})$ theo [3]"* gán quy ước này cho NIID-Bench. Sai về nội dung: Ch.2 mục 2.1.3 đã phân định rõ hai quy ước, và dạng $\mathrm{Dir}(\alpha\cdot p)$ lấy mẫu **theo trục lớp, cho từng client** là quy ước **Hsu–Qi–Brown**. NIID-Bench dùng dạng chuyển vị $p_k \sim \mathrm{Dir}_N(\beta)$, lấy mẫu theo trục client cho từng lớp. Đổi nguồn, không chỉ đổi số.

### A3. Hai mục được viện dẫn không còn tồn tại

Ch.2 hiện chỉ có **2.1–2.4**. Chương 3 viện dẫn `§2.5` hai lần và `§2.6` một lần, và dùng số cũ cho hai mục khác:

| Trong Ch.3 | Nội dung định trỏ | Địa chỉ hiện hành |
|---|---|---|
| §2.1.2 (ở §3.2.2) | ký hiệu Dirichlet mơ hồ | **mục 2.1.3** |
| §2.3.4 (ở §3.5.2, §3.5.3, §3.6) | hiệu chuẩn tầng phân lớp, CCVR | **mục 2.2.2.4** |
| §2.6 (ở §3.3.5) | khoảng trống, cô lập số hạng Taylor | **mục 2.4.1** |
| §2.5 (ở §3.6, hai lần) | tính tái lập, quy tắc báo cáo | **không còn ở Ch.2** — xem A4 |

### A4. Hai câu ở §3.6 viện dẫn nội dung mà Ch.2 không còn trình bày

Đây là lỗi nặng hơn tra cứu sai địa chỉ, vì quyết định 22/09 đã **chuyển** hai nội dung này đi nơi khác:

- *"Như §2.5 đã trình bày, cùng một phương pháp hiệu chuẩn cho $+0{,}29$, $-0{,}76$ và $+0{,}97$…"* — ví dụ CCVR đảo dấu theo ngân sách đã được chuyển **vào chính Chương 3**. Ch.2 không còn dòng nào về nó. Câu này phải viết lại thành một đoạn **tự đủ nghĩa**: nêu tên CCVR, nêu ngân sách mẫu ảo $M_c$ và mức skew ứng với từng con số, kèm caveat IR#1. Vế $-0{,}76$ là vế bắt buộc phải có.
- *"Theo nguyên tắc so sánh trong cùng nền tảng (§2.5)…"* — ba quy tắc báo cáo nay thuộc **Ch.4 mục 4.5**. Chương 3 đứng trước Ch.4 nên không được viện dẫn chúng như điều đã lập. Phát biểu nguyên tắc tại chỗ bằng một mệnh đề ngắn.

### A5. Ký hiệu $\omega$ mang hai nghĩa trong cùng một mục

§3.1.1 dùng $\boldsymbol\omega$ làm **vector tham số toàn mô hình** — $f_i(\boldsymbol\omega)$, rồi $\boldsymbol\omega_t$ và $\boldsymbol\omega_i^K$ ở §3.1.2 — và cách đó hai đoạn lại dùng $\omega$ làm **bộ phân lớp** trong $f = \omega \circ \phi$. `00_outline.md` §7.1 dành $\omega$ cho bộ phân lớp.

Chương 3 là chương mà người đọc quay lại tra ký hiệu, nên đây là chỗ không được để lẫn. Đề xuất: giữ $\omega$ cho bộ phân lớp theo §7.1, đổi tham số mô hình sang $\theta$. Đã kiểm: Ch.4 các công thức (4.1)–(4.3) không bị ảnh hưởng. Ký hiệu $\tilde p_i$ ở bước 3 của §3.1.2 cũng chưa được định nghĩa.

### A6. IR#9 chưa được giải quyết

Khối trạng thái đầu chương đã tự đánh dấu. Nhắc lại để không rơi: tên hội nghị, năm, trạng thái accepted hay published, DOI hoặc chỉ mục; tuyên bố tái sử dụng ở **đầu §3.6** và trong Lời cam đoan; văn bản xác nhận của đồng tác giả; khai báo tỉ lệ trùng lắp **trước** khi quét. Cấm gọi chung chung *"công trình hội nghị"*.

---

## B. Nội dung — phải sửa trước khi chốt chương

### B1. Lập luận bỏ số hạng bậc hai ở §3.3.4 vượt quá mức đại số cho phép

Chương viết: *"Số hạng (IV) là $O(\lambda^2)$. Ở chế độ vận hành $\lambda \in [0{,}05;\,0{,}2]$ … nó nhỏ hơn (III) một bậc và được bỏ qua."*

Tỉ lệ hệ số giữa hai số hạng là $\lambda^2 / [\lambda(1{-}\lambda)] = \lambda/(1{-}\lambda)$:

| $\lambda$ | 0,05 | 0,1 | 0,2 |
|---|---|---|---|
| (IV)/(III) | 0,053 | 0,111 | **0,25** |

Ở $\lambda = 0{,}2$ — đầu trên của chính khoảng mà chương tuyên bố — số hạng (IV) bằng **một phần tư** số hạng (III), không nhỏ hơn một bậc. Phát biểu chỉ đúng quanh $\lambda \approx 0{,}05$–$0{,}1$.

Hai cách sửa, chọn một: (a) ghi thẳng tỉ lệ $\lambda/(1{-}\lambda)$ và hạn định phát biểu về phía $\lambda$ nhỏ, nêu rằng ở $\lambda = 0{,}2$ phép bỏ qua là một xấp xỉ thô hơn; (b) thu hẹp khoảng vận hành được tuyên bố. Phương án (a) tốt hơn, vì Ch.4 mục 4.4.1 quét tới $\lambda = 0{,}2$ và Ch.4 mục 4.2.3 đã lấy chính tỉ lệ hệ số này làm một yếu tố gây nhiễu cần loại trừ; hai chỗ phải nói cùng một điều.

Liên quan: §3.3.6 đóng nhánh bậc hai dựa trên một phép đo tại $\lambda = 0{,}05$ **và tại khởi tạo**. Chương đã giữ đúng caveat "tại khởi tạo"; cần giữ thêm caveat **"tại $\lambda = 0{,}05$"**, vì hiện phát biểu được đọc như thể áp cho cả khoảng.

### B2. Vi phạm §7.5 "gọi tên phương pháp cụ thể" — sáu chỗ

Người đọc luận văn không có tài liệu nào khác. Sáu cụm sau phải thay bằng tên thật, kèm trích dẫn ở lần xuất hiện đầu:

| Vị trí | Đang viết | Thay bằng |
|---|---|---|
| §3.3.4 | *"nền tảng thực nghiệm được sử dụng ở luận văn này"* | FedBR |
| §3.5.2 | *"Các phương pháp ở §2.3.4"* | CCVR và nhóm hiệu chuẩn tầng phân lớp |
| §3.5.3 | *"các phương pháp ở §2.3.4 không phải đối thủ trực tiếp"* | như trên |
| §3.6 | *"một phương pháp hiệu chuẩn"* | CCVR |
| §3.6 | *"một nền tảng thực nghiệm huấn luyện từ đầu"* | nêu tên nền tảng |
| §3.4.1, §3.6 | *"Công trình [44]"* | tên công trình, sau khi A6 xong |

### B3. §3.6 đếm bốn, liệt kê ba

*"**Bốn** biến thể mở rộng khác … — ghép cặp có ý thức về lớp, hiệu chỉnh bậc hai trong không gian đầu vào, và một phép biến đổi trong không gian đặc trưng"* — ba mục cho một con số bốn. Theo `00_outline.md` §3.3, bốn biến thể là: C1 ghép cặp có ý thức về lớp; **C1+C2**; T2 hiệu chỉnh bậc hai; và phép biến đổi trong không gian đặc trưng. Bổ sung mục còn thiếu hoặc sửa con số.

### B4. Con số $-1{,}86 \pm 0{,}79$ chưa ghi rõ $\pm$ là gì, và thiếu cấu hình

Đã kiểm ngược từ `00_outline.md` §3.3: ba hạt giống $-2{,}19 / -0{,}95 / -2{,}43$ cho trung bình $-1{,}857$ và **độ lệch chuẩn mẫu** $0{,}794$; cận trên 95% một phía suy ra đúng $-0{,}52$. Vậy $\pm 0{,}79$ là **sd**, không phải nửa rộng khoảng tin cậy.

`00_outline.md` §7.4 quy định thanh sai số là CI 95% và phải ghi rõ trong caption. Hoặc đổi sang CI, hoặc ghi thẳng *"trung bình ± độ lệch chuẩn mẫu trên ba hạt giống"*. Đồng thời IR#8 đòi truy vết được: bổ sung cấu hình phân hoạch (hai lớp mỗi client) và backbone của con số này.

Ghi chú đối chiếu: Ch.4 mục 4.5.3 dùng $s \approx 1{,}2$ điểm phần trăm để định cỡ thiết kế, trong khi Ch.3 báo $0{,}79$. Hai con số đến từ hai bảng khác nhau của cùng một công trình, nhưng người đọc đặt cạnh nhau sẽ thắc mắc; thêm một mệnh đề phân định ở một trong hai chỗ.

### B5. Ranh giới Ch.2↔Ch.3 chưa được thi hành đủ

Bảng phân vai chốt 22/09 giao cho Ch.3 **định nghĩa chính quy phân phối Dirichlet**. §3.2.2 hiện chỉ phát biểu một quy ước ký hiệu, không có định nghĩa: không nêu đơn hình xác suất, không nêu hàm mật độ, không nêu vai trò của vector nồng độ. Phần khái niệm nằm ở Ch.2 mục 2.1.3; phần hình thức thuộc về đây và đang khuyết.

Ràng buộc (a) của cùng bảng phân vai — *"Ch.3 phát biểu lại đầy đủ chứ không viết 'như đã trình bày ở Chương 2'"* — bị vi phạm hai lần: *"Như §2.1.2 đã cảnh báo"* ở §3.2.2, và *"Như §2.5 đã trình bày"* ở §3.6 (xem A4).

### B6. Tuyên bố mới lạ ở §3.3.5 chưa có hạn định trong câu

*"…biến thể (3.7) là phần chưa được công bố trong phạm vi khảo sát ở §2.6."* IR#3 bản sửa 22/09 đòi hạn định nằm **trong chính câu phát biểu** và ưu tiên phương án (a), tức thu về một đối tượng kiểm chứng được. Ch.2 mục 2.4.1 đã chốt sẵn cách nói: *"Cấu hình như vậy không xuất hiện trong bài báo FedMix, kể cả ở phần phụ lục."* Dùng lại nguyên văn đó.

### B7. Hai tham chiếu tới Chương 5 trỏ sai mục

- §3.2.3: *"đường đặc tuyến ở §5.4"* → đường cong theo độ nghiêm trọng nằm ở **§5.5 Trục độ nghiêm trọng**; §5.4 là mục về hai giá trị của trọng số trộn.
- §3.4.2: *"một kiểm soát ngoại vi (§5.6)"* → Ch.5 không có mục mang tên đó. Kiểm soát kiến trúc là thí nghiệm **E5, đánh dấu *(tuỳ chọn)*** trong §5.1.3, và chỉ xuất hiện như một gạch đầu dòng có điều kiện trong §5.6. Ch.6 mục 6.3.1 nói thẳng rằng nếu nó không chạy thì giả thiết độc lập kiến trúc **chưa được kiểm tra**. Chương 3 không được hứa chắc một kiểm soát có thể không diễn ra; sửa thành cách nói có điều kiện.

### B8. §3.3.4 và Ch.5 §5.2.2 nói gần trọn vẹn cùng một lập luận

Cả hai chỗ đều dẫn lại: hệ số đúng là $\lambda(1{-}\lambda)$; thừa số $(1{-}\lambda)$ kế thừa từ số hạng thứ nhất; công thức in trong bài báo gốc mơ hồ ở chỗ $\partial\ell/\partial\mathbf{x}$ là đạo hàm của số hạng đã nhân trọng số hay của hàm mất mát thuần. `00_outline.md` §7.6 quy định mỗi ý viết một lần, ở đúng một chương.

Đề xuất phân vai: **Ch.3 giữ dẫn xuất và cách đọc công thức đã công bố**, vì đó là việc của chương lý thuyết; **Ch.5 §5.2.2 chỉ giữ quan sát về mã nguồn** — mã tính đúng dạng $\lambda(1{-}\lambda)$ — cùng một câu trỏ về (3.5). Khi đó câu cuối của §3.3.4, *"Chương 5 ghi nhận điều đó như một xác nhận âm tính"*, trở thành chỉ dẫn đọc thêm hợp lệ thay vì mở đầu cho một đoạn trùng lặp.

### B9. Ba nội dung dàn bài giao cho chương này còn khuyết

| Giao ở | Nội dung | Hiện trạng |
|---|---|---|
| §4, mục 3.3.3 | ánh xạ từng số hạng (I)/(II)/(III) sang `loss1`/`loss2`/`loss3` của cài đặt | không có trong §3.3 |
| §4, mục 3.5 | *"Trần đo ở $n/d \approx 3{,}9$ — ghi rõ chế độ, không ngoại suy"* | không có trong §3.5.2 |
| §4, mục 3.2 và IR#7 | **≈2,08 góc hiệu dụng mỗi client** | §3.2.3 chỉ viết *"một đến hai góc trội"*, mơ hồ hơn con số đã đăng ký |

Mục thứ hai đáng làm nhất: §3.5.2 hiện phát biểu trần LDA mà không nêu chế độ $n/d$ đã đo, trong khi chính §3.5.1 đã cẩn thận nhấn rằng kết quả là tiệm cận. Thiếu chế độ thì phần cẩn thận đó mất nửa hiệu lực.

---

## C. Đã kiểm và **đúng** — không sửa, không chữa theo dàn bài cũ

Ghi lại để lượt sau không lật ngược nhầm.

**C1. Dẫn xuất (3.4) sang (3.5) đúng về đại số.** Nhiễu là $\lambda\bar{\mathbf{x}}_g$; áp (3.4) vào số hạng thứ nhất của (3.3) cho $(1{-}\lambda)\ell + \lambda(1{-}\lambda)\nabla\ell_{y_i}\!\cdot\!\bar{\mathbf{x}}_g$, vào số hạng thứ hai cho $\lambda\ell + \lambda^2\nabla\ell_{\bar y_g}\!\cdot\!\bar{\mathbf{x}}_g$. Khớp đúng bốn số hạng (I)–(IV).

**C2. Tuyên bố ở §3.3.4 rằng cài đặt tính đúng dạng $\lambda(1{-}\lambda)$ là ĐÚNG — đã đối chiếu mã nguồn.** Trong `fedbr/algorithms.py`, lớp `FedMix`: `loss1` **đã mang thừa số** $(1{-}\lambda)$; `grad = autograd.grad(loss1, all_x)` nên `grad` bằng $(1{-}\lambda)\nabla_{\mathbf{x}}\ell$; `loss3` nhân thêm $\lambda$, cho hệ số hiệu dụng $\lambda(1{-}\lambda)$. Điểm khai triển cũng đúng: `all_x` đã được gán lại thành $(1{-}\lambda)\mathbf{x}_i$ trước khi lấy đạo hàm, khớp với chỉ số $\mathbf{x}=(1{-}\lambda)\mathbf{x}_i$ trong (3.4).

⚠️ **Ghi chú cho `00_outline.md` §3.1:** bảng tài sản ở đó ghi tắt `loss3 = Σ(λ·grad·x̄_g)/n`. Dòng ghi tắt này đọc như thể hệ số là $\lambda$ và **dễ dẫn tới kết luận ngược**, vì nó không nói `grad` là đạo hàm của `loss1` đã nhân trọng số. Nên chú thích lại ở dàn bài.

⚠️ **Cảnh báo ở khối trạng thái đầu chương có thể đóng một nửa:** dẫn xuất §3.3.4 **khớp mã nguồn**. Việc đối chiếu ký hiệu với Eq. (5) của bài báo FedMix vẫn là một phép kiểm riêng và còn mở, nhưng chính §3.3.4 đã lập luận rằng công thức in trong bài là dạng viết gọn mơ hồ, nên kết quả đối chiếu đó không lật được kết luận.

**C3. (3.3) khớp cài đặt `NaiveMix`.** Mã trộn đầu vào thành $(1{-}\lambda)\mathbf{x}_i + \lambda\bar{\mathbf{x}}_g$ rồi dựng vector nhãn $\lambda\bar y_g$ cộng $(1{-}\lambda)$ tại vị trí $y_i$, đúng bằng $(1{-}\lambda)\ell(\cdot,y_i) + \lambda\ell(\cdot,\bar y_g)$.

**C4. Các giá trị $d$ ở §3.1.1 đúng.** Đối chiếu `fedbr/networks.py`: VGG11 và ResNet18 cho 512, CCT 256, ResNet20-GN 64. Khớp IR#7.

**C5. Quy ước $\alpha_{\text{rot}}$ của §3.2.3 đúng — dàn bài mới là bản lỗi thời.** Mã nguồn dựng `p = ones(10)/10` rồi `Dirichlet(1.0 * p)`, tức **nồng độ tổng $1{,}0$, nồng độ mỗi thành phần $0{,}1$**, đúng như §3.2.3 viết; Ch.4 mục 4.3.1 dùng cùng quy ước với $\alpha_{\text{rot}} = 1{,}0$.

⚠️ `00_outline.md` §7.1 định nghĩa $\alpha_{\text{rot}}$ là *"quy ước tuyệt đối, mặc định ≈0,1"*, và §5.1 đăng ký lưới $\{0{,}1;\ 0{,}5;\ 1;\ 5;\ \infty\}$ — cả hai viết theo **nồng độ mỗi thành phần**, lệch quy ước với Ch.3 và Ch.4 đúng một hệ số bằng 10. **Không sửa Ch.3 theo dàn bài.** Việc cần làm là sửa dàn bài, và cảnh báo người điền bảng P1–P3 ở Ch.5 mục 5.1.1, hiện còn `[điền]`, rằng lưới trong dàn bài không dùng trực tiếp được. Dưới quy ước của Ch.3, quét về phía **nhẹ hơn** nghĩa là $\alpha_{\text{rot}}$ **tăng**.

Cũng vì lệch quy ước này, hai câu ở §3.2.2 và §3.2.3 tuy đúng nhưng đặt cạnh nhau dễ gây ngờ: $\alpha = 0{,}1$ cho nhãn ứng với $0{,}01$ mỗi thành phần, còn $\alpha_{\text{rot}} = 1{,}0$ cho góc ứng với $0{,}1$ mỗi thành phần. Cả hai đều theo quy ước nồng độ tổng và đều nhất quán với Ch.5 mục 5.1.1, nên giữ; cân nhắc thêm một câu nói rõ hai tham số dùng **cùng** một quy ước.

**C6. Lưới A/B/C/D ở §3.3.5 nhất quán với Ch.4.** Ch.4 mục 4.1.1 và 4.2 dùng A/B/C/D đúng theo nghĩa **cấu hình thuật toán** như §3.3.5 định nghĩa.

⚠️ Rủi ro cần biết: `00_outline.md` §4 mục 4.3 và bảng đăng ký thí nghiệm §5.1 dùng **cùng bốn chữ cái A/B/C/D cho bốn ô lệch phân phối** — A là IID, B là feature skew thuần, và tiếp theo — nên các dòng E1/E2 ở đó viết *"4 ô"*, *"ô B+D"* theo nghĩa ấy. Nghĩa này đã bị Ch.4 mục 4.3.1 bác bỏ tường minh, vì luận văn **không** dùng thiết kế $2\times2$, và Ch.5 mục 5.1.3 đã chuyển sang ký hiệu **P0–P4** cho các cấu hình lệch. Giữ nguyên hiện trạng; chỉ cần không để chữ cái A–D quay lại mang nghĩa lệch phân phối ở bất kỳ chương nào.

**C7. Không dùng nhánh hồi quy.** Chương 3 không nhắc tới hồi quy ở bất kỳ đâu, đúng ràng buộc `[GÁC]` 22/09. *(Ngược lại, Ch.4 mục 4.1.1 vẫn mô tả bốn trục gồm trục tác vụ, Ch.4 mục 4.6 vẫn còn nguyên, và Ch.6 mục 6.3.1 cùng 6.4.2 vẫn nhắc hồi quy. Việc của hai chương đó, ghi lại ở đây để không rơi.)*

**C8. Thuật ngữ bên tham gia.** Chương dùng "client" xuyên suốt, không có "thiết bị", "bên", "máy khách"; đúng quy ước D1 chốt 22/09.

---

## D. Lối viết — áp §7.7, đo bằng máy trên thân chương

| Phép đếm | Kết quả | Hạn mức | |
|---|---|---|---|
| AI#1 — cấu trúc tương phản | **5** | ≤ 3 mỗi chương | ⚠️ vượt |
| AI#4 — câu rào | **≈6** | đúng 1 mỗi chương | ⚠️ vượt nặng |
| AI#6 — dấu `—` chêm | **32** (≈6,4 mỗi trang) | ≤ 1 mỗi trang | ⚠️ vượt nặng |
| AI#8 — cụm sáo cấm dùng | **3** | phải bằng 0 | ⚠️ vi phạm |

**D1 — AI#8, ba chỗ phải bỏ.** *"Cần nhấn mạnh rằng"* ở §3.2.1; *"đáng chú ý ở chỗ"* ở §3.2.3, tính chất thứ hai; *"đáng chú ý về mặt khái niệm"* ở §3.4.1. Cả ba đều bỏ được mà câu không mất nghĩa.

**D2 — AI#4, đây là vi phạm đáng kể nhất về lối viết.** Sáu câu tự giới hạn phạm vi rải khắp chương: §3.2.3 *"Luận văn ghi nhận đây là một giới hạn của thiết kế"*; §3.3.5 *"Luận văn không chạy ô này và ghi nhận trong phần hạn chế"*; §3.3.6 *"Luận văn kế thừa giới hạn phát biểu này"*; §3.4.2 *"Luận văn giữ nguyên cảnh báo đó"*; §3.5.2 *"Cần nêu rõ hai giới hạn"*; §3.6 *"Luận văn giữ nguyên nhãn này"*. Giữ **một** câu ở chỗ cần nhất — đề xuất giữ ở §3.4.2, vì cảnh báo về backbone chuẩn hoá là giới hạn chịu lực nhất của chương. Năm câu còn lại dồn về Ch.6 mục 6.3, nơi Ch.6 **đã có sẵn** chỗ cho từng ý: 6.3.1 cho ô D, 6.3.2 cho phép xoay, 6.3.1 cho backbone.

**D3 — AI#6.** 32 dấu gạch ngang chêm là dấu hiệu dễ nhận nhất đối với người đọc quen. Cắt xuống khoảng 5–6 cho toàn chương; phần lớn thay được bằng dấu phẩy hoặc ngoặc đơn.

**D4 — AI#1.** Năm chỗ: *"chứ không đối xứng hai phía"* ở §3.2.3; *"không phải một thuật toán có nguyên tắc mà là một nhánh chẩn đoán"* ở §3.3.5; *"chứ không co giãn nó"* ở §3.4.2; *"chứ không nói Gaussian đó mô tả đúng dữ liệu"* ở §3.5.2; *"không phải đối thủ trực tiếp mà là một họ song song"* ở §3.5.3. Hai chỗ đáng giữ hạn ngạch là §3.4.2 và §3.5.3, vì cả hai tồn tại để sửa một cách hiểu sai. Ba chỗ còn lại viết thẳng.

**D5 — AI#3, nhịp ba dày.** *"Ba tính chất"* ở §3.2.3, *"Ba hệ quả cần ghi nhận"* ở §3.3.4, *"Ba biểu hiện"* ở §3.4.1, *"Hai kết quả cổ điển"* và *"hai giới hạn"* ở §3.5, *"Bốn kết quả"* ở §3.6. Số lượng đúng với nội dung nên không phải bịa cho tròn ba; nhưng khuôn *"Ba X sau đây…"* mở đầu mục lặp lại năm lần trong một chương là chỗ cần đổi cách mở.

**D6 — AI#2.** Gần như mọi tiểu mục đều đáp xuống bằng một câu chốt có nhịp đối. Chọn ba tiểu mục bất kỳ cho kết nhạt, bằng một con số hoặc một chi tiết kỹ thuật.

**D7 — AI#7, ba thuật ngữ tự đặt chưa định nghĩa tại chỗ.** *"xác nhận âm tính"* ở §3.3.4; *"nhánh chẩn đoán"* ở §3.3.5; *"đường đặc tuyến vận hành"* ở §3.6. Cụm thứ ba được Ch.2 mục 2.4.4 định nghĩa dưới dạng ngắn hơn là *"đường đặc tuyến"*; thống nhất một dạng.

**D8 — `\boldsymbol` dùng 8 lần.** Quyết định 21/09 đã gỡ `\boldsymbol` khỏi Ch.2 vì bộ render in nguyên chuỗi lệnh. Chương 3 còn $\boldsymbol\omega$, $\boldsymbol\mu_c$, $\boldsymbol\Sigma$. Đưa về tập lệnh LaTeX lõi cho đồng bộ.

**D9 — §7.4, hai bảng chưa có số và tên.** Hai bảng ở §3.3.5, bảng so sánh hai thuật toán và bảng lưới bốn ô, phải thành **Bảng 3.1** và **Bảng 3.2**; caption đặt **trên** bảng, tự đủ nghĩa, giải thích mọi ký hiệu, kể cả $\bar{\mathbf{x}}_g$, $\lambda$ và ý nghĩa của bốn chữ cái. Thân bài gọi bằng số bảng. Bảng trong khối trạng thái đầu file được miễn.

---

## E. Độ dài — chương đang ngắn khoảng một nửa

Thân Chương 3 hiện **≈3.950 từ**. Lấy bản hiện hành của Ch.2 làm thước — ≈8.256 từ cho 9–10 trang ở format đã chốt — Chương 3 rơi vào khoảng **4,5–5 trang**, trong khi `00_outline.md` §4 giao **9–10 trang**.

Đây là chương trọng tâm lý thuyết và là chương người đọc quay lại tra ký hiệu, nên thiếu hụt này không nên bù bằng cách viết phồng. Ba chỗ ở mục B9 cộng với định nghĩa Dirichlet ở B5 là phần nội dung **đã được giao mà còn khuyết**, và riêng chúng đã lấp được phần lớn khoảng cách. Ngoài ra §3.1 hiện rất gọn so với vai trò *"bản phát biểu chính thức mà Ch.4–Ch.6 tham chiếu"* mà bảng phân vai giao cho nó.

---

## F. Thứ tự thi hành đề xuất

1. **A1–A4** — cơ học, làm một lượt, không cần quyết định gì. Sửa vào bản Word trước.
2. **A5** — đổi ký hiệu tham số mô hình; làm sớm vì mọi công thức của §3.1 phụ thuộc.
3. **B5, B9** — bổ sung nội dung còn khuyết; đây cũng là phần giải quyết mục E.
4. **B1, B3, B4, B6** — sửa phát biểu; mỗi mục một chỗ, độc lập nhau.
5. **B2, B7, B8** — cần đọc kèm Ch.4 và Ch.5, nên làm sau khi bốn bước trên xong.
6. **D** — lượt rà lối viết cuối cùng, sau khi nội dung đã chốt. Chạy lại ba lệnh `rg` ở `00_outline.md` §7.7 và ghi số đếm vào khối trạng thái đầu file.
7. **A6** — song song, không chặn việc viết, nhưng chặn nộp.

**Hai việc thuộc file khác, phát sinh từ lượt rà này:**

- `00_outline.md` §3.1: chú thích lại dòng `loss3 = Σ(λ·grad·x̄_g)/n` — xem C2. Dòng ghi tắt hiện tại dẫn tới kết luận ngược.
- `00_outline.md` §7.1 và §5.1: quy ước $\alpha_{\text{rot}}$ và lưới quét đang lệch một hệ số bằng 10 so với mã nguồn, Ch.3 và Ch.4 — xem C5. Phải sửa **trước** khi ai đó điền bảng P1–P3 ở Ch.5 mục 5.1.1.

---


---

# PHIÊN BẢN CHỈNH SỬA — 23/09/2026

> **CÁCH ĐỌC.** Mọi phần phía trên giữ nguyên trạng để tra lịch sử. Phần dưới đây là **bản hiện hành** của Chương 3; khi chép vào Word, chỉ dùng phần này.
>
> **Việc đã làm:** A1–A6 · B1 theo phương án (a) · B2–B7, B9 · D1–D9 · E (bổ sung nội dung còn khuyết).
>
> ⚠️ **Sửa quan trọng so với bản đầu tiên của khối này:** bản đầu đã bỏ hết tham chiếu `§2.x` nhưng **vẫn còn 13 tham chiếu nội chương** dạng `§3.4`, `§3.5.1`, `§3.2.1`. Đó là vi phạm quy tắc 21/09 (*"bỏ toàn bộ tham chiếu chéo dạng `§2.x` trong thân bài, chỉ giữ tham chiếu cấp chương"*) và `00_outline.md` §7.5 (*"cấm đẩy lập luận ra tham chiếu mục; lý do phải nằm trong câu"*). Bản này **không còn ký hiệu `§` nào trong thân bài**. Mỗi chỗ trước đây trỏ đi nơi khác nay tự mang lý do, hoặc dùng một chỉ dẫn đọc bằng lời (*"phần sau của chương"*, *"mục trước"*), hoặc dùng tham chiếu **cấp chương**. Ký hiệu `§` chỉ còn xuất hiện trong khối này, khối *Tài liệu tham khảo* và khối *Ghi chú thi hành*, và chỉ để trỏ tới `00_outline.md`, tức tài liệu làm việc chứ không phải thân luận văn.
>
> **Tự kiểm §7.7** (chạy trên **thân chương**, tức từ mục 3.1 đến hết mục 3.6; không tính khối này và hai khối cuối):
>
> | Phép đếm | Kết quả | Hạn mức | |
> |---|---|---|---|
> | Tham chiếu `§` trong thân bài | **0** | phải bằng 0 | ✅ |
> | Tham chiếu mục của chương khác | **0** (chỉ còn cấp chương) | phải bằng 0 | ✅ |
> | AI#1 — cấu trúc tương phản, **tổng máy đếm** | **4** | ≤ 3 mỗi chương | ⚠️ xem bảng dưới |
> | AI#1 — cấu trúc tương phản **mang chức năng tu từ** | **3** | ≤ 3 mỗi chương | ✅ |
> | AI#4 — câu rào | **1** (mục 3.4.2) | đúng 1 mỗi chương | ✅ |
> | AI#6 — dấu `—` chêm, ngoài bảng | **1** | ≤ 1 mỗi trang | ✅ |
> | AI#8 — cụm sáo cấm dùng | **0** | phải bằng 0 | ✅ |
> | `\boldsymbol` | **0** | — | ✅ |
>
> | # | Vị trí | Câu | Xử lý |
> |---|---|---|---|
> | 1 | 3.3.4 | "…hệ số của số hạng gradient là $\lambda(1{-}\lambda)$, **không phải** $\lambda$" | giữ — phát biểu đại số, không phải khuôn tu từ; cùng loại với các chỗ máy đếm mà Ch.2 đã ghi nhận |
> | 2 | 3.4.2 | "…hiệu chuẩn **xoay** ranh giới **chứ không** co giãn nó" | giữ — cả câu tồn tại để sửa một trực giác sai |
> | 3 | 3.5.3 | "…**không phải** đối thủ trực tiếp **mà** là một họ song song" | giữ — phân định phạm vi áp dụng của trần LDA |
> | 4 | 3.6 | "…ở **mức cơ chế** … **chứ không** ở mức giá trị tăng từ con số này lên con số kia" | giữ — phát biểu quy tắc so sánh trong cùng nền tảng |
>
> **Ký hiệu đã đổi (A5):** tham số mô hình nay là $\theta$; $\omega$ chỉ còn nghĩa bộ phân lớp, đúng `00_outline.md` §7.1. Lý do chọn $\theta$ thay vì $w$ ghi ở mục 2 của *Ghi chú thi hành*.
>
> **Đánh số phương trình (3.1)–(3.7) giữ nguyên hoàn toàn**, vì Ch.4 mục 4.1.2, 4.2.1 và 4.6.2 tham chiếu trực tiếp tới chúng. Các công thức mới thêm ở mục 3.1 và 3.2 đều để không đánh số.
>
> **Độ dài:** thân chương ≈6.200 từ, tức khoảng **7 trang** ở format đã chốt, so với 9–10 trang được giao ở `00_outline.md` §4. Bản này đã lấp phần nội dung *được giao mà còn khuyết* và nâng từ ≈3.950 lên ≈6.200 từ. Phần còn thiếu **không** nên bù bằng cách viết phồng; chỗ còn chịu được thêm nội dung thật là mục 3.4, hiện mỏng nhất trong sáu mục.
>
> ⚠️ **Còn treo:** A6 (IR#9) là việc hành chính, đã dựng sẵn chỗ ở đầu mục 3.6 nhưng chưa điền được. B8 đòi cắt gọn Ch.5 mục 5.2.2, thuộc file khác. Hai việc cho `00_outline.md` ghi ở cuối khối.

---

## 3.1. Bài toán Học liên kết và local SGD

### 3.1.1. Hình thức hoá

Hệ thống gồm $N$ client. Client thứ $i$ giữ tập dữ liệu cục bộ $D_i = \{(x, y)\}$ lấy mẫu từ phân phối $P_i(x, y)$, và từ đó có hàm mục tiêu riêng

$$f_i(\theta) = \mathbb{E}_{(x,y)\sim P_i}\big[\ell(f(x;\theta),\, y)\big],$$

trong đó $f(\cdot\,;\theta)$ là mô hình với vector tham số $\theta$, và $\ell$ là hàm mất mát trên một mẫu. Mục tiêu của cả hệ thống là nghiệm

$$\theta^{*} = \arg\min_{\theta} f(\theta), \qquad f(\theta) = \sum_{i=1}^{N} p_i\, f_i(\theta), \qquad p_i = \frac{|D_i|}{\sum_j |D_j|},$$

tức một tổ hợp lồi của các mục tiêu cục bộ, với trọng số tỉ lệ theo lượng dữ liệu mỗi client nắm giữ.

Mô hình được tách thành hai phần. **Bộ trích xuất đặc trưng** $\phi: \mathcal{X} \to \mathbb{R}^d$ nhận ảnh đầu vào và trả về một vector $d$ chiều. **Bộ phân lớp** $\omega: \mathbb{R}^d \to \mathbb{R}^C$ nhận vector ấy và trả về điểm số cho từng lớp trong $C$ lớp. Toàn mô hình là hợp thành $f = \omega \circ \phi$, và $\theta$ gom tham số của cả hai phần. Phép tách này cần thiết vì thiên lệch do dữ liệu không đồng nhất gây ra không phân bố đều trên mô hình: nó tập trung ở một trong hai thành phần, và hai mục cuối chương xác định đó là thành phần nào, theo cơ chế gì.

Ký hiệu $w_c \in \mathbb{R}^d$ dành riêng cho vector trọng số của lớp $c$ trong tầng cuối, tức hàng thứ $c$ của ma trận trọng số thuộc $\omega$. Chuẩn $\ell_2$ của các $w_c$ là đại lượng trung tâm của phần phân tích cơ chế ở cuối chương.

Chiều đặc trưng $d$ **phụ thuộc kiến trúc** và được ghi rõ ở mọi bảng kết quả: $d = 512$ với VGG11 và ResNet18, $d = 256$ với CCT, $d = 64$ với ResNet20-GN. Đây không phải một hằng số của bài toán, và hai kết quả đo trên hai backbone khác nhau là hai kết quả ở hai chiều đặc trưng khác nhau.

### 3.1.2. FedAvg và nguồn gốc client drift

Ở vòng truyền thông $t$, FedAvg [2] thực hiện ba bước:

1. Máy chủ phát tham số toàn cục $\theta_t$ tới tập client được chọn $S_t$.
2. Mỗi client $i \in S_t$ đặt $\theta_i^0 \leftarrow \theta_t$, rồi chạy $K$ bước SGD trên $f_i$ để thu được $\theta_i^K$.
3. Máy chủ gộp: $\theta_{t+1} = \sum_{i \in S_t} \tilde p_i\, \theta_i^K$, với $\tilde p_i = p_i / \sum_{j \in S_t} p_j$ là trọng số đã chuẩn hoá lại trên riêng tập được chọn.

Khi $K = 1$ và mọi client tham gia mỗi vòng, quy trình trùng với SGD tập trung trên $f$. Khi $K > 1$, mỗi client chạy nhiều bước trên mục tiêu **riêng** của nó. Nếu $P_i \ne P_j$ thì nói chung $\arg\min f_i \ne \arg\min f_j$, nên sau $K$ bước các $\theta_i^K$ tiến về những điểm khác nhau. Trung bình của các điểm đã lệch không còn bảo đảm là một bước tiến tốt cho $f$, và nó có thể rơi vào một vùng mà không client nào coi là tốt. Hiện tượng này là **client drift**.

Hai đại lượng điều khiển mức độ nghiêm trọng của nó. Thứ nhất là **số bước cục bộ $K$**: càng nhiều bước giữa hai lần đồng bộ thì mỗi client càng đi sâu về phía nghiệm riêng. Thứ hai là **mức chênh lệch giữa các phân phối $P_i$**. Luận văn giữ $K$ cố định ở giá trị của cấu hình đã đăng ký và khảo sát trục thứ hai, nên mọi so sánh trong Chương 5 diễn ra ở cùng một ngân sách bước cục bộ.

Cần phân biệt client drift với hệ quả của nó trên từng thành phần của mô hình. Client drift là một phát biểu về **quỹ đạo tối ưu hoá** của toàn bộ vector tham số: nó nói các $\theta_i^K$ tách xa nhau, nhưng không nói phần nào của $\theta$ chịu trách nhiệm. Việc thiên lệch nằm ở $\omega$ hay ở $\phi$, và hình thành theo cơ chế nào, là một câu hỏi tách biệt, và phần sau của chương trả lời nó bằng bằng chứng đo được.

---

## 3.2. Mô hình hoá dữ liệu không đồng nhất

### 3.2.1. Phân rã phân phối

Viết phân phối liên hợp dưới dạng $P_i(x, y) = P_i(y)\,P_i(x \mid y)$ cho phép tách hai dạng lệch một cách hình thức:

- **Lệch phân phối nhãn (label skew):** $P_i(y) \ne P_j(y)$, trong khi $P_i(x \mid y) = P(x \mid y)$ với mọi $i$.
- **Lệch phân phối đặc trưng (feature skew):** $P_i(x \mid y) \ne P_j(x \mid y)$.

Hai trục này độc lập về mặt khái niệm, và luận văn khảo sát chúng riêng rẽ. Sự độc lập ấy chỉ đúng **ở mức phân phối dữ liệu**. Trong Học liên kết sâu, mỗi client huấn luyện một bộ trích xuất riêng $\phi_i$, nên ngay cả khi các $P_i(x\mid y)$ trùng nhau, phân phối **đặc trưng** có điều kiện lớp, tức phân phối của $\phi_i(x)$ khi biết $y$, vẫn có thể khác nhau giữa các client, bởi vì bản thân các $\phi_i$ đã khác nhau. Đây là một hệ quả của việc huấn luyện, không phải của dữ liệu, và phần phân tích thiên lệch ở cuối chương quay lại nó với số đo cụ thể.

### 3.2.2. Phân phối Dirichlet và cách mô phỏng label skew

Công cụ mô phỏng lệch phân phối nhãn là phân hoạch Dirichlet. Mục này phát biểu định nghĩa chính quy của phân phối ấy, vì các chương sau tham chiếu tới cả ngưỡng chuyển chế độ lẫn quy ước tham số hoá.

Phân phối Dirichlet bậc $C$ nhận giá trị trên **đơn hình xác suất**

$$\Delta^{C-1} = \Big\{\, q \in \mathbb{R}^{C} \;:\; q_c \ge 0 \ \ \forall c, \ \ \textstyle\sum_{c=1}^{C} q_c = 1 \,\Big\},$$

tức tập các vector tỉ lệ lớp hợp lệ. Với **vector nồng độ** $a = (a_1, \ldots, a_C)$, $a_c > 0$, hàm mật độ là

$$\mathrm{Dir}(q; a) \;=\; \frac{1}{B(a)} \prod_{c=1}^{C} q_c^{\,a_c - 1}, \qquad B(a) = \frac{\prod_{c} \Gamma(a_c)}{\Gamma\!\big(\sum_{c} a_c\big)} .$$

Đặt $a_0 = \sum_c a_c$ là **nồng độ tổng**. Khi đó $\mathbb{E}[q_c] = a_c / a_0$ và

$$\mathrm{Var}[q_c] = \frac{a_c\,(a_0 - a_c)}{a_0^{2}\,(a_0 + 1)} .$$

Hai công thức này phân vai rõ ràng cho hai thuộc tính của $a$: **hướng** của $a$ quyết định tỉ lệ lớp kỳ vọng, còn **độ lớn** $a_0$ quyết định mức tập trung quanh kỳ vọng đó, vì phương sai giảm khi $a_0$ tăng.

Số mũ $a_c - 1$ trong hàm mật độ giải thích vì sao $a_c = 1$ là ngưỡng chuyển chế độ. Khi mọi $a_c > 1$, số mũ dương, mật độ triệt tiêu tại các mặt $q_c = 0$, nên mẫu rút ra tránh biên và tập trung quanh vector kỳ vọng. Khi mọi $a_c < 1$, số mũ âm, mật độ phân kỳ khi $q_c \to 0$, nên khối lượng xác suất dồn về biên của đơn hình: mẫu rút ra có vài thành phần nhận giá trị gần 1 và phần còn lại gần 0. Trong chế độ thứ hai, mỗi client trên thực tế chỉ giữ mẫu của một vài lớp.

Luận văn dùng quy ước tham số hoá của Hsu, Qi và Brown [4]: đặt $a = \alpha\,p$, trong đó $p$ là phân phối lớp tiên nghiệm thoả $\sum_c p_c = 1$, rồi rút độc lập cho từng client một vector

$$q_i \;\sim\; \mathrm{Dir}(\alpha \cdot p).$$

Vì $p$ đã chuẩn hoá nên $\alpha$ chính là nồng độ tổng $a_0$, còn nồng độ mỗi thành phần là $\alpha p_c$. NIID-Bench [3] dùng dạng chuyển vị, rút một vector trên $N$ client cho từng lớp, và tham số ghi trong bài báo đó là nồng độ mỗi thành phần. Cùng một con số in trong hai bài báo vì vậy mô tả hai mức lệch khác nhau.

Theo quy ước trên, cấu hình đã đăng ký là $\alpha = 0{,}1$ trên CIFAR-10 với tiên nghiệm đều $p_c = 1/10$, cho nồng độ mỗi thành phần $\alpha p_c = 0{,}01$. Giá trị này nhỏ hơn ngưỡng $1$ hai bậc, nên phân hoạch nằm sâu trong chế độ dồn về biên: mỗi client thực tế chỉ thấy một vài lớp.

Ký hiệu Dirichlet mơ hồ trong văn liệu chính vì hai quy ước cùng dùng một chữ cái. Luận văn vì vậy áp dụng một quy tắc báo cáo cố định: mỗi lần nêu tham số Dirichlet, ghi đủ bộ ba gồm **vector nồng độ, trục lấy mẫu, và số thành phần**. Mọi bảng kết quả trong luận văn tuân theo quy tắc này.

### 3.2.3. Mô phỏng feature skew bằng phép xoay

Feature skew được mô phỏng bằng cách gán cho mỗi client một phân phối trên tập góc xoay $\Theta = \{0^\circ, 15^\circ, \ldots, 135^\circ\}$, tức $|\Theta| = 10$ góc cách đều nhau $15^\circ$. Client $i$ rút

$$q_i^{\text{rot}} \;\sim\; \mathrm{Dir}(\alpha_{\text{rot}} \cdot u),$$

với $u$ là phân phối đều trên $\Theta$, rồi mỗi ảnh cục bộ được xoay bởi một góc lấy mẫu độc lập theo $q_i^{\text{rot}}$. Quy ước tham số hoá ở đây trùng với quy ước vừa dùng cho label skew: $\alpha_{\text{rot}}$ là **nồng độ tổng**, còn nồng độ mỗi thành phần là $\alpha_{\text{rot}}/10$.

Phân phối đầu vào có điều kiện lớp của client $i$ khi đó là

$$P_i(x \mid y) \;=\; \sum_{\theta \in \Theta} q_i^{\text{rot}}(\theta)\; P_0\big(R_\theta^{-1} x \mid y\big),$$

với $P_0$ là phân phối gốc và $R_\theta$ là phép xoay góc $\theta$. Các client khác nhau ở **toán tử trộn góc**, còn phân phối nhãn giữ nguyên.

Cấu hình mặc định đặt $\alpha_{\text{rot}} = 1{,}0$, cho nồng độ mỗi thành phần $0{,}1$. Mức này cũng nằm dưới ngưỡng $1$, nên các mẫu $q_i^{\text{rot}}$ rất thưa. Để định lượng, gọi **số góc hiệu dụng** của client $i$ là nghịch đảo tổng bình phương của vector tỉ lệ,

$$n_{\text{eff}}(i) \;=\; \Big(\textstyle\sum_{\theta} q_i^{\text{rot}}(\theta)^2\Big)^{-1},$$

một đại lượng bằng $10$ khi client dùng cả mười góc đều nhau và bằng $1$ khi nó chỉ dùng một góc. Ở cấu hình mặc định, kỳ vọng của $n_{\text{eff}}$ là $\approx 2{,}09$ với độ lệch chuẩn $\approx 0{,}80$. Mỗi client trên thực tế dùng khoảng hai góc trội.

Ba tính chất của cách mô phỏng này giới hạn phạm vi kết luận, và cả ba phải được nêu ngay ở đây vì chúng chi phối cách đọc toàn bộ phần thực nghiệm.

**Thứ nhất, cấu hình mặc định đã ở gần cực trị nặng.** Với $n_{\text{eff}} \approx 2$ trên mười góc khả dĩ, trục $\alpha_{\text{rot}}$ chỉ còn quét được về phía **nhẹ hơn**, tức về phía $\alpha_{\text{rot}}$ tăng. Đường đặc tuyến theo $\alpha_{\text{rot}}$ trong Chương 5 vì vậy là một nhánh, không đối xứng hai phía.

**Thứ hai, toán tử trộn dùng chung cho mọi lớp.** Góc được lấy mẫu độc lập với nhãn, nên phép biến đổi là như nhau cho mọi lớp trong một client. Đây là feature skew **không phụ thuộc lớp**. Đặc điểm này là đặc điểm chung của văn liệu: nhiễu Gauss theo client, corruption chuẩn hoá, và phân hoạch theo nguồn thật đều độc lập với lớp. Feature skew **phụ thuộc lớp**, trong đó phép biến đổi khác nhau theo từng lớp, chỉ xuất hiện trong hai tiền lệ nằm ngoài các benchmark Học liên kết chuẩn. Chương 6 xếp đặc điểm này vào phần hạn chế và nêu một hướng phát triển tương ứng.

**Thứ ba, phép xoay là biến đổi nhóm khả nghịch, thuần hình học.** Nó bảo toàn nội dung ngữ nghĩa của ảnh và chỉ đổi hệ toạ độ, nên nó nằm ở cực dễ của phổ dịch chuyển miền. Đổi cảm biến, đổi phong cách, hay đổi điều kiện thu thập đều khó hơn nhiều và nói chung không có cấu trúc nhóm.

---

## 3.3. Global Mixup và xấp xỉ Taylor bậc nhất

Đây là mục trung tâm của chương. Nó dẫn xuất chính xác đối tượng mà luận văn đo, và xác định bốn cấu hình thuật toán mà Chương 4 dựng khung thực nghiệm quanh.

### 3.3.1. Mixup và trở ngại trong Học liên kết

Mixup [9] huấn luyện mô hình trên tổ hợp lồi của các cặp mẫu:

$$\tilde{x} = (1-\lambda)x_i + \lambda x_j, \qquad \tilde{y} = (1-\lambda)y_i + \lambda y_j,$$

với $\lambda$ là **trọng số trộn** và nhãn ở dạng one-hot. Trong Học liên kết, phiên bản có ý nghĩa nhất là **global Mixup**, trộn mẫu của client $i$ với mẫu của client $j \ne i$, vì chỉ phép trộn xuyên client mới bắc cầu giữa hai phân phối cục bộ. Nhưng nó đòi hỏi $x_j$ ở dạng **thô**, tức vi phạm đúng ràng buộc định nghĩa bài toán.

### 3.3.2. Tách hàm mất mát theo nhãn

Với hàm mất mát cross-entropy, $\ell(f(x), y) = -\sum_c y_c \log \mathrm{softmax}(f(x))_c$ là **tuyến tính theo nhãn**. Do đó

$$\ell\big(f(\tilde{x}),\, (1-\lambda)y_i + \lambda y_j\big) = (1-\lambda)\,\ell\big(f(\tilde{x}), y_i\big) + \lambda\,\ell\big(f(\tilde{x}), y_j\big).$$

Mục tiêu global Mixup viết lại thành

$$\mathcal{L}_{\text{GM}} = (1-\lambda)\,\ell\big(f((1{-}\lambda)x_i + \lambda x_j), y_i\big) + \lambda\,\ell\big(f((1{-}\lambda)x_i + \lambda x_j), y_j\big). \tag{3.1}$$

Toàn bộ phần còn lại của mục này là các cách khác nhau để xấp xỉ (3.1) mà không cần $x_j$ thô.

### 3.3.3. Mẫu trung bình đại diện và NaiveMix

Khung **Mean Augmented Federated Learning (MAFL)** của FedMix [1] thay cặp $(x_j, y_j)$ của một client khác bằng một **mẫu trung bình đại diện**: client $j$ chọn ngẫu nhiên $M$ mẫu cục bộ và tính

$$\bar{x}_g = \frac{1}{M}\sum_{m=1}^{M} x_m, \qquad \bar{y}_g = \frac{1}{M}\sum_{m=1}^{M} y_m, \tag{3.2}$$

trong đó $\bar y_g$ là một **nhãn mềm**, tức histogram nhãn đã chuẩn hoá của $M$ mẫu đó. Chỉ các cặp $(\bar{x}_g, \bar y_g)$ được chia sẻ qua máy chủ. Tham số $M$ điều khiển mức độ nén: $M = 1$ tương đương chia sẻ ảnh thô, còn $M$ lớn cho ảnh gần như không còn nhận dạng được.

Thay trực tiếp vào (3.1) cho thuật toán thứ nhất:

$$\mathcal{L}_{\text{NaiveMix}} = (1{-}\lambda)\,\ell\big(f((1{-}\lambda)x_i + \lambda\bar{x}_g), y_i\big) + \lambda\,\ell\big(f((1{-}\lambda)x_i + \lambda\bar{x}_g), \bar y_g\big) \tag{3.3}$$

Điểm cần nhớ: trong NaiveMix, $\bar{x}_g$ đi vào **bên trong lượt truyền xuôi**, nên mô hình thực sự nhìn thấy ảnh đã trộn.

### 3.3.4. Khai triển Taylor bậc nhất và FedMix

Thuật toán thứ hai xuất phát từ nhận xét rằng khi $\lambda \ll 1$, điểm $(1{-}\lambda)x_i + \lambda\bar{x}_g$ nằm gần $(1{-}\lambda)x_i$. Khai triển Taylor bậc nhất quanh điểm đó cho, với nhãn $y$ bất kỳ,

$$\ell\big(f((1{-}\lambda)x_i + \lambda\bar{x}_g), y\big) \;\approx\; \ell\big(f((1{-}\lambda)x_i), y\big) \;+\; \lambda\, \nabla_{x}\,\ell\big(f(x), y\big)\Big|_{x=(1-\lambda)x_i} \cdot \bar{x}_g. \tag{3.4}$$

Áp (3.4) vào **cả hai** số hạng của (3.3) và gom lại:

$$\mathcal{L} \approx \underbrace{(1{-}\lambda)\,\ell\big(f((1{-}\lambda)x_i), y_i\big)}_{\text{(I)}} + \underbrace{\lambda\,\ell\big(f((1{-}\lambda)x_i), \bar y_g\big)}_{\text{(II)}} + \underbrace{\lambda(1{-}\lambda)\,\nabla_{x}\ell_{y_i} \cdot \bar{x}_g}_{\text{(III)}} + \underbrace{\lambda^2\,\nabla_{x}\ell_{\bar y_g} \cdot \bar{x}_g}_{\text{(IV)}} \tag{3.5}$$

Số hạng thứ nhất của (3.3) mang trọng số $(1{-}\lambda)$, nên phần bậc nhất của nó là (III) với hệ số $\lambda(1{-}\lambda)$. Số hạng thứ hai mang trọng số $\lambda$, nên phần bậc nhất của nó là (IV) với hệ số $\lambda^2$. Giữ ba số hạng đầu và bỏ (IV):

$$\mathcal{L}_{\text{FedMix}} = (1{-}\lambda)\,\ell\big(f((1{-}\lambda)x_i), y_i\big) + \lambda\,\ell\big(f((1{-}\lambda)x_i), \bar y_g\big) + \lambda(1{-}\lambda)\,\nabla_{x}\ell_{y_i} \cdot \bar{x}_g \tag{3.6}$$

**Phép bỏ số hạng (IV) đắt hay rẻ tuỳ $\lambda$.** Tỉ lệ giữa hệ số của (IV) và hệ số của (III) là

$$\frac{\lambda^2}{\lambda(1{-}\lambda)} \;=\; \frac{\lambda}{1-\lambda},$$

nhận giá trị $0{,}053$ tại $\lambda = 0{,}05$, giá trị $0{,}111$ tại $\lambda = 0{,}1$, và giá trị $0{,}25$ tại $\lambda = 0{,}2$. Ở đầu dưới của khoảng vận hành mà cả hai công trình gốc sử dụng, số hạng bị bỏ nhỏ hơn số hạng được giữ khoảng hai mươi lần, và phép bỏ là rẻ. Ở $\lambda = 0{,}2$ nó bằng một phần tư, và phép bỏ trở thành một xấp xỉ thô. Phát biểu "số hạng bậc hai của $\lambda$ không đáng kể" vì vậy chỉ có hiệu lực về phía $\lambda$ nhỏ. Vì tỉ lệ này thay đổi theo $\lambda$ trong khi hệ số của số hạng (II) thì không, mức cải thiện đo được cũng phụ thuộc $\lambda$ theo một cách không đơn điệu hiển nhiên, và Chương 4 lấy chính điều đó làm một trong các yếu tố gây nhiễu phải loại trừ.

**Ba hệ quả của (3.6).**

*Thứ nhất, $\bar{x}_g$ không còn đi vào lượt truyền xuôi.* Mô hình chỉ nhìn thấy $(1{-}\lambda)x_i$, tức ảnh cục bộ đã co tỉ lệ. Thông tin từ client khác đi vào duy nhất qua số hạng (III), dưới dạng một tích vô hướng giữa $\bar{x}_g$ và gradient của hàm mất mát theo đầu vào.

*Thứ hai, hệ số của số hạng gradient là $\lambda(1{-}\lambda)$, không phải $\lambda$.* Thừa số $(1{-}\lambda)$ kế thừa từ trọng số của số hạng thứ nhất trong (3.3). Công thức rút gọn in trong bài báo FedMix [1] viết số hạng thứ ba dưới dạng $\lambda\,(\partial\ell/\partial x)\cdot\bar{x}_g$ mà không nói rõ $\partial\ell/\partial x$ là đạo hàm của số hạng **đã nhân trọng số** hay của hàm mất mát **thuần**. Dẫn xuất (3.5) cho thấy chỉ cách đọc thứ nhất mới nhất quán với (3.1).

*Thứ ba, $\bar y_g$ vẫn đi vào qua số hạng (II) ở cả hai thuật toán.* Vậy (3.3) và (3.6) không khác nhau ở việc có dùng nhãn mềm hay không.

**Ánh xạ sang cài đặt.** Ba số hạng của (3.6) ứng một-một với ba đại lượng trong hiện thực FedMix của nền tảng FedBR [11]: số hạng (I) là `loss1`, số hạng (II) là `loss2`, và số hạng (III) là `loss3`. Thứ tự tính trong mã nguồn xác nhận hệ số $\lambda(1{-}\lambda)$: `loss1` được tính đã kèm sẵn thừa số $(1{-}\lambda)$; đạo hàm theo đầu vào được lấy của chính `loss1`, nên nó mang theo thừa số ấy; `loss3` rồi nhân thêm $\lambda$. Điểm khai triển cũng khớp, vì biến đầu vào đã được co tỉ lệ thành $(1{-}\lambda)x_i$ trước khi lấy đạo hàm. Chương 5 dùng quan sát này làm mốc đối chiếu cho phần kiểm toán mã nguồn, ở đó nó là một chỗ mà mã và lý thuyết khớp nhau.

### 3.3.5. Điều gì thực sự phân biệt hai thuật toán

So sánh trực tiếp (3.3) và (3.6) cho thấy chúng khác nhau ở **hai chỗ đồng thời**.

**Bảng 3.1.** Hai chỗ khác nhau giữa NaiveMix (3.3) và FedMix (3.6). Cột *Điểm đánh giá* ghi đối số được đưa vào mô hình khi tính hàm mất mát, trong đó $x_i$ là ảnh cục bộ, $\bar x_g$ là mẫu trung bình đại diện nhận từ client khác theo (3.2), và $\lambda$ là trọng số trộn. Cột *Số hạng gradient* ghi sự có mặt của số hạng (III) trong (3.5), tức số hạng $\lambda(1{-}\lambda)\,\nabla_{x}\ell_{y_i}\cdot\bar x_g$.

| Thuật toán | Điểm đánh giá $\ell$ | Số hạng gradient (III) |
|---|---|---|
| NaiveMix (3.3) | $(1{-}\lambda)x_i + \lambda\bar{x}_g$ | không có |
| FedMix (3.6) | $(1{-}\lambda)x_i$ | có |

Quan sát này có hệ quả trực tiếp cho việc quy kết. Chênh lệch hiệu năng giữa hai thuật toán không quy được hoàn toàn cho số hạng Taylor, bởi việc rút $\bar{x}_g$ khỏi lượt truyền xuôi cũng đồng thời thay đổi chế độ chính quy hoá và mức nhiễu của đầu vào. Hai thay đổi xảy ra cùng lúc, nên một con số đo được là tác động tổng hợp của cả hai.

Tháo rời hai trục cho một lưới đầy đủ bốn ô.

**Bảng 3.2.** Lưới bốn cấu hình sinh ra từ hai trục của Bảng 3.1. Hàng là điểm đánh giá hàm mất mát, cột là sự có mặt của số hạng gradient (III). Ô **A** và ô **B** là hai thuật toán đã công bố; ô **C** là cấu hình (3.7) mà luận văn bổ sung; ô **D** không ứng với một khai triển nhất quán nào của (3.1) và được giải thích bên dưới.

| | không có (III) | có (III) |
|---|---|---|
| Đánh giá tại $(1{-}\lambda)x_i + \lambda\bar{x}_g$ | **A** = NaiveMix | D |
| Đánh giá tại $(1{-}\lambda)x_i$ | **C** | **B** = FedMix |

Cấu hình ở ô C là

$$\mathcal{L}_{\text{C}} = (1{-}\lambda)\,\ell\big(f((1{-}\lambda)x_i), y_i\big) + \lambda\,\ell\big(f((1{-}\lambda)x_i), \bar y_g\big) \tag{3.7}$$

tức (3.6) sau khi bỏ đúng số hạng (III). Hiệu $\mathcal{L}_{\text{B}} - \mathcal{L}_{\text{C}}$ vì vậy cô lập số hạng (III) với điểm đánh giá giữ cố định, và đây là đại lượng mà đóng góp thứ nhất của luận văn đo. Cấu hình (3.7) không xuất hiện trong bài báo FedMix [1], kể cả ở phần phụ lục.

Ô D giữ phép trộn ở đầu vào và đồng thời thêm số hạng gradient, nên $\bar{x}_g$ đi vào hàm mất mát hai lần. Nó không tương ứng với bất kỳ khai triển nhất quán nào của (3.1), và vai trò khả dĩ của nó chỉ là chẩn đoán. Luận văn chạy ba ô và bỏ ô D, với cái giá là số hạng (III) chỉ được cô lập tại một điểm đánh giá duy nhất; Chương 4 nêu hệ quả của việc đó đối với thiết kế, và Chương 6 nêu nó như một hướng phát triển gần.

### 3.3.6. Về số hạng bậc hai của khai triển

Tỉ lệ $\lambda/(1-\lambda)$ vừa nêu nói về hệ số của hai số hạng trong cùng một khai triển bậc nhất. Một câu hỏi khác là liệu việc giữ thêm số hạng **bậc hai** của chính khai triển Taylor (3.4) có cải thiện xấp xỉ hay không.

Một phép đo trong [17] cho thấy số hạng hiệu chỉnh bậc hai trong không gian đầu vào có biên độ khoảng $10^{-4}$ so với số hạng bậc nhất, ở trọng số trộn $\lambda = 0{,}05$ và **tại thời điểm khởi tạo**. Hai điều kiện này thuộc về phát biểu và phải đi kèm mỗi lần trích dẫn: nguồn không đo ở các giá trị $\lambda$ lớn hơn, và không tuyên bố biên độ đó giữ nguyên trong suốt quá trình huấn luyện. Kết luận đúng mức là ở $\lambda = 0{,}05$ và tại khởi tạo, số hạng bậc hai không phải một đòn bẩy hợp lý. Nhánh bậc hai không được khảo sát trong luận văn.

---

## 3.4. Thiên lệch học cục bộ: đặc trưng và bộ phân lớp

### 3.4.1. Ba biểu hiện

FedBR [11] phân tách hệ quả của cập nhật cục bộ trên dữ liệu không đồng nhất thành ba hiện tượng, gọi chung là **thiên lệch học cục bộ**:

1. **Bộ phân lớp cục bộ bị thiên lệch.** Sau $K$ bước trên dữ liệu mà một số lớp chiếm đa số, $\omega_i$ có xu hướng gán mọi mẫu vào các lớp xuất hiện tại chỗ, kể cả mẫu thuộc lớp chưa từng thấy.
2. **Đặc trưng cục bộ lệch khỏi đặc trưng toàn cục.** Với cùng một đầu vào $x$, giá trị $\phi_i(x)$ khác đáng kể so với $\phi_g(x)$ của bộ trích xuất toàn cục.
3. **Đặc trưng cục bộ của các lớp khác nhau quá gần nhau.** Bộ trích xuất $\phi_i$ mất khả năng phân tách các mẫu thuộc phân phối mà client $i$ không quan sát.

Hiện tượng thứ hai xác nhận bằng số đo điều mà phép phân rã phân phối ở đầu chương mới chỉ nêu ở mức khái niệm. **Ngay cả dưới label skew thuần**, nơi các $P_i(x\mid y)$ trùng nhau theo định nghĩa phân hoạch, phân phối đặc trưng có điều kiện lớp vẫn khác nhau giữa các client, bởi vì chính $\phi_i$ đã trôi. Nói cách khác, label skew sinh ra lệch trong không gian đặc trưng **thông qua bộ trích xuất**, không phải thông qua dữ liệu.

Điều này có hai hệ quả cho phần còn lại của luận văn. Một phương pháp chỉ hiệu chỉnh $\omega$ không đương nhiên đủ, vì nguồn lệch nằm cả ở $\phi$. Và một phương pháp thao tác trên thống kê đặc trưng đang thao tác trên một đại lượng mà chính nó đã bị lệch, nên phạm vi hiệu lực của nó cần được phát biểu cẩn thận; mục tiếp theo làm việc đó bằng một kết quả lý thuyết cổ điển.

### 3.4.2. Thiên lệch ở bộ phân lớp là thiên lệch định hướng

Một trực giác phổ biến cho rằng thiên lệch của bộ phân lớp thể hiện ở **độ lớn** của các vector trọng số: lớp chiếm đa số cục bộ có $\lVert w_c \rVert$ lớn hơn, nên logit của nó lớn hơn.

Phép đo trong [17] mâu thuẫn với trực giác đó. Trên một backbone không dùng chuẩn hoá theo lô, tỉ lệ giữa $\max_c \lVert w_c \rVert_2$ và $\min_c \lVert w_c \rVert_2$ ở tầng cuối chỉ vào khoảng $1{,}10$ đến $1{,}17$, tức gần như đồng đều. Trong khi đó, việc hiệu chuẩn lại tầng cuối làm thay đổi độ chính xác vài điểm phần trăm và nâng recall của lớp bị phục vụ kém nhất lên rất mạnh.

Một chênh lệch chuẩn ở mức dưới $20\%$ không thể tạo ra biến thiên recall lớn như vậy nếu cơ chế là co giãn độ lớn. Kết luận là thiên lệch nằm ở **hướng** của ranh giới quyết định, và hiệu chuẩn **xoay** ranh giới chứ không co giãn nó.

Kết luận này quan trọng với luận văn vì hai lý do. Thứ nhất, nó xác nhận chẩn đoán mà đề tài dựa vào: mục tiêu là tăng cường đặc trưng tại các vùng ranh giới quyết định để giảm sai lệch nhãn, và phép đo trên cho thấy ranh giới quyết định đúng là nơi thiên lệch tập trung. Thứ hai, nó đặt ra câu hỏi mà Chương 5 trả lời: đòn bẩy trộn trung bình có xoay được ranh giới đó không, hay chỉ tác động lên những chiều ít mang thông tin.

Phạm vi của kết luận cần được nêu kèm: nó được đo trên **một** họ kiến trúc không dùng chuẩn hoá theo lô, và nguồn tự cảnh báo rằng một backbone có chuẩn hoá có thể định hình lại phát hiện này. Chương 5 đăng ký một kiểm soát kiến trúc ở dạng tuỳ chọn; nếu kiểm soát đó không được thực hiện thì giả thiết rằng phát hiện trên độc lập với kiến trúc vẫn chưa được kiểm tra, và Chương 6 ghi nhận điều đó trong phần hạn chế.

---

## 3.5. Bộ phân lớp sinh so với phân biệt: trần LDA

Mục này cung cấp nền lý thuyết để định vị nhóm phương pháp hiệu chuẩn tầng phân lớp từ thống kê lớp, mà CCVR [15] là công trình mẫu, và để làm rõ vì sao đối tượng nghiên cứu của luận văn nằm ngoài phạm vi của trần đó.

### 3.5.1. Hai kết quả cổ điển

Xét bài toán phân lớp trong đó đặc trưng của mỗi lớp tuân theo phân phối Gaussian với **hiệp phương sai chung**: $z \mid y{=}c \sim \mathcal{N}(\mu_c, \Sigma)$. Trong điều kiện này, bộ phân biệt tuyến tính (LDA) là bộ phân lớp sinh tối ưu, và ranh giới Bayes là tuyến tính.

Efron [18] chứng minh rằng hồi quy logistic, một bộ phân lớp **phân biệt**, có hiệu suất tiệm cận tương đối không vượt quá LDA dưới đúng các giả thiết trên. Ng và Jordan [19] bổ sung rằng bộ phân lớp phân biệt chỉ vượt hẳn bộ phân lớp sinh khi có **đủ dữ liệu thật** và mô hình sinh bị đặc tả sai; ở ngân sách mẫu nhỏ, bộ phân lớp sinh hội tụ nhanh hơn.

Hai điều kiện của phát biểu phải được giữ nguyên khi trích dẫn. Kết quả là **tiệm cận** và **trong kỳ vọng**, dưới giả thiết **Gaussian đúng với hiệp phương sai chung**. Nó không phải một chặn cứng ở mọi cỡ mẫu.

### 3.5.2. Hệ quả cho hiệu chuẩn bộ phân lớp trong Học liên kết

CCVR [15] và các phương pháp cùng nhánh ước lượng $(\mu_c, \Sigma_c)$ từ thống kê được truyền thông, rồi huấn luyện lại tầng cuối trên **mẫu ảo lấy từ chính mô hình Gaussian đó**. Theo hai kết quả vừa nêu, một head phân biệt huấn luyện trên dữ liệu sinh từ một Gaussian không thể vượt bộ phân biệt sinh tương ứng trên **tác vụ ảo** ấy. Đo lường trong [17] xác nhận thứ hạng này: head LDA dạng đóng cho mức cải thiện cao nhất, còn các phương án phân biệt tiệm cận nhưng không vượt.

Trần này có hai điều kiện áp dụng. Thứ nhất, nó áp cho **tác vụ ảo**, không cho phân phối thật. Nó phát biểu rằng từ một Gaussian đã cho thì không khai thác thêm được gì; việc Gaussian ấy có mô tả đúng dữ liệu hay không là một câu hỏi tách rời và không nằm trong phạm vi của kết quả. Thứ hai, khi hiệp phương sai của các lớp khác nhau, ranh giới Bayes là bậc hai, thuộc dạng QDA, và kết quả Efron không còn áp dụng.

Chế độ mẫu của phép đo cũng thuộc về phát biểu. Phép đo trong [17] thực hiện ở $n/d \approx 3{,}9$, tức số mẫu ảo dùng để huấn luyện lại tầng cuối chỉ gấp khoảng bốn lần số chiều đặc trưng. Đây là chế độ mẫu hữu hạn, nơi khoảng cách giữa hai họ bộ phân lớp còn đo được; kết quả tiệm cận của Efron dự đoán khoảng cách ấy thu hẹp khi $n/d$ tăng. Thứ hạng đo được vì vậy không ngoại suy sang các ngân sách mẫu ảo khác, và bản thân ngân sách mẫu ảo là biến làm đổi dấu mức cải thiện, như số liệu ở cuối chương cho thấy.

### 3.5.3. Vì sao đối tượng của luận văn nằm ngoài trần này

Cơ chế mà luận văn nghiên cứu, tức mẫu trung bình đại diện kết hợp khai triển Taylor, **không lấy mẫu từ bất kỳ mô hình Gaussian nào**. Nó thao tác trên:

- **không gian đầu vào**, không phải không gian đặc trưng;
- **dữ liệu thật đã được lấy trung bình**, không phải mẫu tổng hợp;
- **thống kê bậc nhất của dữ liệu thô**, không phải moment của đặc trưng.

Trần LDA vì vậy không ràng buộc cơ chế này. CCVR và nhóm hiệu chuẩn tầng phân lớp không phải đối thủ trực tiếp mà là một họ song song, giải quyết cùng triệu chứng bằng cơ chế khác. Mục này có mặt trong luận văn không để so sánh hiệu năng, mà để xác định ranh giới áp dụng của một kết quả lý thuyết thường bị viện dẫn quá phạm vi trong văn liệu Học liên kết.

---

## 3.6. Kết quả nền từ công trình đã công bố của tác giả

> ⚠️ **IR#9 — bắt buộc điền trước khi nộp.** Đoạn mở đầu dưới đây đang để chỗ trống cho: tên hội nghị, năm, trạng thái (accepted hoặc published), và DOI hoặc chỉ mục của [17]. Kèm theo: tuyên bố tái sử dụng ở đây và trong Lời cam đoan; văn bản xác nhận của đồng tác giả; đối chiếu điều khoản tái sử dụng của nhà xuất bản; khai báo tỉ lệ trùng lắp dự kiến **trước** khi quét.

Mục này dựa trên công trình [17], `[CẦN ĐIỀN: tên hội nghị, năm, trạng thái, DOI]`, do chính học viên thực hiện với đồng tác giả là cán bộ hướng dẫn. Nội dung được sử dụng lại ở đây theo khai báo tái sử dụng nêu trong Lời cam đoan.

Công trình đó khảo sát có kiểm soát nhóm phương pháp hiệu chuẩn bộ phân lớp và nhóm tăng cường trung bình, trên nền tảng Flower với mô hình huấn luyện từ đầu, dưới **lệch phân phối nhãn**. Bốn kết quả của nó tạo thành nền cho luận văn này.

**Thứ nhất, cơ chế tăng cường trung bình không mang lại cải thiện đo được trên nền tảng đó.** Ở cấu hình chính của công trình đó, gồm phân hoạch hai lớp mỗi client, 60 client với 15 client tham gia mỗi vòng, 500 vòng truyền thông, backbone VGG không dùng chuẩn hoá theo lô, và một mẫu trung bình đại diện cho mỗi lô, mức chênh của FedMix so với FedAvg trên ba hạt giống là $-1{,}86$ điểm phần trăm với độ lệch chuẩn mẫu $0{,}79$ điểm. Cận trên $95\%$ một phía là $-0{,}53$ điểm, tức loại trừ được khả năng có cải thiện. Đây là kết quả về **chính cơ chế** mà luận văn nghiên cứu, và nó xác lập nửa label skew của câu trả lời.

Bốn biến thể mở rộng khác cũng được khảo sát trong công trình đó: hai biến thể của phép ghép cặp có ý thức về lớp, một hiệu chỉnh bậc hai trong không gian đầu vào, và một phép biến đổi trong không gian đặc trưng. Cả bốn được nguồn gắn nhãn tường minh là **thăm dò**, và hai trong số đó chỉ chạy một hạt giống và chưa tinh chỉnh. Nhãn thăm dò được giữ nguyên ở mọi chỗ luận văn trích dẫn chúng, vì mức bằng chứng của chúng thấp hơn hẳn kết quả thứ nhất.

**Thứ hai, mức cải thiện phụ thuộc ngân sách và có thể đổi dấu.** Cùng một phương pháp hiệu chuẩn, ở đây là CCVR, cho những con số trái dấu nhau tuỳ ngân sách mẫu ảo mỗi lớp $M_c$ và tuỳ mức nghiêm trọng của lệch nhãn.

**Bảng 3.3.** Mức chênh độ chính xác của CCVR so với đường cơ sở, theo ngân sách mẫu ảo mỗi lớp $M_c$ và theo mức nghiêm trọng của lệch phân phối nhãn, đo trong [17]. $M_c$ là số đặc trưng ảo sinh ra cho mỗi lớp để huấn luyện lại tầng phân lớp; $\beta$ là nồng độ Dirichlet theo quy ước của NIID-Bench [3] mà công trình đó tuân theo, tức nồng độ **mỗi thành phần**, lấy mẫu trên trục **client** cho từng lớp, với 60 thành phần ứng với 60 client; nồng độ càng nhỏ thì lệch càng nặng. Đơn vị của cột cuối là điểm phần trăm.

| Ngân sách $M_c$ | Mức skew | Chênh so với đường cơ sở |
|---|---|---|
| 100 | $\beta = 0{,}1$ | $+0{,}29$ |
| 100 | $\beta = 0{,}3$ | $\mathbf{-0{,}76}$ |
| 2000 | $\beta = 0{,}1$ | $+0{,}97$ |
| 2000 | $\beta = 0{,}05$ | $+4{,}36 \pm 0{,}51$ |

Vế $-0{,}76$ là vế quan trọng nhất của bảng: ở ngân sách mẫu ảo thiếu, phương pháp làm mô hình **kém đi**. Đọc theo cặp hàng cũng thấy dấu của mức chênh phụ thuộc đồng thời vào cả hai biến: giữ $M_c$ cố định mà đổi $\beta$ thì dấu đảo, và giữ $\beta$ cố định mà tăng $M_c$ thì biên độ đổi theo. Một con số đơn lẻ vì vậy không mô tả được phương pháp, và mức cải thiện phải được báo cáo như một **đường đặc tuyến**, tức đồ thị mức cải thiện theo lượng thông tin được phép chia sẻ, thay cho một giá trị đo tại một điểm ngân sách duy nhất. Chương 4 xây giao thức đo trên nguyên tắc này, và trục $(\lambda, M)$ của luận văn là đối ứng trực tiếp của trục $M_c$ ở đây.

**Thứ ba, thiên lệch của bộ phân lớp là định hướng.** Đây là kết quả đã trình bày ở mục trước, nơi tỉ lệ chuẩn $\ell_2$ giữa lớp lớn nhất và lớp nhỏ nhất chỉ vào khoảng $1{,}10$ đến $1{,}17$ trong khi hiệu chuẩn lại tầng cuối đổi recall rất mạnh.

**Thứ tư, công trình đó tự khai ba giới hạn ngoại vi.** Phạm vi bằng chứng gồm một họ kiến trúc, một phân phối ảnh $32\times32$, và **một loại lệch phân phối duy nhất là label skew**. Nguồn cũng nêu rõ rằng backbone không dùng chuẩn hoá theo lô là giả thiết chịu lực cho phần phân tích Gaussian.

Ba giới hạn tự khai này định nghĩa trực tiếp phạm vi đóng góp của luận văn: chuyển sang nền tảng thực nghiệm FedBR [11], mở sang chế độ **feature skew**, và kiểm tra trên kiến trúc **có chuẩn hoá**. Hai nền tảng thực nghiệm khác nhau ở cách phân hoạch dữ liệu, ở tập thuật toán đối chứng, và ở công sức tinh chỉnh dành cho mỗi thuật toán, nên con số tuyệt đối của chúng không đặt cạnh nhau được. Mọi đối chiếu giữa chương này và Chương 5 vì vậy được phát biểu ở **mức cơ chế**, chẳng hạn một hiện tượng có lặp lại ở cả hai nền tảng hay không, chứ không ở mức giá trị tăng từ con số này lên con số kia. Chương 4 phát biểu nguyên tắc này thành một quy tắc đo cụ thể.

---

## Tài liệu tham khảo (khối Chương 3)

> Tiếp nối danh mục 1–16 của `02_chuong2.md`. Ba mục mới: [17] là công trình của tác giả theo IR#9, [18] và [19] là hai kết quả cổ điển mà mục 3.5 dựa vào. Các mục [1]–[16] không lặp lại ở đây; Chương 3 trích tới [1], [2], [3], [4], [9], [11] và [15] theo đúng số của danh mục đó.

[17] V. T. Kiệt, N. T. Cầm, "When Does Classifier Calibration Reproduce Under Non-IID Federated Learning? A Controlled Study on a Faithful Flower Stack," Trường Đại học Công nghệ Thông tin, ĐHQG-HCM. `[CẦN ĐIỀN theo IR#9: tên hội nghị, năm, trạng thái accepted/published, DOI hoặc chỉ mục]`
[18] B. Efron, "The Efficiency of Logistic Regression Compared to Normal Discriminant Analysis," *Journal of the American Statistical Association*, vol. 70, no. 352, pp. 892–898, 1975.
[19] A. Y. Ng, M. I. Jordan, "On Discriminative vs. Generative Classifiers: A Comparison of Logistic Regression and Naive Bayes," *NeurIPS*, 2001.

---

## Ghi chú thi hành — đọc trước khi chép vào Word

**1. Không còn tham chiếu mục trong thân bài.** Bản đầu tiên của khối 23/09 còn 13 chỗ dạng `§3.4`, `§3.5.1`, `§3.2.1`. Bản này đã gỡ hết theo ba cách: (a) chỗ nào tham chiếu chỉ để thay cho một lý do thì **viết lý do ra**; (b) chỗ nào cần chỉ đường đọc thì dùng lời (*"phần sau của chương"*, *"mục trước"*, *"hai mục cuối chương"*); (c) chỗ nào trỏ sang chương khác thì dùng **cấp chương** (*"Chương 4"*, *"Chương 5"*, *"Chương 6"*). Phép thử khi rà lại: lệnh `rg "§" ` chạy trên thân bài phải ra **0**. Tham chiếu tới phương trình và bảng vẫn giữ, vì cả hai đều tra được qua danh mục, và `00_outline.md` §7.4 ghi rõ đó là ngoại lệ có chủ ý.

**2. Vì sao chọn $\theta$ chứ không phải $w$ cho tham số mô hình.** Lỗi cần sửa là $\omega$ mang hai nghĩa. Đổi sang $w$ không đóng được lỗi đó một cách an toàn vì hai lý do. Thứ nhất, ở Times New Roman 13 in nghiêng, *w* và *ω* trông rất gần nhau, nên một công thức chứa cả $f_i(w)$ lẫn $\omega \circ \phi$ tái tạo đúng kiểu nhầm mà ta đang gỡ. Thứ hai, $w$ cần được để dành: mục 3.4.2 nói về **vector trọng số theo từng lớp** của tầng cuối và về chuẩn $\ell_2$ của chúng, và Ch.4 mục 4.5.5 đăng ký ghi nhận đại lượng ấy, nên $w_c$ là ký hiệu tự nhiên cho nó. Bản này dùng ba ký hiệu cho ba thứ: $\theta$ cho tham số mô hình, $\omega$ cho bộ phân lớp theo `00_outline.md` §7.1, và $w_c$ cho vector trọng số của lớp $c$.

**3. Ch.2 cần đổi $\omega$ thành $\theta$ ở ba chỗ.** Ch.2 mục 2.1.1 hiện dùng $\omega$ theo nghĩa tham số mô hình: trong câu *"mô hình tham số $\omega$"*, trong phương trình (2.1), và ở $\omega_t$ cùng $\omega_{t+1}$. Ch.2 **không** dùng $\omega$ theo nghĩa bộ phân lớp ở bất kỳ đâu, và Ch.1, Ch.4, Ch.5, Ch.6 không dùng $\omega$ lần nào. Nếu để nguyên thì cùng một chữ cái đổi nghĩa khi người đọc bước từ (2.1) sang chương này. Số phương trình (2.1) giữ nguyên, chỉ đổi chữ cái bên trong. Kèm theo, `00_outline.md` §7.1 cần thêm hàng cho $\theta$ và $w_c$.

**4. Bảng đối chiếu số trích dẫn cũ sang mới.** Dùng khi so bản này với bản 16/09 phía trên, hoặc khi rà bản Word.

| Bản 16/09 | Bản này | Nguồn |
|---|---|---|
| [1] | **[2]** | FedAvg |
| [3] | **[4]** | Hsu, Qi, Brown — đổi cả nguồn, xem mục 5 |
| [12] | **[9]** | Mixup |
| [13] | **[1]** | FedMix, khung MAFL |
| [18] | **[11]** | FedBR |
| [44] | **[17]** | công trình của tác giả |
| [45], [46] | **[18], [19]** | Efron; Ng, Jordan |

**5. Mục 3.2.2 đổi nguồn, không chỉ đổi số.** Bản 16/09 gán quy ước $\mathrm{Dir}(\alpha\cdot p)$ cho NIID-Bench. Quy ước ấy là của Hsu, Qi và Brown; NIID-Bench dùng dạng chuyển vị. Bản này nêu cả hai và nói rõ chỗ khác nhau, khớp với Ch.2 mục 2.1.3.

**6. Con số $\approx 2{,}09$ góc hiệu dụng là con số có định nghĩa.** Mục 3.2.3 định nghĩa $n_{\text{eff}}$ là nghịch đảo tổng bình phương của $q_i^{\text{rot}}$, rồi lấy kỳ vọng dưới $\mathrm{Dir}(1{,}0 \cdot u)$ trên mười góc. Ước lượng bằng mô phỏng $2\times10^5$ lần rút cho $2{,}09$ với độ lệch chuẩn $0{,}80$, tái lập con số $\approx 2{,}08$ đã đăng ký ở IR#7. Nếu hội đồng hỏi, đây là phép tính kiểm lại được trong vài dòng.

**7. ✅ Quy ước $eta$ của Bảng 3.3 đã tra xong; ghi chú cũ đóng.** Bản toàn văn của [17] ghi *"We follow the controlled methodology of NIID-Bench"* cùng $eta \in \{0{,}05;\ 0{,}1;\ 0{,}3\}$, nên $eta$ là nồng độ **mỗi thành phần**, lấy mẫu trên trục **client** cho từng lớp, với 60 client. Caption Bảng 3.3 nay ghi đủ bộ ba, và **mọi tham số Dirichlet trong chương đã ghi đủ bộ ba**.

Hai con số khác cũng đã đối chiếu trực tiếp với bản toàn văn trong lượt này: $-1{,}86 \pm 0{,}79$ với ba hạt giống $-2{,}19 / -0{,}95 / -2{,}43$, và số hạng bậc hai $pprox 10^{-4}$ (nguồn ghi $0{,}013\%$) tại $\lambda = 0{,}05$ và tại khởi tạo. Cả hai khớp với những gì chương đang viết.

**8. Ba bảng của chương đã được đánh số** là Bảng 3.1, Bảng 3.2 và Bảng 3.3, caption đặt trên bảng theo `00_outline.md` §7.4, tự đủ nghĩa và giải thích mọi ký hiệu. Thân bài gọi bằng số bảng. Bảng trong khối trạng thái đầu file là siêu dữ liệu cho người viết, không đánh số, và sẽ bị gỡ khi kết xuất bản nộp.

**9. Việc còn lại ở file khác.**

- **Ch.5 mục 5.2.2** hiện lặp lại gần trọn vẹn lập luận $\lambda(1{-}\lambda)$ của mục 3.3.4. Theo `00_outline.md` §7.6, cắt mục đó về chỉ còn quan sát mã nguồn cộng một câu trỏ về (3.5), và để phần dẫn xuất cùng cách đọc công thức đã công bố ở lại Chương 3.
- **`00_outline.md` §3.1**: chú thích lại dòng `loss3 = Σ(λ·grad·x̄_g)/n`. Dòng ghi tắt ấy đọc như thể hệ số là $\lambda$, vì nó không nói `grad` là đạo hàm của `loss1` đã nhân trọng số.
- **`00_outline.md` §7.1 và §5.1**: quy ước $\alpha_{\text{rot}}$ ở đó viết theo nồng độ **mỗi thành phần** (mặc định $\approx 0{,}1$), còn mã nguồn, Chương 3 và Chương 4 dùng nồng độ **tổng** (mặc định $1{,}0$). Lệch đúng một hệ số bằng 10. Sửa dàn bài trước khi ai đó điền bảng P1–P3 ở Ch.5 mục 5.1.1, và nhớ rằng dưới quy ước của chương này, quét về phía nhẹ hơn nghĩa là $\alpha_{\text{rot}}$ tăng.

---

# PHIÊN BẢN CHỈNH SỬA — 24/09/2026

> **CÁCH ĐỌC.** Chỉ-append; mọi phần phía trên giữ nguyên. Khối này **chỉ thay mục 3.6**. Các mục 3.1–3.5 và danh mục tài liệu tham khảo của bản 23/09 vẫn là bản hiện hành. Khi chép vào Word: lấy mục 3.1–3.5 từ bản 23/09 và mục 3.6 từ khối này. Bản Word hiện **chưa có** mục 3.6.
>
> **Việc đã làm:**
> 1. Đoạn *"Thứ nhất"*: cận trên −0,53 đổi thành **−0,52**, ghi rõ là phép tính của luận văn trên ba hiệu theo hạt giống, và nêu ba hiệu đó để người đọc tính lại được. Lý do: cận trên không có trong bài [17] (khoảng tin cậy bị cắt vì giới hạn trang). −0,53 là kết quả tính từ trung bình và độ lệch chuẩn đã làm tròn; −0,52 là kết quả tính từ ba số theo hạt giống. Xem `INDEX_ma-nguon-va-ket-qua.md` F2 và `00_outline.md` IR#2.
> 2. Điền tên hội nghị và trạng thái của [17] vào chỗ trống IR#9; DOI vẫn để trống. Danh mục tài liệu tham khảo mục [17] cũng cần điền theo `INDEX_ma-nguon-va-ket-qua.md` §2.
>
> ⚠️ **Chưa sửa, chờ học viên chốt:** câu *"Đây là kết quả về chính cơ chế mà luận văn nghiên cứu"* cần một hạn định. Stack Flower của [17] tính số hạng Taylor nhỏ hơn công thức 10 lần, xem `INDEX_ma-nguon-va-ket-qua.md` F1 và khối bổ sung cuối `04_chuong4.md`.

## 3.6. Kết quả nền từ công trình đã công bố của tác giả

> ⚠️ **IR#9 — còn thiếu trước khi nộp:** DOI hoặc chỉ mục của [17] (chưa có, bài chưa lên kỷ yếu); tuyên bố tái sử dụng ở đây và trong Lời cam đoan; văn bản xác nhận của đồng tác giả; đối chiếu điều khoản tái sử dụng của nhà xuất bản; khai báo tỉ lệ trùng lắp dự kiến **trước** khi quét. Tên hội nghị và trạng thái đã điền theo `INDEX_ma-nguon-va-ket-qua.md` §2.

Mục này dựa trên công trình [17], được chấp nhận đăng tại 2026 10th IEEE Symposium on Wireless Technology & Applications (ISWTA 2026) `[CẦN ĐIỀN: DOI khi có]`, do chính học viên thực hiện với đồng tác giả là cán bộ hướng dẫn. Nội dung được sử dụng lại ở đây theo khai báo tái sử dụng nêu trong Lời cam đoan.

Công trình đó khảo sát có kiểm soát nhóm phương pháp hiệu chuẩn bộ phân lớp và nhóm tăng cường trung bình, trên nền tảng Flower với mô hình huấn luyện từ đầu, dưới **lệch phân phối nhãn**. Bốn kết quả của nó tạo thành nền cho luận văn này.

**Thứ nhất, cơ chế tăng cường trung bình không mang lại cải thiện đo được trên nền tảng đó.** Ở cấu hình chính của công trình đó, gồm phân hoạch hai lớp mỗi client, 60 client với 15 client tham gia mỗi vòng, 500 vòng truyền thông, backbone VGG không dùng chuẩn hoá theo lô, và một mẫu trung bình đại diện cho mỗi lô, mức chênh của FedMix so với FedAvg trên ba hạt giống là $-1{,}86$ điểm phần trăm với độ lệch chuẩn mẫu $0{,}79$ điểm; ba hiệu theo từng hạt giống là $-2{,}19$, $-0{,}95$ và $-2{,}43$. Từ ba hiệu này, cận trên của khoảng tin cậy $95\%$ một phía là $-0{,}52$ điểm, nên khả năng có cải thiện bị loại trừ. Cận trên này do luận văn tính; [17] chỉ báo cáo trung bình, độ lệch chuẩn và ba giá trị theo hạt giống. Đây là kết quả về **chính cơ chế** mà luận văn nghiên cứu, và nó xác lập nửa label skew của câu trả lời.

Bốn biến thể mở rộng khác cũng được khảo sát trong công trình đó: hai biến thể của phép ghép cặp có ý thức về lớp, một hiệu chỉnh bậc hai trong không gian đầu vào, và một phép biến đổi trong không gian đặc trưng. Cả bốn được nguồn gắn nhãn tường minh là **thăm dò**, và hai trong số đó chỉ chạy một hạt giống và chưa tinh chỉnh. Nhãn thăm dò được giữ nguyên ở mọi chỗ luận văn trích dẫn chúng, vì mức bằng chứng của chúng thấp hơn hẳn kết quả thứ nhất.

**Thứ hai, mức cải thiện phụ thuộc ngân sách và có thể đổi dấu.** Cùng một phương pháp hiệu chuẩn, ở đây là CCVR, cho những con số trái dấu nhau tuỳ ngân sách mẫu ảo mỗi lớp $M_c$ và tuỳ mức nghiêm trọng của lệch nhãn.

**Bảng 3.3.** Mức chênh độ chính xác của CCVR so với đường cơ sở, theo ngân sách mẫu ảo mỗi lớp $M_c$ và theo mức nghiêm trọng của lệch phân phối nhãn, đo trong [17]. $M_c$ là số đặc trưng ảo sinh ra cho mỗi lớp để huấn luyện lại tầng phân lớp; $\beta$ là nồng độ Dirichlet theo quy ước của NIID-Bench [3] mà công trình đó tuân theo, tức nồng độ **mỗi thành phần**, lấy mẫu trên trục **client** cho từng lớp, với 60 thành phần ứng với 60 client; nồng độ càng nhỏ thì lệch càng nặng. Đơn vị của cột cuối là điểm phần trăm.

| Ngân sách $M_c$ | Mức skew | Chênh so với đường cơ sở |
|---|---|---|
| 100 | $\beta = 0{,}1$ | $+0{,}29$ |
| 100 | $\beta = 0{,}3$ | $\mathbf{-0{,}76}$ |
| 2000 | $\beta = 0{,}1$ | $+0{,}97$ |
| 2000 | $\beta = 0{,}05$ | $+4{,}36 \pm 0{,}51$ |

Vế $-0{,}76$ là vế quan trọng nhất của bảng: ở ngân sách mẫu ảo thiếu, phương pháp làm mô hình **kém đi**. Đọc theo cặp hàng cũng thấy dấu của mức chênh phụ thuộc đồng thời vào cả hai biến: giữ $M_c$ cố định mà đổi $\beta$ thì dấu đảo, và giữ $\beta$ cố định mà tăng $M_c$ thì biên độ đổi theo. Một con số đơn lẻ vì vậy không mô tả được phương pháp, và mức cải thiện phải được báo cáo như một **đường đặc tuyến**, tức đồ thị mức cải thiện theo lượng thông tin được phép chia sẻ, thay cho một giá trị đo tại một điểm ngân sách duy nhất. Chương 4 xây giao thức đo trên nguyên tắc này, và trục $(\lambda, M)$ của luận văn là đối ứng trực tiếp của trục $M_c$ ở đây.

**Thứ ba, thiên lệch của bộ phân lớp là định hướng.** Đây là kết quả đã trình bày ở mục trước, nơi tỉ lệ chuẩn $\ell_2$ giữa lớp lớn nhất và lớp nhỏ nhất chỉ vào khoảng $1{,}10$ đến $1{,}17$ trong khi hiệu chuẩn lại tầng cuối đổi recall rất mạnh.

**Thứ tư, công trình đó tự khai ba giới hạn ngoại vi.** Phạm vi bằng chứng gồm một họ kiến trúc, một phân phối ảnh $32\times32$, và **một loại lệch phân phối duy nhất là label skew**. Nguồn cũng nêu rõ rằng backbone không dùng chuẩn hoá theo lô là giả thiết chịu lực cho phần phân tích Gaussian.

Ba giới hạn tự khai này định nghĩa trực tiếp phạm vi đóng góp của luận văn: chuyển sang nền tảng thực nghiệm FedBR [11], mở sang chế độ **feature skew**, và kiểm tra trên kiến trúc **có chuẩn hoá**. Hai nền tảng thực nghiệm khác nhau ở cách phân hoạch dữ liệu, ở tập thuật toán đối chứng, và ở công sức tinh chỉnh dành cho mỗi thuật toán, nên con số tuyệt đối của chúng không đặt cạnh nhau được. Mọi đối chiếu giữa chương này và Chương 5 vì vậy được phát biểu ở **mức cơ chế**, chẳng hạn một hiện tượng có lặp lại ở cả hai nền tảng hay không, chứ không ở mức giá trị tăng từ con số này lên con số kia. Chương 4 phát biểu nguyên tắc này thành một quy tắc đo cụ thể.

---

# YÊU CẦU SỬA — 24/09/2026 (lượt 2) · Chương 3 chỉ giữ lý thuyết

> **Căn cứ:** quyết định 24/09 (`00_outline.md` §1.5). Kết quả trên nền tảng Flower là kết quả của luận văn và được trình bày ở **Chương 5 mục 5.2**. Chương 3 không trích bài hội nghị và không chứa số đo của luận văn.
>
> **Hệ quả cho các khối phía trên:**
> - **Mục 3.6 bị bỏ hẳn**, cả bản 23/09 lẫn khối `PHIÊN BẢN CHỈNH SỬA — 24/09/2026` ngay phía trên. Nội dung chuyển sang `05_chuong5.md` mục 5.2. Hai khối đó giữ tại chỗ để tra lịch sử; **không chép vào Word**.
> - Mục 3.3.6 bản 23/09 (số hạng bậc hai, "một phép đo trong [17]") cũng thuộc diện này. Word chưa có mục đó, nên **không chép vào Word**. Số đo tương ứng nằm ở Ch.5 mục 5.2.2.
>
> **Cách dùng bảng.** Cột *Tìm trong Word* là cụm gõ vào Ctrl+F. Cột *Trước* chép nguyên văn từ bản Word ngày 24/09. Bản trích văn bản không giữ được công thức, nên chỗ có công thức ghi `⟨công thức⟩` và giữ nguyên công thức đó trong Word. Đoạn nào phải viết lại cả đoạn thì bảng trỏ tới khối S1 hoặc S2 ngay dưới bảng.

| # | Mục | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 3.1.1, đoạn "Mô hình được tách thành hai phần", **vế cuối** | `hai mục cuối chương xác định đó là thành phần nào` | …nó tập trung ở một trong hai thành phần, và hai mục cuối chương xác định đó là thành phần nào, theo cơ chế gì. | …nó tập trung ở một trong hai thành phần. Hai mục cuối chương nêu các giả thuyết về thành phần đó và về cơ chế hình thành thiên lệch; Chương 5 kiểm tra chúng bằng số đo. | Chương 3 không còn số đo |
| 2 | 3.1.1, đoạn ký hiệu $w_c$, **vế cuối** | `phần phân tích cơ chế ở cuối chương` | …là đại lượng trung tâm của phần phân tích cơ chế ở cuối chương. | …là đại lượng trung tâm của phần phân tích cơ chế ở Chương 5. | Như trên |
| 3 | 3.3.4, đoạn "Ánh xạ sang cài đặt", **câu cuối** | `ở đó nó là một chỗ mà mã và lý thuyết khớp nhau` | Chương 5 dùng quan sát này làm mốc đối chiếu cho phần kiểm toán mã nguồn, ở đó nó là một chỗ mà mã và lý thuyết khớp nhau. | Có một chỗ không khớp: số hạng thứ ba trong mã được lấy trung bình trên lô hai lần, nên đi vào mục tiêu với hệ số nhỏ hơn ⟨công thức: λ(1−λ)⟩ một thừa số bằng kích thước lô. Chương 4 trình bày hệ quả của sai lệch này đối với phép cô lập số hạng Taylor, và Chương 5 ghi nó vào danh mục kiểm toán. | Câu cũ sai một nửa: hệ số λ(1−λ) đúng, nhưng phép chuẩn hoá theo lô thì không (`INDEX_ma-nguon-va-ket-qua.md` F1) |
| 4 | 3.4.1, đoạn cuối, **vế cuối** | `mục tiếp theo làm việc đó bằng một kết quả lý thuyết cổ điển` | …nên phạm vi hiệu lực của nó cần được phát biểu cẩn thận; mục tiếp theo làm việc đó bằng một kết quả lý thuyết cổ điển. | …nên phạm vi hiệu lực của nó cần được phát biểu cẩn thận; mục 3.5 làm việc đó bằng một kết quả lý thuyết cổ điển. | Lỗi có sẵn: mục ngay sau là 3.4.2, không phải kết quả cổ điển |
| 5 | **3.4.2, tiêu đề** | `Thiên lệch ở bộ phân lớp là thiên lệch định hướng` | Thiên lệch ở bộ phân lớp là thiên lệch định hướng | Thiên lệch ở bộ phân lớp: độ lớn hay hướng | Tiêu đề cũ khẳng định một kết quả đo; Chương 3 chỉ đặt câu hỏi |
| 6 | 3.4.2, đoạn 1 | `Một trực giác phổ biến cho rằng` | *(giữ nguyên)* | *(giữ nguyên)* | — |
| 7 | 3.4.2, **đoạn 2 và đoạn 3** | `Tuy nhiên, kết quả thực nghiệm mâu thuẫn` và `Một chênh lệch chuẩn ở mức dưới 20%` | Tuy nhiên, kết quả thực nghiệm mâu thuẫn với trực giác đó. Trên một backbone không dùng chuẩn hoá theo lô, tỉ lệ giữa ⟨công thức⟩ và ⟨công thức⟩ ở tầng cuối chỉ vào khoảng 1.10 đến 1.17, tức gần như đồng đều. Trong khi đó, việc hiệu chuẩn lại tầng cuối làm thay đổi độ chính xác vài điểm phần trăm và nâng recall của lớp bị phục vụ kém nhất lên rất mạnh. ‖ Một chênh lệch chuẩn ở mức dưới 20% không thể tạo ra biến thiên recall lớn như vậy nếu cơ chế là co giãn độ lớn. Kết luận là thiên lệch nằm ở hướng của ranh giới quyết định, và hiệu chuẩn xoay ranh giới chứ không co giãn nó. | **Xoá cả hai đoạn, thay bằng đoạn thứ nhất và thứ hai của khối S1** | Số đo 1,10–1,17 và phần recall chuyển sang Ch.5 mục 5.2.4 |
| 8 | 3.4.2, **đoạn 4** | `Kết luận này quan trọng với luận văn vì hai lý do` | Kết luận này quan trọng với luận văn vì hai lý do. Thứ nhất, nó xác nhận chẩn đoán mà đề tài dựa vào: … Thứ hai, nó đặt ra câu hỏi mà Chương 5 trả lời: … | **Thay cả đoạn bằng đoạn thứ ba của khối S1** | Không còn "kết luận" nào ở Chương 3 |
| 9 | 3.4.2, **đoạn 5** | `Phạm vi của kết luận cần được nêu kèm` | Phạm vi của kết luận cần được nêu kèm: nó được đo trên một họ kiến trúc không dùng chuẩn hoá theo lô, và nguồn tự cảnh báo rằng… | **Xoá cả đoạn** | Chuyển sang Ch.5 mục 5.2.4; cụm "nguồn tự cảnh báo" coi bài hội nghị là nguồn ngoài |
| 10 | 3.5.2, đoạn 1, **câu cuối** | `xác nhận thứ hạng này` | Đo lường trong [17] xác nhận thứ hạng này: head LDA dạng đóng cho mức cải thiện cao nhất, còn các phương án phân biệt tiệm cận nhưng không vượt. | Chương 5 kiểm tra thứ hạng này bằng thực nghiệm trên chính bài toán huấn luyện lại tầng cuối. | Không trích bài hội nghị. Thêm nữa, trong danh mục Word [17] là Ng–Jordan, nên câu cũ đang trích sai nguồn |
| 11 | 3.5.2, **đoạn 3** | `Chế độ mẫu của phép đo cũng thuộc về phát biểu` | Chế độ mẫu của phép đo cũng thuộc về phát biểu. Phép đo trong [17] thực hiện ở ⟨công thức⟩, tức số mẫu ảo dùng để huấn luyện lại tầng cuối chỉ gấp khoảng bốn lần số chiều đặc trưng. Đây là chế độ mẫu hữu hạn, … như số liệu ở cuối chương cho thấy. | **Thay cả đoạn bằng khối S2** | Bỏ trích [17] và bỏ trỏ tới "cuối chương". Con số cụ thể của tỉ số chuyển sang Ch.5 |

### S1 — thân mới của mục 3.4.2, sau đoạn "Một trực giác phổ biến…"

Trực giác này là một giả thuyết đo được, và có một giả thuyết cạnh tranh với nó. Theo giả thuyết thứ nhất, thiên lệch nằm ở độ lớn: chuẩn $\ell_2$ của các vector trọng số theo lớp chênh nhau rõ rệt, và co giãn lại các chuẩn ấy là đủ để sửa phần lớn sai lệch. Theo giả thuyết thứ hai, thiên lệch nằm ở hướng của ranh giới quyết định: chuẩn của các vector trọng số gần như bằng nhau, nhưng ranh giới giữa các lớp bị xoay về phía những lớp chiếm đa số tại chỗ.

Hai giả thuyết để lại hai dấu vết khác nhau. Nếu thiên lệch nằm ở độ lớn, tỉ số giữa $\max_c \lVert w_c \rVert_2$ và $\min_c \lVert w_c \rVert_2$ phải xa 1. Nếu thiên lệch nằm ở hướng, tỉ số ấy gần 1, vậy mà hiệu chuẩn lại tầng cuối vẫn làm recall của lớp kém nhất đổi mạnh; một chênh lệch chuẩn nhỏ không thể tạo ra biến thiên recall lớn nếu cơ chế chỉ là co giãn. Hai đại lượng này đo được trên cùng một mô hình, và Chương 5 đo cả hai.

Việc phân định quan trọng với luận văn vì hai lý do. Mục tiêu của đề tài là tăng cường đặc trưng tại các vùng ranh giới quyết định để giảm sai lệch nhãn, và mục tiêu đó chỉ có cơ sở nếu thiên lệch thực sự nằm ở ranh giới, tức giả thuyết thứ hai đúng. Khi đó câu hỏi tiếp theo là đòn bẩy trộn trung bình có xoay được ranh giới ấy không, hay chỉ tác động lên những chiều ít mang thông tin.

### S2 — đoạn thay thế đoạn 3 của mục 3.5.2

Chế độ mẫu cũng thuộc về phát biểu. Gọi $M_c$ là số mẫu ảo sinh cho mỗi lớp và $d$ là số chiều đặc trưng; tỉ số $M_c/d$ cho biết tầng cuối được huấn luyện lại trên bao nhiêu mẫu so với số chiều cần ước lượng. Khi tỉ số này nhỏ, mô hình ở chế độ mẫu hữu hạn, nơi khoảng cách giữa hai họ bộ phân lớp còn đo được; kết quả tiệm cận của Efron dự đoán khoảng cách ấy thu hẹp khi tỉ số tăng. Thứ hạng đo được ở một ngân sách mẫu ảo vì vậy không ngoại suy sang các ngân sách khác, và bản thân ngân sách mẫu ảo có thể làm đổi dấu mức cải thiện, như Chương 5 cho thấy.

*(Trong Word: $M_c$, $d$ và $M_c/d$ nhập bằng công cụ công thức.)*

**Tự kiểm lối viết trên S1 và S2:**
- không có dấu `—` chêm;
- một khuôn tương phản (*"hay chỉ tác động lên…"*), là câu hỏi nghiên cứu chứ không phải câu chốt;
- không có cụm sáo, không có câu rào.

Sau khi đoạn 5 của mục 3.4.2 bị xoá, Chương 3 không còn câu rào nào ngoài câu ở mục 3.5.1 *"Nó không phải một chặn cứng ở mọi cỡ mẫu."*; câu đó thuộc phát biểu toán học, không tính.
