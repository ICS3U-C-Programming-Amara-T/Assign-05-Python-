#!/usr/bin/env python3

# Created By: Amara Tie

# Date: May 22, 2025

# This is a program calculates energy!

import constants
import math


def energy(mass_float):
    # Calculate the energy
    return mass_float * math.pow(constants.C, 2)


def mass2(energy2_float):
    # Calculate the mass
    return energy2_float / math.pow(constants.C, 2)


def main():
    # Greeting
    print("Hello! Let's find energy using Einstein's equation!")
    # Check if mass is a positive number
    while True:
        mass = input("Enter mass: ")
        try:
            mass_float = float(mass)
            if mass_float < 0:
                print("Mass must be positive. Try again.")
                continue

            # Ask for units, check if units are kg
            while True:
                unit = input("Enter unit: ")
                if unit == "kg":
                    break
                else:
                    print("Invalid unit! In Physics, we measure mass in kg.")
                    continue
            break
        except Exception:
            print("That was not a number.")

    # Call the function
    answer = energy(mass_float)

    # Display the energy
    print("Energy = {} (J)".format(answer))

    # Ask if user wants to calculate mass
    print("Would you like to calculate your mass? (Yes or No)")
    choice = input()

    if choice == "Yes":
        # Display new rearranged formula
        print("Your new formula is m = E/c^2")
        # User enters energy
        energy2 = input("Please enter your Energy (J): ")

        try:
            energy2_float = float(energy2)
            # Call function
            answer2 = mass2(energy2_float)
            print("mass = {} (kg) ".format(answer2))
        except Exception:
            print("That was not a number.")
    elif choice == "No":
        print("Alright, Thanks for playing!")
    else:
        print("Invalid Input. Enter Yes or No!")


if __name__ == "__main__":
    main()
