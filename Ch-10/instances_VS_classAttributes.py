# Define a class named Employee
class Employee:
    language = "Python"   # Class attribute shared by all instances
    salary = 100000       # Class attribute shared by all instances
    height = 5.9          # Class attribute shared by all instances
    weight = 75           # Class attribute shared by all instances

# Create another instance of Employee named Rohan
Rohan = Employee()
# Add a new instance attribute 'name' only to Rohan
Rohan.language = "JAVA"
# Print Rohan's name and weight (weight is a class attribute still accessible)
print(Rohan.language)
# Output: JAVA