# Chương 2. CÁC NGHIÊN CỨU LIÊN QUAN

> **KHỐI TRẠNG THÁI** · đồng bộ với bản Word ngày 22/09/2026
>
> | Mục | Trạng thái |
> |---|---|
> | 2.1 – 2.2 | `[ĐÃ CÓ TRONG WORD]` — file này chép theo bản Word, kèm các sửa lỗi liệt kê bên dưới |
> | 2.3 | `[MỚI VIẾT]` — bản Word đang để trống sau tiêu đề; nội dung dưới đây để chép vào |
>
> ⚠️ **Bản Word là bản chính.** Từ 22/09, `.md` chỉ là bản nháp phục vụ soạn thảo; khi hai bên lệch nhau thì **Word đúng**. Agent sau phải hỏi bản Word mới nhất trước khi sửa, không được coi file này là nguồn duy nhất.
>
> ⚠️ **Lỗi trong bản Word cần sửa tay** (chi tiết ở cuối file, mục *Ghi chú biên tập*): trùng số trích dẫn MOON/SCAFFOLD; trích sai nguồn ở 2.1.2; khuyết số [15]; Bảng 2.1 chưa có tên; một số lỗi chính tả và thuật ngữ không nhất quán.
>
> ⚠️ **Hai mục đã bỏ khỏi chương** (quyết định 22/09): bảng đối chiếu các họ phương pháp, và mục về tính tái lập cùng cách báo cáo mức cải thiện. Ba quy tắc báo cáo trong mục bị bỏ (so sánh theo cặp · đường đặc tuyến vận hành · chỉ so sánh trong cùng nền tảng) **vẫn là ràng buộc của luận văn** và nay phải được phát biểu ở **Chương 4, mục giao thức đo lường**; ví dụ đảo dấu của CCVR theo ngân sách chuyển về **Chương 3, mục kết quả nền từ công trình đã công bố của tác giả**. Mục 2.3 dưới đây chỉ giữ lại phần tối thiểu cần cho lập luận về đóng góp thứ hai.
>
> ⚠️ **IR#3 — mất phủ tối thiểu.** Bản Word đã lược **Deep CORAL** và **FedDecorr** khỏi 2.2.2.5, nhưng IR#3 (`00_outline.md` §2) liệt kê đích danh hai công trình này trong danh mục Ch.2 bắt buộc phủ. Cần quyết: đưa lại hai công trình vào 2.2.2.5, hoặc sửa IR#3. **Chưa xử lý.**

---

## 2.1. Học liên kết và thách thức dữ liệu không đồng nhất

### 2.1.1. Khái niệm học liên kết

Federated Learning là mô hình học máy phân tán trong đó dữ liệu huấn luyện không rời khỏi thiết bị của người dùng. Thay vì gom dữ liệu về một máy chủ rồi huấn luyện tập trung, hệ thống gửi mô hình xuống từng thiết bị, để thiết bị tự huấn luyện trên dữ liệu của mình, rồi chỉ thu về tham số mô hình đã cập nhật.

Thuật toán nền tảng của mô hình này là FedAvg [2]. Bài toán được hình thức hoá như sau: có $N$ thiết bị tham gia (thường gọi là client), client thứ $i$ giữ tập dữ liệu cục bộ $D_i$ và do đó có hàm mục tiêu riêng $f_i(\omega)$, là sai số trung bình của mô hình tham số $\omega$ trên chính tập dữ liệu ấy. Mục tiêu của cả hệ thống là nghiệm:

$$\omega^{*} = \arg\min_{\omega} f(\omega), \qquad f(\omega) = \sum_{i=1}^{N} p_i f_i(\omega), \qquad p_i = \frac{|D_i|}{\sum_j |D_j|} \tag{2.1}$$

Mục tiêu toàn cục $f$ là trung bình có trọng số của các mục tiêu cục bộ, và trọng số $p_i$ của mỗi client tỉ lệ với lượng dữ liệu nó nắm giữ.

FedAvg tìm nghiệm ấy theo từng vòng truyền thông. Ở vòng thứ $t$, máy chủ phát mô hình toàn cục $\omega_t$ tới một tập con client; mỗi client nhận về, chạy $K$ bước cập nhật SGD trên dữ liệu của mình, rồi gửi bộ tham số đã đổi ngược lên; máy chủ lấy trung bình có trọng số các bộ tham số nhận được để tạo $\omega_{t+1}$, và vòng sau lặp lại.

Chi tiết quyết định nằm ở con số $K$. Nếu $K = 1$, mỗi vòng truyền thông chỉ đổi lấy một bước cập nhật, và thuật toán tương đương SGD tập trung nhưng chi phí truyền thông trở nên không khả thi trong triển khai thực tế. Cho phép $K > 1$, mỗi client chạy nhiều bước trước khi đồng bộ, là cách FL tiết kiệm truyền thông, và cũng chính là nguồn gốc của vấn đề trung tâm mà luận văn này nghiên cứu.

Vấn đề đó xuất hiện khi dữ liệu giữa các client không phân phối đồng nhất, thường viết tắt là non-IID. Khi ấy cực tiểu của hàm mục tiêu cục bộ $f_i$ nằm ở một chỗ khác với cực tiểu của mục tiêu toàn cục $f$. Chạy càng nhiều bước cục bộ, mỗi client càng đi sâu về phía nghiệm riêng của mình, và trung bình của những nghiệm đã trôi lệch ấy không còn là một bước tiến tốt cho mục tiêu chung vì nó có thể rơi vào một vùng mà không client nào coi là tốt. Hiện tượng này được gọi là client drift, và biểu hiện quan sát được của nó là hội tụ chậm, đường học dao động mạnh giữa các vòng, và độ chính xác cuối cùng của mô hình tổng hợp thấp hơn rõ rệt so với huấn luyện tập trung trên cùng lượng dữ liệu.

### 2.1.2. Ba dạng không đồng nhất dữ liệu

Cụm từ non-IID thường được dùng như thể nó chỉ một hiện tượng duy nhất, nhưng thực ra nó gộp nhiều tình huống khác nhau về bản chất. NIID-Bench [3], công trình khảo sát thực nghiệm được trích dẫn rộng rãi nhất về chủ đề này, phân biệt sáu chiến lược phân hoạch dữ liệu, thuộc ba nhóm hiện tượng.

**Bảng 2.1.** Ba dạng dữ liệu không đồng nhất trong học liên kết và các chiến lược phân hoạch tương ứng, theo phân loại của NIID-Bench [3]. Cột *Cơ chế* nêu thành phần nào của phân phối liên hợp $P_i(x, y)$ thay đổi giữa các client.

| Nhóm | Cơ chế | Chiến lược phân hoạch |
|---|---|---|
| Lệch phân phối nhãn (label distribution skew) | Phân phối nhãn $P_i(y)$ khác nhau giữa các client, còn $P(x \mid y)$ thì chung | mỗi client giữ đúng $k$ lớp; phân hoạch theo Dirichlet |
| Lệch phân phối đặc trưng (feature distribution skew) | Phân phối đầu vào có điều kiện $P_i(x \mid y)$ khác nhau giữa các client | nhiễu Gauss theo client; bộ tổng hợp FCUBE; phân hoạch theo người viết (FEMNIST) |
| Lệch số lượng (quantity skew) | Kích thước $\lvert D_i \rvert$ khác nhau | Dirichlet trên số mẫu |

Hai nhóm đầu khác nhau về bản chất, và sự phân biệt giữa chúng cần được nêu rõ vì toàn bộ thiết kế thực nghiệm của luận văn dựa trên đó. Ở lệch phân phối nhãn, các client quan sát những lớp khác nhau: một client chứa chủ yếu mẫu thuộc một nhóm lớp, client khác chứa chủ yếu mẫu thuộc nhóm lớp còn lại, song mẫu của cùng một lớp ở hai client vẫn được sinh từ cùng một phân phối. Ở lệch phân phối đặc trưng, tình huống ngược lại: tỉ lệ các lớp tại mọi client có thể như nhau, nhưng mẫu của cùng một lớp lại khác nhau về hình thức do điều kiện thu thập khác nhau, chẳng hạn thiết bị ghi hình, độ chiếu sáng, góc chụp. Hai dạng lệch tác động lên mô hình theo hai cơ chế khác nhau, nên không có cơ sở tiên nghiệm để cho rằng một phương pháp khắc phục được dạng này thì cũng khắc phục được dạng kia.

NIID-Bench tách lệch phân phối đặc trưng khỏi lệch phân phối nhãn ngay ở mức thiết kế chiến lược phân hoạch. Trong chiến lược nhiễu Gauss, toàn bộ tập dữ liệu trước hết được chia ngẫu nhiên và đều cho các bên, sau đó mỗi bên được thêm nhiễu Gauss ở một mức khác nhau [3]. Thứ tự của hai thao tác quyết định tính chất của phân hoạch thu được: vì phép chia diễn ra trước và là chia đều, phân phối nhãn giữa các bên là đồng nhất, và khác biệt duy nhất còn lại nằm ở phân phối đầu vào. Bộ dữ liệu tổng hợp FCUBE cũng giữ nhãn cân bằng, bằng cách gán cho mỗi bên hai khối dữ liệu đối xứng qua gốc toạ độ. Công trình này còn dành riêng một mục cho chế độ skew hỗn hợp, trong đó phân hoạch Dirichlet theo nhãn được kết hợp với nhiễu theo đặc trưng.

### 2.1.3. Quy ước tham số hoá Dirichlet

Công cụ phổ biến nhất để mô phỏng lệch phân phối nhãn là phân hoạch Dirichlet. Thay vì chia dữ liệu đều cho các client, ta rút ngẫu nhiên một vector tỉ lệ từ phân phối Dirichlet rồi chia theo tỉ lệ đó. Phân phối Dirichlet nhận giá trị trên đơn hình xác suất, tức tập các vector có mọi thành phần không âm và tổng bằng một, nên mỗi lần rút đều cho ra một vector tỉ lệ hợp lệ.

Hình dạng của phân phối này được điều khiển bởi tham số nồng độ $\alpha$ (concentration), và chính tham số ấy quyết định mức độ lệch của phân hoạch thu được. Khi nồng độ mỗi thành phần lớn hơn một, các vector rút ra tập trung quanh vector đều, nên mọi client nhận tỉ lệ lớp xấp xỉ như nhau và phân hoạch gần với đồng nhất. Khi nồng độ mỗi thành phần nhỏ hơn một, khối lượng xác suất dồn về phía các đỉnh của đơn hình: vector rút ra có một vài thành phần nhận giá trị gần một, còn các thành phần còn lại gần không. Trong chế độ thứ hai, mỗi client trên thực tế chỉ giữ mẫu của một vài lớp, và nồng độ càng nhỏ thì số lớp hiệu dụng mà client quan sát được càng ít. Đây là lý do nồng độ được dùng làm tham số điều khiển độ lệch phân phối nhãn.

Khó khăn nằm ở chỗ các nghiên cứu sử dụng hai quy ước khác nhau dưới cùng một ký hiệu, và điều này ảnh hưởng trực tiếp tới khả năng tái lập của các kết quả được công bố.

Quy ước thứ nhất, do Hsu, Qi và Brown đưa ra, lấy mẫu theo trục các lớp, thực hiện cho từng client: với mỗi client, rút một vector phân phối lớp $q \sim \mathrm{Dir}(\alpha \cdot p)$, trong đó $p$ là phân phối lớp tiên nghiệm, thường là phân phối đều, và do đó thoả $\sum_c p_c = 1$. Vì tổng các thành phần của $p$ bằng 1, tham số $\alpha$ ở đây là nồng độ tổng, còn nồng độ của mỗi thành phần chỉ là $\alpha / C$ với $C$ là số lớp [4].

Quy ước thứ hai, áp dụng trong nghiên cứu NIID-Bench, lấy mẫu theo trục các bên, thực hiện cho từng lớp, là chuyển vị của quy ước trên: với mỗi lớp $k$, rút một vector $p_k \sim \mathrm{Dir}_N(\beta)$ trên $N$ bên, rồi giao tỉ lệ $p_{k,j}$ số mẫu của lớp $k$ cho bên $j$. Ở đây $\beta$ là nồng độ mỗi thành phần, và nồng độ tổng là $N\beta$ [3].

Với CIFAR-10, tức 10 lớp chia cho 10 bên, ký hiệu "0,5" theo quy ước thứ nhất tương ứng nồng độ mỗi thành phần là 0,05, còn theo quy ước thứ hai thì đúng bằng 0,5, chênh nhau mười lần. Một công bố ghi "Dirichlet $\alpha = 0{,}1$" mà không nói rõ đang dùng quy ước nào thì không tái lập được, vì người đọc không biết mức lệch thực tế nặng hay nhẹ gấp mười lần.

Luận văn này do đó áp dụng một quy tắc báo cáo cố định: mỗi lần nêu tham số Dirichlet đều ghi đủ bộ ba gồm vector nồng độ, trục lấy mẫu và số thành phần, kèm dòng quy đổi $\alpha_{\text{Hsu}} = N \cdot \beta_{\text{NIID-Bench}}$ áp dụng khi phân phối tiên nghiệm là đều.

---

## 2.2. Tăng cường dữ liệu và chia sẻ thống kê trong FL

Các phương pháp khắc phục client drift có thể chia thành hai hướng. Hướng thứ nhất sửa cách học mà giữ nguyên lượng thông tin được trao đổi. Hướng thứ hai trao đổi thêm thông tin về dữ liệu với một lượng nhỏ và ở dạng đã được xử lý để không bộc lộ dữ liệu gốc.

### 2.2.1. Hướng tiếp cận không chia sẻ dữ liệu

Hướng thứ nhất chống client drift bằng cách can thiệp vào quá trình tối ưu hoá. Các client vẫn chỉ trao đổi tham số mô hình, đúng như FedAvg, không kèm bất kỳ thông tin nào về dữ liệu.

#### 2.2.1.1. Ràng buộc trên bộ tham số

FedProx [5] là phương pháp đơn giản nhất trong nhóm và cũng được trích dẫn nhiều nhất. Nó thêm vào hàm mất mát cục bộ một số hạng phạt, kéo mô hình cục bộ về gần mô hình toàn cục của vòng hiện tại. Số hạng này không cho client đi quá xa trong $K$ bước cục bộ, và vì vậy làm nhẹ bớt độ trôi, nhưng cũng đồng thời làm chậm tốc độ học, nên cường độ phạt là một đánh đổi phải chỉnh tay. FedProx là một trong hai phương pháp đối chứng được dùng trong phần thực nghiệm của luận văn.

#### 2.2.1.2. Hiệu chỉnh hướng gradient

SCAFFOLD [6] xử lý vấn đề ở tầng sâu hơn, tại chính bộ tối ưu. Mỗi client duy trì một biến kiểm soát (control variate) ước lượng phần lệch giữa hướng gradient cục bộ của nó và hướng gradient toàn cục, rồi trừ đi phần lệch đó ở mỗi bước cập nhật. Về mặt lý thuyết đây là kỹ thuật giảm phương sai kinh điển áp cho bối cảnh liên kết, và nó cho bảo đảm hội tụ mạnh hơn FedProx; cái giá là mỗi vòng phải truyền thêm biến kiểm soát, tức chi phí truyền thông tăng gấp đôi.

#### 2.2.1.3. Ràng buộc trên biểu diễn

Để mô tả MOON [7] cần tách mạng phân loại thành hai phần. Phần thứ nhất là bộ trích xuất đặc trưng: nó nhận ảnh đầu vào và trả về một vector $d$ chiều, gọi là biểu diễn hay đặc trưng của ảnh đó. Phần thứ hai là tầng phân lớp (classifier head), nhận vector đặc trưng và trả về điểm số cho từng lớp. Cơ chế của MOON như sau: với cùng một ảnh cục bộ, ba mô hình cho ba biểu diễn khác nhau, gồm mô hình toàn cục vừa nhận được từ máy chủ, mô hình cục bộ đang được huấn luyện, và mô hình cục bộ ở cuối vòng trước. MOON thêm một số hạng phạt kéo biểu diễn của mô hình đang huấn luyện lại gần biểu diễn của mô hình toàn cục, đồng thời đẩy nó ra xa biểu diễn của mô hình cục bộ vòng trước. Lập luận đằng sau là mô hình toàn cục mang thông tin của mọi client nên biểu diễn của nó ít lệch hơn, còn mô hình cục bộ vòng trước là hiện thân của phần lệch đã tích luỹ, nên đáng dùng làm mốc để tránh xa.

FedProx và SCAFFOLD đều thao tác trên vector tham số của toàn mạng; MOON thao tác trên vector biểu diễn mà bộ trích xuất đặc trưng sinh ra. FedProx đo khoảng cách giữa hai bộ tham số, còn MOON đo khoảng cách giữa tác động của hai bộ tham số ấy lên dữ liệu thật. Hai mạng có tham số rất khác nhau vẫn có thể sinh ra biểu diễn gần như nhau, nên ràng buộc của MOON nới hơn và ít cản trở việc học hơn, trong khi vẫn giữ được mục tiêu là không để mô hình cục bộ trôi xa.

Vì không trao đổi thêm bất kỳ thông tin nào về dữ liệu, hướng tiếp cận này không làm phát sinh câu hỏi riêng tư nào ngoài những gì đã có sẵn trong FedAvg. Đó là ưu điểm lớn, nhưng đồng thời là trần của nó: nếu phân phối dữ liệu của các client thực sự khác nhau, thì không một thao tác nào trên quỹ đạo tối ưu hoá có thể cấp cho một client thông tin về những gì nó chưa bao giờ nhìn thấy. Bên cạnh đó, các phương pháp trong hướng này can thiệp chủ yếu vào quá trình huấn luyện, trong khi phần lớn suy giảm do non-IID định vị được ở tầng phân lớp. Chính vì vậy đã sinh ra một họ phương pháp khác, được trình bày ở tiểu mục về hiệu chuẩn bộ phân lớp phía dưới.

### 2.2.2. Hướng tiếp cận có chia sẻ dữ liệu

Hướng này chấp nhận truyền thêm một lượng thông tin nhỏ ngoài tham số mô hình, đủ để mỗi client có một hình dung về phân phối của toàn hệ thống, nhưng nhỏ tới mức không phá vỡ ràng buộc riêng tư của bài toán. Các nhánh trong hướng này khác nhau ở hai trục: thông tin gì được truyền, và thông tin đó được dùng như thế nào.

Zhao và cộng sự [8] cho thấy chỉ cần chia sẻ cho mọi client một tập dữ liệu nhỏ có phân phối lớp cân bằng là đủ khôi phục phần lớn độ chính xác đã mất do non-IID. Kết quả ấy có hai mặt: một mặt, nó chứng minh lượng thông tin cần bổ sung là nhỏ; mặt khác, tập được chia sẻ gồm dữ liệu thô, tức trái với nguyên tắc nền tảng của học liên kết.

Năm nhánh trình bày dưới đây có thể được đọc như những nỗ lực khác nhau nhằm giữ lại lợi ích của việc bổ sung thông tin mà giảm mức riêng tư phải đánh đổi; nhánh cuối cùng trình bày FedBR, công trình được luận văn dùng làm nền tảng thực nghiệm.

#### 2.2.2.1. Học liên kết tăng cường trung bình và bài toán xấp xỉ global Mixup

Mixup [9] là một kỹ thuật tăng cường dữ liệu đơn giản và rất hiệu quả trong học tập trung: thay vì huấn luyện trên từng mẫu riêng lẻ, mô hình được huấn luyện trên các tổ hợp lồi của các cặp mẫu, với nhãn cũng được trộn theo đúng tỉ lệ ấy. Trộn hai ảnh theo tỉ lệ 70–30 thì nhãn đích cũng là 70% lớp thứ nhất và 30% lớp thứ hai.

Áp ý tưởng này cho học liên kết gặp trở ngại ngay từ bước đầu. Phiên bản có giá trị nhất trong bối cảnh non-IID là global Mixup, trộn mẫu của client này với mẫu của client khác, vì chính sự pha trộn xuyên client mới mang thông tin mà client không tự có. Nhưng làm được điều đó thì phải truy cập dữ liệu thô xuyên client, tức vi phạm đúng cái ràng buộc định nghĩa bài toán.

FedMix [1] đề xuất khung Mean Augmented Federated Learning (MAFL) để vượt trở ngại đó. Mỗi client tính một số ít mẫu trung bình đại diện: lấy $M$ ảnh cục bộ, tính trung bình pixel theo từng vị trí để được một ảnh, đồng thời tính trung bình các nhãn one-hot tương ứng để được một nhãn mềm, rồi chia sẻ các cặp ảnh-nhãn trung bình đó cho các client khác thông qua máy chủ. Phép lấy trung bình đóng vai trò một cơ chế nén: ảnh riêng lẻ không rời khỏi thiết bị, chỉ bản đã bị làm mịn được chia sẻ, và số ảnh được gộp $M$ là tham số điều khiển mức nén, $M$ càng lớn thì ảnh chia sẻ càng mờ và càng khó truy ngược về mẫu gốc.

Bên trong khung MAFL, FedMix định nghĩa hai thuật toán khác nhau. NaiveMix trộn trực tiếp dữ liệu cục bộ với mẫu trung bình nhận được rồi tính hàm mất mát trên đầu vào đã trộn, nghĩa là mẫu trung bình đi qua toàn bộ mạng như một ảnh bình thường. FedMix thì khai triển Taylor bậc nhất chính hàm mất mát ấy quanh đầu vào đã co tỉ lệ, và thu được một dạng trong đó mẫu trung bình không còn đi vào lượt truyền xuôi nữa, mà chỉ còn xuất hiện trong một tích vô hướng với đạo hàm của hàm mất mát theo đầu vào. Hai thuật toán khác nhau ở hai chỗ cùng lúc, số hạng Taylor được thêm vào, và mẫu trung bình bị rút khỏi lượt truyền xuôi. Vì hai thay đổi này xảy ra đồng thời, chênh lệch hiệu năng đo được giữa chúng không quy riêng cho chỗ nào được.

#### 2.2.2.2. Dữ liệu ảo

Một hướng triệt để hơn cắt đứt hoàn toàn liên hệ với dữ liệu thật. VHL [10] sinh một tập dữ liệu ảo từ nhiễu, gán nhãn cho tập ảo đó, phát cho mọi client, rồi trong quá trình huấn luyện cục bộ ép đặc trưng của dữ liệu thật tiến về gần đặc trưng của dữ liệu ảo cùng lớp. Vì tập ảo không chứa thông tin của bất kỳ người dùng nào, rủi ro riêng tư gần như bị loại bỏ hẳn; đổi lại, mọi client chia sẻ chung một hệ quy chiếu nhân tạo để căn chỉnh không gian đặc trưng về. Tuy nhiên, VHL yêu cầu nhãn. Theo số liệu được đối chiếu trong FedBR [11], VHL cần khoảng 2.000 mẫu ảo cho CIFAR-10 và 20.000 cho CIFAR-100, tỉ lệ thuận với số lớp, và các mẫu này bắt buộc phải có nhãn.

#### 2.2.2.3. Chưng cất tri thức

Phương thức này không truyền dữ liệu mà truyền tri thức của mô hình. Ý tưởng chung là dùng đầu ra của mô hình toàn cục trên một tập dữ liệu trung gian làm mục tiêu để mô hình cục bộ học theo, thay vì so sánh tham số với tham số.

FedDF [12] dùng logits của mô hình toàn cục trên một tập proxy không cần nhãn làm mục tiêu chưng cất, và thực hiện việc chưng cất này ở máy chủ sau khi đã gộp mô hình. FedNTD [13] chưng cất có chọn lọc hơn: nó chỉ giữ lại phần phân phối trên các lớp không phải nhãn đúng, với lập luận rằng chính phần này mang thông tin toàn cục mà mô hình cục bộ có xu hướng quên khi chỉ nhìn thấy vài lớp. FedGen [14] loại bỏ nhu cầu về tập proxy bằng cách học một bộ sinh nhẹ ngay tại máy chủ, rồi dùng bộ sinh đó tạo dữ liệu cho việc chưng cất.

#### 2.2.2.4. Hiệu chuẩn bộ phân lớp từ thống kê lớp

Phương pháp này xuất phát từ một quan sát thực nghiệm cụ thể. Quan sát ấy liên quan tới cách hai phần của mạng phân loại, là bộ trích xuất đặc trưng và tầng phân lớp, chịu ảnh hưởng khác nhau bởi tính không đồng nhất của dữ liệu: dưới lệch phân phối nhãn, bộ trích xuất đặc trưng vẫn học được biểu diễn tương đối tốt, trong khi tầng phân lớp lệch mạnh về các lớp chiếm đa số tại chỗ. Nếu quan sát trên là đúng thì chỉ cần hiệu chỉnh riêng tầng cuối là đủ, và việc ấy rẻ hơn rất nhiều so với can thiệp vào toàn bộ quá trình huấn luyện.

CCVR [15] là công trình mẫu của nhánh này. Mỗi client ước lượng, cho từng lớp $c$, vector trung bình đặc trưng $\mu_c$ và ma trận hiệp phương sai $\Sigma_c$, rồi gửi các thống kê ấy lên máy chủ. Máy chủ mô hình hoá mỗi lớp bằng một phân phối Gauss với hai tham số đó, lấy mẫu ra các đặc trưng ảo, và huấn luyện lại riêng tầng phân lớp trên tập đặc trưng ảo cân bằng này. Không một mẫu dữ liệu thô nào rời khỏi thiết bị; chỉ có thống kê bậc một và bậc hai của đặc trưng.

#### 2.2.2.5. Căn chỉnh đặc trưng có điều kiện lớp

Nhóm phương pháp này không sửa tầng phân lớp sau khi huấn luyện xong, mà ràng buộc không gian đặc trưng ngay trong lúc huấn luyện cục bộ.

FedProto [16] là công trình nền. Mỗi client tính cho từng lớp một prototype, là trung bình đặc trưng của các mẫu thuộc lớp đó; máy chủ gộp các prototype cục bộ thành prototype toàn cục cho từng lớp; và ở vòng sau, mỗi client bị phạt theo khoảng cách từ đặc trưng nó sinh ra tới prototype toàn cục của lớp tương ứng. Kết quả là các client dần thống nhất với nhau về vị trí của mỗi lớp trong không gian đặc trưng. Chi phí truyền thông rất thấp: $C$ vector $d$ chiều mỗi vòng.

Điểm chung của các phương pháp theo hướng này là chúng dừng ở moment bậc nhất: chúng đồng nhất vị trí của cụm đặc trưng ứng với mỗi lớp giữa các client, nhưng không ràng buộc gì về hình dạng của cụm đó. Giới hạn ấy không gây hậu quả gì dưới lệch phân phối nhãn, nơi cùng một lớp ở hai client vẫn là cùng một phân phối ảnh và do đó rơi vào cùng một vùng đặc trưng. Nhưng dưới lệch phân phối đặc trưng thì khác hẳn: cùng một lớp ở hai client có thể nằm ở hai vùng khác nhau của không gian, và khi đó một vector trung bình duy nhất cho mỗi lớp không còn mô tả được lớp ấy, nó chỉ đánh dấu điểm giữa của hai cụm tách rời, một vị trí có thể không có mẫu thật nào.

#### 2.2.2.6. FedBR

FedBR [11] giữ một vai trò đặc biệt trong luận văn: nó là nền tảng thực nghiệm mà toàn bộ thí nghiệm mới được chạy trên đó. FedBR nhắm vào hai biểu hiện của thiên lệch học cục bộ bằng hai thành phần, cả hai đều vận hành trên một tập pseudo-data dùng chung, tập dữ liệu giả này được xây bằng phép lấy trung bình mẫu ngẫu nhiên (Random Sample Mean) hoặc bằng một phương án gọi là Mixture.

Thành phần thứ nhất cân bằng phân phối đầu ra của tầng phân lớp trên tập pseudo-data, chống lại xu hướng mô hình cục bộ gán mọi mẫu vào những lớp xuất hiện nhiều tại chỗ. Thành phần thứ hai là một bài toán min-max trên không gian đặc trưng: một tầng chiếu được huấn luyện theo lối đối kháng để phân biệt đặc trưng do mô hình cục bộ sinh ra với đặc trưng do mô hình toàn cục sinh ra, sau đó bộ trích xuất cục bộ được huấn luyện ngược lại để đặc trưng của pseudo-data gần đặc trưng toàn cục mà xa đặc trưng của dữ liệu cục bộ thật.

Thành phần thứ hai ghép cặp theo từng mẫu, không phải theo phân phối. Cặp dương trong hàm mất mát là cặp gồm đặc trưng cục bộ và đặc trưng toàn cục của cùng một mẫu pseudo-data, chứ không phải hai mẫu bất kỳ lấy từ hai phía. Ràng buộc theo từng mẫu trên cùng một đầu vào chặt hơn căn chỉnh phân phối biên, vì nó ràng buộc mọi thống kê có điều kiện tính được trên tập pseudo-data, trong khi căn chỉnh biên chỉ ràng buộc các moment tổng. Do đó, mô tả thành phần này như một phép căn chỉnh phân phối biên là không chính xác.

---

## 2.3. Khoảng trống luận văn

### 2.3.1. Cô lập số hạng khai triển Taylor

Công trình FedMix [1] có đối chứng giữa FedMix và NaiveMix, và trình bày kết quả đối chứng ở bảng chính. Tuy nhiên, như mục 2.2.2.1 đã nêu, hai thuật toán khác nhau ở hai chỗ cùng lúc: số hạng Taylor được thêm vào, và mẫu trung bình bị rút khỏi lượt truyền xuôi. Chênh lệch hiệu năng giữa chúng do đó phản ánh tác động tổng hợp của hai thay đổi, không cho phép quy riêng cho số hạng Taylor.

Cấu hình đủ để cô lập số hạng này là cấu hình giữ nguyên điểm đánh giá hàm mất mát, tức mẫu trung bình vẫn tham gia lượt truyền xuôi như ở FedMix, và chỉ loại bỏ số hạng đạo hàm. Cấu hình như vậy không xuất hiện trong bài báo FedMix, kể cả ở phần phụ lục.

FedMix có khảo sát một trục khác, trực giao với trục vừa nêu: giữ nguyên số hạng đạo hàm và thay dữ liệu đưa vào số hạng ấy bằng nhiễu ngẫu nhiên hoặc bằng trung bình của dữ liệu cục bộ, và cho thấy cả hai phương án thay thế đều cho kết quả kém hơn. Kết quả này chứng minh mẫu trung bình toàn cục phải mang thông tin thật, nhưng chưa chứng minh số hạng đạo hàm là thành phần cần thiết. Vẫn có khả năng mẫu trung bình mang thông tin hữu ích trong khi cách đưa nó vào qua đạo hàm không hiệu quả hơn cách trộn trực tiếp vào đầu vào.

Hai đặc điểm khác của phép đối chứng gốc cũng hạn chế khả năng quy kết. Trọng số trộn $\lambda$ được tinh chỉnh riêng cho từng thuật toán, nên hai nhánh được đo tại hai giá trị $\lambda$ khác nhau, và chênh lệch quan sát được chứa cả ảnh hưởng của ngân sách tinh chỉnh không đồng đều. Bên cạnh đó, chính công trình gốc cho thấy giá trị $\lambda$ tốt nhất của NaiveMix cho kết quả tiến sát FedMix.

Trong số các công trình trích dẫn FedMix mà luận văn khảo sát được, chưa có công trình nào thực hiện lại phép đối chứng này một cách độc lập, và cũng chưa có công trình nào thực hiện nó dưới lệch phân phối đặc trưng.

### 2.3.2. Phạm vi đánh giá theo loại lệch phân phối

NIID-Bench [3] tách lệch phân phối đặc trưng khỏi lệch phân phối nhãn và dành riêng một mục cho chế độ skew hỗn hợp, như mục 2.1.2 đã trình bày. Khảo sát ở chế độ này đo bốn thuật toán là FedAvg, FedProx, SCAFFOLD và FedNova, đều thuộc hướng can thiệp vào quá trình tối ưu hoá. Các phương pháp thuộc hướng chia sẻ dữ liệu, trong đó có họ tăng cường trung bình, không nằm trong phạm vi khảo sát đó.

Hai hướng tác động lên những thành phần khác nhau của mô hình: một bên điều chỉnh quỹ đạo tối ưu hoá, một bên bổ sung thông tin về phân phối dữ liệu. Vì vậy không có cơ sở để suy kết luận của hướng này sang hướng kia, và hành vi của họ tăng cường trung bình dưới lệch phân phối đặc trưng vẫn còn là câu hỏi để ngỏ.

NIID-Bench còn để lại một vấn đề mà luận văn thừa hưởng. Hai loại lệch được điều khiển bởi hai tham số không cùng đơn vị: nồng độ Dirichlet trên phân phối lớp đối với lệch nhãn, và cường độ nhiễu hoặc biên độ biến đổi hình học đối với lệch đặc trưng. Chưa có cách quy đổi độ nghiêm trọng của hai loại lệch về cùng một thang. Luận văn không giải quyết vấn đề này mà sử dụng một phương án căn chỉnh vận hành, trình bày ở Chương 4.

### 2.3.3. Định vị luận văn

Luận văn không đề xuất thuật toán học liên kết mới, mà xác định biên giới hiệu lực của cơ chế tăng cường dữ liệu bằng mẫu trung bình đại diện kết hợp xấp xỉ hàm mất mát bằng khai triển Taylor bậc nhất. Ba đóng góp sau tương ứng với hai khoảng trống vừa trình bày.

Đóng góp thứ nhất là phép đo có kiểm soát đối với số hạng khai triển Taylor. Phép đối chứng giữa FedMix và NaiveMix được thực hiện lại trên FedBR [11] với nhiều hạt giống ngẫu nhiên, báo cáo kèm khoảng tin cậy. Hai nhánh được đo tại cùng một trọng số trộn, đồng thời báo cáo giá trị $\lambda$ tối ưu riêng của từng nhánh để tách phần đóng góp của cơ chế khỏi phần đến từ ngân sách tinh chỉnh. Luận văn bổ sung cấu hình cô lập chặt mô tả ở mục 2.3.1 và mở rộng toàn bộ phép đối chứng sang chế độ lệch phân phối đặc trưng.

Đóng góp thứ hai là phép đo cơ chế tại nhiều mức độ nghiêm trọng của cả hai loại lệch phân phối, với mức cải thiện được báo cáo dưới dạng đường đặc tuyến theo tham số ngân sách. Cách báo cáo này xuất phát từ đặc điểm của các phương pháp chia sẻ thông tin: mức cải thiện phụ thuộc vào lượng thông tin được phép chia sẻ, nên một giá trị đo tại một điểm ngân sách không đại diện cho toàn bộ đường cong.

Đóng góp thứ ba là kiểm toán tính tái lập của nền tảng thực nghiệm, gồm danh mục các điểm mã nguồn phát hành không khớp với mô tả trong bài báo tương ứng. Kết luận của phần này được giới hạn ở mức mô tả: mã nguồn cho thấy các thuật toán đối chứng hoạt động dưới mức mà bài báo hàm ý, nhưng luận văn không định lượng mức đóng góp của từng nguyên nhân.

Chương 3 trình bày nền tảng lý thuyết cho ba đóng góp trên, trọng tâm là dẫn xuất khai triển Taylor bậc nhất và các cấu hình thuật toán sinh ra từ nó.

---

## Ghi chú biên tập — lỗi trong bản Word cần sửa tay

> Phần này **không thuộc luận văn**, chỉ để đối chiếu khi sửa file Word. Xoá trước khi nộp.

**Trích dẫn.**

1. **MOON và SCAFFOLD cùng mang số [6].** Ở 2.2.1.3 bản Word ghi "MOON [6]" trong khi 2.2.1.2 đã dùng [6] cho SCAFFOLD. File này tạm gán MOON là **[7]** và dịch toàn bộ các số sau lên một đơn vị (Zhao [8], Mixup [9], VHL [10], FedBR [11], FedDF [12], FedNTD [13], FedGen [14], CCVR [15], FedProto [16]). **Cần đối chiếu với danh mục tài liệu tham khảo thật trong Word** — nếu MOON đã có sẵn một số khác thì dùng số đó và bỏ phép dịch này.
2. **Khuyết số [15] trong bản Word.** Bản Word nhảy từ CCVR [14] sang FedProto [16]. Nhiều khả năng [15] là một công trình đã bị lược khỏi thân bài nhưng còn sót trong danh mục. Cần kiểm tra và xoá mục mồ côi đó.
3. **Trích sai nguồn ở 2.1.2.** Câu mô tả chiến lược nhiễu Gauss của NIID-Bench trong bản Word ghi [2], tức FedAvg. Phải là **[3]** (NIID-Bench). Đã sửa trong file này.

**Bảng.**

4. **Bảng 2.1 chưa có tên.** Bản Word chỉ có dòng "Bảng 2.1." rồi tới bảng. Tên đã soạn sẵn trong file này, chép vào. Theo quy ước đã chốt ở `00_outline.md` §7.4, caption đặt **trên** bảng và phải tự đủ nghĩa.

**Chính tả và thuật ngữ.**

5. Tiêu đề 2.2: "chia **sẽ**" → "chia **sẻ**".
6. "**concerntration**" (3 chỗ ở 2.1.3) → viết sai chính tả tiếng Anh, và không nhất quán với "nồng độ" dùng ở cùng đoạn. File này thống nhất dùng **"nồng độ"**, nêu kèm "(concentration)" một lần ở lần xuất hiện đầu.
7. 2.1.3: câu "Khi $\alpha$ mỗi thành phần nhỏ hơn một" thiếu chữ, và "$\alpha$càng nhỏ" thiếu dấu cách. Đã sửa.
8. 2.2.2.5: "theo **hương** này" → "theo **hướng** này".
9. 2.2.2.4: ký hiệu hiệp phương sai trong bản Word hiển thị sai thành `∑▒c`; phải là $\Sigma_c$.

**Nội dung.**

10. **IR#3 — mất phủ tối thiểu.** Bản Word đã lược **Deep CORAL** và **FedDecorr** khỏi 2.2.2.5. `00_outline.md` §2, IR#3 liệt kê đích danh hai công trình này trong danh mục Ch.2 buộc phải phủ. Cần quyết định: đưa lại (mỗi công trình một câu ở cuối 2.2.2.5), hoặc sửa IR#3 và ghi lý do vào nhật ký. **Chưa xử lý trong file này.**
11. **Ba quy tắc báo cáo** của mục tính tái lập đã bỏ (so sánh theo cặp · đường đặc tuyến vận hành · chỉ so sánh trong cùng nền tảng) là ràng buộc mà Chương 4 và Chương 5 dựa vào. Nay phải phát biểu ở **Chương 4, mục giao thức đo lường**. Mục 2.3.3 chỉ giữ lại phần lập luận tối thiểu cho đóng góp thứ hai.
12. **Ví dụ CCVR đảo dấu theo ngân sách** ($+0{,}29$ / $-0{,}76$ / $+0{,}97$ điểm phần trăm) chuyển về **Chương 3**, mục kết quả nền từ công trình đã công bố của tác giả. Khi dùng lại phải kèm caveat theo IR#1: ba hạt giống, và nguồn tự xếp loại là kết quả thăm dò.

---

# YÊU CẦU SỬA — 22/09/2026 · lượt rà lối viết + đưa bảng đối chiếu trở lại

> **CÁCH DÙNG KHỐI NÀY.** Đây là **đơn đặt việc**, không phải bản viết lại. Mọi phần phía trên — gồm cả mục *Ghi chú biên tập* — giữ nguyên trạng, **không xoá dòng nào**. Agent thực hiện: sửa vào **bản Word** (bản chính), rồi chép phần đã sửa xuống **dưới** khối này dưới một mốc `# PHIÊN BẢN CHỈNH SỬA — <ngày>` mới. Lịch sử phiên bản giữ đầy đủ theo yêu cầu của học viên.
>
> Nguồn ràng buộc: `00_outline.md` §4 (khối Ch.2 và khối Ch.3), §7.2 (chốt từ "client"), §7.7 (chống giọng văn máy), IR#3 bản sửa 22/09, nhật ký 22/09 lần 3.
>
> ⚠️ Hiện trạng đối chiếu lấy từ **bản Word đã lưu** tại thời điểm rà. Học viên đã sửa một phần danh mục trích dẫn — các mục dưới đây chỉ liệt kê những gì **còn lại** trong bản đã lưu; nếu đã sửa trong cửa sổ Word chưa lưu thì bỏ qua mục tương ứng.

## A. Trích dẫn và lỗi vặt còn lại

✅ **Đã sửa, ghi lại để khỏi rà lần nữa:** `[14]` nay là **Luo và cộng sự, NeurIPS 2021** — đúng bài CCVR. Mục 1 trong *Ghi chú biên tập* phía trên về bài sai coi như đóng.

**A1. MOON và SCAFFOLD vẫn cùng mang số `[6]`.** Mục 2.2.1.2 dùng `[6]` cho SCAFFOLD, mục 2.2.1.3 cũng dùng `[6]` cho MOON. MOON (Li, He, Song — CVPR 2021) chưa có mục riêng trong danh mục.

**A2. Thân bài trích tới `[16]` nhưng danh mục chỉ có 14 mục.** FedProto được trích là `[16]` mà không có mục tương ứng; `[15]` khuyết hẳn. Sau khi thêm MOON thì đánh số lại cho liên tục và rà toàn bộ các số trong thân bài.

**A3. Mục 2.1.2 trích sai nguồn.** Câu mô tả chiến lược nhiễu Gauss ghi `[2]` — tức FedAvg. Phải là `[3]`, NIID-Bench.

**A4. Mục `[5]` FedProx thiếu nơi công bố và năm.** Danh mục hiện chỉ có tên tác giả và nhan đề. Bổ sung: MLSys 2020.

**A5. Chính tả còn lại.** Tiêu đề 2.2: "chia **sẽ**" → "chia **sẻ**" (còn 1 chỗ). "**concerntration**" ở 2.1.3 (còn 2 chỗ) → dùng "nồng độ", nêu kèm "(concentration)" đúng một lần ở lần xuất hiện đầu.

**A6. Cập nhật lại các trường Word (F9).** Danh mục bảng hiện in ra *"Bảng 2.1."* **không kèm tên** dù caption trong thân bài đã có tên. Mục lục vẫn còn dòng *"2.3. Tính tái lập trong FL"* — mục này đã bị bỏ khỏi thân bài. Cả hai là trường cần cập nhật, không phải lỗi soạn thảo.

**A7. Danh mục ký hiệu và chữ viết tắt mới có hai dòng** (FL, non-IID) trong khi thân bài đã dùng SGD, MAFL, MLP, one-hot, và tên các phương pháp. Bổ sung.

## B. Cấu trúc chương

**B1. Thêm mục `2.3. Bảng đối chiếu các họ phương pháp`.** Bản nháp 13 hàng, 6 cột, kèm caption và các ràng buộc đã dựng sẵn ở `00_outline.md` §4, khối Ch.2. Ba điểm không được làm sai:

- **Bảng chỉ chứa phương pháp đã trình bày trong thân bài.** Không thêm công trình mới chỉ để lấp bảng. Mixup không vào bảng vì là kỹ thuật học tập trung.
- **Cột "Chế độ lệch đã đo" phải tra từ chính công trình gốc, không suy đoán.** Ô nào chưa tra thì để `[TRA]` (IR#8). Đây là cột chở lập luận về khoảng trống.
- Caption đặt **trên** bảng, tự đủ nghĩa, giải thích $M$, $C$, $d$, $\mu_c$, $\Sigma_c$ (§7.4).

Bảng này là **Bảng 2.2**. Sau bảng viết một đoạn 3–5 câu đọc bảng, chỉ ra vị trí của FedMix/NaiveMix so với các họ còn lại — không thuật lại từng hàng.

**B2. Dịch số mục `2.3. Khoảng trống luận văn` → `2.4`**, kèm ba tiểu mục con. Rà lại mọi chỗ trong luận văn có tham chiếu tới số mục này.

**B3. Thêm đoạn bắc cầu sang Chương 3 ở cuối chương.** Chương hiện kết thúc đột ngột ở đoạn cuối của mục định vị luận văn. Một đoạn ngắn nói Chương 3 sẽ dựng nền hình thức cho những gì chương này vừa mô tả ở mức khái niệm.

**B4. ⚠️ Ranh giới Chương 2 ↔ Chương 3 — chốt 22/09, ảnh hưởng tới cách sửa chương này.** Chi tiết ở `00_outline.md` §4, đầu khối Ch.3. Tóm tắt phần liên quan tới Ch.2:

- **Ch.2 giữ phần khái niệm, Ch.3 giữ phần hình thức.**
- Mục 2.1.1 giữ ở mức: FL là gì, vì sao chỉ trao đổi tham số, vì sao nhiều bước cục bộ sinh ra drift. Phương trình (2.1) ở lại như một câu giới thiệu.
- Mục 2.1.3 giữ ở mức: Dirichlet dùng để làm gì, $\alpha$ điều khiển cái gì, hai quy ước lệch nhau mười lần và hệ quả đối với tính tái lập.
- **Không bổ sung thêm chi tiết hình thức vào Ch.2 khi sửa**, kể cả khi thấy thiếu — chỗ thiếu đó thuộc Ch.3. Ngược lại, Ch.3 sẽ phát biểu lại đầy đủ chứ không viết "như đã trình bày ở Chương 2".

## C. Lập luận

**C1. Mục 2.2.1 nói quá về hướng không chia sẻ dữ liệu.** Câu *"Các client vẫn chỉ trao đổi tham số mô hình, đúng như FedAvg, không kèm bất kỳ thông tin nào về dữ liệu."* — biến kiểm soát của SCAFFOLD là ước lượng gradient, tức đại lượng tính trực tiếp từ dữ liệu, và cả dòng nghiên cứu gradient inversion tồn tại vì lý do đó. Hạ xuống mức đúng: hướng này không trao đổi thêm đại lượng nào ngoài những gì FedAvg đã trao đổi.

**C2. Đoạn cuối mục 2.2.1 khẳng định trần mà không trích dẫn.** Câu *"phần lớn suy giảm do non-IID định vị được ở tầng phân lớp"* là quan sát của CCVR, nhưng CCVR mãi tới 2.2.2.4 mới xuất hiện. Thêm trích dẫn ngay tại chỗ.

**C3. Cùng đoạn, thay tham chiếu mô tả bằng tên phương pháp.** *"…được trình bày ở tiểu mục về hiệu chuẩn bộ phân lớp phía dưới"* → gọi thẳng tên CCVR. §7.5 yêu cầu gọi tên cụ thể.

**C4. Mục 2.1.2 — phép xoay không nằm trong phân loại của chính Bảng 2.1.** Bảng liệt kê ba chiến lược lệch đặc trưng của NIID-Bench (nhiễu Gauss · FCUBE · phân hoạch theo người viết). Lệch đặc trưng của luận văn là **xoay ảnh**, không có trong bảng, và chương không có câu nào nối hai chỗ. Người đọc gặp "xoay ảnh" ở Chương 1 rồi gặp một phân loại không chứa nó ở Chương 2. Thêm một câu định vị phép xoay so với ba chiến lược đó.

**C5. Mục 2.2.2.5 là đoạn phân tích mạnh nhất chương nhưng bị bỏ rơi.** Lập luận "họ prototype dừng ở moment bậc nhất, nên một vector trung bình mỗi lớp không mô tả được lớp dưới lệch đặc trưng" chính là lý lẽ mạnh nhất cho trục lệch đặc trưng của luận văn, mà mục Khoảng trống không hề dùng lại. Nhắc lại ngắn gọn ở tiểu mục về phạm vi đánh giá theo loại lệch phân phối — nhắc lại bằng nội dung, không bằng tham chiếu mục.

**C6. Mục Khoảng trống còn một phủ định không hạn định.** *"Chưa có cách quy đổi độ nghiêm trọng của hai loại lệch về cùng một thang."* Vi phạm IR#3. Thêm hạn định theo mẫu đã dùng đúng ở tiểu mục trước đó.

**C7. Mục 2.2.2.3 — "Phương thức này không truyền dữ liệu mà truyền tri thức"** → "Hướng này" hoặc "Nhóm phương pháp này". Đang nói về cả một nhánh, không phải một phương pháp.

**C8. ⚠️ Việc còn treo, cần quyết định của học viên.** Đóng góp thứ ba của luận văn là **kiểm toán tính tái lập**, nhưng mục *Tính tái lập trong FL* đã bị bỏ khỏi chương, nên hiện không còn dòng nào trong phần nghiên cứu liên quan đặt nền cho đóng góp đó — một đóng góp không có văn liệu chống lưng, và hội đồng sẽ hỏi. Hai cách: **(a)** trả lại vài câu kèm trích dẫn trong mục 2.4; **(b)** chấp nhận và chuẩn bị trả lời ở buổi bảo vệ.

## D. Thuật ngữ

**D1. Chốt từ "client" cho toàn chương** — quy ước ở `00_outline.md` §7.2. Bản Word đang dùng ba từ cho cùng một thứ: `client` 51 lần, `thiết bị` 18 lần, `bên` 11 lần; riêng mục 2.1.3 có cả *"chia dữ liệu đều cho các **client**"* lẫn *"giao tỉ lệ số mẫu của lớp $j$ cho **bên** $i$"*. Cách sửa:

- Giới thiệu đúng **một lần** ở mục 2.1.1: *"mỗi bên tham gia huấn luyện, sau đây gọi là client"*.
- Từ đó trở đi **chỉ dùng "client"**, kể cả khi thuật lại công trình khác (NIID-Bench, Hsu–Qi–Brown).
- Không dùng "bên" làm danh từ chỉ client nữa; "bên" chỉ còn nghĩa thông thường.
- Chương 1 vẫn dùng "thiết bị" — đó là chủ ý, không phải chỗ cần đồng bộ.

## E. Lối viết — áp §7.7

**E1. AI#1, hạn ngạch cấu trúc tương phản: hạn mức 3 lần mỗi chương.** Các chỗ đếm được trong Chương 2:

1. 2.2.1.3 — *"MOON thao tác trên vector biểu diễn… FedProx đo khoảng cách giữa hai bộ tham số, còn MOON đo khoảng cách giữa tác động của hai bộ tham số ấy lên dữ liệu thật"*
2. 2.2.2.6 — *"Cặp dương… chứ không phải hai mẫu bất kỳ lấy từ hai phía"*
3. 2.2.2.6 — *"mô tả thành phần này như một phép căn chỉnh phân phối biên là không chính xác"*
4. 2.2.2.5 — *"nó chỉ đánh dấu điểm giữa của hai cụm tách rời"* (vế tương phản ngầm)
5. Mục Khoảng trống — *"phản ánh tác động tổng hợp của hai thay đổi, không cho phép quy riêng cho số hạng Taylor"*
6. Mục Khoảng trống — *"chứng minh mẫu trung bình toàn cục phải mang thông tin thật, nhưng chưa chứng minh số hạng đạo hàm là thành phần cần thiết"*

Đề xuất giữ **(2)**, **(3)** và **(6)**: cả ba đều tồn tại để chặn một cách hiểu sai cụ thể, đúng chỗ hạn ngạch nên được tiêu. Ba câu còn lại viết thành câu khẳng định thường.

**E2. AI#2, câu chốt cuối đoạn.** Chương 2 có ít nhất ba đoạn kết bằng câu có nhịp đối: *"…một vị trí có thể không có mẫu thật nào."* (2.2.2.5), *"…người đọc không biết mức lệch thực tế nặng hay nhẹ gấp mười lần."* (2.1.3), *"…thông tin mà nó không bao giờ quan sát được."* (2.2.1). Giữ tối đa một câu mỗi mục hai cấp; các đoạn còn lại cho phép kết nhạt.

**E3. AI#6, dấu gạch ngang chêm.** Đếm lại số dấu `—` chêm giữa câu, đối chiếu hạn mức một lần mỗi trang.

**E4. Chạy ba lệnh tự kiểm ở cuối §7.7** và ghi số đếm vào khối trạng thái đầu file khi nộp bản sửa.


---

# QUYẾT ĐỊNH — 22/09/2026 · chốt mục C8 của khối YÊU CẦU SỬA phía trên

> Khối này **không thay thế** khối yêu cầu phía trên; nó chốt mục còn để ngỏ ở đó. Mọi mục khác của khối yêu cầu giữ nguyên hiệu lực.

## C8 → chọn **(a)**: trả lại phần nền văn liệu về tính tái lập

Đóng góp thứ ba của luận văn là kiểm toán tính tái lập. Sau khi mục *Tính tái lập trong FL* bị bỏ khỏi chương ngày 22/09, đóng góp đó không còn chỗ dựa nào trong phần nghiên cứu liên quan. Nay trả lại **một tiểu mục ngắn**, khoảng nửa trang.

### Vị trí: tiểu mục mới trong mục Khoảng trống

Mục Khoảng trống hiện có ba tiểu mục. Chèn tiểu mục mới vào **giữa**, thành bốn:

| Thứ tự mới | Tiểu mục | Trạng thái |
|---|---|---|
| 1 | Cô lập số hạng khai triển Taylor | đã có |
| 2 | Phạm vi đánh giá theo loại lệch phân phối | đã có |
| **3** | **Tính tái lập của các kết quả đã công bố** | **viết mới** |
| 4 | Định vị luận văn | đã có, dịch xuống một bậc |

⚠️ **Kéo theo ở tiểu mục Định vị luận văn:** câu mở hiện viết *"Ba đóng góp sau tương ứng với **hai** khoảng trống vừa trình bày."* → đổi thành **"ba khoảng trống"**. Sau sửa đổi này, ba khoảng trống ứng một-một với ba đóng góp, và đoạn định vị chặt hơn hẳn bản cũ.

### Ranh giới: chỉ trả lại phần nền văn liệu

⚠️ **Không kéo theo ba quy tắc báo cáo.** Mục bị bỏ ngày 22/09 chứa cả phần nền văn liệu lẫn ba quy tắc báo cáo của luận văn (so sánh theo cặp · đường đặc tuyến vận hành · chỉ so sánh trong cùng nền tảng). **Chỉ phần nền văn liệu được trả lại.** Ba quy tắc kia vẫn thuộc **Chương 4, mục giao thức đo lường** theo quyết định 22/09, và ví dụ CCVR đảo dấu theo ngân sách vẫn thuộc **Chương 3**. Đừng vì tiện tay mà đưa chúng ngược về đây.

### Trích dẫn: mặc định **không thêm mục mới nào**

Đoạn này dựng được hoàn toàn từ tài liệu đã có trong danh mục — NIID-Bench và phần Dirichlet mà chính chương này đã trình bày. Ngân sách trích dẫn còn lại dành cho Chương 3–6 theo quyết định 21/09.

*(Tuỳ chọn, không bắt buộc:* nếu muốn một mốc tổng quát hơn về tái lập trong học máy thì thêm **đúng một** mục. Hai ứng viên thường được dẫn trong bối cảnh này là công trình của Pineau và cộng sự về cải thiện tính tái lập trong nghiên cứu học máy, và các công trình đánh giá lại tiến bộ được công bố trong một lĩnh vực hẹp. **Phải đọc trước khi trích** — không đưa vào danh mục một mục chưa đọc.*)

### Bản nháp nội dung

Bản dưới đây để sửa, không phải để chép nguyên. Đã rà theo §7.7: không có cấu trúc tương phản, không câu chốt cuối đoạn, không dấu gạch ngang chêm, không tham chiếu chéo dạng ký hiệu mục.

> **Tính tái lập của các kết quả đã công bố**
>
> Hai khoảng trống trên đều được phát biểu dựa trên số liệu mà các công trình gốc báo cáo. Điều đó chỉ có nghĩa nếu những con số ấy so sánh được với nhau.
>
> Trong học liên kết, điều kiện đó không hiển nhiên. NIID-Bench [3] ra đời chính vì lý do này: các thuật toán được công bố trên những nền tảng khác nhau, với cách phân hoạch dữ liệu khác nhau, độ mạnh của phương pháp đối chứng khác nhau, và công sức tinh chỉnh siêu tham số dành cho mỗi thuật toán cũng khác nhau, nên mức cải thiện báo cáo ở hai công trình không đặt cạnh nhau được. Cách xử lý của công trình đó là cài đặt lại toàn bộ các thuật toán trong một khung thống nhất rồi đo lại.
>
> Hai quy ước tham số hoá Dirichlet đã trình bày ở trên là một ví dụ cụ thể cho mức độ của vấn đề: cùng một ký hiệu, hai quy ước cho mức lệch khác nhau mười lần, và một công bố không ghi rõ mình dùng quy ước nào thì không dựng lại được. Tham số phân hoạch chỉ là một trong nhiều chỗ mà mô tả trong bài báo có thể không đủ để tái hiện thí nghiệm.
>
> Hệ quả đối với luận văn là một yêu cầu về trình tự: trước khi đo bất cứ thứ gì trên một nền tảng thực nghiệm, phải xác định nền tảng đó thực sự chạy gì. Việc đối chiếu mã nguồn phát hành với mô tả trong bài báo tương ứng vì vậy thuộc về thiết kế đo, và kết quả đối chiếu được báo cáo như đóng góp thứ ba của luận văn.

### Việc kiểm sau khi viết xong

1. Tiểu mục Định vị luận văn đã đổi "hai khoảng trống" → "ba khoảng trống" chưa.
2. Ba quy tắc báo cáo **không** có mặt trong tiểu mục mới.
3. Danh mục tài liệu tham khảo **không phát sinh mục mới** (trừ khi đã chọn phương án tuỳ chọn ở trên).
4. Số trích dẫn `[3]` vẫn trỏ đúng NIID-Bench sau khi đánh số lại danh mục theo mục A1–A2 của khối yêu cầu.

## Đính chính trạng thái các mục cũ trong file này

Hai chỗ phía trên còn ghi *"Chưa xử lý"* nhưng **đã được xử lý ngày 22/09**, giữ nguyên tại chỗ theo quy ước chỉ-append. Đọc theo bản đính chính này:

- **Khối trạng thái đầu file, mục "IR#3 — mất phủ tối thiểu"** và **mục 10 của Ghi chú biên tập**: ✅ **đã đóng.** Quyết định là **sửa IR#3**, không đưa Deep CORAL và FedDecorr trở lại. Hai công trình đó đã được gỡ khỏi danh mục phủ tối thiểu trong `00_outline.md` §2. Lý do: bảng đối chiếu ở mục 2.3 chỉ chứa phương pháp đã xuất hiện trong thân bài, và học viên đã chốt không liệt kê phương pháp chưa được nhắc tới. **Agent sau không đưa hai công trình này vào chương.**
- **Mục 1 của Ghi chú biên tập (trích dẫn CCVR sai bài)**: ✅ **đã đóng** — `[14]` trong bản Word nay là Luo và cộng sự, NeurIPS 2021.

Các mục còn lại của Ghi chú biên tập vẫn còn hiệu lực; trạng thái cập nhật của chúng nằm ở nhóm A của khối `# YÊU CẦU SỬA — 22/09/2026`.


---
---

# PHIÊN BẢN CHỈNH SỬA — 22/09/2026 (lượt 2)

> **CÁCH ĐỌC.** Mọi phần phía trên giữ nguyên trạng để tra lịch sử. Phần dưới đây là **bản hiện hành** của Chương 2; khi chép vào Word, chỉ dùng phần này.
>
> **Tự kiểm §7.7** (chạy trên riêng khối này):
>
> | Phép đếm | Kết quả | Hạn mức | |
> |---|---|---|---|
> | AI#1 — cấu trúc tương phản, **tổng máy đếm** | **6** | ≤ 3 mỗi chương | ⚠️ xem ghi chú |
> | AI#1 — cấu trúc tương phản **mang chức năng tu từ** | **2** | ≤ 3 mỗi chương | ✅ |
> | AI#6 — dấu `—` chêm, ngoài bảng | **7** | ≤ 1 mỗi trang (chương ≈9–10 tr) | ✅ |
> | AI#8 — cụm sáo cấm dùng | **0** | phải bằng 0 | ✅ |
> | AI#4 — câu rào | **1** | đúng 1 mỗi chương | ✅ |
>
> ⚠️ **AI#1 vượt hạn mức nếu đếm bằng máy, và tôi không tự sửa bốn chỗ còn lại.** Lệnh `rg -c "chứ không|không phải .*mà |thay vì"` ở §7.7 bắt cả cụm *"thay vì"* dùng theo nghĩa cơ học, không phải theo nghĩa tu từ mà AI#1 nhắm tới. Sáu chỗ đếm được:
>
> | # | Vị trí | Câu | Xử lý |
> |---|---|---|---|
> | 1 | 2.1.1 | "**Thay vì** gom dữ liệu về một máy chủ rồi huấn luyện tập trung…" | giữ — câu của học viên, AI#10 |
> | 2 | 2.1.3 | "**Thay vì** chia dữ liệu đều cho các client…" | giữ — câu của học viên, AI#10 |
> | 3 | 2.2.2.1 | "**thay vì** huấn luyện trên từng mẫu riêng lẻ…" | giữ — câu của học viên, AI#10 |
> | 4 | caption Bảng 2.2 | "…**không phải** chế độ **mà** phương pháp có thể áp dụng" | giữ — nguyên văn bản nháp caption ở `00_outline.md` §4 |
> | 5 | 2.2.2.6 | "…**chứ không phải** hai mẫu bất kỳ lấy từ hai phía" | giữ — chỗ (2) mà E1 chỉ định |
> | 6 | 2.4.4 | "…**thay cho** một giá trị đo tại một điểm duy nhất" | giữ — định nghĩa "đường đặc tuyến" theo AI#7 |
>
> Bốn chỗ đầu đều là câu mộc của học viên hoặc nguyên văn bản nháp trong dàn bài; AI#10 cấm làm mượt loại câu này chỉ vì nó khớp một mẫu đếm. **Cần học viên quyết:** giữ nguyên và ghi nhận hạn mức AI#1 đo bằng máy sẽ luôn vượt ở chương này, hay nới lệnh đếm ở §7.7 để bỏ qua *"thay vì"* mang nghĩa cơ học.
>
> Hai cấu trúc tương phản mang chức năng tu từ đều nằm ở mục FedBR, đúng chỗ (2) và (3) mà E1 chỉ định. Chỗ (6) mà E1 đề xuất giữ — câu phân định điều FedMix đã chứng minh với điều chưa chứng minh — đã viết thành câu khẳng định có liên từ *"nhưng"*, nên không còn khớp mẫu đếm và không tiêu hạn ngạch.
>
> **Việc đã làm:** A1–A5 (A6, A7 là thao tác trong Word, xem ghi chú cuối khối) · B1–B4 · C1–C7 · C8 theo phương án (a) · D1 · E1–E4.
>
> ⚠️ **Hai chỗ lệch so với đơn đặt việc, có lý do** — xem mục *Ghi chú thi hành* ở cuối khối này: cách phát biểu lại mục C1, và cách xử lý C6 để không phá hạn ngạch AI#4.
>
> ✅ **Cột "Chế độ lệch đã đo" của Bảng 2.2 đã tra xong** (22/09, lượt 3), nguồn là bản toàn văn của từng công trình; bảng truy vết ở mục 6 của *Ghi chú thi hành*. Kết quả: **12 trên 13 phương pháp chỉ đo dưới lệch phân phối nhãn**, chỉ FedBR có lệch đặc trưng được điều khiển tách biệt.
>
> ⚠️ **Việc tra làm lộ một lỗi trong bản trước và đã sửa.** FedMix có chạy trên FEMNIST, mà Bảng 2.1 xếp phân hoạch theo người viết vào nhóm lệch đặc trưng; câu khoảng trống cũ *"chưa có công trình nào thực hiện nó dưới lệch phân phối đặc trưng"* vì vậy sai. Mục 2.4.1 nay thừa nhận FEMNIST và thu phát biểu về *"lệch phân phối đặc trưng được tách riêng khỏi lệch nhãn"*. Chi tiết ở mục 6 của *Ghi chú thi hành*.

---

## 2.1. Học liên kết và thách thức dữ liệu không đồng nhất

### 2.1.1. Khái niệm học liên kết

Federated Learning là mô hình học máy phân tán trong đó dữ liệu huấn luyện không rời khỏi nơi nó được sinh ra. Thay vì gom dữ liệu về một máy chủ rồi huấn luyện tập trung, hệ thống gửi mô hình xuống từng bên tham gia huấn luyện, sau đây gọi là client, để client tự huấn luyện trên dữ liệu của mình, rồi chỉ thu về tham số mô hình đã cập nhật.

Thuật toán nền tảng của mô hình này là FedAvg [2]. Bài toán được hình thức hoá như sau: có $N$ client tham gia, client thứ $i$ giữ tập dữ liệu cục bộ $D_i$ và do đó có hàm mục tiêu riêng $f_i(\omega)$, là sai số trung bình của mô hình tham số $\omega$ trên chính tập dữ liệu ấy. Mục tiêu của cả hệ thống là nghiệm:

$$\omega^{*} = \arg\min_{\omega} f(\omega), \qquad f(\omega) = \sum_{i=1}^{N} p_i f_i(\omega), \qquad p_i = \frac{|D_i|}{\sum_j |D_j|} \tag{2.1}$$

Mục tiêu toàn cục $f$ là trung bình có trọng số của các mục tiêu cục bộ, và trọng số $p_i$ của mỗi client tỉ lệ với lượng dữ liệu nó nắm giữ.

FedAvg tìm nghiệm ấy theo từng vòng truyền thông. Ở vòng thứ $t$, máy chủ phát mô hình toàn cục $\omega_t$ tới một tập con client; mỗi client nhận về, chạy $K$ bước cập nhật SGD trên dữ liệu của mình, rồi gửi bộ tham số đã đổi ngược lên; máy chủ lấy trung bình có trọng số các bộ tham số nhận được để tạo $\omega_{t+1}$, và vòng sau lặp lại.

Chi tiết quyết định nằm ở con số $K$. Nếu $K = 1$, mỗi vòng truyền thông chỉ đổi lấy một bước cập nhật, và thuật toán tương đương SGD tập trung nhưng chi phí truyền thông trở nên không khả thi trong triển khai thực tế. Cho phép $K > 1$, mỗi client chạy nhiều bước trước khi đồng bộ, là cách FL tiết kiệm truyền thông, và cũng chính là nguồn gốc của vấn đề trung tâm mà luận văn này nghiên cứu.

Vấn đề đó xuất hiện khi dữ liệu giữa các client không phân phối đồng nhất, thường viết tắt là non-IID. Khi ấy cực tiểu của hàm mục tiêu cục bộ $f_i$ nằm ở một chỗ khác với cực tiểu của mục tiêu toàn cục $f$. Chạy càng nhiều bước cục bộ, mỗi client càng đi sâu về phía nghiệm riêng của mình, và trung bình của những nghiệm đã trôi lệch ấy không còn là một bước tiến tốt cho mục tiêu chung vì nó có thể rơi vào một vùng mà không client nào coi là tốt. Hiện tượng này được gọi là client drift. Biểu hiện quan sát được của nó gồm hội tụ chậm, đường học dao động mạnh giữa các vòng, và độ chính xác cuối cùng của mô hình tổng hợp thấp hơn rõ rệt so với huấn luyện tập trung trên cùng lượng dữ liệu.

### 2.1.2. Ba dạng không đồng nhất dữ liệu

Cụm từ non-IID thường được dùng như thể nó chỉ một hiện tượng duy nhất, nhưng thực ra nó gộp nhiều tình huống khác nhau về bản chất. NIID-Bench [3], công trình khảo sát thực nghiệm được trích dẫn rộng rãi nhất về chủ đề này, phân biệt sáu chiến lược phân hoạch dữ liệu, thuộc ba nhóm hiện tượng.

**Bảng 2.1.** Ba dạng dữ liệu không đồng nhất trong học liên kết và các chiến lược phân hoạch tương ứng, theo phân loại của NIID-Bench [3]. Cột *Cơ chế* nêu thành phần nào của phân phối liên hợp $P_i(x, y)$ thay đổi giữa các client.

| Nhóm | Cơ chế | Chiến lược phân hoạch |
|---|---|---|
| Lệch phân phối nhãn (label distribution skew) | Phân phối nhãn $P_i(y)$ khác nhau giữa các client, còn $P(x \mid y)$ thì chung | mỗi client giữ đúng $k$ lớp; phân hoạch theo Dirichlet |
| Lệch phân phối đặc trưng (feature distribution skew) | Phân phối đầu vào có điều kiện $P_i(x \mid y)$ khác nhau giữa các client | nhiễu Gauss theo client; bộ tổng hợp FCUBE; phân hoạch theo người viết (FEMNIST) |
| Lệch số lượng (quantity skew) | Kích thước $\lvert D_i \rvert$ khác nhau | Dirichlet trên số mẫu |

Hai nhóm đầu khác nhau về bản chất, và sự phân biệt giữa chúng cần được nêu rõ vì toàn bộ thiết kế thực nghiệm của luận văn dựa trên đó. Ở lệch phân phối nhãn, các client quan sát những lớp khác nhau: một client chứa chủ yếu mẫu thuộc một nhóm lớp, client khác chứa chủ yếu mẫu thuộc nhóm lớp còn lại, song mẫu của cùng một lớp ở hai client vẫn được sinh từ cùng một phân phối. Ở lệch phân phối đặc trưng, tình huống ngược lại: tỉ lệ các lớp tại mọi client có thể như nhau, nhưng mẫu của cùng một lớp lại khác nhau về hình thức do điều kiện thu thập khác nhau, chẳng hạn thiết bị ghi hình, độ chiếu sáng, góc chụp. Hai dạng lệch tác động lên mô hình theo hai cơ chế khác nhau, nên không có cơ sở tiên nghiệm để cho rằng một phương pháp khắc phục được dạng này thì cũng khắc phục được dạng kia.

NIID-Bench tách lệch phân phối đặc trưng khỏi lệch phân phối nhãn ngay ở mức thiết kế chiến lược phân hoạch. Trong chiến lược nhiễu Gauss, toàn bộ tập dữ liệu trước hết được chia ngẫu nhiên và đều cho các client, sau đó mỗi client được thêm nhiễu Gauss ở một mức khác nhau [3]. Thứ tự của hai thao tác quyết định tính chất của phân hoạch thu được: vì phép chia diễn ra trước và là chia đều, phân phối nhãn giữa các client là đồng nhất, và khác biệt duy nhất còn lại nằm ở phân phối đầu vào. Bộ dữ liệu tổng hợp FCUBE cũng giữ nhãn cân bằng, bằng cách gán cho mỗi client hai khối dữ liệu đối xứng qua gốc toạ độ. Công trình này còn dành riêng một mục cho chế độ skew hỗn hợp, trong đó phân hoạch Dirichlet theo nhãn được kết hợp với nhiễu theo đặc trưng.

Cách mô phỏng lệch đặc trưng mà luận văn sử dụng không nằm trong ba chiến lược trên. Luận văn xoay ảnh những góc khác nhau ở những client khác nhau, nên phân phối đầu vào của mỗi client là ảnh gốc qua một phép quay riêng. Đặt cạnh nhiễu Gauss, phép xoay giữ nguyên thông tin chứa trong ảnh và chỉ đổi hệ toạ độ, vì vậy nó nằm ở phía dễ của phổ lệch đặc trưng. Đặt cạnh phân hoạch theo người viết của FEMNIST, phép xoay là lệch nhân tạo có tham số điều khiển được, và cái giá phải trả là nó không phản ánh một nguồn lệch có thật trong triển khai. Chương 3 trình bày cách mô hình hoá phân phối góc xoay.

### 2.1.3. Quy ước tham số hoá Dirichlet

Công cụ phổ biến nhất để mô phỏng lệch phân phối nhãn là phân hoạch Dirichlet. Thay vì chia dữ liệu đều cho các client, ta rút ngẫu nhiên một vector tỉ lệ từ phân phối Dirichlet rồi chia theo tỉ lệ đó. Phân phối Dirichlet nhận giá trị trên đơn hình xác suất, tức tập các vector có mọi thành phần không âm và tổng bằng một, nên mỗi lần rút đều cho ra một vector tỉ lệ hợp lệ.

Hình dạng của phân phối này được điều khiển bởi tham số nồng độ (concentration), ký hiệu $\alpha$, và chính tham số ấy quyết định mức độ lệch của phân hoạch thu được. Khi nồng độ mỗi thành phần lớn hơn một, các vector rút ra tập trung quanh vector đều, nên mọi client nhận tỉ lệ lớp xấp xỉ như nhau và phân hoạch gần với đồng nhất. Khi nồng độ mỗi thành phần nhỏ hơn một, khối lượng xác suất dồn về phía các đỉnh của đơn hình: vector rút ra có một vài thành phần nhận giá trị gần một, còn các thành phần còn lại gần không. Trong chế độ thứ hai, mỗi client trên thực tế chỉ giữ mẫu của một vài lớp, và nồng độ càng nhỏ thì số lớp hiệu dụng mà client quan sát được càng ít. Đây là lý do nồng độ được dùng làm tham số điều khiển độ lệch phân phối nhãn.

Khó khăn nằm ở chỗ các nghiên cứu sử dụng hai quy ước khác nhau dưới cùng một ký hiệu, và điều này ảnh hưởng trực tiếp tới khả năng tái lập của các kết quả được công bố.

Quy ước thứ nhất, do Hsu, Qi và Brown đưa ra, lấy mẫu theo trục các lớp, thực hiện cho từng client: với mỗi client, rút một vector phân phối lớp $q \sim \mathrm{Dir}(\alpha \cdot p)$, trong đó $p$ là phân phối lớp tiên nghiệm, thường là phân phối đều, và do đó thoả $\sum_c p_c = 1$. Vì tổng các thành phần của $p$ bằng 1, tham số $\alpha$ ở đây là nồng độ tổng, còn nồng độ của mỗi thành phần chỉ là $\alpha / C$ với $C$ là số lớp [4].

Quy ước thứ hai, áp dụng trong nghiên cứu NIID-Bench, lấy mẫu theo trục các client, thực hiện cho từng lớp, là chuyển vị của quy ước trên: với mỗi lớp $k$, rút một vector $p_k \sim \mathrm{Dir}_N(\beta)$ trên $N$ client, rồi giao tỉ lệ $p_{k,j}$ số mẫu của lớp $k$ cho client $j$. Ở đây $\beta$ là nồng độ mỗi thành phần, và nồng độ tổng là $N\beta$ [3].

Với CIFAR-10, tức 10 lớp chia cho 10 client, ký hiệu "0,5" theo quy ước thứ nhất tương ứng nồng độ mỗi thành phần là 0,05, còn theo quy ước thứ hai thì đúng bằng 0,5, chênh nhau mười lần. Một công bố ghi "Dirichlet $\alpha = 0{,}1$" mà không nói rõ đang dùng quy ước nào thì không tái lập được, vì người đọc không biết mức lệch thực tế nặng hay nhẹ gấp mười lần.

Luận văn này do đó áp dụng một quy tắc báo cáo cố định: mỗi lần nêu tham số Dirichlet đều ghi đủ bộ ba gồm vector nồng độ, trục lấy mẫu và số thành phần, kèm dòng quy đổi $\alpha_{\text{Hsu}} = N \cdot \beta_{\text{NIID-Bench}}$ áp dụng khi phân phối tiên nghiệm là đều.

---

## 2.2. Tăng cường dữ liệu và chia sẻ thống kê trong FL

Các phương pháp khắc phục client drift có thể chia thành hai hướng. Hướng thứ nhất sửa cách học mà giữ nguyên lượng thông tin được trao đổi. Hướng thứ hai trao đổi thêm thông tin về dữ liệu với một lượng nhỏ và ở dạng đã được xử lý để không bộc lộ dữ liệu gốc.

### 2.2.1. Hướng tiếp cận không chia sẻ dữ liệu

Hướng thứ nhất chống client drift bằng cách can thiệp vào quá trình tối ưu hoá. Các phương pháp trong hướng này không chia sẻ dữ liệu, cũng không chia sẻ thống kê mô tả phân phối dữ liệu; đại lượng được trao đổi thêm, nếu có, thuộc về chính quá trình tối ưu hoá. Ranh giới ấy không tuyệt đối. Biến kiểm soát của SCAFFOLD là một ước lượng gradient, mà gradient được tính trực tiếp từ dữ liệu cục bộ, và cả dòng nghiên cứu về khôi phục dữ liệu từ gradient tồn tại vì lý do đó.

#### 2.2.1.1. Ràng buộc trên bộ tham số

FedProx [5] là phương pháp đơn giản nhất trong nhóm và cũng được trích dẫn nhiều nhất. Nó thêm vào hàm mất mát cục bộ một số hạng phạt, kéo mô hình cục bộ về gần mô hình toàn cục của vòng hiện tại. Số hạng này không cho client đi quá xa trong $K$ bước cục bộ, và vì vậy làm nhẹ bớt độ trôi, nhưng cũng đồng thời làm chậm tốc độ học, nên cường độ phạt là một đánh đổi phải chỉnh tay. FedProx là một trong hai phương pháp đối chứng được dùng trong phần thực nghiệm của luận văn.

#### 2.2.1.2. Hiệu chỉnh hướng gradient

SCAFFOLD [6] xử lý vấn đề ở tầng sâu hơn, tại chính bộ tối ưu. Mỗi client duy trì một biến kiểm soát (control variate) ước lượng phần lệch giữa hướng gradient cục bộ của nó và hướng gradient toàn cục, rồi trừ đi phần lệch đó ở mỗi bước cập nhật. Về mặt lý thuyết đây là kỹ thuật giảm phương sai kinh điển áp cho bối cảnh liên kết, và nó cho bảo đảm hội tụ mạnh hơn FedProx. Cái giá là mỗi vòng phải truyền thêm biến kiểm soát, tức chi phí truyền thông tăng gấp đôi.

#### 2.2.1.3. Ràng buộc trên biểu diễn

Để mô tả MOON [7] cần tách mạng phân loại thành hai phần. Phần thứ nhất là bộ trích xuất đặc trưng: nó nhận ảnh đầu vào và trả về một vector $d$ chiều, gọi là biểu diễn hay đặc trưng của ảnh đó. Phần thứ hai là tầng phân lớp (classifier head), nhận vector đặc trưng và trả về điểm số cho từng lớp. Cơ chế của MOON như sau: với cùng một ảnh cục bộ, ba mô hình cho ba biểu diễn khác nhau, gồm mô hình toàn cục vừa nhận được từ máy chủ, mô hình cục bộ đang được huấn luyện, và mô hình cục bộ ở cuối vòng trước. MOON thêm một số hạng phạt kéo biểu diễn của mô hình đang huấn luyện lại gần biểu diễn của mô hình toàn cục, đồng thời đẩy nó ra xa biểu diễn của mô hình cục bộ vòng trước. Lập luận đằng sau là mô hình toàn cục mang thông tin của mọi client nên biểu diễn của nó ít lệch hơn, còn mô hình cục bộ vòng trước là hiện thân của phần lệch đã tích luỹ, nên đáng dùng làm mốc để tránh xa.

Điểm phân biệt giữa MOON và hai phương pháp trên nằm ở đại lượng bị ràng buộc. FedProx và SCAFFOLD thao tác trên vector tham số của toàn mạng, đo khoảng cách giữa hai bộ tham số. MOON thao tác trên vector biểu diễn mà bộ trích xuất đặc trưng sinh ra, tức đo khoảng cách giữa tác động của hai bộ tham số ấy lên dữ liệu thật. Hai mạng có tham số rất khác nhau vẫn có thể sinh ra biểu diễn gần như nhau, nên ràng buộc của MOON nới hơn và ít cản trở việc học hơn, trong khi vẫn giữ được mục tiêu là không để mô hình cục bộ trôi xa.

Vì không trao đổi thông tin mô tả phân phối dữ liệu, hướng tiếp cận này giữ nguyên bề mặt rủi ro riêng tư của FedAvg. Đó là ưu điểm lớn, đồng thời là trần của nó: nếu phân phối dữ liệu của các client thực sự khác nhau, thì không một thao tác nào trên quỹ đạo tối ưu hoá có thể cấp cho một client thông tin về những gì nó chưa bao giờ quan sát được. Bên cạnh đó, các phương pháp trong hướng này can thiệp chủ yếu vào quá trình huấn luyện, trong khi Luo và cộng sự [15] cho thấy phần lớn suy giảm do non-IID định vị được ở tầng phân lớp. Quan sát đó dẫn tới CCVR và cả nhóm phương pháp hiệu chuẩn tầng phân lớp trình bày ở mục 2.2.2.4.

### 2.2.2. Hướng tiếp cận có chia sẻ dữ liệu

Hướng này chấp nhận truyền thêm một lượng thông tin nhỏ ngoài tham số mô hình, đủ để mỗi client có một hình dung về phân phối của toàn hệ thống, nhưng nhỏ tới mức không phá vỡ ràng buộc riêng tư của bài toán. Các nhánh trong hướng này khác nhau ở hai trục: thông tin gì được truyền, và thông tin đó được dùng như thế nào.

Zhao và cộng sự [8] cho thấy chỉ cần chia sẻ cho mọi client một tập dữ liệu nhỏ có phân phối lớp cân bằng là đủ khôi phục phần lớn độ chính xác đã mất do non-IID. Kết quả ấy có hai mặt: một mặt, nó chứng minh lượng thông tin cần bổ sung là nhỏ; mặt khác, tập được chia sẻ gồm dữ liệu thô, tức trái với nguyên tắc nền tảng của học liên kết.

Năm nhánh trình bày dưới đây có thể được đọc như những nỗ lực khác nhau nhằm giữ lại lợi ích của việc bổ sung thông tin mà giảm mức riêng tư phải đánh đổi. Nhánh cuối cùng trình bày FedBR, công trình được luận văn dùng làm nền tảng thực nghiệm.

#### 2.2.2.1. Học liên kết tăng cường trung bình và bài toán xấp xỉ global Mixup

Mixup [9] là một kỹ thuật tăng cường dữ liệu đơn giản và rất hiệu quả trong học tập trung: thay vì huấn luyện trên từng mẫu riêng lẻ, mô hình được huấn luyện trên các tổ hợp lồi của các cặp mẫu, với nhãn cũng được trộn theo đúng tỉ lệ ấy. Trộn hai ảnh theo tỉ lệ 70–30 thì nhãn đích cũng là 70% lớp thứ nhất và 30% lớp thứ hai.

Áp ý tưởng này cho học liên kết gặp trở ngại ngay từ bước đầu. Phiên bản có giá trị nhất trong bối cảnh non-IID là global Mixup, trộn mẫu của client này với mẫu của client khác, vì chính sự pha trộn xuyên client mới mang thông tin mà client không tự có. Nhưng làm được điều đó thì phải truy cập dữ liệu thô xuyên client, tức vi phạm đúng cái ràng buộc định nghĩa bài toán.

FedMix [1] đề xuất khung Mean Augmented Federated Learning (MAFL) để vượt trở ngại đó. Mỗi client tính một số ít mẫu trung bình đại diện: lấy $M$ ảnh cục bộ, tính trung bình pixel theo từng vị trí để được một ảnh, đồng thời tính trung bình các nhãn one-hot tương ứng để được một nhãn mềm, rồi chia sẻ các cặp ảnh-nhãn trung bình đó cho các client khác thông qua máy chủ. Phép lấy trung bình đóng vai trò một cơ chế nén: ảnh riêng lẻ không rời khỏi client, chỉ bản đã bị làm mịn được chia sẻ, và số ảnh được gộp $M$ là tham số điều khiển mức nén, $M$ càng lớn thì ảnh chia sẻ càng mờ và càng khó truy ngược về mẫu gốc.

Bên trong khung MAFL, FedMix định nghĩa hai thuật toán khác nhau. NaiveMix trộn trực tiếp dữ liệu cục bộ với mẫu trung bình nhận được rồi tính hàm mất mát trên đầu vào đã trộn, nghĩa là mẫu trung bình đi qua toàn bộ mạng như một ảnh bình thường. FedMix thì khai triển Taylor bậc nhất chính hàm mất mát ấy quanh đầu vào đã co tỉ lệ, và thu được một dạng trong đó mẫu trung bình không còn đi vào lượt truyền xuôi nữa, mà chỉ còn xuất hiện trong một tích vô hướng với đạo hàm của hàm mất mát theo đầu vào. Hai thuật toán khác nhau ở hai chỗ cùng lúc: số hạng Taylor được thêm vào, và mẫu trung bình bị rút khỏi lượt truyền xuôi. Vì hai thay đổi này xảy ra đồng thời, chênh lệch hiệu năng đo được giữa chúng là tác động tổng hợp của cả hai.

#### 2.2.2.2. Dữ liệu ảo

Một hướng triệt để hơn cắt đứt hoàn toàn liên hệ với dữ liệu thật. VHL [10] sinh một tập dữ liệu ảo từ nhiễu, gán nhãn cho tập ảo đó, phát cho mọi client, rồi trong quá trình huấn luyện cục bộ ép đặc trưng của dữ liệu thật tiến về gần đặc trưng của dữ liệu ảo cùng lớp. Vì tập ảo không chứa thông tin của bất kỳ người dùng nào, rủi ro riêng tư gần như bị loại bỏ hẳn; đổi lại, mọi client chia sẻ chung một hệ quy chiếu nhân tạo để căn chỉnh không gian đặc trưng về. Tuy nhiên, VHL yêu cầu nhãn. Theo số liệu được đối chiếu trong FedBR [11], VHL cần khoảng 2.000 mẫu ảo cho CIFAR-10 và 20.000 cho CIFAR-100, tỉ lệ thuận với số lớp, và các mẫu này bắt buộc phải có nhãn.

#### 2.2.2.3. Chưng cất tri thức

Nhóm phương pháp này không truyền dữ liệu mà truyền tri thức của mô hình. Ý tưởng chung là dùng đầu ra của mô hình toàn cục trên một tập dữ liệu trung gian làm mục tiêu để mô hình cục bộ học theo, thay cho việc so sánh tham số với tham số.

FedDF [12] dùng logits của mô hình toàn cục trên một tập proxy không cần nhãn làm mục tiêu chưng cất, và thực hiện việc chưng cất này ở máy chủ sau khi đã gộp mô hình. FedNTD [13] chưng cất có chọn lọc hơn: nó chỉ giữ lại phần phân phối trên các lớp không phải nhãn đúng, với lập luận rằng chính phần này mang thông tin toàn cục mà mô hình cục bộ có xu hướng quên khi chỉ nhìn thấy vài lớp. FedGen [14] loại bỏ nhu cầu về tập proxy bằng cách học một bộ sinh nhẹ ngay tại máy chủ, rồi dùng bộ sinh đó tạo dữ liệu cho việc chưng cất.

#### 2.2.2.4. Hiệu chuẩn bộ phân lớp từ thống kê lớp

Nhóm phương pháp này xuất phát từ một quan sát thực nghiệm cụ thể. Quan sát ấy liên quan tới cách hai phần của mạng phân loại, là bộ trích xuất đặc trưng và tầng phân lớp, chịu ảnh hưởng khác nhau bởi tính không đồng nhất của dữ liệu: dưới lệch phân phối nhãn, bộ trích xuất đặc trưng vẫn học được biểu diễn tương đối tốt, trong khi tầng phân lớp lệch mạnh về các lớp chiếm đa số tại chỗ. Nếu quan sát trên là đúng thì chỉ cần hiệu chỉnh riêng tầng cuối là đủ, và việc ấy rẻ hơn rất nhiều so với can thiệp vào toàn bộ quá trình huấn luyện.

CCVR [15] là công trình mẫu của nhánh này. Mỗi client ước lượng, cho từng lớp $c$, vector trung bình đặc trưng $\mu_c$ và ma trận hiệp phương sai $\Sigma_c$, rồi gửi các thống kê ấy lên máy chủ. Máy chủ mô hình hoá mỗi lớp bằng một phân phối Gauss với hai tham số đó, lấy mẫu ra các đặc trưng ảo, và huấn luyện lại riêng tầng phân lớp trên tập đặc trưng ảo cân bằng này. Không một mẫu dữ liệu thô nào rời khỏi client; chỉ có thống kê bậc một và bậc hai của đặc trưng.

#### 2.2.2.5. Căn chỉnh đặc trưng có điều kiện lớp

Nhóm phương pháp này không sửa tầng phân lớp sau khi huấn luyện xong, mà ràng buộc không gian đặc trưng ngay trong lúc huấn luyện cục bộ.

FedProto [16] là công trình nền. Mỗi client tính cho từng lớp một prototype, là trung bình đặc trưng của các mẫu thuộc lớp đó; máy chủ gộp các prototype cục bộ thành prototype toàn cục cho từng lớp; và ở vòng sau, mỗi client bị phạt theo khoảng cách từ đặc trưng nó sinh ra tới prototype toàn cục của lớp tương ứng. Kết quả là các client dần thống nhất với nhau về vị trí của mỗi lớp trong không gian đặc trưng. Chi phí truyền thông rất thấp: $C$ vector $d$ chiều mỗi vòng.

Điểm chung của các phương pháp theo hướng này là chúng dừng ở moment bậc nhất. Chúng đồng nhất vị trí của cụm đặc trưng ứng với mỗi lớp giữa các client, nhưng không ràng buộc gì về hình dạng của cụm đó. Giới hạn ấy không gây hậu quả gì dưới lệch phân phối nhãn, nơi cùng một lớp ở hai client vẫn là cùng một phân phối ảnh và do đó rơi vào cùng một vùng đặc trưng. Dưới lệch phân phối đặc trưng thì khác hẳn: cùng một lớp ở hai client có thể nằm ở hai vùng tách rời của không gian, và một vector trung bình duy nhất khi đó rơi vào điểm giữa hai cụm, một vị trí có thể không có mẫu thật nào.

#### 2.2.2.6. FedBR

FedBR [11] giữ một vai trò đặc biệt trong luận văn: nó là nền tảng thực nghiệm mà toàn bộ thí nghiệm mới được chạy trên đó. FedBR nhắm vào hai biểu hiện của thiên lệch học cục bộ bằng hai thành phần, cả hai đều vận hành trên một tập pseudo-data dùng chung, tập dữ liệu giả này được xây bằng phép lấy trung bình mẫu ngẫu nhiên (Random Sample Mean) hoặc bằng một phương án gọi là Mixture.

Thành phần thứ nhất cân bằng phân phối đầu ra của tầng phân lớp trên tập pseudo-data, chống lại xu hướng mô hình cục bộ gán mọi mẫu vào những lớp xuất hiện nhiều tại chỗ. Thành phần thứ hai là một bài toán min-max trên không gian đặc trưng: một tầng chiếu được huấn luyện theo lối đối kháng để phân biệt đặc trưng do mô hình cục bộ sinh ra với đặc trưng do mô hình toàn cục sinh ra, sau đó bộ trích xuất cục bộ được huấn luyện ngược lại để đặc trưng của pseudo-data gần đặc trưng toàn cục mà xa đặc trưng của dữ liệu cục bộ thật.

Thành phần thứ hai ghép cặp theo từng mẫu, không phải theo phân phối. Cặp dương trong hàm mất mát là cặp gồm đặc trưng cục bộ và đặc trưng toàn cục của cùng một mẫu pseudo-data, chứ không phải hai mẫu bất kỳ lấy từ hai phía. Ràng buộc theo từng mẫu trên cùng một đầu vào chặt hơn căn chỉnh phân phối biên, vì nó ràng buộc mọi thống kê có điều kiện tính được trên tập pseudo-data, trong khi căn chỉnh biên chỉ ràng buộc các moment tổng. Do đó, mô tả thành phần này như một phép căn chỉnh phân phối biên là không chính xác.

Phạm vi đánh giá của FedBR là lý do luận văn chọn nó làm nền tảng. Ngoài phân hoạch Dirichlet theo nhãn, công trình này còn đo trên RotatedMNIST, trên CIFAR-10 với mỗi client xoay ảnh một góc riêng, và trên PACS, tức ba cấu hình lệch phân phối đặc trưng. Trong số các phương pháp được trình bày ở chương này, FedBR là công trình duy nhất có sẵn cả hai chế độ lệch, nên nó là nền tảng cho phép chạy cùng một phép đối chứng dưới cả lệch nhãn lẫn lệch đặc trưng mà không phải tự dựng lại đường ống thí nghiệm.

---

## 2.3. Bảng đối chiếu các họ phương pháp

Bảng 2.2 đặt các phương pháp đã trình bày trong chương lên cùng một hệ trục. Trục chính là lượng thông tin trao đổi thêm ngoài tham số mô hình, vì đó đồng thời là trục riêng tư: phương pháp trao đổi càng nhiều thông tin về dữ liệu thì càng phải giải trình về mặt riêng tư. Mixup không có mặt trong bảng vì nó là kỹ thuật học tập trung, trong chương chỉ đóng vai dẫn vào global Mixup.

**Bảng 2.2.** Đối chiếu các phương pháp khắc phục dữ liệu không đồng nhất được trình bày trong chương này, theo lượng thông tin trao đổi thêm ngoài tham số mô hình. $M$ là số ảnh cục bộ được gộp trong một mẫu trung bình đại diện; $C$ là số lớp; $d$ là số chiều vector đặc trưng; $\mu_c$ và $\Sigma_c$ là vector trung bình và ma trận hiệp phương sai của đặc trưng thuộc lớp $c$. Cột cuối ghi chế độ lệch phân phối mà công trình gốc thực sự đo, không phải chế độ mà phương pháp có thể áp dụng; ký hiệu *nhãn*, *số lượng*, *đặc trưng* theo phân loại ở Bảng 2.1, còn *tự nhiên* chỉ các phân hoạch có sẵn trong dữ liệu, như tách theo người viết hoặc theo vai diễn, nơi ba loại lệch xuất hiện cùng lúc và không tách rời được.

| Phương pháp | Thông tin chia sẻ thêm | Cần nhãn? | Bậc thống kê | Chi phí truyền thông thêm | Chế độ lệch đã đo |
|---|---|---|---|---|---|
| FedProx [5] | không | – | – | không | nhãn, số lượng; tự nhiên |
| SCAFFOLD [6] | biến kiểm soát (ước lượng độ lệch gradient) | không | – | gấp đôi | nhãn |
| MOON [7] | không | – | – | không | nhãn |
| Zhao và cộng sự [8] | tập dữ liệu thô nhỏ, cân bằng lớp | có, nhãn cứng | dữ liệu thô | một lần, theo cỡ tập | nhãn |
| NaiveMix [1] | ảnh trung bình của $M$ ảnh cục bộ kèm nhãn mềm; trộn thẳng vào đầu vào | nhãn mềm | bậc nhất | theo số mẫu đại diện | nhãn, số lượng; tự nhiên |
| FedMix [1] | cùng thông tin như NaiveMix; vào mục tiêu qua tích vô hướng với đạo hàm theo đầu vào | nhãn mềm | bậc nhất | như NaiveMix | nhãn, số lượng; tự nhiên |
| VHL [10] | tập dữ liệu ảo sinh từ nhiễu (~2.000 mẫu cho CIFAR-10, ~20.000 cho CIFAR-100) | có, phải gán nhãn cho tập ảo | không lấy từ dữ liệu thật | một lần | nhãn |
| FedDF [12] | logits của mô hình toàn cục trên tập proxy | không cần nhãn cho proxy | – | tập proxy đặt ở máy chủ | nhãn |
| FedNTD [13] | phần phân phối trên các lớp không phải nhãn đúng | dùng nhãn cục bộ sẵn có | – | không | nhãn, số lượng |
| FedGen [14] | bộ sinh nhẹ học tại máy chủ | có, bộ sinh có điều kiện theo nhãn | – | truyền tham số bộ sinh | nhãn; tự nhiên |
| CCVR [15] | $\mu_c$ và $\Sigma_c$ của đặc trưng theo từng lớp | có, thống kê theo lớp | bậc hai | một lần, $C \times (d + d^2)$ | nhãn |
| FedProto [16] | prototype, tức trung bình đặc trưng theo lớp | có | bậc nhất | $C$ vector $d$ chiều mỗi vòng | nhãn, số lượng |
| FedBR [11] | tập pseudo-data dùng chung (Random Sample Mean hoặc Mixture) | nhãn mềm ở nhánh Mixture | bậc nhất | theo cỡ pseudo-data | **nhãn, đặc trưng** |

Đọc theo cột, FedMix và NaiveMix chiếm một vị trí riêng. Chúng là hai phương pháp duy nhất trong bảng thao tác ở không gian đầu vào, trong khi mọi phương pháp có chia sẻ thống kê còn lại đều làm việc trên không gian đặc trưng. Chúng cũng chỉ dùng thống kê bậc nhất và không tách thông tin theo lớp, nên lượng cấu trúc mà chúng khai thác được từ dữ liệu là ít nhất trong bảng. Bù lại, chi phí truyền thông của chúng thuộc nhóm thấp nhất và chỉ phát sinh một lần. Chính vị trí nghèo thông tin ấy làm câu hỏi trung tâm của luận văn đáng đặt ra: phần lý thuyết của cơ chế, tức số hạng khai triển Taylor, có thực sự đóng góp gì không, và nếu có thì trong điều kiện nào.

Cột cuối cho thấy một hình ảnh khác. Trong mười ba phương pháp, chỉ FedBR có thí nghiệm dưới lệch phân phối đặc trưng được điều khiển tách biệt, qua RotatedMNIST, CIFAR-10 xoay và PACS. Mười hai phương pháp còn lại đo dưới lệch phân phối nhãn, một số kèm lệch số lượng. Ba phương pháp có chạy thêm trên phân hoạch tự nhiên, như FEMNIST tách theo người viết ở FedMix và NaiveMix, hoặc CelebA gộp theo người ở FedGen; những cấu hình ấy có chứa lệch đặc trưng, nhưng chứa đồng thời cả lệch nhãn lẫn lệch số lượng, nên không dùng để quy kết riêng cho loại lệch nào. Đây là căn cứ thực tế cho khoảng trống phát biểu ở mục 2.4.2.

---

## 2.4. Khoảng trống luận văn

### 2.4.1. Cô lập số hạng khai triển Taylor

Công trình FedMix [1] có đối chứng giữa FedMix và NaiveMix, và trình bày kết quả đối chứng ở bảng chính. Tuy nhiên, như mục 2.2.2.1 đã nêu, hai thuật toán khác nhau ở hai chỗ cùng lúc: số hạng Taylor được thêm vào, và mẫu trung bình bị rút khỏi lượt truyền xuôi. Chênh lệch hiệu năng giữa chúng do đó là tác động tổng hợp của hai thay đổi, và chỉ riêng con số ấy không đủ để quy kết cho số hạng Taylor.

Cấu hình đủ để cô lập số hạng này là cấu hình giữ nguyên điểm đánh giá hàm mất mát, tức mẫu trung bình vẫn tham gia lượt truyền xuôi như ở FedMix, và chỉ loại bỏ số hạng đạo hàm. Cấu hình như vậy không xuất hiện trong bài báo FedMix, kể cả ở phần phụ lục.

FedMix có khảo sát một trục khác, trực giao với trục vừa nêu. Công trình đó giữ nguyên số hạng đạo hàm và thay dữ liệu đưa vào số hạng ấy bằng nhiễu ngẫu nhiên hoặc bằng trung bình của dữ liệu cục bộ, và cho thấy cả hai phương án thay thế đều cho kết quả kém hơn. Kết quả này chứng minh mẫu trung bình toàn cục phải mang thông tin thật, nhưng chưa chứng minh số hạng đạo hàm là thành phần cần thiết. Vẫn có khả năng mẫu trung bình mang thông tin hữu ích trong khi cách đưa nó vào qua đạo hàm không hiệu quả hơn cách trộn trực tiếp vào đầu vào.

Hai đặc điểm khác của phép đối chứng gốc cũng hạn chế khả năng quy kết. Trọng số trộn $\lambda$ được tinh chỉnh riêng cho từng thuật toán, nên hai nhánh được đo tại hai giá trị $\lambda$ khác nhau, và chênh lệch quan sát được chứa cả ảnh hưởng của công sức tinh chỉnh không đồng đều giữa hai nhánh. Bên cạnh đó, chính công trình gốc cho thấy giá trị $\lambda$ tốt nhất của NaiveMix cho kết quả tiến sát FedMix.

Bản thân FedMix có chạy trên FEMNIST, tức phân hoạch tách theo người viết, mà Bảng 2.1 xếp vào nhóm lệch phân phối đặc trưng. Phân hoạch ấy đồng thời mang cả lệch nhãn lẫn lệch số lượng, vì mỗi người viết vừa có nét chữ riêng, vừa viết những ký tự khác nhau với số lượng khác nhau; kết quả trên FEMNIST do đó không quy riêng cho loại lệch nào. Trong số các công trình trích dẫn FedMix mà luận văn khảo sát được, chưa có công trình nào thực hiện lại phép đối chứng này một cách độc lập, và cũng chưa có công trình nào thực hiện nó dưới lệch phân phối đặc trưng được tách riêng khỏi lệch nhãn.

### 2.4.2. Phạm vi đánh giá theo loại lệch phân phối

NIID-Bench [3] tách lệch phân phối đặc trưng khỏi lệch phân phối nhãn và dành riêng một mục cho chế độ skew hỗn hợp, như mục 2.1.2 đã trình bày. Khảo sát ở chế độ này đo bốn thuật toán là FedAvg, FedProx, SCAFFOLD và FedNova, đều thuộc hướng can thiệp vào quá trình tối ưu hoá. Các phương pháp thuộc hướng chia sẻ dữ liệu, trong đó có họ tăng cường trung bình, không nằm trong phạm vi khảo sát đó.

Cột cuối của Bảng 2.2 cho thấy tình trạng này không riêng ở NIID-Bench mà ở cả nhóm công trình được trình bày trong chương. Trong mười ba phương pháp, chỉ FedBR có thí nghiệm dưới lệch phân phối đặc trưng được điều khiển tách biệt. Phần còn lại đo dưới lệch phân phối nhãn, và ba phương pháp có chạy thêm trên phân hoạch tự nhiên, nơi ba loại lệch xuất hiện cùng lúc.

Hai hướng tác động lên những thành phần khác nhau của mô hình: một bên điều chỉnh quỹ đạo tối ưu hoá, một bên bổ sung thông tin về phân phối dữ liệu. Vì vậy không có cơ sở để suy kết luận của hướng này sang hướng kia, và hành vi của họ tăng cường trung bình dưới lệch phân phối đặc trưng vẫn còn là câu hỏi để ngỏ.

Mục 2.2.2.5 cho thấy vì sao câu hỏi ấy không trả lời được bằng suy luận. Các phương pháp căn chỉnh prototype dừng ở moment bậc nhất, và dưới lệch phân phối đặc trưng, một vector trung bình cho mỗi lớp không còn mô tả được lớp đó. Cơ chế tăng cường trung bình cũng chia sẻ một đại lượng bậc nhất, tính trên không gian đầu vào. Giới hạn của moment bậc nhất có lặp lại ở đó hay không là một câu hỏi thực nghiệm, và không suy ra được từ trường hợp prototype vì hai cơ chế tác động lên hai không gian khác nhau.

NIID-Bench còn để lại một vấn đề mà luận văn thừa hưởng. Hai loại lệch được điều khiển bởi hai tham số không cùng đơn vị: nồng độ Dirichlet trên phân phối lớp đối với lệch nhãn, và cường độ nhiễu hoặc biên độ biến đổi hình học đối với lệch đặc trưng. NIID-Bench không đề xuất cách quy đổi độ nghiêm trọng của hai loại lệch về cùng một thang, và luận văn cũng không giải quyết vấn đề này, mà sử dụng một phương án căn chỉnh vận hành trình bày ở Chương 4.

### 2.4.3. Tính tái lập của các kết quả đã công bố

Hai khoảng trống trên đều được phát biểu dựa trên số liệu mà các công trình gốc báo cáo. Điều đó chỉ có nghĩa nếu những con số ấy so sánh được với nhau.

Trong học liên kết, điều kiện đó không hiển nhiên. NIID-Bench [3] ra đời chính vì lý do này: các thuật toán được công bố trên những nền tảng khác nhau, với cách phân hoạch dữ liệu khác nhau, độ mạnh của phương pháp đối chứng khác nhau, và công sức tinh chỉnh siêu tham số dành cho mỗi thuật toán cũng khác nhau, nên mức cải thiện báo cáo ở hai công trình không đặt cạnh nhau được. Cách xử lý của công trình đó là cài đặt lại toàn bộ các thuật toán trong một khung thống nhất rồi đo lại.

Hai quy ước tham số hoá Dirichlet đã trình bày ở mục 2.1.3 là một ví dụ cụ thể cho mức độ của vấn đề: cùng một ký hiệu, hai quy ước cho mức lệch khác nhau mười lần, và một công bố không ghi rõ mình dùng quy ước nào thì không dựng lại được. Tham số phân hoạch chỉ là một trong nhiều chỗ mà mô tả trong bài báo có thể không đủ để tái hiện thí nghiệm.

Hệ quả đối với luận văn là một yêu cầu về trình tự: trước khi đo bất cứ thứ gì trên một nền tảng thực nghiệm, phải xác định nền tảng đó thực sự chạy gì. Việc đối chiếu mã nguồn phát hành với mô tả trong bài báo tương ứng vì vậy thuộc về thiết kế đo, và kết quả đối chiếu được báo cáo như đóng góp thứ ba của luận văn.

### 2.4.4. Định vị luận văn

Luận văn xác định biên giới hiệu lực của cơ chế tăng cường dữ liệu bằng mẫu trung bình đại diện kết hợp xấp xỉ hàm mất mát bằng khai triển Taylor bậc nhất. Biên giới hiệu lực ở đây có nghĩa là tập các điều kiện, gồm loại lệch phân phối và lượng thông tin được phép chia sẻ, mà trong đó cơ chế cho cải thiện đo được. Ba đóng góp sau tương ứng với ba khoảng trống vừa trình bày.

Đóng góp thứ nhất là phép đo có kiểm soát đối với số hạng khai triển Taylor. Phép đối chứng giữa FedMix và NaiveMix được thực hiện lại trên FedBR [11] với nhiều hạt giống ngẫu nhiên, báo cáo kèm khoảng tin cậy. Hai nhánh được đo tại cùng một trọng số trộn, đồng thời báo cáo giá trị $\lambda$ tối ưu riêng của từng nhánh để tách phần đóng góp của cơ chế khỏi phần đến từ công sức tinh chỉnh. Luận văn bổ sung cấu hình cô lập chặt mô tả ở mục 2.4.1 và mở rộng toàn bộ phép đối chứng sang chế độ lệch phân phối đặc trưng.

Đóng góp thứ hai là phép đo cơ chế tại nhiều mức độ nghiêm trọng của cả hai loại lệch phân phối, với mức cải thiện được báo cáo dưới dạng đường đặc tuyến theo tham số ngân sách. Đường đặc tuyến ở đây là đồ thị mức cải thiện theo lượng thông tin được phép chia sẻ, thay cho một giá trị đo tại một điểm duy nhất. Cách báo cáo này xuất phát từ đặc điểm của các phương pháp chia sẻ thông tin: mức cải thiện của chúng phụ thuộc vào lượng thông tin được phép chia sẻ, nên một giá trị đo tại một điểm ngân sách không đại diện cho toàn bộ đường cong.

Đóng góp thứ ba là kiểm toán tính tái lập của nền tảng thực nghiệm, gồm danh mục các điểm mã nguồn phát hành không khớp với mô tả trong bài báo tương ứng. Kết luận của phần này được giới hạn ở mức mô tả: mã nguồn cho thấy các thuật toán đối chứng hoạt động dưới mức mà bài báo hàm ý, nhưng luận văn không định lượng mức đóng góp của từng nguyên nhân.

Chương này đã trình bày các hướng tiếp cận ở mức khái niệm, đủ để định vị đối tượng nghiên cứu và phát biểu ba khoảng trống. Chương 3 dựng nền hình thức cho những gì vừa mô tả: ký hiệu đầy đủ của bài toán học liên kết và local SGD, định nghĩa chính quy của phân phối Dirichlet cùng các giá trị nồng độ thực dùng trong luận văn, cách mô hình hoá phân phối góc xoay, và dẫn xuất khai triển Taylor bậc nhất cùng các cấu hình thuật toán sinh ra từ nó.

---

## Tài liệu tham khảo (khối Chương 2 — đã đánh số lại theo mục A1–A2)

> Danh mục liên tục 1–16, đã thêm MOON. So với bản Word: **MOON chèn vào vị trí [7]**, mọi mục từ [7] cũ trở đi dịch lên một đơn vị, nên CCVR chuyển từ [14] sang **[15]**, và [16] FedProto nay có mục thật thay vì trích tới một số không tồn tại. Mục [5] FedProx đã bổ sung nơi công bố và năm theo mục A4.

[1] T. Yoon, S. Shin, S. J. Hwang, E. Yang, "FedMix: Approximation of Mixup under Mean Augmented Federated Learning," *ICLR*, 2021.
[2] B. McMahan, E. Moore, D. Ramage, S. Hampson, B. Agüera y Arcas, "Communication-Efficient Learning of Deep Networks from Decentralized Data," *AISTATS*, PMLR 54:1273–1282, 2017.
[3] Q. Li, Y. Diao, Q. Chen, B. He, "Federated Learning on Non-IID Data Silos: An Experimental Study," *IEEE ICDE*, pp. 965–978, 2022.
[4] T.-M. H. Hsu, H. Qi, M. Brown, "Measuring the Effects of Non-Identical Data Distribution for Federated Visual Classification," arXiv:1909.06335, 2019.
[5] T. Li, A. K. Sahu, M. Zaheer, M. Sanjabi, A. Talwalkar, V. Smith, "Federated Optimization in Heterogeneous Networks," *MLSys*, 2020.
[6] S. P. Karimireddy, S. Kale, M. Mohri, S. J. Reddi, S. U. Stich, A. T. Suresh, "SCAFFOLD: Stochastic Controlled Averaging for Federated Learning," *ICML*, PMLR 119:5132–5143, 2020.
[7] Q. Li, B. He, D. Song, "Model-Contrastive Federated Learning," *CVPR*, pp. 10713–10722, 2021.
[8] Y. Zhao, M. Li, L. Lai, N. Suda, D. Civin, V. Chandra, "Federated Learning with Non-IID Data," arXiv:1806.00582, 2018.
[9] H. Zhang, M. Cisse, Y. N. Dauphin, D. Lopez-Paz, "mixup: Beyond Empirical Risk Minimization," *ICLR*, 2018.
[10] Z. Tang, Y. Zhang, S. Shi, X. He, B. Han, X. Chu, "Virtual Homogeneity Learning: Defending against Data Heterogeneity in Federated Learning," *ICML*, PMLR 162:21111–21132, 2022.
[11] Y. Guo, X. Tang, T. Lin, "FedBR: Improving Federated Learning on Heterogeneous Data via Local Learning Bias Reduction," *ICML*, PMLR 202:12034–12054, 2023.
[12] T. Lin, L. Kong, S. U. Stich, M. Jaggi, "Ensemble Distillation for Robust Model Fusion in Federated Learning," *NeurIPS*, 2020.
[13] G. Lee, M. Jeong, Y. Shin, S. Bae, S.-Y. Yun, "Preservation of the Global Knowledge by Not-True Distillation in Federated Learning," *NeurIPS*, 2022.
[14] Z. Zhu, J. Hong, J. Zhou, "Data-Free Knowledge Distillation for Heterogeneous Federated Learning," *ICML*, 2021.
[15] M. Luo, F. Chen, D. Hu, Y. Zhang, J. Liang, J. Feng, "No Fear of Heterogeneity: Classifier Calibration for Federated Learning with Non-IID Data," *NeurIPS*, 2021.
[16] Y. Tan, G. Long, L. Liu, T. Zhou, Q. Lu, J. Jiang, C. Zhang, "FedProto: Federated Prototype Learning across Heterogeneous Clients," *AAAI*, 36(8):8432–8440, 2022.

---

## Ghi chú thi hành — đọc trước khi chép vào Word

**1. Mục C1 phát biểu lệch so với đơn đặt việc, có chủ ý.** Đơn viết *"Hạ xuống mức đúng: hướng này không trao đổi thêm đại lượng nào ngoài những gì FedAvg đã trao đổi."* Cách nói đó mâu thuẫn với chính mục 2.2.1.2, nơi chương ghi SCAFFOLD làm chi phí truyền thông **tăng gấp đôi** vì phải gửi thêm biến kiểm soát. Bản sửa dùng ranh giới khác: hướng này không chia sẻ dữ liệu và không chia sẻ thống kê mô tả phân phối dữ liệu, còn đại lượng trao đổi thêm thuộc về quá trình tối ưu hoá. Câu nhượng bộ về biến kiểm soát và gradient inversion giữ nguyên theo đúng tinh thần C1.

**2. Mục C6 xử lý bằng cách thu hẹp, không bằng cách thêm hạn định.** Thêm một mệnh đề hạn định nữa sẽ nâng số câu rào của chương lên hai, vượt hạn ngạch AI#4 (đúng một câu mỗi chương). Thay vào đó, phát biểu được thu về một đối tượng kiểm chứng được: *"NIID-Bench không đề xuất cách quy đổi…"*. Đây là phương án (a) của IR#3 bản sửa 22/09, và là phương án được IR#3 ưu tiên. Câu rào duy nhất của chương nằm ở cuối mục 2.4.1.

**3. Một cấu trúc tương phản ngoài danh sách E1 cũng đã sửa.** Câu mở mục định vị luận văn, *"Luận văn không đề xuất thuật toán học liên kết mới, mà xác định…"*, chính là ví dụ mà §7.7 AI#1 nêu đích danh. Nay viết thẳng: *"Luận văn xác định biên giới hiệu lực của cơ chế…"*.

**4. Hai thuật ngữ tự đặt đã được định nghĩa tại chỗ theo AI#7:** "biên giới hiệu lực" và "đường đặc tuyến", cả hai ở mục 2.4.4. Chương 1 hiện vẫn dùng hai cụm này mà chưa định nghĩa; §7.7 ghi nhận đó là việc phải sửa ở Chương 1.

**5. Việc chỉ làm được trong Word, không làm được ở file này:**

- **A6** — cập nhật trường (F9): danh mục bảng đang in *"Bảng 2.1."* không kèm tên, và mục lục còn dòng *"2.3. Tính tái lập trong FL"* đã bị bỏ. Sau khi chép bản này vào, chọn toàn văn bản rồi nhấn F9, chọn cập nhật cả số lẫn nội dung.
- **A7** — danh mục chữ viết tắt: bổ sung tối thiểu SGD, MAFL, one-hot, non-IID, FL, cùng tên các phương pháp xuất hiện trong chương.
- **B1, khổ giấy** — Bảng 2.2 có 6 cột 13 hàng. Nếu tràn khổ dọc thì xoay ngang trang hoặc hạ cỡ chữ trong bảng; không cắt bớt hàng.

**6. Cột *Chế độ lệch đã đo* đã tra xong, 22/09.** Nguồn là bản toàn văn của từng công trình, không lấy qua bài thứ cấp. Bảng truy vết dưới đây để hội đồng kiểm lại; **không chép vào luận văn**.

| Hàng | Phân hoạch mà công trình gốc thực sự dùng | Kết luận |
|---|---|---|
| FedProx [5] | MNIST và FEMNIST: mỗi thiết bị chỉ có hai chữ số, số mẫu theo luật luỹ thừa. Shakespeare tách theo vai diễn, Sent140 tách theo tài khoản | nhãn, số lượng; tự nhiên |
| SCAFFOLD [6] | EMNIST: cấp cho mỗi client $s\%$ dữ liệu i.i.d., phần còn lại sắp theo nhãn rồi chia; thêm dữ liệu mô phỏng | nhãn |
| MOON [7] | CIFAR-10, CIFAR-100, Tiny-ImageNet: $p_k \sim \mathrm{Dir}_N(\beta)$ trên nhãn | nhãn |
| Zhao và cộng sự [8] | MNIST, CIFAR-10, KWS: sắp theo nhãn rồi chia, cấu hình 1 lớp và 2 lớp mỗi client | nhãn |
| FedMix, NaiveMix [1] | CIFAR-10 hai lớp mỗi client; CIFAR-100 hai mươi lớp mỗi client; Dirichlet $\alpha = 0{,}2$ và $0{,}5$ ở phụ lục J; FEMNIST tách theo người viết; Shakespeare tách theo vai diễn | nhãn, số lượng; tự nhiên |
| VHL [10] | CIFAR-10, FMNIST, SVHN, CIFAR-100: LDA $\alpha = 0{,}1$ và $0{,}05$; thêm cấu hình 2 lớp và cấu hình một lớp trội | nhãn |
| FedDF [12] | CIFAR-10, CIFAR-100, ImageNet thu nhỏ, AG News, SST-2: Dirichlet trên nhãn; thêm không đồng nhất về kiến trúc mô hình | nhãn |
| FedNTD [13] | MNIST, CIFAR-10, CIFAR-100, CINIC-10: sắp theo nhãn rồi chia mảnh, và LDA | nhãn, số lượng |
| FedGen [14] | MNIST, EMNIST: Dirichlet trên nhãn. CelebA gộp ảnh theo từng người vào các nhóm rời nhau | nhãn; tự nhiên |
| CCVR [15] | CIFAR-10, CIFAR-100, CINIC-10: Dirichlet $\alpha = 0{,}5$, $0{,}1$, $0{,}05$ trên nhãn | nhãn |
| FedProto [16] | MNIST, FEMNIST, CIFAR-10: khung $n$-way $k$-shot, thay đổi $n$ và $k$ giữa các client kèm nhiễu; thêm không đồng nhất về kiến trúc | nhãn, số lượng |
| FedBR [11] | RotatedMNIST với mười góc xoay; CIFAR-10 mỗi client xoay một góc riêng; PACS chia theo miền; CIFAR-10 và CIFAR-100 với LDA $\alpha = 0{,}1$ | **nhãn, đặc trưng** |

⚠️ **Một phát hiện làm thay đổi cách phát biểu khoảng trống.** FedMix **có** chạy trên FEMNIST, mà Bảng 2.1 xếp phân hoạch theo người viết vào nhóm lệch phân phối đặc trưng. Câu khoảng trống ở bản trước — *"chưa có công trình nào thực hiện nó dưới lệch phân phối đặc trưng"* — vì vậy sai, và một phản biện mở bài báo FedMix ra là bắt được. Mục 2.4.1 nay thừa nhận FEMNIST tường minh, chỉ ra rằng phân hoạch ấy trộn cả ba loại lệch, rồi thu phát biểu về **"lệch phân phối đặc trưng được tách riêng khỏi lệch nhãn"**. Phát biểu sau hẹp hơn nhưng đúng, và vẫn đủ để chống đỡ đóng góp của luận văn.

**7. Cột *Cần nhãn?* của FedGen đã điền:** có, bộ sinh được huấn luyện có điều kiện theo nhãn và lấy mẫu theo phân phối nhãn ước lượng.

---

# YÊU CẦU SỬA — 24/09/2026 · kết quả trên nền tảng Flower là kết quả của luận văn

> **Căn cứ:** quyết định 24/09, ghi ở `00_outline.md` §1.5 và khối cùng ngày cuối `01_chuong1.md`. Luận văn nay có hai nền tảng thực nghiệm: Flower cho lệch nhãn, FedBR cho lệch đặc trưng. Ch.2 có hai câu nói FedBR là nền tảng của **toàn bộ** thực nghiệm, nên phải sửa. Cột *Trước* chép nguyên văn từ Word ngày 24/09. Chỉ-append.

| # | Mục | Tìm trong Word | Trước | Sau | Lý do |
|---|---|---|---|---|---|
| 1 | 2.2.2, đoạn dẫn trước 2.2.2.1 | `công trình được luận văn dùng làm nền tảng thực nghiệm` | …nhánh cuối cùng trình bày FedBR, công trình được luận văn dùng làm nền tảng thực nghiệm. | …nhánh cuối cùng trình bày FedBR, công trình mà mã nguồn của nó được luận văn dùng làm nền tảng thực nghiệm cho phần lệch phân phối đặc trưng. | Không còn là nền tảng duy nhất |
| 2 | 2.2.2.6 FedBR, câu đầu | `nó là nền tảng thực nghiệm mà toàn bộ thí nghiệm mới` | FedBR [11] giữ một vai trò đặc biệt trong luận văn: nó là nền tảng thực nghiệm mà toàn bộ thí nghiệm mới được chạy trên đó. | FedBR [11] giữ một vai trò đặc biệt trong luận văn: mã nguồn của nó là nền tảng cho toàn bộ các thực nghiệm dưới lệch phân phối đặc trưng. | Như trên; các thực nghiệm lệch nhãn chạy trên nền tảng Flower |
| 3 | 2.4.4, đoạn "Đóng góp thứ ba" — **chỉ làm nếu học viên duyệt hàng 3 của Ch.1** | `Đóng góp thứ ba là kiểm toán tính tái lập` | Đóng góp thứ ba là kiểm toán tính tái lập của nền tảng thực nghiệm, gồm danh mục các điểm mã nguồn phát hành không khớp với mô tả trong bài báo tương ứng. Kết luận của phần này… *(giữ nguyên phần sau)* | Đóng góp thứ ba là kiểm tra tính tái lập trên cả hai nền tảng thực nghiệm: đo lại FedMix và nhóm hiệu chuẩn tầng phân lớp dưới lệch phân phối nhãn trên nền tảng Flower, và lập danh mục các điểm mã nguồn FedBR phát hành không khớp với mô tả trong bài báo tương ứng. Kết luận của phần này… *(giữ nguyên phần sau)* | Giữ Ch.1 và Ch.2 nói cùng một điều về đóng góp thứ ba |

Không chỗ nào khác của Ch.2 trong Word nhắc tới bài hội nghị hay kết quả nền, nên không cần sửa thêm.

⚠️ **Việc cũ còn treo trong Word Ch.2**, ghi lại để không rơi (chi tiết ở *Ghi chú thi hành* cuối `04_chuong4.md`, mục 3):
- mục 2.4.1: *"mẫu trung bình vẫn tham gia lượt truyền xuôi như ở FedMix"* sai;
- mục 2.4.3: trích NIID-Bench là [8], số đúng là [3];
- mục 2.4.4: còn *"hai khoảng trống"* và trỏ *"mục 2.3.1"*;
- mục 2.2.1.3: MOON mang số [6], trùng với SCAFFOLD.
