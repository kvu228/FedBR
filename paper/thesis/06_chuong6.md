# CHƯƠNG 6 — KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

> **KHỐI TRẠNG THÁI** · 16/09/2026
>
> | Mục | Trạng thái | Chờ |
> |---|---|---|
> | 6.1 | `[KHUNG]` | toàn bộ Chương 5 |
> | 6.2 | `[KHUNG]` | §5.9 |
> | 6.3 | `[BẢN NHÁP ĐẦY ĐỦ]` | — |
> | 6.4 | `[BẢN NHÁP ĐẦY ĐỦ]` | — |
>
> ⚠️ **Khi viết §6.1–6.2, áp dụng nguyên tắc phòng thủ ở `PLAN_ke-hoach-8-tuan.md` §8:** đóng góp C1 gồm ba thành phần và **không được treo vào thành phần (c)**. Không viết câu nào dạng "luận văn lần đầu cô lập số hạng Taylor".

---

## 6.1. Kết luận

`[CHỜ: Chương 5]`

**Cấu trúc dự kiến:** đối chiếu từng mục tiêu cụ thể đã đăng ký trong đề cương với kết quả đạt được, theo thứ tự các câu hỏi nghiên cứu ở §1.2.

## 6.2. Đóng góp

`[CHỜ: §5.9]`

**Cấu trúc dự kiến:** phát biểu lại C1 (ba thành phần), C2, C3 với phạm vi hạn định, dựa trên kết quả thực tế chứ không dựa trên kế hoạch.

---

## 6.3. Hạn chế

Mục này liệt kê các giới hạn của luận văn một cách tường minh. Cách trình bày theo mẫu của [44]: nêu rõ phạm vi bằng chứng thay vì để người đọc tự suy ra.

### 6.3.1. Giới hạn của thiết kế thực nghiệm

**Không có cấu hình kết hợp đồng thời hai loại lệch phân phối.** Các cấu hình P1–P3 là lệch phân phối đặc trưng thuần, P4 là lệch phân phối nhãn thuần. Luận văn vì vậy **không kết luận gì về tương tác** giữa hai loại: liệu tác động của chúng cộng tính, cộng hưởng, hay triệt tiêu nhau đều nằm ngoài phạm vi. Một thiết kế giai thừa đầy đủ đòi hỏi lưới hai chiều và chi phí tính toán vượt ngân sách của luận văn.

**Số hạng khai triển Taylor chỉ được cô lập tại một điểm đánh giá.** Lưới ở §3.3.5 có bốn ô; luận văn chạy ba, bỏ ô D vì lý do đã nêu ở §4.2.2. Hệ quả: nếu tác động của số hạng gradient phụ thuộc vào việc mẫu trung bình có đồng thời đi vào lượt truyền xuôi hay không, thiết kế hiện tại không phát hiện được sự phụ thuộc đó.

**Chỉ một bộ dữ liệu và một họ kiến trúc trong cấu hình chính.** Toàn bộ kết quả chính chạy trên CIFAR-10 với một backbone không dùng chuẩn hoá theo lô. Kiểm soát kiến trúc là tuỳ chọn trong kế hoạch; nếu nó không được thực hiện, giả thiết rằng các phát hiện độc lập với kiến trúc **chưa được kiểm tra** — và đây là một giới hạn nghiêm trọng hơn thường được nhìn nhận, vì [44] tự cảnh báo rằng một backbone có chuẩn hoá có thể định hình lại phần phân tích cơ chế mà Chương 3 dựa vào.

**Không có thí nghiệm cho tác vụ hồi quy.** Mệnh đề 4.1 cho thấy khung mở rộng được sang hồi quy ở mức thiết kế, nhưng đó là một kết quả **lý thuyết**. Không có bằng chứng thực nghiệm nào về hành vi của cơ chế ở tác vụ hồi quy.

**Không có bộ dữ liệu số lớp cao.** Kết quả không được kiểm chứng ở chế độ nhiều lớp, nơi các hiện tượng liên quan tới hình học tầng phân lớp có thể biểu hiện khác.

### 6.3.2. Giới hạn của cách mô phỏng lệch phân phối đặc trưng

Ba tính chất đã nêu ở §3.2.3 tạo thành giới hạn quan trọng nhất về tính ngoại suy của luận văn.

**Phép xoay nằm ở cực dễ của phổ dịch chuyển miền.** Nó là một biến đổi nhóm, khả nghịch, thuần hình học, và không làm thay đổi nội dung ngữ nghĩa của ảnh. Dịch chuyển miền trong triển khai thực tế — đổi cảm biến, đổi điều kiện chiếu sáng, đổi quy trình xử lý ảnh — nói chung không khả nghịch và không có cấu trúc nhóm.

**Phép biến đổi độc lập với lớp.** Góc xoay được lấy mẫu không phụ thuộc nhãn, nên mọi lớp trong một client chịu cùng một toán tử trộn. Cần ghi nhận rằng đây **không phải đặc thù của lựa chọn này**: nhiễu cộng, corruption chuẩn hoá, và phân hoạch theo nguồn thật trong các benchmark phổ biến đều độc lập với lớp. Lệch phân phối đặc trưng **phụ thuộc lớp** — nơi phép biến đổi khác nhau theo từng lớp — hầu như vắng mặt khỏi các benchmark FL chuẩn. Luận văn kế thừa giới hạn này của văn liệu chứ không tạo ra nó, nhưng vẫn phải ghi nhận nó.

**Chỉ quét được một phía của trục độ nghiêm trọng.** Cấu hình mặc định đã nằm gần cực trị nặng, nên đường cong ở §5.5 là một nhánh chứ không đối xứng.

### 6.3.3. Giới hạn của giao thức đo lường

**Trục độ nghiêm trọng là căn chỉnh vận hành, không phải căn chỉnh phân phối.** Như §4.3.2 đã nêu, độ suy giảm của FedAvg trộn lẫn độ khó của bài toán với cơ chế thất bại cụ thể của FedAvg. Hai loại lệch phân phối khác nhau có thể cho cùng một giá trị thông qua hai cơ chế khác nhau, và trục này không phân biệt được.

**Độ phân giải thống kê bị chặn.** Với $n = 8$ hạt giống, nửa rộng khoảng tin cậy khoảng một điểm phần trăm. Mọi hiệu ứng nhỏ hơn mức đó không phân giải được, và luận văn báo cáo chúng dưới dạng khoảng chứ không dưới dạng kết luận có hay không.

**Chẩn đoán cơ chế dùng mô hình ở vòng cuối.** Lựa chọn này không gây thiên lệch vì mọi cấu hình được so tại cùng một vòng, nhưng nó làm phân tích nhiễu hơn so với việc dùng mô hình ở vòng có độ chính xác cao nhất.

**Phần khảo sát chạy ở số vòng rút gọn.** Hiện vật bằng chứng ở §5.1.4 hỗ trợ kết luận về **thứ hạng** giữa các nhánh, không hỗ trợ kết luận về **độ lớn** của chênh lệch ở số vòng đầy đủ.

### 6.3.4. Giới hạn của khảo sát văn liệu

Khảo sát ở Chương 2 là khảo sát **có phạm vi**, không phải tổng quan hệ thống. Ba giới hạn cụ thể đã được nêu ở §2.6.1: tập công trình trích dẫn không được duyệt vét cạn; bản được đối chiếu của một nguồn chính là bản toàn văn trên kho tiền ấn phẩm chứ không phải bản kỷ yếu chính thức; và phần thảo luận phản biện công khai của nguồn đó không truy cập được.

Giới hạn thứ ba đáng nhắc lại ở đây: nếu phần thảo luận đó chứa một biến thể ablation đã được thực hiện theo yêu cầu phản biện, phát biểu ở §2.6.2 về sự vắng mặt của biến thể tương ứng cần điều chỉnh. Như §2.6.3 đã nêu, **đóng góp C1 được cấu trúc để không phụ thuộc vào kết quả của việc kiểm tra này**.

### 6.3.5. Giới hạn về quyền riêng tư

Luận văn **không đưa ra tuyên bố riêng tư vi phân nào**. Tham số nén $M$ được dùng như một đại lượng đại diện cho mức bảo mật, không phải một bảo đảm hình thức. Giao thức chia sẻ mẫu trung bình chỉ có tính chất không phụ thuộc phân phối lớp ở mức hệ thống. Một phân tích $(\varepsilon, \delta)$ hình thức, cũng như đánh giá trước các tấn công tái dựng dữ liệu, nằm ngoài phạm vi.

### 6.3.6. Giới hạn về môi trường triển khai

Toàn bộ thực nghiệm chạy ở chế độ **mô phỏng** trên một máy, với toàn bộ client tham gia mỗi vòng. Các yếu tố của triển khai thực tế — client rời mạng, băng thông không đồng đều, năng lực tính toán khác nhau, lịch tham gia không đồng bộ — đều không được mô hình hoá.

---

## 6.4. Hướng phát triển

Bảy hướng dưới đây được sắp theo mức độ gần với kết quả của luận văn. Bốn hướng đầu có thể thực hiện trực tiếp trên khung đã xây.

### 6.4.1. Bổ sung ô còn thiếu của lưới

Ô D ở §3.3.5 — giữ phép trộn ở đầu vào và đồng thời thêm số hạng gradient — cho phép cô lập số hạng Taylor tại **điểm đánh giá thứ hai**. Đối chiếu $\Delta_{\text{Taylor}}$ đo ở hai điểm đánh giá sẽ trả lời được câu hỏi mà thiết kế hiện tại bỏ ngỏ: tác động của số hạng gradient có phụ thuộc vào việc mẫu trung bình đồng thời đi vào lượt truyền xuôi hay không. Chi phí thấp vì cấu hình đã có trong khung.

### 6.4.2. Thí nghiệm cho tác vụ hồi quy

Mệnh đề 4.1 cung cấp nền lý thuyết đầy đủ: phép tách theo nhãn đúng sai khác một hằng số độc lập tham số, nên toàn bộ dẫn xuất và cả bốn cấu hình chuyển nguyên vẹn sang hàm mất mát bình phương. Việc còn lại là chọn một bộ dữ liệu hồi quy có phân hoạch không đồng nhất kiểm soát được, và một tập thuật toán đối chứng tương ứng.

Hướng này có giá trị vượt ngoài việc hoàn thiện phạm vi: như §4.6.1 đã lập luận, tác vụ hồi quy **không có bộ phân lớp**, nên lời giải thích cơ học quy thiên lệch về tầng phân lớp không áp dụng được. Kết quả ở hồi quy vì vậy là một phép kiểm tra tính tổng quát của chính lời giải thích đó.

### 6.4.3. Lệch phân phối đặc trưng phụ thuộc lớp

Như §6.3.2 đã nêu, các benchmark FL chuẩn hầu như chỉ dùng biến đổi độc lập với lớp. Hai tiền lệ cho biến đổi phụ thuộc lớp tồn tại trong văn liệu học máy rộng hơn — một dựa trên việc gán đặc trưng giả tương quan với nhãn, một dựa trên phân cụm trong không gian nhúng theo từng lớp — nhưng chưa được đưa vào benchmark FL dưới dạng một giao thức phân hoạch có tham số hoá liên tục.

Xây dựng một giao thức như vậy, tương tự cách tham số hoá Dirichlet đã làm cho lệch phân phối nhãn, là một đóng góp có thể bảo vệ được. Hạ tầng cho hướng này đã có sẵn một phần trong nền tảng thực nghiệm được sử dụng.

### 6.4.4. Hiệu chuẩn độ nghiêm trọng giữa các trục lệch phân phối

§4.3.1 đã nêu bài toán: hai loại lệch phân phối được điều khiển bởi hai tham số không cùng đơn vị, khiến so sánh giữa chúng không quy kết nhân quả được. Luận văn dùng một phương án vận hành thay thế và ghi nhận giới hạn của nó ở §6.3.3.

Một lời giải thật sự đòi hỏi một thước đo độ không đồng nhất **chung cho mọi loại lệch phân phối** — chẳng hạn một khoảng cách phân phối giữa các client tính trực tiếp trên dữ liệu. Có được thước đo đó thì thiết kế giai thừa ở §6.4.5 mới có nghĩa, và rộng hơn, các kết quả giữa những công bố dùng các giao thức phân hoạch khác nhau mới so sánh được.

### 6.4.5. Thiết kế giai thừa đầy đủ

Với thước đo ở §6.4.4, một lưới hai chiều {mức lệch nhãn} $\times$ {mức lệch đặc trưng} cho phép trả lời câu hỏi về **tương tác** mà §6.3.1 nêu là ngoài phạm vi. Đây cũng là khoảng trống đã xác định trong khảo sát ở §2.6.2: khảo sát skew hỗn hợp hiện có chỉ là một điểm, không phải một mặt phẳng, và không bao gồm các phương pháp can thiệp ở tầng biểu diễn.

### 6.4.6. Benchmark dịch chuyển miền thực tế

Nền tảng thực nghiệm được sử dụng đã tích hợp sẵn một số bộ dữ liệu dịch chuyển miền thật, trong đó mỗi miền là một nguồn thu thập riêng biệt. Chạy cơ chế trên các bộ này sẽ kiểm chứng xem kết luận rút ra từ phép xoay tổng hợp có chuyển sang dịch chuyển miền thật hay không — đây là kiểm soát ngoại vi trực tiếp nhất cho giới hạn ở §6.3.2.

### 6.4.7. Phân tích riêng tư hình thức

Như §6.3.5 đã nêu, luận văn không đưa ra tuyên bố riêng tư hình thức. Một phân tích $(\varepsilon, \delta)$ cho giao thức chia sẻ mẫu trung bình, kèm đánh giá thực nghiệm trước các tấn công tái dựng dữ liệu theo tham số nén $M$, sẽ biến trục $M$ ở §4.4 từ một đại lượng đại diện thành một trục đánh đổi có bảo đảm. Hướng này cũng cần thiết nếu cơ chế được cân nhắc cho triển khai thực tế.

---

## 6.5. Kết luận chung

`[CHỜ: §6.1]`

**Cấu trúc dự kiến:** một đoạn tổng kết mối quan hệ giữa ba đóng góp và câu hỏi nghiên cứu trung tâm, và một đoạn về ý nghĩa của kết quả đối với cách văn liệu Học liên kết báo cáo mức cải thiện.