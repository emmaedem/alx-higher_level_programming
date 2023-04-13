#!/usr/bin/python
"""Defines a text file reading function"""

def read_file(filename=""):

    """"Reads text file and print it to stdout"""

    with open(filename, 'r', encoding="utf-8") as f:

            print(f.read(), end="")
