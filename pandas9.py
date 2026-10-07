import pandas as pd

salary = {
    "Amit": 45000,
    "Sneha": 60000,
    "Rahul": 75000,
    "Priya": 52000,
    "Neha": 80000
}

series = pd.Series(salary)

print("Employee Salaries:")
print(series)

print("\nHighest Salary:")
print(series.max())

print("\nLowest Salary:")
print(series.min())

print("\nAverage Salary:")
print(series.mean())

print("\nEmployees earning more than 50000:")
print(series[series > 50000])