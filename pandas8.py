import pandas as pd

marks = {
    "Amit": 80,
    "Sneha": 70,
    "Rahul": 90,
    "Priya": 85,
    "Neha": 60
}

series = pd.Series(marks)

print("Student Marks:")
print(series)

print("\nMarks of Rahul:")
print(series["Rahul"])

print("\nMaximum Marks:")
print(series.max())

print("\nMinimum Marks:")
print(series.min())

print("\nAverage Marks:")
print(series.mean())

print("\nStudents scoring more than 75:")
print(series[series > 75])