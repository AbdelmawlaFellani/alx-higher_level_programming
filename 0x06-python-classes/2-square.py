#!/usr/bin/python3
"""this module defines a class Square"""


class Square:
    """Class to represent a square object.

    Attributes:
        size (int): The length of one side of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square object."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
