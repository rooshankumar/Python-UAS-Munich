# Define a class named Demo
class Demo:
    a = 4  # Class attribute 'a' shared by all instances unless overridden

# Create an instance of Demo named 'o'
o = Demo()

# Override the attribute 'a' for this particular instance 'o'
o.a = 5  # Now 'a' is an instance attribute for 'o', separate from the class attribute

# Print the value of 'a' for the instance 'o'
print(o.a)  # Output: 5 -> because instance attribute 'a' is 5 for 'o'

# Print the value of 'a' for the class Demo
print(Demo.a)  # Output: 4 -> because the class attribute 'a' remains unchanged
