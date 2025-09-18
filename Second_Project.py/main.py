import random

# Generate a random number between 1 and 100
n = random.randint(1, 100)

a = -1      # Start with an invalid guess
guess = 0   # Counter for number of attempts

# Keep looping until user guesses correctly
while a != n:
    # Ask user for input
    a = int(input("Enter your guess: "))
    guess += 1   # Increment attempt count

    # Check conditions
    if a < n:
        print("Too low!")   # If guess is smaller
    elif a > n:
        print("Too high!")  # If guess is larger
    else:
        print(f"Congratulations! You've guessed the number {n} in {guess} attempts.")

print("Game Over")
