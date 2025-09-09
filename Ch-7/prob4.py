num = int(input("Enter a number : "))

for i in range(2, num):
    if num % i == 0:
        print("Not a prime number.")
        break
else:
    # This else belongs to the for-loop, runs only if loop was not broken
    print("Yes it is a prime number.")

print("End of Program.")
