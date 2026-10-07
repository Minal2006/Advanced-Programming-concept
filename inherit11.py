class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def calculate(self):
        total = sum(self.marks)
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


r = Result(101, "Rahul", "BCA", [80, 85, 90])
r.calculate()