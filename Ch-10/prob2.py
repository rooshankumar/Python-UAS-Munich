# Define a class named Calculator
class Calculator:
    # Constructor to initialize 'n'
    def __init__(self, n):
        self.n = n  # Instance attribute 'n'

    # Method to calculate and print the square of 'n'
    def square(self):
        print(f"The square of {self.n} is {self.n**2}")
    
    # Method to calculate and print the cube of 'n'
    def cube(self):
        print(f"The cube of {self.n} is {self.n**3}")
    
    # Method to calculate and print the square root of 'n'
    def square_root(self):
        print(f"The square root of {self.n} is {self.n**0.5}")

# Create an instance of Calculator with n=5
a = Calculator(5)

# Call the square method
a.square()
# Output: The square of 5 is 25

# Call the cube method
a.cube()
# Output: The cube of 5 is 125

# Call the square_root method
a.square_root()
# Output: The square root of 5 is 2.23606797749979
