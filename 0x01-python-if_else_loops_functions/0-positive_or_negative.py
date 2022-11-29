#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# To check if the number is negative
if number < 0:
    print(f"{number:d} is negative")

# To check if the number is zero
elif number == 0:
    print(f"{number:d} is zero")

# To check if the number is positive
else:
    print(f"{number:d} is positive")
