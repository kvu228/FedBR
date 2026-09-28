# CHƯƠNG 6 — KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN (hướng B)

> **KHỐI TRẠNG THÁI** · 28/09/2026 (bản rút gọn, lượt 2)
>
> - **Word:** chương mới có bốn tiêu đề (Kết luận, Đóng góp, Hạn chế, Hướng phát triển). Chép thân bài dưới đây vào dưới các tiêu đề tương ứng. Chương chưa có trong Word nên file được viết đè; bản trước còn trong git.
> - **Độ dài (học viên):** khoảng 2–3 trang A4, Times New Roman 13, giãn dòng 1.5. Thân bài dưới đây khoảng 900 chữ, tương đương khoảng 2.5 trang.
> - **Hướng phát triển (học viên):** viết theo hướng cải thiện phương pháp và mở rộng phạm vi, không đề nghị chạy lại thực nghiệm.
> - **Quy ước:** văn xuôi liền (§7.6); số thập phân dấu chấm; trích dẫn theo danh mục Word 28/09 ([2] FedMix, [3] FedBR); không nói về mã nguồn; không trích bài hội nghị của học viên.
> - **Tự kiểm §7.7:** không dấu `—` chêm, không cụm sáo, một khuôn tương phản (6.1, câu cuối). Mọi con số khớp Ch.5 bản md 28/09.

## 6.1. Kết luận

Luận văn đặt câu hỏi: tăng cường dữ liệu bằng mẫu trung bình đại diện, dùng qua khai triển Taylor bậc nhất của hàm mất mát, có nâng được hiệu suất học liên kết trên dữ liệu không đồng nhất hay không. Để trả lời, luận văn dựng một khung chia sẻ mẫu trung bình trong đó cách dùng mẫu trung bình là một thành phần thay được, rồi đo các cách dùng trên hai nền tảng thực nghiệm.

Ở mọi cấu hình đã đo, cách dùng dựa trên khai triển Taylor không nâng được hiệu suất. Trên nền tảng Flower, FedMix kém FedAvg 1.86 ± 0.79 điểm phần trăm, và khoảng tin cậy loại trừ khả năng cải thiện. Trên nền tảng FedBR, hiệu của FedMix so với FedAvg nằm dưới ngưỡng đọc. Cộng số hạng Taylor ở đúng biên độ công thức vào FedBR thì huấn luyện phân kỳ.

FedBR [3] là cách dùng duy nhất cho mức cải thiện rõ, hơn FedAvg 6.37 điểm; gần một nửa khoảng cách này biến mất khi cả hai được hiệu chuẩn lại tầng phân lớp. Mẫu trung bình rẻ về truyền thông nhưng mất thông tin nhanh khi số ảnh gộp tăng: ở mười ảnh mỗi mẫu, chúng không còn đủ để huấn luyện lại tầng phân lớp. Trên nền tảng Flower, thiên lệch của tầng phân lớp nằm ở hướng của ranh giới quyết định. Trong phạm vi đã đo, mẫu trung bình giúp được khi làm điểm tựa cho tầng phân lớp và không gian đặc trưng, chứ không phải khi đi vào mục tiêu qua số hạng Taylor.

## 6.2. Đóng góp

Luận văn có ba đóng góp. Thứ nhất là khung học liên kết chia sẻ mẫu trung bình ở Chương 4, trong đó NaiveMix, FedMix [2] và FedBR [3] là ba cách dùng thay được của cùng một kênh dữ liệu, kèm công thức chi phí truyền thông của kênh đó.

Thứ hai là phép đánh giá có kiểm soát các cách dùng ấy trên hai nền tảng, dưới lệch phân phối nhãn và dưới lệch phân phối nhãn kèm lệch phân phối đặc trưng. Mức cải thiện được báo cáo theo cặp, kèm chi phí tính toán và lượng thông tin được chia sẻ; phép chẩn đoán ở mục 5.3.3 đo trực tiếp lượng thông tin mà mẫu trung bình còn giữ cho tầng phân lớp.

Thứ ba là kiểm chứng lại các kết quả đã công bố: đo lại FedMix và nhóm hiệu chuẩn tầng phân lớp trên nền tảng Flower, tái hiện bảng CIFAR-10 của FedBR, và chỉ ra rằng cách tính số hạng Taylor theo lô thường gặp làm số hạng này nhỏ hơn công thức $B$ lần. Kết quả ở mục 5.5 cho thấy phát hiện này có hệ quả thực tế, vì ở đúng biên độ công thức số hạng Taylor làm huấn luyện phân kỳ.

## 6.3. Hạn chế

Trên nền tảng FedBR, mỗi thuật toán chỉ chạy với một seed, nên các hiệu được đọc bằng một ngưỡng thô thay cho khoảng tin cậy. NaiveMix chưa được đo, và số hạng Taylor ở đúng biên độ công thức chỉ được thử trong một cấu hình, với một giá trị $\lambda$; cách giải thích cho hiện tượng phân kỳ ở mục 5.5 vì vậy vẫn là giả thuyết.

Lệch phân phối đặc trưng chỉ được mô phỏng bằng phép xoay ảnh, một biến đổi dễ và như nhau với mọi lớp, và trên nền tảng FedBR nó luôn đi cùng lệch nhãn. Mọi thí nghiệm dùng CIFAR-10 với backbone VGG không chuẩn hoá theo lô, nên phát hiện về thiên lệch định hướng chưa được kiểm tra trên kiến trúc khác.

Luận văn không đưa ra bảo đảm riêng tư hình thức; số ảnh gộp trong mỗi mẫu chỉ là đại lượng đại diện thô cho mức bảo vệ. Thực nghiệm chạy ở chế độ mô phỏng. Hai hướng trong đề cương là tác vụ hồi quy và mở rộng vùng lân cận song phương chưa được thực hiện.

## 6.4. Hướng phát triển

Hướng thứ nhất là làm cho số hạng Taylor dùng được ở biên độ thật. Số hạng này tuyến tính theo gradient đầu vào nên không bị chặn dưới, và ở mục 5.5 nó làm huấn luyện phân kỳ; một phiên bản có chuẩn hoá theo độ lớn gradient hoặc có ràng buộc biên độ sẽ giữ được thông tin của mẫu trung bình mà không làm mất ổn định.

Hướng thứ hai là kết hợp hai điểm mạnh mà luận văn quan sát được. FedBR dùng mẫu trung bình làm điểm tựa trong lúc huấn luyện, còn mẫu trung bình gộp ít ảnh đủ để hiệu chuẩn tầng phân lớp sau huấn luyện. Một phương pháp dùng cả hai, với số ảnh gộp chọn theo ngân sách riêng tư, là bước tiếp theo tự nhiên.

Hướng thứ ba là mở rộng phạm vi của khung: sang tác vụ hồi quy, nơi phép tách hàm mất mát theo nhãn vẫn đúng với hàm mất mát bình phương, sang mở rộng vùng lân cận song phương như đề cương đặt ra, và sang dịch chuyển miền thật cùng lệch đặc trưng phụ thuộc lớp. Cuối cùng, một phân tích riêng tư hình thức cho giao thức chia sẻ mẫu trung bình sẽ biến số ảnh gộp trong mỗi mẫu từ một đại lượng đại diện thành một tham số có bảo đảm.