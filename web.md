1. Hàm plt.subplot là gì ?
- Tưởng tượng có một tờ giấy NxM
- Một subplot là một cell trong đó
- index các cell sẽ bắt đầu từ 1
- hàm subplot là chọn chỗ để vẽ
- Và subplot chính là trả về ax
    - chúng ta có thể sử dụng ax[0][0] để truy cập ô đầu tiên
    - figsize khai báo chiều dài chiều rộng bằng đơn vị in
2. Hàm ax.pie, ax.axis là gì ?
- Nói chung ta tưởng tượng fig chính là một cái khung tranh và ta đặt lên nó một tờ giấy chính là ax
- Bước tiếp theo ta sẽ vẽ cái gì thú vị lên tờ giấy này
- ax.axis("equal") chính là giữ cho tỉ lệ trục x và y bằng nhau -> Làm cho hình tròn nó tròn trịa
- ax.pie chính là vẽ một hình tròn lên tờ giấy, startangle = 90 chính là căn miếng đầu tiên ở hướng 12h, nếu không có nó thì mặc đỉnh ở hướng 3h. Hay nói cách khác là quay ngược chiều kim đồng hồ đi 90 độ

3. Ý nghĩa của %1.1f%% ?
- Đây chính là kiến thức liên quan đến string formatting của c
- Chữ f báo là số đưa vào là số float
- 1 có nghĩa là độ rộng tối thiểu
- .1 chính là số lượng số sau dấu thập phân

4. st.pyplot(fig)?
- Theo như ở trên chính là đưa khung tranh lên web
5. st.markdown()? 
- Hiển thị văn bản bằng ngôn ngữ markdown lên web
6. Thư viện io và Image là gì ?
- PIL hay là Python Image Library. Thư viện dùng xử lí hình ảnh
- io là bộ nhớ đệm thông minh biến hình ảnh từ đĩa cứng ra bộ nhớ
- Thường là ảnh phải lấy từ đĩa cứng ra, còn io.BytesIO() là tạo một file ảo trong ram -> Tốc độ nhanh -> Không rác ổ cứng
- io là đường ống để đưa dữ liệu sang PIL
7. buf.seek(0) ?
- Tưởng tượng cuộn bằng cát sét, lệnh này là đưa đầu đọc về vị trí bắt đầu
