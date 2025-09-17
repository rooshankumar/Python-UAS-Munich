# Define a base class 'employee'
class employee:
    company = "Google"  # Class attribute shared by all employee objects

    # Instance method to show name and salary (will be used if attributes are set)
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# Define a derived class 'programmer' that inherits from 'employee'
class programmer(employee):
    company = "YouTube"  # Class attribute overridden in programmer class

    # Instance method to show name and programming language
    def showlang(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

# Create an object 'a' of the base class 'employee'
a = employee()

# Create an object 'b' of the derived class 'programmer'
b = programmer()

# Print the 'company' attribute for both objects
print(a.company, b.company)
# Output: Google YouTube
