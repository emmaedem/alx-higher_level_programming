#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = "number"
if Last_digit > 5:
	print("and is greater than 5")

elif Last_digit == 0:
	print("and is 0")

elif Last_digit < 6 and Last_digit != 0:
	print("and is less than 6 and not 0")
else:
	print(f"Last digit of {number} is {number}")
