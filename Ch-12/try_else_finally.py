try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"Double of {num} is {num*2}")
finally:
    print("This always runs (cleanup code).")
