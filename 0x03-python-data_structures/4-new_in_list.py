#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list.copy()
    if 0 < idx <= len(cpy_list):
        cpy_list[idx] = element
    return cpy_list
