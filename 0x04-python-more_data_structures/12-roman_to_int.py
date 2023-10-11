#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    res = 0
    prev = 0

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    for symbol in roman_string[::-1]:
        if roman[symbol] >= prev:
            res += roman[symbol]
        else:
            res -= roman[symbol]
        prev = roman[symbol]

    return int(res)
