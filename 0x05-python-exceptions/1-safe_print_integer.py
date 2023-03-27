#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))

        print()  # print a new line after the integer

        return True

    except:

        return False
