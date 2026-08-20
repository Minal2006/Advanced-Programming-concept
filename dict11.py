students = {
    "vedika": 80,
    "Gauri": 95,
    "Ishita": 88,
    "vedika": 92
}

highest = max(students, key=students.get)

print("Highest marks:", students[highest])
print("Student:", highest)