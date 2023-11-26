#!/usr/bin/python3
""" this Module is about reading a file """


def read_file(filename=""):
    """
    Method for read_file.

    Args:
        filename (str): The file name.
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
