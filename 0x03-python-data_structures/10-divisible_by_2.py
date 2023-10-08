#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    arr = []
    for el in my_list:
        arr.append(True if el % 2 == 0 else False)
    return arr
