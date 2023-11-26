#!/usr/bin/python3
""" this Module is about Append a string to a file """


def append_write(filename="", text=""):
    """
    Method for append_write.

    Args:
        filename (str): The file name.
        text (str): The text Content.

    Return: Number of characters of the text Content.
    """
    with open(filename, 'a', encoding="utf-8") as myFile:
        return (myFile.write(text))
