# RÀ SOÁT CHƯƠNG 1–5 · 28/09/2026 · theo bản Word lưu 28/09 08:34

> **Nguồn.** Rà trên chính file Word (trích `word/document.xml`), không trên md. Công thức OMML không trích được thành chữ, nên trong bảng ký hiệu ⟨…⟩ là chỗ có công thức: giữ nguyên công thức, chỉ sửa chữ quanh nó, trừ khi hàng nói rõ phải sửa công thức.
>
> **Cách dùng.** Ctrl+F dán cụm ở cột *Tìm trong Word*. Mỗi cụm đã được đếm là xuất hiện **đúng một lần** trong toàn văn bản (vài ngoại lệ có ghi ở hàng, thường vì cụm cũng nằm trong mục lục hoặc danh mục bảng).
>
> **Thứ tự nên áp** (để số bảng và trích dẫn không bị lệch khi sửa chữ):
> 1. **Mục B1:** chèn chú thích còn thiếu cho bảng "Bốn cách huấn luyện lại tầng phân lớp" ở Ch.5. Trường tự đánh số sẽ đẩy các bảng sau về đúng số (5.8 tái hiện … 5.12 hướng A). Các hàng ở phần A Ch.5 đã viết theo số đúng này.
> 2. **Mục E:** trích dẫn gõ tay sai số. Nên chèn lại bằng Zotero.
> 3. **Phần A** từng chương: câu chữ, lối viết, câu sai với quyết định hiện tại.
> 4. **Mục C, D:** định dạng số và ký hiệu.
> 5. Cập nhật mục lục, danh mục bảng, danh mục hình (Ctrl+A, F9).
>
> **Quyết định làm nền cho lượt rà này:** NaiveMix không chạy (bỏ T1); nền tảng FedBR một seed (12345), đọc bằng ngưỡng 3 điểm; nền tảng Flower ba seed; hướng A là kết quả âm (Ch.5 mục 5.5); thân bài không nói về mã nguồn; luận văn không sửa phép chuẩn hoá của FedMix, Ch.4 mục 4.3 chỉ chỉ ra chỗ lệch; dấu chấm thập phân, dấu phẩy phân tách hàng nghìn.
>
> **Lối viết (dàn bài §7.7).** Các câu thay thế giữ giọng mộc của học viên: câu ngắn đến vừa, không dấu gạch ngang chêm, không khuôn "không phải… mà…", mỗi chương một câu rào. Câu của học viên chỉ bị sửa khi sai hoặc rõ khuôn máy (AI#10).

## Mục lục

- **A. Câu chữ và lối viết**: A1 Chương 1–2 · A2 Chương 3 · A3 Chương 4 · A4 Chương 5
- **B. Chú thích bảng, hình**
- **C. Định dạng số**
- **D. Ký hiệu trong công thức**
- **E. Số trích dẫn**

## A. Câu chữ và lối viết

## A1. Chương 1 và Chương 2

Cách dùng: trong Word, Ctrl+F dán chuỗi ở cột "Tìm trong Word" (mỗi chuỗi chỉ xuất hiện một lần trong toàn luận văn), rồi thay câu ở cột "Trước" bằng câu ở cột "Sau". Ký hiệu ⟨…⟩ là chỗ có công thức: giữ nguyên công thức trong Word, chỉ sửa chữ quanh nó.

Thứ tự ưu tiên trong cột "Lý do": (1) sai với quyết định hiện tại, (2) lỗi ngữ pháp, lỗi tham chiếu, sai nội dung công trình được trích, (3) vượt hạn ngạch AI#1–AI#9, (4) giọng rào đón.

Ghi chú về số trích dẫn: trong Chương 1 và 2, số trích dẫn khớp với danh mục tài liệu tham khảo hiện có trong Word ([1] Zhao, [2] FedMix, [3] FedBR, [4] FedAvg, [10] Luo/CCVR, [12] VHL…), nên bảng không đổi số nào. Các số lệch nằm ở Chương 4–5 (xem cuối file).

### Chương 1

| # | Mục (section + which paragraph) | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 1.2.2, đoạn 1, câu cuối | FedMix, NaiveMix và FedBR là ba cách dùng được khảo sát | FedMix, NaiveMix và FedBR là ba cách dùng được khảo sát. | Khung của luận văn chứa ba cách dùng là FedMix, NaiveMix và FedBR; phần thực nghiệm đo FedMix và FedBR. | Sai với quyết định: NaiveMix không chạy |
| 2 | 1.2.1, đoạn ngay sau danh sách bốn mục tiêu | Đại lượng cần đo có thể nhỏ hơn độ dao động | Đại lượng cần đo có thể nhỏ hơn độ dao động giữa các lần chạy, nên mọi phép so sánh hiệu năng được phát biểu ở dạng ước lượng kèm khoảng tin cậy thay vì dạng kiểm định có hay không: một khoảng hẹp quanh 0 vẫn là một kết luận, còn một kiểm định không có ý nghĩa thống kê thì không. | **Xoá cả đoạn** | Sai với quyết định: nền tảng FedBR chỉ chạy một seed, không có khoảng tin cậy; §7.6 không bàn thiết kế đo ở 1.2; AI#1 + AI#2 (câu chốt có nhịp đối). Ý đúng đã chuyển vào dòng 4 |
| 3 | 1.2.1, mục tiêu 2 (danh sách đánh số) | Đánh giá các cách dùng ấy so với FedAvg và FedProx | Đánh giá các cách dùng ấy so với FedAvg và FedProx dưới lệch phân phối nhãn, và dưới lệch phân phối nhãn kèm lệch phân phối đặc trưng. | Đánh giá FedMix và FedBR so với FedAvg và FedProx dưới lệch phân phối nhãn, và dưới lệch phân phối nhãn kèm lệch phân phối đặc trưng. | Sai với quyết định: NaiveMix không chạy. Nếu mục tiêu phải khớp nguyên văn đề cương thì giữ câu cũ và nêu việc bỏ NaiveMix ở Ch.6 phần Hạn chế |
| 4 | 1.2.3, đoạn 1, câu cuối | Với ba seed cho mỗi cấu hình, nửa rộng | Với ba seed cho mỗi cấu hình, nửa rộng khoảng tin cậy 95% vào khoảng ba điểm phần trăm, và mọi hiệu ứng nhỏ hơn mức đó chỉ được báo cáo dưới dạng khoảng. | Trên nền tảng Flower, các phép so sánh chính chạy ba seed và hiệu được báo cáo kèm khoảng tin cậy 95%. Trên nền tảng FedBR, mỗi cấu hình chỉ chạy một seed (12345), nên hiệu nhỏ hơn 3 điểm phần trăm được coi là không phân biệt được. | Sai với quyết định: nền tảng FedBR một seed, đọc bằng ngưỡng 3 điểm |
| 5 | 1.3, đoạn "Thứ hai" | Thứ hai, phép đánh giá có kiểm soát các cách dùng ấy | Thứ hai, phép đánh giá có kiểm soát các cách dùng ấy trên hai nền tảng thực nghiệm, dưới lệch phân phối nhãn và dưới lệch phân phối nhãn kèm lệch phân phối đặc trưng, báo cáo theo cặp với khoảng tin cậy và kèm chi phí tài nguyên. | Thứ hai, phép đánh giá có kiểm soát FedMix và FedBR trên hai nền tảng thực nghiệm, dưới lệch phân phối nhãn và dưới lệch phân phối nhãn kèm lệch phân phối đặc trưng, báo cáo theo cặp và kèm chi phí tài nguyên. | Sai với quyết định: NaiveMix không chạy; nền tảng FedBR không có khoảng tin cậy |
| 6 | 1.4, đoạn về Chương 5 | phép so sánh các cách dùng mẫu trung bình trên nền tảng FedBR, và chi phí | Chương 5 trình bày thiết lập và giao thức đo, các thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower, phép so sánh các cách dùng mẫu trung bình trên nền tảng FedBR, và chi phí tài nguyên đo được. | Chương 5 trình bày thiết lập và giao thức đo, các thực nghiệm dưới lệch phân phối nhãn trên nền tảng Flower, phần tái hiện bảng kết quả của FedBR cùng phép so sánh các cách dùng mẫu trung bình trên nền tảng FedBR, chi phí tài nguyên đo được, và phép thử cộng số hạng Taylor của FedMix vào FedBR. | Thiếu mục 5.5 (cộng số hạng Taylor vào FedBR, kết quả âm) và mục 5.3.1 (tái hiện) |
| 7 | 1.4, đoạn về Chương 4 | cách chuẩn hoá số hạng Taylor khi tính theo lô | …, cách chuẩn hoá số hạng Taylor khi tính theo lô, và chi phí tài nguyên của khung. | …, vấn đề chuẩn hoá số hạng Taylor khi tính theo lô, và chi phí tài nguyên của khung. | "Cách chuẩn hoá" đọc như luận văn đề xuất cách tính mới; mục 4.3 chỉ chỉ ra số hạng bị nhỏ đi B lần |
| 8 | 1.4, đoạn về Chương 3 | và một kết quả cổ điển về bộ phân lớp sinh so với phân biệt | …, và một kết quả cổ điển về bộ phân lớp sinh so với phân biệt. | …, và hai kết quả cổ điển về bộ phân lớp sinh so với phân biệt. | Sai tham chiếu: mục 3.6.1 có tên "Hai kết quả cổ điển" (Efron [17], Ng và Jordan [18]) |
| 9 | 1.2.3, đoạn 2, câu cuối | mọi phát biểu bắc cầu chỉ đặt ở mức cơ chế | Con số tuyệt đối giữa hai nền tảng vì vậy không so sánh được với nhau, và mọi phát biểu bắc cầu chỉ đặt ở mức cơ chế. | Hai nền tảng khác nhau về số client, backbone, cách phân hoạch và chỉ số, nên con số của chúng không so trực tiếp được; luận văn chỉ đối chiếu hiện tượng giữa hai nền tảng. | AI#7: "phát biểu bắc cầu" là thuật ngữ tự đặt, chưa định nghĩa; "vì vậy" không có lý do ở câu trước; khớp cách nói ở mục 5.1.1 |
| 10 | 1.2.3, đoạn 1, câu 3 | đây là một biến đổi khả nghịch, thuần hình học | Lệch phân phối đặc trưng được mô phỏng bằng cách xoay ảnh những góc khác nhau ở những thiết bị khác nhau; đây là một biến đổi khả nghịch, thuần hình học và tác động như nhau lên mọi lớp, nằm ở cực dễ của phổ dịch chuyển miền, nên kết quả thu được dưới nó không ngoại suy sang dịch chuyển miền thực tế. | Lệch phân phối đặc trưng được mô phỏng bằng cách xoay ảnh những góc khác nhau ở những thiết bị khác nhau. Đây là một dạng lệch nhân tạo và dễ, nên kết quả thu được không ngoại suy sang dịch chuyển miền thực tế. | AI#5 (một câu hơn 60 từ); AI#3; tính chất của phép xoay đã nêu ở mục 2.1.2 và 3.2.3 (§7.6: mỗi ý viết một lần) |
| 11 | 1.2.1, đoạn 1, câu 2 | Đây là mục tiêu nghiên cứu, không phải cam kết | Đây là mục tiêu nghiên cứu, không phải cam kết rằng cơ chế được khảo sát sẽ vượt qua các phương pháp đối chứng. | **Xoá** | AI#4: câu rào thứ hai của chương (giữ câu rào ở đầu 1.3); AI#1 |
| 12 | 1.1, đoạn 5 | chia sẻ tri thức của mô hình thay vì dữ liệu | Toàn bộ dòng nghiên cứu sau đó có thể đọc như những nỗ lực giữ lại lợi ích ấy mà giảm mức riêng tư phải hi sinh: chia sẻ dữ liệu sinh nhân tạo, chia sẻ tri thức của mô hình thay vì dữ liệu, chia sẻ thống kê đặc trưng theo lớp, hoặc chia sẻ các mẫu đã được lấy trung bình, đây cũng là hướng mà luận văn này nghiên cứu. | Toàn bộ dòng nghiên cứu sau đó có thể đọc như những nỗ lực giữ lại lợi ích ấy mà giảm mức riêng tư phải hi sinh: chia sẻ dữ liệu sinh nhân tạo, chia sẻ tri thức của mô hình, chia sẻ thống kê đặc trưng theo lớp, hoặc chia sẻ các mẫu đã được lấy trung bình. Luận văn nghiên cứu hướng cuối cùng này. | AI#1 (cắt để còn trong hạn ngạch); lỗi nối hai mệnh đề bằng dấu phẩy (", đây cũng là…") |
| 13 | 1.1, đoạn 2, câu cuối | Hiện tượng này làm chậm hội tụ, gây dao động | Hiện tượng này làm chậm hội tụ, gây dao động, và hạ độ chính xác của mô hình tổng hợp. | Hiện tượng này làm mô hình tổng hợp hội tụ chậm hơn và kém chính xác hơn. | AI#3: hai bộ ba trong cùng một đoạn (câu 2 đã liệt kê "thói quen, thiết bị, môi trường"); bộ ba này lặp lại ở mục 2.1.1 |
| 14 | 1.1, đoạn 6, câu 3 | chỉ khác ở cách tiêu thụ nó | Hai phương pháp chia sẻ cùng một thứ dữ liệu, chỉ khác ở cách tiêu thụ nó. | Hai phương pháp dùng cùng một loại mẫu trung bình, chỉ khác ở cách dùng. | "Tiêu thụ" là từ dịch sát "consume"; FedMix gửi thêm nhãn mềm nên "cùng một thứ dữ liệu" chưa chính xác (xem 1.2.2, đoạn 2) |
| 15 | 1.1, đoạn 3, câu 1 | điều chỉnh quy tắc tổng hợp… | …như thêm số hạng chính quy hoá, hiệu chỉnh gradient, điều chỉnh quy tắc tổng hợp… có ưu điểm là không trao đổi thêm… | …như thêm số hạng chính quy hoá, hiệu chỉnh gradient hay điều chỉnh quy tắc tổng hợp, có ưu điểm là không trao đổi thêm… | Dấu "…" bỏ lửng danh sách không hợp văn học thuật; thiếu dấu phẩy đóng cụm "như…" nên chủ ngữ khó tách |
| 16 | 1.4, đoạn mở | Phần còn lại của luận văn đi theo trình tự | Phần còn lại của luận văn đi theo trình tự từ định vị vấn đề, qua nền tảng lý thuyết và khung được đề xuất, đến kết quả đo và các kết luận rút ra từ chúng; năm chương sau được tổ chức như sau. | Năm chương còn lại được tổ chức như sau. | AI#9: câu dẫn nhập rỗng, các đoạn sau đã nói đủ trình tự; lặp "sau … như sau" |

**Đếm hạn ngạch Chương 1.** Khuôn tương phản (AI#1): trước 5 (đoạn 5 "thay vì dữ liệu", đoạn 6 "thay vì trộn thẳng", 1.2.1 "không phải cam kết", mục tiêu 4 "chứ không ở độ lớn", đoạn sau danh sách "thay vì dạng kiểm định"); sau 2 (giữ "thay vì trộn thẳng" ở 1.1 và "chứ không ở độ lớn" ở mục tiêu 4). Gạch ngang chêm "—": trước 0, sau 0. Câu rào (AI#4): trước 2, sau 1 (giữ câu đầu mục 1.3).

### Chương 2

| # | Mục (section + which paragraph) | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 2.3.4, đoạn "Đóng góp thứ nhất", câu 2–3 | phép đối chứng giữa FedMix và NaiveMix được thực hiện lại trong khung | Vì ba cách dùng nhận cùng một loại mẫu trung bình, phép đối chứng giữa FedMix và NaiveMix được thực hiện lại trong khung, ở cùng một trọng số trộn và với nhiều seed ngẫu nhiên. Nhờ đó tách được phần chênh lệch đến từ ngân sách tinh chỉnh không đồng đều mà bài báo FedMix gộp chung. | Vì ba cách dùng nhận cùng một loại mẫu trung bình, khung cho phép thêm hoặc bỏ riêng số hạng Taylor mà giữ nguyên các phần còn lại. Luận văn dùng điều này để đo riêng số hạng Taylor khi cộng vào FedBR. | Sai với quyết định: NaiveMix không chạy, không có phép đối chứng FedMix–NaiveMix, nền tảng FedBR chỉ một seed. Câu mới vẫn nối với khoảng trống 2.3.1 (cô lập số hạng Taylor) qua mục 5.5 |
| 2 | 2.3.1, đoạn 2, câu cuối | khoảng trống được nêu để giới hạn cách đọc phép so FedMix với NaiveMix | Luận văn cũng không chạy cấu hình này; khoảng trống được nêu để giới hạn cách đọc phép so FedMix với NaiveMix ở Chương 5. | Luận văn không chạy cấu hình này với FedMix, và cũng không chạy NaiveMix. Số hạng Taylor chỉ được đo riêng ở Chương 5, khi cộng vào FedBR. | Sai với quyết định: Chương 5 không có phép so FedMix với NaiveMix |
| 3 | 2.3.4, đoạn "Đóng góp thứ hai", câu 1 | Đóng góp thứ hai là phép đánh giá có kiểm soát các cách dùng ấy | Đóng góp thứ hai là phép đánh giá có kiểm soát các cách dùng ấy trên hai nền tảng thực nghiệm: … | Đóng góp thứ hai là phép đánh giá có kiểm soát FedMix và FedBR trên hai nền tảng thực nghiệm: … | Sai với quyết định: NaiveMix không chạy |
| 4 | 2.3.4, đoạn "Đóng góp thứ hai", câu 2 | kèm khoảng tin cậy và kèm lượng thông tin được chia sẻ | Mức cải thiện được báo cáo theo cặp, kèm khoảng tin cậy và kèm lượng thông tin được chia sẻ tại đó nó được đo. | Mức cải thiện được báo cáo theo cặp và kèm lượng thông tin được chia sẻ tại điểm đo. Trên nền tảng Flower, mỗi hiệu chính có khoảng tin cậy từ ba seed; trên nền tảng FedBR, mỗi cấu hình chạy một seed và hiệu được đọc với ngưỡng 3 điểm phần trăm. | Sai với quyết định: nền tảng FedBR một seed; "tại đó nó được đo" sai trật tự từ |
| 5 | 2.2.2.6 (FedBR), đoạn 1, câu 1 | là một trong ba cách dùng mẫu trung bình mà luận văn so sánh | …, và phương pháp của nó là một trong ba cách dùng mẫu trung bình mà luận văn so sánh. | …, và phương pháp của nó là một trong ba cách dùng mẫu trung bình cài trong khung của luận văn. | Sai với quyết định: thực nghiệm chỉ so hai cách dùng (NaiveMix không chạy) |
| 6 | 2.3.3, đoạn cuối | Hệ quả đối với luận văn là một yêu cầu về trình tự | Hệ quả đối với luận văn là một yêu cầu về trình tự: trước khi đo bất cứ thứ gì trên một nền tảng thực nghiệm, phải xác định nền tảng đó thực sự chạy gì. Việc kiểm tra một nền tảng thực nghiệm có chạy đúng như bài báo mô tả hay không vì vậy thuộc về thiết kế đo. | Vì vậy, trước khi so sánh các cách dùng mẫu trung bình trên nền tảng FedBR, luận văn chạy lại bảng kết quả CIFAR-10 của bài báo FedBR để kiểm tra nền tảng này cho kết quả như đã công bố. | "Nền tảng thực sự chạy gì" gợi việc đọc mã nguồn, nay nằm ở Phụ lục A; nối thẳng với đóng góp thứ ba; AI#2 (câu chốt) |
| 7 | 2.2.3, đoạn sau Bảng 2.2, câu 1 | là hai phương pháp duy nhất trong bảng thao tác ở không gian đầu vào | FedMix và NaiveMix là hai phương pháp duy nhất trong bảng thao tác ở không gian đầu vào, trong khi mọi phương pháp có chia sẻ thống kê còn lại đều làm việc trên không gian đặc trưng. | Trong bảng, NaiveMix, FedMix và FedBR là ba phương pháp chia sẻ thống kê tính trên ảnh, tức trên không gian đầu vào; CCVR và FedProto chia sẻ thống kê tính trên không gian đặc trưng. | Sai nội dung: pseudo-data của FedBR cũng là ảnh trung bình (Ch.1, mục 3.5.1, Bảng 4.1); câu cũ mâu thuẫn với "cùng một loại mẫu trung bình". Hai câu sau của đoạn ("Chúng cũng chỉ dùng thống kê bậc nhất…") vẫn đúng cho cả ba |
| 8 | 2.3.2, đoạn 2, câu 2 | chỉ FedBR có thí nghiệm dưới lệch phân phối đặc trưng được điều khiển tách biệt | Trong mười ba phương pháp, chỉ FedBR có thí nghiệm dưới lệch phân phối đặc trưng được điều khiển tách biệt. | Trong mười ba phương pháp, chỉ FedBR có thí nghiệm với lệch phân phối đặc trưng được điều khiển bằng một tham số riêng, dù lệch này luôn đi kèm lệch phân phối nhãn. | "Tách biệt" dễ đọc thành lệch đặc trưng đơn lẻ, mâu thuẫn với 1.2.3 ("lệch đặc trưng chỉ xuất hiện cùng lệch nhãn") |
| 9 | 2.3.2, đoạn 2, câu 3 | và ba phương pháp có chạy thêm trên phân hoạch tự nhiên | Phần còn lại đo dưới lệch phân phối nhãn, và ba phương pháp có chạy thêm trên phân hoạch tự nhiên, nơi ba loại lệch xuất hiện cùng lúc. | Phần còn lại đo dưới lệch phân phối nhãn, và bốn phương pháp có chạy thêm trên phân hoạch tự nhiên, nơi ba loại lệch xuất hiện cùng lúc. | Sai số đếm: Bảng 2.2 ghi "tự nhiên" ở bốn hàng (FedProx, NaiveMix, FedMix, FedGen). Nếu muốn tính NaiveMix và FedMix là một công trình thì viết "ba công trình" |
| 10 | 2.2.2.3, đoạn 2, câu 1 (FedDF) | dùng logits của mô hình toàn cục trên một tập proxy | FedDF [13] dùng logits của mô hình toàn cục trên một tập proxy không cần nhãn làm mục tiêu chưng cất, và thực hiện việc chưng cất này ở máy chủ sau khi đã gộp mô hình. | FedDF [13] lấy trung bình logits của các mô hình client trên một tập proxy không cần nhãn làm mục tiêu, và chưng cất vào mô hình toàn cục ngay tại máy chủ, sau bước gộp tham số. | Sai nội dung công trình: FedDF chưng cất từ tập hợp các mô hình client vào mô hình toàn cục. Sửa tương ứng ô "logits của mô hình toàn cục trên tập proxy" ở hàng FedDF của Bảng 2.2 |
| 11 | 2.2.2.3, đoạn 1, câu 2 | thay vì so sánh tham số với tham số | Ý tưởng chung là dùng đầu ra của mô hình toàn cục trên một tập dữ liệu trung gian làm mục tiêu để mô hình cục bộ học theo, thay vì so sánh tham số với tham số. | Ý tưởng chung là dùng đầu ra của một mô hình trên một tập dữ liệu trung gian làm mục tiêu cho một mô hình khác học theo. | AI#1; câu cũ không đúng với FedDF (mô hình học theo là mô hình toàn cục, ở máy chủ) |
| 12 | 2.2.2.3, đoạn 2, câu cuối (FedGen) | rồi dùng bộ sinh đó tạo dữ liệu cho việc chưng cất | FedGen [15] loại bỏ nhu cầu về tập proxy bằng cách học một bộ sinh nhẹ ngay tại máy chủ, rồi dùng bộ sinh đó tạo dữ liệu cho việc chưng cất. | FedGen [15] loại bỏ nhu cầu về tập proxy bằng cách học một bộ sinh nhẹ ngay tại máy chủ; bộ sinh tạo biểu diễn đặc trưng theo nhãn và được phát xuống client để điều chuẩn huấn luyện cục bộ. | Sai nội dung công trình: bộ sinh của FedGen sinh trong không gian đặc trưng, được dùng ở client (đối chiếu lại bài báo trước khi sửa) |
| 13 | 2.2.1.3 (MOON), đoạn 1, câu 4 | Cơ chế của MOON như sau: | Cơ chế của MOON như sau: với cùng một ảnh cục bộ, ba mô hình cho ba biểu diễn khác nhau: mô hình toàn cục vừa nhận được từ máy chủ, mô hình cục bộ đang được huấn luyện, và mô hình cục bộ ở cuối vòng trước. | Với cùng một ảnh cục bộ, MOON lấy biểu diễn từ ba mô hình: mô hình toàn cục vừa nhận từ máy chủ, mô hình cục bộ đang huấn luyện, và mô hình cục bộ ở cuối vòng trước. | Hai dấu hai chấm trong một câu; AI#9 ("như sau") |
| 14 | 2.2.1.3, đoạn 2, câu 2 | FedProx và SCAFFOLD thao tác trên vector tham số của toàn mạng | FedProx và SCAFFOLD thao tác trên vector tham số của toàn mạng, đo khoảng cách giữa hai bộ tham số. | FedProx và SCAFFOLD thao tác trong không gian tham số của toàn mạng: FedProx phạt khoảng cách giữa hai bộ tham số, còn SCAFFOLD hiệu chỉnh hướng cập nhật. | Sai nội dung: SCAFFOLD không đo khoảng cách tham số (mâu thuẫn với đoạn SCAFFOLD ngay trên) |
| 15 | 2.2.1, đoạn mở, câu cuối | Biến kiểm soát của SCAFFOLD là một ước lượng gradient | Biến kiểm soát của SCAFFOLD là một ước lượng gradient, mà gradient được tính trực tiếp từ dữ liệu cục bộ, và cả dòng nghiên cứu về khôi phục dữ liệu từ gradient tồn tại vì lý do đó. | Chẳng hạn, biến kiểm soát của SCAFFOLD [8] là một ước lượng gradient, mà gradient được tính trực tiếp từ dữ liệu cục bộ nên vẫn mang thông tin về dữ liệu đó; các công trình khôi phục dữ liệu từ gradient dựa trên chính điều này. | §7.5: tên SCAFFOLD xuất hiện trước trích dẫn [8]; câu cũ không nói ra ý chính (gradient mang thông tin dữ liệu) |
| 16 | 2.2.2.1, đoạn 4, câu 3 | Hai thuật toán khác nhau ở hai chỗ cùng lúc, số hạng Taylor | Hai thuật toán khác nhau ở hai chỗ cùng lúc, số hạng Taylor được thêm vào, và mẫu trung bình bị rút khỏi lượt truyền xuôi. | Hai thuật toán khác nhau ở hai chỗ cùng lúc: số hạng Taylor được thêm vào, và mẫu trung bình bị rút khỏi lượt truyền xuôi. | Lỗi dấu câu: thiếu dấu hai chấm trước phần liệt kê |
| 17 | 2.2.2.1, đoạn 4, câu cuối | chênh lệch hiệu năng đo được giữa chúng không quy riêng cho chỗ nào được | Vì hai thay đổi này xảy ra đồng thời, chênh lệch hiệu năng đo được giữa chúng không quy riêng cho chỗ nào được. | **Xoá** | Lặp gần nguyên văn kết luận ở 2.3.1 đoạn 1 (nơi ý này thuộc về); AI#2 |
| 18 | 2.2.2.2 (VHL), câu 3–4 | đổi lại, mọi client chia sẻ chung một hệ quy chiếu | Vì tập ảo không chứa thông tin của bất kỳ người dùng nào, rủi ro riêng tư gần như bị loại bỏ hẳn; đổi lại, mọi client chia sẻ chung một hệ quy chiếu nhân tạo để căn chỉnh không gian đặc trưng về. Tuy nhiên, VHL yêu cầu nhãn. | Vì tập ảo không chứa thông tin của bất kỳ người dùng nào, rủi ro riêng tư gần như bị loại bỏ, và mọi client có chung một hệ quy chiếu nhân tạo để căn chỉnh không gian đặc trưng. | "Đổi lại" sai logic (vế sau là lợi ích, không phải cái giá); "Tuy nhiên, VHL yêu cầu nhãn" lặp với câu ngay sau ("các mẫu này bắt buộc phải có nhãn") |
| 19 | 2.2.2.4, đoạn 1, câu 1–2 | Phương pháp này xuất phát từ một quan sát thực nghiệm cụ thể | Phương pháp này xuất phát từ một quan sát thực nghiệm cụ thể. Quan sát ấy liên quan tới cách hai phần của mạng phân loại (bộ trích xuất đặc trưng và tầng phân lớp) chịu ảnh hưởng khác nhau bởi tính không đồng nhất của dữ liệu: … | Nhánh này xuất phát từ quan sát rằng hai phần của mạng phân loại (bộ trích xuất đặc trưng và tầng phân lớp) chịu ảnh hưởng khác nhau bởi tính không đồng nhất của dữ liệu: … | AI#9: câu đầu rỗng, bỏ đi đoạn vẫn đủ nghĩa |
| 20 | 2.2.2.5, đoạn 2, câu 2 | Mỗi client tính cho từng lớp, một prototype | Mỗi client tính cho từng lớp, một prototype trung bình đặc trưng của các mẫu thuộc lớp đó; … | Mỗi client tính, cho từng lớp, một prototype, tức trung bình đặc trưng của các mẫu thuộc lớp đó; … | Lỗi dấu phẩy làm câu khó đọc; "prototype trung bình đặc trưng" thiếu từ nối |
| 21 | 2.2.2, đoạn 3 | Sáu nhánh trình bày dưới đây có thể được đọc như | Sáu nhánh trình bày dưới đây có thể được đọc như những nỗ lực khác nhau nhằm giữ lại lợi ích của việc bổ sung thông tin mà giảm mức riêng tư phải đánh đổi; nhánh cuối cùng trình bày FedBR, công trình mà nền tảng của nó được luận văn dùng làm nền tảng thực nghiệm cho phần lệch phân phối nhãn kèm lệch phân phối đặc trưng. | Sáu nhánh dưới đây là những cách khác nhau để giữ lợi ích ấy với ít rủi ro riêng tư hơn. Nhánh cuối là FedBR, có bộ thực nghiệm công bố được luận văn dùng làm nền tảng thực nghiệm cho phần lệch phân phối nhãn kèm lệch phân phối đặc trưng. | Lặp gần nguyên văn câu ở 1.1 đoạn 5 ("có thể đọc như những nỗ lực giữ lại lợi ích ấy…"); "nền tảng của nó … làm nền tảng" lặp từ |
| 22 | 2.2.1.4 (đoạn cuối 2.2.1), câu 2 | Đó là ưu điểm lớn, đồng thời là trần của nó | Đó là ưu điểm lớn, đồng thời là trần của nó: nếu phân phối dữ liệu của các client thực sự khác nhau, thì không một thao tác nào trên quỹ đạo tối ưu hoá có thể cấp cho một client thông tin về những gì nó chưa bao giờ quan sát được. | Nhưng cũng vì vậy, hướng này không bổ sung được cho client thông tin về phần phân phối mà nó chưa quan sát. | Lặp gần nguyên văn câu chốt ở 1.1 đoạn 3; AI#2 |
| 23 | 2.3.2, đoạn 2, câu 1 | cho thấy tình trạng này không riêng ở NIID-Bench | Bảng 2.2 cho thấy tình trạng này không riêng ở NIID-Bench mà ở cả nhóm công trình được trình bày trong chương. | Bảng 2.2 cho thấy các công trình khác được trình bày trong chương cũng ở tình trạng này. | AI#8 (biến thể của "không chỉ… mà còn"); AI#1 |
| 24 | 2.3.2, đoạn 3, câu 1 | Hai hướng tác động lên những thành phần khác nhau của mô hình | Hai hướng tác động lên những thành phần khác nhau của mô hình: một bên điều chỉnh quỹ đạo tối ưu hoá, một bên bổ sung thông tin về phân phối dữ liệu. | Hướng can thiệp vào tối ưu hoá và hướng chia sẻ dữ liệu tác động theo hai cách khác nhau: một bên điều chỉnh quỹ đạo tối ưu hoá, một bên bổ sung thông tin về phân phối dữ liệu. | AI#9: chủ ngữ "hai hướng" không rõ chỉ gì ngay đầu đoạn; quỹ đạo tối ưu và thông tin dữ liệu không phải "thành phần của mô hình" |
| 25 | 2.3.2, đoạn 5, câu cuối | và luận văn cũng không giải quyết vấn đề này | NIID-Bench không đề xuất cách quy đổi độ nghiêm trọng của hai loại lệch về cùng một thang, và luận văn cũng không giải quyết vấn đề này. | NIID-Bench không đề xuất cách quy đổi độ nghiêm trọng của hai loại lệch về cùng một thang. | AI#4: câu rào, chuyển sang Ch.6 phần Hạn chế |
| 26 | 2.3.1, đoạn 4, câu 2 | chứa cả ảnh hưởng của ngân sách tinh chỉnh | …, và chênh lệch quan sát được chứa cả ảnh hưởng của ngân sách tinh chỉnh không đồng đều. | …, và chênh lệch quan sát được chứa cả ảnh hưởng của việc hai thuật toán được tinh chỉnh ở mức khác nhau. | AI#7: "ngân sách tinh chỉnh" là thuật ngữ tự đặt, chưa định nghĩa (đã bị nêu tên trong §7.7) |
| 27 | 2.3.1, đoạn 3, câu 3 | Kết quả này chứng minh mẫu trung bình toàn cục | Kết quả này chứng minh mẫu trung bình toàn cục phải mang thông tin thật, nhưng chưa chứng minh số hạng đạo hàm là thành phần cần thiết. | Kết quả này cho thấy mẫu trung bình toàn cục phải mang thông tin thật, nhưng chưa cho thấy số hạng đạo hàm là thành phần cần thiết. | Thực nghiệm "cho thấy", không "chứng minh" |
| 28 | 2.3.1, đoạn 5, câu 1 | dataset mở rộng từ tập dữ liệu chữ số viết tay MNIST | Bản thân FedMix có chạy trên FEMNIST (dataset mở rộng từ tập dữ liệu chữ số viết tay MNIST thiết kế cho FL), … | Bản thân FedMix có chạy trên FEMNIST (bản dành cho học liên kết của EMNIST, gồm chữ số và chữ cái viết tay, chia theo người viết), … | Trộn tiếng Anh "dataset"; FEMNIST gồm cả chữ cái (câu sau nói "ký tự khác nhau") |
| 29 | 2.2.2.1 (Mixup), câu 1 | thay vì huấn luyện trên từng mẫu riêng lẻ | …trong học tập trung: thay vì huấn luyện trên từng mẫu riêng lẻ, mô hình được huấn luyện trên các tổ hợp lồi của các cặp mẫu, … | …trong học tập trung: mô hình được huấn luyện trên các tổ hợp lồi của các cặp mẫu, … | AI#1 (vượt hạn ngạch) |
| 30 | 2.1.3, đoạn 1, câu 2 | Thay vì chia dữ liệu đều cho các client, ta rút | Thay vì chia dữ liệu đều cho các client, ta rút ngẫu nhiên một vector tỷ lệ từ phân phối Dirichlet rồi chia theo tỷ lệ đó. | Phân hoạch này rút ngẫu nhiên một vector tỷ lệ từ phân phối Dirichlet rồi chia dữ liệu theo tỷ lệ đó. | AI#1 (vượt hạn ngạch) |
| 31 | 2.2.2.5, đoạn 1 | Nhóm phương pháp này không sửa tầng phân lớp | Nhóm phương pháp này không sửa tầng phân lớp sau khi huấn luyện xong, mà ràng buộc không gian đặc trưng ngay trong lúc huấn luyện cục bộ. | Nhóm phương pháp này ràng buộc không gian đặc trưng ngay trong lúc huấn luyện cục bộ. | AI#1 (vượt hạn ngạch) |
| 32 | 2.2.2.6, đoạn 3, câu 2 | chứ không phải hai mẫu bất kỳ lấy từ hai phía | Cặp dương trong hàm mất mát là cặp gồm đặc trưng cục bộ và đặc trưng toàn cục của cùng một mẫu pseudo-data, chứ không phải hai mẫu bất kỳ lấy từ hai phía. | Cặp dương trong hàm mất mát gồm đặc trưng cục bộ và đặc trưng toàn cục của cùng một mẫu pseudo-data. | AI#1: hai khuôn tương phản trong cùng một đoạn (giữ câu "ghép cặp theo từng mẫu, không phải theo phân phối") |
| 33 | 2.1.3, đoạn 3 (quy ước Hsu), câu 1 | thường là phân phối đều, và do đó thoả | …, trong đó ⟨p⟩ là phân phối lớp tiên nghiệm, thường là phân phối đều, và do đó thoả ⟨Σ p_c = 1⟩. | …, trong đó ⟨p⟩ là phân phối lớp tiên nghiệm (thường là phân phối đều), nên ⟨Σ p_c = 1⟩. | Sai quan hệ nhân quả: tổng bằng 1 vì p là phân phối, không phải vì nó đều |
| 34 | 2.1.3, đoạn 2, câu 3 | mỗi thành phần nhỏ hơn một, khối lượng xác suất | Khi ⟨α⟩ mỗi thành phần nhỏ hơn một, khối lượng xác suất dồn về phía các đỉnh của đơn hình: … | Khi nồng độ ⟨α⟩ của mỗi thành phần nhỏ hơn một, khối lượng xác suất dồn về phía các đỉnh của đơn hình: … | Lỗi ngữ pháp: thiếu "nồng độ … của" |
| 35 | 2.1.1, đoạn 5, câu 2 | tốn băng thông khủng khiếp | …, và thuật toán tương đương SGD tập trung nhưng tốn băng thông khủng khiếp. | …, và thuật toán tương đương SGD tập trung nhưng tốn rất nhiều băng thông. | Từ khẩu ngữ, sai văn phong học thuật |
| 36 | 2.1.2, đoạn 1, câu 2 | công trình khảo sát thực nghiệm được trích dẫn rộng rãi nhất | NIID-Bench [5], công trình khảo sát thực nghiệm được trích dẫn rộng rãi nhất về chủ đề này, … | NIID-Bench [5], một công trình khảo sát thực nghiệm được trích dẫn rộng rãi về chủ đề này, … | Khẳng định so sánh nhất không có số liệu đi kèm |
| 37 | 2.2.1.1 (FedProx), câu 1 | và cũng được trích dẫn nhiều nhất | FedProx [7] là phương pháp đơn giản nhất trong nhóm và cũng được trích dẫn nhiều nhất. | FedProx [7] là phương pháp đơn giản nhất trong nhóm. | Khẳng định so sánh nhất không có số liệu đi kèm |

**Đếm hạn ngạch Chương 2.** Khuôn tương phản (AI#1): trước 9 (2.1.1 "Thay vì gom dữ liệu", 2.1.3 "Thay vì chia dữ liệu", Mixup "thay vì huấn luyện", FedMix "không còn … nữa, mà", chưng cất "thay vì so sánh tham số", 2.2.2.5 "không sửa … mà", FedBR "không phải theo phân phối" và "chứ không phải hai mẫu", 2.3.2 "không riêng … mà"); sau 3 (giữ 2.1.1 "Thay vì gom dữ liệu", đoạn FedMix "không còn … nữa, mà", FedBR "ghép cặp theo từng mẫu, không phải theo phân phối"). Gạch ngang chêm "—": trước 1 (2.1.2, "khác nhau — thiết bị ghi hình…"), sau 1; trong hạn ngạch, giữ nguyên. Câu rào (AI#4): trước 2 ("luận văn cũng không giải quyết vấn đề này", "Luận văn cũng không chạy cấu hình này"), sau 1 (câu ở dòng 2 nay là phát biểu sự thật về phạm vi, gắn với khoảng trống).

### Ghi chú ngoài phạm vi Chương 1–2 (không sửa trong bảng trên)

- Số trích dẫn ở Chương 4–5 lệch với danh mục trong Word: Bảng 5.3 ghi "CCVR [8]" (đúng là [10]; [8] là SCAFFOLD); Bảng 5.3 và mục 5.1.3 ghi "bài báo FedMix [1]" (đúng là [2]; [1] là Zhao); Bảng 5.8 và mục 5.3.2, 5.6 ghi "Bảng 1 của [2]" / "bảng công bố của [2]" cho FedBR (đúng là [3]); mục 4.4 ghi "cấu hình pseudo-data của [11]" (đúng là [3]; [11] là Mixup). Danh sách số trong đề bài ([1] FedMix, [2] FedBR, [8] CCVR, [9] Zhao, [11] VHL) khớp với các chỗ lệch này, không khớp với danh mục hiện có trong Word.
- Mục 5.1.3 vẫn nêu "NaiveMix" và "hiệu FedMix – NaiveMix" là phép so thăm dò, và Bảng 5.2 còn hàng "NaiveMix, FedMix", trong khi không bảng kết quả nào có NaiveMix.
- Hàng FedDF của Bảng 2.2 cần sửa theo dòng 10 của Chương 2.

## A2. Chương 3

Cách dùng: mỗi cụm ở cột *Tìm trong Word* đã được đếm là xuất hiện **đúng một lần** trong toàn văn bản (trừ hàng 4, xem ghi chú ở hàng). `⟨…⟩` là chỗ có công thức trong Word; giữ nguyên công thức, chỉ sửa chữ quanh nó. Không xét định dạng số, ký hiệu toán và caption.

### Đối chiếu với các khối rà 25/09 và 26/09 trong `03_chuong3.md`

- **Đã áp trong Word:** hàng 1–9, 11, 12 (dấu cách), 14–18 của khối 25/09; toàn bộ cấu trúc mục 3.5 của khối 26/09 (ký hiệu γ, biến thể Mixture và FedBR + Mixup, Beta nội dòng, tiểu mục 3.5.5); hàng 2–4 của khối "SỬA — 26/09".
- **Áp chưa đúng:** hàng 13 (25/09) đã chép vào Word nhưng ghi tên nguồn là "FedMix [3]" (xem hàng 14 dưới). Hàng 1 của "SỬA — 26/09" mới áp nửa sau, còn thiếu vế định nghĩa μ, γ (hàng 18 dưới).
- **Không cần nữa:** hàng 10 (25/09, "Tỷ" → "Tỉ"). Câu đứng trước nay cũng viết "Tỷ lệ", nên đoạn đã thống nhất.

### Bảng sửa

| # | Mục (section + paragraph) | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 3.1.1, đoạn "Mô hình được tách thành hai phần", câu 5 | `nó tập trung ở một trong hai thành phần` | Phép tách này cần thiết vì thiên lệch do dữ liệu không đồng nhất gây ra không phân bố đều trên mô hình: nó tập trung ở một trong hai thành phần. | Phép tách này cần thiết vì thiên lệch do dữ liệu không đồng nhất gây ra không phân bố đều trên mô hình: hai thành phần có thể bị lệch ở mức độ khác nhau và theo cơ chế khác nhau. | Mâu thuẫn với 3.4.1 ("nguồn lệch nằm cả ở ⟨ϕ⟩"), và 3.4 mới chỉ nêu giả thuyết |
| 2 | 3.1.2, câu mở đầu | `Ở vòng truyền thông (communication)` | Ở vòng truyền thông (communication), FedAvg [4] thực hiện ba bước: | Ở vòng truyền thông thứ ⟨t⟩ (communication round), FedAvg [4] thực hiện ba bước: | Ba bước dưới dùng ⟨θt⟩, ⟨St⟩ nhưng chưa giới thiệu ⟨t⟩; chú thích tiếng Anh bị cụt |
| 3 | 3.1.2, đoạn "Cần phân biệt client drift", câu cuối | `kiểm tra chúng bằng số đo..` | …là một câu hỏi tách biệt. Mục 3.4 nêu các giả thuyết về câu hỏi này, và Chương 5 kiểm tra chúng bằng số đo.. | …là một câu hỏi tách biệt, và mục 3.4 nêu các giả thuyết về câu hỏi này. | Dấu chấm kép; vế "Chương 5 kiểm tra…" lặp gần nguyên văn câu cuối của 3.1.1 |
| 4 | Tiêu đề 3.2 | `Mô hình hóa dữ liệu` (lần thứ hai; lần đầu nằm trong Mục lục) | Mô hình hóa dữ liệu không đồng nhất | Mô hình hoá dữ liệu không đồng nhất | Cả chương viết "hoá" (hình thức hoá, chuẩn hoá); sửa tiêu đề rồi cập nhật Mục lục |
| 5 | 3.2.2, đoạn "Theo quy ước trên", câu 1 | `cấu hình của nền tảng FedBR (Chương 5, mục 5.1)` | Theo quy ước trên, cấu hình của nền tảng FedBR (Chương 5, mục 5.1) ⟨α = 0.1⟩ trên CIFAR-10… | Theo quy ước trên, cấu hình của nền tảng FedBR (Chương 5, mục 5.1) là ⟨α = 0.1⟩ trên CIFAR-10… | Thiếu động từ "là" (sót khi áp hàng 7 của rà 25/09) |
| 6 | 3.2.3, đoạn dẫn trước ba gạch đầu dòng | `cả ba phải chi phối cách đọc` | Ba tính chất của cách mô phỏng này giới hạn phạm vi kết luận, và cả ba phải chi phối cách đọc toàn bộ phần thực nghiệm. | Ba tính chất của cách mô phỏng này giới hạn phạm vi kết luận về lệch đặc trưng. | Sai: nền tảng Flower không dùng phép xoay, nên không phải "toàn bộ phần thực nghiệm"; bỏ vế rào thứ hai (AI#4) |
| 7 | 3.2.3, gạch đầu dòng thứ hai, câu 5 | `chỉ xuất hiện trong hai tiền lệ` | Feature skew phụ thuộc lớp, trong đó phép biến đổi khác nhau theo từng lớp, chỉ xuất hiện trong hai tiền lệ nằm ngoài các benchmark Học liên kết chuẩn. | Feature skew phụ thuộc lớp, trong đó phép biến đổi khác nhau theo từng lớp, chỉ xuất hiện trong hai công trình [x], [y], cả hai nằm ngoài các benchmark Học liên kết chuẩn. *(Nếu không muốn thêm tài liệu: "…hiếm gặp và nằm ngoài các benchmark Học liên kết chuẩn.")* | "Hai tiền lệ" không trích dẫn (§7.5) |
| 8 | 3.3.3, đoạn "Khung Mean Augmented…" | `(MAFL) của FedMix [1]` | Khung Mean Augmented Federated Learning (MAFL) của FedMix [1] thay cặp… | Khung Mean Augmented Federated Learning (MAFL) của FedMix [2] thay cặp… | Danh mục tài liệu: [1] là Zhao và cộng sự, FedMix là [2] (Ch.1 đã dùng [2]) |
| 9 | 3.3.3, câu dẫn vào (3.12) | `cho thuật toán thứ nhất` | Thay trực tiếp vào (3.10) cho thuật toán thứ nhất: | Thay trực tiếp vào (3.10) cho thuật toán thứ nhất, NaiveMix: | Thân mục chưa gọi tên NaiveMix lần nào, chỉ có ở tiêu đề (§7.5) |
| 10 | 3.3.4, câu mở đầu | `Thuật toán thứ hai xuất phát` | Thuật toán thứ hai xuất phát từ nhận xét rằng khi ⟨λ ≪ 1⟩… | FedMix xuất phát từ nhận xét rằng khi ⟨λ ≪ 1⟩… | Gọi tên phương pháp (§7.5) |
| 11 | 3.3.4, đoạn "Tỷ lệ này nhận giá trị", câu 2 | `cả hai công trình gốc` | Ở đầu dưới của khoảng vận hành mà cả hai công trình gốc sử dụng, … | Ở đầu dưới của khoảng vận hành mà FedMix [2] và FedBR [3] sử dụng, … | §7.5: gọi tên thay cho "công trình gốc". Nếu "hai công trình" là hai bài khác thì thay tên cho đúng |
| 12 | 3.3.4, cùng đoạn, câu cuối | `Luận văn vì vậy giữ` | Luận văn vì vậy giữ ⟨λ⟩. cố định trong mỗi nền tảng thực nghiệm (Chương 5, mục 5.1) và không so mức cải thiện giữa hai giá trị ⟨λ⟩ khác nhau | Luận văn vì vậy giữ ⟨λ⟩ cố định trong mỗi nền tảng thực nghiệm (Chương 5, mục 5.1) và không so mức cải thiện giữa hai giá trị ⟨λ⟩ khác nhau. | Dấu chấm thừa sau ⟨λ⟩; thiếu dấu chấm cuối đoạn |
| 13 | 3.3.4, gạch đầu dòng thứ hai | `in trong bài báo FedMix [1]` | Công thức rút gọn in trong bài báo FedMix [1] viết… | Công thức rút gọn in trong bài báo FedMix [2] viết… | Như hàng 8 |
| 14 | 3.4.1, đoạn "Hiện tượng thứ hai", câu 1 | `được FedMix [3] ghi nhận` | Hiện tượng thứ hai, được FedMix [3] ghi nhận bằng thực nghiệm, … | Hiện tượng thứ hai, được FedBR [3] ghi nhận bằng thực nghiệm, … | Sai nguồn: ba hiện tượng là của FedBR; [3] là FedBR (áp chưa đúng từ rà 25/09, hàng 13) |
| 15 | 3.4.1, cùng đoạn, câu cuối | `Nói cách khác, label skew` | Nói cách khác, label skew sinh ra lệch trong không gian đặc trưng thông qua bộ trích xuất, không phải thông qua dữ liệu. | **Xoá** | Nhắc lại câu ngay trước và câu cuối đoạn 3.2.1; thêm một khuôn "không phải" (AI#1) và một câu chốt (AI#2) |
| 16 | 3.4.2, đoạn "Việc phân định quan trọng", câu cuối | `đòn bẩy trộn trung bình` | Khi đó câu hỏi tiếp theo là đòn bẩy trộn trung bình có xoay được ranh giới ấy không, hay chỉ tác động lên những chiều ít mang thông tin. | Khi đó câu hỏi tiếp theo là các cách dùng mẫu trung bình có xoay được ranh giới ấy không, hay chỉ tác động lên những chiều ít mang thông tin. | "Đòn bẩy trộn trung bình" là thuật ngữ tự đặt, chưa định nghĩa (AI#7) |
| 17 | 3.5.2, đoạn "Ở mỗi bước cục bộ", cuối đoạn | `được ghép với nhau theo chỉ số` (câu ngay trước chỗ sửa) | Với mỗi ⟨k⟩, đặt. ⟨a_k = …, b_k = …, c_k = …⟩ | Với mỗi ⟨k⟩, đặt ⟨a_k = …, b_k = …, c_k = …⟩. | Dấu chấm đặt nhầm trước công thức |
| 18 | 3.5.4, câu ngay sau (3.19) | `Các thực nghiệm ở Chương 5 dùng` | với ⟨y_k⟩ ở dạng one-hot. Các thực nghiệm ở Chương 5 dùng ⟨μ = 0.5⟩, ⟨γ = 1.0⟩ và ⟨τ1 = τ2 = 2.0⟩. | với ⟨y_k⟩ ở dạng one-hot, ⟨μ⟩ và ⟨γ⟩ là trọng số của hai thành phần. Các thực nghiệm ở Chương 5 dùng ⟨μ = 0.5⟩, ⟨γ = 1.0⟩ và ⟨τ1 = τ2 = 2.0⟩ (Bảng 5.2). | ⟨μ⟩, ⟨γ⟩ chưa được định nghĩa ở đâu (chưa áp từ rà 25–26/09) |
| 19 | 3.5.5, đoạn cuối | `Mục này không đánh giá phương pháp nào tốt hơn` | Mục này không đánh giá phương pháp nào tốt hơn. Chương 4 đặt ba cách dùng vào cùng một khung, và Chương 5 so sánh chúng bằng thực nghiệm. | Chương 4 đặt ba cách dùng vào cùng một khung, và Chương 5 so sánh FedMix và FedBR với FedAvg bằng thực nghiệm. | Sai: NaiveMix không được chạy. Bỏ câu rào (AI#4) |
| 20 | 3.6, đoạn mở | `Mục này cung cấp nền lý thuyết` | Mục này cung cấp nền lý thuyết để định vị nhóm phương pháp hiệu chuẩn tầng phân lớp từ thống kê lớp, mà CCVR [10] là công trình mẫu, và để làm rõ vì sao đối tượng nghiên cứu của luận văn nằm ngoài phạm vi của trần đó. | Mục này trình bày hai kết quả cổ điển đặt một giới hạn trên (gọi tắt là trần) cho nhóm phương pháp hiệu chuẩn tầng phân lớp từ thống kê lớp, mà CCVR [10] là công trình mẫu, rồi giải thích vì sao đối tượng nghiên cứu của luận văn nằm ngoài phạm vi của trần đó. | "Trần đó" trỏ tới thứ chưa được nói; định nghĩa "trần" ở lần đầu (AI#7) |
| 21 | 3.6.1, đoạn cuối | `Hai điều kiện của phát biểu` | Hai điều kiện của phát biểu phải được giữ nguyên khi trích dẫn. Kết quả là tiệm cận và trong kỳ vọng, dưới giả thiết Gaussian đúng với hiệp phương sai chung. Nó không phải một chặn cứng ở mọi cỡ mẫu. | Kết quả của Efron là tiệm cận và trong kỳ vọng, dưới giả thiết Gaussian đúng với hiệp phương sai chung. Ở cỡ mẫu hữu hạn, nó không chặn được từng lần đo. | Câu rào kiểu cãi phản biện (AI#4); khuôn "không phải" (AI#1) |
| 22 | 3.6.2, đoạn 1, câu 2 | `không thể vượt bộ phân biệt sinh` | Theo hai kết quả vừa nêu, một head phân biệt huấn luyện trên dữ liệu sinh từ một Gaussian không thể vượt bộ phân biệt sinh tương ứng trên tác vụ ảo ấy. | Theo hai kết quả vừa nêu, một tầng phân lớp phân biệt huấn luyện trên dữ liệu sinh từ một Gaussian, xét về tiệm cận, không vượt được bộ phân lớp sinh tương ứng (LDA) trên tác vụ ảo ấy. | "Không thể vượt" mâu thuẫn với 3.6.1 (kết quả chỉ là tiệm cận); "bộ phân biệt sinh" sai thuật ngữ; "head" chưa định nghĩa |
| 23 | 3.6.2, đoạn "Trần này có hai điều kiện", câu 2 | `nó áp cho tác vụ ảo, không cho phân phối thật` | Thứ nhất, nó áp cho tác vụ ảo, không cho phân phối thật. | Thứ nhất, nó chỉ áp cho tác vụ ảo. | Câu sau đã nói rõ phần phân phối thật; bớt một khuôn tương phản vì cùng trang với ba gạch đầu dòng ở 3.6.3 (AI#1) |
| 24 | 3.6.3, đoạn cuối, câu 2–3 | `không phải đối thủ trực tiếp` | CCVR và nhóm hiệu chuẩn tầng phân lớp không phải đối thủ trực tiếp mà là một họ song song, giải quyết cùng triệu chứng bằng cơ chế khác. Mục này có mặt trong luận văn không để so sánh hiệu năng, mà để xác định ranh giới áp dụng của một kết quả lý thuyết thường bị viện dẫn quá phạm vi trong văn liệu FL. | CCVR và nhóm hiệu chuẩn tầng phân lớp là một họ song song, giải quyết cùng triệu chứng bằng cơ chế khác. | Hai khuôn tương phản trong một đoạn (AI#1); câu cuối là câu rào kiêm câu chốt, và "thường bị viện dẫn quá phạm vi" không có trích dẫn |

### Đếm hạn ngạch

**Khuôn tương phản (AI#1: tối đa 3/chương, không quá 1/trang, không 2 trong một đoạn)**

| | Vị trí | Trước | Sau |
|---|---|---|---|
| 1 | 3.2.1 "hệ quả của việc huấn luyện, không phải của dữ liệu" | có | giữ (lần nêu ý đầu tiên) |
| 2 | 3.3.4 "hệ số … là ⟨λ(1−λ)⟩, không phải ⟨λ⟩" | có | giữ (chỗ phân định thật) |
| 3 | 3.4.1 "thông qua bộ trích xuất, không phải thông qua dữ liệu" | có | xoá (hàng 15) |
| 4 | 3.6.1 "Nó không phải một chặn cứng" | có | xoá (hàng 21) |
| 5 | 3.6.2 "áp cho tác vụ ảo, không cho phân phối thật" | có | xoá (hàng 23) |
| 6 | 3.6.3 ba gạch đầu dòng "X, không phải Y" | có | giữ, tính là một cấu trúc (câu của học viên, giữ theo AI#10 như rà 25/09) |
| 7 | 3.6.3 "không phải đối thủ trực tiếp mà là" | có | xoá (hàng 24) |
| 8 | 3.6.3 "không để so sánh hiệu năng, mà để" | có | xoá (hàng 24) |
| | **Tổng** | **8** (10 nếu đếm riêng từng gạch đầu dòng) | **3** (5 nếu đếm riêng từng gạch đầu dòng) |

Câu "căn chỉnh biên chỉ đòi …, còn (3.17) đòi …" ở 3.5.2 là phép đối song song, không thuộc khuôn "không phải… mà…"; giữ như rà 26/09 đã quyết.

**Dấu gạch ngang chêm "—" (AI#6):** trước 0, sau 0. Không câu mới nào dùng "—".

**Câu rào (AI#4: một câu mỗi chương):** giữ câu ở gạch đầu dòng thứ nhất 3.2.3 ("Luận văn chỉ chạy ở cấu hình mặc định này…"). Bỏ các câu rào ở 3.2.3 đoạn dẫn, 3.5.5, 3.6.1, 3.6.3 (hàng 6, 19, 21, 24).

**Cụm sáo cấm (AI#8):** 0 trước, 0 sau.

### Ghi chú ngoài bảng

- **Số trích dẫn.** Danh mục tài liệu hiện đánh số [1] Zhao và cộng sự, **[2] FedMix, [3] FedBR**, [4] FedAvg, [10] CCVR. Ch.1 và Ch.3 đã theo cách đánh số này (Ch.3 chỉ lệch ở FedMix [1], hàng 8 và 13). Ghi chú "FedBR là [2]" trong khối rà 25/09 đã cũ. Ch.5 vẫn dùng số cũ: "bài báo FedMix [1]", "Bảng 1 của [2]" cho FedBR, "CCVR [8]". Ch.4 còn "cấu hình pseudo-data của [11]". Hai chỗ này nằm ngoài Ch.3, cần một lượt rà riêng.
- **Ngoài phạm vi (ký hiệu toán):** ở 3.2.1, "mỗi client huấn luyện một bộ trích xuất riêng ⟨θi⟩" đang dùng ⟨θi⟩, trong khi bộ trích xuất là ⟨ϕi⟩ (3.4.1 dùng ⟨ϕi⟩). Nên xử lý trong lượt sửa ký hiệu.
- **Ch.5 so với quyết định "NaiveMix không chạy":** mục 5.1.3 liệt kê NaiveMix trong các phép so sánh thăm dò, và Bảng 5.2 có hàng "NaiveMix, FedMix". Cần xử lý ở Ch.5.

## A3. Chương 4

Nguồn: `ch4.txt` (khối 404–448). Mọi cụm ở cột "Tìm trong Word" đã đếm trong `all.txt`: mỗi cụm xuất hiện đúng 1 lần. ⟨…⟩ là chỗ công thức trong Word, giữ nguyên khi sửa.

Số trích dẫn theo danh mục Word ngày 28/09 (mục E).

| # | Mục (section + paragraph) | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 4.1, đoạn 1 ("Giai đoạn chuẩn bị ở client…"), chèn trước câu đầu | `Giai đoạn chuẩn bị ở client diễn ra một lần` | Giai đoạn chuẩn bị ở client diễn ra một lần, trước vòng truyền thông đầu tiên. | Khung gồm bốn giai đoạn: client tạo mẫu trung bình, máy chủ gom và phát lại chúng, client huấn luyện cục bộ, máy chủ tổng hợp tham số. Giai đoạn chuẩn bị ở client diễn ra một lần, trước vòng truyền thông đầu tiên. | (chưa áp) Word bỏ đoạn mở chương của bản md, nên "bốn giai đoạn" ở đoạn lớp ghi nhận, Thuật toán 4.1 và Hình 4.1 chưa được giới thiệu lần nào |
| 2 | 4.1, đoạn "Thuật toán 4.1 tóm tắt…" | `Cách dùng mẫu trung bình chỉ xuất hiện ở dòng 17` | Cách dùng mẫu trung bình chỉ xuất hiện ở dòng 17, qua hàm mất mát ⟨ℒ_g⟩; đổi ⟨g⟩ là đổi phương pháp, các dòng còn lại giữ nguyên. | Cách dùng mẫu trung bình nằm chủ yếu ở dòng 17, qua hàm mất mát ⟨ℒ_g⟩; đổi ⟨g⟩ là đổi phương pháp. Ngoài dòng 17, chỉ FedBR cần thêm hai chỗ: bỏ nhãn ở dòng 6 và cập nhật tầng chiếu ở dòng 18. | Sai với chính thuật toán: dòng 6 và 18 cũng đổi theo cách dùng |
| 3 | 4.1, đoạn mô tả Hình 4.1 | `Hình 4.1. là sơ đồ của khung` | Hình 4.1. là sơ đồ của khung, | Hình 4.1 là sơ đồ của khung, | Thừa dấu chấm sau số hình |
| 4 | 4.2, đoạn ký hiệu đứng trước chú thích Bảng 4.1 | `Bảng 4.1. Ba cách dùng mẫu trung bình trong khung` | Bảng 4.1. Ba cách dùng mẫu trung bình trong khung. ⟨x_i⟩ là ảnh cục bộ; … | Ký hiệu trong Bảng 4.1: ⟨x_i⟩ là ảnh cục bộ; … | Đoạn thân bài mở như một chú thích, lặp chú thích "Bảng 4.1." ngay dưới |
| 5 | 4.2.2, câu đầu | `FedMix xấp xỉ chính mục tiêu (3.12)` | FedMix xấp xỉ chính mục tiêu (3.12) | FedMix [2] xấp xỉ chính mục tiêu (3.12) | Mục mô tả phương pháp của người khác, cần trích dẫn |
| 6 | 4.2.2, câu cuối | `và là cách dùng mặc định của khung` | Đây là cơ chế xấp xỉ hàm mất mát bằng khai triển Taylor mà luận văn nghiên cứu, và là cách dùng mặc định của khung. | Đây là cơ chế xấp xỉ hàm mất mát bằng khai triển Taylor mà luận văn nghiên cứu. | Khung không có cách dùng mặc định (Thuật toán 4.1 để ⟨g⟩ tự chọn); vế này không có căn cứ |
| 7 | 4.2.3, câu đầu | `FedBR bỏ nhãn của mẫu trung bình` | FedBR bỏ nhãn của mẫu trung bình và dùng nó theo (3.19). | FedBR [3] bỏ nhãn của mẫu trung bình và dùng nó làm điểm tựa cho hai số hạng điều chuẩn của (3.19). | IR#11: mô tả FedBR phải kèm trích dẫn; nối chữ "điểm tựa" ở tiêu đề với nội dung (AI#7) |
| 8 | 4.3, bước 2 ("Số hạng thứ ba nhân gradient…") | `rồi lấy trung bình trên lô, tức chia cho` | …rồi lấy trung bình trên lô, tức chia cho ⟨B⟩ một lần nữa | …rồi lấy trung bình trên lô, tức chia cho ⟨B⟩ một lần nữa. | Thiếu dấu chấm cuối đoạn |
| 9 | 4.3, đoạn "Một phép thử số…", câu cuối | `nhỏ hơn công thức lần lượt 32 và 10 lần` | Với lô 32 và lô 10 dùng ở Chương 5, số hạng Taylor vì vậy nhỏ hơn công thức lần lượt 32 và 10 lần. | Với lô 32 và lô 10 dùng ở Chương 5, số hạng Taylor nhỏ hơn mức của (3.15) lần lượt 32 và 10 lần. | "nhỏ hơn công thức" so sai đối tượng; bớt một "vì vậy" (5 lần trong 4.3–4.4) |
| 10 | 4.3, đoạn "Mọi kết quả FedMix…", câu 1 | `và mỗi bảng kết quả ghi rõ điều đó` | Mọi kết quả FedMix trong luận văn đều dùng cách chuẩn hoá này, và mỗi bảng kết quả ghi rõ điều đó. | Mọi kết quả FedMix trong luận văn đều dùng cách chuẩn hoá này. | Sai: ghi chú Bảng 5.4 và 5.5 (FedMix trên Flower) không nhắc cách chuẩn hoá; chỉ Bảng 5.2, 5.8 có |
| 11 | 4.3, cùng đoạn, vế cuối | `không được đo trong luận văn` | …đã bị thu nhỏ ⟨B⟩ lần; biên độ của số hạng Taylor theo đúng (3.15) không được đo trong luận văn. | …đã bị thu nhỏ ⟨B⟩ lần. Số hạng Taylor ở đúng biên độ của (3.15) được thử ở Chương 5, mục 5.5, trong một cấu hình khác là FedBR cộng số hạng Taylor. | (chưa áp, khối SỬA 27/09) Câu cũ sai: mục 5.5 đã thử biên độ công thức |
| 12 | 4.3, ý "Phép co", câu cuối | `So sánh FedMix với FedAvg hay với NaiveMix` | So sánh FedMix với FedAvg hay với NaiveMix vì vậy luôn gộp cả ảnh hưởng của phép co. | So sánh FedMix với FedAvg vì vậy luôn gộp cả ảnh hưởng của phép co. | NaiveMix không được chạy; câu cũ gợi một phép so không có trong luận văn |
| 13 | 4.4, đoạn "⟨C_y = C⟩ khi nhãn mềm được gửi…" | `tới từng client, tốn` | Chiều xuống gửi toàn bộ ⟨V⟩ tới từng client, tốn ⟨N⟩ lần. | Chiều xuống gửi toàn bộ ⟨V⟩ tới từng client, tốn gấp ⟨N⟩ lần chiều lên. | Câu cụt: thiếu "gấp N lần cái gì" (bản md có "chừng ấy") |
| 14 | 4.4, đoạn ví dụ CIFAR-10 | `cấu hình pseudo-data của [11]` | Lấy cấu hình pseudo-data của [11]: | Lấy cấu hình pseudo-data của [3]: | (chưa áp) [11] là Mixup; FedBR là [3] trong danh mục Word |
| 15 | 4.4, đoạn ví dụ CIFAR-10, câu cuối | `và chỉ trả một lần` | Chi phí phụ trội của mẫu trung bình vì vậy dưới 1% lưu lượng của một vòng, và chỉ trả một lần. | Chi phí phụ trội của mẫu trung bình vì vậy dưới 1% lưu lượng của một vòng. | Lặp "trả một lần" ba câu trước; mục 4.4 đã có một câu chốt ở đoạn sau (AI#2) |
| 16 | 4.4, đoạn cuối, câu cuối | `nên luận văn đo nó bằng thời gian mỗi bước cục bộ` | Mức tốn thêm thực tế phụ thuộc phần cứng, nên luận văn đo nó bằng thời gian mỗi bước cục bộ quy về 1000 vòng truyền thông; số đo nằm ở mục 5.4. | Mức tốn thêm thực tế phụ thuộc phần cứng; Chương 5, mục 5.4 báo cáo số đo. | Cách đo thuộc Chương 5; Chương 4 chỉ trình bày đề xuất |

### Ghi chú không thành hàng

- **4.3, "Cách tính đó đi qua hai bước:"** Trong Word hai đoạn sau mất số 1, 2 (kiểu đoạn thường). Nên đặt lại danh sách đánh số; không phải sửa chữ.
- **Thuật toán 4.1, dòng 23:** bản trích ra "cấu hìnhlớp ghi nhận". Kiểm trong Word xem dấu ▷ trước "lớp ghi nhận" còn không.
- **Ngoài Ch.4 (để rà Ch.5):** 5.4 viết "Chi phí truyền thông tính theo thuật toán 4.1", phải là "công thức (4.1)"; 5.3.3 viết "Theo mục 4.1, chiều lên…", phải là "Theo (4.1)". Ch.5 trích FedBR [2], FedMix [1], lệch danh mục Word.

### Đếm hạn ngạch

| Hạng mục | Trước | Sau |
|---|---|---|
| AI#1 khuôn tương phản, theo lệnh rg ở §7.7 (`chứ không`, `không phải … mà`, `thay vì`) | 0 | 0 |
| AI#1 tính rộng (`thay cho` ở 4.3; "đáp ứng … nhưng không đáp ứng" ở 4.3) | 2 | 2 |
| AI#6 dấu gạch ngang chêm `—` | 0 | 0 |
| AI#8 cụm sáo | 0 | 0 |
| AI#4 câu rào | 1 ("Các kết quả ấy vì vậy nói về FedMix với số hạng Taylor đã bị thu nhỏ B lần") | 1 |
| "vì vậy" (nhịp nối lặp ở 4.3–4.4) | 5 | 4 |

## A4. Chương 5

Quy ước:
- "Tìm trong Word": chuỗi đã đếm trên `all.txt`, mỗi chuỗi xuất hiện đúng 1 lần, trừ chỗ có ghi chú riêng. Dán vào Ctrl+F.
- ⟨…⟩ là công thức (OMML), giữ nguyên trong Word, không gõ lại.
- Số bảng trong cột "Sau" theo đánh số của bản md (5.7 = bốn cách huấn luyện lại head, 5.8 = tái hiện, 5.9 = hiệu theo cặp, 5.10 = hiệu chuẩn theo M, 5.11 = thời gian, 5.12 = hướng A). Các số này chỉ đúng **sau khi** thêm dòng Caption còn thiếu cho bảng "Bốn cách huấn luyện lại tầng phân lớp" (khối 493/494); việc đánh số caption xử lý riêng.
- Số trích dẫn theo **danh mục tài liệu của Word**: [2] = FedMix, [3] = FedBR, [10] = CCVR. Bản md `05_chuong5.md` đã đổi theo danh mục này (28/09).
- Số thập phân trong cột "Sau" đã đổi sang dấu chấm theo quy ước ở mục C.

| # | Mục (section + paragraph) | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 5.1, đoạn mở | `chạy trên bộ thực nghiệm công bố cùng bài báo FedBR` | Các thí nghiệm còn lại chạy trên bộ thực nghiệm công bố cùng bài báo FedBR. | Các thí nghiệm còn lại chạy trên bộ thực nghiệm công bố cùng bài báo FedBR [3], gọi tắt là nền tảng FedBR. | "Nền tảng FedBR" dùng suốt chương mà chưa định nghĩa; thiếu trích dẫn (bản md đã sửa) |
| 2 | 5.1.1, Bảng 5.2, hàng "NaiveMix, FedMix" | `mỗi bước cục bộ nhận 32 mẫu trung bình mới` (nằm cùng hàng) | Ô đầu hàng: NaiveMix, FedMix | Ô đầu hàng: FedMix | Quyết định 28/09: không chạy NaiveMix |
| 3 | 5.1.1, đoạn sau Bảng 5.2 | `Cách lấy mẫu trung bình của NaiveMix và FedMix` | Cách lấy mẫu trung bình của NaiveMix và FedMix giữ đúng như [3], … | Cách lấy mẫu trung bình của FedMix giữ đúng như [3], … | Quyết định 28/09: bỏ NaiveMix |
| 4 | 5.1.3, đoạn 1, câu 2 | `Cả hai dùng` | Cả hai dùng ⟨λ = 0.1⟩; FedMix dùng cách chuẩn hoá số hạng Taylor nêu ở Chương 4, mục 4.3. | FedMix dùng ⟨λ = 0.1⟩, giá trị mặc định của [3], và cách chuẩn hoá số hạng Taylor nêu ở Chương 4, mục 4.3. | Sai: S1 (FedBR − FedAvg) không có λ; thêm nguồn của giá trị λ (bản md đã sửa) |
| 5 | 5.1.3, đoạn 1, câu cuối | `Các phép so sánh khác là thăm dò` | Các phép so sánh khác là thăm dò: FedProx, NaiveMix, FedBR + Mixup, và hiệu FedMix – NaiveMix. | Các phép so sánh khác là thăm dò: FedProx, FedAvg + Mixup và FedBR + Mixup. | Quyết định 28/09: bỏ NaiveMix và hiệu FedMix − NaiveMix; thêm FedAvg + Mixup cho khớp Bảng 5.9 |
| 6 | 5.1.3, đoạn 2 (cả đoạn) | `so hai cách dùng cùng một thông tin` | Hiệu FedMix − NaiveMix so hai cách dùng cùng một thông tin: … khi quét ⟨λ⟩ ở phụ lục, NaiveMix tốt nhất đạt 80,6%. | **Xoá** | Quyết định 28/09: không còn phép đo nào để đọc; đoạn cũng trích sai FedMix là [1] |
| 7 | 5.2.1, đoạn giải thích Bảng 5.3 | `là nồng độ Dirichlet mỗi thành phần, lấy mẫu trên trục client` | Bảng 5.3. Thiết lập thực nghiệm trên nền tảng Flower. ⟨β⟩ là nồng độ Dirichlet mỗi thành phần, … | Trong Bảng 5.3, ⟨β⟩ là nồng độ Dirichlet mỗi thành phần, … | Mở đoạn bằng câu trùng caption |
| 8 | 5.2.1, Bảng 5.3, hàng Backbone | `phụ lục bài báo FedMix [1]` | … theo phụ lục bài báo FedMix [1]: … | … theo phụ lục bài báo FedMix [2]: … | Trích dẫn sai: [1] là Zhao và cộng sự |
| 9 | 5.2.1, Bảng 5.3, hàng Hiệu chuẩn | `CCVR [8]` | CCVR [8] với ⟨M_c ∈ {100; 2000}⟩ | CCVR [10] với ⟨M_c ∈ {100; 2000}⟩ | Trích dẫn sai: [8] là SCAFFOLD; Ch.2 trích CCVR là [10] |
| 10 | 5.2.2, đoạn giải thích Bảng 5.4 | `Bảng 5.4. Độ chính xác cao nhất theo vòng (%) của FedAvg và FedMix trên` | Bảng 5.4. Độ chính xác cao nhất theo vòng (%) của FedAvg và FedMix trên CIFAR-10, … | Bảng 5.4 cho độ chính xác cao nhất theo vòng (%) của FedAvg và FedMix trên CIFAR-10, … | Mở đoạn bằng câu trùng caption |
| 11 | 5.2.2, đoạn giải thích Bảng 5.5 | `Hai biến thể thăm dò của FedMix. C1` | Bảng 5.5. Hai biến thể thăm dò của FedMix. C1: mỗi client gửi … | Bảng 5.5 gồm hai biến thể thăm dò của FedMix. C1: mỗi client gửi … | Mở đoạn bằng câu trùng caption |
| 12 | 5.2.2, đoạn sau Bảng 5.5, câu cuối | `Hai biến thể này chỉ là thăm dò` | Hai biến thể này chỉ là thăm dò. | **Xoá** | Câu rào lặp lại caption (AI#4) |
| 13 | 5.2.3, đoạn giải thích Bảng 5.6 | `Bảng 5.6. Mức chênh độ chính xác của CCVR so với` | Bảng 5.6. Mức chênh độ chính xác của CCVR so với mô hình trước hiệu chuẩn, … | Bảng 5.6 ghi mức chênh độ chính xác của CCVR so với mô hình trước hiệu chuẩn, … | Mở đoạn bằng câu trùng caption |
| 14 | 5.2.3, đoạn giải thích Bảng 5.7 | `Bảng 5.7. Bốn cách huấn luyện lại` | Bảng 5.7. Bốn cách huấn luyện lại tầng phân lớp từ cùng một thống kê lớp, trên cùng mô hình … | Bảng 5.7 so bốn cách huấn luyện lại tầng phân lớp từ cùng một thống kê lớp, trên cùng mô hình … | Mở đoạn bằng câu trùng caption. Đoạn này chưa có dòng Caption đi kèm, cần thêm "Bảng 5.7. Bốn cách huấn luyện lại tầng phân lớp" (cùng đợt đánh số) |
| 15 | 5.2.3, đoạn giải thích Bảng 5.7 | `chỉ để đọc mô tả` | … nên cột CINIC-10 chỉ để đọc mô tả, không dùng để suy luận thống kê. | … nên cột CINIC-10 chỉ mang tính mô tả. | Khuôn tương phản kèm câu rào (AI#1, AI#4) |
| 16 | 5.2.4, đoạn 3, câu cuối | `Phép đo này làm trên backbone` | Phép đo này làm trên backbone không dùng chuẩn hoá theo lô. | **Xoá** | Câu rào; Bảng 5.1 và 5.3 đã ghi backbone không chuẩn hoá theo lô, giới hạn dồn về Ch.6 §6.3 (AI#4) |
| 17 | 5.3.1, đoạn giải thích Bảng 5.8 | (1) `Bảng 5.8. Độ chính xác (%) trên CIFAR-10 xoay` (2) `giá trị công bố trong Bảng 1 của [2]` | Bảng 5.8. Độ chính xác (%) trên CIFAR-10 xoay, … Cột thứ hai là giá trị công bố trong Bảng 1 của [2]; … | Các số trong Bảng 5.8 là độ chính xác (%) trên CIFAR-10 xoay, … Cột thứ hai là giá trị công bố trong Bảng 1 của [3]; … | Mở đoạn trùng caption, và đoạn liền trước cũng mở bằng "Bảng 5.8" (AI#5); [2] là FedMix |
| 18 | 5.3.1, caption bảng tái hiện | `Kết quả chạy lại công bố của FedBR` (2 lần: dòng Caption và Danh mục bảng; sửa ở Caption rồi cập nhật danh mục) | Kết quả chạy lại công bố của FedBR | Kết quả chạy lại so với bảng công bố của FedBR | Tên bảng tối nghĩa ("chạy lại công bố") |
| 19 | 5.3.1, đoạn cuối | (1) `cũng cho biết hai lần chạy cùng một cấu hình` (2) `giờ (Bảng 5.10)` | Bảng 5.7 cũng cho biết hai lần chạy … mất khoảng 7.5 giờ (Bảng 5.10). | Bảng 5.8 cũng cho biết hai lần chạy … mất khoảng 7.5 giờ (Bảng 5.11). | Số bảng sai sau khi thêm caption còn thiếu |
| 20 | 5.3.2, đoạn mở | `đặt các cách dùng mẫu trung bình cạnh FedAvg` | Bảng 5.8 đặt các cách dùng mẫu trung bình cạnh FedAvg và FedProx, trên cùng lượt chạy của Bảng 5.7. | Bảng 5.9 đặt các cách dùng mẫu trung bình cạnh FedAvg và FedProx, trên cùng lượt chạy của Bảng 5.8. | Hai số bảng đều sai |
| 21 | 5.3.2, đoạn giải thích Bảng 5.9 | (1) `Bảng 5.8. Hiệu theo cặp so với FedAvg trên nền tảng FedBR` (2) `FedMix và NaiveMix dùng` | Bảng 5.8. Hiệu theo cặp so với FedAvg trên nền tảng FedBR (…), seed 12345. … FedMix và NaiveMix dùng ⟨λ = 0.1⟩; FedMix dùng cách chuẩn hoá ở Chương 4, mục 4.3, … | Các hiệu trong Bảng 5.9 là hiệu theo cặp so với FedAvg trên nền tảng FedBR (…), seed 12345. … FedMix dùng ⟨λ = 0.1⟩ và cách chuẩn hoá ở Chương 4, mục 4.3, … | Mở đoạn trùng caption, số bảng sai, đoạn liền trước cũng mở bằng "Bảng 5.9"; bỏ NaiveMix (28/09) |
| 22 | 5.3.2, đoạn S1 | `Bảng 1 của [2] cho FedBR` | Bảng 1 của [2] cho FedBR hơn FedAvg 5.66 điểm, … | Bảng 1 của [3] cho FedBR hơn FedAvg 5.66 điểm, … | Trích dẫn sai: FedBR là [3] |
| 23 | 5.3.2, đoạn S2 | `Công bố của FedBR báo cáo` | (Công bố của FedBR báo cáo kém 1.62 điểm) | (bài báo FedBR [3] báo cáo kém 1.62 điểm) | Viết hoa giữa câu; thiếu trích dẫn |
| 24 | 5.3.3, đoạn thủ tục | `mỗi thuật toán trong Bảng 5.7` | … của mỗi thuật toán trong Bảng 5.7 và đóng băng … | … của mỗi thuật toán trong Bảng 5.8 và đóng băng … | Số bảng sai |
| 25 | 5.3.3, đoạn chi phí | `Theo mục 4.1` | Theo mục 4.1, chiều lên với … | Theo công thức (4.1), chiều lên với … | Sai tham chiếu: chi phí truyền thông là công thức (4.1), mục 4.1 là kiến trúc khung |
| 26 | 5.3.3, đoạn giải thích Bảng 5.10 | `Bảng 5.9. Mức thay đổi độ chính xác trên phần dữ liệu giữ lại (điểm` | Bảng 5.9. Mức thay đổi độ chính xác trên phần dữ liệu giữ lại (điểm phần trăm) khi thay … | Bảng 5.10 ghi mức thay đổi độ chính xác trên phần dữ liệu giữ lại (điểm phần trăm) khi thay … | Mở đoạn trùng caption; số bảng sai |
| 27 | 5.3.3, đoạn giải thích Hình 5.1 | `Số liệu của Bảng 5.10 vẽ theo` | Hình 5.1. Số liệu của Bảng 5.10 vẽ theo ⟨M⟩. | Hình 5.1 vẽ số liệu của Bảng 5.10 theo ⟨M⟩. | Mở đoạn trùng caption |
| 28 | 5.3.3, câu dẫn ba nhận xét | `và hình 5.1 cho ba nhận xét` | Bảng 5.9 và hình 5.1 cho ba nhận xét sau: | Bảng 5.10 và Hình 5.1 cho ba nhận xét. | Số bảng sai; "Hình" viết hoa; dấu hai chấm treo trước đoạn mới |
| 29 | 5.3.3 nhận xét thứ nhất; 5.6 đoạn 3 | (1) `việc hiệu chuẩn làm giảm độ chính xác của mọi mô hình` (2) `sụt từ 14 đến 54 điểm` | … làm giảm độ chính xác của mọi mô hình, từ 14 đến 54 điểm. / … làm mọi mô hình sụt từ 14 đến 54 điểm … | … làm giảm độ chính xác của mọi mô hình, từ 13 đến 54 điểm. / … làm mọi mô hình sụt từ 13 đến 54 điểm … | Sai số: Moon ở ⟨M = 10⟩ là −12,96 |
| 30 | 5.3.3, nhận xét thứ hai | `trong huấn luyện được từ` | Các phương pháp không tác động trực tiếp lên tầng phân lớp trong huấn luyện được từ +3.9 đến +5.8 điểm; FedBR và FedBR + Mixup chỉ được +1.3 và +1.7. | Không tính Moon, các phương pháp không tác động trực tiếp lên tầng phân lớp trong huấn luyện được từ +3.9 đến +5.8 điểm, riêng FedAvg + Mixup chỉ được +1.0; FedBR và FedBR + Mixup chỉ được +1.3 và +1.7. | Câu gốc sai với Bảng 5.10 (FedAvg + Mixup +1,03, Moon +10,95). Học viên xem lại câu "tách hai nhóm" |
| 31 | 5.4, đoạn 1 | (1) `tính theo thuật toán 4.1` (2) `nhật ký của lượt chạy ở Bảng 5.7` | Chi phí truyền thông tính theo thuật toán 4.1. … trong nhật ký của lượt chạy ở Bảng 5.7. | Chi phí truyền thông tính theo công thức (4.1). … trong nhật ký của lượt chạy ở Bảng 5.8. | Thuật toán 4.1 là khung huấn luyện, chi phí là công thức (4.1); số bảng sai |
| 32 | 5.4, đoạn giải thích Bảng 5.11 | `Bảng 5.10. Thời gian huấn luyện quy về` | Bảng 5.10. Thời gian huấn luyện quy về 1000 vòng truyền thông, lượt chạy một seed ở Bảng 5.7. Cột cuối là tỉ lệ so với FedAvg. Thực nghiệm chạy trên 2 GPU RTX 3060 12GB VRAM | Bảng 5.11 ghi thời gian huấn luyện quy về 1000 vòng truyền thông của lượt chạy một seed ở Bảng 5.8. Cột cuối là tỉ lệ so với FedAvg. Thực nghiệm chạy trên 2 GPU RTX 3060, mỗi GPU 12 GB VRAM. | Mở đoạn trùng caption; hai số bảng sai; câu cuối thiếu dấu chấm |
| 33 | 5.5, đoạn mở | `còn FedMix thì không` | Mục 5.3.2 cho thấy FedBR là cách dùng mẫu trung bình duy nhất vượt ngưỡng đọc, còn FedMix thì không. | Ở mục 5.3.2, FedMix nằm dưới ngưỡng đọc và FedBR là cách dùng mẫu trung bình duy nhất vượt ngưỡng. | Khuôn tương phản vượt hạn ngạch (AI#1); nhiều đoạn liền mở bằng "Mục …" (AI#5) |
| 34 | 5.5.1, đoạn cuối | (1) `như FedBR ở Bảng 5.2` (2) `được xác định trước khi chạy thực nghiệm` | … như FedBR ở Bảng 5.2; 1000 vòng. Bốn cấu hình và các phép so sánh này được xác định trước khi chạy thực nghiệm. | … như FedBR ở Bảng 5.2; seed 12345; 1000 vòng. Bốn cấu hình và các phép so sánh này được xác định trước khi chạy thực nghiệm. ↵ *(đoạn mới)* Các lượt chạy này đánh giá mỗi 2 vòng, dày hơn lượt chạy ở Bảng 5.8 (mỗi 5 vòng). Chỉ số chọn năm mốc cao nhất được lợi khi có nhiều mốc hơn, nên Bảng 5.12 tính mọi chỉ số trên 101 mốc chung của hai lịch đánh giá, tức mỗi 10 vòng. | Thiếu seed; caption Bảng 5.12 nhắc "101 mốc chung" mà thân bài không giải thích (bản md đã sửa) |
| 35 | 5.5.2, đoạn giải thích Bảng 5.12 | (1) `Bảng 5.11. FedBR cộng` (2) `lệch nhẹ so với Bảng 5.8` | Bảng 5.11. FedBR cộng các số hạng mẫu trung bình của FedMix theo (5.1), … lệch nhẹ so với Bảng 5.8. | Bảng 5.12 ghi kết quả của FedBR khi cộng các số hạng mẫu trung bình của FedMix theo (5.1), … lệch nhẹ so với Bảng 5.9. | Mở đoạn trùng caption; số bảng sai (hàng FedAvg, FedBR lấy từ bảng hiệu theo cặp) |
| 36 | 5.5.2, caption Bảng 5.12 và Hình 5.2 | Dòng Caption ngay sau đoạn `Bảng 5.11. FedBR cộng`; dòng Caption ngay trước đoạn `Số hạng nhãn (II) không tạo khác biệt đo được` | Caption bảng chỉ có "Bảng 5.11." Caption hình chỉ có "Hình 5.2.", không có đoạn giải thích hình. | Tên bảng: "FedBR cộng các số hạng mẫu trung bình của FedMix". Tên hình: "Đường học của FedAvg, FedBR và bốn cấu hình của (5.1)". Thêm đoạn trước hình: "Hình 5.2 vẽ đường học của FedAvg, FedBR và bốn cấu hình của (5.1), seed 12345; trục tung là độ chính xác trên phần dữ liệu giữ lại của các client. Màu tím là FedBR + (II) không có (III), màu cam là cấu hình có (III); nét liền ứng với nhãn mềm, nét đứt ứng với nhãn đều. Dấu × đánh dấu vòng hàm mất mát thành NaN, sau đó mô hình chỉ còn đoán ngẫu nhiên." | Bảng và hình phải có tên; hình chưa có chú giải màu và nét |
| 37 | 5.5.2, đoạn cuối | `làm thời gian tăng từ khoảng` | Trong cùng loạt chạy, (III) làm thời gian tăng từ khoảng 8.7–8.8 lên 9.9–10.0 giờ mỗi 1000 vòng. | Trong cùng loạt chạy, (III) làm thời gian tăng từ khoảng 8.7–8.8 lên 9.9–10.0 giờ mỗi 1000 vòng. Loạt chạy này khác thời điểm với Bảng 5.11, nên con số không đặt cạnh bảng đó. | 8,7 giờ khi không có (III) trông mâu thuẫn với 7,5 giờ của FedBR ở Bảng 5.11 (bản md đã sửa) |
| 38 | 5.6, đoạn 2 | `bảng công bố của [2]` | … cùng chiều và cùng cỡ với bảng công bố của [2] (mục 5.3.2). | … cùng chiều và cùng cỡ với bảng công bố của [3] (mục 5.3.2). | Trích dẫn sai: FedBR là [3] |
| 39 | 5.6, đoạn 3, câu cuối | `thời gian của FedAvg (Bảng 5.10)` | … khoảng 3.3 lần thời gian của FedAvg (Bảng 5.10). | … khoảng 3.3 lần thời gian của FedAvg (Bảng 5.11). | Số bảng sai |
| 40 | 5.6, đoạn 4, câu cuối | `nên phép đo này chỉ có trên Flower` | Nhật ký của nền tảng FedBR không ghi các đại lượng theo lớp, nên phép đo này chỉ có trên Flower. | **Xoá** | Lặp mục 5.1.2; câu mở đoạn đã ghi "Trên nền tảng Flower"; câu rào (AI#4) |

### Ghi chú ngoài bảng

- **Đã đúng trong Word, không cần sửa:** đoạn "Giới hạn của các kết luận." không có trong Word; không còn `[CHỜ SỐ LIỆU: T1]` hay hàng NaiveMix trong bảng hiệu theo cặp. "Seed" dùng thống nhất trong Ch.5 (0 lần "hạt giống" trong toàn bộ file Word).
- **Mâu thuẫn với quyết định 28/09 ở chương khác (ngoài phạm vi Ch.5):** khối 238 (Ch.2, mục 2.4.1) kết bằng "…khoảng trống được nêu để giới hạn cách đọc phép so FedMix với NaiveMix ở Chương 5"; khối 255 (phần đóng góp) viết "phép đối chứng giữa FedMix và NaiveMix được thực hiện lại trong khung, ở cùng một trọng số trộn và với nhiều seed ngẫu nhiên". Cả hai giờ không còn đúng.
- **Trích dẫn sai ở chương khác:** "FedMix [1]" ở khối 323 và 340, "FedMix [3]" ở khối 348 (Ch.3), "cấu hình pseudo-data của [11]" ở khối 446 (Ch.4; [11] là Mixup, đúng ra là [3]).
- **Mục 5.5.3 "Đọc kết quả"** có trong bản md nhưng không có trong Word. Không có mục này thì chương không giải thích vì sao FedMix (số hạng Taylor chia cho B) huấn luyện ổn định còn (III) ở đúng biên độ công thức lại làm phân kỳ. Học viên tự quyết định có chép vào hay không. Nếu chép thì chương thêm một câu rào ("Cách giải thích này chưa được kiểm chứng"), nên bỏ bớt một câu rào khác.

### Đếm hạn ngạch

| Chỉ tiêu | Trước | Sau | Ghi chú |
|---|---|---|---|
| Khuôn tương phản (AI#1), đếm cả biến thể "X, không Y" và "còn … thì không" | 4 (khối 455, 493, 528, 540) | 2 (455, 528) | Regex chặt `chứ không\|không phải .*mà \|thay vì` ra 0/0. Hai chỗ "thay cho" (480, 483) chỉ mô tả, không tính. Không đoạn nào có hai khuôn |
| Gạch ngang chêm "—" trong văn xuôi (AI#6) | 0 | 0 | "—" chỉ có trong ô bảng; chương khoảng 16 trang (tr. 51–66) |
| Câu rào (AI#4) | 8 (482, 486, 493, 499, 508, 521, 557, 560) | 5 (482, 493 đã rút gọn, 508, 521, 557) | Năm câu còn lại đều mang thông tin cần cho việc đọc bảng. Câu kết của đoạn 557 (5.6) là câu rào nên giữ nhất |
| Cụm sáo cấm (AI#8) | 0 | 0 | |
| Đoạn mở bằng "Bảng 5.x." / "Hình 5.x." trùng caption | 11 | 0 | Hàng 7, 10, 11, 13, 14, 17, 21, 26, 27, 32, 35 |
| Tham chiếu "Bảng 5.x" sai số (so với đánh số của md), kể cả số trong đoạn mở | 14 | 0 | Hàng 19–21, 24, 26, 28, 31, 32, 35, 39 |

## B. Chú thích bảng, hình

Trong Word, chú thích dùng trường tự đánh số (Insert Caption), còn các chỗ nhắc "Bảng 5.x" trong thân bài là chữ gõ tay. Quy ước đang dùng trong Word: chú thích nằm **phía trên** cả bảng lẫn hình; đoạn diễn giải của học viên đứng ngay trước chú thích. Bảng này giữ quy ước đó.

| # | Vị trí | Hiện trạng | Sửa | Lý do |
|---|---|---|---|---|
| B1 | Ch.5, 5.2.3, bảng "Head · CIFAR-10 · CINIC-10" (ngay sau đoạn "Bảng 5.7. Bốn cách huấn luyện lại tầng phân lớp…") | **không có chú thích** | chèn chú thích **"Bảng 5.7. Bốn cách huấn luyện lại tầng phân lớp từ cùng một thống kê lớp"** (References → Insert Caption, nhãn Bảng) | Thiếu chú thích nên mọi bảng sau bị trường tự động đánh lùi một số: bảng tái hiện đang là 5.7 thay vì 5.8, …, bảng hướng A đang là 5.11 thay vì 5.12. Chèn xong, các chú thích sau tự đúng; chỗ nhắc trong thân bài sửa theo phần A4 (Ch.5) |
| B2 | Ch.5, 5.5.2, chú thích đang là "Bảng 5.11." (sau B1 thành 5.12) | chỉ có số, không có tên | **"Bảng 5.12. FedBR cộng các số hạng mẫu trung bình của FedMix"** | Thiếu tên |
| B3 | Ch.5, 5.5.2, chú thích "Hình 5.2." | chỉ có số, không có tên | **"Hình 5.2. Đường học của FedAvg, FedBR và bốn cấu hình của (5.1)"** | Thiếu tên |
| B4 | Ch.5, 5.3.1, chú thích "Bảng 5.7 Kết quả chạy lại công bố của FedBR" | thiếu dấu chấm sau số; tên đọc ngược nghĩa | **"Bảng 5.8. Kết quả chạy lại so với bảng công bố của FedBR"** (số tự nhảy sau B1) | Các chú thích khác đều có dạng "Bảng x.y. Tên" |
| B5 | Ch.5, 5.1.1, chú thích "Bảng 5.1. Hai nền tảng thực nghiệm." | có dấu chấm cuối | bỏ dấu chấm cuối | Các chú thích khác không có dấu chấm cuối |
| B6 | Ch.4, 4.1, đoạn "Hình 4.1. là sơ đồ của khung…" | dư dấu chấm sau "4.1" | "Hình 4.1 là sơ đồ của khung…" | Lỗi đánh máy |
| B7 | Ch.4, Hình 4.1 và Thuật toán 4.1 | tham số mô hình ký hiệu $w$ | thay ảnh Hình 4.1 bằng `paper/thesis/figures/hinh4_1.png` mới (đã vẽ lại với $\theta$); trong Thuật toán 4.1 đổi $w$ thành $\theta$ (xem mục D) | Ch.2, Ch.3 dùng $\theta$ cho tham số |
| B8 | Ch.2, Ch.4, Ch.5: các đoạn diễn giải mở đầu bằng "Bảng x.y. …" / "Hình x.y. …" | đọc như chú thích lặp hai lần | viết câu mở tự nhiên, ví dụ "Bảng 5.3 ghi thiết lập…", "Trong Bảng 5.4, …" | Liệt kê từng đoạn ở phần A của từng chương (A1–A4) |

**Không thiếu chú thích** ở Ch.1, Ch.3 (không có bảng, hình), Ch.2 (Bảng 2.1, 2.2 đủ), Ch.4 (Bảng 4.1, Hình 4.1, Thuật toán 4.1 đủ).

## C. Định dạng số

Quy ước theo học viên: **dấu chấm thập phân**; **dấu phẩy phân tách hàng nghìn** cho số từ 5 chữ số trở lên (20,000; 50,000); số 4 chữ số viết liền (1000 vòng, 2000 mẫu, 3072). Khi dấu chấm là dấu thập phân, các phần tử trong tập hợp hoặc tham số cách nhau bằng dấu phẩy, không dùng dấu chấm phẩy. Bảng số liệu trong Word đã dùng dấu chấm; các chỗ dưới đây còn sót.

| # | Chương | Tìm trong Word | Sửa | Ghi chú |
|---|---|---|---|---|
| C1 | Ch.2 | `VHL cần khoảng 2.000 mẫu ảo` | "2.000" → "2000"; "20.000" → "20,000" | dấu chấm đang làm dấu nghìn |
| C2 | Ch.2 | Bảng 2.2, hàng VHL, ô "Thông tin chia sẻ thêm" | "~2,000" → "~2000" | số 4 chữ số viết liền, khớp C1 |
| C3 | Ch.2 | công thức trong đoạn `Với CIFAR-10, tức 10 lớp chia cho 10 bên` | "0,5" → "0.5"; "α = 0,1" → "α = 0.1" | cùng đoạn đã có "0.5", "0.05" |
| C4 | Ch.3 | công thức trong đoạn `trọng số trộn rút từ phân phối` | "Beta(0.2; 0.2)" → "Beta(0.2, 0.2)" | dấu chấm phẩy → dấu phẩy |
| C5 | Ch.3 | công thức trong đoạn `Các thực nghiệm ở Chương 5 dùng` | "τ1 = τ2 = 2.0" → "τ1 = τ2 = 2" | khớp Bảng 5.2 |
| C6 | Ch.4 | `cho khoảng 4,3 MB` và `có khoảng 9,23 triệu tham số` | "4,3" → "4.3"; "9,23" → "9.23" | công thức cùng đoạn đã dùng 9.23 |
| C7 | Ch.5 | Bảng 5.3 (thiết lập Flower), công thức trong bảng | "β ∈ {0.05; 0.1; 0.3}" → "{0.05, 0.1, 0.3}"; "M_c ∈ {100; 2000}" → "{100, 2000}" | dấu chấm phẩy → dấu phẩy |
| C8 | Ch.5 | công thức trong đoạn `FedMix kém FedAvg ở cả ba seed` | "t_{0.95; 2}" → "t_{0.95, 2}" | như trên |
| C9 | Ch.5 | công thức trong Bảng 5.5 (hai biến thể thăm dò), hàng C1+C2 | "β = 0,3" → "β = 0.3" | |
| C10 | Ch.5 | công thức trong đoạn diễn giải Bảng 5.6 (CCVR) | "β = 0,05" → "β = 0.05" | |
| C11 | Ch.5 | công thức trong đoạn `Ở ngân sách 100 mẫu mỗi lớp` | "β = 0,1" → "β = 0.1" | cùng đoạn đã có "β = 0.3" |
| C12 | Ch.5 | công thức trong đoạn diễn giải Bảng 5.8 (tái hiện) | "λ = 0,1" → "λ = 0.1" | |
| C13 | Ch.5 | công thức trong đoạn `Nhãn … có hai cấu hình` (5.5.1) | "λ = 0,1" → "λ = 0.1" | |
| C14 | Ch.5 | `từ 16,9% lên 61,8%` và `từ 22,3% lên 48,6%` | "16,9 / 61,8 / 22,3 / 48,6" → "16.9 / 61.8 / 22.3 / 48.6" | cùng đoạn đã có 1.099, 18.0 |
| C15 | Ch.5 | `của 20 000 mẫu` | "20 000" → "20,000" | |
| C16 | Ch.5 | `đứng quanh 2,0 trong suốt` và `xuống khoảng 1,5 vào vòng 400` | "2,0" → "2.0"; "1,5" → "1.5" | |
| C17 | Ch.5 | 5.6, đoạn `kém FedAvg 1,86 ± 0,79 điểm` | "1,86 ± 0,79" → "1.86 ± 0.79"; "−0,52" → "−0.52"; "−2,29" → "−2.29"; "−0,58" → "−0.58"; "(0,05 … 0,1 …)" → "(0.05 … 0.1 …)" | |
| C18 | Ch.5 | 5.6, `hơn FedAvg 6,37 điểm` | "6,37" → "6.37"; "7,35" → "7.35" | |
| C19 | Ch.5 | 5.6, `gấp khoảng 2,5 lần` | "2,5" → "2.5" | |

Bản md `05_chuong5.md` đã đổi toàn bộ theo quy ước này.

## D. Ký hiệu trong công thức

| # | Vị trí | Hiện trạng | Sửa | Lý do |
|---|---|---|---|---|
| D1 | Ch.2, công thức (2.1) | $\omega^* = \arg\min_\theta f(\theta)$ | $\theta^* = \arg\min_\theta f(\theta)$ | Ch.3 (3.2) dùng $\theta^*$; $\omega$ ở Ch.3 là bộ phân lớp |
| D2 | Ch.2, đoạn `FedAvg tìm nghiệm ấy theo từng vòng truyền thông` | "mô hình toàn cục $\omega_t$" | "$\theta_t$" | cùng đoạn đã có $\theta_{t+1}$ |
| D3 | Ch.4, Thuật toán 4.1 | $w_0$, $w_T$, $w_t$, $w_t^i$, $w$, $\nabla_w$ | $\theta_0$, $\theta_T$, $\theta_t$, $\theta_t^i$, $\theta$, $\nabla_\theta$ | thống nhất tham số là $\theta$ với Ch.2, Ch.3; Hình 4.1 đã vẽ lại theo |
| D4 | Ch.3, đoạn `Mô hình được tách thành hai phần` | $\omega: \mathbb{R}^d \to \mathbb{R}^c$ (chữ c thường) | $\mathbb{R}^C$ | số lớp là $C$ (cùng đoạn, và mọi chương sau); $c$ là chỉ số lớp |
| D5 | Ch.3 3.5 và Ch.5 Bảng 5.2 | $\tau_1 = \tau_2 = 2.0$ và $\tau_1 = \tau_2 = 2$ | dùng "2" ở cả hai (xem C5) | nhất quán |
| D6 | Toàn luận văn | hàm mất mát viết $l$ (chữ l thường), chuẩn viết $l_2$ | giữ nguyên, hoặc đổi cả hai sang $\ell$, $\ell_2$ | Word đang nhất quán với $l$; chỉ cần không trộn hai kiểu |
| D8 | Ch.3, 3.2.1, đoạn "Hai trục này độc lập về mặt khái niệm" | "mỗi client huấn luyện một bộ trích xuất riêng ⟨θ_i⟩" | ⟨ϕ_i⟩ | bộ trích xuất là ϕ (3.1.1, 3.4.1); θ là toàn bộ tham số |
| D7 | Ch.2 Bảng 2.2, Ch.3 mục 3.6 và mục 3.5 | $\mu_c$ là trung bình đặc trưng của lớp $c$; $\mu$ là trọng số thành phần tương phản của FedBR | giữ nguyên | hai nghĩa phân biệt được nhờ chỉ số $c$; ghi chú để biết, không bắt buộc sửa |

Các ký hiệu còn lại nhất quán giữa các chương: $\phi$ (bộ trích xuất, cùng một glyph ϕ), $\omega$ (bộ phân lớp), $\omega_c$ (vector trọng số lớp $c$), $\lambda$ (trọng số trộn), $\gamma$ (trọng số $L_{\text{bal}}$), $\mu$, $\tau_1$, $\tau_2$, $M$ (số ảnh mỗi mẫu trung bình), $M_c$ (số đặc trưng ảo mỗi lớp), $n_V$, $N$, $K$, $B$, $C$, $d$, $\alpha$, $\alpha_{\text{rot}}$, $\beta$.

## E. Số trích dẫn

Danh mục trong Word (28/09) đã đánh lại sau khi thêm MOON: **[1] Zhao · [2] FedMix · [3] FedBR · [4] FedAvg · [5] NIID-Bench · [6] Hsu–Qi–Brown · [7] FedProx · [8] SCAFFOLD · [9] MOON · [10] CCVR · [11] Mixup · [12] VHL · [13] FedDF · [14] FedNTD · [15] FedGen · [16] FedProto · [17] Efron · [18] Ng–Jordan**. Trích dẫn chèn bằng Zotero tự cập nhật; chỉ các số **gõ tay** (thường là đoạn dán từ md) bị sai. Cách sửa gọn nhất là xoá số gõ tay và chèn lại bằng Zotero (Add/Edit Citation).

| # | Chương | Tìm trong Word | Hiện | Đúng |
|---|---|---|---|---|
| E1 | Ch.5 | `phụ lục bài báo FedMix [1]` (Bảng 5.3, hàng Backbone) | [1] | [2] |
| E2 | Ch.5 | `CCVR [8] với` (Bảng 5.3, hàng Hiệu chuẩn) | [8] | [10] |
| E3 | Ch.5 | `công bố trong Bảng 1 của [2]` | [2] | [3] |
| E4 | Ch.5 | `Bảng 1 của [2] cho FedBR` | [2] | [3] |
| E5 | Ch.5 | `bảng công bố của [2] (mục 5.3.` | [2] | [3] |
| E6 | Ch.5 | `bài báo FedMix [1]: ở bảng` | [1] | [2] (đoạn này bị xoá theo quyết định bỏ NaiveMix, xem phần A của Ch.5) |

Các số gõ tay sai ở Ch.3 và Ch.4 nằm trong phần A của từng chương (Ch.3: "FedMix [1]" hai chỗ, "FedMix [3]" ở 3.4.1; Ch.4: "của [11]" ở 4.4). Bản md `05_chuong5.md` đã đổi theo danh mục mới.

---

# LƯỢT 2 · rà lại bản Word lưu 28/09 12:05

> **Kết quả chung.** Gần như toàn bộ các hàng ở phần A (Ch.1–5) và các mục B, D, E đã được áp. Chú thích bảng, hình giờ liên tục (Bảng 2.1–5.12, Hình 4.1–5.2), không trùng số, mọi chỗ nhắc "Bảng/Hình x.y" trong thân bài đều trỏ tới chú thích có thật. Trích dẫn khớp danh mục hiện tại (danh mục đã đổi thứ tự: [7] SCAFFOLD, [8] FedProx; Zotero tự cập nhật). Ký hiệu $\theta^*$, $\mathbb{R}^C$, $\phi_i$ đã sửa. Mỗi chương còn 0–2 khuôn tương phản, không cụm sáo, một dấu gạch ngang chêm ở Ch.2. Lời cam đoan, Mở đầu, Danh mục công bố đã có.
>
> Các chỗ dưới đây là phần còn lại. Cụm ở cột *Tìm* đã kiểm có trong Word.

| # | Vị trí | Tìm trong Word | Hiện | Sửa |
|---|---|---|---|---|
| L1 | Mở đầu, đoạn 2 | `rồi so sánh ba cách dùng NaiveMix, FedMix và FedBR` | …dựng một khung…, rồi so sánh ba cách dùng NaiveMix, FedMix và FedBR về độ chính xác và chi phí. | …dựng một khung…, đặt ba cách dùng NaiveMix, FedMix và FedBR vào cùng khung, rồi so sánh FedMix và FedBR về độ chính xác và chi phí. *(NaiveMix không chạy; lỗi của bản md, đã sửa trong md)* |
| L2 | Danh mục ký hiệu và chữ viết tắt | tiêu đề "DANH MỤC CÁC KÝ HIỆU VÀ CHỮ VIẾT TẮT" | chỉ có bảng chữ viết tắt (13 dòng) | chèn bảng **Ký hiệu** ở mục 2 của `00_mo-dau-va-danh-muc.md` phía trên bảng chữ viết tắt; nếu không dùng bảng ký hiệu thì đổi tiêu đề thành "DANH MỤC CÁC CHỮ VIẾT TẮT" |
| L3 | Ch.4, 4.3, ý "Phép co" | `ảnh hưởng của phép co..` | "…của phép co.." | một dấu chấm |
| L4 | Ch.5, 5.1, đoạn mở | `gọi tắt là nền tảng FedBR..` | "…nền tảng FedBR.." | một dấu chấm |
| L5 | Ch.5, 5.3.2, đoạn giải thích Bảng 5.9 | `FedMix và NaiveMix dùng` | "FedMix và NaiveMix dùng ⟨λ = 0.1⟩; FedMix dùng cách chuẩn hoá ở Chương 4, mục 4.3…" | "FedMix dùng ⟨λ = 0.1⟩ và cách chuẩn hoá ở Chương 4, mục 4.3…" (bảng không còn hàng NaiveMix) |
| L6 | Ch.5, 5.3.3, đoạn giải thích Hình 5.1 | `vẽ số liệu của Bảng 5.10 vẽ theo` | "Hình 5.1 vẽ số liệu của Bảng 5.10 vẽ theo ⟨M⟩." | "Hình 5.1 vẽ số liệu của Bảng 5.10 theo ⟨M⟩." |
| L7 | Ch.4, Thuật toán 4.1, phần Đầu vào/Đầu ra | `số vòng truyền thông ;số bước cục bộ` | dấu chấm phẩy dính chữ sau, có cách trước: " ;số bước", " ;số ảnh", " ;cách dùng", "Đầu ra:tham số" | "…; số bước…", "…; số ảnh…", "…; cách dùng…", "Đầu ra: tham số…" |
| L8 | Ch.4, Thuật toán 4.1 | ký hiệu $w_0$, $w_T$, $w$, $\nabla_w$ | tham số viết $w$ | $\theta_0$, $\theta_T$, $\theta$, $\nabla_\theta$ (mục D3; Hình 4.1 đã dùng $\theta$) |
| L9 | Ch.5, Bảng 5.7, hàng "Bậc nhất tốt nhất" | `tốc độ học 0,1, 2000 bước` | "0,1" | "0.1" |
| L10 | Ch.5, 5.3.3, đoạn thủ tục | `với hệ số 0,01` | "0,01" | "0.01" |
| L11 | Số có 4 chữ số | `VHL cần khoảng 2,000 mẫu ảo`; Bảng 2.2 `(~2,000 mẫu cho`; Bảng 5.2 `1,000 vòng`; công thức "M_c = 2,000" ở đoạn giải thích Bảng 5.6 và đoạn trước Bảng 5.7 | có dấu phẩy ở 5 chỗ, trong khi 23 chỗ khác viết liền (1000 vòng, 2000 mẫu, 2000 bước, n_V = 2000) | viết liền cả 5 chỗ: 2000, 1000; giữ dấu phẩy cho số từ 5 chữ số (20,000). Seed 12345 là mã, không tách |
| L12 | Ch.5, Bảng 5.3 (thiết lập Flower), công thức | "β ∈ {0.05; 0.1; 0.3}", "M_c ∈ {100; 2000}" | dấu chấm phẩy | "{0.05, 0.1, 0.3}", "{100, 2000}" (mục C7, chưa áp) |
| L13 | Ch.5, 5.2.2, công thức | "t_{0.95; 2}" | dấu chấm phẩy | "t_{0.95, 2}" (mục C8, chưa áp) |
| L14 | Ch.5, 5.5.1, công thức sau (5.1) | "δ ∈ {0;1}" | dấu chấm phẩy | "δ ∈ {0, 1}" |
| L15 | Ch.4, 4.4 (tuỳ chọn) | `tới từng client, tốn` | "…tốn ⟨N⟩ lần chiều lên." | "…tốn gấp ⟨N⟩ lần chiều lên." |
