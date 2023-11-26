#!/usr/bin/python3
""" Module for from_json_string function """


import json


def from_json_string(my_str):
    """
        Method for from_json_string

        Args:
            my_str (str): The string provided

        Return:
            object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
