#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: February 28, 2025
# This program asks the user for a radius and then calculates the circumference of a circle using tau
import constants


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()