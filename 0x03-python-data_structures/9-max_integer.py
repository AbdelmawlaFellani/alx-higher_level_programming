#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = None
    if my_list:
        max_val = my_list[0]
        for elm in my_list:
            if elm >= max_val:
                max_val = elm
    return max_val
