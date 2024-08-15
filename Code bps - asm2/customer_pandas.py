import pandas as pd

# 1. Đọc tệp CSV
file_path = 'customer_table.csv'
data = pd.read_csv(file_path)

# 2. Hiển thị 5 dòng đầu tiên để kiểm tra dữ liệu
print("Dữ liệu ban đầu:")
print(data.head())

# 3. Xử lý dữ liệu trống
# Kiểm tra số lượng giá trị trống trong mỗi cột
print("\nSố lượng giá trị trống trong mỗi cột trước khi xử lý:")
print(data.isnull().sum())

# Cách 1: Xóa các hàng chứa giá trị trống
data_cleaned = data.dropna()

# Hoặc cách 2: Điền giá trị mặc định cho các giá trị trống (tuỳ chọn)
# data_cleaned = data.fillna({'CustomerPhone': 'Unknown'})

# Kiểm tra lại dữ liệu sau khi xử lý giá trị trống
print("\nSố lượng giá trị trống trong mỗi cột sau khi xử lý:")
print(data_cleaned.isnull().sum())

# 4. Xử lý dữ liệu lỗi
# Ví dụ: Kiểm tra và sửa các số điện thoại không hợp lệ
# Xác định các số điện thoại không khớp với định dạng thông thường
invalid_phone_numbers = data_cleaned[~data_cleaned['CustomerPhone'].str.match(r'^\+?\d{1,4}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$')]

print("\nCác số điện thoại không hợp lệ:")
print(invalid_phone_numbers)

# Sửa chữa số điện thoại bằng cách loại bỏ các ký tự không phải số (chỉ giữ lại các số và dấu + nếu có)
data_cleaned['CustomerPhone'] = data_cleaned['CustomerPhone'].str.replace(r'[^\d+]', '', regex=True)

# Kiểm tra lại sau khi sửa
print("\nSố điện thoại sau khi chuẩn hóa:")
print(data_cleaned['CustomerPhone'].head())

# 5. Biến đổi dữ liệu
# Chuẩn hóa địa chỉ bằng cách thay thế ký tự xuống dòng '\n' bằng dấu phẩy ', '
data_cleaned['CustomerAddress'] = data_cleaned['CustomerAddress'].str.replace(r'\n', ', ', regex=True)

# Tạo cột mới 'MarketCategory' dựa trên giá trị của 'MarketTrendID'
data_cleaned['MarketCategory'] = data_cleaned['MarketTrendID'].apply(lambda x: 'High' if x > 5 else 'Low')

print("\nDữ liệu sau khi làm sạch và biến đổi:")
print(data_cleaned.head())

# 6. Lưu dữ liệu đã làm sạch
data_cleaned.to_csv('cleaned_customer_table.csv', index=False)
print("\nDữ liệu đã được làm sạch và lưu vào 'cleaned_customer_table.csv'")
