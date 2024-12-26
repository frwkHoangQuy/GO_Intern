import pandas as pd

# Sử dụng chunksize để đọc file CSV theo từng phần nhỏ
chunksize = 10 ** 6

# Tạo một DataFrame rỗng để lưu trữ tên cột và một mẫu dữ liệu
column_names = None
sample_data = None

# Đọc từng phần của file CSV
for chunk in pd.read_csv('../../dataset/diem_thi_thpt_2024.csv', chunksize=chunksize):
    if column_names is None:
        column_names = chunk.columns
        sample_data = chunk.head()  # Lấy một vài dòng đầu tiên làm mẫu dữ liệu
        break

print("Các cột trong file CSV là:")
print(column_names)
print("\nMẫu dữ liệu:")
print(sample_data)
