import pandas as pd

df = pd.read_csv("/usercode/data/sales_data.csv")
df["date"] = df["date"].apply(
    lambda date: pd.to_datetime(date, errors="coerce")
)

print("\nAccuracy Check")
negative_prices = (df["price"] < 0).sum()
print(f"Negative Prices: {negative_prices}")

current_date = pd.Timestamp.now()
future_dates = (df["date"] > current_date).sum()
print(f"Number of Future Dates: {future_dates}")

print("\nConsistency Check")
unique_products = df["product"].unique()
print(f"Unique products: {unique_products}")

unique_count = df["product"].nunique()
print(f"Count of unique products: {unique_count}")

print("\nCompleteness Check")
missing_values = df.isnull().sum()
print(f"Missing Values: {missing_values}")

completeness_rate = df.notnull().mean().mean() * 100
print(f"Overall completeness rate: {completeness_rate:.1f}%")

assert (df["price"] >= 0).all(), "Negative product prices found!"
