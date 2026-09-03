
import student
name = input("Enter student name: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

marks = [m1, m2, m3]


total = student.total_marks(marks)
per = student.percentage(marks)
gr = student.grade(per)


print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", per, "%")
print("Grade:", gr)