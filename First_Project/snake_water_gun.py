import random

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def get_user_choice():
    choice = input("Enter your choice (snake, water, gun): ").lower()
    while choice not in ['snake', 'water', 'gun']:
        print("Invalid choice. Please choose 'snake', 'water', or 'gun'.")
        choice = input("Enter your choice (snake, water, gun): ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    if (user == 'snake' and computer == 'water') or \
       (user == 'water' and computer == 'gun') or \
       (user == 'gun' and computer == 'snake'):
        return "user"
    else:
        return "computer"

def play():
    rounds = int(input("Enter number of rounds you want to play: "))
    user_score = 0
    computer_score = 0

    for i in range(1, rounds + 1):
        print(f"\nRound {i}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a draw!")

    print("\nFinal Results:")
    print(f"Your Score: {user_score}")
    print(f"Computer's Score: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > user_score:
        print("Computer wins the game. Better luck next time!")
    else:
        print("The game is a draw!")

if __name__ == "__main__":
    print("Welcome to Snake-Water-Gun Game!")
    play()
