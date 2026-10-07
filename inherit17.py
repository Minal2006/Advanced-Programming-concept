class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal:", self.name)


class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")


d = Dog("Dog")
c = Cat("Cat")
w = Cow("Cow")

d.display()
d.sound()

c.display()
c.sound()

w.display()
w.sound()