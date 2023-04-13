#!/usr/bin/python

def read_file(filename=""):
    """"Reads text file and print it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
