# GO_Intern

## Hướng dẫn cài đặt và khởi chạy

Tham khảo ứng dụng fullstack được cài đặt trong docker qua repo: https://github.com/frwkHoangQuy/GO_Docker/tree/main

### 1. Clone code từ GitHub
Sử dụng lệnh sau để clone code về máy:

```bash
git clone https://github.com/frwkHoangQuy/GO_Intern
```


### 2. Cài đặt các gói cần thiết
Sau khi clone code về, cài đặt các gói cần thiết bằng cách sử dụng pip với file requirements.txt:

```bash
pip install -r requirements.txt
```
### 3. Tạo và kết nối cơ sở dữ liệu (Database)
Bước 1: Tạo cơ sở dữ liệu MySQL
Tạo một cơ sở dữ liệu MySQL mới với tên tùy chọn (ví dụ: webdev_intern).

Bước 2: Cấu hình file config.ini
Trong thư mục gốc của dự án, tạo một file config.ini và điền thông tin kết nối cơ sở dữ liệu với nội dung sau:

```ini
[mysql]
host = <địa chỉ host của database>
user = <tên người dùng MySQL>
password = <mật khẩu MySQL>
database = <tên cơ sở dữ liệu>
port = <cổng MySQL>
```
- host: Địa chỉ của máy chủ MySQL (ví dụ: localhost hoặc một địa chỉ IP cụ thể).
- user: Tên người dùng MySQL (ví dụ: root).
- password: Mật khẩu của tài khoản MySQL.
- database: Tên cơ sở dữ liệu đã tạo ở Bước 1.
- port: Cổng MySQL (mặc định là 3306).

Bước 3: Áp dụng migration
Sau khi cấu hình xong file config.ini, chạy lệnh sau để áp dụng migration và kết nối với cơ sở dữ liệu:
```bash
py manage.py migrate
```
### 4. Import dữ liệu từ CSV vào Database
Để import dữ liệu từ file CSV vào cơ sở dữ liệu, thực hiện các bước sau:

Mở Django shell bằng lệnh:
```bash
py manage.py shell
```
Trong shell vừa mở, chạy đoạn mã Python trong file script/csv_to_database.py để import dữ liệu từ CSV vào cơ sở dữ liệu.

### 5. Khởi động hệ thống
Sau khi hoàn tất các bước trên, khởi chạy hệ thống bằng lệnh:
```bash
py manage.py runserver
```
