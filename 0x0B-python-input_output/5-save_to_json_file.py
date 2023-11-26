#!/usr/bin/python3
""" Module for save_to_json_file function """


import json


def save_to_json_file(my_obj, filename):
    """
        Method save_to_json_file.

        Args:
            my_obj (object): The object to be converted.
            filename (str): The file name.

    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
