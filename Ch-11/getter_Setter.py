# Define a class
class Employee:
    def __init__(self, name, salary):
        self._name = name       # Private attribute (convention: _name)
        self._salary = salary   # Private attribute

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        self._name = value

    # Getter for salary
    @property
    def salary(self):
        return self._salary

    # Setter for salary with a condition
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative!")
        else:
            self._salary = value

# Create an instance
e = Employee("Alice", 50000)

# Access using getter
print(e.name)    # Output: Alice
print(e.salary)  # Output: 50000

# Modify using setter
e.name = "Bob"
e.salary = 60000

print(e.name)    # Output: Bob
print(e.salary)  # Output: 60000

# Try setting a negative salary
e.salary = -100
# Output: Salary cannot be negative!
