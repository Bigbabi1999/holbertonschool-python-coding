#!/usr/bin/python3
"""Defines a Square class with size validatiomn"""

class Square:

    def__init__(self, size=0):

    """Represents a square"""

    def__init__(self, size=0):
        """
        initializes aSquare instance

        Args:
        size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
