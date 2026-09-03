#Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.
# Create attendance file
file = open("attendance.txt", "w")

file.write("101,Amit,70,100\n")
file.write("102,Priya,85,100\n")
file.write("103,Rahul,60,100\n")
file.write("104,Neha,90,100\n")

file.close()


file = open("attendance.txt", "r")

students = []

for line in file:
    data = line.strip().split(",")

    roll_no = data[0]
    name = data[1]
    present = int(data[2])
    total = int(data[3])

    percentage = (present / total) * 100

    students.append([roll_no, name, percentage])

file.close()



print("Student Attendance:")

for student in students:
    print("Roll No:", student[0],
          "Name:", student[1],
          "Attendance:", student[2], "%")



print("\nStudents having attendance below 75%:")

for student in students:
    if student[2] < 75:
        print("Roll No:", student[0],
              "Name:", student[1],
              "Attendance:", student[2], "%")