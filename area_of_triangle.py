#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: November 2019
# This program calculates area of tiangle


def area_of_triangle(base, height):
    # calculates are of triangle
    area = (base * height)/2

    print("The area of the triangle {0}cm^2".format(area))


def main():
    # asks for inputs and calls other functions
    while True:

        base_from_user = input("Enter the base of the triangle (cm): ")
        height_from_user = input("Enter the height of the triangle (cm): ")

        try:
            base_from_user_number = int(base_from_user)
            height_from_user_number = int(height_from_user)

            area_of_triangle(base_from_user_number, height_from_user_number)
            break

        except(ValueError):
            print("Not a valid number inputted")


if __name__ == "__main__":
    main()
