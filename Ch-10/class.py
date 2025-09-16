# Define a class named Employee
class Employee:
    language = "Python"   # Class attribute shared by all instances
    salary = 100000       # Class attribute shared by all instances
    height = 5.9          # Class attribute shared by all instances
    weight = 75           # Class attribute shared by all instances

# Create an instance of Employee named Roshan
Roshan = Employee()
# Access the class attributes using the instance and print them
print(Roshan.language, Roshan.salary, Roshan.height, Roshan.weight)
# Output: Python 100000 5.9 75

# Create another instance of Employee named Rohan
Rohan = Employee()
# Add a new instance attribute 'name' only to Rohan
Rohan.name = "Rohan"
# Print Rohan's name and weight (weight is a class attribute still accessible)
print(Rohan.name, Rohan.weight)
# Output: Rohan 75

# Create a third instance of Employee named Priya
Priya = Employee()
# Add a new instance attribute 'name' only to Priya
Priya.name = "Priya"
# Print Priya's name and salary (salary is a class attribute still accessible)
print(Priya.name, Priya.salary)
# Output: Priya 100000
