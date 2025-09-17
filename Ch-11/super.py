# Base class
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, I am {self.name} from the Parent class.")

# Derived class
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the Parent's constructor
        self.age = age          # Child-specific attribute
    
    def greet_child(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old from the Child class.")

# Create an instance of Child
c = Child("Alice", 12)

# Call methods
c.greet()       # Method from Parent
c.greet_child() # Method from Child
