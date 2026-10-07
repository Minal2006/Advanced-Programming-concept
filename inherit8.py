class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + self.salary * 0.30


class Developer(Employee):
    def calculate_salary(self):
        return self.salary + self.salary * 0.20


class Tester(Employee):
    def calculate_salary(self):
        return self.salary + self.salary * 0.15


m = Manager(101, "Rahul", 50000)
d = Developer(102, "Amit", 40000)
t = Tester(103, "Priya", 35000)

print("Manager Salary:", m.calculate_salary())
print("Developer Salary:", d.calculate_salary())
print("Tester Salary:", t.calculate_salary())