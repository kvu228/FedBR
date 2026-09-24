# CHƯƠNG 5 — KẾT QUẢ THỰC NGHIỆM

> **KHỐI TRẠNG THÁI** · 16/09/2026
>
> | Mục | Trạng thái | Chờ |
> |---|---|---|
> | 5.1 | `[BẢN NHÁP]` — bảng cấu hình cần điền sau `make probe` | — |
> | 5.2 | `[BẢN NHÁP ĐẦY ĐỦ]` — danh mục kiểm toán đã xong; bảng tái hiện chờ số liệu | E2 |
> | 5.3 – 5.8 | `[KHUNG]` | E1, E2, E3, E6 |
> | 5.9 | `[KHUNG]` | tất cả |
>
> ⛔ **IR#10 — Không điền số minh hoạ, số ước lượng, hay số "dự kiến" vào bất kỳ ô nào.** Mục nào chưa có dữ liệu thì để nguyên `[CHỜ SỐ LIỆU: <id>]`.
>
> Đánh số thí nghiệm ở §5.1.3 **thay thế** hệ E-id trong `00_outline.md` §5.1 (đã lỗi thời sau khi rút gọn phạm vi).

---

## 5.1. Thiết lập thực nghiệm

### 5.1.1. Cấu hình chung

| Thành phần | Giá trị | Ghi chú |
|---|---|---|
| Bộ dữ liệu | CIFAR-10 | |
| Số client | 10, tham gia toàn bộ mỗi vòng | |
| Số bước cục bộ $K$ | 50 | theo cấu hình đã đăng ký |
| Optimizer | SGD, lr $=0{,}01$ | |
| Kích thước lô cục bộ | 32 | |
| Backbone | VGG11, $d = 512$ | không dùng chuẩn hoá theo lô |
| Số vòng truyền thông | 300 (giao thức khảo sát) / 1000 (bảng đối chiếu) | §5.1.4 |
| Tần suất đánh giá | mỗi 2 vòng | |
| Chỉ số báo cáo | trung bình 5 giá trị độ chính xác cao nhất theo vòng | theo quy ước của [18] |
| Số hạt giống | 8 (cấu hình chính) / 3 (cấu hình dựng đường cong) | §4.5.3 |

Tham số lệch phân phối được ghi theo quy ước ở §3.2.2 và §3.2.3, đủ bộ ba **(vector nồng độ, trục lấy mẫu, số thành phần)**:

| Cấu hình | Tham số | Nồng độ mỗi thành phần | Trục lấy mẫu | Số thành phần |
|---|---|---|---|---|
| P0 (IID) | — | — | — | — |
| P1 | $\alpha_{\text{rot}} = $ `[điền]` | `[điền]` | góc xoay, cho từng client | 10 |
| P2 | $\alpha_{\text{rot}} = $ `[điền]` | `[điền]` | nt | 10 |
| P3 | $\alpha_{\text{rot}} = $ `[điền]` | `[điền]` | nt | 10 |
| P4 | $\alpha = 0{,}1$ | $0{,}01$ | lớp, cho từng client | 10 |

### 5.1.2. Thay đổi mã nguồn cho luận văn

Nền tảng thực nghiệm là mã nguồn công bố của [18]. Các thay đổi được liệt kê đầy đủ để có thể rà soát hoặc hoàn tác; mặc định giữ nguyên hành vi gốc trừ nơi ghi rõ.

**Bổ sung cần thiết cho thiết kế**

| # | Thay đổi | Lý do |
|---|---|---|
| **T1** | Thêm cấu hình **C** — hàm mất mát (3.7): giữ điểm đánh giá $(1{-}\lambda)\mathbf{x}_i$, bỏ số hạng gradient | §4.2; cài đặt gốc chỉ có A và B |
| **T2** | Tham số hoá $M$ (số ảnh gộp mỗi mẫu đại diện) | §4.4; giá trị gốc là hằng số, và [13] không công bố giá trị này |
| **T3** | Tham số hoá $\alpha_{\text{rot}}$ (nồng độ Dirichlet trên góc xoay) | §4.3.3; giá trị gốc là hằng số |
| **T4** | Bổ sung chế độ lệch phân phối **đặc trưng thuần**: phân hoạch nhãn đều, giữ nguyên phép xoay theo client | §4.3.3, cấu hình P1–P3 |
| **T5** | **Thống nhất tập môi trường kiểm tra cho mọi cấu hình** | §4.3.4 — điều kiện cần để so sánh xuyên cấu hình |
| **T6** | Ghi nhận chuẩn $\ell_2$ theo lớp của tầng cuối, độ chính xác theo lớp, ma trận nhầm lẫn | §4.5.5 |

**Sửa lỗi chặn**

| # | Thay đổi | Lý do |
|---|---|---|
| **T7** | Bổ sung tệp khởi tạo gói thiếu trong bản phát hành | không import được nếu thiếu |
| **T8** | Gỡ hai lệnh import không sử dụng | gây lỗi mô-đun không tồn tại |
| **T9** | Thay dạng gọi `add_` đã lỗi thời trong ba lớp optimizer tuỳ biến | cảnh báo trên PyTorch 2.x; số học không đổi |
| **T10** | Nới ràng buộc nồng độ Dirichlet khi một lớp đã cạn mẫu | phiên bản PyTorch hiện tại từ chối nồng độ không dương |
| **T11** | Đăng ký các siêu tham số MLP còn thiếu cho một thuật toán | không khởi tạo được nếu thiếu |

**Thay đổi làm đổi kết quả** — cần nêu riêng

| # | Thay đổi | Lý do |
|---|---|---|
| **T12** | Sửa điều kiện kiểm tra góc xoay trong bộ dữ liệu CIFAR-10 | Chi tiết ở §5.2.3, mục D1 |

### 5.1.3. Đăng ký thí nghiệm

| ID | Nội dung | Cấu hình | Hạt giống |
|---|---|---|---|
| **E0** | Hạ tầng: T1–T12, kiểm tra khói | — | — |
| **E1** | Quét $\lambda \in \{0{,}05;\ 0{,}1;\ 0{,}2\}$, ba cấu hình A/B/C | P1, P4 | 3 |
| **E2** | Bảng chính: bốn nhánh (FedAvg, A, B, C) tại $\lambda$ khớp | P1, P4 | **8** |
| **E3** | Đường cong độ nghiêm trọng: bốn nhánh | P0, P2, P3 | 3 |
| **E4** | *(tuỳ chọn)* đối chiếu 1000 vòng | một cấu hình | 3 |
| **E5** | *(tuỳ chọn)* kiểm soát kiến trúc, backbone $d = 64$ | một cấu hình | 3 |
| **E6** | Chẩn đoán cơ chế — hậu nghiệm trên mô hình đã lưu của E2 | P1, P4 | 8 |

### 5.1.4. Giao thức số vòng

Phần khảo sát chạy ở **300 vòng** thay vì 1000. Đây là một lựa chọn có chủ đích nhằm đổi độ dài lấy số hạt giống — với cùng ngân sách tính toán, 300 vòng cho phép $n = 8$ thay vì $n = 2$, và §4.5.3 đã lập luận vì sao độ chính xác của ước lượng quan trọng hơn ở bài toán này.

Lựa chọn đó cần một hiện vật bằng chứng, và luận văn cung cấp nó thay vì viện dẫn: từ nhật ký theo vòng của lần chạy đối chiếu E4, trích thứ hạng các nhánh tại vòng 300 và tại vòng 1000, rồi đối chiếu.

`[CHỜ SỐ LIỆU: E4]` — Bảng 5.x: thứ hạng các nhánh tại vòng 300 so với vòng 1000.

Một giới hạn phải nêu kèm: bảo toàn **thứ hạng** giữa các nhánh không kéo theo bảo toàn **giá trị** của chênh lệch theo cặp. Vì đại lượng trung tâm của luận văn là một chênh lệch có thể ở mức dưới một điểm phần trăm, hiện vật trên chỉ hỗ trợ kết luận về thứ tự, không hỗ trợ kết luận về độ lớn ở 1000 vòng.

---

## 5.2. Tái hiện và kiểm toán tính tái lập

Mục này trình bày đóng góp C3. Nó có hai phần: xác nhận rằng nền tảng thực nghiệm tái hiện được kết quả đã công bố (§5.2.1), và danh mục các sai lệch giữa mã nguồn công bố và mô tả trong bài báo tương ứng (§5.2.2–5.2.5).

Cần nêu rõ tinh thần của mục này. Mục tiêu **không** phải phủ nhận kết quả của [18], mà là ghi nhận những chỗ mà **người đọc bài báo không thể suy ra hành vi của mã nguồn**, và ngược lại. Đây là thông tin cần thiết cho bất kỳ ai muốn xây tiếp trên nền tảng đó — trong đó có chính luận văn này.

### 5.2.1. Tái hiện

`[CHỜ SỐ LIỆU: E2]` — Bảng 5.x: độ chính xác tái hiện được so với giá trị công bố, cột CIFAR-10.

### 5.2.2. Một xác nhận âm tính

Trước khi liệt kê các sai lệch, cần ghi nhận một chỗ mà mã nguồn và mô tả lý thuyết **khớp nhau**, vì nó xác định chuẩn mực để đọc phần còn lại.

Số hạng gradient trong cấu hình B được cài đặt với hệ số $\lambda(1{-}\lambda)$, chứ không phải $\lambda$. Thoạt nhìn đây có vẻ là một sai lệch so với công thức rút gọn in trong [13]. Nhưng dẫn xuất ở §3.3.4 cho thấy $\lambda(1{-}\lambda)$ mới là **hệ số đúng** của khai triển Taylor bậc nhất: thừa số $(1{-}\lambda)$ kế thừa từ trọng số của số hạng thứ nhất trong (3.3). Cài đặt vì vậy đúng, và công thức in trong bài báo là dạng viết gọn, mơ hồ ở chỗ $\partial\ell/\partial\mathbf{x}$ là đạo hàm của số hạng đã nhân trọng số hay của hàm mất mát thuần.

Tương tự, việc cài đặt chỉ lấy gradient của số hạng ứng với nhãn thật $y_i$ mà không lấy của số hạng ứng với nhãn mềm $\bar y_g$ cũng đúng: số hạng thứ hai là $O(\lambda^2)$ theo (3.5) và được bỏ một cách hợp lệ.

Việc nêu xác nhận này có hai mục đích. Thứ nhất, nó cho thấy quá trình kiểm toán không chỉ đi tìm lỗi. Thứ hai, nó minh hoạ rằng một số "sai lệch" biểu kiến thực ra là hệ quả của việc bài báo viết gọn công thức — và chỉ có thể phân định bằng cách **tự dẫn xuất lại**, không phải bằng cách đối chiếu ký hiệu.

### 5.2.3. Ba sai lệch trọng tâm

**D1 — Điều kiện kiểm tra góc xoay bắt cả trường hợp góc bằng không.**

Bộ dữ liệu xoay phân biệt hai loại môi trường: môi trường huấn luyện, nhận một giá trị rỗng để báo hiệu "lấy mẫu góc theo phân phối của client", và môi trường kiểm tra, nhận một góc cố định trong $\{0°, 15°, \ldots, 135°\}$. Điều kiện kiểm tra trong bản phát hành bắt cả giá trị rỗng **và** giá trị $0$. Hệ quả là môi trường kiểm tra ở $0°$ — tức ảnh không xoay — bị thay bằng một tập ảnh xoay ngẫu nhiên.

Chỉ số "trung bình trên 10 môi trường kiểm tra" do đó được tính trên chín góc cố định cộng một môi trường ngẫu nhiên. Ảnh hưởng giới hạn ở một phần mười số môi trường kiểm tra và **không** chạm tới môi trường huấn luyện.

Hai chi tiết xác nhận đây là một lỗi sơ suất chứ không phải lựa chọn thiết kế: lớp bộ dữ liệu tương ứng cho CIFAR-100 trong cùng tệp viết điều kiện đúng; và mô tả trong phụ lục của [18] nói rõ các môi trường kiểm tra dùng góc cố định.

Đây là thay đổi T12 — thay đổi duy nhất trong luận văn làm đổi số liệu so với mã gốc. Vì lỗi chỉ ảnh hưởng môi trường kiểm tra, mức chênh lệch đo được bằng cách **đánh giá lại một mô hình đã lưu** trên tập kiểm tra đã sửa, không cần huấn luyện lại.

`[CHỜ SỐ LIỆU: E2]` — Bảng 5.x: chênh lệch chỉ số trước và sau T12.

**D2 — Trọng số của số hạng proximal bị ghi đè trong mỗi bước.**

Một thuật toán đối chứng có trọng số proximal được khai báo như một siêu tham số, có tuỳ chọn dòng lệnh tương ứng, và được [18] mô tả là đã tinh chỉnh trên lưới ba giá trị. Tuy nhiên, lớp optimizer tương ứng gán lại trọng số này thành một hằng số ở **đầu mỗi lần gọi bước cập nhật**, xoá giá trị được truyền từ hàm khởi tạo.

Hệ quả: trọng số luôn bằng hằng số đó bất kể cấu hình, và lưới tinh chỉnh được công bố không thể thực hiện được bằng mã đã phát hành. Cùng dạng lỗi này xuất hiện ở hai lớp optimizer tuỳ biến khác trong cùng tệp.

Đây là một ví dụ về **siêu tham số giả**: có khai báo, có tuỳ chọn cấu hình, có lưới quét được công bố — và cả ba đều không có hiệu lực. Nó cũng minh hoạ một giới hạn của kiểm toán chỉ dựa trên giao diện cấu hình: tài liệu tái lập được viết trước đó cho chính kho mã này đã ghi hướng dẫn quét lưới cho siêu tham số này, và hướng dẫn đó không hoạt động.

**D3 — Dữ liệu giả được dựng một lần, trong khi cấu hình mặc định của bài báo là dựng lại mỗi vòng.**

[18] mô tả cấu hình mặc định là sinh một lô dữ liệu giả **ở mỗi vòng truyền thông**, và nêu riêng một biến thể chỉ sinh một lần ở đầu quá trình huấn luyện nhằm giảm chi phí truyền thông; biến thể này được khảo sát ở một hình riêng trong bài.

Mã nguồn phát hành hiện thực **biến thể** chứ không phải cấu hình mặc định: dữ liệu giả được dựng một lần trước vòng lặp, và nhánh dựng lại mỗi vòng tồn tại dưới dạng mã đã bị chú thích.

Hai hệ quả. Thứ nhất, mã phát hành không tạo ra được cấu hình đã sinh ra bảng kết quả chính của bài báo. Thứ hai, ablation so sánh hai tần suất dựng lại không tái lập được, vì chỉ một trong hai nhánh còn hoạt động.

### 5.2.4. Nhóm sai lệch làm suy yếu thuật toán đối chứng

Bốn phát hiện dưới đây có chung một hệ quả: chúng làm các thuật toán đối chứng trong bảng kết quả chính hoạt động dưới mức mà mô tả trong bài báo hàm ý.

| # | Phát hiện |
|---|---|
| **D4** | **Mô hình cục bộ của vòng trước trong một thuật toán tương phản không bao giờ được cập nhật.** Thuộc tính được gán ở vòng lặp huấn luyện và thuộc tính được đọc trong hàm cập nhật có **tên khác nhau**. Thuộc tính được đọc chỉ được tạo một lần lúc khởi tạo, không nằm trong optimizer, và không tham gia phép tổng hợp — nên nó là một mạng khởi tạo ngẫu nhiên, đóng băng suốt quá trình huấn luyện. Số hạng đối lập của hàm mất mát tương phản do đó được tính với đặc trưng nhiễu |
| **D5** | **Cấu hình optimizer không đồng nhất giữa các thuật toán đối chứng.** Một nhóm thuật toán kế thừa momentum $0{,}9$ từ lớp cơ sở; ba thuật toán khác dùng SGD thuần và **không có đường nào để bật momentum** — các biến thể tương ứng tồn tại dưới dạng mã đã chú thích. Ngoài ra, phụ lục của [18] nêu momentum $0{,}9$ cho các thí nghiệm dùng một kiến trúc nhất định, nhưng thuật toán được đề xuất trong chính bài báo đó không thể nhận cấu hình này |
| **D6** | **Một thuật toán đối chứng luôn áp dụng phép trộn mẫu**, bất kể tuỳ chọn tương ứng có được bật hay không. Với một lô mỗi client, phép ghép cặp suy biến thành trộn **trong nội bộ lô**. Hàng kết quả tương ứng vì vậy không phải thuật toán được ghi tên mà là tổ hợp của nó với phép trộn |
| **D7** | **Một thuật toán đối chứng chỉ nhận một nửa số bước cập nhật** cho phần trích xuất đặc trưng và phần phân lớp, do lịch xen kẽ giữa hai thành phần. Qua toàn bộ quá trình huấn luyện, nó nhận một nửa số bước SGD so với mọi thuật toán khác, trong khi bảng kết quả trình bày chúng như thể cùng ngân sách |

> ⚠️ **Giới hạn bắt buộc của kết luận.** Bốn phát hiện trên cho thấy các thuật toán đối chứng bị suy yếu theo bốn cơ chế độc lập. Nhưng **không có cơ sở để định lượng** mỗi cơ chế đóng góp bao nhiêu vào khoảng cách được báo cáo, và luận văn **không** đưa ra bất kỳ ước lượng nào về điều đó. Việc định lượng đòi hỏi chạy lại từng thuật toán đối chứng sau khi sửa từng lỗi — nằm ngoài phạm vi. Kết luận đúng mức là: **khoảng cách được báo cáo trong bảng kết quả chính không được đo trên các thuật toán đối chứng ở trạng thái mà mô tả trong bài báo hàm ý.**

### 5.2.5. Các sai lệch khác

| # | Phát hiện |
|---|---|
| **D8** | **Hai quy ước Dirichlet khác nhau được dùng trong cùng một tệp.** Nhánh CIFAR-100 truyền vào một vector chưa chuẩn hoá — tức nồng độ mỗi thành phần; nhánh CIFAR-10 truyền vào một vector đã chuẩn hoá — tức nồng độ tổng. Cùng một hằng số xuất hiện ở hai chỗ nhưng mang hai ý nghĩa khác nhau, chênh nhau một hệ số bằng số lớp. Thêm vào đó, việc cắt bớt vector khi một lớp cạn mẫu làm **tổng nồng độ thay đổi động** trong quá trình phân hoạch. Đây là biểu hiện cụ thể của vấn đề ký hiệu đã nêu ở §2.1.2 |
| **D9** | **Tuỳ chọn lưu mô hình theo mốc đánh giá ghi đè cùng một tệp** ở mỗi lần gọi. Tên tuỳ chọn hàm ý lưu nhiều mốc; hành vi thực tế là chỉ giữ mốc cuối cùng. Đây là lý do phân tích cơ chế ở §5.7 sử dụng mô hình ở vòng cuối (§4.5.5) |
| **D10** | **Một thuật toán đối chứng có trong bảng kết quả của bài báo nhưng không chạy được** bằng mã phát hành: hàm cập nhật của nó yêu cầu một đối số mà vòng lặp huấn luyện không truyền, và lớp đó vắng mặt trong danh sách thuật toán khả dụng |
| **D11** | **Một thuật toán đối chứng căn chỉnh logit thay vì căn chỉnh đặc trưng.** Đại lượng được đưa vào hàm mất mát căn chỉnh là đầu ra của tầng phân lớp, có số chiều bằng số lớp, trong khi phụ lục của [18] mô tả phương pháp này là căn chỉnh **đặc trưng** |
| **D12** | **Lớp bộ dữ liệu xoay cho CIFAR-100 không gọi hàm biến đổi**, nên dữ liệu CIFAR-100 **không được xoay** bất chấp tên lớp, và mười môi trường kiểm tra của nó giống hệt nhau. Ngoài phạm vi CIFAR-10 của luận văn, nhưng thuộc cùng loại phát hiện |
| **D13** | **Số lượng ảnh gộp cho mỗi mẫu đại diện là hằng số ở ba hàm dựng dữ liệu khác nhau**, và [13] **không công bố giá trị của tham số này**. Đây là thiếu thông tin trong bài báo hơn là mâu thuẫn giữa mã và bài báo, nhưng nó khiến tham số nén — vốn là tham số bảo mật của cơ chế — không kiểm chứng được |

### 5.2.6. Một giả thuyết chưa kết luận

Vòng lặp huấn luyện khởi tạo mỗi mô hình cục bộ bằng một lần khởi tạo ngẫu nhiên độc lập, và vòng đồng bộ ngay sau đó không ghi kết quả trở lại danh sách mô hình — tức nó không có hiệu lực. Trong một lần chạy thông thường, phép tổng hợp ở bước đầu tiên che lấp vấn đề này. Nhưng ở cấu hình không truyền thông, phép tổng hợp chỉ diễn ra một lần trên các mô hình khởi tạo khác nhau, và mô hình toàn cục không được cập nhật nữa.

Đáng chú ý, hàng kết quả tương ứng trong [18] cho ba bộ dữ liệu đều **xấp xỉ mức đoán ngẫu nhiên**. Điều này nhất quán với hành vi trên, và không nhất quán với cách hiểu thông thường về cấu hình đó — huấn luyện cục bộ không truyền thông thường cho độ chính xác cao hơn đáng kể.

Luận văn **không kết luận** về điểm này, vì mã phát hành không có chế độ tương ứng nên không thể xác định các tác giả đã chạy cấu hình nào. Phép kiểm chứng cần thiết — chạy cấu hình không truyền thông và đối chiếu — được nêu như một việc bỏ ngỏ.

---

## 5.3. Cô lập số hạng khai triển Taylor

*Trả lời câu hỏi nghiên cứu thứ nhất.*

`[CHỜ SỐ LIỆU: E2]`

**Nội dung dự kiến:**
- Bảng chính: $\Delta_{\text{Taylor}}$ (4.1) tại $\lambda$ khớp, hai cấu hình P1 và P4, $n = 8$, kèm khoảng tin cậy $95\%$
- Bảng đối chiếu: $\Delta_{\text{gốc}}$ (4.2) và $\Delta_{\text{đánh giá}}$ (4.3); kiểm tra tính cộng tính và báo cáo phần dư
- Kiểm định họ giả thuyết chính (§4.5.4) với hiệu chỉnh Holm; nếu không có ý nghĩa, báo cáo TOST với biên $\pm 1{,}5$ điểm phần trăm
- Độ lệch chuẩn của chênh lệch theo cặp **đo được trên nền tảng này**, đối chiếu với giá trị $1{,}2$ dùng để định cỡ thiết kế
- Đường cong hội tụ

## 5.4. Hai giá trị của trọng số trộn

`[CHỜ SỐ LIỆU: E1, E2]`

**Nội dung dự kiến:**
- Đường cong độ chính xác theo $\lambda$ cho ba cấu hình A, B, C tại P1 và P4
- Giá trị $\lambda$ tối ưu của từng cấu hình
- $\Delta$ tại $\lambda$ khớp so với $\Delta$ tại $\lambda$ tối ưu riêng — và **khoảng cách giữa hai con số** (§4.4.3)

## 5.5. Trục độ nghiêm trọng

`[CHỜ SỐ LIỆU: E2, E3]`

**Nội dung dự kiến:**
- Độ suy giảm (4.4) của FedAvg tại từng cấu hình
- Đồ thị $\Delta_{\text{Taylor}}$ theo $\mathrm{Drop}$, với cả hai loại lệch phân phối trên cùng trục hoành
- Báo cáo tách biệt chỉ số trong phân phối và ngoài phân phối (§4.3.4)

## 5.6. Mặt vận hành và chi phí tài nguyên

`[CHỜ SỐ LIỆU: E1]`

**Nội dung dự kiến:**
- Ba đại lượng của §4.4.2: độ chính xác, chi phí truyền thông, độ nén
- Thời gian mỗi bước và bộ nhớ đỉnh cho từng cấu hình
- *(nếu chạy E5)* kiểm soát kiến trúc với $d = 64$

## 5.7. Phân tích cơ chế

`[CHỜ SỐ LIỆU: E6]`

**Nội dung dự kiến:**
- Chuẩn $\ell_2$ theo lớp của tầng cuối; đối chiếu với tỉ lệ $1{,}10$–$1{,}17$ ghi nhận ở §3.4.2
- Độ chính xác theo lớp và recall của lớp bị phục vụ kém nhất
- Câu hỏi trung tâm: cơ chế trộn trung bình có **xoay** ranh giới quyết định hay chỉ tác động lên các chiều ít mang thông tin
- Mọi đối chiếu với Chương 3 phát biểu ở **mức cơ chế** (§4.5.2)

## 5.8. Biên độ tương đối của số hạng gradient

`[CHỜ SỐ LIỆU: E2]`

**Nội dung dự kiến:** biên độ của số hạng (III) so với số hạng (I) ở các mốc vòng khác nhau — phân biệt "số hạng không mang thông tin" với "số hạng có biên độ quá nhỏ ở cấu hình đang xét" (§4.2.3).

## 5.9. Tổng hợp và thảo luận

`[CHỜ: tất cả]`

**Nội dung dự kiến:**
- Trả lời từng câu hỏi nghiên cứu, mỗi câu một đoạn, **kèm điều kiện hiệu lực**
- **Threats to validity** — theo mẫu của [44], liệt kê tường minh các giới hạn ngoại vi
---

# YÊU CẦU SỬA — 24/09/2026 · thêm mục 5.2: thực nghiệm dưới lệch nhãn trên nền tảng Flower

> **Căn cứ:** quyết định 24/09 (`00_outline.md` §1.5). Các thực nghiệm trên stack Flower là thực nghiệm của luận văn. Chúng được trình bày ở một mục riêng, đặt **trước** các thực nghiệm trên mã nguồn FedBR, để Chương 5 đi theo trình tự: lệch nhãn trên nền tảng thứ nhất, rồi mở rộng sang lệch đặc trưng trên nền tảng thứ hai. Thân bài không trích bài hội nghị.
>
> Mọi con số trong mục 5.2 đã được đối chiếu lại với tệp kết quả thô ngày 24/09. Đường dẫn ở khối *Truy vết* cuối mục; khối đó không chép vào Word.

## Đổi cấu trúc chương

| Word hiện tại | Sau khi sửa | Việc trong Word |
|---|---|---|
| 5.1 Thiết lập thực nghiệm | 5.1 Thiết lập thực nghiệm | giữ tiêu đề; thêm một câu mở đầu (hàng dưới) |
| — | **5.2 Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower** | chèn tiêu đề cấp 2 mới, cùng năm tiêu đề cấp 3 từ 5.2.1 tới 5.2.5 |
| 5.2 Tái hiện và kiểm toán tính tái lập | 5.3 Tái hiện và kiểm toán tính tái lập | Word tự đánh lại số nếu tiêu đề dùng kiểu Heading tự đánh số |
| *(các mục sau trong `05_chuong5.md`)* | dịch số thêm một: 5.3→5.4, …, 5.9→5.10 | chỉ ảnh hưởng file `.md`; Word chưa có các mục này |

Câu mở đầu đề xuất cho mục 5.1 trong Word, đặt ngay dưới tiêu đề:

> Luận văn chạy thực nghiệm trên hai nền tảng. Các thực nghiệm dưới lệch phân phối nhãn chạy trên một nền tảng mô phỏng dựng bằng Flower, với thiết lập riêng trình bày ở mục 5.2.1. Các thực nghiệm còn lại, gồm toàn bộ phần lệch phân phối đặc trưng, chạy trên mã nguồn FedBR với thiết lập dưới đây.

⚠️ Các bảng của mục 5.2 mang số **Bảng 5.1–5.5**. Bảng nào ở các mục sau được đánh số khi chép vào Word thì bắt đầu từ Bảng 5.6.

---

# PHIÊN BẢN CHỈNH SỬA — 24/09/2026 · mục 5.2 (mới)

> Thân mục từ tiêu đề `## 5.2.` tới hết mục 5.2.5 là phần chép vào Word.
>
> **Tự kiểm §7.7** trên thân mục:
> - không có dấu `—` chêm, không có cụm sáo, không viện dẫn bài hội nghị hay đề cương;
> - AI#1: hai khuôn tương phản, ở 5.2.1 (*"kiểm tra tính nhất quán … không phải một phép kiểm chứng độc lập"*) và 5.2.2 (*"… vì phạm vi, không phải vì …"*);
> - AI#4: một câu rào, cuối mục 5.2.4, về backbone không chuẩn hoá.

## 5.2. Thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower

Mục này đo ba điều dưới lệch phân phối nhãn: FedMix có cải thiện so với FedAvg hay không; mức cải thiện của nhóm hiệu chuẩn tầng phân lớp từ thống kê lớp phụ thuộc thế nào vào ngân sách mẫu ảo; và thiên lệch của tầng phân lớp nằm ở độ lớn hay ở hướng. Các thực nghiệm chạy trên một nền tảng mô phỏng dựng bằng Flower, mô hình huấn luyện từ đầu. Nền tảng này khác mã nguồn FedBR ở cách phân hoạch, số client, backbone và tập thuật toán đối chứng, nên con số của mục này không đặt cạnh con số của các mục sau; các mục sau chỉ đối chiếu với nó ở mức cơ chế.

### 5.2.1. Thiết lập

**Bảng 5.1.** Thiết lập thực nghiệm trên nền tảng Flower. $\beta$ là nồng độ Dirichlet **mỗi thành phần**, lấy mẫu trên trục **client** cho từng lớp, với 60 thành phần ứng với 60 client; nồng độ càng nhỏ thì lệch càng nặng. $M_c$ là số đặc trưng ảo sinh cho mỗi lớp khi huấn luyện lại tầng phân lớp; $d$ là số chiều đặc trưng.

| Thành phần | Giá trị |
|---|---|
| Khung | Flower, chế độ mô phỏng |
| Dữ liệu | CIFAR-10; CINIC-10 chỉ dùng cho phép so sánh các head hiệu chuẩn |
| Client | 60, mỗi vòng chọn 15 |
| Huấn luyện cục bộ | 2 epoch, lô 10, SGD với tốc độ học 0,01 giảm theo hệ số 0,999 mỗi vòng, không momentum, không weight decay |
| Backbone | VGG sửa đổi theo phụ lục bài báo FedMix [1]: 6 tầng tích chập và 3 tầng kết nối đầy đủ, không chuẩn hoá theo lô, $d = 512$ |
| Phân hoạch | hai lớp mỗi client, 500 vòng (phép so sánh FedMix); Dirichlet $\beta \in \{0{,}05;\ 0{,}1;\ 0{,}3\}$, 150 vòng (hiệu chuẩn tầng phân lớp) |
| FedMix | $\lambda = 0{,}05$; mỗi client gửi một ảnh trung bình của toàn bộ dữ liệu cục bộ kèm nhãn mềm; mỗi lô cục bộ ghép với một ảnh trung bình rút ngẫu nhiên |
| Hiệu chuẩn | CCVR [7] với $M_c \in \{100;\ 2000\}$, biến đổi Tukey 0,5, huấn luyện lại tầng cuối 10 epoch; head LDA dùng hiệp phương sai gộp co về đường chéo với hệ số 0,01 |
| Hạt giống | 42, 43, 44 |

Chỉ số của phép so sánh FedMix là độ chính xác cao nhất theo vòng trên tập kiểm tra. Chỉ số của phép hiệu chuẩn là chênh lệch độ chính xác trước và sau khi hiệu chuẩn, đo trên cùng một mô hình đã huấn luyện. Mọi dấu $\pm$ trong mục này là độ lệch chuẩn mẫu của ba hiệu theo cặp, mỗi hiệu ứng với một hạt giống.

Bài báo FedMix không công bố mã nguồn. Nền tảng được đối chiếu với bản cài đặt mã mở của DevPranjal, chạy trên cùng cấu hình với hạt giống 42. Hai bên chênh nhau khoảng 3 điểm phần trăm ở độ chính xác tuyệt đối (FedAvg 65,81% so với 68,69%; FedMix 63,67% so với 66,50%), nhưng hiệu theo cặp gần như trùng: −2,14 và −2,19 điểm. Vì bản cài đặt đó cũng là mốc mà nền tảng được hiệu chỉnh theo, phép đối chiếu này là một kiểm tra tính nhất quán, không phải một phép kiểm chứng độc lập.

### 5.2.2. FedMix so với FedAvg

**Bảng 5.2.** Độ chính xác cao nhất theo vòng (%) của FedAvg và FedMix trên CIFAR-10, phân hoạch hai lớp mỗi client, 500 vòng, backbone VGG không chuẩn hoá ($d = 512$), $\lambda = 0{,}05$. Cột cuối là hiệu theo cặp FedMix − FedAvg, đơn vị điểm phần trăm. Hàng cuối: trung bình ± độ lệch chuẩn mẫu, $n = 3$.

| Hạt giống | FedAvg | FedMix | Hiệu |
|---|---|---|---|
| 42 | 68,69 | 66,50 | −2,19 |
| 43 | 67,42 | 66,47 | −0,95 |
| 44 | 64,74 | 62,31 | −2,43 |
| | | | **−1,86 ± 0,79** |

FedMix kém FedAvg ở cả ba hạt giống. Với ba quan sát, riêng dấu của hiệu không đủ làm bằng chứng: khi không có hiệu ứng, xác suất để ba hiệu cùng dấu đã là 0,25. Phát biểu dựa vào khoảng tin cậy thì chặt hơn. Với $t_{0{,}95;\,2} = 2{,}920$, cận trên của khoảng tin cậy 95% một phía là −0,52 điểm, nên ở cấu hình này khả năng FedMix cải thiện được loại trừ.

Kết luận phụ thuộc vào chỉ số. Lấy độ chính xác ở vòng cuối thay cho vòng tốt nhất, ba hiệu là −3,55, −4,49 và +0,59: trung bình vẫn âm nhưng một hạt giống đổi dấu.

Bản cài đặt này có cùng đặc điểm với mọi bản cài đặt FedMix mã mở mà luận văn đối chiếu: số hạng Taylor được lấy trung bình trên lô hai lần, nên đi vào mục tiêu với hệ số nhỏ hơn công thức (3.15) mười lần ở lô 10 ảnh (Chương 4, mục 4.2.3). Kết quả ở Bảng 5.2 vì vậy là kết quả về FedMix như nó đang được cài đặt. Số hạng Taylor ở đúng biên độ của (3.15) được đo ở các mục sau.

Nền tảng này cũng cho phép đo biên độ của số hạng bậc hai trong khai triển Taylor so với số hạng bậc nhất, ở $\lambda = 0{,}05$. Tại khởi tạo ngẫu nhiên, trên 10 ảnh CIFAR-10, tỉ số là khoảng $1{,}3 \times 10^{-4}$. Trên ba mô hình đã huấn luyện 150 vòng với Dirichlet $\beta = 0{,}05$, tỉ số giữa số hạng bậc hai và số hạng bậc nhất là 0,039, 0,224 và 0,025 theo từng hạt giống. Như vậy số hạng bậc hai lớn lên hai đến ba bậc khi mô hình được huấn luyện. Luận văn không khảo sát nhánh bậc hai vì phạm vi, không phải vì số hạng đó không đáng kể.

**Bảng 5.3.** Hai biến thể thăm dò của FedMix. C1: mỗi client gửi một ảnh trung bình cho từng lớp, thay cho một ảnh trung bình trên toàn bộ dữ liệu cục bộ. C1+C2: C1 cộng thêm quy tắc ghép cặp chọn ảnh trung bình khác lớp có tích vô hướng với gradient theo đầu vào lớn nhất. Hiệu theo cặp so với FedAvg, trung bình ± độ lệch chuẩn mẫu, $n = 3$, đơn vị điểm phần trăm; cột cuối là cận trên của khoảng tin cậy 95% một phía.

| Biến thể | Phân hoạch, số vòng | Hiệu theo hạt giống | Trung bình | Cận trên |
|---|---|---|---|---|
| C1 | hai lớp mỗi client, 500 | −2,22 / −0,55 / −2,94 | −1,90 ± 1,23 | +0,16 |
| C1+C2 | Dirichlet $\beta = 0{,}3$, 150 | −1,36 / −2,95 / −0,60 | −1,64 ± 1,20 | +0,38 |

Cả hai biến thể đều âm về trung bình, nhưng cận trên của cả hai đều dương, nên không loại trừ được khả năng có cải thiện. Chúng được giữ nhãn thăm dò và không tham gia kết luận của luận văn.

### 5.2.3. Hiệu chuẩn tầng phân lớp và ngân sách mẫu ảo

CCVR ước lượng trung bình và hiệp phương sai của đặc trưng theo từng lớp, sinh đặc trưng ảo từ các phân phối Gauss đó, rồi huấn luyện lại riêng tầng phân lớp. Số đặc trưng ảo mỗi lớp, $M_c$, là ngân sách của phương pháp.

**Bảng 5.4.** Mức chênh độ chính xác của CCVR so với mô hình trước hiệu chuẩn, trên CIFAR-10, 150 vòng, theo ngân sách mẫu ảo $M_c$ và nồng độ Dirichlet $\beta$ (quy ước ở Bảng 5.1). Hàng $\beta = 0{,}05$ gồm ba hạt giống (+3,88 / +4,30 / +4,90); các hàng còn lại chỉ có hạt giống 42. Đơn vị: điểm phần trăm.

| $M_c$ | $\beta$ | Mức chênh |
|---|---|---|
| 100 | 0,1 | +0,29 |
| 100 | 0,3 | −0,76 |
| 2000 | 0,1 | +0,97 |
| 2000 | 0,05 | +4,36 ± 0,51 |

Ở ngân sách 100 mẫu mỗi lớp, CCVR cải thiện mô hình ở $\beta = 0{,}1$ nhưng làm mô hình kém đi ở $\beta = 0{,}3$. Cùng một phương pháp cho hai dấu ngược nhau chỉ vì mức lệch thay đổi. Hai hàng $M_c = 100$ và hai hàng $M_c = 2000$ không so được trực tiếp với nhau: chúng dùng hai lần huấn luyện backbone khác nhau, và tốc độ học của bước huấn luyện lại cũng đổi từ 0,01 sang 0,001 cùng lúc với ngân sách. Kết luận rút ra được là giới hạn: một con số đo tại một điểm ngân sách không mô tả được phương pháp. Mức cải thiện phải được báo cáo như một đường đặc tuyến theo ngân sách, và Chương 4 xây giao thức đo trên nguyên tắc đó.

**Bảng 5.5.** Bốn cách huấn luyện lại tầng phân lớp từ cùng một thống kê lớp, trên cùng mô hình đã huấn luyện 150 vòng với Dirichlet $\beta = 0{,}05$, $M_c = 2000$, $d = 512$, tức $M_c/d \approx 3{,}9$. Hiệu so với mô hình trước hiệu chuẩn, trung bình ± độ lệch chuẩn mẫu, $n = 3$; độ chính xác trước hiệu chuẩn là 54,66 / 54,55 / 48,14%. Hàng "hội tụ" và dòng "LDA − Newton" lấy từ một lượt chạy riêng trên cùng ba hạt giống, trong đó LDA đạt +6,39 ± 1,24. CINIC-10 chứa ảnh của CIFAR-10, nên cột CINIC-10 chỉ để đọc mô tả, không dùng để suy luận thống kê. Đơn vị: điểm phần trăm.

| Head | CIFAR-10 | CINIC-10 |
|---|---|---|
| LDA dạng đóng | +6,45 ± 1,29 | +5,93 ± 0,33 |
| CCVR | +4,41 ± 1,19 | +4,26 ± 0,12 |
| Newton cross-entropy, một bước | +2,98 ± 1,04 | +1,95 ± 3,17 |
| Bậc nhất, một bước | +0,36 ± 0,12 | +0,24 ± 0,08 |
| Newton cross-entropy, hội tụ | +6,14 ± 1,37 | +5,65 ± 0,28 |
| Bậc nhất tốt nhất (tốc độ học 0,1, 2000 bước) | +5,29 ± 1,09 | +5,32 ± 0,29 |
| **LDA − Newton hội tụ** | **+0,25 ± 0,18** | **+0,35 ± 0,06** |

Thứ hạng khớp với dự đoán của Chương 3. Trên tác vụ ảo sinh từ phân phối Gauss, head LDA dạng đóng cho mức cải thiện cao nhất. Các head phân biệt, khi được tối ưu tới hội tụ, tiến sát LDA nhưng vẫn thấp hơn ở cả ba hạt giống trên CIFAR-10 (0,31 / 0,39 / 0,05 điểm). Phép đo ở $M_c/d \approx 3{,}9$, tức chế độ mẫu hữu hạn, nên thứ hạng này không ngoại suy sang các ngân sách mẫu ảo khác.

### 5.2.4. Dạng thiên lệch của tầng phân lớp

Hai giả thuyết của Chương 3 được kiểm tra trên ba mô hình của hàng $\beta = 0{,}05$, $M_c = 2000$ ở Bảng 5.4, trước và sau khi hiệu chuẩn bằng CCVR.

Tỉ số giữa chuẩn $\ell_2$ lớn nhất và nhỏ nhất của các vector trọng số theo lớp ở tầng cuối là 1,099, 1,147 và 1,172 theo từng hạt giống, tức các chuẩn gần như bằng nhau. Độ lệch ở số hạng tự do cũng nhỏ: trung bình trị tuyệt đối của $b_c$ khoảng 0,16, so với chuẩn trung bình của $w_c$ khoảng 1,17. Trong khi đó, hiệu chuẩn lại tầng cuối nâng recall của lớp kém nhất từ 18,0% lên 61,9% (lớp tàu thuỷ, hạt giống 42), từ 16,9% lên 61,8% (lớp chó, hạt giống 43), và từ 22,3% lên 48,6% (lớp hươu, hạt giống 44). Lớp kém nhất được xác định sau khi đo, riêng cho từng hạt giống.

Một chênh lệch chuẩn dưới 20% không thể tạo ra biến thiên recall cỡ 26 đến 45 điểm nếu thiên lệch nằm ở độ lớn. Số đo vì vậy ủng hộ giả thuyết thứ hai: thiên lệch nằm ở hướng của ranh giới quyết định, và hiệu chuẩn xoay ranh giới ấy. Phát hiện này đo trên một họ kiến trúc không dùng chuẩn hoá theo lô, và một backbone có chuẩn hoá có thể định hình lại nó; kiểm soát kiến trúc được đăng ký ở dạng tuỳ chọn trong mục 5.1.

### 5.2.5. Những gì chuyển sang các mục sau

Ba kết quả của mục này được mang sang phần còn lại của chương, ở mức cơ chế. Dưới lệch phân phối nhãn, FedMix như đang được cài đặt không cải thiện so với FedAvg. Mức cải thiện của nhóm hiệu chuẩn tầng phân lớp phụ thuộc ngân sách mẫu ảo và có thể đổi dấu. Thiên lệch của tầng phân lớp mang tính định hướng. Các mục sau kiểm tra, trên mã nguồn FedBR và dưới cả lệch phân phối đặc trưng, xem ba hiện tượng này có lặp lại hay không; con số của hai nền tảng không được đem so với nhau.

---

## Truy vết — không chép vào Word

Gốc đường dẫn: `C:\Users\KietVu\Testplace\uit-msc-dp-adaptive-fedmix\`. Tra thêm ở `INDEX_ma-nguon-va-ket-qua.md` §3.

| Bảng / số liệu | Tệp thô | Tái tính |
|---|---|---|
| Bảng 5.1 | `configs/cifar10/paper_k2.yaml`, `configs/cifar10/fedmix.yaml`, `configs/cifar10/dirichlet_sweep/ccvr_b005_paperhp.yaml`, `runs/runs/e2/config_resolved.yaml` | — |
| Đối chiếu DevPranjal | `runs/_archive/hydra_reference/results/cifar10_{0,1}/`; `docs/reproductions/REPRODUCTION_CIFAR10_GATE.md:57–69` | — |
| Bảng 5.2 | `runs/_archive/fedmca_closed/negative_k2/{fedavg,fedmix}_cifar10_k2{,_s43,_s44}/<ts>/metrics.csv`; timestamp đúng ở chỉ mục §3 | `python -m scripts.aggregate_negatives_k2 --log-root runs/_archive/fedmca_closed/negative_k2` |
| Cận trên −0,52 / +0,16 / +0,38 | tính từ các hiệu theo hạt giống, $t_{0,95;2} = 2{,}920$ | chỉ mục F2 |
| Số hạng bậc hai tại khởi tạo | `docs/reproductions/REPRODUCTION_FEDMCA_C1_GATE.md:55` | `scripts/check_t2_magnitude.py` |
| Số hạng bậc hai trên mô hình đã huấn luyện (0,039 / 0,224 / 0,025) | `runs/gate_2nd/second_order_gate.json`, trường `trained.seed4x.m1.ratio_B_over_A` | `experiments/run_second_order_gate.py` |
| Bảng 5.3 | C1: `negative_k2/fedmca_c1_cifa10_k2` (s42), `fedmca_c1_cifar10_k2_{s43,s44}`; C1+C2: `runs/fedtc/*_b030_screen` (s42), `runs/_archive/fedmca_closed/*_screen_s43/s44` | C1: script trên; C1+C2: tự tính từ `metrics.csv` |
| Bảng 5.4 | $M_c=100$: `runs/_archive/void_superseded/fedtc4/ccvr_cifar10_dir_b0{10,30}_screen/`; $M_c=2000$: `runs/fedtc5/ccvr_b010_paperhp`, `runs/fedtc5/ccvr_b005_paperhp{,_s43,_s44}` (`calibration_metrics.json`) | `scripts/make_paper_figures.py` `make_fig1` |
| Bảng 5.5 | `runs/runs/e2/head_methods_summary.json`, `runs/runs/e2_cinic/…`; hàng hội tụ: `runs/runs/e3/e3_fair_baselines.json`, `runs/runs/e3_cinic/…` | `experiments/run_head_methods.py`, `experiments/run_e3_fair_baselines.py` |
| Mục 5.2.4 | `runs/fedtc5/ccvr_b005_paperhp*/calibration_metrics.json`: `head_weight_l2_before`, `recall_before`, `recall_after`, `head_bias_before` | `make_paper_figures.py` `make_fig2` |

⚠️ **Ba điểm cần biết khi bảo vệ:**
- Hàng $M_c = 100$ của Bảng 5.4 nằm trong thư mục `void_superseded`: đây là các lượt screen cũ, được giữ vì là lượt duy nhất ở ngân sách đó.
- Mục 5.2.3 nói thẳng rằng ngân sách và tốc độ học huấn luyện lại đổi cùng lúc giữa hai nhóm hàng. Không viết lại theo kiểu "trên cùng một checkpoint" (chỉ mục F6).
- Chỉ số "tỉ số bậc hai / bậc nhất trên mô hình đã huấn luyện" lấy nhánh Hessian (`ratio_B_over_A`). Không dùng các tỉ số có hậu tố `_gn`, vì chúng chuẩn hoá không nhất quán (chỉ mục F4).
