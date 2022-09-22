#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Sept 2022
# This program calculates area and perimeter of a circle with 15mm radius

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of 15mm:")
    print("\nArea is {}mm².".format(math.pi * 15**2))
    print("Perimeter is {}mm.".format(2 * math.pi * 15))

    print("\nDone.")


if __name__ == "__main__":
    main()
