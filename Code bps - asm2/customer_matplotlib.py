import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu đã được làm sạch từ các tệp CSV
customer_data = pd.read_csv('cleaned_customer_table.csv')
market_trend_data = pd.read_csv('cleaned_market_trend_table.csv')
product_detail_data = pd.read_csv('cleaned_product_detail_table.csv')
product_group_data = pd.read_csv('cleaned_product_group_table.csv')
sale_data = pd.read_csv('cleaned_sale_table.csv')
website_access_category_data = pd.read_csv('cleaned_website_access_category_table.csv')

# 1. Tạo biểu đồ cột (Bar Chart) để so sánh số lượng khách hàng theo MarketTrendID
market_counts = customer_data['MarketTrendID'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(market_counts.index, market_counts.values, color='skyblue')
plt.title('Number of Customers by Market Category (MarketTrendID)', fontsize=16)
plt.xlabel('Market Category (MarketTrendID)', fontsize=14)
plt.ylabel('Number of Customers', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Tạo biểu đồ đường (Line Chart) để hiển thị xu hướng doanh thu theo thời gian
sale_data['SaleDate'] = pd.to_datetime(sale_data['SaleDate'])
daily_sales = sale_data.groupby('SaleDate')['TotalPrice'].sum()

plt.figure(figsize=(12, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', color='blue')
plt.title('Sales Trend Over Time', fontsize=16)
plt.xlabel('Sale Date', fontsize=14)
plt.ylabel('Total Sales', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Tạo biểu đồ tròn (Pie Chart) để hiển thị tỷ lệ phần trăm khách hàng theo MarketTrendID
plt.figure(figsize=(8, 8))
plt.pie(market_counts, labels=market_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Percentage of Customers by Market Category (MarketTrendID)', fontsize=16)
plt.tight_layout()
plt.show()

# 4. Tạo biểu đồ histogram để phân tích phân phối của TotalPrice trong sale_data
plt.figure(figsize=(10, 6))
plt.hist(sale_data['TotalPrice'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Total Sales (TotalPrice)', fontsize=16)
plt.xlabel('Total Price', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.tight_layout()
plt.show()

# 5. Tạo biểu đồ cột để so sánh số lượng sản phẩm theo nhóm sản phẩm (ProductGroupID) trong product_detail_data
product_group_counts = product_detail_data['ProductGroupID'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(product_group_counts.index, product_group_counts.values, color='orange')
plt.title('Number of Products by Product Group (ProductGroupID)', fontsize=16)
plt.xlabel('Product Group (ProductGroupID)', fontsize=14)
plt.ylabel('Number of Products', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()