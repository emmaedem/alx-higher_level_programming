#!/usr/bin/python3
# a function that prints the last digit of a number.

def print_last_digit(number):

    if number < 0:

        print("{}".format((number * (-1)) % 10), end='')

        return (number * (-1)) % 10

    else:

        print("{}".format(number % 10), end='')

        return number % 10
