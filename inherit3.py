class Academic:
    def __init__(self,marks):
        self.marks=marks
class Sports:
    def __init__(self,points):
        self.points=points
class Student(Academic,Sports):
    def __init__(self,name,marks,points):
        Academic.__init__(self,marks)
        Sports.__init__(self,points)
        self.name=name
    def performance(self):
        total=self.marks+self.points
        print("Name:",self.name)
        print("Marks:",self.marks)
        print("Sport points:",self.points)
        print("Total:",total)
s=Student("Shreya",89,8)
s.performance()