# Define a class named Employee
class Employee:
    language = "Python"   # Class attribute shared by all instances
    salary = 100000       # Class attribute shared by all instances

    # Define a method that prints information about the employee
    def getInfo(self):   # 'self' parameter is required to access instance and class attributes
        print(f"The language is {self.language} and the salary is {self.salary}")

    # Define a static method that does not require 'self'
    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

# Create another instance of Employee named Rohan
Rohan = Employee()

# Override the 'language' attribute only for this instance
Rohan.language = "JAVA"

# Print Rohan's language (overridden value at instance level)
print(Rohan.language)
# Output: JAVA

# Call the static method greet, which does not use 'self'
Rohan.greet()

# Call the getInfo method, which uses 'self' to access the correct attributes
Rohan.getInfo()

# Output: The language is JAVA and the salary is 100000
