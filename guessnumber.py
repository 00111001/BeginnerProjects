# -----------------------------------------------
# Author: Nick V.
# Number guessing Game
# Version: 1.0
# creation date: 29.03.2022
# -----------------------------------------------

# To get random integers
from random import randint

# Referencing our random integer with a var to access
random_number = randint(0, 10)


# The Game
def main():
    # Initializing a Counter Var for the Try's
    counter = 0
    # Initializing a Number Var  to work with the Var
    number = 0

    # Loop during number == random_number
    while number != random_number:
        # Creating a Input referenced to Number.
        # Converting it to int to let it match with the random integer func
        number = int(input("Please insert your Number: "))
        # Add every try to the initialized counter var +1
        counter = counter + 1
        # If clause for the last try.
        # Without it , it would print on the Right answer "Wrong number" aswell.
        if number != random_number:
            print("Wrong Number")

    # Printing our Result
    print(f"The number was {random_number} and you did {counter} inputs")


# Calling our main function
if __name__ == '__main__':
    main()
