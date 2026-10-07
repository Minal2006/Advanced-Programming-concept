class Shape:
    def display(self):
        print("Shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().display()

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())