class Person:
    def display_role(self):
        pass

class Student(Person):
    def display_role(self):
        print("Role: Student")

class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")

class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")

people = [Student(), Faculty(), Administrator()]

for p in people:
    p.display_role()