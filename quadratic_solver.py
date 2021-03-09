#! /usr/bin/python3

import os
import argparse

from mylib import Equation

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("equation", type=str)
    args = parser.parse_args()

    try:
        eq = Equation(args.equation)
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(42)

    print("Reduced form:", eq)
    print("Polynomial degree:", eq.degree)