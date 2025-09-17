# Base class
class Animals:
    pass

# Pets class inherits from Animals
class Pets(Animals):
    pass

# Dogs class inherits from Pets
class Dogs(Pets):
    @staticmethod
    def bark(self):  # Static method defined with 'self' unnecessarily
        print("Woof! Woof!")

# Create an instance of Dogs
d = Dogs()

# Call the static method by passing the instance as argument
d.bark(d)  # Output: Woof! Woof!
