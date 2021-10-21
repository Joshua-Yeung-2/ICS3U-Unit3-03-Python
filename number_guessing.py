# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on September 2021
# This program is a number guessing game.

import random


def main():
    # this function is to guessing the number
    # a number between 1 and 100
    some_variable = random.randint(1, 100)

    # input
    user_input = int(input("Enter a random number from 1 to 100 here: "))
    print("")

    # process
    if user_input == some_variable:
        # output
        print("congratulations!")
        print("you got it right")

    else:
        print("oops! you got it wrong")
        print("try again")
        
    print("the answer is {}".format(some_variable))
    
    print("\ndone")


if __name__ == "__main__":
    main()
