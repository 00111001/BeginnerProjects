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
        # Catching wrong User inputs    
        else:
            print ("Wrong Input")
            continue

# Game 1 as function with normal String concatenation
def madlib1():
    color = input("Please insert a Color: ")
    animal = input("Name a Animal: ")
    house_nr = input("Please insert a House Number: ")
    lake = input("Please insert a lake: ")
    cafe = input("Please insert a Caféteria Name: ")
    city = input("Please insert your favorite City: ")

    print("One day there was a " + animal + " which was " + color)
    print("It was right in front of the House with the Number: " + house_nr + " which was located near the Lake:  " + lake)
    print("Wo es auch ein Café" + cafe + "gab")
    print("All dies ist passiert in der Stadt: " + stadt)

# Game 2 as function with format.
def madlib2():
    color = input("Please insert a Color: ")
    animal = input("Name a Animal: ")
    house_nr = input("Please insert a House Number: ")
    lake = input("Please insert a lake: ")
    cafe = input("Please insert a Caféteria Name: ")
    city = input("Please insert your favorite City: ")

    print(f"Eines tages war da ein  {tier}  wessen farbe {farbe}  war.")
    print(f"Es stand vor der Hausnummer {haus_nr} das am {see} stand.")
    print(f"Wo es auch ein Café {cafe} gab")
    print(f"All dies ist passiert in der Stadt: {stadt}")

# Starting the Game ( Calling the Main function)
if __name__ == '__main__':
    choose_game()
