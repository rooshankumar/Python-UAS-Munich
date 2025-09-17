# Define a class
class Employee:
    company = "Google"  # Class attribute

    # Class method to show company info
    @classmethod
    def show_company(cls):
        print(f"The company is {cls.company}")

# Call the class method using the class name
Employee.show_company()  
# Output: The company is Google

# Create an instance
e = Employee()
e.show_company()  # Can also call via instance
# Output: The company is Google
