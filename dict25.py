students = {
    "Prathamesh": 80,
    "Swaraj": 75,
    "Sneha": 90
}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All")
    print("6. Highest Marks")
    print("7. Average")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added")

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated")
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
            print("Student deleted")
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found")

    elif choice == 5:
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == 6:
        if len(students) > 0:
            name = max(students, key=students.get)
            print("Highest:", name, students[name])

    elif choice == 7:
        if len(students) > 0:
            average = sum(students.values()) / len(students)
            print("Average:", average)

    elif choice == 8:
        break

    else:
        print("Invalid choice")