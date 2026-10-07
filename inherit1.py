class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee ID:",self.empid)
        print("Name:",self.name)
        print("Salary:",self.salary)
class Manager(Employee):
    def __init__(self,empid,name,salary,dept):
        super().__init__(empid,name,salary)
        self.dept=dept
    def display(self):
        super().display()
        print("Department:",self.dept)
        print("Annual salary:",self.salary)
m=Manager(16,"Shreya",90000,"HR")
m.display()
