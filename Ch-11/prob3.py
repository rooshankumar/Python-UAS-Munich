class Employee:
    salary = 100000  # Class attribute

    def __init__(self):
        self._increment = 20  # Instance attribute with a default value

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, new_salary):
        # Calculate increment based on new salary
        self._increment = ((new_salary / self.salary) - 1) * 100

    @property
    def salaryincrement(self):
        return (self.salary * self._increment) / 100


# Create an instance of Employee
e = Employee()

# Access the initial increment
print("Initial Increment:", e.increment)  # Output: 20

# Access salary increment value
print("Salary Increment Amount:", e.salaryincrement)  # Output: 20000.0

# Set a new salary to adjust increment
e.increment = 120000  # This will recalculate increment based on new salary

# Check updated increment
print("Updated Increment:", e.increment)  # Output: 20.0
print("Updated Salary Increment Amount:", e.salaryincrement)  # Output: 20000.0
