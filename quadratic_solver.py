#! /usr/bin/python3

import argparse
from mylib import Equation




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("equation", type=Equation)
    args = parser.parse_args()
    print(args.equation)