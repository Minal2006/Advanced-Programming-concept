import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Python": [80, 70, 90, 85, 60],
    "DBMS": [75, 80, 88, 90, 65],
    "Mathematics": [85, 75, 92, 80, 70]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average:")
print(df)

print("\nStudents with average more than 75:")
print(df[df["Average"] > 75])