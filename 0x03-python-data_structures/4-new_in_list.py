#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 < idx < len(my_list):
        cpy_list = my_list[:]
        cpy_list[idx] = element
        return cpy_list
    else:
        return my_list.copy()
