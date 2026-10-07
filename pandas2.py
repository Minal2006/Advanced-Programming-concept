import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Department": ["CSE", "IT", "CSE", "HR", "IT"],
    "Salary": [45000, 60000, 75000, 52000, 80000],
    "Experience": [2, 5, 7, 4, 8]
}

df = pd.DataFrame(data)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])