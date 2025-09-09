# factorial(3) = 3 x 2 x 1
n = int(input("Enter a number: "))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

result = factorial(n)
print(f"The factorial of {n} is {result}")
