import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


sales_data = pd.read_csv('cleaned_sale_table.csv')

sales_data['SaleDate'] = pd.to_datetime(sales_data['SaleDate'])

sales_data = sales_data.sort_values('SaleDate')

sales_data['Year'] = sales_data['SaleDate'].dt.year
sales_data['Month'] = sales_data['SaleDate'].dt.month

X = sales_data[['Year', 'Month']]  
y = sales_data['TotalPrice']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

future_dates = pd.DataFrame({
    'Year': [2024, 2024, 2024, 2024],
    'Month': [1, 2, 3, 4]  
})
future_sales_forecast = model.predict(future_dates)

plt.figure(figsize=(14, 7))
plt.plot(sales_data['SaleDate'], y, label='Actual Sales', marker='o', color='blue')
plt.plot(sales_data['SaleDate'], model.predict(X), label='Predicted Sales', color='green')
plt.scatter(future_dates.apply(lambda x: pd.Timestamp(x['Year'], x['Month'], 1), axis=1), future_sales_forecast, label='Forecasted Sales', color='red')
plt.title('Sales Forecasting')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
plt.grid(True)
plt.show()
