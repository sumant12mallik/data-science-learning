import pandas as pd

df = pd.read_csv("house-price.csv")
print(df.head)
print(df.columns)
print(df.info())
print(df["price"].mean())
print(df["price"].max())
print(df["price"].min())

print(df[["price", "area", "bedrooms", "bathrooms"]].head())

print(df.groupby("bedrooms")["price"].mean())

report = df.groupby("bedrooms")["price"].mean()

for beds, avg_price in report.items():
    print(beds, "bedroom house avg price =", int(avg_price))