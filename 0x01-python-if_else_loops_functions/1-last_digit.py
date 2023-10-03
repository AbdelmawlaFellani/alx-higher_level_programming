#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 
greater_than_5 = "greater" if last_digit > 5 else "less"
not_zero = "not" if last_digit != 0 else "is"
print(f'Last digit of {number} is {last_digit} and is {greater_than_5} than 5 and {not_zero} 0')
