n = int(input("Enter a number : "))

for i in range(1, n+1):
    # spaces before stars
    print(" " * (n - i), end="")
    # stars: 2*i - 1 for odd numbers per row
    print("*" * (2 * i - 1))
