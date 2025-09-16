# Define a class named Calculator
class Calculator:
    # Constructor to initialize 'n'
    def __init__(self, n):
        self.n = n  # Instance attribute 'n'

    # Instance method to calculate and print the square of 'n'
    def square(self):
        print(f"The square of {self.n} is {self.n**2}")
    
    # Instance method to calculate and print the cube of 'n'
    def cube(self):
        print(f"The cube of {self.n} is {self.n**3}")
    
    # Instance method to calculate and print the square root of 'n'
    def square_root(self):
        print(f"The square root of {self.n} is {self.n**0.5}")

    # Static method to greet users
    @staticmethod
    def greet():
        print("Hello! Welcome to the Calculator program.")

# Create an instance of Calculator with n=5
a = Calculator(5)

# Call the static method 'greet' using the class name
Calculator.greet()  # Output: Hello! Welcome to the Calculator program.

# Call instance methods using the object 'a'
a.square()
# Output: The square of 5 is 25

Calculator.greet()  # Can be called again using the class name
# Output: Hello! Welcome to the Calculator program.

a.cube()
# Output: The cube of 5 is 125

Calculator.greet()  # Can be called again using the class name
# Output: Hello! Welcome to the Calculator program.

a.square_root()
# Output: The square root of 5 is 2.23606797749979
