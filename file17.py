


file = open("student.txt", "w")

file.write("RollNo,Name,Marks\n")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")

file.close()


file = open("student.txt", "r")

students = []

next(file)  

for line in file:
    data = line.strip().split(",")

    roll_no = data[0]
    name = data[1]
    marks = int(data[2])

    students.append([roll_no, name, marks])

file.close()


print("All Student Records:")

for student in students:
    print("Roll No:", student[0],
          "Name:", student[1],
          "Marks:", student[2])



highest = students[0]

for student in students:
    if student[2] > highest[2]:
        highest = student

print("\nStudent with Highest Marks:")
print("Roll No:", highest[0])
print("Name:", highest[1])
print("Marks:", highest[2])



total = 0

for student in students:
    total = total + student[2]

average = total / len(students)

print("\nAverage Marks:", average)



print("\nStudents who scored more than 80:")

for student in students:
    if student[2] > 80:
        print("Roll No:", student[0],
              "Name:", student[1],
              "Marks:", student[2])