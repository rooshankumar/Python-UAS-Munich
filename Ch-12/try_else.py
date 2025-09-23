try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    # Runs only if try block succeeds (no exception)
    print(f"You entered {num}, and its square is {num**2}")
