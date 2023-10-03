#!/usr/bin/python3
def print_last_digit(number):
    abs_n = number % 10 if number > 0 else abs(number % -10)
    print(abs_n, end="")
    return abs_n
