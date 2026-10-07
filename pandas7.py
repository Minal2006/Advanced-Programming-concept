import pandas as pd

data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 25000, 1500, 12000, 10000],
    "Quantity": [2, 4, 10, 3, 2]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:")
print(df["Total_Sales"].mean())