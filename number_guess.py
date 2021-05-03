#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program lets the user guess a number from 1-10

import random


def main():
    # This function lets the user guess a number from 1-10

    # Input
    guessed_number = int(input("Guess a number from 1-10: "))
    random_number = random.randint(1, 10)

    # Process and Output
    if guessed_number == random_number:
        print("\nCorrect! The number was {}.".format(random_number))
    else:
        print("\nIncorrect! The number was {}.".format(random_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
