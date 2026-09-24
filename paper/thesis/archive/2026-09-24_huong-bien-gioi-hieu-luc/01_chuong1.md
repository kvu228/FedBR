# CHƯƠNG 1 — GIỚI THIỆU

> **KHỐI TRẠNG THÁI** · 16/09/2026
>
> | Mục | Trạng thái |
> |---|---|
> | 1.1 – 1.4 | `[BẢN NHÁP ĐẦY ĐỦ]` — chờ tác giả chỉnh lý |
> | §1.3 | ⚠️ **Rà soát lại sau khi có kết quả Chương 5.** Phát biểu đóng góp phải phản ánh kết quả thực tế, không phải kế hoạch |
>
> ⛔ **Nguyên tắc phòng thủ (`PLAN_ke-hoach-8-tuan.md` §8):** đóng góp C1 gồm ba thành phần và **không được treo vào thành phần (c)**. Cấm mọi câu dạng "lần đầu tiên cô lập số hạng Taylor".

---

## 1.1. Lý do chọn đề tài

### 1.1.1. Bối cảnh

Học liên kết (Federated Learning) cho phép huấn luyện một mô hình dùng chung trên dữ liệu nằm rải rác ở nhiều thiết bị, mà dữ liệu đó không bao giờ rời khỏi thiết bị. Chỉ tham số mô hình được trao đổi. Kiến trúc này giải quyết đồng thời hai ràng buộc thực tế: quyền riêng tư của người dùng và băng thông hạn chế của mạng biên.

Trở ngại trung tâm của mô hình này là dữ liệu giữa các thiết bị **không phân phối đồng nhất**. Người dùng khác nhau có thói quen khác nhau, thiết bị khác nhau, môi trường thu thập khác nhau; hệ quả là mục tiêu tối ưu cục bộ của mỗi thiết bị lệch khỏi mục tiêu toàn cục. Khi mỗi thiết bị chạy nhiều bước cập nhật trước khi đồng bộ — điều cần thiết để tiết kiệm truyền thông — các mô hình cục bộ trôi về những nghiệm khác nhau, và phép trung bình của chúng không còn là một bước tiến tốt. Hiện tượng này làm chậm hội tụ, gây dao động, và hạ độ chính xác của mô hình tổng hợp.

### 1.1.2. Vì sao tăng cường dữ liệu là hướng đáng nghiên cứu

Trong các hướng khắc phục đã được đề xuất, nhóm can thiệp vào quá trình tối ưu hoá — thêm số hạng chính quy hoá, hiệu chỉnh gradient, điều chỉnh quy tắc tổng hợp — có ưu điểm là không trao đổi thêm bất kỳ thông tin nào về dữ liệu. Nhưng đó cũng là giới hạn của chúng: nếu các phân phối cục bộ thực sự khác nhau, không một thao tác nào trên quỹ đạo tối ưu hoá có thể cung cấp cho một thiết bị thông tin mà nó không bao giờ quan sát được.

Hướng **tăng cường dữ liệu** chấp nhận một đánh đổi khác: truyền thêm một lượng thông tin nhỏ về dữ liệu, đủ để mỗi thiết bị có một hình dung về phân phối toàn hệ thống, nhưng nhỏ tới mức không vi phạm ràng buộc riêng tư. Ý tưởng này đã được chứng minh là hiệu quả từ sớm — chia sẻ một tập dữ liệu nhỏ cân bằng lớp khôi phục được phần lớn độ chính xác bị mất. Vấn đề là tập chia sẻ đó gồm **dữ liệu thô**, điều đi ngược nguyên tắc nền tảng.

Toàn bộ dòng nghiên cứu sau đó có thể đọc như những nỗ lực giữ lại lợi ích ấy mà giảm mức riêng tư phải hi sinh: chia sẻ dữ liệu sinh nhân tạo, chia sẻ tri thức của mô hình thay vì dữ liệu, chia sẻ thống kê đặc trưng theo lớp, hoặc — hướng mà luận văn này nghiên cứu — **chia sẻ các mẫu đã được lấy trung bình**.

### 1.1.3. Vì sao khai triển Taylor

Cơ chế được nghiên cứu hoạt động như sau. Mỗi thiết bị tính trung bình của một số ít mẫu cục bộ, kèm nhãn mềm tương ứng, rồi chia sẻ các cặp trung bình đó. Phép lấy trung bình đóng vai trò cơ chế nén: ảnh riêng lẻ không rời thiết bị, chỉ bản đã làm mịn được chia sẻ, và số lượng ảnh được gộp là một tham số điều khiển mức nén.

Điều làm cơ chế này đáng nghiên cứu về mặt lý thuyết là cách nó sử dụng các mẫu trung bình. Cách đơn giản nhất — trộn trực tiếp mẫu cục bộ với mẫu trung bình nhận được — không cần lý thuyết gì. Nhưng phương pháp tiêu biểu của họ này làm một việc tinh tế hơn: nó **khai triển Taylor bậc nhất** hàm mất mát, và kết quả là mẫu trung bình không còn đi vào đầu vào của mạng, mà chỉ đi vào qua một tích vô hướng với đạo hàm của hàm mất mát theo đầu vào.

Số hạng khai triển đó **chính là đóng góp lý thuyết của phương pháp**. Nếu nó mang thông tin, cơ chế là một cách xấp xỉ có nguyên tắc một mục tiêu không thể tính trực tiếp. Nếu nó không mang thông tin, thì cả họ phương pháp rút gọn về một ý tưởng cũ và đơn giản hơn nhiều — chia sẻ ảnh trung bình rồi trộn chúng vào — và phần "khai triển Taylor" chỉ là trang trí. Câu hỏi này chưa được trả lời một cách tách bạch, và đó là điểm xuất phát của luận văn.

### 1.1.4. Khoảng trống trong cách đo

Ngoài câu hỏi trên, có ba đặc điểm của văn liệu khiến các mức cải thiện đã công bố khó diễn giải.

**Thứ nhất, mức cải thiện phụ thuộc mạnh vào ngân sách nhưng ngân sách hiếm khi được quét.** Nhiều phương pháp trong dòng này có một tham số điều khiển lượng thông tin phụ trợ. Khi tham số đó được cố định ở một giá trị, con số báo cáo là một điểm trên một đường cong chưa biết hình dạng. Công trình đã công bố của chính tác giả cho thấy hệ quả cụ thể: một phương pháp hiệu chuẩn cho mức cải thiện dương ở ngân sách gốc nhưng **đổi dấu** khi ngân sách bị hạ.

**Thứ hai, độ mạnh của phương pháp đối chứng không đồng nhất và hiếm khi được báo cáo.** Cùng một phương pháp đo trên đối chứng chưa tinh chỉnh sẽ cho mức cải thiện lớn hơn nhiều so với đo trên đối chứng đã tinh chỉnh tốt.

**Thứ ba, hầu hết bằng chứng chỉ có ở một loại lệch phân phối.** Phần lớn công trình trong dòng này đánh giá dưới **lệch phân phối nhãn**, trong khi lệch phân phối **đặc trưng** — thiết bị khác nhau, điều kiện thu thập khác nhau — là dạng không đồng nhất phổ biến không kém trong triển khai thực tế.

### 1.1.5. Bản chất của luận văn

Luận văn này **không đề xuất một thuật toán học liên kết mới**. Nó xác định **biên giới hiệu lực** của một cơ chế đã có, bằng cách tháo rời cơ chế đó thành các thành phần đo được độc lập.

Cần nói rõ một điểm về cách đọc tên đề tài. Tên đề tài nêu kỹ thuật được nghiên cứu — tăng cường dữ liệu dựa trên khai triển Taylor — và mục tiêu tổng quát đã đăng ký là **nghiên cứu cơ sở lý thuyết** của kỹ thuật ấy. Một nghiên cứu xác định được cơ chế hoạt động trong điều kiện nào và không hoạt động trong điều kiện nào là **hoàn thành mục tiêu đó**, bất kể dấu của kết quả đo được. Trong nghiên cứu, một kết quả dự kiến không thành hiện thực là **dữ liệu**, không phải thất bại của đề tài — với điều kiện phép đo đủ chặt để kết luận có ý nghĩa.

Chính vì vậy, luận văn đặt trọng tâm vào **độ chặt của phép đo** chứ không vào việc thu được một dấu cụ thể: câu hỏi nghiên cứu được phát biểu ở dạng ước lượng kèm khoảng tin cậy thay vì dạng kiểm định nhị phân, và thiết kế thực nghiệm được xây sao cho phát biểu kết luận có giá trị bất kể giá trị đo được là bao nhiêu (§4.5.3).

---

## 1.2. Mục tiêu, đối tượng và phạm vi

### 1.2.1. Mục tiêu tổng quát

> Nghiên cứu cơ sở lý thuyết về các kỹ thuật làm phong phú không gian đặc trưng và phương pháp xấp xỉ hàm mất mát dựa trên khai triển Taylor trong môi trường học máy phân tán.

### 1.2.2. Câu hỏi nghiên cứu

| | Câu hỏi | Trả lời ở |
|---|---|---|
| **RQ1** | Số hạng khai triển Taylor bậc nhất đóng góp **bao nhiêu** vào hiệu năng, khi được tách khỏi bản thân phép trộn mẫu trung bình, ở trọng số trộn khớp nhau giữa các cấu hình? | §5.3 |
| **RQ2** | Đóng góp đó biến thiên thế nào theo **loại** và **độ nghiêm trọng** của lệch phân phối — cụ thể, kết luận thu được dưới lệch phân phối nhãn có chuyển sang lệch phân phối đặc trưng không? | §5.5 |
| **RQ3** | Đóng góp đó biến thiên thế nào theo **ngân sách** — trọng số trộn và mức nén — và đánh đổi với chi phí truyền thông ra sao? | §5.4, §5.6 |
| **RQ4** | Cơ chế nào giải thích kết quả? Thiên lệch có nằm ở **ranh giới quyết định** như giả định của đề tài không? | §5.7 |
| **RQ5** | Cơ chế có mở rộng được sang tác vụ **hồi quy** không? | §4.6 |

RQ1 là câu hỏi trung tâm. Nó được phát biểu ở dạng **"bao nhiêu"** chứ không phải **"có hay không"**, và §4.5.3 trình bày lý do: hiệu ứng cần đo có thể nhỏ hơn độ phân giải thống kê khả thi, nên một thiết kế xây quanh kiểm định nhị phân sẽ cho kết quả không kết luận được, trong khi một thiết kế xây quanh ước lượng luôn cho một phát biểu có giá trị.

RQ5 được trả lời ở **mức thiết kế** bằng một kết quả lý thuyết (Mệnh đề 4.1), không bằng thực nghiệm; §1.2.4 và §6.3 nêu rõ giới hạn này.

### 1.2.3. Đối tượng nghiên cứu

Đối tượng là **cơ chế tăng cường dữ liệu bằng mẫu trung bình đại diện kết hợp xấp xỉ hàm mất mát bằng khai triển Taylor bậc nhất**, trong bài toán học liên kết có giám sát.

Đối tượng này được tháo rời thành bốn thành phần đo được độc lập (§4.1.1): cơ chế tăng cường, ngân sách, chế độ lệch phân phối, và tác vụ cùng hàm mất mát.

### 1.2.4. Phạm vi và giới hạn

Các giới hạn dưới đây được nêu ngay từ đầu thay vì để ở cuối, vì chúng ràng buộc cách đọc mọi kết quả trong luận văn. Phần trình bày đầy đủ ở §6.3.

**Về dữ liệu và kiến trúc.** Toàn bộ kết quả chính chạy trên một bộ dữ liệu ảnh $32\times32$ với một họ kiến trúc không dùng chuẩn hoá theo lô. Kiểm soát kiến trúc là tuỳ chọn; nếu không thực hiện được, giả thiết rằng các phát hiện độc lập với kiến trúc **chưa được kiểm tra**.

**Về cách mô phỏng lệch phân phối đặc trưng.** Lệch phân phối đặc trưng được mô phỏng bằng phép xoay ảnh — một biến đổi nhóm, khả nghịch, thuần hình học, và **độc lập với lớp**. Nó nằm ở cực dễ của phổ dịch chuyển miền. Cần ghi nhận rằng tính độc lập với lớp không phải đặc thù của lựa chọn này mà là đặc điểm chung của các benchmark phổ biến (§6.3.2).

**Về thiết kế thực nghiệm.** Không có cấu hình kết hợp đồng thời hai loại lệch phân phối, nên luận văn **không kết luận gì về tương tác** giữa chúng. Số hạng khai triển chỉ được cô lập tại **một** điểm đánh giá hàm mất mát.

**Về độ phân giải thống kê.** Với số hạt giống khả thi, nửa rộng khoảng tin cậy khoảng một điểm phần trăm. Mọi hiệu ứng nhỏ hơn mức đó được báo cáo dưới dạng khoảng, không dưới dạng kết luận có hay không.

**Về tác vụ hồi quy.** Chỉ có kết quả **lý thuyết** (Mệnh đề 4.1); không có bằng chứng thực nghiệm.

**Về quyền riêng tư.** Luận văn **không đưa ra tuyên bố riêng tư vi phân nào**. Tham số nén được dùng như đại lượng đại diện cho mức bảo mật, không phải bảo đảm hình thức.

**Về môi trường.** Toàn bộ thực nghiệm chạy ở chế độ mô phỏng với toàn bộ thiết bị tham gia mỗi vòng; các yếu tố của triển khai thực tế không được mô hình hoá.

**Về so sánh.** Luận văn sử dụng hai nền tảng thực nghiệm khác nhau cho phần nền lý thuyết và phần thực nghiệm mới. Theo kỷ luật đã nêu ở §4.5.2, **không so sánh con số tuyệt đối giữa hai nền tảng**; mọi phát biểu xuyên chương đặt ở mức cơ chế.

---

## 1.3. Đóng góp của luận văn

### C1 — Đo có kiểm soát đóng góp của số hạng khai triển Taylor

Đóng góp này gồm ba thành phần, trình bày theo thứ tự **mức độ độc lập với các phát biểu về tính mới** ở §2.6.

**(a) Tái lập độc lập.** Phép đối chiếu giữa hai cấu hình của cơ chế được chạy lại trên một nền tảng thực nghiệm thứ hai, với nhiều hạt giống ngẫu nhiên và báo cáo khoảng tin cậy thay vì con số đơn lẻ. Giá trị của thành phần này nằm ở **chính việc tái lập**: trong phạm vi khảo sát ở §2.6.1, phép đối chiếu này chưa được lặp lại độc lập bởi công trình nào khác.

**(b) Đo ở trọng số trộn khớp nhau.** Công trình gốc tinh chỉnh trọng số trộn **riêng cho từng cấu hình**, rồi báo cáo chênh lệch như thể đó là hiệu ứng của cơ chế. Luận văn đo lại ở trọng số khớp, đồng thời báo cáo cả giá trị tối ưu riêng từng cấu hình, và **khoảng cách giữa hai con số** — đại lượng định lượng phần mức cải thiện thực chất đến từ ngân sách tinh chỉnh không đồng đều.

**(c) Biến thể cô lập chặt.** Bổ sung một cấu hình giữ nguyên điểm đánh giá hàm mất mát và chỉ bỏ số hạng đạo hàm, cho phép cô lập số hạng khai triển mà không đồng thời thay đổi cách mẫu trung bình đi vào mục tiêu; đồng thời mở rộng toàn bộ phép đối chiếu sang chế độ lệch phân phối đặc trưng.

Hai thành phần đầu **đứng vững độc lập** với kết quả kiểm tra ở giới hạn thứ ba của §2.6.1. Nếu kiểm tra đó cho thấy biến thể ở (c) đã từng được thực hiện ở đâu đó, thành phần này chuyển từ đóng góp về tính mới thành một **xác nhận độc lập**, và C1 giữ nguyên giá trị.

### C2 — Đo cơ chế dọc theo một trục độ nghiêm trọng chung

Luận văn đo cơ chế tại nhiều mức độ nghiêm trọng của cả hai loại lệch phân phối, và báo cáo mức cải thiện dưới dạng **đường đặc tuyến vận hành** thay vì một con số.

Khảo sát thực nghiệm được trích dẫn rộng rãi nhất về các dạng không đồng nhất **có** tách hai loại lệch phân phối, nhưng phần khảo sát chế độ hỗn hợp của nó chỉ đo bốn thuật toán, tất cả đều can thiệp ở tầng tối ưu hoá hoặc quy tắc tổng hợp; các phương pháp **chia sẻ dữ liệu** như cơ chế đang xét không có mặt. Trong phạm vi khảo sát ở §2.6.1, giả thuyết rằng hai họ phương pháp này phản ứng khác nhau với hai loại lệch phân phối chưa được kiểm định.

Để so sánh giữa các cấu hình có nghĩa, luận văn đề xuất chiếu mọi cấu hình lên một trục chung trong không gian kết quả (§4.3.2). Đây là một phép **căn chỉnh vận hành**, không thay thế bài toán hiệu chuẩn độ nghiêm trọng thật sự — giới hạn này được nêu tường minh và bài toán gốc được ghi nhận ở §6.4.4.

### C3 — Kiểm toán tính tái lập của nền tảng thực nghiệm

Luận văn lập danh mục các sai lệch giữa mã nguồn công bố của nền tảng được sử dụng và mô tả trong bài báo tương ứng (§5.2). Danh mục gồm ba sai lệch trọng tâm — một công thức được cài đặt khác dạng in trong bài, một siêu tham số được công bố là đã tinh chỉnh nhưng bị ghi đè trong mã, và một cấu hình mặc định không thực hiện được bằng mã đã phát hành — cùng bốn cơ chế độc lập làm các thuật toán đối chứng hoạt động dưới mức mà mô tả hàm ý.

Danh mục cũng ghi nhận một **xác nhận âm tính**: một chỗ mà cài đặt và lý thuyết khớp nhau, nơi một sai lệch biểu kiến hoá ra là hệ quả của việc bài báo viết gọn công thức (§5.2.2).

Kết luận của C3 được giới hạn tường minh: mã nguồn cho thấy các thuật toán đối chứng bị suy yếu, nhưng luận văn **không định lượng** mức đóng góp của từng cơ chế và không đưa ra ước lượng nào về điều đó.

---

## 1.4. Cấu trúc luận văn

**Chương 2** định vị đối tượng nghiên cứu giữa các hướng tiếp cận lân cận, và phát biểu khoảng trống mà luận văn nhắm tới, kèm phạm vi khảo sát văn liệu.

**Chương 3** trình bày nền tảng lý thuyết: bài toán học liên kết, cách mô hình hoá hai loại lệch phân phối, dẫn xuất đầy đủ của khai triển Taylor bậc nhất và bốn cấu hình sinh ra từ nó, các kết quả về thiên lệch học cục bộ, và một kết quả cổ điển về bộ phân lớp sinh so với phân biệt cùng ranh giới áp dụng của nó.

**Chương 4** trình bày khung thực nghiệm được đề xuất, định nghĩa hình thức các đại lượng được đo, thiết kế trục độ nghiêm trọng, mặt vận hành theo ngân sách, giao thức đo lường, và kết quả lý thuyết về mở rộng sang tác vụ hồi quy.

**Chương 5** trình bày kết quả: tái hiện và kiểm toán tính tái lập, rồi lần lượt trả lời các câu hỏi nghiên cứu.

**Chương 6** tổng kết, nêu các giới hạn một cách tường minh, và đề xuất bảy hướng phát triển.

---
---

# PHIÊN BẢN CHỈNH SỬA — 21/09/2026

> **CÁCH ĐỌC FILE NÀY.** Phần trên là bản nháp 16/09/2026, **giữ lại nguyên trạng để tra cứu lịch sử**. Phần dưới đây là **bản hiện hành** của Chương 1. Khi trích dẫn, đánh số trang, hay chuyển sang LaTeX/DOCX, **chỉ dùng phần dưới**.
>
> **Những gì đã đổi so với bản 16/09:**
>
> | Mục | Thay đổi |
> |---|---|
> | 1.1 | Đoạn mở do tác giả viết lại, dùng **nguyên văn**; bỏ toàn bộ tiểu mục `1.1.1`–`1.1.5`, viết liền mạch thành văn xuôi. **Rút gọn (21/09, ba lượt):** sau năm đoạn của tác giả chỉ còn **một đoạn ba câu** — số hạng Taylor là gì · nó chưa được tách riêng để đo và bằng chứng mới chỉ có ở lệch nhãn · luận văn xác định biên giới hiệu lực chứ không đề xuất thuật toán mới. Không in đậm, không trích dẫn mục. **Trần cứng cho §1.1: không quá một trang A4** (13pt, giãn 1,5). Mọi khảo sát văn liệu thuộc Chương 2; mọi lập luận về thiết kế đo thuộc §1.2.1 và Chương 4 — **không mở lại ở đây** |
> | 1.2 | Chia lại thành đúng ba tiểu mục **Mục tiêu · Đối tượng · Phạm vi**; **bỏ bảng RQ**, RQ1–RQ5 chuyển thành văn xuôi. **Rút gọn (21/09):** §1.2.1 còn ba đoạn — mục tiêu tổng quát · năm mục tiêu cụ thể gói trong một đoạn, mỗi mục tiêu một câu · một câu về dạng phát biểu kết quả. Phần biện minh cho thiết kế đo (dao động giữa các lần chạy, vì sao ước lượng thay vì kiểm định) thuộc **Chương 4**, không trình bày lại ở §1.2.1. §1.2.2 còn hai đoạn, §1.2.3 còn ba đoạn — **bỏ toàn bộ tám khối in đậm**, mỗi giới hạn nay là một mệnh đề trong câu; đủ tám giới hạn cũ, phần trình bày đầy đủ để **Chương 6** |
> | 1.3 | Gộp thành một phần liền, **bỏ ba tiêu đề `C1`/`C2`/`C3`**; nội dung ba đóng góp giữ nguyên, đổi cách trình bày. **Rút gọn (21/09):** còn bốn đoạn — một câu khung về phạm vi hạn định, rồi mỗi đóng góp đúng một đoạn. Ba thành phần của đóng góp thứ nhất gói trong một đoạn; **câu phòng thủ "hai thành phần đầu đứng vững độc lập" là bắt buộc, không được cắt** |
> | 1.4 | Thêm câu dẫn mở đoạn trước khi liệt kê các chương |
>
> **Nguyên tắc chi phối toàn chương (chốt 21/09):** chương phải **đọc độc lập được**. Người đọc không có đề cương đã duyệt, không có `00_outline.md`, và chưa đọc Chương 4–6 vẫn phải hiểu trọn vẹn. Cụ thể: (a) không viện dẫn đề cương như một nguồn quyền uy — nếu một mục tiêu cần được biện minh thì biện minh ngay tại chỗ; (b) **không đẩy lập luận ra tham chiếu mục** — cấm các câu dạng "§4.5.3 trình bày lý do"; lý do phải nằm trong câu, tham chiếu chỉ còn là chỉ dẫn đọc thêm; (c) gọi tên phương pháp cụ thể (FedMix, NaiveMix, CCVR) thay vì "công trình gốc", "một phương pháp hiệu chuẩn"; (d) mọi thuật ngữ được định nghĩa ở lần xuất hiện đầu.
>
> ⚠️ **Việc kéo theo cho agent sau:** §1.1 và §1.3 nay nêu đích danh **FedMix (Yoon và cộng sự, 2021)**, **NaiveMix** và **CCVR**. Ba mục này cần trích dẫn đầy đủ trong `refs.bib` `[CẦN TẠO]`. Việc nêu tên là có chủ ý — đây là điều kiện để chương đọc độc lập được — nhưng phải khớp với Chương 2 khi Chương 2 được viết.
>
> **Ràng buộc còn hiệu lực:** IR#1–IR#10 (`00_outline.md` §2). Đặc biệt IR#3 — mọi phát biểu về tính mới đều phải **có hạn định** kèm phạm vi khảo sát (§2.6.1); và nguyên tắc phòng thủ ở khối trạng thái đầu file: đóng góp thứ nhất **không được treo vào thành phần (c)**.
>
> ⚠️ §1.3 vẫn phải **rà soát lại sau khi có kết quả Chương 5**.

---

## 1.1. Lý do chọn đề tài

Học liên kết (Federated Learning) cho phép huấn luyện một mô hình dùng chung trên dữ liệu nằm rải rác ở nhiều thiết bị, mà dữ liệu đó không bao giờ rời khỏi thiết bị. Chỉ tham số mô hình được trao đổi. Kiến trúc này giải quyết đồng thời hai ràng buộc thực tế: quyền riêng tư của người dùng và băng thông hạn chế của mạng biên.

Trở ngại trung tâm của mô hình này là dữ liệu giữa các thiết bị không phân phối đồng nhất. Người dùng khác nhau có thói quen khác nhau, thiết bị khác nhau, môi trường thu thập khác nhau; hệ quả là mục tiêu tối ưu cục bộ của mỗi thiết bị lệch khỏi mục tiêu toàn cục. Khi mỗi thiết bị chạy nhiều bước cập nhật trước khi đồng bộ, các mô hình cục bộ bị trôi về những nghiệm khác nhau, và phép trung bình của chúng không còn là một bước tiến tốt. Hiện tượng này làm chậm hội tụ, gây dao động, và hạ độ chính xác của mô hình tổng hợp.

Trong các hướng khắc phục đã được đề xuất, nhóm can thiệp vào quá trình tối ưu hoá như thêm số hạng chính quy hoá, hiệu chỉnh gradient, điều chỉnh quy tắc tổng hợp… có ưu điểm là không trao đổi thêm bất kỳ thông tin nào về dữ liệu. Nhưng đó cũng là giới hạn của chúng: nếu các phân phối cục bộ thực sự khác nhau, không một thao tác nào trên quỹ đạo tối ưu hoá có thể cung cấp cho một thiết bị thông tin mà nó không bao giờ quan sát được.

Hướng tăng cường dữ liệu chấp nhận một đánh đổi khác: truyền thêm một lượng thông tin nhỏ về dữ liệu, đủ để mỗi thiết bị có một hình dung về phân phối toàn hệ thống, nhưng nhỏ tới mức không vi phạm ràng buộc riêng tư. Ý tưởng này đã được chứng minh là hiệu quả từ nhờ chia sẻ một tập dữ liệu nhỏ cân bằng lớp khôi phục được phần lớn độ chính xác bị mất. Vấn đề là tập chia sẻ đó gồm dữ liệu thô, điều đi ngược nguyên tắc nền tảng.

Toàn bộ dòng nghiên cứu sau đó có thể đọc như những nỗ lực giữ lại lợi ích ấy mà giảm mức riêng tư phải hi sinh: chia sẻ dữ liệu sinh nhân tạo, chia sẻ tri thức của mô hình thay vì dữ liệu, chia sẻ thống kê đặc trưng theo lớp, hoặc chia sẻ các mẫu đã được lấy trung bình, đây cũng là hướng mà luận văn này nghiên cứu.

Trong hướng ấy, phương pháp tiêu biểu là FedMix (Yoon và cộng sự, 2021): thay vì trộn thẳng mẫu trung bình vào ảnh cục bộ, nó khai triển Taylor bậc nhất hàm mất mát, khiến mẫu trung bình chỉ còn đi vào qua một tích vô hướng với đạo hàm của hàm mất mát theo đầu vào. Số hạng đó là toàn bộ phần lý thuyết của phương pháp, nhưng chưa từng được tách riêng khỏi bản thân phép trộn để đo, và phần lớn bằng chứng đã công bố lại chỉ có ở lệch phân phối nhãn. Luận văn vì vậy không đề xuất một thuật toán mới, mà xác định biên giới hiệu lực của cơ chế đã có: nó hoạt động trong điều kiện nào, không hoạt động trong điều kiện nào, và vì sao.

---

## 1.2. Mục tiêu, đối tượng và phạm vi

### 1.2.1. Mục tiêu

Mục tiêu tổng quát của luận văn là nghiên cứu cơ sở lý thuyết của các kỹ thuật làm phong phú không gian đặc trưng và của phương pháp xấp xỉ hàm mất mát bằng khai triển Taylor trong môi trường học máy phân tán. Đây là mục tiêu nghiên cứu, không phải cam kết rằng cơ chế được khảo sát sẽ vượt qua các phương pháp đối chứng.

Mục tiêu đó được cụ thể hoá thành năm việc. Thứ nhất, đo đóng góp của số hạng khai triển vào hiệu năng của mô hình toàn cục, khi số hạng ấy được tách khỏi bản thân phép trộn và hai cấu hình được đo ở cùng một trọng số trộn. Thứ hai, xác định đóng góp đó thay đổi thế nào theo loại và mức độ không đồng nhất của dữ liệu, cụ thể là kết luận rút ra dưới lệch phân phối nhãn có còn đúng dưới lệch phân phối đặc trưng hay không. Thứ ba, xác định đóng góp đó thay đổi thế nào theo lượng thông tin phụ trợ được phép chia sẻ, và cái giá phải trả về chi phí truyền thông. Thứ tư, kiểm tra giả định làm nền cho cả hướng nghiên cứu, rằng thiên lệch do dữ liệu không đồng nhất gây ra tập trung ở tầng phân lớp cuối chứ không ở phần trích xuất đặc trưng. Thứ năm, xác định cơ chế có mở rộng được sang tác vụ hồi quy hay không; câu hỏi này được trả lời bằng một mệnh đề lý thuyết ở Chương 4, không bằng thực nghiệm.

Đại lượng cần đo có thể nhỏ hơn độ dao động giữa các lần chạy, nên cả năm mục tiêu đều được phát biểu ở dạng ước lượng kèm khoảng tin cậy thay vì dạng kiểm định có hay không: một khoảng hẹp quanh 0 vẫn là một kết luận, còn một kiểm định không có ý nghĩa thống kê thì không.

### 1.2.2. Đối tượng

Đối tượng nghiên cứu là cơ chế tăng cường dữ liệu bằng mẫu trung bình đại diện kết hợp với xấp xỉ hàm mất mát bằng khai triển Taylor bậc nhất, trong bài toán học liên kết có giám sát. Đối tượng được hiểu ở mức cơ chế chứ không ở mức một cài đặt cụ thể; FedMix chỉ là hiện thân để cơ chế trở nên đo được.

Để đo được, cơ chế được tháo thành bốn thành phần có thể thay đổi độc lập với nhau: cách mẫu trung bình đi vào mục tiêu huấn luyện, tức trộn thẳng vào đầu vào như NaiveMix, qua khai triển Taylor như FedMix, hay không dùng; lượng thông tin phụ trợ, gồm trọng số trộn và số ảnh gộp trong mỗi mẫu đại diện; chế độ không đồng nhất, gồm loại lệch phân phối và mức độ nghiêm trọng; và tác vụ cùng hàm mất mát đi kèm. Toàn bộ thực nghiệm của luận văn là các phép quét dọc theo bốn trục này, nhờ đó kết luận có thể phát biểu theo vùng thay vì thành một phán quyết chung.

### 1.2.3. Phạm vi

Các giới hạn dưới đây được nêu ngay ở đây vì chúng ràng buộc cách đọc mọi kết quả về sau; Chương 6 trình bày đầy đủ hơn.

Toàn bộ kết quả chính chạy trên một bộ dữ liệu ảnh $32\times32$ với một họ kiến trúc không dùng chuẩn hoá theo lô, nên nếu phép kiểm soát trên các kiến trúc khác không thực hiện được thì giả thiết rằng kết quả độc lập với kiến trúc là chưa được kiểm tra, chứ không phải đã được xác nhận. Lệch phân phối đặc trưng được mô phỏng bằng cách xoay ảnh những góc khác nhau ở những thiết bị khác nhau; đây là một biến đổi khả nghịch, thuần hình học và tác động như nhau lên mọi lớp, nằm ở cực dễ của phổ dịch chuyển miền, nên kết quả thu được dưới nó không ngoại suy sang dịch chuyển miền thực tế. Không có cấu hình nào kết hợp đồng thời hai loại lệch phân phối, nên luận văn không kết luận gì về tương tác giữa chúng. Với số lần chạy khả thi, nửa rộng khoảng tin cậy 95% vào khoảng một điểm phần trăm, và mọi hiệu ứng nhỏ hơn mức đó chỉ được báo cáo dưới dạng khoảng.

Phần hồi quy chỉ có kết quả lý thuyết, không có bằng chứng thực nghiệm. Luận văn không đưa ra bảo đảm riêng tư hình thức nào, kể cả riêng tư vi phân; số ảnh gộp trong mỗi mẫu đại diện chỉ là đại lượng đại diện thô cho mức bảo mật. Toàn bộ thực nghiệm chạy ở chế độ mô phỏng với mọi thiết bị tham gia mọi vòng, nên các yếu tố của triển khai thực tế như thiết bị rời mạng hay tham gia một phần đều không được mô hình hoá. Cuối cùng, phần kết quả nền ở Chương 3 và phần thực nghiệm mới ở Chương 5 chạy trên hai nền tảng khác nhau, nên con số tuyệt đối giữa hai phần không so sánh được với nhau và mọi phát biểu bắc cầu chỉ đặt ở mức cơ chế.

---

## 1.3. Đóng góp của luận văn

Luận văn có ba đóng góp; mọi phát biểu về tính mới dưới đây chỉ có hiệu lực trong phạm vi khảo sát văn liệu mà Chương 2 mô tả.

Thứ nhất, một phép đo có kiểm soát đối với đóng góp của số hạng khai triển, gồm ba thành phần: chạy lại phép đối chiếu giữa cấu hình có và không có số hạng ấy trên một nền tảng thực nghiệm thứ hai, với nhiều hạt giống và báo cáo khoảng tin cậy; đo ở trọng số trộn khớp nhau, để tách hiệu ứng của cơ chế khỏi phần đến từ ngân sách tinh chỉnh không đồng đều mà công trình gốc gộp chung; và một biến thể cô lập chặt hơn, giữ nguyên điểm đánh giá hàm mất mát và chỉ bỏ số hạng đạo hàm, mở rộng sang lệch phân phối đặc trưng. Hai thành phần đầu đứng vững độc lập với việc thành phần thứ ba có thực sự mới hay không.

Thứ hai, phép đo cơ chế tại nhiều mức độ nghiêm trọng của cả hai loại lệch phân phối, báo cáo mức cải thiện như một đường đặc tuyến thay vì một con số; các khảo sát hiện có tuy đã tách riêng hai loại lệch nhưng chưa đo nhóm phương pháp chia sẻ dữ liệu ở chế độ hỗn hợp. Vì hai loại lệch được điều khiển bởi hai tham số khác nhau về bản chất, luận văn chiếu mọi cấu hình lên một trục chung trong không gian kết quả; đây là một phép căn chỉnh vận hành phục vụ việc so sánh, không phải lời giải cho bài toán hiệu chuẩn độ nghiêm trọng.

Thứ ba, kiểm toán tính tái lập của nền tảng thực nghiệm được sử dụng: danh mục những chỗ mã nguồn phát hành không khớp với mô tả trong bài báo, kèm một xác nhận âm tính ở chỗ hai bên thực sự khớp nhau. Kết luận được giới hạn tường minh: mã nguồn cho thấy các thuật toán đối chứng bị suy yếu, nhưng luận văn không định lượng mức đóng góp của từng cơ chế.

---

## 1.4. Cấu trúc luận văn

Phần còn lại của luận văn đi theo trình tự từ định vị vấn đề, qua nền tảng lý thuyết và khung thực nghiệm được đề xuất, đến kết quả đo và các kết luận rút ra từ chúng; năm chương sau được tổ chức như sau.

**Chương 2** định vị đối tượng nghiên cứu giữa các hướng tiếp cận lân cận, và phát biểu khoảng trống mà luận văn nhắm tới, kèm phạm vi khảo sát văn liệu.

**Chương 3** trình bày nền tảng lý thuyết: bài toán học liên kết, cách mô hình hoá hai loại lệch phân phối, dẫn xuất đầy đủ của khai triển Taylor bậc nhất và bốn cấu hình sinh ra từ nó, các kết quả về thiên lệch học cục bộ, và một kết quả cổ điển về bộ phân lớp sinh so với phân biệt cùng ranh giới áp dụng của nó.

**Chương 4** trình bày khung thực nghiệm được đề xuất, định nghĩa hình thức các đại lượng được đo, thiết kế trục độ nghiêm trọng, mặt vận hành theo ngân sách, giao thức đo lường, và kết quả lý thuyết về mở rộng sang tác vụ hồi quy.

**Chương 5** trình bày kết quả: tái hiện và kiểm toán tính tái lập, rồi lần lượt trả lời các câu hỏi nghiên cứu.

**Chương 6** tổng kết, nêu các giới hạn một cách tường minh, và đề xuất bảy hướng phát triển.

---

# YÊU CẦU SỬA — 22/09/2026 · lượt rà lối viết + quyết định gác nhánh hồi quy

> **CÁCH DÙNG KHỐI NÀY.** Đây là **đơn đặt việc**, không phải bản viết lại. Mọi phần phía trên giữ nguyên trạng, **không xoá dòng nào**. Agent thực hiện: sửa vào **bản Word** (bản chính từ 22/09), rồi chép phần đã sửa xuống **dưới** khối này dưới một mốc `# PHIÊN BẢN CHỈNH SỬA — <ngày>` mới. Lịch sử phiên bản giữ đầy đủ theo yêu cầu của học viên.
>
> Nguồn ràng buộc: `00_outline.md` §7.2 (chốt từ chỉ bên tham gia), §7.7 (chống giọng văn máy), khối Ch.1 trong §4, nhật ký 22/09 lần 3.
>
> ⚠️ Hiện trạng đối chiếu trong khối này lấy từ **bản Word đã lưu** tại thời điểm rà. Nếu học viên đã sửa trong cửa sổ Word chưa lưu thì bỏ qua mục tương ứng.

## A. Nội dung — bắt buộc

**A1. §1.2.1 — "năm việc" nhưng chỉ liệt kê bốn.** Bản Word đã lưu viết *"Mục tiêu đó được cụ thể hoá thành **năm** việc"* rồi dừng ở *"Thứ tư, kiểm tra giả định…"*. Mục tiêu thứ năm (mở rộng sang hồi quy) **đã được gác lại theo quyết định của học viên**, nên cách sửa là đổi **"năm" → "bốn"**, không phải thêm ý thứ năm vào.

**A2. §1.2.3 — bỏ câu còn nhắc hồi quy.** Xoá nguyên câu: *"Phần hồi quy chỉ có kết quả lý thuyết, không có bằng chứng thực nghiệm."* Câu sau nó (*"Luận văn không đưa ra bảo đảm riêng tư hình thức nào…"*) trở thành câu mở đoạn.

**A3. §1.4 — bỏ cụm còn nhắc hồi quy.** Trong đoạn giới thiệu Chương 4, xoá cụm *"và kết quả lý thuyết về mở rộng sang tác vụ hồi quy"*, kết thúc đoạn ở *"giao thức đo lường"*.

**A4. §1.2.2 — trục thứ tư nay chỉ còn một mức.** `[QUYẾT]` Đoạn hiện viết *"cơ chế được tháo thành **bốn** thành phần có thể thay đổi độc lập với nhau"*, thành phần thứ tư là *"tác vụ cùng hàm mất mát đi kèm"*. Bỏ hồi quy thì trục đó chỉ còn phân loại, tức không còn là một trục. Hai cách, cần học viên chọn:

- **(a)** viết lại thành **ba** thành phần, bỏ hẳn vế tác vụ — gọn nhất và trung thực với phạm vi hiện tại;
- **(b)** giữ bốn, thêm một mệnh đề nói rõ trục thứ tư nằm trong thiết kế nhưng chưa được quét trong luận văn này — giữ đường mở nếu sau này bổ sung hồi quy.

**A5. §1.1 — phủ định toàn cầu không hạn định, vi phạm IR#3.** Câu *"Số hạng đó là toàn bộ phần lý thuyết của phương pháp, nhưng **chưa từng** được tách riêng khỏi bản thân phép trộn để đo, và phần lớn bằng chứng đã công bố lại chỉ có ở lệch phân phối nhãn."* Chương 2 đã làm đúng ở mục Khoảng trống (*"Cấu hình như vậy không xuất hiện trong bài báo FedMix, kể cả ở phần phụ lục"*), nên Chương 1 không được phát biểu mạnh hơn Chương 2. Bản thay đề xuất: *"…nhưng bài báo FedMix không có cấu hình nào tách riêng nó khỏi phép trộn để đo, kể cả ở phần phụ lục; và phần lớn bằng chứng đã công bố chỉ có ở lệch phân phối nhãn."*

**A6. Nêu tên hai nền tảng thực nghiệm.** §1.3 viết *"trên một nền tảng thực nghiệm **thứ hai**"* và §1.2.3 viết *"chạy trên **hai nền tảng** khác nhau"*, nhưng nền tảng thứ nhất không được gọi tên ở bất kỳ đâu trong Chương 1 — người đọc không có cách nào biết đó là gì. Vi phạm §7.5 (gọi tên cụ thể; chương phải đọc độc lập được), và liên quan IR#9: công trình đã công bố của tác giả hiện **không được nhắc tới một lần nào** trong Chương 1. Phải nêu tên cả hai nền tảng, kèm trích dẫn công trình hội nghị ngay lần xuất hiện đầu.

**A7. §1.3 — câu về kiểm toán tái lập nói mạnh mà không nêu đối tượng.** *"mã nguồn cho thấy các thuật toán đối chứng bị suy yếu"*: không nói thuật toán nào, của nền tảng nào, và "bị suy yếu" là khẳng định về mã nguồn của người khác, đặt ở Chương 1 trước khi có bất kỳ bằng chứng nào. Nêu đích danh nền tảng và hạ về mức mô tả.

**A8. §1.3 — "một xác nhận âm tính ở chỗ hai bên thực sự khớp nhau" khó hiểu.** Diễn đạt lại bằng lời thường: ý là kiểm toán ghi nhận cả những chỗ mã nguồn **khớp** với bài báo, không chỉ những chỗ lệch.

## B. Lối viết — áp §7.7

**B1. AI#1, hạn ngạch cấu trúc tương phản: Chương 1 đang dùng 8 lần, hạn mức 3.** Các chỗ đếm được:

1. §1.2.1 — *"Đây là mục tiêu nghiên cứu, không phải cam kết rằng…"*
2. §1.2.1 — *"phát biểu ở dạng ước lượng kèm khoảng tin cậy thay vì dạng kiểm định có hay không"*
3. §1.1 — *"luận văn không đề xuất một thuật toán mới, mà xác định biên giới hiệu lực…"*
4. §1.2.2 — *"Đối tượng được hiểu ở mức cơ chế chứ không ở mức một cài đặt cụ thể"*
5. §1.2.2 — *"kết luận có thể phát biểu theo vùng thay vì thành một phán quyết chung"*
6. §1.2.3 — *"là chưa được kiểm tra, chứ không phải đã được xác nhận"*
7. §1.3 — *"báo cáo mức cải thiện như một đường đặc tuyến thay vì một con số"*
8. §1.3 — *"đây là một phép căn chỉnh vận hành phục vụ việc so sánh, không phải lời giải cho bài toán hiệu chuẩn độ nghiêm trọng"*

Đề xuất giữ **(3)** vì là câu định danh của cả luận văn, **(6)** vì vế tương phản ở đó mang nội dung thật (chưa kiểm tra khác với đã xác nhận), và **(8)** vì nó chặn một cách hiểu sai cụ thể. Năm câu còn lại viết thành câu khẳng định thường.

**B2. AI#4, một câu rào cho mỗi chương: Chương 1 đang có ba.** Ngoài câu (1) ở B1, còn *"mọi phát biểu về tính mới dưới đây chỉ có hiệu lực trong phạm vi khảo sát văn liệu mà Chương 2 mô tả"* (§1.3) và *"Hai thành phần đầu đứng vững độc lập với việc thành phần thứ ba có thực sự mới hay không"* (§1.3).

⚠️ **Xung đột quy tắc cần biết trước khi sửa:** khối trạng thái 21/09 phía trên ghi câu *"hai thành phần đầu đứng vững độc lập"* là **bắt buộc, không được cắt**. Vậy chính câu đó là câu rào được giữ lại; hai câu còn lại chuyển thành phát biểu thường hoặc dời về Ch.6 §6.3.

**B3. AI#7, thuật ngữ tự đặt chưa định nghĩa.** §1.3 dùng *"đường đặc tuyến"* và *"ngân sách tinh chỉnh"*, §1.2.2 dùng *"biên giới hiệu lực"* — không cụm nào được định nghĩa ở lần xuất hiện đầu, mà Chương 1 chính là nơi người đọc gặp chúng lần đầu. Hoặc thêm một mệnh đề định nghĩa tại chỗ, hoặc thay bằng cách nói thường.

**B4. AI#2 và AI#6.** Đếm số câu kết đoạn có nhịp đối và số dấu `—` chêm giữa câu, đối chiếu hạn mức ở §7.7, ghi kết quả vào khối trạng thái khi nộp bản sửa.

## C. Đọc trôi chảy

**C1. §1.2.1 — bốn mục tiêu nhồi trong một đoạn văn xuôi.** `[QUYẾT]` Đoạn *"Thứ nhất… Thứ tư…"* là một khối liền, mỗi mục tiêu một câu dài, không có chỗ nghỉ mắt. Đây là chỗ quy tắc tự đặt ở §7.6 (*Chương 1 không tiểu mục, không gạch đầu dòng*) gây hại: danh sách mục tiêu cụ thể là nơi hội đồng đối chiếu với đề cương, và mọi mẫu luận văn đều cho phép đánh số ở đây. **Đề xuất phá lệ đúng chỗ này**: đánh số 1–4, hoặc tối thiểu tách thành hai đoạn.

**C2. §1.2.3 — câu đầu dài 5 dòng, phải đọc hai lần.** *"Toàn bộ kết quả chính chạy trên một bộ dữ liệu ảnh 32×32 với một họ kiến trúc không dùng chuẩn hoá theo lô, nên nếu phép kiểm soát trên các kiến trúc khác không thực hiện được thì giả thiết rằng kết quả độc lập với kiến trúc là chưa được kiểm tra, chứ không phải đã được xác nhận."* — điều kiện lồng phủ định lồng tương phản. Thêm nữa, viết phạm vi dưới dạng **điều kiện về một việc chưa xảy ra** (*"nếu … không thực hiện được"*) là lạ với một bản đã nộp. Tách thành hai câu và bỏ mệnh đề điều kiện: nói thẳng rằng kết quả chính chạy trên một họ kiến trúc, và luận văn không khẳng định kết luận độc lập với kiến trúc.

**C3. §1.3 — đóng góp thứ nhất là một câu khoảng 90 từ**, ba thành phần ngăn bằng dấu chấm phẩy, thành phần thứ ba còn mang mệnh đề phụ. Tách thành ba câu.

## D. Thuật ngữ

**D1. Chương 1 dùng "thiết bị", xuyên suốt** — quy ước chốt ở `00_outline.md` §7.2. Từ Chương 2 trở đi mới dùng "client". Rà toàn chương, không để lẫn "client" hay "bên".


---

# QUYẾT ĐỊNH — 22/09/2026 · chốt hai mục `[QUYẾT]` của khối YÊU CẦU SỬA phía trên

> Khối này **không thay thế** khối yêu cầu phía trên; nó chốt hai mục còn để ngỏ ở đó. Mọi mục khác của khối yêu cầu giữ nguyên hiệu lực.

## A4 → chọn **(a)**: rút về **ba** thành phần

Bỏ hẳn vế tác vụ khỏi §1.2.2. Ba sửa đổi trên cùng một đoạn:

1. *"cơ chế được tháo thành **bốn** thành phần"* → **"ba thành phần"**
2. xoá cụm *"; và tác vụ cùng hàm mất mát đi kèm"* — danh sách kết thúc ở *"mức độ nghiêm trọng"*
3. *"các phép quét dọc theo **bốn** trục này"* → **"ba trục này"**

⚠️ **Làm cùng lúc với B1 mục (5).** Câu cuối của chính đoạn này — *"nhờ đó kết luận có thể phát biểu theo vùng **thay vì** thành một phán quyết chung"* — nằm trong danh sách cấu trúc tương phản phải chuyển thành câu khẳng định thường (AI#1). Sửa một lần cho cả hai việc, đừng đụng vào đoạn hai lần.

Hệ quả cần rà: nếu chỗ nào khác trong luận văn còn nói cơ chế có bốn trục hoặc bốn thành phần thì sửa theo. `00_outline.md` §4, khối Ch.4 mục 4.1 đã được đánh dấu `[GÁC]` cho vế tác vụ.

## C1 → **đánh số 1–4** ở §1.2.1

Đây là **ngoại lệ có chủ ý** so với §7.6 (*"Văn xuôi liền mạch cho Ch.1 và Ch.6"*). Đã ghi vào `00_outline.md` §7.6 để agent sau không tự ý gỡ số về lại văn xuôi.

Cách trình bày:

- Giữ câu dẫn, sửa theo A1: *"Mục tiêu đó được cụ thể hoá thành **bốn** việc."*
- Bốn mục tiêu tách thành **danh sách đánh số 1–4**, mỗi mục **đúng một câu**.
- **Bỏ các từ "Thứ nhất / Thứ hai / Thứ ba / Thứ tư"** — số thứ tự đã làm việc đó, giữ lại là thừa.
- Đoạn tiếp theo (*"Đại lượng cần đo có thể nhỏ hơn độ dao động giữa các lần chạy…"*) **giữ nguyên dạng đoạn văn xuôi**, không gộp vào danh sách.

**Phạm vi của ngoại lệ: chỉ §1.2.1.** Các mục §1.1, §1.2.2, §1.2.3, §1.3, §1.4 vẫn là văn xuôi liền mạch, không đánh số, không gạch đầu dòng, không khối in đậm mở câu.

⚠️ **Cần đối chiếu mẫu trình bày của khoa** về danh sách đánh số trong thân bài (kiểu số, thụt lề, giãn dòng) trước khi định dạng trong Word — cùng loại việc với lần đối chiếu đánh số bốn cấp ở Chương 2.

---

# YÊU CẦU SỬA — 24/09/2026 · kết quả trên nền tảng Flower là kết quả của luận văn

> **Căn cứ.** Quyết định của học viên ngày 24/09: luận văn viết như thể chưa có bài hội nghị. Các thực nghiệm trên stack Flower (FedMix dưới lệch nhãn, CCVR và các head hiệu chuẩn, thiên lệch định hướng) là thực nghiệm của chính luận văn và được trình bày ở **Chương 5, mục 5.2 mới**. Bài ISWTA 2026 chỉ xuất hiện ở *Danh mục công bố khoa học của tác giả* và trong *Lời cam đoan*; thân bài **không trích** bài đó. Ghi đầy đủ ở `00_outline.md` §1.5.
>
> **Cách dùng bảng.** Cột *Tìm trong Word* là một cụm có trong đoạn cần sửa, gõ vào Ctrl+F. Cột *Trước* chép nguyên văn từ bản Word ngày 24/09. Các đoạn sửa ở đây không chứa công thức. Chỉ-append: mọi phần phía trên giữ nguyên.

| # | Mục | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 1.2.3, đoạn 2, câu cuối | `Cuối cùng, phần kết quả nền` | Cuối cùng, phần kết quả nền ở Chương 3 và phần thực nghiệm mới ở Chương 5 chạy trên hai nền tảng khác nhau, nên con số tuyệt đối giữa hai phần không so sánh được với nhau và mọi phát biểu bắc cầu chỉ đặt ở mức cơ chế. | Cuối cùng, thực nghiệm của luận văn chạy trên hai nền tảng: nền tảng Flower cho phần lệch phân phối nhãn và mã nguồn FedBR cho phần lệch phân phối đặc trưng. Con số tuyệt đối giữa hai nền tảng vì vậy không so sánh được với nhau, và mọi phát biểu bắc cầu chỉ đặt ở mức cơ chế. | Chương 3 không còn "kết quả nền"; cả hai nền tảng đều là của luận văn |
| 2 | 1.3, đoạn "Thứ nhất" | `trên một nền tảng thực nghiệm thứ hai` | …chạy lại phép đối chiếu giữa cấu hình có và không có số hạng ấy **trên một nền tảng thực nghiệm thứ hai**, với nhiều hạt giống… | …chạy lại phép đối chiếu giữa cấu hình có và không có số hạng ấy **trên mã nguồn FedBR**, với nhiều hạt giống… | Luận văn nay tự có hai nền tảng, nên "thứ hai" không còn rõ là thứ hai so với cái gì |
| 3 | 1.3, đoạn "Thứ ba" — `[QUYẾT]` | `Thứ ba, kiểm toán tính tái lập` | Thứ ba, kiểm toán tính tái lập của nền tảng thực nghiệm được sử dụng: danh mục những chỗ mã nguồn phát hành không khớp với mô tả trong bài báo, kèm một xác nhận âm tính ở chỗ hai bên thực sự khớp nhau. Kết luận được giới hạn tường minh: mã nguồn cho thấy các thuật toán đối chứng bị suy yếu, nhưng luận văn không định lượng mức đóng góp của từng cơ chế. | Thứ ba, kiểm tra tính tái lập trên cả hai nền tảng. Trên nền tảng Flower, luận văn đo lại FedMix và nhóm hiệu chuẩn tầng phân lớp dưới lệch phân phối nhãn: FedMix không cải thiện so với FedAvg, còn mức cải thiện của hiệu chuẩn đổi dấu theo ngân sách mẫu ảo. Trên mã nguồn FedBR, luận văn lập danh mục những chỗ mã nguồn phát hành không khớp với mô tả trong bài báo. Kết luận của phần này được giới hạn tường minh: mã nguồn cho thấy các thuật toán đối chứng bị suy yếu, nhưng luận văn không định lượng mức đóng góp của từng cơ chế. | (a) Kết quả Flower phải có chỗ trong phần đóng góp; chỗ hợp nhất là đóng góp về tính tái lập, vì đó đúng là nội dung của chúng. (b) Bỏ "xác nhận âm tính": số hạng Taylor trong mã bị chia thêm cho kích thước lô, nên chỗ "khớp nhau" không còn trọn vẹn (`INDEX_ma-nguon-va-ket-qua.md` F1). **Nếu học viên không muốn đổi đóng góp thứ ba thì ít nhất bỏ cụm "kèm một xác nhận âm tính ở chỗ hai bên thực sự khớp nhau"** |
| 4 | 1.4, đoạn Chương 3 | `Chương 3 trình bày nền tảng lý thuyết` | Chương 3 trình bày nền tảng lý thuyết: bài toán học liên kết, cách mô hình hoá hai loại lệch phân phối, dẫn xuất đầy đủ của khai triển Taylor bậc nhất và bốn cấu hình sinh ra từ nó, các kết quả về thiên lệch học cục bộ, và một kết quả cổ điển về bộ phân lớp sinh so với phân biệt cùng ranh giới áp dụng của nó. | Chương 3 trình bày nền tảng lý thuyết: bài toán học liên kết, cách mô hình hoá hai loại lệch phân phối, dẫn xuất khai triển Taylor bậc nhất dẫn tới NaiveMix và FedMix, các biểu hiện của thiên lệch học cục bộ cùng hai giả thuyết về dạng thiên lệch ở bộ phân lớp, và một kết quả cổ điển về bộ phân lớp sinh so với phân biệt cùng ranh giới áp dụng của nó. | Chương 3 chỉ còn lý thuyết; số đo thiên lệch chuyển sang Chương 5. "Bốn cấu hình" nay ở Chương 4 (Q1 của `04_chuong4.md`) |
| 5 | 1.4, đoạn Chương 4 | `Chương 4 trình bày khung thực nghiệm` | Chương 4 trình bày khung thực nghiệm được đề xuất, định nghĩa hình thức các đại lượng được đo, thiết kế trục độ nghiêm trọng, mặt vận hành theo ngân sách, giao thức đo lường. | Chương 4 trình bày khung thực nghiệm được đề xuất: bốn cấu hình hàm mất mát dùng để cô lập số hạng Taylor, định nghĩa hình thức các đại lượng được đo, thiết kế trục độ nghiêm trọng, mặt vận hành theo ngân sách và giao thức đo lường. | Đi cùng hàng 4. Nếu học viên chọn để lưới bốn cấu hình ở Chương 3 thì giữ nguyên câu cũ ở hàng này và bỏ vế "dẫn tới NaiveMix và FedMix" ở hàng 4 |
| 6 | 1.4, đoạn Chương 5 | `Chương 5 trình bày kết quả` | Chương 5 trình bày kết quả: tái hiện và kiểm toán tính tái lập, rồi lần lượt trả lời các câu hỏi nghiên cứu. | Chương 5 trình bày kết quả, bắt đầu từ các thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower, tiếp theo là phần tái hiện và kiểm toán tính tái lập của mã nguồn FedBR, rồi lần lượt trả lời các câu hỏi nghiên cứu. | Chương 5 có mục 5.2 mới |

## Phần ngoài chương — hai chỗ trong Word đang để trống

**Lời cam đoan** (Word hiện chỉ có tiêu đề). Đoạn đề xuất, cần đối chiếu mẫu Lời cam đoan của Trường trước khi dùng:

> Tôi xin cam đoan luận văn này là công trình nghiên cứu của bản thân, được thực hiện dưới sự hướng dẫn khoa học của PGS.TS. Nguyễn Tấn Cầm. Các số liệu và kết quả trình bày trong luận văn là trung thực và do tôi trực tiếp thực hiện. Một phần kết quả của luận văn, gồm các thực nghiệm dưới lệch phân phối nhãn trình bày ở Chương 5, đã được công bố trong bài báo khoa học liệt kê ở Danh mục công bố khoa học của tác giả, với người hướng dẫn khoa học là đồng tác giả. Mọi tài liệu tham khảo được sử dụng trong luận văn đều được trích dẫn đầy đủ.

Câu thứ ba là câu cần có: nó khai báo phần trùng nội dung giữa luận văn và bài đã đăng, để phần quét trùng lặp không bị hỏi.

**Danh mục công bố khoa học của tác giả:**

> [1] Vu Tuan Kiet, Nguyen Tan Cam, "When Does Classifier Calibration Reproduce Under Non-IID Federated Learning? A Controlled Study on a Faithful Flower Stack," *2026 10th IEEE Symposium on Wireless Technology & Applications (ISWTA 2026)*, 2026. (Đã được chấp nhận đăng.)

Khi có DOI hoặc số trang thì bổ sung. Không ghi hạng CORE (xem `INDEX_ma-nguon-va-ket-qua.md` §2).

⚠️ **Việc cũ còn treo, không thuộc lượt này nhưng cùng chương:** Word mục 1.2.2 vẫn tháo cơ chế thành **bốn** thành phần, còn vế *"tác vụ cùng hàm mất mát đi kèm"* (quyết định 22/09 đã chốt rút về ba). Đoạn sau bốn mục tiêu vẫn viết *"cả **năm** mục tiêu"*.
