# -----------------------------------------------
# Author: Nick V.
# Roll a Dice
# Version: 1.0
# creation date: 29.03.2022
# -----------------------------------------------

# To get random integers
from random import randint

# Main Function and the Game
def roll_dice():
    # Endless Loop for the Game 
    while True:
        # Referencing the randint from random to the Var "dice" to access it.
        dice = randint(1, 6)
        # Simply a print to give feedback to the User
        print(f"You rolled the Dice and got: {dice}")
        # Check if User wants to roll again.
        again = input("Do you want to go again and roll a dice? (0) Exit, (1) Yes: ")
        # Small Chec for options
        if again == "0":
            # Breaking out of the Loop (Exiting Program)
            break
        # Small Chec for options
        if again == "1":
            # Continiung with the Loop
            continue


# Calling main Function
if __name__ == '__main__':
    roll_dice()


