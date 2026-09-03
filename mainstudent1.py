# main.py

from studentrecord.marks import total_marks, percentage
from studentrecord.grade import calculate_grade
from studentrecord.attendance import attendance_percentage, eligibility

name = input("Enter student name: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

present = int(input("Enter classes attended: "))
total_classes = int(input("Enter total classes: "))

marks = [m1, m2, m3]

# Calculate marks
total = total_marks(marks)
per = percentage(marks)

# Calculate grade
grade = calculate_grade(per)

# Calculate attendance
att_per = attendance_percentage(present, total_classes)
status = eligibility(att_per)

# Display report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", per, "%")
print("Grade:", grade)
print("Attendance:", att_per, "%")
print("Attendance Status:", status)