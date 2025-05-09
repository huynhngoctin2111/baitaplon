# LandPro Scraper - Tự động thu thập dữ liệu nhà đất

Dự án này sử dụng Python và Selenium để **tự động truy cập trang [https://landpro.vn](https://landpro.vn)**, lọc dữ liệu theo tỉnh và loại nhà đất, thu thập tất cả thông tin bài đăng (tiêu đề, mô tả, địa chỉ, diện tích, giá), lưu vào file `.csv`, và **tự động chạy mỗi sáng lúc 6:00**.

---

## Chức năng chính

- Truy cập website [landpro.vn](https://landpro.vn)
- Chọn tỉnh/thành và loại nhà đất
- Thu thập dữ liệu bài đăng ở nhiều trang
- Lưu dữ liệu vào file CSV (`data/landpro_data.csv`)
- Tự động chạy vào **6:00 sáng hàng ngày**

---

## Yêu cầu cài đặt

### 1. Cài Python

Tải và cài đặt Python 3.8+ tại: https://www.python.org/downloads/

---

### 2. Cài thư viện cần thiết

Tạo virtual environment (tuỳ chọn):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
