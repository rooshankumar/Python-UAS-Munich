import random
import os

def game():
    print("You are inside the game")
    score = random.randint(1, 1000)
    filename = "Ch-9/gamescores.txt"

    # Ensure the file exists before reading
    if os.path.exists(filename):
        with open(filename, "r") as f:
            gamescore = f.read()
            if gamescore.strip() != "":
                gamescore = int(gamescore)
            else:
                gamescore = 0
    else:
        gamescore = 0

    print("Your score is", score)

    if score > gamescore:
        print("You have the highest score!")
        with open(filename, "w") as f:
            f.write(str(score))
    else:
        print("You don't have the highest score. Highest score is", gamescore)

    return score

game()
