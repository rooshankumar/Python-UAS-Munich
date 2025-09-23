try:
    a = int(input("Hey, enter a number: "))

except ValueError:
    # Raised if input cannot be converted into an int
    print("That's not a valid number!")
    a = None   # fallback value if conversion fails

except Exception as e:
    # Catches all other exceptions (e.g., KeyboardInterrupt, unexpected errors)
    print("Something went wrong:", e)
    a = None   # fallback value if conversion fails

print(a)
print("Continuing with the rest of the program...")