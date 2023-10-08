#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for c in my_string:
        if c not in 'Cc':
            new_str += c
    return new_str
