#!/usr/bin/python3
"""This Module has a Class Square"""


class Square:
    """
    Square Class.

    Attributes:
        size (int): the size of the square
        position (int, int): the position of sqaure as tuple
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Init methode is a constructor for Square Class.
        Args:
            size: size of the square
            position: the position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        x, y = value
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        py = self.__position[1]
        px = self.__position[0]
        if self.__size == 0:
            print()
        else:
            for i in range(py):
                print()
            for i in range(self.__size):
                print("{}{}".format(" " * px, "#" * self.__size))
