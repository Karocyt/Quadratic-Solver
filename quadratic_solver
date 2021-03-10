#! /usr/bin/python3

import os
import argparse

from mylib import Equation
from mylib.exceptions import CustomError

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("equation", help="an equation in the form \"1 + X + 14 * X^2 = x^1\"", type=str)
    parser.add_argument("-v", "--verbose", help="show intermediate steps", action="store_true")
    args = parser.parse_args()

    try:
        eq = Equation(args.equation)
    except CustomError as e:
        print(f"Error: {str(e)}")
        exit(42)

    print("Reduced form:", eq)
    print("Polynomial degree:", eq.degree)

    eq.solve(args.verbose)