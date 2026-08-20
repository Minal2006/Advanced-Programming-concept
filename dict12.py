students = {
    "mitali": 80,
    "Shital": 95,
    "Supriya": 65,
    "radha": 92
}

lowest = min(students, key=students.get)

print("Lowest marks:", students[lowest])
print("Student:", lowest)