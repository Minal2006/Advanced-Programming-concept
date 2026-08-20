students = {
    "minal": "Computer",
    "Gauri": "IT",
    "shreya": "Computer",
    "dipli": "ENTC",
    "sayali": "IT"
}

departments = {}

for name, department in students.items():
    if department not in departments:
        departments[department] = []

    departments[department].append(name)

print(departments)