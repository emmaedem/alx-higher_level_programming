#!/usr/bin/python3

"""Define a locked class."""

class LockedClass:

    """
    Prevent user from instantiating new LockedClass attributes
    for attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
