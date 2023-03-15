#!/usr/bin/python3
# a function that replaces all occurrences of an element by another in a new list.

def search_replace(my_list, search, replace):
    my_list = [1, 4, 5, "search", 7, 8]

    my_list["search"] = "replace"
    print(my_list)
