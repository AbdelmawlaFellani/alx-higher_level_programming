#!/usr/bin/python3
""" This module contains a function that writes to a file """


def write_file(filename="", text=""):
    """
        Method for write_file.

        Args:
            filename (str): The file name.
            text (str): The text content.

        Return: Number of Characters of @text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
