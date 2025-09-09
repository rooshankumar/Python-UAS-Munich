def greet(name, message="Have a nice day!"):
    """Greets the user with a message."""
    print(f"Hello, {name}! {message}")

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def multiply(x, y=2):
    """Returns the product of two numbers, default second is 2."""
    return x * y

def describe_person(name, age, **kwargs):
    """Describes a person with additional optional information."""
    print(f"{name} is {age} years old.")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def total(*numbers):
    """Calculates the sum of an arbitrary number of numbers."""
    return sum(numbers)


# Using functions with required arguments
greet("Roshan")

# Using default argument
greet("Sonia", "Welcome to the team!")

# Using return value
sum_result = add(5, 10)
print(f"Sum: {sum_result}")

# Using default and provided argument
product1 = multiply(4)
product2 = multiply(4, 5)
print(f"Product with default exponent: {product1}")
print(f"Product with provided exponent: {product2}")

# Using keyword arguments
describe_person("Amit", 25, city="Patna", hobby="Reading")

# Using arbitrary number of arguments
print(f"Total sum: {total(1, 2, 3, 4, 5)}")
