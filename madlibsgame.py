# -----------------------------------------------
# Author: Nick V.
# Mad Libs Game
# Version: 1.0
# creation date: 29.03.2022
# -----------------------------------------------


# importing sys for closing programm with "0".
import sys


# Basically a Menu in a function
def choose_game():
    # Endless loop
    while True:
        # Menu outprint.
        print("""(1) Madlib Game 1
(2) Madlib Game 2
(0) Exit""")
        # Input for the Gameoption choices
        game_choice = input("Which Option do you wanna choose: ")
        
        
        # Entering Madlib Game 1 
        if game_choice == "1":
            madlib1()
        # Entering Madlib Game 2
        elif game_choice == "2":
            madlib2()
        # Option to exit the Pgm
        elif game_choice == "0":
            # Function to end the Game
            sys.exit()
        else:
            print ("Falsche Eingabe")
            continue

# Game 1 as function with normal String concatenation
def madlib1():
    farbe = input("Geben Sie eine Farbe ein: ")
    tier = input("Geben Sie eine Tier ein: ")
    haus_nr = input("Geben Sie eine Haus ein: ")
    see = input("Geben Sie eine See ein: ")
    cafe = input("Geben Sie eine Café ein: ")
    stadt = input("Geben Sie eine Stadt ein: ")

    print("Eines tages war da ein" + tier + " wessen farbe " + farbe + "war.")
    print("Es stand vor der Hausnummer " + haus_nr + " das am  " + see + "stand.")
    print("Wo es auch ein Café" + cafe + "gab")
    print("All dies ist passiert in der Stadt: " + stadt)

# Game 2 as function with format.
def madlib2():
    farbe = input("Geben Sie eine Farbe ein: ")
    tier = input("Geben Sie eine Tier ein: ")
    haus_nr = input("Geben Sie eine Haus ein: ")
    see = input("Geben Sie eine See ein: ")
    cafe = input("Geben Sie eine Café ein: ")
    stadt = input("Geben Sie eine Stadt ein: ")

    print(f"Eines tages war da ein  {tier}  wessen farbe {farbe}  war.")
    print(f"Es stand vor der Hausnummer {haus_nr} das am {see} stand.")
    print(f"Wo es auch ein Café {cafe} gab")
    print(f"All dies ist passiert in der Stadt: {stadt}")

# Starting the Game ( Calling the Main function)
if __name__ == '__main__':
    choose_game()
