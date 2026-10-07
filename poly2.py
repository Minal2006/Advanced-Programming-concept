class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 15000

class Developer(Employee):
    def calculate_salary(self):
        return 40000 + 10000

class Tester(Employee):
    def calculate_salary(self):
        return 35000 + 7000

employees = [Manager(), Developer(), Tester()]

for e in employees:
    print("Salary:", e.calculate_salary())