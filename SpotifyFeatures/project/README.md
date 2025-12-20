Spotify Audio Features Analysis Dashboard
1. Giới thiệu 
Dashboard này được xây dựng nhằm trực quan hóa và minh họa kết quả phân tích dữ liệu âm nhạc Spotify, phục vụ cho đề tài môn học Phân tích dữ liệu.
Ứng dụng tập trung vào:
    Phân tích dặc trưng âm thanh 
    So sánh mức độ phổ biến của bài hát
    Minh họa kết quả Phân tích mô tả (EDA) và Phân tích nâng cao (Clustering & Classification) một cách trực quan, dễ hiểu và có tính ứng dụng
Dashboard được phát triển bằng Streamlit, cho phép người dùng tương tác trực tiếp với dữ liệu mà không cần kến thức lập trình sâu.

2. Dữ liệu sử dụng 
Tên file: spotify_processed.csv
Nguồn gốc: Kaggle – Spotify Audio Features Dataset
Mô tả dữ liệu:
    Các thuộc tính âm thanh do Spotify Web API cung cấp như:
        danceability, energy, loudness, acousticness, instrumentalness, valence, tempo, …
    Biến mục tiêu:
        popularity (0–100)
        is_popular (nhãn phân loại: phổ biến / không phổ biến)
Nhãn phân cụm:
    cluster (tạo từ K-Means)
Dữ liệu đã được làm sạch, chuẩn hóa và xử lý trước trong notebook phân tích.

3. Chức năng chính của Dashboard 
Dashboard gồm các phần chính sau:
    Tổng quan dữ liệu
        Hiển thị số lượng bài hát, số lượng thể loại
        Xem nhanh cấu trúc dữ liệu

    Phân tích đặc trưng âm thanh (EDA)
        Phân phối các thuộc tính âm thanh
        So sánh đặc trưng giữa các mức độ phổ biến
        Phân tích tương quan giữa các thuộc tính

    Phân cụm âm nhạc (Clustering)
        Trực quan hóa các nhóm âm nhạc tự nhiên (K-Means)
        So sánh hồ sơ đặc trưng của từng cụm

    Dự đoán mức độ phổ biến (Classification)
        Minh họa kết quả Logistic Regression & Random Forest
        Hiển thị Confusion Matrix
        Phân tích các yếu tố ảnh hưởng mạnh đến độ phổ biến

4. Cấu trúc thư mục 
project/
│
├── app.py                 # File chính chạy dashboard Streamlit
├── spotify_processed.csv  # Dữ liệu đã xử lý
└── requirements.txt       # Danh sách thư viện cần cài đặt 

5. Cài đặt và chạy ứng dụng 
Bước 1: Cài đặt môi trường
    pip install -r requirements.txt
Bước 2: Chạy dashboard 
    streamlit run app.py
Sau đó mở trình duyệt tài địa chỉ:
    http://localhost:8501

6. Công nghệ sử dụng 
Python 3
Streamlit – xây dựng dashboard
Pandas, NumPy – xử lý dữ liệu
Matplotlib, Seaborn – trực quan hóa
Scikit-learn – mô hình phân cụm & phân loại

7. Ý nghĩa học thuật & thực tiễn 
Minh họa trực quan cho các câu hỏi nghiên cứu (RQ1–RQ5) trong báo cáo
Giúp người xem dễ hiểu hơn:
    Vì sao một bài hát trở nên phổ biến
    Các nhóm âm nhạc hình thành dựa trên đặc trưng âm thanh
Có thể mở rộng thành:
    Hệ thống gợi ý âm nhạc
    Công cụ hỗ trợ nghệ sĩ/nhà sản xuất phân tích xu hướng

8. Hạn chế & hướng mở rộng 
Dashboard hiện tại mang tính minh họa phân tích, chưa tối ưu cho dự đoán thời gian thực
Có thể mở rộng thêm:
    Bộ lọc theo thể loại, cluster
    Phân tích theo thời gian (nếu có dữ liệu năm)
    Tích hợp playlist hoặc dữ liệu người dùng