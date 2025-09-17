# Base class
class Animal:
    def eat(self):
        print("This animal can eat food.")

# Derived class that inherits from Animal
class Mammal(Animal):
    def walk(self):
        print("This mammal can walk.")

# Another derived class that inherits from Mammal
class Dog(Mammal):
    def bark(self):
        print("This dog can bark.")

# Create an instance of Dog
d = Dog()

# Call methods from all three classes
d.eat()   # Method from Animal
d.walk()  # Method from Mammal
d.bark()  # Method from Dog
