#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        res += chr(ord(c) - 32) if 'a' <= c <= 'z' else c
    print("{}".format(res))
