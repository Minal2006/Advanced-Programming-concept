# Store employee ID, name, department, and salary in a file. Write functions to: 
# Display all employees. 
# Find the highest-paid employee. 
# Calculate average salary. 
# Display employees earning above a given salary.

file = open("employee.txt", "w")

file.write("101,Amit,HR,35000\n")
file.write("102,Priya,IT,55000\n")
file.write("103,Rahul,Sales,42000\n")
file.write("104,Neha,IT,65000\n")

file.close()


def read_employees():
    file = open("employee.txt", "r")
    employees = []

    for line in file:
        data = line.strip().split(",")

        emp_id = data[0]
        name = data[1]
        department = data[2]
        salary = int(data[3])

        employees.append([emp_id, name, department, salary])

    file.close()
    return employees


def display_all():
    employees = read_employees()

    print("All Employee Records:")
    for emp in employees:
        print("ID:", emp[0],
              "Name:", emp[1],
              "Department:", emp[2],
              "Salary:", emp[3])


def highest_paid():
    employees = read_employees()

    highest = employees[0]

    for emp in employees:
        if emp[3] > highest[3]:
            highest = emp

    print("\nHighest-Paid Employee:")
    print("ID:", highest[0])
    print("Name:", highest[1])
    print("Department:", highest[2])
    print("Salary:", highest[3])



def average_salary():
    employees = read_employees()

    total = 0

    for emp in employees:
        total = total + emp[3]

    average = total / len(employees)

    print("\nAverage Salary:", average)



def above_salary():
    employees = read_employees()

    salary_limit = int(input("\nEnter salary limit: "))

    print("Employees earning above", salary_limit, ":")

    for emp in employees:
        if emp[3] > salary_limit:
            print("ID:", emp[0],
                  "Name:", emp[1],
                  "Department:", emp[2],
                  "Salary:", emp[3])



display_all()
highest_paid()
average_salary()
above_salary()