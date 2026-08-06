students = ["Amit", "Neha", "Aditi", "Priya"]
print("Total Students:", len(students))
name = input("Enter student name: ")
if name in students:
    print("Student is present")
else:
    print("Student is absent")
new = input("Enter new student name: ")
students.append(new)
print("After adding:", students)
remove = input("Enter absent student name: ")
students.remove(remove)
print("After removing:", students)