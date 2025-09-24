from functools import reduce

l = [1,2,3,4,5,6,7,8,9]

# Map example
squared = lambda x: x*x
sqList = map(squared, l)
print("Squares:", list(sqList))

# Filter example
def even(n):
    return n % 2 == 0
    
evenList = filter(even, l)
print("Evens:", list(evenList))

# Reduce example (sum)
def add(a, b):
    return a + b

# Reduce example (product using lambda)
mul = lambda a, b: a * b

print("Multiply two numbers (5,10):", mul(5, 10))
print("Sum using reduce:", reduce(add, l))
print("Product using reduce:", reduce(mul, l))
