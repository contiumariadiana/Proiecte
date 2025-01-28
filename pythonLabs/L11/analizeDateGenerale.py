import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

num_days = 60

daily_sales = []

for day in range(num_days):

    num_products = np.random.randint(5, 20)

    prices = np.random.normal(loc=40, scale=8, size=num_products)
    prices = np.clip(prices, 10, None)

    quantities = np.random.randint(1, 11, size=num_products)

    promo_mask = np.random.rand(num_products) < 0.3
    discounted_prices = prices.copy()
    discounted_prices[promo_mask] *= 0.8

    sales_per_product = discounted_prices * quantities

    total_sales = np.sum(sales_per_product)

    total_profit = total_sales * 0.3

    daily_sales.append(
        [day + 1, num_products, total_sales, total_profit, np.mean(discounted_prices), np.mean(quantities),
         promo_mask.sum()])

df = pd.DataFrame(daily_sales,
                  columns=["Day", "Num_Products", "Total_Sales", "Total_Profit", "Avg_Price", "Avg_Quantity",
                           "Num_Promotions"])

stats = {
    "Average Price": df["Avg_Price"].mean(),
    "Max Price": df["Avg_Price"].max(),
    "Min Price": df["Avg_Price"].min(),
    "Average Quantity": df["Avg_Quantity"].mean(),
    "Max Quantity": df["Avg_Quantity"].max(),
    "Min Quantity": df["Avg_Quantity"].min(),
    "Average Profit": df["Total_Profit"].mean(),
    "Max Profit": df["Total_Profit"].max(),
    "Min Profit": df["Total_Profit"].min(),
    "Total Sales (60 days)": df["Total_Sales"].sum(),
    "Total Profit (60 days)": df["Total_Profit"].sum()
}
plt.figure(figsize=(12, 6))
plt.plot(df["Day"], df["Total_Sales"], label="Total Sales", marker="o")
plt.plot(df["Day"], df["Total_Profit"], label="Total Profit", marker="s")
plt.xlabel("Day")
plt.ylabel("Amount")
plt.title("Evolution of Sales and Profit Over 60 Days")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(df["Avg_Price"], bins=15, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel("Average Price")
plt.ylabel("Frequency")
plt.title("Distribution of Prices Over 60 Days")
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(df["Avg_Quantity"], bins=10, color='green', alpha=0.7, edgecolor='black')
plt.xlabel("Average Quantity")
plt.ylabel("Frequency")
plt.title("Distribution of Quantities Sold Over 60 Days")
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(df["Day"], df["Num_Promotions"], color='red', alpha=0.7)
plt.xlabel("Day")
plt.ylabel("Number of Promotions")
plt.title("Number of Promotions Applied Each Day")
plt.grid()
plt.show()

print(df.head())

for key, value in stats.items():
    print(f"{key}: {value:.2f}")