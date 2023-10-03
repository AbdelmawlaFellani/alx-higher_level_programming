#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 0 else number % -10
greater = "greater than 5" if last_digit > 5 else "less than 6"
not_zero = "not" if last_digit != 0 else "is"
print(f'Last digit of {number} is {last_digit} and is {greater} and {not_zero} 0')
