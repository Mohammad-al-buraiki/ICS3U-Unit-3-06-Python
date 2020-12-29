# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is Number Guessing Game

import random

pyguess = random.randint(1, 10)


def main():
    # this function asks the user to guess the right integer number
    # also this function check the input data

    # input
    guessing = input("Guess the right number between 1-10: ")
    print("")

    # process
    try:
        guessing_as_number = int(guessing)
        if guessing == pyguess:
            print("You got it right 😃, the number was {}".format(pyguess))
        else:
            print("You got it wrong 😞, the number was {}".format(pyguess))
            print("Try again ...")
    except Exception:
        print("This was not an integer")
    


if __name__ == "__main__":
    main()
