import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Chuẩn bị Dữ liệu
# Đọc dữ liệu từ các tệp CSV đã được cung cấp
sale_data = pd.read_csv('cleaned_sale_table.csv')
product_detail_data = pd.read_csv('cleaned_product_detail_table.csv')

# Thêm cột 'Month' từ cột 'SaleDate'
sale_data['SaleDate'] = pd.to_datetime(sale_data['SaleDate'])
sale_data['Month'] = sale_data['SaleDate'].dt.month

# Kết hợp dữ liệu từ sale_data và product_detail_data dựa trên ProductDetailID
merged_data = pd.merge(sale_data, product_detail_data, on='ProductDetailID')

# Chọn các đặc trưng (features) và mục tiêu (target)
X = merged_data[['Price', 'Month']]  # Chọn các đặc trưng
y = merged_data['TotalPrice']  # Mục tiêu cần dự đoán (doanh số)

# 2. Tách Dữ liệu Thành Tập Huấn luyện và Tập Kiểm tra
# Tách dữ liệu thành tập huấn luyện (80%) và tập kiểm tra (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Xây dựng và Huấn luyện Mô hình Hồi quy tuyến tính
# Khởi tạo mô hình hồi quy tuyến tính
model = LinearRegression()

model.fit(X_train, y_train)

# 4. Dự đoán Doanh số và Đánh giá Mô hình
# Sử dụng mô hình để dự đoán doanh số trên tập kiểm tra
y_pred = model.predict(X_test)

# Tính toán Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Tính toán R-squared (R²)
r2 = r2_score(y_test, y_pred)
print(f'R-squared: {r2}')

# 5. Tạo biểu đồ so sánh giữa giá trị dự đoán và giá trị thực tế
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Actual Sales', marker='o')
plt.plot(y_pred, label='Predicted Sales', marker='x')
plt.title('Actual vs Predicted Sales')
plt.xlabel('Test Samples')
plt.ylabel('Total Sales')
plt.legend()
plt.grid(True)
plt.show()

# 6. Dự đoán Doanh số cho Dữ liệu Mới (nếu có)
# Ví dụ: Dự đoán doanh số cho dữ liệu mới
new_data = pd.DataFrame({'Price': [300], 'Month': [7]})
predicted_sales = model.predict(new_data)
print(f'Predicted Sales for new data: {predicted_sales[0]}')
