class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar(Car):
    def display(self):
        print("Sports Car:", self.brand, self.model)


class ElectricBike(Bike):
    def display(self):
        print("Electric Bike:", self.brand, self.model)


s = SportsCar("BMW", "M4")
e = ElectricBike("Ather", "450X")

s.display()
e.display()