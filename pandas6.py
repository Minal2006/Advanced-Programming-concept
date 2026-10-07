import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 90, 80, 100],
    "Classes_Attended": [80, 70, 85, 50, 95]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])