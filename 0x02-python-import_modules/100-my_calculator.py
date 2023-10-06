#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
if __name__ = "__main__":
    from sys import argv, exit

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))
