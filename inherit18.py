class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease


class Surgeon(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Person.__init__(self, name, age)
        self.specialization = specialization
        self.disease = disease

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


class MedicalResearcher(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Person.__init__(self, name, age)
        self.specialization = specialization
        self.disease = disease

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


s = Surgeon("Rahul", 40, "Heart Surgery", "Heart Disease")
m = MedicalResearcher("Priya", 35, "Medical Research", "Cancer")

s.display()
m.display()