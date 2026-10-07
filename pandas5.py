import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Product": ["Laptop", "Mobile", "Tablet", "Printer", "Monitor"],
    "Quantity": [2, 3, 2, 5, 4],
    "Price": [50000, 25000, 30000, 10000, 15000],
    "Discount": [5000, 2000, 3000, 1000, 2000]
}

df = pd.DataFrame(data)

df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage order value:")
print(df["Final_Amount"].mean())