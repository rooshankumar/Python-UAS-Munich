# Define a class named Employee
class Employee:
    # Constructor to initialize name, language, and salary for each instance
    def __init__(self, name, language, salary):
        self.name = name            # Instance attribute 'name'
        self.language = language    # Instance attribute 'language'
        self.salary = salary        # Instance attribute 'salary'
    
    # Method to display employee information
    def getInfo(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

# Create instances of Employee with specific data
emp1 = Employee("Roshan", "Python", 100000)
emp2 = Employee("Rohan", "Java", 90000)

# Call the getInfo method for each instance
emp1.getInfo()
# Output: Name: Roshan, Language: Python, Salary: 100000

emp2.getInfo()
# Output: Name: Rohan, Language: Java, Salary: 90000
