#!/usr/bin/python3
# a function that replaces an element of a list at a specific position (like in C)

def replace_in_list(my_list, idx, element):

    if idx >= 0 and idx < len(my_list):

        my_list[idx] = element

        print("my_list")
    
