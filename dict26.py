employees = {
    "ravi": 45000,
    "megha": 60000,
    "Sneha": 75000,
    "riya": 40000
}

highest = max(employees, key=employees.get)
lowest = min(employees, key=employees.get)

average = sum(employees.values()) / len(employees)

print("Highest salary:", highest, employees[highest])
print("Lowest salary:", lowest, employees[lowest])
print("Average salary:", average)

print("Employees earning more than 50000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)