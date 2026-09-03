from student1.details import student_details
from student1.marks import student_marks
from faculty.details import faculty_details

# Student information
name, roll_no, branch = student_details()
total, percentage = student_marks()

# Faculty information
faculty_name, faculty_id, department = faculty_details()

print("========== STUDENT INFORMATION ==========")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Branch     :", branch)
print("Total Marks:", total)
print("Percentage :", percentage)

print("\n========== FACULTY INFORMATION ==========")
print("Name       :", faculty_name)
print("Faculty ID :", faculty_id)
print("Department :", department)