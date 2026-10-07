class Student:
    def calculate_grade(self, marks):
        pass

class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"

class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 65:
            return "B"
        else:
            return "C"

class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 70:
            return "A"
        elif marks >= 55:
            return "B"
        else:
            return "C"

students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for s in students:
    print(s.calculate_grade(75))