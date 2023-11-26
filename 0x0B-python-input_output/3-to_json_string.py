#!/usr/bin/python3
""" Module contains function JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """
    Convert the given object to its JSON representation.

    Args:
        my_obj (object): The object to be converted.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
