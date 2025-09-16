# Define a class named Programmer
class Programmer:
    company = "Microsoft"  # Class attribute shared by all instances

    # Constructor to initialize name, salary, and pincode for each instance
    def __init__(self, name, salary, pincode):
        self.name = name        # Instance attribute 'name'
        self.salary = salary    # Instance attribute 'salary'
        self.pincode = pincode  # Instance attribute 'pincode'

# Create an instance 'p' of Programmer with name "Rohit"
p = Programmer("Rohit", 100000, 411057)
print(p.company, p.name, p.salary, p.pincode)
# Output: Microsoft Rohit 100000 411057

# Create another instance 'p' with name "John"
p = Programmer("John", 100000, 411057)
print(p.company, p.name, p.salary, p.pincode)
# Output: Microsoft John 100000 411057

# Create another instance 'p' with name "Kick"
p = Programmer("Kick", 100000, 411057)
print(p.company, p.name, p.salary, p.pincode)
# Output: Microsoft Kick 100000 411057
