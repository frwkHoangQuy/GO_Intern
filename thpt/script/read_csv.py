import pandas as pd

chunksize = 10 ** 6

column_names = None
sample_data = None

# Đọc từng phần của file CSV
for chunk in pd.read_csv('dataset/diem_thi_thpt_2024.csv', chunksize=chunksize):
    if column_names is None:
        column_names = chunk.columns
        sample_data = chunk.head()
        break

print("Các cột trong file CSV là:")
print(column_names)
print("\nMẫu dữ liệu:")
print(sample_data)
