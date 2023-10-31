#!/usr/bin/python3

"""
    This module contains a function that adds 2 integers.
        (int) a: the first integer.
        (int) b: the second integer with default value of 98.
"""


def add_integer(a, b=98):
    """
        This function adds 2 integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
