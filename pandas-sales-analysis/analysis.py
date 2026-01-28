import pandas as pd

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [20, 0, 45, 30, 60]
}

df = pd.DataFrame(data)

print(df)

print("sum is :   ",df["Sales"].sum())
print("mean is :  ",df["Sales"].mean())
print("minimum is :  ",df["Sales"].min())
print("zero count is :  ",(df["Sales"] == 0).sum())
print("\nHigh Sales Days (>30):")
print(df[df["Sales"] > 30])