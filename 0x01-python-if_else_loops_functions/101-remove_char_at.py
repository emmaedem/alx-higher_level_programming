#!/usr/bin/python3
# a function that creates a copy of the string,
# removing the character at the position n

def remove_char_at(str, n):

    if n >= 0:

        return str[0:n] + str[n + 1:]

    return str
